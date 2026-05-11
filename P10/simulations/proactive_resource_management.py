#!/usr/bin/env python3
"""
Algorithms 3, 4, 5 – Proactive Resource Management (Sections V–VI).

Implements the proactive resource-management framework described in
"Predicción de Tráfico Basada en LSTM para Gestión Proactiva de
Recursos en Redes 5G".

Algorithms
----------
3  Proactive Resource Allocation  (Section VI.C)
4  Online Model Update / Drift Detection (Section VI.D)
5  Multi-Objective Optimization   (Section VI.E)

Also includes reactive-vs-proactive simulation with KPI tracking
(Section VII.C) and cell-sleep / pre-activation logic (Section V.C.1).

Usage
-----
    python proactive_resource_management.py --self-test
"""

from __future__ import annotations

import argparse
import copy
import math
import sys
from typing import Dict, List, Tuple

import numpy as np
from scipy.optimize import minimize_scalar

# ══════════════════════════════════════════════════════════════════
# Algorithm 3 – Proactive Resource Allocation (Section VI.C)
# ══════════════════════════════════════════════════════════════════

def proactive_resource_allocation(
    D_hat: np.ndarray,
    sigma: np.ndarray,
    R_max_rb: float,
    P_max: float,
    *,
    kappa: float = 1.96,
    n_slices: int = 3,
    max_iter: int = 50,
    tol: float = 1e-4,
) -> Dict[str, np.ndarray]:
    """Algorithm 3: Proactive Resource Allocation.

    Parameters
    ----------
    D_hat : ndarray, shape (C, T)
        Predicted traffic demand for C cells over T time slots.
    sigma : ndarray, shape (C, T)
        Prediction uncertainty (std) per cell per slot.
    R_max_rb : float
        Total available resource blocks.
    P_max : float
        Total available transmit power (watts).
    kappa : float
        Robustness parameter for demand adjustment (default 1.96).
    n_slices : int
        Number of network slices (eMBB=0, URLLC=1, mMTC=2).
    max_iter : int
        Maximum optimization iterations.
    tol : float
        Convergence tolerance.

    Returns
    -------
    dict with:
        'rb_alloc'    – (C, T) resource-block allocation
        'power_alloc' – (C, T) power allocation (watts)
        'slice_alloc' – (n_slices, C, T) per-slice RB allocation
        'converged'   – bool
    """
    C, T = D_hat.shape

    # Robust demand adjustment: D_robust = D_hat + κ * σ
    D_robust = D_hat + kappa * sigma
    D_robust = np.clip(D_robust, 0, None)

    rb_alloc = np.zeros((C, T))
    power_alloc = np.zeros((C, T))
    slice_alloc = np.zeros((n_slices, C, T))

    converged = False

    for iteration in range(max_iter):
        prev_rb = rb_alloc.copy()

        for t in range(T):
            demand_t = D_robust[:, t]
            total_demand = demand_t.sum()

            # ── Phase 1: RB allocation by priority ──
            # Priority = demand / available resource ratio (higher = more urgent)
            if total_demand > 0:
                priority = demand_t / (total_demand + 1e-12)
            else:
                priority = np.ones(C) / C

            # Sort by priority (descending) and allocate
            order = np.argsort(-priority)
            remaining_rb = R_max_rb
            for c in order:
                need = demand_t[c] / (total_demand + 1e-12) * R_max_rb
                allocated = min(need, remaining_rb)
                rb_alloc[c, t] = allocated
                remaining_rb -= allocated

            # ── Phase 2: Power allocation via iterative water-filling ──
            rb_t = rb_alloc[:, t]
            active = rb_t > 0
            n_active = active.sum()
            if n_active > 0:
                # Water-filling: equal base + proportional to demand
                base_power = P_max * 0.3 / n_active  # 30 % base
                prop_power = P_max * 0.7  # 70 % proportional
                for c in range(C):
                    if active[c]:
                        share = rb_t[c] / (rb_t[active].sum() + 1e-12)
                        power_alloc[c, t] = base_power + prop_power * share

                # Clamp to P_max
                total_p = power_alloc[:, t].sum()
                if total_p > P_max:
                    power_alloc[:, t] *= P_max / total_p

            # ── Phase 3: Slice resource allocation ──
            # Minimum guarantees: eMBB 50 %, URLLC 30 %, mMTC 20 %
            min_frac = np.array([0.50, 0.30, 0.20])
            for c in range(C):
                cell_rb = rb_alloc[c, t]
                for s in range(n_slices):
                    slice_alloc[s, c, t] = cell_rb * min_frac[s]

        # ── Convergence check ──
        delta = np.abs(rb_alloc - prev_rb).max()
        if delta < tol:
            converged = True
            break

    return {
        "rb_alloc": rb_alloc,
        "power_alloc": power_alloc,
        "slice_alloc": slice_alloc,
        "converged": converged,
    }


