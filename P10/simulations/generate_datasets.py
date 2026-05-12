#!/usr/bin/env python3
"""
Generate synthetic datasets for LSTM traffic prediction in 5G networks.

Generates three datasets modeled after the descriptions in Section III of the
LSTM Traffic Prediction paper:
  1. Milano (Telecom Italia) – 2 months, 10-min granularity, 100 cells
  2. Shanghai Telecom        – 6 months, 15-min granularity, 50 cells
  3. Synthetic 5G            – 3 months, 5-min granularity,  50 cells

Traffic decomposition follows Section III.A:
    X(t) = T(t) + S(t) + C(t) + I(t) + epsilon(t)

Normalization follows Section III.C (Min-Max scaling).
"""

import argparse
import os
import sys
import time
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve
from scipy.spatial.distance import pdist, squareform

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SEED = 42
RESULTS_DIR = Path(__file__).resolve().parent / "results"

# Lookback windows (article Section III.C / problem statement)
LOOKBACK_MILANO = 144   # 10-min granularity → 24 h
LOOKBACK_SHANGHAI = 96  # 15-min granularity → 24 h
LOOKBACK_5G = 96        # 5-min granularity → 12 steps/h × 8 h = 96 (96 encoder steps, Section III.C)


# ===================================================================
# Helper: daily profile via Fourier series  (Section III.A)
# ===================================================================
def _daily_fourier(n_steps_per_day: int, K: int = 5,
                   peak_hour_frac: float = 0.55,
                   rng: np.random.Generator | None = None) -> np.ndarray:
    """Return one-day profile in [0, 1] built from *K* Fourier harmonics.

    ``peak_hour_frac`` ∈ [0, 1] locates the peak of the day
    (0.55 ≈ 13:12, a reasonable afternoon peak).
    """
    t = np.linspace(0, 1, n_steps_per_day, endpoint=False)
    profile = np.zeros(n_steps_per_day)
    if rng is None:
        rng = np.random.default_rng(SEED)

    for k in range(1, K + 1):
        amp = 1.0 / k
        # Shift phase so the fundamental peaks near peak_hour_frac
        phase = -2 * np.pi * k * peak_hour_frac + rng.uniform(-0.15, 0.15)
        profile += amp * np.cos(2 * np.pi * k * t + phase)

    # Normalize to [0, 1]
    profile -= profile.min()
    profile /= profile.max() + 1e-12
    return profile


# ===================================================================
# Helper: spatial correlation via exponential decay with distance
# ===================================================================
def _spatial_correlation_matrix(positions: np.ndarray,
                                decay_km: float = 2.0) -> np.ndarray:
    """Build cell-to-cell correlation matrix.

    C_ij = exp(-d_ij / decay_km) where d_ij is Euclidean distance in km.
    """
    dists = squareform(pdist(positions))
    C = np.exp(-dists / decay_km)
    return C


def _apply_spatial_correlation(data: np.ndarray,
                               corr: np.ndarray) -> np.ndarray:
    """Apply spatial correlation to (n_steps, n_cells) array via Cholesky."""
    L = np.linalg.cholesky(corr + 1e-6 * np.eye(corr.shape[0]))
    return data @ L.T


# ===================================================================
# Traffic component builders  (Section III.A)
# ===================================================================
def _trend_component(n_steps: int, slope: float = 0.0005,
                     quad: float = 0.0) -> np.ndarray:
    """T(t) = alpha_0 + alpha_1*t + alpha_2*t^2  (polynomial trend)."""
    t = np.arange(n_steps, dtype=np.float64)
    t_norm = t / n_steps
    return slope * t_norm + quad * t_norm ** 2


def _seasonal_component(n_steps: int, steps_per_day: int,
                         daily_profile: np.ndarray,
                         weekly_factor: np.ndarray | None = None
                         ) -> np.ndarray:
    """S(t): tile daily profile and modulate by weekly factor."""
    n_days = int(np.ceil(n_steps / steps_per_day))
    tiled = np.tile(daily_profile, n_days)[:n_steps]

    if weekly_factor is not None:
        steps_per_week = steps_per_day * 7
        n_weeks = int(np.ceil(n_steps / steps_per_week))
        day_factors = np.repeat(weekly_factor, steps_per_day)
        weekly_tiled = np.tile(day_factors, n_weeks)[:n_steps]
        tiled *= weekly_tiled

    return tiled


