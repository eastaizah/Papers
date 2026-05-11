#!/usr/bin/env python3
"""
Neural network architectures for traffic prediction in 5G networks.

Implements all models described in Sections II and IV of
"Predicción de Tráfico Basada en LSTM para Gestión Proactiva de
Recursos en Redes 5G", plus traditional ML/statistical baselines.

Models
------
- BaseLSTM           : Stacked LSTM (Section IV.A)
- AttentionLSTM      : Encoder-Decoder with Bahdanau attention (IV.B / IV.G)
- MultiResolutionLSTM: Multi-resolution parallel branches (IV.E)
- ResidualLSTM       : LSTM with residual connections + LayerNorm (IV.F)
- SimpleRNN          : Vanilla RNN baseline
- GRUModel           : GRU baseline (Section II.B.4.a)
- FeedforwardNN      : MLP baseline (512-256-128)
- LSTMNoAttention    : Encoder-Decoder LSTM without attention

Baselines (sklearn / statsmodels wrappers)
------------------------------------------
- ARIMABaseline, SARIMABaseline, SVRBaseline,
  RandomForestBaseline, XGBoostBaseline
"""

from __future__ import annotations

import argparse
import math
from typing import Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

# ──────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────

def _xavier_init(module: nn.Module) -> None:
    """Apply Xavier uniform initialization to Linear and LSTM weights."""
    for name, param in module.named_parameters():
        if "weight_ih" in name or "weight_hh" in name:
            nn.init.xavier_uniform_(param.data)
        elif "weight" in name and param.dim() >= 2:
            nn.init.xavier_uniform_(param.data)
        elif "bias" in name:
            nn.init.zeros_(param.data)


def _count_parameters(model: nn.Module) -> int:
    """Return total number of trainable parameters."""
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


# ──────────────────────────────────────────────────────────────────
# 1. BaseLSTM  (Section IV.A)
# ──────────────────────────────────────────────────────────────────

class BaseLSTM(nn.Module):
    """Stacked LSTM for direct multi-step prediction.

    Parameters
    ----------
    input_size : int
        Number of input features per time-step.
    hidden_size : int
        LSTM hidden dimension (default 256).
    num_layers : int
        Number of stacked LSTM layers (default 2).
    output_size : int
        Prediction horizon length (default 1).
    dropout : float
        Dropout probability between LSTM layers (default 0.3).
    """

    def __init__(
        self,
        input_size: int,
        hidden_size: int = 256,
        num_layers: int = 2,
        output_size: int = 1,
        dropout: float = 0.3,
    ) -> None:
        super().__init__()
        self.lstm = nn.LSTM(
            input_size,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.fc = nn.Linear(hidden_size, output_size)
        _xavier_init(self)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (batch, seq_len, features)
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])  # (batch, horizon)

    def count_parameters(self) -> int:
        return _count_parameters(self)


# ──────────────────────────────────────────────────────────────────
# 2. AttentionLSTM  (Sections IV.B / IV.G – proposed model)
# ──────────────────────────────────────────────────────────────────

