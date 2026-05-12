#!/usr/bin/env python3
"""
Training pipeline for LSTM traffic prediction in 5G networks.

Implements Algorithm 1 (Section VI.A) of
"Predicción de Tráfico Basada en LSTM para Gestión Proactiva de
Recursos en Redes 5G".

Training configuration follows Section VII.A.2:
  - Adam optimizer (β1=0.9, β2=0.999), η=0.001
  - Exponential LR decay: factor 0.95 every 10 epochs
  - Batch size 64, max 200 epochs, early stopping patience 40
  - Dropout 0.3, gradient clipping max-norm 5.0
  - Huber loss (δ=1.0), Xavier weight initialization
  - Teacher forcing ratio decaying from 1.0 → 0.0

Metrics (Section II.F): RMSE, MAE, MAPE, R², directional accuracy.
"""

from __future__ import annotations

import argparse
import math
import os
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
# torch.amp is the unified AMP API introduced in PyTorch 2.x (replaces
# the deprecated torch.cuda.amp sub-module for all device types).
import torch.amp as _torch_amp
from torch.utils.data import DataLoader, TensorDataset

# Local imports
from generate_datasets import create_sequences, normalize_data
from models import (
    AttentionLSTM,
    BaseLSTM,
    FeedforwardNN,
    GRUModel,
    LSTMNoAttention,
    MultiResolutionLSTM,
    ProposedLSTM,
    ResidualLSTM,
    SimpleRNN,
)

# ──────────────────────────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────────────────────────
RESULTS_DIR = Path(__file__).resolve().parent / "results"

MODEL_REGISTRY: dict[str, type[nn.Module]] = {
    "BaseLSTM": BaseLSTM,
    "AttentionLSTM": AttentionLSTM,
    "MultiResolutionLSTM": MultiResolutionLSTM,
    "ResidualLSTM": ResidualLSTM,
    "SimpleRNN": SimpleRNN,
    "GRUModel": GRUModel,
    "FeedforwardNN": FeedforwardNN,
    "LSTMNoAttention": LSTMNoAttention,
    "ProposedLSTM": ProposedLSTM,
}

DATASET_FILES: dict[str, str] = {
    "milano": "milano_dataset.npz",
    "shanghai": "shanghai_dataset.npz",
    "synthetic5g": "synthetic_5g_dataset.npz",
}


# ──────────────────────────────────────────────────────────────────
# Metrics  (Section II.F)
# ──────────────────────────────────────────────────────────────────

def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Root Mean Squared Error."""
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Mean Absolute Error."""
    return float(np.mean(np.abs(y_true - y_pred)))