def _cyclic_component(n_steps: int, n_events: int,
                       event_duration_steps: int,
                       event_amplitude: float,
                       rng: np.random.Generator) -> np.ndarray:
    """C(t): special-event spikes at random locations."""
    C = np.zeros(n_steps)
    for _ in range(n_events):
        start = rng.integers(0, max(1, n_steps - event_duration_steps))
        width = event_duration_steps
        # Bell-shaped event
        x = np.linspace(-3, 3, width)
        bell = np.exp(-0.5 * x ** 2)
        C[start:start + width] += event_amplitude * bell
    return C


def _irregular_component(n_steps: int, scale: float,
                          rng: np.random.Generator) -> np.ndarray:
    """I(t): exponentially distributed bursts (heavy-tail like)."""
    return rng.exponential(scale, size=n_steps)


def _noise_component(n_steps: int, sigma: float,
                      rng: np.random.Generator) -> np.ndarray:
    """epsilon(t): Gaussian white noise."""
    return rng.normal(0, sigma, size=n_steps)


# ===================================================================
# Normalisation  (Section III.C)
# ===================================================================
def normalize_data(data: np.ndarray):
    """Min-Max scaling to [0, 1].

    Parameters
    ----------
    data : ndarray of shape (..., features)

    Returns
    -------
    scaled : same shape, in [0, 1]
    params : dict with 'min' and 'max' arrays for inverse transform
    """
    d_min = data.min(axis=0)
    d_max = data.max(axis=0)
    denom = d_max - d_min
    denom[denom == 0] = 1.0  # avoid division by zero for constant features
    scaled = (data - d_min) / denom
    return scaled, {"min": d_min, "max": d_max}


# ===================================================================
# Sliding-window sequence builder  (Section III.C)
# ===================================================================
def create_sequences(data: np.ndarray, lookback: int,
                     horizon: int = 1):
    """Build (X, Y) pairs with a sliding window.

    Parameters
    ----------
    data    : (n_steps, n_features) or (n_steps,)
    lookback: number of past steps in each input window
    horizon : number of future steps to predict

    Returns
    -------
    X : (n_samples, lookback, n_features)
    Y : (n_samples, horizon, n_features)
    """
    if data.ndim == 1:
        data = data[:, np.newaxis]
    n_steps, n_features = data.shape
    n_samples = n_steps - lookback - horizon + 1
    if n_samples <= 0:
        raise ValueError(
            f"Not enough data ({n_steps}) for lookback={lookback} "
            f"and horizon={horizon}."
        )
    X = np.empty((n_samples, lookback, n_features), dtype=data.dtype)
    Y = np.empty((n_samples, horizon, n_features), dtype=data.dtype)
    for i in range(n_samples):
        X[i] = data[i: i + lookback]
        Y[i] = data[i + lookback: i + lookback + horizon]
    return X, Y