class _BahdanauAttention(nn.Module):
    """Additive (Bahdanau) attention with scale factor."""

    def __init__(self, enc_dim: int, dec_dim: int) -> None:
        super().__init__()
        self.W1 = nn.Linear(enc_dim, dec_dim, bias=False)
        self.W2 = nn.Linear(dec_dim, dec_dim, bias=False)
        self.v = nn.Linear(dec_dim, 1, bias=False)
        self.scale = math.sqrt(dec_dim)

    def forward(
        self,
        decoder_hidden: torch.Tensor,
        encoder_outputs: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Parameters
        ----------
        decoder_hidden : (batch, dec_dim)
        encoder_outputs : (batch, seq_len, enc_dim)

        Returns
        -------
        context : (batch, enc_dim)
        attn_weights : (batch, seq_len)
        """
        # score: v^T tanh(W1 h_enc + W2 h_dec) / sqrt(d)
        proj_enc = self.W1(encoder_outputs)            # (B, T, dec_dim)
        proj_dec = self.W2(decoder_hidden).unsqueeze(1) # (B, 1, dec_dim)
        energy = self.v(torch.tanh(proj_enc + proj_dec)).squeeze(-1)  # (B, T)
        energy = energy / self.scale

        attn_weights = F.softmax(energy, dim=-1)       # (B, T)
        context = torch.bmm(attn_weights.unsqueeze(1), encoder_outputs)
        return context.squeeze(1), attn_weights


class AttentionLSTM(nn.Module):
    """Encoder-Decoder LSTM with Bahdanau attention (Section IV.B / IV.G).

    This is the **proposed** architecture in the article.

    Parameters
    ----------
    input_size : int
        Number of input features.
    hidden_size : int
        Hidden dimension for both encoder and decoder (default 256).
    num_layers : int
        Layers per LSTM stack (default 2).
    output_size : int
        Prediction horizon (default 1).
    dropout : float
        Dropout rate (default 0.3).
    """

    def __init__(
        self,
        input_size: int,
        hidden_size: int = 256,
        num_layers: int = 2,
        output_size: int = 1,
        dropout: float = 0.3,
    ) -> None:
        super().__init__()
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.num_layers = num_layers

        # Encoder: bidirectional → output dim = 2 * hidden_size
        self.encoder = nn.LSTM(
            input_size,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
            bidirectional=True,
        )
        enc_dim = hidden_size * 2

        # Project encoder final states to decoder initial states
        self.h_proj = nn.Linear(enc_dim, hidden_size)
        self.c_proj = nn.Linear(enc_dim, hidden_size)

        # Decoder: unidirectional
        # Input = previous prediction (1) + context (enc_dim)
        self.decoder = nn.LSTM(
            1 + enc_dim,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )

        self.attention = _BahdanauAttention(enc_dim, hidden_size)

        # Dense layers: 128 neurons, ReLU → linear output
        self.fc1 = nn.Linear(hidden_size + enc_dim, 128)
        self.fc_out = nn.Linear(128, 1)

        _xavier_init(self)

    # -----------------------------------------------------------------
    def _init_decoder_state(
        self,
        h_enc: torch.Tensor,
        c_enc: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Merge bidirectional encoder states for the decoder."""
        # h_enc, c_enc: (num_layers*2, B, H)
        batch = h_enc.size(1)
        # Reshape to (num_layers, 2, B, H), concat directions
        h = h_enc.view(self.num_layers, 2, batch, self.hidden_size)
        c = c_enc.view(self.num_layers, 2, batch, self.hidden_size)
        h = torch.cat([h[:, 0], h[:, 1]], dim=-1)  # (L, B, 2H)
        c = torch.cat([c[:, 0], c[:, 1]], dim=-1)
        h = torch.tanh(self.h_proj(h))  # (L, B, H)
        c = torch.tanh(self.c_proj(c))
        return h.contiguous(), c.contiguous()

    def forward(
        self,
        x: torch.Tensor,
        teacher_forcing_ratio: float = 0.0,
        target: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """
        Parameters
        ----------
        x : (batch, seq_len, features)
        teacher_forcing_ratio : float
            Probability of using ground-truth previous output during
            training (teacher forcing).
        target : (batch, horizon), optional
            Ground-truth future values (needed for teacher forcing).

        Returns
        -------
        predictions : (batch, horizon)
        """
        batch = x.size(0)
        enc_out, (h_enc, c_enc) = self.encoder(x)  # enc_out: (B, T, 2H)

        h_dec, c_dec = self._init_decoder_state(h_enc, c_enc)

        # First decoder input: zeros (start token)
        dec_input = torch.zeros(batch, 1, 1, device=x.device)

        predictions = []
        for t in range(self.output_size):
            # Attention over encoder outputs using top-layer decoder hidden
            context, _ = self.attention(h_dec[-1], enc_out)  # (B, 2H)

            # Decoder step
            dec_combined = torch.cat(
                [dec_input, context.unsqueeze(1)], dim=-1,
            )  # (B, 1, 1+2H)
            dec_out, (h_dec, c_dec) = self.decoder(
                dec_combined, (h_dec, c_dec),
            )

            # Prediction from concatenation of decoder output + context
            pred_in = torch.cat([dec_out.squeeze(1), context], dim=-1)
            pred = self.fc_out(F.relu(self.fc1(pred_in)))  # (B, 1)
            predictions.append(pred)

            # Next decoder input
            if target is not None and np.random.random() < teacher_forcing_ratio:
                dec_input = target[:, t].unsqueeze(-1).unsqueeze(-1)
            else:
                dec_input = pred.unsqueeze(1)  # (B, 1, 1)

        return torch.cat(predictions, dim=-1)  # (B, horizon)

    def count_parameters(self) -> int:
        return _count_parameters(self)


# ──────────────────────────────────────────────────────────────────
# 3. MultiResolutionLSTM  (Section IV.E)
# ──────────────────────────────────────────────────────────────────

class _ResolutionBranch(nn.Module):
    """Single branch for one resolution level."""

    def __init__(
        self,
        input_size: int,
        hidden_size: int = 128,
        num_layers: int = 2,
        dropout: float = 0.3,
        downsample_factor: int = 1,
    ) -> None:
        super().__init__()
        self.downsample_factor = downsample_factor
        self.lstm = nn.LSTM(
            input_size,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
            bidirectional=True,
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Downsample by averaging non-overlapping windows
        if self.downsample_factor > 1:
            B, T, F = x.shape
            trim = T - T % self.downsample_factor
            x = x[:, :trim, :]
            x = x.reshape(B, trim // self.downsample_factor, self.downsample_factor, F)
            x = x.mean(dim=2)
        out, _ = self.lstm(x)  # (B, T', 2*H)
        return out[:, -1, :]   # (B, 2*H)


class MultiResolutionLSTM(nn.Module):
    """Multi-resolution LSTM with attention-based fusion (Section IV.E).

    Three parallel branches process the input at factors 1, 2, 4.
    Learned attention weights β_k fuse the branch outputs.
    """

    def __init__(
        self,
        input_size: int,
        hidden_size: int = 128,
        num_layers: int = 2,
        output_size: int = 1,
        dropout: float = 0.3,
    ) -> None:
        super().__init__()
        self.branches = nn.ModuleList([
            _ResolutionBranch(input_size, hidden_size, num_layers, dropout, ds)
            for ds in [1, 2, 4]
        ])
        branch_out = hidden_size * 2  # bidirectional

        # Attention gate: W_beta projects each branch output to scalar
        self.W_beta = nn.Linear(branch_out, 1, bias=False)

        self.fc = nn.Linear(branch_out, output_size)
        _xavier_init(self)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        branch_outs = [br(x) for br in self.branches]       # list of (B, 2H)
        stacked = torch.stack(branch_outs, dim=1)            # (B, 3, 2H)
        betas = F.softmax(self.W_beta(stacked).squeeze(-1), dim=-1)  # (B, 3)
        fused = torch.bmm(betas.unsqueeze(1), stacked).squeeze(1)    # (B, 2H)
        return self.fc(fused)  # (B, horizon)

    def count_parameters(self) -> int:
        return _count_parameters(self)


# ──────────────────────────────────────────────────────────────────
# 4. ResidualLSTM  (Section IV.F)
# ──────────────────────────────────────────────────────────────────

class _ResidualLSTMLayer(nn.Module):
    """Single LSTM layer with residual connection + LayerNorm.

    h_t^(l) = LayerNorm(LSTM^(l)(...) + proj(h_t^(l-1)))
    """

    def __init__(self, input_size: int, hidden_size: int, dropout: float) -> None:
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.layer_norm = nn.LayerNorm(hidden_size)
        self.dropout = nn.Dropout(dropout)
        # Projection when input_size != hidden_size
        self.proj = (
            nn.Linear(input_size, hidden_size, bias=False)
            if input_size != hidden_size
            else nn.Identity()
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        residual = self.proj(x)             # (B, T, H)
        out, _ = self.lstm(x)               # (B, T, H)
        out = self.layer_norm(out + residual)
        return self.dropout(out)


class ResidualLSTM(nn.Module):
    """LSTM with residual connections and layer normalization (Section IV.F)."""

    def __init__(
        self,
        input_size: int,
        hidden_size: int = 256,
        num_layers: int = 2,
        output_size: int = 1,
        dropout: float = 0.3,
    ) -> None:
        super().__init__()
        layers: list[nn.Module] = []
        for i in range(num_layers):
            in_dim = input_size if i == 0 else hidden_size
            layers.append(_ResidualLSTMLayer(in_dim, hidden_size, dropout))
        self.layers = nn.ModuleList(layers)
        self.fc = nn.Linear(hidden_size, output_size)
        _xavier_init(self)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        for layer in self.layers:
            x = layer(x)
        return self.fc(x[:, -1, :])

    def count_parameters(self) -> int:
        return _count_parameters(self)


# ──────────────────────────────────────────────────────────────────
# 5. SimpleRNN  (baseline)
# ──────────────────────────────────────────────────────────────────

class SimpleRNN(nn.Module):
    """Vanilla RNN baseline – 2 layers, 256 units."""

    def __init__(
        self,
        input_size: int,
        hidden_size: int = 256,
        num_layers: int = 2,
        output_size: int = 1,
        dropout: float = 0.3,
    ) -> None:
        super().__init__()
        self.rnn = nn.RNN(
            input_size,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.fc = nn.Linear(hidden_size, output_size)
        _xavier_init(self)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out, _ = self.rnn(x)
        return self.fc(out[:, -1, :])

    def count_parameters(self) -> int:
        return _count_parameters(self)


# ──────────────────────────────────────────────────────────────────
# 6. GRUModel  (Section II.B.4.a baseline)
# ──────────────────────────────────────────────────────────────────

class GRUModel(nn.Module):
    """GRU baseline – 2 layers, 256 units."""

    def __init__(
        self,
        input_size: int,
        hidden_size: int = 256,
        num_layers: int = 2,
        output_size: int = 1,
        dropout: float = 0.3,
    ) -> None:
        super().__init__()
        self.gru = nn.GRU(
            input_size,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.fc = nn.Linear(hidden_size, output_size)
        _xavier_init(self)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out, _ = self.gru(x)
        return self.fc(out[:, -1, :])

    def count_parameters(self) -> int:
        return _count_parameters(self)


# ──────────────────────────────────────────────────────────────────
# 7. FeedforwardNN  (MLP baseline)
# ──────────────────────────────────────────────────────────────────

class FeedforwardNN(nn.Module):
    """Three-hidden-layer MLP baseline (512 → 256 → 128, ReLU)."""

    def __init__(
        self,
        input_size: int,
        hidden_size: int = 256,
        num_layers: int = 3,
        output_size: int = 1,
        dropout: float = 0.3,
        seq_len: int = 1,
    ) -> None:
        super().__init__()
        flat_in = input_size * seq_len
        self.seq_len = seq_len
        self.net = nn.Sequential(
            nn.Linear(flat_in, 512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(128, output_size),
        )
        _xavier_init(self)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (batch, seq_len, features) → flatten temporal dimension
        return self.net(x.reshape(x.size(0), -1))

    def count_parameters(self) -> int:
        return _count_parameters(self)


# ──────────────────────────────────────────────────────────────────
# 8. LSTMNoAttention  (Encoder-Decoder without attention)
# ──────────────────────────────────────────────────────────────────

class LSTMNoAttention(nn.Module):
    """Encoder-Decoder LSTM without attention mechanism."""

    def __init__(
        self,
        input_size: int,
        hidden_size: int = 256,
        num_layers: int = 2,
        output_size: int = 1,
        dropout: float = 0.3,
    ) -> None:
        super().__init__()
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.num_layers = num_layers

        self.encoder = nn.LSTM(
            input_size,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        # Decoder input: previous prediction (1 dim)
        self.decoder = nn.LSTM(
            1,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.fc = nn.Linear(hidden_size, 1)
        _xavier_init(self)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        batch = x.size(0)
        _, (h, c) = self.encoder(x)

        dec_input = torch.zeros(batch, 1, 1, device=x.device)
        predictions = []
        for _ in range(self.output_size):
            dec_out, (h, c) = self.decoder(dec_input, (h, c))
            pred = self.fc(dec_out.squeeze(1))  # (B, 1)
            predictions.append(pred)
            dec_input = pred.unsqueeze(1)       # (B, 1, 1)

        return torch.cat(predictions, dim=-1)   # (B, horizon)

    def count_parameters(self) -> int:
        return _count_parameters(self)


# ══════════════════════════════════════════════════════════════════
# Traditional / ML Baselines (sklearn & statsmodels wrappers)
# ══════════════════════════════════════════════════════════════════

class ARIMABaseline:
    """ARIMA wrapper using statsmodels.

    Parameters
    ----------
    order : tuple
        (p, d, q) order of the ARIMA model.
    """

    def __init__(self, order: tuple = (5, 1, 0)) -> None:
        self.order = order
        self._model = None
        self._result = None

    def fit(self, y: np.ndarray) -> "ARIMABaseline":
        from statsmodels.tsa.arima.model import ARIMA

        self._model = ARIMA(y, order=self.order)
        self._result = self._model.fit()
        return self

    def predict(self, steps: int = 1) -> np.ndarray:
        if self._result is None:
            raise RuntimeError("Call fit() before predict().")
        return self._result.forecast(steps=steps)


class SARIMABaseline:
    """Seasonal ARIMA wrapper using statsmodels.

    Parameters
    ----------
    order : tuple
        (p, d, q) non-seasonal order.
    seasonal_order : tuple
        (P, D, Q, s) seasonal order.
    """

    def __init__(
        self,
        order: tuple = (1, 1, 1),
        seasonal_order: tuple = (1, 1, 1, 24),
    ) -> None:
        self.order = order
        self.seasonal_order = seasonal_order
        self._result = None

    def fit(self, y: np.ndarray) -> "SARIMABaseline":
        from statsmodels.tsa.statespace.sarimax import SARIMAX

        model = SARIMAX(y, order=self.order, seasonal_order=self.seasonal_order)
        self._result = model.fit(disp=False)
        return self

    def predict(self, steps: int = 1) -> np.ndarray:
        if self._result is None:
            raise RuntimeError("Call fit() before predict().")
        return self._result.forecast(steps=steps)


class SVRBaseline:
    """SVR wrapper using sklearn with RBF kernel.

    The model is trained on windowed features (flattened look-back).
    """

    def __init__(self, kernel: str = "rbf", C: float = 1.0, epsilon: float = 0.1) -> None:
        from sklearn.svm import SVR

        self._model = SVR(kernel=kernel, C=C, epsilon=epsilon)

    def fit(self, X: np.ndarray, y: np.ndarray) -> "SVRBaseline":
        self._model.fit(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self._model.predict(X)


class RandomForestBaseline:
    """Random-Forest wrapper using sklearn."""

    def __init__(self, n_estimators: int = 100, random_state: int = 42) -> None:
        from sklearn.ensemble import RandomForestRegressor

        self._model = RandomForestRegressor(
            n_estimators=n_estimators, random_state=random_state,
        )

    def fit(self, X: np.ndarray, y: np.ndarray) -> "RandomForestBaseline":
        self._model.fit(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self._model.predict(X)


class XGBoostBaseline:
    """Gradient Boosting stand-in for XGBoost (sklearn)."""

    def __init__(
        self,
        n_estimators: int = 200,
        learning_rate: float = 0.1,
        max_depth: int = 5,
        random_state: int = 42,
    ) -> None:
        from sklearn.ensemble import GradientBoostingRegressor

        self._model = GradientBoostingRegressor(
            n_estimators=n_estimators,
            learning_rate=learning_rate,
            max_depth=max_depth,
            random_state=random_state,
        )

    def fit(self, X: np.ndarray, y: np.ndarray) -> "XGBoostBaseline":
        self._model.fit(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self._model.predict(X)


# ══════════════════════════════════════════════════════════════════
# Self-test
# ══════════════════════════════════════════════════════════════════

def _self_test() -> None:
    """Instantiate every model with small dims, run a forward pass,
    verify output shapes, and print parameter counts."""

    INPUT_SIZE = 4
    HIDDEN_SIZE = 32
    NUM_LAYERS = 2
    OUTPUT_SIZE = 4
    SEQ_LEN = 16
    BATCH = 8

    torch.manual_seed(0)
    x = torch.randn(BATCH, SEQ_LEN, INPUT_SIZE)

    models: dict[str, nn.Module] = {
        "BaseLSTM": BaseLSTM(INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE),
        "AttentionLSTM": AttentionLSTM(INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE),
        "MultiResolutionLSTM": MultiResolutionLSTM(INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE),
        "ResidualLSTM": ResidualLSTM(INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE),
        "SimpleRNN": SimpleRNN(INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE),
        "GRUModel": GRUModel(INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE),
        "FeedforwardNN": FeedforwardNN(INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE, seq_len=SEQ_LEN),
        "LSTMNoAttention": LSTMNoAttention(INPUT_SIZE, HIDDEN_SIZE, NUM_LAYERS, OUTPUT_SIZE),
    }

    print(f"{'Model':<25s} {'Params':>10s}  {'Output shape':>15s}  {'OK':>4s}")
    print("-" * 60)

    for name, model in models.items():
        model.eval()
        with torch.no_grad():
            out = model(x)
        ok = out.shape == (BATCH, OUTPUT_SIZE)
        assert ok, f"{name}: expected ({BATCH}, {OUTPUT_SIZE}), got {out.shape}"
        params = model.count_parameters()
        print(f"{name:<25s} {params:>10,d}  {str(out.shape):>15s}  {'✓' if ok else '✗':>4s}")

    # AttentionLSTM with teacher forcing
    model_attn = models["AttentionLSTM"]
    model_attn.train()
    target = torch.randn(BATCH, OUTPUT_SIZE)
    out_tf = model_attn(x, teacher_forcing_ratio=0.5, target=target)
    assert out_tf.shape == (BATCH, OUTPUT_SIZE), (
        f"AttentionLSTM (teacher forcing): expected ({BATCH}, {OUTPUT_SIZE}), got {out_tf.shape}"
    )
    print(f"\nAttentionLSTM teacher-forcing check: ✓")

    # Quick ML baseline smoke-tests
    rng = np.random.default_rng(42)
    X_ml = rng.standard_normal((50, INPUT_SIZE))
    y_ml = rng.standard_normal(50)

    for cls_name, cls in [
        ("SVRBaseline", SVRBaseline),
        ("RandomForestBaseline", RandomForestBaseline),
        ("XGBoostBaseline", XGBoostBaseline),
    ]:
        bl = cls()
        bl.fit(X_ml, y_ml)
        pred = bl.predict(X_ml[:5])
        assert pred.shape == (5,), f"{cls_name}: expected (5,), got {pred.shape}"
        print(f"{cls_name:<25s}  predict shape {pred.shape}  ✓")

    # ARIMA / SARIMA need a longer series
    y_ts = rng.standard_normal(200).cumsum()
    arima = ARIMABaseline(order=(2, 1, 0))
    arima.fit(y_ts)
    pred_a = arima.predict(steps=OUTPUT_SIZE)
    assert pred_a.shape == (OUTPUT_SIZE,), f"ARIMA: expected ({OUTPUT_SIZE},), got {pred_a.shape}"
    print(f"{'ARIMABaseline':<25s}  predict shape {pred_a.shape}  ✓")

    sarima = SARIMABaseline(order=(1, 1, 0), seasonal_order=(1, 0, 0, 12))
    sarima.fit(y_ts)
    pred_s = sarima.predict(steps=OUTPUT_SIZE)
    assert pred_s.shape == (OUTPUT_SIZE,), f"SARIMA: expected ({OUTPUT_SIZE},), got {pred_s.shape}"
    print(f"{'SARIMABaseline':<25s}  predict shape {pred_s.shape}  ✓")

    print("\n✅  All self-tests passed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="5G traffic prediction models")
    parser.add_argument(
        "--self-test", action="store_true", help="Run self-test suite",
    )
    args = parser.parse_args()
    if args.self_test:
        _self_test()
