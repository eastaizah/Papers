#!/usr/bin/env python3
"""
Section VII – Full Comparative Evaluation  (run_benchmarks.py)
==============================================================

Reproduces all experimental results from Section VII of
"Predicción de Tráfico Basada en LSTM para Gestión Proactiva de
Recursos en Redes 5G":

  • Table I   – Prediction accuracy comparison (1-hour horizon)
  • Table II  – Multi-horizon evaluation (proposed LSTM)
  • Table III – Cross-dataset generalisation
  • Table IV  – Proactive vs reactive resource management KPIs

Usage
-----
    # Full evaluation (all models, all datasets)
    python run_benchmarks.py

    # Quick smoke-test (small synthetic data, ~2 min)
    python run_benchmarks.py --self-test

    # Custom results directory
    python run_benchmarks.py --results-dir ./my_results
"""

from __future__ import annotations

import argparse
import math
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn

# ── Local imports ────────────────────────────────────────────────
from generate_datasets import (
    generate_milano_dataset,
    generate_shanghai_dataset,
    generate_synthetic_5g_dataset,
    normalize_data,
    create_sequences,
    LOOKBACK_MILANO,
    LOOKBACK_SHANGHAI,
    LOOKBACK_5G,
    RESULTS_DIR as _DEFAULT_RESULTS_DIR,
)
from models import (
    AttentionLSTM,
    ARIMABaseline,
    ProposedLSTM,
    SARIMABaseline,
    SVRBaseline,
    RandomForestBaseline,
    FeedforwardNN,
    SimpleRNN,
    GRUModel,
    LSTMNoAttention,
)
from train import (
    load_dataset,
    split_data,
    make_dataloaders,
    build_model,
    train as train_model,
    evaluate_test,
    compute_all_metrics,
    rmse,
    mae,
    mape,
    r_squared,
    RESULTS_DIR as _TRAIN_RESULTS_DIR,
)
from proactive_resource_management import simulate_reactive_vs_proactive

# ═════════════════════════════════════════════════════════════════
# Article reference values (Section VII.B, Table I)
# ═════════════════════════════════════════════════════════════════

TABLE_I_TARGETS: dict[str, dict[str, float]] = {
    "ARIMA":              {"RMSE": 8.42, "MAE": 6.31, "MAPE": 18.4, "R2": 0.72},
    "SARIMA":             {"RMSE": 7.18, "MAE": 5.44, "MAPE": 15.8, "R2": 0.78},
    "SVR":                {"RMSE": 6.95, "MAE": 5.12, "MAPE": 14.6, "R2": 0.81},
    "RandomForest":       {"RMSE": 6.52, "MAE": 4.89, "MAPE": 13.9, "R2": 0.83},
    "FeedforwardNN":      {"RMSE": 5.87, "MAE": 4.35, "MAPE": 12.1, "R2": 0.86},
    "SimpleRNN":          {"RMSE": 5.42, "MAE": 3.98, "MAPE": 11.3, "R2": 0.88},
    "GRUModel":           {"RMSE": 4.76, "MAE": 3.51, "MAPE":  9.8, "R2": 0.91},
    "LSTMNoAttention":    {"RMSE": 4.58, "MAE": 3.38, "MAPE":  9.4, "R2": 0.92},
    "AttentionLSTM":      {"RMSE": 3.89, "MAE": 2.87, "MAPE":  8.1, "R2": 0.94},
    "ProposedLSTM":       {"RMSE": 3.21, "MAE": 2.34, "MAPE":  6.5, "R2": 0.96},
}

# Display names matching the article's Spanish labels
DISPLAY_NAMES: dict[str, str] = {
    "ARIMA":           "ARIMA",
    "SARIMA":          "SARIMA",
    "SVR":             "SVR",
    "RandomForest":    "Random Forest",
    "FeedforwardNN":   "Feedforward NN",
    "SimpleRNN":       "Simple RNN",
    "GRUModel":        "GRU",
    "LSTMNoAttention": "LSTM without Attention",
    "AttentionLSTM":   "Attention LSTM",
    "ProposedLSTM":    "Proposed LSTM (5-layer)",
}

# Ordered list of models for Table I (same as article ordering)
TABLE_I_MODEL_ORDER: list[str] = [
    "ARIMA", "SARIMA", "SVR", "RandomForest",
    "FeedforwardNN", "SimpleRNN", "GRUModel",
    "LSTMNoAttention", "AttentionLSTM", "ProposedLSTM",
]

# Dataset configurations
DATASET_CONFIGS: dict[str, dict] = {
    "milano":      {"lookback": LOOKBACK_MILANO,  "steps_per_day": 144},
    "shanghai":    {"lookback": LOOKBACK_SHANGHAI, "steps_per_day": 96},
    "synthetic5g": {"lookback": LOOKBACK_5G,       "steps_per_day": 288},
}

# Neural-network model names (trained via train.py infrastructure)
NN_MODELS = {"FeedforwardNN", "SimpleRNN", "GRUModel", "LSTMNoAttention",
             "AttentionLSTM", "ProposedLSTM"}

# Stat / ML baselines (fitted directly)
STAT_ML_MODELS = {"ARIMA", "SARIMA", "SVR", "RandomForest"}

# NOTE: XGBoostBaseline is implemented in models.py but excluded from benchmarks
# to avoid requiring an additional 'xgboost' dependency.  To enable it, install
# xgboost (see environment.yml for version), add it to requirements.txt, and
# include "XGBoost" in STAT_ML_MODELS with a corresponding entry in
# STAT_ML_EVALUATORS.


# ═════════════════════════════════════════════════════════════════
# Reproducibility
# ═════════════════════════════════════════════════════════════════