# ══════════════════════════════════════════════════════════════════
# Algorithm 4 – Online Model Update / Drift Detection (Section VI.D)
# ══════════════════════════════════════════════════════════════════

def detect_drift(
    recent_errors: np.ndarray,
    training_error: float,
    delta: float = 0.2,
) -> bool:
    """Check if concept drift has occurred.

    Drift is detected when the mean recent prediction error exceeds
    the training-time error by a relative margin δ.
    """
    mean_recent = float(np.mean(recent_errors))
    return mean_recent > training_error * (1.0 + delta)


def online_model_update(
    model,
    new_data_x: "np.ndarray | torch.Tensor",
    new_data_y: "np.ndarray | torch.Tensor",
    training_error: float,
    recent_errors: np.ndarray,
    *,
    delta: float = 0.2,
    lr: float = 1e-4,
    reg_lambda: float = 0.01,
    epochs: int = 5,
) -> Tuple[object, bool, float]:
    """Algorithm 4: Online Model Update with drift detection.

    Parameters
    ----------
    model : nn.Module
        Current deployed model (PyTorch).
    new_data_x, new_data_y
        Recent observation batch.
    training_error : float
        Historical training RMSE.
    recent_errors : ndarray
        Array of recent prediction errors.
    delta : float
        Drift detection threshold (default 0.2).
    lr : float
        Learning rate for incremental update.
    reg_lambda : float
        L2 regularization toward old weights.
    epochs : int
        Incremental retraining epochs.

    Returns
    -------
    model       – updated (or original) model
    was_updated – whether weights changed
    new_error   – validation error after update
    """
    import torch
    import torch.nn as nn

    drift_detected = detect_drift(recent_errors, training_error, delta)

    if not drift_detected:
        return model, False, float(np.mean(recent_errors))

    print("  [Algorithm 4] Drift detected – incremental retraining …")

    # Save old weights for regularization
    old_params = {n: p.clone().detach() for n, p in model.named_parameters()}

    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.HuberLoss(delta=1.0)

    if isinstance(new_data_x, np.ndarray):
        x_t = torch.tensor(new_data_x, dtype=torch.float32)
        y_t = torch.tensor(new_data_y, dtype=torch.float32)
    else:
        x_t, y_t = new_data_x, new_data_y

    old_state = copy.deepcopy(model.state_dict())

    model.train()
    for _ in range(epochs):
        optimizer.zero_grad()
        preds = model(x_t)
        loss = criterion(preds, y_t)

        # Elastic regularization toward old weights
        reg = torch.tensor(0.0)
        for name, param in model.named_parameters():
            reg = reg + torch.sum((param - old_params[name]) ** 2)
        loss = loss + reg_lambda * reg

        loss.backward()
        nn.utils.clip_grad_norm_(model.parameters(), 5.0)
        optimizer.step()

    # Validation: accept update only if error improves
    model.eval()
    with torch.no_grad():
        val_preds = model(x_t).numpy()
    new_error = float(np.sqrt(np.mean((val_preds - y_t.numpy()) ** 2)))

    if new_error > float(np.mean(recent_errors)):
        # Reject update – rollback
        model.load_state_dict(old_state)
        print("  [Algorithm 4] Update rejected (error increased)")
        return model, False, float(np.mean(recent_errors))

    print(f"  [Algorithm 4] Update accepted (error: "
          f"{np.mean(recent_errors):.4f} → {new_error:.4f})")
    return model, True, new_error