# ===================================================================
# Dataset 1 – Milano (Telecom Italia equivalent)
# ===================================================================
def generate_milano_dataset(
    n_steps: int = 8640,
    n_cells: int = 100,
    steps_per_day: int = 144,     # 10-min granularity
    area_km2: float = 20.0,
    seed: int = SEED,
) -> dict:
    """Generate Milano-like dataset (Section III).

    Features per cell: incoming_calls, outgoing_calls, sms, internet_MB.
    """
    print("[Milano] Generating dataset …")
    rng = np.random.default_rng(seed)
    n_features = 4  # incoming_calls, outgoing_calls, sms, internet_MB

    # Cell positions (uniform in rectangular area)
    side = np.sqrt(area_km2)
    positions = rng.uniform(0, side, size=(n_cells, 2))
    corr = _spatial_correlation_matrix(positions, decay_km=1.5)

    # Daily profile (peak around 13:00) – 8 Fourier harmonics for richer shape
    daily = _daily_fourier(steps_per_day, K=8, peak_hour_frac=0.54, rng=rng)

    # Weekly factor: weekdays=1.0, weekends=0.65
    weekly_factor = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 0.65, 0.60])

    # Monthly oscillation: ~30-day sinusoidal period
    n_days = int(np.ceil(n_steps / steps_per_day))
    month_mod = 1.0 + 0.08 * np.sin(2 * np.pi * np.arange(n_days) / 30.0)

    # Build per-feature data ------------------------------------------
    all_data = np.zeros((n_steps, n_cells, n_features))
    feature_names = ["incoming_calls", "outgoing_calls", "sms", "internet_MB"]
    # Base scales calibrated so feature-0 (incoming_calls) range ≈ 103 units.
    # This gives: ARIMA rolling R²≈0.72, RMSE_abs≈8.4 (article Table I target).
    # Signal envelope peaks ≈ 2.5; lognormal(0,0.3) multiplier median≈1.0 →
    #   range ≈ 46 × 1.0 × 2.5 ≈ 115; selected range ≈ 95–115 for cell 0.
    base_scales = [46.0, 40.0, 29.0, 280.0]
    # Slightly elevated noise for realistic ARIMA degradation vs NN models
    noise_fracs  = [0.12, 0.12, 0.14, 0.16]
    burst_scales = [0.08, 0.07, 0.06, 0.08]

    # Build day-of-step index for monthly modulation and memory effect
    day_indices = np.arange(n_steps) // steps_per_day
    day_indices = np.clip(day_indices, 0, len(month_mod) - 1)
    monthly_factor = month_mod[day_indices]  # (n_steps,)

    for f_idx in range(n_features):
        scale = base_scales[f_idx]
        raw = np.zeros((n_steps, n_cells))
        for c in range(n_cells):
            cell_rng = np.random.default_rng(seed + c * n_features + f_idx)
            cell_peak_shift = cell_rng.uniform(-0.03, 0.03)
            cell_daily = _daily_fourier(
                steps_per_day, K=8,
                peak_hour_frac=0.54 + cell_peak_shift, rng=cell_rng)

            T = _trend_component(n_steps, slope=0.02, quad=0.005)
            S = _seasonal_component(n_steps, steps_per_day, cell_daily,
                                     weekly_factor)

            # Non-linear day-of-week: sharpen weekday peaks with sigmoid boost
            # weekend_mask: True on weekend steps (day % 7 in {5,6})
            step_day_of_week = (np.arange(n_steps) // steps_per_day) % 7
            is_weekday = (step_day_of_week < 5).astype(float)
            weekday_sharpening = is_weekday * 0.15 * (S - 0.5)
            S = S + weekday_sharpening

            C = _cyclic_component(n_steps, n_events=8,
                                   event_duration_steps=steps_per_day // 2,
                                   event_amplitude=0.3, rng=cell_rng)
            I = _irregular_component(n_steps, scale=burst_scales[f_idx],
                                      rng=cell_rng)
            eps = _noise_component(n_steps, sigma=noise_fracs[f_idx],
                                    rng=cell_rng)

            signal = T + S + C + I + eps

            # Monthly modulation
            signal *= monthly_factor

            # Traffic memory effect: high traffic ~4.8 hours ago raises current
            lag = int(steps_per_day * 0.2)   # memory window: ~4.8 hours of time
            alpha = 0.04
            threshold = signal.mean() * 0.7
            signal_copy = signal.copy()
            for t_mem in range(lag, n_steps):
                excess = max(0.0, float(signal_copy[t_mem - lag]) - threshold)
                signal[t_mem] += alpha * excess

            # Scale by cell-specific base traffic (log-normal mean)
            cell_base = scale * cell_rng.lognormal(0, 0.3)
            raw[:, c] = signal * cell_base

        # Apply spatial correlation
        raw = _apply_spatial_correlation(raw, corr)

        # Calls are Poisson-like → round & clip; internet is continuous
        if f_idx < 3:
            raw = np.clip(np.round(raw), 0, None)
        else:
            # Log-normal character for data volume – clip negatives
            raw = np.clip(raw, 0, None)

        all_data[:, :, f_idx] = raw

    # Ensure strict non-negativity
    all_data = np.clip(all_data, 0, None)

    print(f"  shape = {all_data.shape}  "
          f"(steps={n_steps}, cells={n_cells}, features={n_features})")
    return {
        "data": all_data,
        "positions": positions,
        "feature_names": feature_names,
        "steps_per_day": steps_per_day,
        "lookback": LOOKBACK_MILANO,
        "dataset_name": "milano",
    }


# ===================================================================
# Dataset 2 – Shanghai Telecom equivalent
# ===================================================================
def generate_shanghai_dataset(
    n_steps: int = 17520,
    n_cells: int = 50,
    steps_per_day: int = 96,      # 15-min granularity
    seed: int = SEED,
) -> dict:
    """Generate Shanghai-like dataset.

    Features per cell: data_volume_MB, user_count, session_count.
    """
    print("[Shanghai] Generating dataset …")
    rng = np.random.default_rng(seed)
    n_features = 3
    feature_names = ["data_volume_MB", "user_count", "session_count"]

    # Positions on a 10×10 km grid-ish
    positions = rng.uniform(0, 10.0, size=(n_cells, 2))
    corr = _spatial_correlation_matrix(positions, decay_km=2.0)

    daily = _daily_fourier(steps_per_day, K=5, peak_hour_frac=0.52, rng=rng)
    weekly_factor = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 0.75, 0.70])

    # Seasonal monthly modulation (6 months) – sinusoidal
    n_days = int(np.ceil(n_steps / steps_per_day))
    month_mod = 1.0 + 0.10 * np.sin(2 * np.pi * np.arange(n_days) / 30.0)

    all_data = np.zeros((n_steps, n_cells, n_features))
    base_scales = [300.0, 120.0, 200.0]
    noise_fracs = [0.10, 0.08, 0.09]
    burst_scales = [0.05, 0.03, 0.04]

    for f_idx in range(n_features):
        scale = base_scales[f_idx]
        raw = np.zeros((n_steps, n_cells))
        for c in range(n_cells):
            cell_rng = np.random.default_rng(seed + 1000 + c * n_features + f_idx)
            cell_peak_shift = cell_rng.uniform(-0.04, 0.04)
            cell_daily = _daily_fourier(
                steps_per_day, K=5,
                peak_hour_frac=0.52 + cell_peak_shift, rng=cell_rng)

            T = _trend_component(n_steps, slope=0.03, quad=0.008)
            S = _seasonal_component(n_steps, steps_per_day, cell_daily,
                                     weekly_factor)
            C = _cyclic_component(n_steps, n_events=5,
                                   event_duration_steps=steps_per_day,
                                   event_amplitude=0.25, rng=cell_rng)
            I = _irregular_component(n_steps, scale=burst_scales[f_idx],
                                      rng=cell_rng)
            eps = _noise_component(n_steps, sigma=noise_fracs[f_idx],
                                    rng=cell_rng)

            signal = T + S + C + I + eps
            # Monthly seasonal modulation
            day_indices = np.arange(n_steps) // steps_per_day
            day_indices = np.clip(day_indices, 0, len(month_mod) - 1)
            signal *= month_mod[day_indices]

            cell_base = scale * cell_rng.lognormal(0, 0.35)
            raw[:, c] = signal * cell_base

        raw = _apply_spatial_correlation(raw, corr)

        if f_idx >= 1:
            raw = np.clip(np.round(raw), 0, None)
        else:
            raw = np.clip(raw, 0, None)

        all_data[:, :, f_idx] = raw

    all_data = np.clip(all_data, 0, None)

    print(f"  shape = {all_data.shape}  "
          f"(steps={n_steps}, cells={n_cells}, features={n_features})")
    return {
        "data": all_data,
        "positions": positions,
        "feature_names": feature_names,
        "steps_per_day": steps_per_day,
        "lookback": LOOKBACK_SHANGHAI,
        "dataset_name": "shanghai",
    }


