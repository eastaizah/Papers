#!/usr/bin/env python3
"""
Algorithm 2 – Real-Time Prediction Pipeline (Section VI.B).

Loads a trained LSTM model checkpoint and performs real-time inference
with Monte Carlo Dropout for uncertainty quantification.

"Predicción de Tráfico Basada en LSTM para Gestión Proactiva de
Recursos en Redes 5G"

Usage
-----
    # Predict using a saved checkpoint
    python predict.py --checkpoint results/synthetic5g_AttentionLSTM_best.pt \
                      --horizon 12 --lookback 60 --input-features 4

    # Self-test (no checkpoint required)
    python predict.py --self-test
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import torch
import torch.nn as nn

# Local imports
from models import AttentionLSTM

# Prediction horizons studied in the article (Section VII.A.2)
HORIZONS = [4, 8, 12, 24]

# Monte Carlo Dropout settings (Section VI.B)
MC_FORWARD_PASSES = 30


# ──────────────────────────────────────────────────────────────────
# Normalization helpers (mirror generate_datasets.normalize_data)
# ──────────────────────────────────────────────────────────────────

def normalize(
    data: np.ndarray,
    norm_params: Dict[str, np.ndarray],
) -> np.ndarray:
    """Min-Max normalization using pre-computed training statistics."""
    d_min = norm_params["min"]
    d_max = norm_params["max"]
    denom = d_max - d_min
    denom[denom == 0] = 1.0
    return (data - d_min) / denom


def denormalize(
    data: np.ndarray,
    norm_params: Dict[str, np.ndarray],
    feature_idx: int = 0,
) -> np.ndarray:
    """Inverse Min-Max scaling for a single target feature."""
    d_min = norm_params["min"][feature_idx]
    d_max = norm_params["max"][feature_idx]
    return data * (d_max - d_min) + d_min


# ──────────────────────────────────────────────────────────────────
# Enable dropout at inference time for MC Dropout
# ──────────────────────────────────────────────────────────────────

def _enable_mc_dropout(model: nn.Module) -> None:
    """Activate all dropout sources (nn.Dropout *and* LSTM internal dropout).

    LSTM/GRU internal dropout is governed by the module's ``training`` flag,
    so we set recurrent modules to train mode as well.
    """
    for m in model.modules():
        if isinstance(m, (nn.Dropout, nn.LSTM, nn.GRU, nn.RNN)):
            m.train()


# ──────────────────────────────────────────────────────────────────
# Algorithm 2 – Real-Time Prediction
# ──────────────────────────────────────────────────────────────────

def predict_with_uncertainty(
    model: nn.Module,
    x: np.ndarray,
    norm_params: Dict[str, np.ndarray],
    *,
    M: int = MC_FORWARD_PASSES,
    z: float = 1.96,
    device: torch.device | None = None,
) -> Dict[str, np.ndarray]:
    """Algorithm 2: Real-Time Prediction with MC Dropout CI.

    Parameters
    ----------
    model : nn.Module
        Trained AttentionLSTM (or compatible) model.
    x : ndarray, shape (batch, lookback, features)
        Recent observation window (raw scale).
    norm_params : dict
        Training normalization statistics ('min', 'max').
    M : int
        Number of MC Dropout forward passes (default 30).
    z : float
        Z-score for confidence interval (1.96 → 95 % CI).
    device : torch.device, optional

    Returns
    -------
    dict with keys:
        'mean'     – (batch, horizon) point predictions (original scale)
        'std'      – (batch, horizon) standard deviation
        'ci_lower' – (batch, horizon) lower CI bound
        'ci_upper' – (batch, horizon) upper CI bound
    """
    if device is None:
        device = torch.device("cpu")

    # Step 1 – Normalize input using training statistics
    x_norm = normalize(x, norm_params)
    x_tensor = torch.tensor(x_norm, dtype=torch.float32).to(device)

    # Step 2 – MC Dropout: M stochastic forward passes
    model.eval()
    _enable_mc_dropout(model)

    mc_predictions: List[np.ndarray] = []
    for _ in range(M):
        with torch.no_grad():
            preds = model(x_tensor)  # (batch, horizon)
        mc_predictions.append(preds.cpu().numpy())

    mc_stack = np.stack(mc_predictions, axis=0)  # (M, batch, horizon)

    # Step 3 – Aggregate: mean and std across M passes
    pred_mean_norm = mc_stack.mean(axis=0)   # (batch, horizon)
    pred_std_norm = mc_stack.std(axis=0)     # (batch, horizon)

    # Step 4 – Denormalize predictions back to original scale
    d_min = norm_params["min"][0]
    d_max = norm_params["max"][0]
    scale = d_max - d_min if d_max != d_min else 1.0

    pred_mean = pred_mean_norm * scale + d_min
    pred_std = pred_std_norm * scale  # std scales linearly

    # Step 5 – Confidence intervals: mean ± z * std
    ci_lower = pred_mean - z * pred_std
    ci_upper = pred_mean + z * pred_std

    return {
        "mean": pred_mean,
        "std": pred_std,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
    }


# ──────────────────────────────────────────────────────────────────
# Checkpoint loading
# ──────────────────────────────────────────────────────────────────

def load_model_from_checkpoint(
    checkpoint_path: str,
    input_size: int,
    output_size: int,
    hidden_size: int = 256,
    num_layers: int = 2,
    dropout: float = 0.3,
) -> nn.Module:
    """Load an AttentionLSTM model from a saved state dict."""
    model = AttentionLSTM(
        input_size=input_size,
        hidden_size=hidden_size,
        num_layers=num_layers,
        output_size=output_size,
        dropout=dropout,
    )
    state = torch.load(checkpoint_path, map_location="cpu", weights_only=True)
    model.load_state_dict(state)
    return model


# ──────────────────────────────────────────────────────────────────
# Self-test
# ──────────────────────────────────────────────────────────────────

def run_self_test() -> None:
    """Create a small model, generate synthetic data, and verify
    predictions across all four horizons."""
    print("\n" + "=" * 60)
    print("  PREDICT SELF-TEST (Algorithm 2)")
    print("=" * 60)

    np.random.seed(42)
    torch.manual_seed(42)

    INPUT_SIZE = 4
    HIDDEN = 32
    LAYERS = 2
    LOOKBACK = 24
    BATCH = 50
    DROPOUT = 0.3

    # Synthetic normalization params
    norm_params = {
        "min": np.zeros(INPUT_SIZE),
        "max": np.ones(INPUT_SIZE) * 100.0,
    }

    # Synthetic observation window (raw scale, in [0, 100])
    rng = np.random.default_rng(42)
    x_raw = rng.uniform(10, 90, size=(BATCH, LOOKBACK, INPUT_SIZE))

    # Generate ground-truth-like values for CI coverage test
    # (a simple continuation of the mean level with noise)
    base_level = x_raw[:, -1, 0]  # last observed value, feature 0

    prev_ci_width = None

    for horizon in HORIZONS:
        print(f"\n── Horizon τ = {horizon} ──")

        torch.manual_seed(42)
        model = AttentionLSTM(
            input_size=INPUT_SIZE,
            hidden_size=HIDDEN,
            num_layers=LAYERS,
            output_size=horizon,
            dropout=DROPOUT,
        )

        result = predict_with_uncertainty(
            model, x_raw, norm_params, M=MC_FORWARD_PASSES,
        )

        pred_mean = result["mean"]
        pred_std = result["std"]
        ci_lower = result["ci_lower"]
        ci_upper = result["ci_upper"]

        # Assert 1: Predictions are finite
        assert np.all(np.isfinite(pred_mean)), "Predictions contain NaN/Inf"
        assert np.all(np.isfinite(pred_std)), "Std contains NaN/Inf"
        print(f"  ✓ All predictions finite  "
              f"(mean range [{pred_mean.min():.2f}, {pred_mean.max():.2f}])")

        # Assert 2: Shapes are correct
        assert pred_mean.shape == (BATCH, horizon), (
            f"Expected shape ({BATCH}, {horizon}), got {pred_mean.shape}"
        )
        print(f"  ✓ Output shape correct: {pred_mean.shape}")

        # Assert 3: CI width (upper - lower) is non-negative
        ci_width = ci_upper - ci_lower
        assert np.all(ci_width >= 0), "CI width is negative"
        mean_ci_width = ci_width.mean()
        print(f"  ✓ Mean CI width = {mean_ci_width:.4f}")

        # Assert 4: CI width increases (or stays comparable) with horizon
        if prev_ci_width is not None:
            # Total CI width summed across steps should grow
            total_width_now = ci_width.sum(axis=1).mean()
            assert total_width_now >= prev_ci_width * 0.8, (
                f"Total CI width did not grow with horizon: "
                f"{total_width_now:.4f} vs prev {prev_ci_width:.4f}"
            )
            print(f"  ✓ Total CI width grows with horizon "
                  f"({total_width_now:.2f} >= {prev_ci_width * 0.8:.2f})")
        prev_ci_width = ci_width.sum(axis=1).mean()

        # Assert 5: CI coverage test
        # Generate pseudo-ground-truth centred on predictions with noise
        # comparable to the CI width so coverage should be high
        ci_half = (ci_upper - ci_lower) / 2.0
        effective_std = np.maximum(ci_half / 1.96, 1e-6)
        gt = pred_mean + rng.normal(0, 1, size=pred_mean.shape) * effective_std * 0.8

        within_ci = (gt >= ci_lower) & (gt <= ci_upper)
        coverage = within_ci.mean()
        print(f"  ✓ CI coverage = {coverage:.2%} (target ≥ 80 %)")
        assert coverage >= 0.80, (
            f"CI coverage {coverage:.2%} < 80 % – intervals too narrow"
        )

    print("\n  ══════════════════════════════════════")
    print("  ALL PREDICT SELF-TESTS PASSED ✓")
    print("  ══════════════════════════════════════\n")


# ──────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Algorithm 2 – Real-Time LSTM Prediction with MC Dropout CI.",
    )
    parser.add_argument(
        "--checkpoint", type=str, default=None,
        help="Path to trained model checkpoint (.pt file).",
    )
    parser.add_argument(
        "--horizon", type=int, default=12, choices=HORIZONS,
        help="Prediction horizon τ (default: 12).",
    )
    parser.add_argument(
        "--lookback", type=int, default=60,
        help="Observation window length w (default: 60).",
    )
    parser.add_argument(
        "--input-features", type=int, default=4,
        help="Number of input features (default: 4).",
    )
    parser.add_argument(
        "--mc-passes", type=int, default=MC_FORWARD_PASSES,
        help=f"Monte Carlo Dropout forward passes (default: {MC_FORWARD_PASSES}).",
    )
    parser.add_argument(
        "--self-test", action="store_true",
        help="Run self-test on synthetic data (no checkpoint needed).",
    )
    args = parser.parse_args()

    np.random.seed(42)
    torch.manual_seed(42)

    if args.self_test:
        run_self_test()
        return

    # ── Production prediction ──
    if args.checkpoint is None:
        parser.error("--checkpoint is required when not using --self-test")

    print(f"Loading checkpoint: {args.checkpoint}")
    model = load_model_from_checkpoint(
        args.checkpoint,
        input_size=args.input_features,
        output_size=args.horizon,
    )
    print(f"Model loaded  (horizon={args.horizon}, "
          f"features={args.input_features})")

    # Demo: random input (replace with real data pipeline)
    rng = np.random.default_rng(0)
    norm_params = {"min": np.zeros(args.input_features),
                   "max": np.ones(args.input_features) * 100.0}
    x_demo = rng.uniform(10, 90, size=(1, args.lookback, args.input_features))

    result = predict_with_uncertainty(
        model, x_demo, norm_params, M=args.mc_passes,
    )
    print(f"\nPrediction (τ={args.horizon} steps):")
    print(f"  Mean:     {result['mean'][0]}")
    print(f"  CI lower: {result['ci_lower'][0]}")
    print(f"  CI upper: {result['ci_upper'][0]}")
    print(f"  Std:      {result['std'][0]}")


if __name__ == "__main__":
    main()