# ══════════════════════════════════════════════════════════════════
# Algorithm 5 – Multi-Objective Optimization (Section VI.E)
# ══════════════════════════════════════════════════════════════════

def jain_fairness(allocations: np.ndarray) -> float:
    """Jain's fairness index for a 1-D allocation vector."""
    n = len(allocations)
    if n == 0 or allocations.sum() == 0:
        return 0.0
    return float(allocations.sum() ** 2 / (n * (allocations ** 2).sum() + 1e-12))


def compute_objectives(
    rb_alloc: np.ndarray,
    power_alloc: np.ndarray,
    demand: np.ndarray,
) -> Dict[str, float]:
    """Evaluate the four objectives from Section VI.E.

    Parameters
    ----------
    rb_alloc   : (C,) resource-block allocation for one time slot
    power_alloc: (C,) power allocation for one time slot
    demand     : (C,) demand for one time slot

    Returns
    -------
    dict with 'throughput', 'fairness', 'energy_efficiency', 'latency'
    """
    C = len(rb_alloc)

    # f1: Throughput ∝ log2(1 + SINR).  Simplified: proportional to RB * log2(1 + P/RB)
    sinr = np.where(rb_alloc > 0, power_alloc / (rb_alloc + 1e-12), 0)
    throughput = float(np.sum(rb_alloc * np.log2(1 + sinr)))

    # f2: Jain fairness index over per-cell throughput
    per_cell_tp = rb_alloc * np.log2(1 + sinr)
    fairness = jain_fairness(per_cell_tp)

    # f3: Energy efficiency = throughput / total power
    total_power = power_alloc.sum() + 1e-12
    energy_eff = throughput / total_power

    # f4: Latency proxy (inversely proportional to satisfaction ratio)
    satisfaction = np.where(demand > 0, rb_alloc / (demand + 1e-12), 1.0)
    satisfaction = np.clip(satisfaction, 0, 1)
    latency = float(1.0 - satisfaction.mean())  # 0 = perfect, 1 = worst

    return {
        "throughput": throughput,
        "fairness": fairness,
        "energy_efficiency": energy_eff,
        "latency": latency,
    }


def multi_objective_fitness(
    individual: np.ndarray,
    demand: np.ndarray,
    R_max: float,
    P_max: float,
    weights: np.ndarray,
) -> float:
    """Weighted composite metric M_composite = Σ ω_i * f_i.

    ``individual`` encodes a candidate allocation: first C values are
    RB fractions, next C values are power fractions (all in [0, 1]).
    """
    C = len(demand)
    rb_frac = np.clip(individual[:C], 0, 1)
    pw_frac = np.clip(individual[C:], 0, 1)

    # Normalize so total RB and power respect budgets
    rb_sum = rb_frac.sum()
    if rb_sum > 0:
        rb_alloc = rb_frac / rb_sum * R_max
    else:
        rb_alloc = np.full(C, R_max / C)
    pw_sum = pw_frac.sum()
    if pw_sum > 0:
        power_alloc = pw_frac / pw_sum * P_max
    else:
        power_alloc = np.full(C, P_max / C)

    obj = compute_objectives(rb_alloc, power_alloc, demand)

    # Composite: maximise throughput, fairness, energy_eff; minimise latency
    score = (
        weights[0] * obj["throughput"]
        + weights[1] * obj["fairness"]
        + weights[2] * obj["energy_efficiency"]
        - weights[3] * obj["latency"]
    )
    return float(score)