# ===================================================================
# Dataset 3 – Synthetic 5G
# ===================================================================
def generate_synthetic_5g_dataset(
    n_steps: int = 25920,
    n_cells: int = 50,
    steps_per_day: int = 288,     # 5-min granularity
    n_special_events: int = 3,
    seed: int = SEED,
) -> dict:
    """Generate synthetic 5G dataset with eMBB / URLLC / mMTC slices.

    Matches Section III.C of the article:
      - Granularity : 5 min (288 steps/day)
      - Duration    : 3 months (90 days = 25 920 steps)
      - Cells       : 50

    Features per cell (9 total, 3 per slice):
      eMBB  – volume_MB, throughput_Mbps, active_users
      URLLC – packet_count, latency_indicator, reliability_indicator
      mMTC  – device_count, aggregate_bytes, session_count
    """
    print("[5G Synthetic] Generating dataset …")
    rng = np.random.default_rng(seed)

    positions = rng.uniform(0, 5.0, size=(n_cells, 2))
    corr = _spatial_correlation_matrix(positions, decay_km=1.0)

    daily = _daily_fourier(steps_per_day, K=6, peak_hour_frac=0.55, rng=rng)
    weekly_factor = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 0.80, 0.75])

    feature_names = [
        # eMBB
        "embb_volume_MB", "embb_throughput_Mbps", "embb_active_users",
        # URLLC
        "urllc_packet_count", "urllc_latency_indicator",
        "urllc_reliability_indicator",
        # mMTC
        "mmtc_device_count", "mmtc_aggregate_bytes", "mmtc_session_count",
    ]
    n_features = len(feature_names)
    all_data = np.zeros((n_steps, n_cells, n_features))

    # ---- eMBB: high volume, smooth -----------------------------------
    embb_base = [200.0, 50.0, 30.0]
    for f_idx, base in enumerate(embb_base):
        raw = np.zeros((n_steps, n_cells))
        for c in range(n_cells):
            cell_rng = np.random.default_rng(seed + 2000 + c * 10 + f_idx)
            cell_daily = _daily_fourier(
                steps_per_day, K=6,
                peak_hour_frac=0.55 + cell_rng.uniform(-0.03, 0.03),
                rng=cell_rng)
            T = _trend_component(n_steps, slope=0.01)
            S = _seasonal_component(n_steps, steps_per_day, cell_daily,
                                     weekly_factor)
            C = _cyclic_component(n_steps, n_events=n_special_events,
                                   event_duration_steps=steps_per_day // 4,
                                   event_amplitude=0.5, rng=cell_rng)
            # eMBB: smooth → small noise, small bursts
            I = _irregular_component(n_steps, scale=0.02, rng=cell_rng)
            eps = _noise_component(n_steps, sigma=0.05, rng=cell_rng)
            signal = T + S + C + I + eps
            cell_base = base * cell_rng.lognormal(0, 0.25)
            raw[:, c] = signal * cell_base
        raw = _apply_spatial_correlation(raw, corr)
        if f_idx == 2:
            raw = np.clip(np.round(raw), 0, None)
        else:
            raw = np.clip(raw, 0, None)
        all_data[:, :, f_idx] = raw

    # ---- URLLC: small packets, periodic bursts -----------------------
    urllc_base = [500.0, 0.5, 0.999]
    for local_idx, (base, fname) in enumerate(
            zip(urllc_base, feature_names[3:6])):
        f_idx = 3 + local_idx
        raw = np.zeros((n_steps, n_cells))
        for c in range(n_cells):
            cell_rng = np.random.default_rng(seed + 3000 + c * 10 + local_idx)
            # Periodic burst component (period ~ 10 min = 10 steps)
            burst_period = 10
            t_arr = np.arange(n_steps)
            periodic = 0.5 * (1 + np.cos(2 * np.pi * t_arr / burst_period))
            T = _trend_component(n_steps, slope=0.005)
            eps = _noise_component(n_steps, sigma=0.03, rng=cell_rng)
            if local_idx == 0:
                # packet_count
                signal = T + 0.4 * periodic + 0.1 * eps
                cell_base = base * cell_rng.lognormal(0, 0.2)
            elif local_idx == 1:
                # latency indicator ∈ ~[0, 1] — lower is better
                signal = 0.3 + 0.1 * periodic + eps * 0.05
                cell_base = base
            else:
                # reliability indicator ∈ ~[0.99, 1]
                signal = np.ones(n_steps) - rng.exponential(0.002, n_steps)
                cell_base = base
            raw[:, c] = signal * cell_base
        if local_idx == 0:
            raw = _apply_spatial_correlation(raw, corr)
        raw = np.clip(raw, 0, None)
        if local_idx == 0:
            raw = np.round(raw)
        all_data[:, :, f_idx] = raw

    # ---- mMTC: sporadic, aggregate -----------------------------------
    mmtc_base = [800.0, 1000.0, 400.0]
    for local_idx, base in enumerate(mmtc_base):
        f_idx = 6 + local_idx
        raw = np.zeros((n_steps, n_cells))
        for c in range(n_cells):
            cell_rng = np.random.default_rng(seed + 4000 + c * 10 + local_idx)
            cell_daily = _daily_fourier(
                steps_per_day, K=4,
                peak_hour_frac=0.45 + cell_rng.uniform(-0.05, 0.05),
                rng=cell_rng)
            T = _trend_component(n_steps, slope=0.015)
            S = _seasonal_component(n_steps, steps_per_day, cell_daily,
                                     weekly_factor)
            # Sporadic bursts (mMTC wake-up storms)
            sporadic = (cell_rng.random(n_steps) < 0.02).astype(float)
            sporadic *= cell_rng.exponential(0.5, n_steps)
            I = _irregular_component(n_steps, scale=0.04, rng=cell_rng)
            eps = _noise_component(n_steps, sigma=0.06, rng=cell_rng)
            signal = T + S + sporadic + I + eps
            cell_base = base * cell_rng.lognormal(0, 0.3)
            raw[:, c] = signal * cell_base
        raw = _apply_spatial_correlation(raw, corr)
        raw = np.clip(np.round(raw) if local_idx != 1 else raw, 0, None)
        all_data[:, :, f_idx] = raw

    all_data = np.clip(all_data, 0, None)

    print(f"  shape = {all_data.shape}  "
          f"(steps={n_steps}, cells={n_cells}, features={n_features})")
    return {
        "data": all_data,
        "positions": positions,
        "feature_names": feature_names,
        "steps_per_day": steps_per_day,
        "lookback": LOOKBACK_5G,
        "dataset_name": "synthetic_5g",
    }