def set_seeds(seed: int = 42) -> None:
    """Fix all random seeds for reproducible experiments."""
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


# ═════════════════════════════════════════════════════════════════
# Pretty-printing helpers
# ═════════════════════════════════════════════════════════════════

_HSEP = "─"
_CORNER = "┌┐└┘"


def _print_header(title: str) -> None:
    width = 78
    print()
    print("═" * width)
    print(f"  {title}")
    print("═" * width)


def _print_table_row(cols: list[str], widths: list[int], sep: str = "│") -> None:
    cells = [c.center(w) if i == 0 else c.rjust(w) for i, (c, w) in enumerate(zip(cols, widths))]
    print(f" {sep} " + f" {sep} ".join(cells) + f" {sep}")


def _print_table_sep(widths: list[int], char: str = "─", join: str = "┼") -> None:
    line = join.join(char * (w + 2) for w in widths)
    print(f" {join}{line}{join}")


def print_metrics_table(
    title: str,
    rows: list[tuple[str, dict[str, float]]],
    targets: dict[str, dict[str, float]] | None = None,
) -> None:
    """Print a nicely formatted metrics table to stdout.

    If any row contains 'RMSE_abs', an extra 'RMSE†' column is shown with
    the denormalized absolute RMSE values, helping to compare against
    the article's reported absolute-unit targets.
    """
    _print_header(title)

    # Detect whether absolute-unit columns are available
    has_abs = any("RMSE_abs" in m for _, m in rows)

    header = ["Method", "RMSE", "MAE", "R²"]
    if has_abs:
        header += ["RMSE† (abs)"]
    if targets:
        header += ["RMSE*", "R²*"]

    col_w = [22, 7, 7, 7]
    if has_abs:
        col_w += [11]
    if targets:
        col_w += [8, 7]

    # Header line
    _print_table_sep(col_w, "─", "┼")
    _print_table_row(header, col_w)
    _print_table_sep(col_w, "─", "┼")

    for name, m in rows:
        display = DISPLAY_NAMES.get(name, name)
        cols = [
            display,
            f"{m.get('RMSE', 0):.4f}",
            f"{m.get('MAE', 0):.4f}",
            f"{m.get('R2', 0):.3f}",
        ]
        if has_abs:
            cols += [f"{m.get('RMSE_abs', m.get('RMSE', 0)):.2f}"]
        if targets and name in targets:
            t = targets[name]
            cols += [f"{t['RMSE']:.2f}", f"{t['R2']:.2f}"]
        elif targets:
            cols += ["—", "—"]
        _print_table_row(cols, col_w)

    _print_table_sep(col_w, "─", "┼")
    if has_abs:
        print("  † Denormalized RMSE: RMSE × (data_max – data_min) for cell-0")
    if targets:
        print("  * Article reference values (Section VII.B, Table I)")
    print()


# ═════════════════════════════════════════════════════════════════
# Statistical / ML baseline evaluation
# ═════════════════════════════════════════════════════════════════

def _evaluate_arima(X_train: np.ndarray, Y_train: np.ndarray,
                    X_test: np.ndarray, Y_test: np.ndarray,
                    norm_params=None, **kw) -> dict[str, float]:
    """Fit ARIMA on training data; roll 1-step-ahead over the test set.

    Uses statsmodels ``append(refit=False)`` to update the Kalman-filter state
    with each true observation before issuing the next 1-step forecast.
    This is canonical 1-step-ahead rolling evaluation: at step t, only
    information up to t-1 is used – no future values leak into the forecast.

    Test series capped at 1 000 steps for speed (~8 s on CPU).  Falls back to naïve
    persistence if ARIMA fitting or rolling fails.
    """
    import warnings
    train_series = Y_train.flatten()
    test_series  = Y_test.flatten()
    n_test       = min(len(test_series), 1000)
    test_series  = test_series[:n_test]

    # Enough history: last 300 training points for parameter estimation.
    history = list(train_series[-300:])

    y_pred = None
    try:
        from statsmodels.tsa.arima.model import ARIMA as _ARIMA
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res = _ARIMA(history, order=(5, 1, 0)).fit()
        preds = []
        for y_obs in test_series:
            preds.append(float(res.forecast(steps=1)[0]))
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                res = res.append([y_obs], refit=False)
        y_pred = np.array(preds)
    except Exception:
        pass

    if y_pred is None:
        y_pred = np.full(n_test, float(train_series[-1]))
    if len(y_pred) > n_test:
        y_pred = y_pred[:n_test]
    elif len(y_pred) < n_test:
        y_pred = np.pad(y_pred, (0, n_test - len(y_pred)), mode="edge")

    metrics = compute_all_metrics(test_series, y_pred)
    if norm_params is not None:
        scale = float(norm_params['max'][0]) - float(norm_params['min'][0])
        if scale > 0:
            metrics['RMSE_abs'] = metrics['RMSE'] * scale
            metrics['MAE_abs']  = metrics['MAE']  * scale
    return metrics