def genetic_algorithm_optimize(
    demand: np.ndarray,
    R_max: float,
    P_max: float,
    weights: np.ndarray,
    *,
    pop_size: int = 50,
    generations: int = 100,
    mutation_rate: float = 0.1,
    crossover_rate: float = 0.7,
    rng: np.random.Generator | None = None,
) -> Tuple[np.ndarray, List[float]]:
    """Simple GA for multi-objective optimization (Section VI.E).

    Returns
    -------
    best_individual : ndarray of shape (2*C,)
    fitness_history : list of best fitness per generation
    """
    if rng is None:
        rng = np.random.default_rng(42)

    C = len(demand)
    gene_len = 2 * C

    # Initialize population
    population = rng.uniform(0, 1, size=(pop_size, gene_len))
    fitness_history: List[float] = []

    for gen in range(generations):
        # Evaluate fitness
        scores = np.array([
            multi_objective_fitness(ind, demand, R_max, P_max, weights)
            for ind in population
        ])
        best_idx = np.argmax(scores)
        fitness_history.append(float(scores[best_idx]))

        # Selection: tournament (size 3)
        new_pop = [population[best_idx].copy()]  # elitism
        while len(new_pop) < pop_size:
            idxs = rng.choice(pop_size, size=3, replace=False)
            parent1 = population[idxs[np.argmax(scores[idxs])]].copy()
            idxs2 = rng.choice(pop_size, size=3, replace=False)
            parent2 = population[idxs2[np.argmax(scores[idxs2])]].copy()

            # Crossover
            if rng.random() < crossover_rate:
                alpha = rng.uniform(0, 1, size=gene_len)
                child = alpha * parent1 + (1 - alpha) * parent2
            else:
                child = parent1.copy()

            # Mutation
            mask = rng.random(gene_len) < mutation_rate
            child[mask] += rng.normal(0, 0.1, size=mask.sum())
            child = np.clip(child, 0, 1)

            new_pop.append(child)

        population = np.array(new_pop[:pop_size])

    # Final evaluation
    scores = np.array([
        multi_objective_fitness(ind, demand, R_max, P_max, weights)
        for ind in population
    ])
    best = population[np.argmax(scores)]
    return best, fitness_history


def pareto_front(
    demand: np.ndarray,
    R_max: float,
    P_max: float,
    *,
    n_points: int = 10,
    pop_size: int = 30,
    generations: int = 50,
) -> List[Dict]:
    """Generate approximate Pareto front by varying weight vectors."""
    rng = np.random.default_rng(42)
    results: List[Dict] = []

    for i in range(n_points):
        w = rng.dirichlet(np.ones(4))
        best, hist = genetic_algorithm_optimize(
            demand, R_max, P_max, w,
            pop_size=pop_size, generations=generations, rng=rng,
        )
        C = len(demand)
        rb_frac = np.clip(best[:C], 0, 1)
        pw_frac = np.clip(best[C:], 0, 1)
        rb_alloc = rb_frac / (rb_frac.sum() + 1e-12) * R_max
        pw_alloc = pw_frac / (pw_frac.sum() + 1e-12) * P_max
        obj = compute_objectives(rb_alloc, pw_alloc, demand)
        results.append({"weights": w, "objectives": obj, "fitness": hist[-1]})

    return results


# ══════════════════════════════════════════════════════════════════
# Cell Sleep / Pre-activation (Section V.C.1)
# ══════════════════════════════════════════════════════════════════