def mape(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Mean Absolute Percentage Error (%)."""
    mask = np.abs(y_true) > 1e-8
    if mask.sum() == 0:
        return 0.0
    return float(100.0 * np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])))


def r_squared(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Coefficient of determination R²."""
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    if ss_tot == 0:
        return 1.0 if ss_res == 0 else 0.0
    return float(1.0 - ss_res / ss_tot)


def directional_accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Fraction of time steps where predicted direction matches actual.

    For multi-step horizons, compares direction between consecutive
    predicted steps.  For single-step, always returns 1.0.
    """
    if y_true.ndim == 1 or y_true.shape[-1] <= 1:
        return 1.0
    true_dir = np.sign(np.diff(y_true, axis=-1))
    pred_dir = np.sign(np.diff(y_pred, axis=-1))
    return float(np.mean(true_dir == pred_dir))


def compute_all_metrics(
    y_true: np.ndarray, y_pred: np.ndarray,
) -> dict[str, float]:
    """Return dict of all article metrics."""
    return {
        "RMSE": rmse(y_true, y_pred),
        "MAE": mae(y_true, y_pred),
        "MAPE": mape(y_true, y_pred),
        "R2": r_squared(y_true, y_pred),
        "DA": directional_accuracy(y_true, y_pred),
    }


# ──────────────────────────────────────────────────────────────────
# Data loading & preprocessing
# ──────────────────────────────────────────────────────────────────

def load_dataset(
    dataset_name: str,
    lookback: int,
    horizon: int,
    cell_idx: int = 0,
) -> tuple[np.ndarray, np.ndarray, dict]:
    """Load .npz dataset and build sliding-window sequences.

    Uses a single cell (``cell_idx``) aggregated across all features.
    Returns X (samples, lookback, features), Y (samples, horizon).
    Y is the first feature only (primary prediction target).
    """
    npz_path = RESULTS_DIR / DATASET_FILES[dataset_name]
    ds = np.load(npz_path, allow_pickle=True)
    data = ds["data"]  # (n_steps, n_cells, n_features)

    # Select one cell
    cell_data = data[:, cell_idx, :]  # (n_steps, n_features)

    # Normalize using training statistics (min-max)
    normed, norm_params = normalize_data(cell_data)

    # Build sequences
    X, Y_full = create_sequences(normed, lookback=lookback, horizon=horizon)
    # Y_full: (samples, horizon, n_features) → take first feature as target
    Y = Y_full[:, :, 0]  # (samples, horizon)
    if horizon == 1:
        Y = Y.squeeze(-1)  # (samples,)

    return X, Y, norm_params


def split_data(
    X: np.ndarray,
    Y: np.ndarray,
    train_frac: float = 0.6,
    val_frac: float = 0.2,
) -> tuple:
    """Temporal-order split: 60/20/20 train/val/test."""
    n = len(X)
    n_train = int(n * train_frac)
    n_val = int(n * (train_frac + val_frac))

    X_train, Y_train = X[:n_train], Y[:n_train]
    X_val, Y_val = X[n_train:n_val], Y[n_train:n_val]
    X_test, Y_test = X[n_val:], Y[n_val:]

    return X_train, Y_train, X_val, Y_val, X_test, Y_test


def make_dataloaders(
    X_train: np.ndarray,
    Y_train: np.ndarray,
    X_val: np.ndarray,
    Y_val: np.ndarray,
    batch_size: int = 64,
) -> tuple[DataLoader, DataLoader]:
    """Convert numpy arrays to DataLoaders.

    Uses ``pin_memory=True`` when CUDA is available to speed up host→device
    transfers on RTX-class GPUs (e.g., RTX 5070).
    """
    use_cuda = torch.cuda.is_available()
    train_ds = TensorDataset(
        torch.tensor(X_train, dtype=torch.float32),
        torch.tensor(Y_train, dtype=torch.float32),
    )
    val_ds = TensorDataset(
        torch.tensor(X_val, dtype=torch.float32),
        torch.tensor(Y_val, dtype=torch.float32),
    )
    train_loader = DataLoader(
        train_ds, batch_size=batch_size, shuffle=True,
        pin_memory=use_cuda, num_workers=0,
    )
    val_loader = DataLoader(
        val_ds, batch_size=batch_size, shuffle=False,
        pin_memory=use_cuda, num_workers=0,
    )
    return train_loader, val_loader


# ──────────────────────────────────────────────────────────────────
# Model construction
# ──────────────────────────────────────────────────────────────────

def build_model(
    model_name: str,
    input_size: int,
    output_size: int,
    lookback: int,
    dropout: float = 0.3,
) -> nn.Module:
    """Instantiate a model from the registry."""
    cls = MODEL_REGISTRY[model_name]
    kwargs: dict = dict(
        input_size=input_size,
        output_size=output_size,
        dropout=dropout,
    )
    if model_name == "FeedforwardNN":
        kwargs["seq_len"] = lookback
    model = cls(**kwargs)
    return model


# ──────────────────────────────────────────────────────────────────
# Training loop  (Algorithm 1)
# ──────────────────────────────────────────────────────────────────

def train(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    *,
    model_name: str,
    dataset_name: str,
    device: torch.device,
    lr: float = 0.001,
    epochs: int = 200,
    patience: int = 40,
    clip_norm: float = 5.0,
    lr_decay_factor: float = 0.95,
    lr_decay_step: int = 10,
) -> dict:
    """Full training loop implementing Algorithm 1 (Section VI.A).

    Returns
    -------
    history : dict with keys 'train_loss', 'val_loss', 'val_r2',
              'best_epoch', 'test_metrics' (filled later).
    """
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, betas=(0.9, 0.999))
    # OneCycleLR: cosine annealing with warmup; step() called per batch
    total_steps = len(train_loader) * epochs
    scheduler = torch.optim.lr_scheduler.OneCycleLR(
        optimizer,
        max_lr=lr * 3,
        total_steps=total_steps,
        pct_start=0.1,
        anneal_strategy='cos',
        div_factor=10.0,
        final_div_factor=100.0,
    )
    criterion = nn.HuberLoss(delta=1.0)
    # Automatic Mixed Precision: speeds up training on RTX-class GPUs ≥ Ampere
    _use_amp = device.type == "cuda" and torch.cuda.is_bf16_supported()
    _scaler = _torch_amp.GradScaler("cuda", enabled=_use_amp)

    # Determine if model supports teacher forcing
    has_teacher_forcing = model_name in ("AttentionLSTM", "ProposedLSTM")

    history: dict = {
        "train_loss": [],
        "val_loss": [],
        "val_r2": [],
        "best_epoch": 0,
    }
    best_val_loss = float("inf")
    epochs_no_improve = 0
    best_state = None

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    for epoch in range(1, epochs + 1):
        # ── Teacher forcing ratio: decay from 1.0 → 0.0 ──
        tf_ratio = max(0.0, 1.0 - (epoch - 1) / max(epochs - 1, 1))

        # ── Training phase ──
        model.train()
        running_loss = 0.0
        n_batches = 0
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()

            with _torch_amp.autocast(device_type=device.type, enabled=_use_amp):
                if has_teacher_forcing:
                    preds = model(xb, teacher_forcing_ratio=tf_ratio, target=yb)
                else:
                    preds = model(xb)
                loss = criterion(preds, yb)

            assert not torch.isnan(loss), f"NaN loss at epoch {epoch}"
            _scaler.scale(loss).backward()
            _scaler.unscale_(optimizer)
            nn.utils.clip_grad_norm_(model.parameters(), clip_norm)
            _scaler.step(optimizer)
            _scaler.update()
            scheduler.step()

            running_loss += loss.item()
            n_batches += 1

        train_loss = running_loss / max(n_batches, 1)
        history["train_loss"].append(train_loss)

        # ── Validation phase ──
        val_loss, val_r2 = _evaluate(model, val_loader, criterion, device,
                                     model_name=model_name)
        history["val_loss"].append(val_loss)
        history["val_r2"].append(val_r2)

        # ── Early stopping ──
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            epochs_no_improve = 0
            history["best_epoch"] = epoch
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
        else:
            epochs_no_improve += 1

        cur_lr = optimizer.param_groups[0]["lr"]
        print(
            f"Epoch {epoch:3d}/{epochs} │ "
            f"train_loss={train_loss:.6f}  val_loss={val_loss:.6f}  "
            f"val_R²={val_r2:.4f}  lr={cur_lr:.6f}  "
            f"tf={tf_ratio:.2f}  patience={epochs_no_improve}/{patience}"
        )

        if epochs_no_improve >= patience:
            print(f"Early stopping at epoch {epoch}.")
            break

    # Restore best model
    if best_state is not None:
        model.load_state_dict(best_state)
        model.to(device)

    # Save checkpoint
    ckpt_path = RESULTS_DIR / f"{dataset_name}_{model_name}_best.pt"
    torch.save(best_state or model.state_dict(), ckpt_path)
    print(f"Best model saved → {ckpt_path}")

    return history


def _evaluate(
    model: nn.Module,
    loader: DataLoader,
    criterion: nn.Module,
    device: torch.device,
    *,
    model_name: str = "",
) -> tuple[float, float]:
    """Compute validation loss and R² on a DataLoader."""
    model.eval()
    total_loss = 0.0
    n_batches = 0
    all_true, all_pred = [], []

    with torch.no_grad():
        for xb, yb in loader:
            xb, yb = xb.to(device), yb.to(device)
            preds = model(xb)
            loss = criterion(preds, yb)
            total_loss += loss.item()
            n_batches += 1
            all_true.append(yb.cpu().numpy())
            all_pred.append(preds.cpu().numpy())

    avg_loss = total_loss / max(n_batches, 1)
    y_true = np.concatenate(all_true, axis=0)
    y_pred = np.concatenate(all_pred, axis=0)
    r2 = r_squared(y_true.flatten(), y_pred.flatten())
    return avg_loss, r2


# ──────────────────────────────────────────────────────────────────
# Test evaluation
# ──────────────────────────────────────────────────────────────────

def evaluate_test(
    model: nn.Module,
    X_test: np.ndarray,
    Y_test: np.ndarray,
    device: torch.device,
    model_name: str = "",
    norm_params=None,
) -> dict[str, float]:
    """Evaluate all metrics on test set."""
    model.eval()
    x_t = torch.tensor(X_test, dtype=torch.float32).to(device)
    with torch.no_grad():
        preds = model(x_t).cpu().numpy()
    metrics = compute_all_metrics(Y_test.flatten(), preds.flatten())
    if norm_params is not None:
        scale = float(norm_params['max'][0]) - float(norm_params['min'][0])
        if scale > 0:
            metrics['RMSE_abs'] = metrics['RMSE'] * scale
            metrics['MAE_abs'] = metrics['MAE'] * scale
    return metrics


# ──────────────────────────────────────────────────────────────────
# Self-test mode
# ──────────────────────────────────────────────────────────────────

def _generate_synthetic_selftest(
    n_steps: int = 2000,
    lookback: int = 24,
    horizon: int = 1,
) -> tuple[np.ndarray, np.ndarray]:
    """Build a small deterministic dataset for fast self-testing.

    Uses a sine + trend signal that is easy to learn.
    """
    rng = np.random.default_rng(42)
    t = np.arange(n_steps, dtype=np.float64)
    # Deterministic: sine with trend + small noise
    signal = 0.5 + 0.3 * np.sin(2 * np.pi * t / 100) + 0.1 * (t / n_steps)
    signal += rng.normal(0, 0.02, n_steps)
    signal = np.clip(signal, 0, None)

    # Make it 2-feature
    data = np.stack([signal, signal * 0.8 + 0.1], axis=-1)  # (n_steps, 2)
    normed, _ = normalize_data(data)
    X, Y_full = create_sequences(normed, lookback=lookback, horizon=horizon)
    Y = Y_full[:, :, 0]
    if horizon == 1:
        Y = Y.squeeze(-1)
    return X, Y


def run_self_test() -> None:
    """Train on small synthetic data for 30 epochs, assert convergence."""
    print("\n" + "=" * 60)
    print("  SELF-TEST MODE")
    print("=" * 60)

    np.random.seed(42)
    torch.manual_seed(42)
    device = torch.device("cpu")

    lookback = 24
    horizon = 4

    X, Y = _generate_synthetic_selftest(n_steps=2000, lookback=lookback,
                                        horizon=horizon)
    X_train, Y_train, X_val, Y_val, X_test, Y_test = split_data(X, Y)

    print(f"  Train: {X_train.shape[0]}, Val: {X_val.shape[0]}, "
          f"Test: {X_test.shape[0]} samples")
    print(f"  Input features: {X.shape[-1]}, Horizon: {horizon}")

    train_loader, val_loader = make_dataloaders(
        X_train, Y_train, X_val, Y_val, batch_size=32,
    )

    # Test with BaseLSTM (fast) and AttentionLSTM (teacher forcing)
    for model_name in ["BaseLSTM", "AttentionLSTM"]:
        print(f"\n── Testing {model_name} ──")
        torch.manual_seed(42)
        model = build_model(
            model_name,
            input_size=X.shape[-1],
            output_size=horizon,
            lookback=lookback,
        )
        print(f"  Parameters: {sum(p.numel() for p in model.parameters()):,d}")

        history = train(
            model, train_loader, val_loader,
            model_name=model_name,
            dataset_name="selftest",
            device=device,
            lr=0.001,
            epochs=30,
            patience=30,
            clip_norm=5.0,
        )

        # ── Assert 1: Loss decreases ──
        tl = history["train_loss"]
        first_5 = np.mean(tl[:5])
        last_5 = np.mean(tl[-5:])
        assert last_5 < first_5, (
            f"{model_name}: loss did not decrease "
            f"(first_5={first_5:.6f}, last_5={last_5:.6f})"
        )
        print(f"  ✓ Loss decreased: {first_5:.6f} → {last_5:.6f}")

        # ── Assert 2: No NaN in losses ──
        assert not any(math.isnan(v) for v in tl), f"{model_name}: NaN in train_loss"
        assert not any(math.isnan(v) for v in history["val_loss"]), (
            f"{model_name}: NaN in val_loss"
        )
        print("  ✓ No NaN in losses")

        # ── Assert 3: Reasonable predictions ──
        test_metrics = evaluate_test(model, X_test, Y_test, device,
                                     model_name=model_name)
        print(f"  Test metrics: {test_metrics}")
        assert not math.isnan(test_metrics["RMSE"]), "RMSE is NaN"
        assert test_metrics["RMSE"] > 0, "RMSE is zero (trivial model)"

        # ── Assert 4: Minimum R² on validation ──
        best_val_r2 = max(history["val_r2"])
        assert best_val_r2 > 0.5, (
            f"{model_name}: best val R²={best_val_r2:.4f} < 0.5"
        )
        print(f"  ✓ Best val R² = {best_val_r2:.4f} > 0.5")

        # ── Assert 5: Predictions not all zeros ──
        x_t = torch.tensor(X_test, dtype=torch.float32)
        with torch.no_grad():
            preds = model(x_t).numpy()
        assert not np.allclose(preds, 0), f"{model_name}: all-zero predictions"
        print(f"  ✓ Predictions are non-trivial (std={preds.std():.6f})")

    print("\n  ══════════════════════════════════════")
    print("  ALL SELF-TESTS PASSED ✓")
    print("  ══════════════════════════════════════\n")


# ──────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Train LSTM models for 5G traffic prediction (Algorithm 1).",
    )
    parser.add_argument(
        "--dataset", type=str, default="synthetic5g",
        choices=["milano", "shanghai", "synthetic5g"],
        help="Dataset to use (default: synthetic5g).",
    )
    parser.add_argument(
        "--model", type=str, default="AttentionLSTM",
        choices=list(MODEL_REGISTRY.keys()),
        help="Model architecture (default: AttentionLSTM).",
    )
    parser.add_argument("--lookback", type=int, default=60,
                        help="Look-back window w (default: 60).")
    parser.add_argument("--horizon", type=int, default=1,
                        help="Prediction horizon τ (default: 1).")
    parser.add_argument("--epochs", type=int, default=200,
                        help="Maximum training epochs (default: 200).")
    parser.add_argument("--batch-size", type=int, default=64,
                        help="Mini-batch size (default: 64).")
    parser.add_argument("--lr", type=float, default=0.001,
                        help="Initial learning rate η (default: 0.001).")
    parser.add_argument(
        "--self-test", action="store_true",
        help="Run fast self-test on synthetic data (30 epochs).",
    )
    args = parser.parse_args()

    # ── Reproducibility ──
    np.random.seed(42)
    torch.manual_seed(42)

    if args.self_test:
        run_self_test()
        return

    # ── Device ──
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    # ── Load data ──
    print(f"Loading dataset '{args.dataset}' …")
    X, Y, norm_params = load_dataset(
        args.dataset, lookback=args.lookback, horizon=args.horizon,
    )
    print(f"  X shape: {X.shape}, Y shape: {Y.shape}")

    X_train, Y_train, X_val, Y_val, X_test, Y_test = split_data(X, Y)
    print(f"  Train: {len(X_train)}, Val: {len(X_val)}, Test: {len(X_test)}")

    train_loader, val_loader = make_dataloaders(
        X_train, Y_train, X_val, Y_val, batch_size=args.batch_size,
    )

    # ── Build model ──
    input_size = X.shape[-1]
    output_size = args.horizon
    model = build_model(
        args.model, input_size, output_size,
        lookback=args.lookback, dropout=0.3,
    )
    n_params = sum(p.numel() for p in model.parameters())
    print(f"Model: {args.model}  ({n_params:,d} parameters)")

    # ── Train ──
    t0 = time.time()
    history = train(
        model, train_loader, val_loader,
        model_name=args.model,
        dataset_name=args.dataset,
        device=device,
        lr=args.lr,
        epochs=args.epochs,
        patience=40,
        clip_norm=5.0,
    )
    elapsed = time.time() - t0
    print(f"\nTraining completed in {elapsed:.1f} s  "
          f"(best epoch: {history['best_epoch']})")

    # ── Test evaluation ──
    test_metrics = evaluate_test(model, X_test, Y_test, device,
                                 model_name=args.model)
    history["test_metrics"] = test_metrics

    print("\n" + "=" * 50)
    print("  Final Test Metrics")
    print("=" * 50)
    for k, v in test_metrics.items():
        print(f"  {k:5s}: {v:.6f}")
    print("=" * 50)

    # ── Quality checks ──
    best_val_r2 = max(history["val_r2"])
    print(f"\nBest validation R²: {best_val_r2:.4f}")
    assert best_val_r2 > 0.85, (
        f"Quality check failed: best val R²={best_val_r2:.4f} < 0.85"
    )
    print("  ✓ R² > 0.85 quality check passed")

    tl = history["train_loss"]
    assert np.mean(tl[-5:]) < np.mean(tl[:5]), (
        "Convergence check failed: loss did not decrease over training"
    )
    print("  ✓ Convergence check passed")

    assert not any(math.isnan(v) for v in tl), "NaN detected in training losses"
    print("  ✓ No NaN in losses")

    # ── Save training history ──
    hist_path = RESULTS_DIR / f"{args.dataset}_{args.model}_history.npz"
    np.savez_compressed(
        hist_path,
        train_loss=np.array(history["train_loss"]),
        val_loss=np.array(history["val_loss"]),
        val_r2=np.array(history["val_r2"]),
        best_epoch=np.array(history["best_epoch"]),
        test_rmse=np.array(test_metrics["RMSE"]),
        test_mae=np.array(test_metrics["MAE"]),
        test_mape=np.array(test_metrics["MAPE"]),
        test_r2=np.array(test_metrics["R2"]),
        test_da=np.array(test_metrics["DA"]),
    )
    print(f"History saved → {hist_path}")


if __name__ == "__main__":
    main()