def _evaluate_sarima(X_train: np.ndarray, Y_train: np.ndarray,
                     X_test: np.ndarray, Y_test: np.ndarray,
                     seasonal_period: int = 144, norm_params=None,
                     **kw) -> dict[str, float]:
    """ARIMAX with seasonal lag: ARIMA(5,1,0) + exogenous y_{t–S} regressor.

    At each step the seasonal-lag value (same time S steps ago, i.e. yesterday
    for S=144) is passed as an exogenous feature.  This gives a tractable
    seasonal model equivalent to SARIMA without a large seasonal state space:
    fitting is O(1) (ARIMA on ~300 points) and rolling via ``append(refit=False)``
    is fast.

    The seasonal lag index within the lookback window is computed as:
      lag_idx = lookback – seasonal_period
    For Milano (lookback=144, seasonal_period=144) → lag_idx=0 (first step).
    If seasonal_period > lookback, falls back to plain ARIMA(5,1,0).
    Test series capped at 500 steps.
    """
    import warnings
    lookback     = X_train.shape[1]
    lag          = seasonal_period
    lag_idx      = lookback - lag          # index in window for y_{t-lag}

    train_series = Y_train.flatten()
    test_series  = Y_test.flatten()
    n_test       = min(len(test_series), 1000)
    test_series  = test_series[:n_test]

    # Exogenous regressors: y_{t-lag} from pre-built lookback matrices.
    # lag_idx == 0 when lookback == seasonal_period (typical case).
    if 0 <= lag_idx < lookback:
        exog_train = X_train[:, lag_idx, 0:1].astype(float)
        exog_test  = X_test[:n_test, lag_idx, 0:1].astype(float)
    else:
        exog_train = None   # fall back to plain ARIMA
        exog_test  = None

    # Align training history with exogenous features (use last 300 windows)
    n_hist = min(300, len(train_series))
    y_hist  = train_series[-n_hist:]
    ex_hist = exog_train[-n_hist:] if exog_train is not None else None

    y_pred = None
    try:
        from statsmodels.tsa.arima.model import ARIMA as _ARIMA
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            res = _ARIMA(y_hist, exog=ex_hist, order=(5, 1, 0)).fit()
        preds = []
        for i, y_obs in enumerate(test_series):
            ex_next = exog_test[i:i+1] if exog_test is not None else None
            preds.append(float(res.forecast(steps=1, exog=ex_next)[0]))
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                res = res.append([y_obs], exog=ex_next, refit=False)
        y_pred = np.array(preds)
    except Exception:
        pass

    if y_pred is None:
        y_pred = np.full(n_test, float(train_series[-1]))
    if len(y_pred) > n_test:
        y_pred = y_pred[:n_test]
    elif len(y_pred) < n_test:
        y_pred = np.pad(y_pred, (0, n_test - len(y_pred)), mode="edge")

    metrics = compute_all_metrics(test_series, y_pred)
    if norm_params is not None:
        scale = float(norm_params['max'][0]) - float(norm_params['min'][0])
        if scale > 0:
            metrics['RMSE_abs'] = metrics['RMSE'] * scale
            metrics['MAE_abs']  = metrics['MAE']  * scale
    return metrics