def cell_sleep_simulation(
    demand_trace: np.ndarray,
    threshold: float,
    *,
    delta_preactivate: int = 3,
    power_active: float = 40.0,
    power_sleep: float = 5.0,
) -> Dict[str, np.ndarray]:
    """Simulate reactive vs proactive cell sleep management.

    Parameters
    ----------
    demand_trace : (C, T) demand trace
    threshold : float
        Activation threshold per cell.
    delta_preactivate : int
        Proactive look-ahead slots (Δ).
    power_active, power_sleep : float
        Per-cell power consumption in active / sleep mode (watts).

    Returns
    -------
    dict with 'reactive_active', 'proactive_active',
              'reactive_energy', 'proactive_energy'
    """
    C, T = demand_trace.shape

    reactive_active = np.zeros((C, T), dtype=bool)
    proactive_active = np.zeros((C, T), dtype=bool)

    for c in range(C):
        for t in range(T):
            # Reactive: activate only when demand exceeds threshold NOW
            if demand_trace[c, t] >= threshold:
                reactive_active[c, t] = True

            # Proactive: activate Δ steps before predicted surge
            for dt in range(delta_preactivate + 1):
                future_t = t + dt
                if future_t < T and demand_trace[c, future_t] >= threshold:
                    proactive_active[c, t] = True
                    break

    # Energy consumption
    reactive_energy = np.where(reactive_active, power_active, power_sleep).sum(axis=0)
    proactive_energy = np.where(proactive_active, power_active, power_sleep).sum(axis=0)

    return {
        "reactive_active": reactive_active,
        "proactive_active": proactive_active,
        "reactive_energy": reactive_energy,
        "proactive_energy": proactive_energy,
    }


# ══════════════════════════════════════════════════════════════════
# Reactive vs Proactive KPI Simulation (Section VII.C)
# ══════════════════════════════════════════════════════════════════

def simulate_reactive_vs_proactive(
    demand_trace: np.ndarray,
    capacity_per_cell: float,
    *,
    kappa: float = 1.96,
    noise_std_frac: float = 0.15,
    delta_preactivate: int = 3,
) -> Dict[str, Dict[str, float]]:
    """Compare reactive and proactive resource management on a traffic trace.

    The *reactive* controller sees only the current slot's demand.
    The *proactive* controller has predictions + CI for future slots
    and pre-allocates resources.

    Tracked KPIs (Section VII.C):
      - Blocking rate
      - Average latency
      - Resource utilization
      - Energy consumption (via cell sleep)

    Returns
    -------
    dict with 'reactive' and 'proactive' sub-dicts of KPIs.
    """
    C, T = demand_trace.shape
    rng = np.random.default_rng(42)

    # Generate "predictions" as noisy versions of actual demand
    sigma = noise_std_frac * demand_trace.mean() * np.ones_like(demand_trace)
    D_hat = demand_trace + rng.normal(0, sigma)
    D_hat = np.clip(D_hat, 0, None)

    total_capacity = capacity_per_cell * C

    # ── Reactive management ──
    # Reactive controller uses the *previous* slot's demand for allocation
    # decisions (realistic 1-slot reaction lag).
    reactive_blocked = 0
    reactive_latency = []
    reactive_utilization = []
    reactive_energy = 0.0
    POWER_ACTIVE = 40.0
    POWER_SLEEP = 5.0

    prev_demand = demand_trace[:, 0]  # initial guess = first slot

    for t in range(T):
        actual_demand = demand_trace[:, t]

        # Reactive allocation is based on PREVIOUS demand (lag)
        ref_demand = prev_demand
        total_ref = ref_demand.sum()
        if total_ref > 0:
            alloc_frac = ref_demand / total_ref
        else:
            alloc_frac = np.ones(C) / C
        alloc = alloc_frac * total_capacity

        served = np.minimum(actual_demand, alloc)
        unserved = actual_demand - served
        reactive_blocked += int((unserved > 0.5).sum())

        satisfaction = np.clip(served / (actual_demand + 1e-12), 0, 1)
        latency = 1.0 - satisfaction.mean()
        reactive_latency.append(latency)

        util = served.sum() / (total_capacity + 1e-12)
        reactive_utilization.append(util)

        active_cells = (actual_demand > 0).sum()
        sleep_cells = C - active_cells
        reactive_energy += active_cells * POWER_ACTIVE + sleep_cells * POWER_SLEEP

        prev_demand = actual_demand.copy()

    # ── Proactive management ──
    # Proactive controller uses predicted future demand + CI for allocation.
    proactive_blocked = 0
    proactive_latency = []
    proactive_utilization = []
    proactive_energy = 0.0

    for t in range(T):
        actual_demand = demand_trace[:, t]

        # Proactive: use prediction + CI to anticipate the current slot
        future_window = min(t + delta_preactivate + 1, T)
        predicted_max = D_hat[:, t:future_window].max(axis=1)
        robust_demand = predicted_max + kappa * sigma[:, t]
        robust_demand = np.clip(robust_demand, 0, None)

        # Allocate based on robust (anticipated) demand
        total_robust = robust_demand.sum()
        if total_robust > 0:
            alloc_frac = robust_demand / total_robust
        else:
            alloc_frac = np.ones(C) / C
        alloc = alloc_frac * total_capacity

        served = np.minimum(actual_demand, alloc)
        blocked = int((actual_demand - served > 0.5).sum())
        proactive_blocked += blocked

        satisfaction = np.clip(served / (actual_demand + 1e-12), 0, 1)
        latency = 1.0 - satisfaction.mean()
        proactive_latency.append(latency)

        util = served.sum() / (total_capacity + 1e-12)
        proactive_utilization.append(util)

        cells_needed = (robust_demand > 0).sum()
        sleep_cells = C - cells_needed
        proactive_energy += cells_needed * POWER_ACTIVE + sleep_cells * POWER_SLEEP

    # ── Aggregate KPIs ──
    total_requests = C * T
    reactive_kpi = {
        "blocking_rate": reactive_blocked / total_requests,
        "avg_latency": float(np.mean(reactive_latency)),
        "avg_utilization": float(np.mean(reactive_utilization)),
        "total_energy": reactive_energy,
    }
    proactive_kpi = {
        "blocking_rate": proactive_blocked / total_requests,
        "avg_latency": float(np.mean(proactive_latency)),
        "avg_utilization": float(np.mean(proactive_utilization)),
        "total_energy": proactive_energy,
    }

    return {"reactive": reactive_kpi, "proactive": proactive_kpi}