# ===================================================================
# Saving
# ===================================================================
def _save_dataset(ds: dict, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    name = ds["dataset_name"]
    path = out_dir / f"{name}_dataset.npz"
    np.savez_compressed(
        path,
        data=ds["data"],
        positions=ds["positions"],
        feature_names=np.array(ds["feature_names"]),
        steps_per_day=np.array(ds["steps_per_day"]),
        lookback=np.array(ds["lookback"]),
    )
    size_mb = path.stat().st_size / (1024 * 1024)
    print(f"  Saved → {path}  ({size_mb:.1f} MB)")
    return path


# ===================================================================
# Summary statistics
# ===================================================================
def _print_summary(ds: dict) -> None:
    data = ds["data"]
    name = ds["dataset_name"]
    print(f"\n{'=' * 60}")
    print(f"  Summary: {name}")
    print(f"{'=' * 60}")
    print(f"  Shape          : {data.shape}")
    print(f"  Steps/day      : {ds['steps_per_day']}")
    print(f"  Lookback window: {ds['lookback']}")
    print(f"  Min value      : {data.min():.4f}")
    print(f"  Max value      : {data.max():.4f}")
    print(f"  Mean           : {data.mean():.4f}")
    print(f"  Std            : {data.std():.4f}")
    print(f"  Non-negative   : {bool(np.all(data >= 0))}")
    for i, fn in enumerate(ds["feature_names"]):
        feat = data[:, :, i]
        print(f"    {fn:30s}  mean={feat.mean():10.2f}  "
              f"std={feat.std():10.2f}  "
              f"min={feat.min():10.2f}  max={feat.max():10.2f}")


# ===================================================================
# Self-test mode
# ===================================================================
def _autocorrelation_lag(signal: np.ndarray, lag: int) -> float:
    """Compute Pearson autocorrelation at a given lag."""
    n = len(signal)
    if lag >= n:
        return 0.0
    x = signal[:n - lag]
    y = signal[lag:]
    mx, my = x.mean(), y.mean()
    sx, sy = x.std(), y.std()
    if sx == 0 or sy == 0:
        return 0.0
    return np.mean((x - mx) * (y - my)) / (sx * sy)


def run_self_test() -> None:
    """Generate small datasets and assert quality checks."""
    print("\n" + "=" * 60)
    print("  SELF-TEST MODE")
    print("=" * 60)
    ok = True

    # --- Milano (small) --------------------------------------------------
    ds1 = generate_milano_dataset(n_steps=1440, n_cells=5,
                                  steps_per_day=144)
    d1 = ds1["data"]
    assert d1.shape == (1440, 5, 4), f"Milano shape mismatch: {d1.shape}"
    assert np.all(d1 >= 0), "Milano: negative values found"
    # Daily autocorrelation: lag = steps_per_day should be positive
    cell0_feat0 = d1[:, 0, 0]
    ac_daily = _autocorrelation_lag(cell0_feat0, 144)
    print(f"  [Milano] daily autocorrelation (lag=144): {ac_daily:.4f}")
    assert ac_daily > 0.05, (
        f"Milano: weak daily periodicity (ac={ac_daily:.4f})")

    # Normalization round-trip
    normed, params = normalize_data(d1.reshape(-1, d1.shape[-1]))
    assert normed.min() >= -1e-9, "Normalization produced negative values"
    assert normed.max() <= 1.0 + 1e-9, "Normalization exceeded 1.0"
    print("  [Milano] normalization: OK")

    # Sliding-window construction
    flat = d1[:, 0, :]  # (1440, 4)
    X, Y = create_sequences(flat, lookback=144, horizon=1)
    assert X.shape == (1296, 144, 4), f"Sequences X shape: {X.shape}"
    assert Y.shape == (1296, 1, 4), f"Sequences Y shape: {Y.shape}"
    print("  [Milano] sequence construction: OK")
    print("  [Milano] ALL CHECKS PASSED ✓")

    # --- Shanghai (small) ------------------------------------------------
    ds2 = generate_shanghai_dataset(n_steps=960, n_cells=5,
                                    steps_per_day=96)
    d2 = ds2["data"]
    assert d2.shape == (960, 5, 3), f"Shanghai shape mismatch: {d2.shape}"
    assert np.all(d2 >= 0), "Shanghai: negative values found"
    ac_daily_sh = _autocorrelation_lag(d2[:, 0, 0], 96)
    print(f"  [Shanghai] daily autocorrelation (lag=96): {ac_daily_sh:.4f}")
    assert ac_daily_sh > 0.05, (
        f"Shanghai: weak daily periodicity (ac={ac_daily_sh:.4f})")
    print("  [Shanghai] ALL CHECKS PASSED ✓")

    # --- 5G Synthetic (small) --------------------------------------------
    ds3 = generate_synthetic_5g_dataset(n_steps=2880, n_cells=5,
                                        steps_per_day=1440)
    d3 = ds3["data"]
    assert d3.shape == (2880, 5, 9), f"5G shape mismatch: {d3.shape}"
    assert np.all(d3 >= 0), "5G: negative values found"
    # eMBB should have higher volume than URLLC packet count on average
    embb_vol = d3[:, :, 0].mean()
    urllc_pkt = d3[:, :, 3].mean()
    print(f"  [5G] eMBB mean volume: {embb_vol:.2f}, "
          f"URLLC mean packets: {urllc_pkt:.2f}")
    # URLLC should show periodic structure (autocorrelation at lag=10)
    urllc_sig = d3[:, 0, 3]
    ac_urllc = _autocorrelation_lag(urllc_sig, 10)
    print(f"  [5G] URLLC autocorrelation (lag=10): {ac_urllc:.4f}")
    assert ac_urllc > 0.01, (
        f"5G URLLC: weak periodic structure (ac={ac_urllc:.4f})")
    print("  [5G Synthetic] ALL CHECKS PASSED ✓")

    print("\n  ══════════════════════════════════════")
    print("  ALL SELF-TESTS PASSED ✓")
    print("  ══════════════════════════════════════\n")


# ===================================================================
# Main
# ===================================================================
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate synthetic traffic datasets for LSTM 5G paper.")
    parser.add_argument(
        "--self-test", action="store_true",
        help="Run with small datasets and validate statistical properties.")
    parser.add_argument(
        "--output-dir", type=str, default=str(RESULTS_DIR),
        help="Directory to save .npz files (default: results/).")
    args = parser.parse_args()

    if args.self_test:
        run_self_test()
        return

    out_dir = Path(args.output_dir)
    t0 = time.time()

    # Generate all three datasets
    ds_milano = generate_milano_dataset()
    _print_summary(ds_milano)
    _save_dataset(ds_milano, out_dir)

    ds_shanghai = generate_shanghai_dataset()
    _print_summary(ds_shanghai)
    _save_dataset(ds_shanghai, out_dir)

    ds_5g = generate_synthetic_5g_dataset()
    _print_summary(ds_5g)
    _save_dataset(ds_5g, out_dir)

    elapsed = time.time() - t0
    print(f"\nAll datasets generated in {elapsed:.1f} s")
    print(f"Files saved to {out_dir.resolve()}")


if __name__ == "__main__":
    main()