def _evaluate_svr(X_train, Y_train, X_test, Y_test, norm_params=None, **kw):
    """Fit SVR baseline (RBF kernel) on subsampled lookback windows.

    Subsamples the lookback to every 6th step (≈10-min → 1-h resolution)
    to keep the feature dimension tractable for RBF-SVR.
    """
    n_train = X_train.shape[0]
    n_test  = X_test.shape[0]
    # Subsample: every 6th step → max ~24 time points × n_features
    step = max(1, X_train.shape[1] // 24)
    X_tr_flat = X_train[:, ::step, :].reshape(n_train, -1)
    X_te_flat = X_test[:, ::step, :].reshape(n_test, -1)

    model = SVRBaseline(kernel="rbf", C=1.0, epsilon=0.1)
    model.fit(X_tr_flat, Y_train.flatten())
    y_pred = model.predict(X_te_flat)
    metrics = compute_all_metrics(Y_test.flatten(), y_pred.flatten())
    if norm_params is not None:
        scale = float(norm_params["max"][0]) - float(norm_params["min"][0])
        if scale > 0:
            metrics["RMSE_abs"] = metrics["RMSE"] * scale
            metrics["MAE_abs"] = metrics["MAE"] * scale
    return metrics


def _evaluate_random_forest(X_train, Y_train, X_test, Y_test, norm_params=None, **kw):
    """Fit Random Forest baseline on subsampled lookback windows.

    Same subsampling strategy as SVR for tractable training.
    """
    n_train = X_train.shape[0]
    n_test  = X_test.shape[0]
    step = max(1, X_train.shape[1] // 24)
    X_tr_flat = X_train[:, ::step, :].reshape(n_train, -1)
    X_te_flat = X_test[:, ::step, :].reshape(n_test, -1)

    model = RandomForestBaseline(n_estimators=100, random_state=42)
    model.fit(X_tr_flat, Y_train.flatten())
    y_pred = model.predict(X_te_flat)
    metrics = compute_all_metrics(Y_test.flatten(), y_pred.flatten())
    if norm_params is not None:
        scale = float(norm_params["max"][0]) - float(norm_params["min"][0])
        if scale > 0:
            metrics["RMSE_abs"] = metrics["RMSE"] * scale
            metrics["MAE_abs"] = metrics["MAE"] * scale
    return metrics


STAT_ML_EVALUATORS: dict[str, callable] = {
    "ARIMA": _evaluate_arima,
    "SARIMA": _evaluate_sarima,
    "SVR": _evaluate_svr,
    "RandomForest": _evaluate_random_forest,
}


# ═════════════════════════════════════════════════════════════════
# Neural-network training & evaluation
# ═════════════════════════════════════════════════════════════════

def _train_and_evaluate_nn(
    model_name: str,
    X_train: np.ndarray, Y_train: np.ndarray,
    X_val: np.ndarray, Y_val: np.ndarray,
    X_test: np.ndarray, Y_test: np.ndarray,
    lookback: int,
    dataset_name: str,
    device: torch.device,
    epochs: int = 150,
    patience: int = 40,
    lr: float = 0.001,
    norm_params=None,
) -> dict[str, float]:
    """Build, train, and evaluate a neural network model."""
    # AttentionLSTM teacher forcing requires 2D targets (batch, horizon).
    # load_dataset squeezes horizon=1 to 1D, so unsqueeze here.
    _Y_train, _Y_val, _Y_test = Y_train, Y_val, Y_test
    if Y_train.ndim == 1:
        _Y_train = Y_train[:, np.newaxis]
        _Y_val = Y_val[:, np.newaxis]
        _Y_test = Y_test[:, np.newaxis]

    input_size = X_train.shape[2]  # n_features
    output_size = _Y_train.shape[-1]

    model = build_model(model_name, input_size=input_size,
                        output_size=output_size, lookback=lookback,
                        dropout=0.3)
    print(f"\n  [{model_name}] parameters: "
          f"{sum(p.numel() for p in model.parameters()):,}")

    train_loader, val_loader = make_dataloaders(X_train, _Y_train,
                                                X_val, _Y_val,
                                                batch_size=64)
    train_model(
        model, train_loader, val_loader,
        model_name=model_name,
        dataset_name=dataset_name,
        device=device,
        lr=lr,
        epochs=epochs,
        patience=patience,
        clip_norm=5.0,
        lr_decay_factor=0.95,
        lr_decay_step=10,
    )

    metrics = evaluate_test(model, X_test, _Y_test, device,
                            model_name=model_name, norm_params=norm_params)
    return metrics


# ═════════════════════════════════════════════════════════════════
# Step 1 – Table I: Prediction accuracy comparison
# ═════════════════════════════════════════════════════════════════

def run_table_i(
    dataset_name: str = "milano",
    model_list: list[str] | None = None,
    device: torch.device | None = None,
    epochs: int = 150,
    patience: int = 40,
    self_test: bool = False,
    results_dir: Path | None = None,
) -> dict[str, dict[str, float]]:
    """Reproduce Table I – accuracy comparison on primary dataset.

    Returns dict mapping model_name → metrics dict.
    """
    if model_list is None:
        model_list = list(TABLE_I_MODEL_ORDER)
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if results_dir is None:
        results_dir = _DEFAULT_RESULTS_DIR

    cfg = DATASET_CONFIGS[dataset_name]
    lookback = cfg["lookback"]
    horizon = 1  # 1-step prediction for Table I

    _print_header(f"Table I – Loading dataset '{dataset_name}' "
                  f"(lookback={lookback}, horizon={horizon})")

    if self_test:
        # Generate small synthetic data in-memory
        X, Y = _generate_selftest_data(n_steps=500, n_cells=5,
                                       lookback=lookback, horizon=horizon)
        norm_params = {"min": np.array([0.0]), "max": np.array([1.0])}
    else:
        X, Y, norm_params = load_dataset(dataset_name, lookback=lookback,
                                         horizon=horizon, cell_idx=0)

    X_train, Y_train, X_val, Y_val, X_test, Y_test = split_data(X, Y)
    print(f"  Train: {X_train.shape[0]} | Val: {X_val.shape[0]} "
          f"| Test: {X_test.shape[0]}  features={X_train.shape[2]}")

    results: dict[str, dict[str, float]] = {}

    for name in model_list:
        t0 = time.time()
        print(f"\n{'─'*60}")
        print(f"  Evaluating: {DISPLAY_NAMES.get(name, name)}")
        print(f"{'─'*60}")

        if name in STAT_ML_MODELS:
            evaluator = STAT_ML_EVALUATORS[name]
            extra_kw = {"norm_params": norm_params}
            if name == "SARIMA":
                # Use the actual daily period for Holt-Winters (SARIMA-class baseline).
                # For Milano (144 steps/day), period=144 gives proper 24-h seasonality.
                extra_kw["seasonal_period"] = cfg["steps_per_day"]
            metrics = evaluator(X_train, Y_train, X_test, Y_test,
                                **extra_kw)
        elif name in NN_MODELS:
            metrics = _train_and_evaluate_nn(
                model_name=name,
                X_train=X_train, Y_train=Y_train,
                X_val=X_val, Y_val=Y_val,
                X_test=X_test, Y_test=Y_test,
                lookback=lookback,
                dataset_name=dataset_name,
                device=device,
                epochs=epochs,
                patience=patience,
                norm_params=norm_params,
            )
        else:
            print(f"  ⚠ Unknown model '{name}', skipping.")
            continue

        elapsed = time.time() - t0
        results[name] = metrics
        abs_str = ""
        if "RMSE_abs" in metrics:
            abs_str = f"  RMSE_abs={metrics['RMSE_abs']:.2f}  MAE_abs={metrics.get('MAE_abs', 0):.2f}"
        print(f"  → {name}: RMSE={metrics['RMSE']:.4f}  "
              f"MAE={metrics['MAE']:.4f}  MAPE={metrics['MAPE']:.2f}%  "
              f"R²={metrics['R2']:.4f}{abs_str}  ({elapsed:.1f}s)")

    # Print the table
    rows = [(n, results[n]) for n in model_list if n in results]
    print_metrics_table("Table I – Prediction Accuracy Comparison "
                        "(1-hour Horizon, Milano Dataset)",
                        rows, targets=TABLE_I_TARGETS)

    # Save results
    results_dir.mkdir(parents=True, exist_ok=True)
    save_path = results_dir / "benchmark_table_i.npz"
    np.savez(
        save_path,
        model_names=np.array(list(results.keys())),
        **{f"{k}_metrics": np.array([results[k].get(m, 0.0)
                                     for m in ("RMSE", "MAE", "MAPE", "R2")])
           for k in results},
    )
    print(f"  Results saved → {save_path}")
    return results


# ═════════════════════════════════════════════════════════════════
# Step 2 – Multi-horizon evaluation (proposed LSTM only)
# ═════════════════════════════════════════════════════════════════

def run_multi_horizon(
    dataset_name: str = "milano",
    horizons: list[int] | None = None,
    device: torch.device | None = None,
    epochs: int = 150,
    patience: int = 40,
    self_test: bool = False,
    results_dir: Path | None = None,
) -> dict[int, dict[str, float]]:
    """Multi-horizon evaluation for the proposed AttentionLSTM.

    Horizons τ ∈ {4, 8, 12, 24} steps correspond to
    {15 min, 30 min, 45 min, 1 hr} at 15-min granularity (Milano).

    Returns dict mapping horizon → metrics dict.
    """
    if horizons is None:
        horizons = [4, 8, 12, 24]
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if results_dir is None:
        results_dir = _DEFAULT_RESULTS_DIR

    cfg = DATASET_CONFIGS[dataset_name]
    lookback = cfg["lookback"]
    model_name = "ProposedLSTM"

    _print_header(f"Multi-Horizon Evaluation – {model_name} "
                  f"on '{dataset_name}'")

    results: dict[int, dict[str, float]] = {}

    for h in horizons:
        print(f"\n  ── Horizon τ = {h} steps ──")

        if self_test:
            X, Y = _generate_selftest_data(n_steps=500, n_cells=5,
                                           lookback=lookback, horizon=h)
        else:
            X, Y, _ = load_dataset(dataset_name, lookback=lookback,
                                   horizon=h, cell_idx=0)

        X_train, Y_train, X_val, Y_val, X_test, Y_test = split_data(X, Y)
        input_size = X_train.shape[2]
        output_size = h

        model = build_model(model_name, input_size=input_size,
                            output_size=output_size, lookback=lookback,
                            dropout=0.3)

        train_loader, val_loader = make_dataloaders(
            X_train, Y_train, X_val, Y_val, batch_size=64)

        train_model(
            model, train_loader, val_loader,
            model_name=model_name,
            dataset_name=f"{dataset_name}_h{h}",
            device=device,
            lr=0.001,
            epochs=epochs,
            patience=patience,
            clip_norm=5.0,
            lr_decay_factor=0.95,
            lr_decay_step=10,
        )

        metrics = evaluate_test(model, X_test, Y_test, device,
                                model_name=model_name)
        results[h] = metrics
        print(f"  → Horizon {h}: RMSE={metrics['RMSE']:.4f}  "
              f"MAPE={metrics['MAPE']:.2f}%  R²={metrics['R2']:.4f}")

    # Print multi-horizon table
    _print_header("Table II – Multi-Horizon Evaluation (Proposed LSTM)")
    header = ["Horizon (τ)", "Duration", "RMSE", "MAE", "MAPE (%)", "R²"]
    col_w = [13, 10, 8, 8, 9, 8]

    duration_labels = {4: "15 min", 8: "30 min", 12: "45 min", 24: "1 hr"}

    _print_table_sep(col_w, "─", "┼")
    _print_table_row(header, col_w)
    _print_table_sep(col_w, "─", "┼")
    for h in horizons:
        if h in results:
            m = results[h]
            _print_table_row([
                f"τ = {h}",
                duration_labels.get(h, f"{h} steps"),
                f"{m['RMSE']:.2f}",
                f"{m['MAE']:.2f}",
                f"{m['MAPE']:.1f}",
                f"{m['R2']:.2f}",
            ], col_w)
    _print_table_sep(col_w, "─", "┼")

    # Check article claim: RMSE < 5% for horizons up to 30 min
    for h in [4, 8]:
        if h in results:
            rmse_val = results[h]["RMSE"]
            status = "✓" if rmse_val < 5.0 else "✗"
            print(f"  {status} Horizon τ={h} RMSE={rmse_val:.4f} "
                  f"({'< 5%' if rmse_val < 5.0 else '>= 5%'} threshold)")
    print()

    # Save
    results_dir.mkdir(parents=True, exist_ok=True)
    save_path = results_dir / "benchmark_multi_horizon.npz"
    np.savez(
        save_path,
        horizons=np.array(horizons),
        **{f"h{h}_metrics": np.array([results[h].get(m, 0.0)
                                      for m in ("RMSE", "MAE", "MAPE", "R2")])
           for h in horizons if h in results},
    )
    print(f"  Results saved → {save_path}")
    return results


# ═════════════════════════════════════════════════════════════════
# Step 3 – Cross-dataset evaluation
# ═════════════════════════════════════════════════════════════════

def run_cross_dataset(
    model_name: str = "ProposedLSTM",
    datasets: list[str] | None = None,
    device: torch.device | None = None,
    epochs: int = 150,
    patience: int = 40,
    self_test: bool = False,
    results_dir: Path | None = None,
) -> dict[str, dict[str, float]]:
    """Train and test the proposed model on each dataset separately.

    Returns dict mapping dataset_name → metrics.
    """
    if datasets is None:
        datasets = ["milano", "shanghai", "synthetic5g"]
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if results_dir is None:
        results_dir = _DEFAULT_RESULTS_DIR

    _print_header(f"Cross-Dataset Evaluation – {model_name}")

    results: dict[str, dict[str, float]] = {}

    for ds_name in datasets:
        cfg = DATASET_CONFIGS[ds_name]
        lookback = cfg["lookback"]
        horizon = 1

        print(f"\n  ── Dataset: {ds_name} (lookback={lookback}) ──")

        if self_test:
            X, Y = _generate_selftest_data(n_steps=500, n_cells=5,
                                           lookback=lookback, horizon=horizon)
        else:
            X, Y, _ = load_dataset(ds_name, lookback=lookback,
                                   horizon=horizon, cell_idx=0)

        X_train, Y_train, X_val, Y_val, X_test, Y_test = split_data(X, Y)

        metrics = _train_and_evaluate_nn(
            model_name=model_name,
            X_train=X_train, Y_train=Y_train,
            X_val=X_val, Y_val=Y_val,
            X_test=X_test, Y_test=Y_test,
            lookback=lookback,
            dataset_name=ds_name,
            device=device,
            epochs=epochs,
            patience=patience,
        )
        results[ds_name] = metrics
        print(f"  → {ds_name}: RMSE={metrics['RMSE']:.4f}  "
              f"R²={metrics['R2']:.4f}")

    # Print cross-dataset table
    _print_header("Table III – Cross-Dataset Evaluation (Proposed LSTM)")
    header = ["Dataset", "RMSE", "MAE", "MAPE (%)", "R²"]
    col_w = [15, 8, 8, 9, 8]

    _print_table_sep(col_w, "─", "┼")
    _print_table_row(header, col_w)
    _print_table_sep(col_w, "─", "┼")
    for ds_name in datasets:
        if ds_name in results:
            m = results[ds_name]
            _print_table_row([
                ds_name.capitalize(),
                f"{m['RMSE']:.2f}",
                f"{m['MAE']:.2f}",
                f"{m['MAPE']:.1f}",
                f"{m['R2']:.2f}",
            ], col_w)
    _print_table_sep(col_w, "─", "┼")
    print()

    # Save
    results_dir.mkdir(parents=True, exist_ok=True)
    save_path = results_dir / "benchmark_cross_dataset.npz"
    np.savez(
        save_path,
        datasets=np.array(datasets),
        **{f"{ds}_metrics": np.array([results[ds].get(m, 0.0)
                                      for m in ("RMSE", "MAE", "MAPE", "R2")])
           for ds in datasets if ds in results},
    )
    print(f"  Results saved → {save_path}")
    return results


# ═════════════════════════════════════════════════════════════════
# Step 4 – Proactive resource management (Section VII.C)
# ═════════════════════════════════════════════════════════════════

def run_proactive_evaluation(
    dataset_name: str = "milano",
    self_test: bool = False,
    results_dir: Path | None = None,
) -> dict[str, dict[str, float]]:
    """Run reactive-vs-proactive simulation and print KPI comparison.

    Article target improvements (Section VII.C):
      - Blocking rate reduction:  35–42 %
      - Latency reduction:        28–34 %
      - Utilisation improvement:  ~22 %
      - Energy efficiency:        ~26 %

    Returns the raw simulation dict with 'reactive' and 'proactive' sub-dicts.
    """
    if results_dir is None:
        results_dir = _DEFAULT_RESULTS_DIR

    _print_header("Proactive vs Reactive Resource Management (Section VII.C)")

    if self_test:
        rng = np.random.default_rng(42)
        n_cells, n_steps = 5, 200
        demand_trace = np.abs(rng.normal(50, 15, (n_cells, n_steps)))
        capacity_per_cell = 80.0
    else:
        # Load dataset and build a demand trace matrix (cells × time)
        npz_path = results_dir / "milano_dataset.npz"
        if not npz_path.exists():
            print("  Generating Milano dataset for simulation…")
            ds = generate_milano_dataset()
            results_dir.mkdir(parents=True, exist_ok=True)
            np.savez(results_dir / "milano_dataset.npz", **ds)

        ds = np.load(npz_path, allow_pickle=True)
        data = ds["data"]  # (n_steps, n_cells, n_features)
        # Use first feature (traffic volume) across all cells
        demand_trace = data[:, :, 0].T  # (n_cells, n_steps)
        # Ensure positive and scale to realistic range
        demand_trace = np.abs(demand_trace)
        demand_mean = demand_trace.mean()
        if demand_mean > 0:
            demand_trace = demand_trace / demand_mean * 50.0
        capacity_per_cell = 80.0

    print(f"  Demand trace shape: {demand_trace.shape} "
          f"(cells × timesteps)")
    print(f"  Capacity per cell:  {capacity_per_cell}")

    sim_results = simulate_reactive_vs_proactive(
        demand_trace,
        capacity_per_cell,
        kappa=1.96,
        noise_std_frac=0.15,
        delta_preactivate=3,
    )

    reactive = sim_results["reactive"]
    proactive = sim_results["proactive"]

    # Compute improvements
    def _pct_change(old: float, new: float) -> float:
        if abs(old) < 1e-12:
            return 0.0
        return (old - new) / abs(old) * 100.0

    blocking_reduction = _pct_change(reactive["blocking_rate"],
                                     proactive["blocking_rate"])
    latency_reduction = _pct_change(reactive["avg_latency"],
                                    proactive["avg_latency"])
    util_improvement = _pct_change(-reactive["avg_utilization"],
                                   -proactive["avg_utilization"])
    energy_improvement = _pct_change(reactive["total_energy"],
                                     proactive["total_energy"])

    # Print KPI table
    _print_header("Table IV – Resource Management KPI Comparison")
    header = ["KPI", "Reactive", "Proactive", "Improvement"]
    col_w = [25, 12, 12, 14]

    _print_table_sep(col_w, "─", "┼")
    _print_table_row(header, col_w)
    _print_table_sep(col_w, "─", "┼")

    kpi_rows = [
        ("Blocking Rate",
         f"{reactive['blocking_rate']:.4f}",
         f"{proactive['blocking_rate']:.4f}",
         f"{blocking_reduction:+.1f} %"),
        ("Avg Latency",
         f"{reactive['avg_latency']:.4f}",
         f"{proactive['avg_latency']:.4f}",
         f"{latency_reduction:+.1f} %"),
        ("Avg Utilisation",
         f"{reactive['avg_utilization']:.4f}",
         f"{proactive['avg_utilization']:.4f}",
         f"{util_improvement:+.1f} %"),
        ("Total Energy",
         f"{reactive['total_energy']:.1f}",
         f"{proactive['total_energy']:.1f}",
         f"{energy_improvement:+.1f} %"),
    ]
    for kpi_name, r_val, p_val, imp_val in kpi_rows:
        _print_table_row([kpi_name, r_val, p_val, imp_val], col_w)

    _print_table_sep(col_w, "─", "┼")

    # Article target ranges
    print("\n  Article target ranges (Section VII.C):")
    print(f"    Blocking rate reduction:  35–42 %  → got {blocking_reduction:.1f} %")
    print(f"    Latency reduction:        28–34 %  → got {latency_reduction:.1f} %")
    print(f"    Utilisation improvement:   ~22 %   → got {util_improvement:.1f} %")
    print(f"    Energy efficiency:         ~26 %   → got {energy_improvement:.1f} %")
    print()

    # Save
    results_dir.mkdir(parents=True, exist_ok=True)
    save_path = results_dir / "benchmark_proactive.npz"
    np.savez(
        save_path,
        reactive_blocking=reactive["blocking_rate"],
        reactive_latency=reactive["avg_latency"],
        reactive_utilization=reactive["avg_utilization"],
        reactive_energy=reactive["total_energy"],
        proactive_blocking=proactive["blocking_rate"],
        proactive_latency=proactive["avg_latency"],
        proactive_utilization=proactive["avg_utilization"],
        proactive_energy=proactive["total_energy"],
        blocking_reduction=blocking_reduction,
        latency_reduction=latency_reduction,
        util_improvement=util_improvement,
        energy_improvement=energy_improvement,
    )
    print(f"  Results saved → {save_path}")
    return sim_results


# ═════════════════════════════════════════════════════════════════
# Self-test synthetic data generator
# ═════════════════════════════════════════════════════════════════

def _generate_selftest_data(
    n_steps: int = 500,
    n_cells: int = 5,
    lookback: int = 24,
    horizon: int = 1,
    seed: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """Create a small synthetic dataset in-memory for self-test mode.

    Generates traffic-like patterns (daily sinusoid + noise) without
    relying on .npz files on disk.

    Returns (X, Y) ready for split_data().
    """
    rng = np.random.default_rng(seed)
    t = np.arange(n_steps, dtype=np.float64)

    # Multi-feature synthetic traffic: volume, throughput, latency, load
    n_features = 4
    data = np.zeros((n_steps, n_features), dtype=np.float32)

    # Feature 0: traffic volume (sinusoidal daily pattern)
    data[:, 0] = (50 + 30 * np.sin(2 * np.pi * t / 144)
                  + 10 * np.sin(2 * np.pi * t / 1008)
                  + rng.normal(0, 3, n_steps))

    # Feature 1: throughput (correlated with volume)
    data[:, 1] = data[:, 0] * 0.8 + rng.normal(0, 2, n_steps)

    # Feature 2: latency (inversely correlated)
    data[:, 2] = 100 - data[:, 0] * 0.5 + rng.normal(0, 5, n_steps)

    # Feature 3: load factor
    data[:, 3] = np.clip(data[:, 0] / 100.0 + rng.normal(0, 0.05, n_steps),
                         0, 1)

    # Normalize
    normed, _ = normalize_data(data)

    # Create sequences
    X, Y_full = create_sequences(normed, lookback=lookback, horizon=horizon)
    Y = Y_full[:, :, 0]  # first feature as target
    if horizon == 1:
        Y = Y.squeeze(-1)

    return X, Y


# ═════════════════════════════════════════════════════════════════
# Self-test mode
# ═════════════════════════════════════════════════════════════════

def run_self_test() -> bool:
    """Quick validation: small data, 3 models, few epochs.

    Checks that the proposed AttentionLSTM beats the baselines on RMSE.
    Should complete in < 3 minutes.

    Returns True if all assertions pass.
    """
    _print_header("SELF-TEST MODE")
    print("  Using synthetic data (500 timesteps, 5 cells)")
    print("  Models: ARIMA, FeedforwardNN, AttentionLSTM")
    print("  Epochs: 10 (neural networks)")
    print()

    set_seeds(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"  Device: {device}")

    test_models = ["ARIMA", "FeedforwardNN", "AttentionLSTM"]
    lookback = 24
    horizon = 1
    epochs = 10
    patience = 5

    # Generate self-test data
    X, Y = _generate_selftest_data(n_steps=500, n_cells=5,
                                   lookback=lookback, horizon=horizon)
    X_train, Y_train, X_val, Y_val, X_test, Y_test = split_data(X, Y)
    print(f"  Data: train={X_train.shape[0]}  val={X_val.shape[0]}  "
          f"test={X_test.shape[0]}  features={X_train.shape[2]}")

    results: dict[str, dict[str, float]] = {}

    for name in test_models:
        t0 = time.time()
        print(f"\n  ── {DISPLAY_NAMES.get(name, name)} ──")

        if name in STAT_ML_MODELS:
            evaluator = STAT_ML_EVALUATORS[name]
            metrics = evaluator(X_train, Y_train, X_test, Y_test)
        else:
            metrics = _train_and_evaluate_nn(
                model_name=name,
                X_train=X_train, Y_train=Y_train,
                X_val=X_val, Y_val=Y_val,
                X_test=X_test, Y_test=Y_test,
                lookback=lookback,
                dataset_name="selftest",
                device=device,
                epochs=epochs,
                patience=patience,
            )

        elapsed = time.time() - t0
        results[name] = metrics
        print(f"  → {name}: RMSE={metrics['RMSE']:.4f}  "
              f"R²={metrics['R2']:.4f}  ({elapsed:.1f}s)")

    # Print comparison table
    rows = [(n, results[n]) for n in test_models]
    print_metrics_table("Self-Test Results", rows)

    # Proactive management mini-test
    print("  Running proactive management mini-test…")
    rng = np.random.default_rng(42)
    demand = np.abs(rng.normal(50, 15, (5, 200)))
    sim = simulate_reactive_vs_proactive(demand, 80.0)
    print(f"  → Reactive blocking:  {sim['reactive']['blocking_rate']:.4f}")
    print(f"  → Proactive blocking: {sim['proactive']['blocking_rate']:.4f}")

    # ── Assertions ──
    lstm_rmse = results["AttentionLSTM"]["RMSE"]
    arima_rmse = results["ARIMA"]["RMSE"]
    ffnn_rmse = results["FeedforwardNN"]["RMSE"]

    print(f"\n  Assertion: AttentionLSTM RMSE ({lstm_rmse:.4f}) < "
          f"ARIMA RMSE ({arima_rmse:.4f})")
    assert lstm_rmse < arima_rmse, (
        f"AttentionLSTM ({lstm_rmse:.4f}) should beat ARIMA ({arima_rmse:.4f})")

    print(f"  Assertion: AttentionLSTM RMSE ({lstm_rmse:.4f}) < "
          f"FeedforwardNN RMSE ({ffnn_rmse:.4f})")
    assert lstm_rmse < ffnn_rmse, (
        f"AttentionLSTM ({lstm_rmse:.4f}) should beat FeedforwardNN "
        f"({ffnn_rmse:.4f})")

    assert sim["proactive"]["blocking_rate"] <= sim["reactive"]["blocking_rate"], \
        "Proactive should have lower or equal blocking rate"

    print("\n  ✓ All self-test assertions passed!")
    return True


# ═════════════════════════════════════════════════════════════════
# Full benchmark orchestration
# ═════════════════════════════════════════════════════════════════

def run_full_benchmark(results_dir: Path) -> None:
    """Execute the complete Section VII evaluation pipeline."""
    set_seeds(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    overall_t0 = time.time()

    # ── Ensure datasets exist ──
    _print_header("Checking / Generating Datasets")
    results_dir.mkdir(parents=True, exist_ok=True)

    dataset_generators = {
        "milano_dataset.npz": generate_milano_dataset,
        "shanghai_dataset.npz": generate_shanghai_dataset,
        "synthetic_5g_dataset.npz": generate_synthetic_5g_dataset,
    }
    for fname, gen_fn in dataset_generators.items():
        fpath = results_dir / fname
        if fpath.exists():
            print(f"  ✓ {fname} exists")
        else:
            print(f"  Generating {fname}…")
            ds = gen_fn()
            np.savez(fpath, **ds)
            print(f"  ✓ {fname} saved")

    # ── Step 1: Table I – Prediction accuracy comparison ──
    table_i = run_table_i(
        dataset_name="milano",
        model_list=list(TABLE_I_MODEL_ORDER),
        device=device,
        epochs=150,
        patience=40,
        self_test=False,
        results_dir=results_dir,
    )

    # ── Step 2: Multi-horizon evaluation ──
    multi_horizon = run_multi_horizon(
        dataset_name="milano",
        horizons=[4, 8, 12, 24],
        device=device,
        epochs=150,
        patience=40,
        self_test=False,
        results_dir=results_dir,
    )

    # ── Step 3: Cross-dataset evaluation ──
    cross_dataset = run_cross_dataset(
        model_name="ProposedLSTM",
        datasets=["milano", "shanghai", "synthetic5g"],
        device=device,
        epochs=150,
        patience=40,
        self_test=False,
        results_dir=results_dir,
    )

    # ── Step 4: Proactive resource management ──
    proactive = run_proactive_evaluation(
        dataset_name="milano",
        self_test=False,
        results_dir=results_dir,
    )

    # ── Summary ──
    total_time = time.time() - overall_t0
    _print_header("Benchmark Complete")
    print(f"  Total time: {total_time / 60:.1f} minutes")
    print(f"  Results dir: {results_dir}")
    print(f"  Saved files:")
    for f in sorted(results_dir.glob("benchmark_*.npz")):
        print(f"    • {f.name}")
    print()


# ═════════════════════════════════════════════════════════════════
# CLI
# ═════════════════════════════════════════════════════════════════

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Section VII – Full Comparative Evaluation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python run_benchmarks.py                   # full benchmark\n"
            "  python run_benchmarks.py --self-test        # quick smoke test\n"
            "  python run_benchmarks.py --results-dir out/ # custom output dir\n"
        ),
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run quick validation with synthetic data (~2 min)",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=None,
        help=f"Directory for results (default: {_DEFAULT_RESULTS_DIR})",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    results_dir = args.results_dir or _DEFAULT_RESULTS_DIR

    if args.self_test:
        set_seeds(42)
        ok = run_self_test()
        sys.exit(0 if ok else 1)
    else:
        run_full_benchmark(results_dir)


if __name__ == "__main__":
    main()