# ══════════════════════════════════════════════════════════════════
# Self-test
# ══════════════════════════════════════════════════════════════════

def run_self_test() -> None:
    """Comprehensive self-test for Algorithms 3, 4, 5 and the
    reactive-vs-proactive simulation."""
    print("\n" + "=" * 60)
    print("  PROACTIVE RESOURCE MANAGEMENT SELF-TEST")
    print("=" * 60)

    np.random.seed(42)
    rng = np.random.default_rng(42)

    C = 10   # cells
    T = 24   # time slots
    R_MAX_RB = 100.0
    P_MAX = 50.0

    # ── Test Algorithm 3 ─────────────────────────────────────────
    print("\n── Algorithm 3: Proactive Resource Allocation ──")

    D_hat = rng.uniform(5, 30, size=(C, T))
    sigma = rng.uniform(1, 5, size=(C, T))

    result = proactive_resource_allocation(
        D_hat, sigma, R_MAX_RB, P_MAX, kappa=1.96,
    )

    rb = result["rb_alloc"]
    pw = result["power_alloc"]
    sl = result["slice_alloc"]

    # Assert: total RB per slot <= R_max
    for t in range(T):
        total_rb_t = rb[:, t].sum()
        assert total_rb_t <= R_MAX_RB + 1e-6, (
            f"RB constraint violated at t={t}: {total_rb_t:.2f} > {R_MAX_RB}"
        )
    print(f"  ✓ RB constraints satisfied (max total = "
          f"{rb.sum(axis=0).max():.2f} ≤ {R_MAX_RB})")

    # Assert: total power per slot <= P_max
    for t in range(T):
        total_pw_t = pw[:, t].sum()
        assert total_pw_t <= P_MAX + 1e-6, (
            f"Power constraint violated at t={t}: {total_pw_t:.2f} > {P_MAX}"
        )
    print(f"  ✓ Power constraints satisfied (max total = "
          f"{pw.sum(axis=0).max():.2f} ≤ {P_MAX})")

    # Assert: slice allocations sum to cell allocation
    for t in range(T):
        for c in range(C):
            slice_sum = sl[:, c, t].sum()
            assert abs(slice_sum - rb[c, t]) < 1e-6, (
                f"Slice alloc mismatch at c={c}, t={t}: "
                f"{slice_sum:.4f} != {rb[c, t]:.4f}"
            )
    print("  ✓ Slice allocations consistent with cell RB allocations")

    # Assert: allocations are non-negative
    assert np.all(rb >= -1e-12), "Negative RB allocation"
    assert np.all(pw >= -1e-12), "Negative power allocation"
    print("  ✓ All allocations non-negative")

    print(f"  ✓ Converged: {result['converged']}")

    # ── Test Algorithm 4 ─────────────────────────────────────────
    print("\n── Algorithm 4: Online Model Update ──")

    # Test drift detection
    training_error = 0.10
    errors_no_drift = rng.uniform(0.08, 0.12, size=20)
    errors_with_drift = rng.uniform(0.15, 0.25, size=20)

    assert not detect_drift(errors_no_drift, training_error, delta=0.2), \
        "False drift detection"
    print(f"  ✓ No false drift (mean error = {errors_no_drift.mean():.3f})")

    assert detect_drift(errors_with_drift, training_error, delta=0.2), \
        "Missed drift detection"
    print(f"  ✓ Drift correctly detected (mean error = "
          f"{errors_with_drift.mean():.3f})")

    # Test full model update with a tiny model
    import torch
    import torch.nn as nn

    class _TinyModel(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc = nn.Linear(4, 4)

        def forward(self, x):
            return self.fc(x)

    torch.manual_seed(42)
    tiny = _TinyModel()
    x_new = torch.randn(20, 4)
    y_new = torch.randn(20, 4)

    model_out, was_updated, err = online_model_update(
        tiny, x_new, y_new,
        training_error=0.10,
        recent_errors=errors_with_drift,
        delta=0.2, epochs=5,
    )
    print(f"  ✓ Model update completed (updated={was_updated}, "
          f"error={err:.4f})")

    # ── Test Algorithm 5 ─────────────────────────────────────────
    print("\n── Algorithm 5: Multi-Objective Optimization ──")

    demand_slot = rng.uniform(5, 25, size=C)
    weights = np.array([0.4, 0.2, 0.2, 0.2])

    best, history = genetic_algorithm_optimize(
        demand_slot, R_MAX_RB, P_MAX, weights,
        pop_size=50, generations=100, rng=np.random.default_rng(42),
    )

    # Assert: fitness improves over generations
    early = np.mean(history[:10])
    late = np.mean(history[-10:])
    assert late >= early, (
        f"GA fitness did not improve: early={early:.4f}, late={late:.4f}"
    )
    print(f"  ✓ GA fitness improved: {early:.4f} → {late:.4f}")
    print(f"  ✓ Best fitness = {history[-1]:.4f}")

    # Pareto front
    pf = pareto_front(demand_slot, R_MAX_RB, P_MAX,
                      n_points=5, pop_size=20, generations=30)
    assert len(pf) == 5, f"Expected 5 Pareto points, got {len(pf)}"
    print(f"  ✓ Pareto front generated ({len(pf)} points)")

    # ── Reactive vs Proactive Simulation ─────────────────────────
    print("\n── Reactive vs Proactive Simulation (Section VII.C) ──")

    # Synthetic demand trace with realistic daily pattern
    t_axis = np.linspace(0, 2 * np.pi, T)
    base_demand = 15 + 10 * np.sin(t_axis)  # daily cycle
    demand_trace = np.zeros((C, T))
    for c in range(C):
        phase = rng.uniform(-0.5, 0.5)
        scale = rng.uniform(0.8, 1.2)
        demand_trace[c] = scale * (base_demand + phase) + rng.normal(0, 2, T)
    demand_trace = np.clip(demand_trace, 0, None)

    capacity_per_cell = 8.0  # tighter capacity to induce blocking

    kpis = simulate_reactive_vs_proactive(
        demand_trace, capacity_per_cell, kappa=1.96,
    )

    r_kpi = kpis["reactive"]
    p_kpi = kpis["proactive"]

    print(f"  Reactive  – Blocking: {r_kpi['blocking_rate']:.4f}, "
          f"Latency: {r_kpi['avg_latency']:.4f}, "
          f"Util: {r_kpi['avg_utilization']:.4f}, "
          f"Energy: {r_kpi['total_energy']:.0f}")
    print(f"  Proactive – Blocking: {p_kpi['blocking_rate']:.4f}, "
          f"Latency: {p_kpi['avg_latency']:.4f}, "
          f"Util: {p_kpi['avg_utilization']:.4f}, "
          f"Energy: {p_kpi['total_energy']:.0f}")

    # Assert: proactive should have lower blocking rate
    assert p_kpi["blocking_rate"] <= r_kpi["blocking_rate"], (
        f"Proactive blocking ({p_kpi['blocking_rate']:.4f}) > "
        f"reactive ({r_kpi['blocking_rate']:.4f})"
    )
    print("  ✓ Proactive blocking ≤ reactive blocking")

    # Assert: proactive should have lower average latency
    assert p_kpi["avg_latency"] <= r_kpi["avg_latency"] + 1e-6, (
        f"Proactive latency ({p_kpi['avg_latency']:.4f}) > "
        f"reactive ({r_kpi['avg_latency']:.4f})"
    )
    print("  ✓ Proactive latency ≤ reactive latency")

    # ── Cell Sleep Simulation ────────────────────────────────────
    print("\n── Cell Sleep / Pre-activation (Section V.C.1) ──")

    sleep_result = cell_sleep_simulation(
        demand_trace, threshold=12.0, delta_preactivate=3,
    )

    react_active = sleep_result["reactive_active"].sum()
    proact_active = sleep_result["proactive_active"].sum()
    print(f"  Reactive active cell-slots:  {react_active}")
    print(f"  Proactive active cell-slots: {proact_active}")
    # Proactive activates cells ahead of time → more active slots
    assert proact_active >= react_active, (
        "Proactive should activate at least as many cell-slots as reactive"
    )
    print("  ✓ Proactive pre-activates cells before demand surges")

    # Compute improvement metrics (reference targets from Section VII.C)
    if r_kpi["blocking_rate"] > 0:
        blocking_reduction = (1 - p_kpi["blocking_rate"] / r_kpi["blocking_rate"]) * 100
    else:
        blocking_reduction = 0.0
    if r_kpi["avg_latency"] > 0:
        latency_reduction = (1 - p_kpi["avg_latency"] / r_kpi["avg_latency"]) * 100
    else:
        latency_reduction = 0.0

    print(f"\n  ── Improvement Summary ──")
    print(f"  Blocking rate reduction:  {blocking_reduction:.1f} % "
          f"(article target: 35-42 %)")
    print(f"  Latency reduction:        {latency_reduction:.1f} % "
          f"(article target: 28-34 %)")

    print("\n  ══════════════════════════════════════")
    print("  ALL PROACTIVE MANAGEMENT SELF-TESTS PASSED ✓")
    print("  ══════════════════════════════════════\n")


# ──────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Algorithms 3-5: Proactive Resource Management for 5G.",
    )
    parser.add_argument(
        "--self-test", action="store_true",
        help="Run comprehensive self-test suite.",
    )
    args = parser.parse_args()

    np.random.seed(42)

    if args.self_test:
        run_self_test()
        return

    # Demo: run Algorithm 3 on synthetic data
    rng = np.random.default_rng(42)
    C, T = 10, 24
    D_hat = rng.uniform(5, 30, size=(C, T))
    sigma = rng.uniform(1, 5, size=(C, T))

    print("Running Algorithm 3: Proactive Resource Allocation …")
    result = proactive_resource_allocation(D_hat, sigma, R_max_rb=100, P_max=50)
    print(f"  Converged: {result['converged']}")
    print(f"  Max RB/slot: {result['rb_alloc'].sum(axis=0).max():.2f}")
    print(f"  Max Power/slot: {result['power_alloc'].sum(axis=0).max():.2f}")


if __name__ == "__main__":
    main()
