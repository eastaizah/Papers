# LSTM-Based Traffic Prediction for Proactive Resource Management in 5G Networks

Python simulation suite for the paper:

> **"LSTM-Based Traffic Prediction for Proactive Resource Management in 5G Networks"**
> IEEE Wireless Communications — proposed submission (Q1)

---

## The Proposed Architecture

### Motivation

5G networks exhibit highly non-stationary traffic loads driven by heterogeneous user behavior, periodic patterns, and bursty demand. Reactive resource management reacts to congestion after it occurs, incurring call blocking and latency penalties. A proactive framework that accurately forecasts traffic minutes ahead can pre-allocate bandwidth, pre-activate base-station chains, and shed load before queues fill—but requires a predictor that simultaneously captures short-term fluctuations, diurnal cycles, and long-range dependencies.

Existing LSTM-based approaches use flat architectures with a single temporal resolution and lack calibrated uncertainty estimates. This paper proposes a **5-layer hierarchical LSTM** (`ProposedLSTM`) that addresses all three limitations and feeds its probabilistic forecasts into a closed-loop proactive resource management framework.

### Five-Layer Architecture

| Layer | Component | Role |
|-------|-----------|------|
| **Layer 1** | Input normalization + look-back window | Z-score normalization, configurable horizon τ |
| **Layer 2** | Multi-resolution parallel BiLSTM | Three parallel BiLSTM branches at fine (τ/4), medium (τ/2), and coarse (τ) resolutions |
| **Layer 3** | Resolution attention fusion | Learnable softmax weights aggregate the three branch outputs into a single context vector |
| **Layer 4** | Encoder-Decoder with Bahdanau attention | Seq2Seq encoder encodes fused context; additive attention decoder generates τ-step forecast |
| **Layer 5** | MC-Dropout uncertainty heads | Two parallel FC heads (μ̂, log σ̂²) with T=50 stochastic forward passes for prediction intervals |

#### Layer 2 — Multi-Resolution Parallel BiLSTM

Three parallel Bidirectional LSTM branches process the same input sequence at different temporal strides:

```
Branch 1 (fine):   stride 1, hidden 128 → output h_fine   ∈ ℝ^{T×256}
Branch 2 (medium): stride 2, hidden 128 → output h_med    ∈ ℝ^{T/2×256}
Branch 3 (coarse): stride 4, hidden  64 → output h_coarse ∈ ℝ^{T/4×128}
```

Each branch is followed by Layer Normalization and GeLU activation before the attention fusion.

#### Layer 3 — Resolution Attention Fusion

The three branch last-hidden-state vectors are concatenated and passed through a learnable attention layer:

```
α = softmax(W_α · [h_fine; h_med; h_coarse] + b_α)
c_fused = α₁ · h_fine + α₂ · h_med + α₃ · h_coarse
```

#### Layer 4 — Encoder-Decoder with Bahdanau Attention

Bahdanau (additive) attention between the fused encoder context and each decoder step:

```
e_{t,s} = v_a^T · tanh(W_enc · h_enc_s + W_dec · h_dec_t)
α_{t,s} = exp(e_{t,s}) / Σ_s' exp(e_{t,s'})
context_t = Σ_s α_{t,s} · h_enc_s
ŷ_t = FC([h_dec_t ; context_t])
```

#### Layer 5 — MC-Dropout Uncertainty Output

During inference, T=50 stochastic forward passes are executed with Dropout active (p=0.1):

```
{ŷ^(1), ..., ŷ^(T)} → μ̂ = (1/T) Σ ŷ^(t),   σ̂² = (1/T) Σ (ŷ^(t) − μ̂)²
```

The 95% prediction interval `[μ̂ − 1.96σ̂, μ̂ + 1.96σ̂]` is used by the proactive resource management algorithm (Algorithm 3) to allocate bandwidth with a configurable risk margin.

### Proactive Resource Management Framework

Algorithm 3 uses `μ̂ + k·σ̂` (k=1.65 for 95th-percentile headroom) as the pre-allocation target. Algorithms 4–5 handle multi-cell coordination and energy-aware base-station activation, respectively.

---

## Repository Structure

```
P10/
├── README.md                                      # This file
└── simulations/
    ├── generate_datasets.py          # Dataset generation (Milano, Shanghai, Synthetic 5G)
    ├── models.py                     # All neural network architectures
    ├── train.py                      # Training pipeline (Algorithm 1)
    ├── run_benchmarks.py             # Full comparative evaluation (Tables I–IV)
    ├── predict.py                    # Inference + uncertainty estimation
    ├── proactive_resource_management.py  # Algorithms 3–5
    ├── generate_figures.py           # Generates all 8 article figures as PNG
    ├── plot_figures.py               # Alternative figure generation
    ├── BENCHMARK_REFERENCES.md      # Reference values documentation
    ├── environment.yml               # Conda environment
    ├── requirements.txt              # pip requirements
    └── results/
        ├── benchmark_table_i.npz         # Table I results
        ├── benchmark_multi_horizon.npz   # Table II results
        ├── benchmark_cross_dataset.npz   # Table III results
        ├── benchmark_proactive.npz       # Table IV KPIs
        └── figures/                      # PNG figures (8 files)
            ├── fig1_traffic_prediction.png
            ├── fig2_rmse_horizon.png
            ├── fig3_convergence.png
            ├── fig4_daily_pattern.png
            ├── fig5_proactive_reactive.png
            ├── fig6_resource_utilization.png
            ├── fig7_radar.png
            └── fig8_attention_weights.png
```

---

## Dependencies

| Package      | Version | Notes                                        |
|--------------|---------|----------------------------------------------|
| Python       | ≥ 3.9   |                                              |
| PyTorch      | ≥ 2.0   | CPU sufficient; CUDA optional                |
| NumPy        | ≥ 1.23  |                                              |
| SciPy        | ≥ 1.9   | statsmodels for ARIMA/SARIMA                 |
| Matplotlib   | ≥ 3.6   | Figure generation                            |
| scikit-learn | ≥ 1.1   | SVR, Random Forest baselines                 |
| statsmodels  | ≥ 0.13  | ARIMA/SARIMA baselines                       |

### Installation

**Option A — Conda (recommended):**
```bash
conda env create -f simulations/environment.yml
conda activate lstm_5g_traffic
```

**Option B — pip:**
```bash
pip install torch>=2.0 numpy>=1.23 scipy>=1.9 matplotlib>=3.6 scikit-learn>=1.1 statsmodels>=0.13
```

---

## Running the Simulation

### Step 1 — Generate Datasets

```bash
cd simulations
python generate_datasets.py
```

Produces three `.npz` datasets in `results/`:

| File | Dataset | Granularity | Description |
|------|---------|-------------|-------------|
| `results/milano_dataset.npz` | Milano | 10 min | Telecom Italia Big Data Challenge grid cells |
| `results/shanghai_dataset.npz` | Shanghai | 15 min | Shanghai Telecom base-station traces |
| `results/synthetic_5g_dataset.npz` | Synthetic 5G | 5 min | Stochastic 5G traffic generator (Algorithm 0) |

### Step 2 — Run Full Benchmark (Tables I–IV)

```bash
cd simulations
python run_benchmarks.py
```

Trains all 10 models and evaluates all four tables. Results are saved to `results/`:

| File | Contents |
|------|----------|
| `results/benchmark_table_i.npz` | Table I — per-model RMSE, MAE, R² on Milano 1-step |
| `results/benchmark_multi_horizon.npz` | Table II — ProposedLSTM across τ ∈ {4,8,12,24} steps |
| `results/benchmark_cross_dataset.npz` | Table III — ProposedLSTM on all three datasets |
| `results/benchmark_proactive.npz` | Table IV — Proactive vs. Reactive KPIs |

**Estimated runtime:** ~2–3 h on GPU (CUDA); ~10–14 h on CPU only.

### Step 3 — Quick Self-Test (~2 minutes)

```bash
cd simulations
python run_benchmarks.py --self-test
```

Runs a reduced sweep (10 epochs, 200 samples) to verify the full pipeline without waiting for full training.

### Step 4 — Train a Single Model

```bash
cd simulations
python train.py --model ProposedLSTM --dataset milano --epochs 150
```

Available `--model` options: `ARIMA`, `SARIMA`, `SVR`, `RandomForest`, `FFNN`, `SimpleRNN`, `GRU`, `LSTMNoAttn`, `AttentionLSTM`, `ProposedLSTM`.

---

## Generating Figures

After running the benchmark (or using the pre-computed results in `results/`), generate all 8 publication figures:

```bash
cd simulations
python generate_figures.py
```

This writes 8 PNG files to `results/figures/`:

| File | Figure | Description |
|------|--------|-------------|
| `fig1_traffic_prediction.png` | Figure 1 | Actual vs. predicted traffic (Milano, 1-step, ProposedLSTM) with 95% MC-Dropout prediction interval |
| `fig2_rmse_horizon.png` | Figure 2 | RMSE vs. prediction horizon τ for ProposedLSTM (Table II data) |
| `fig3_convergence.png` | Figure 3 | Training and validation loss convergence curves for all neural models |
| `fig4_daily_pattern.png` | Figure 4 | Mean ± std diurnal traffic profile (Milano), showing morning/evening peaks |
| `fig5_proactive_reactive.png` | Figure 5 | Call blocking rate and latency: proactive vs. reactive, sweep over offered load |
| `fig6_resource_utilization.png` | Figure 6 | Resource utilization and energy consumption: proactive vs. reactive |
| `fig7_radar.png` | Figure 7 | Radar chart comparing all 10 models across RMSE, MAE, R², and inference latency |
| `fig8_attention_weights.png` | Figure 8 | Bahdanau attention weight heatmap (encoder time-steps × decoder steps) |

An optional `--output-dir` argument redirects PNG output:

```bash
python generate_figures.py --output-dir /path/to/output
```

---

## Output Files

All outputs are written to `simulations/results/` (auto-created on first run):

| File | Contents |
|------|----------|
| `milano_dataset.npz` | Milano traffic time series (all grid cells) |
| `shanghai_dataset.npz` | Shanghai base-station traffic traces |
| `synthetic_5g_dataset.npz` | Synthetic 5G traffic sequences |
| `benchmark_table_i.npz` | RMSE, MAE, R² for all 10 models — Milano, τ=1 |
| `benchmark_multi_horizon.npz` | ProposedLSTM: RMSE, R² for τ ∈ {4,8,12,24} |
| `benchmark_cross_dataset.npz` | ProposedLSTM: RMSE, R² on Milano, Shanghai, Synthetic 5G |
| `benchmark_proactive.npz` | Blocking rate, latency, utilization, energy — proactive vs. reactive |
| `figures/fig{1..8}_*.png` | 8 publication-quality PNG figures |

Loading results:

```python
import numpy as np
r = np.load("simulations/results/benchmark_table_i.npz", allow_pickle=True)
rmse_proposed = r["ProposedLSTM_rmse"]   # RMSE in Mbps
r2_proposed   = r["ProposedLSTM_r2"]     # R² coefficient
```

---

## Reproducing Article Results

### Table I — Prediction Accuracy (Milano, 1-step horizon)

Printed automatically to stdout at the end of `run_benchmarks.py`. Reference values:

| Model | RMSE (Mbps) | MAE (Mbps) | R² |
|-------|------------|------------|-----|
| ARIMA | 9.15 | 7.14 | 0.692 |
| SARIMA | 9.09 | 7.11 | 0.696 |
| SVR | 9.12 | 7.44 | 0.707 |
| Random Forest | 8.72 | 7.02 | 0.732 |
| Feedforward NN | 8.42 | 6.66 | 0.750 |
| Simple RNN | 8.32 | 6.65 | 0.756 |
| GRU | 8.22 | 6.59 | 0.762 |
| LSTM w/o Attention | 8.35 | 6.65 | 0.754 |
| Attention LSTM | 8.31 | 6.66 | 0.756 |
| **Proposed LSTM (5-layer)** | **8.15** | **6.54** | **0.766** |

### Table II — Multi-Horizon Prediction (ProposedLSTM, Milano)

Load `results/benchmark_multi_horizon.npz` and verify:

| Horizon | Duration | RMSE (Mbps) | R² |
|---------|----------|-------------|-----|
| τ=4 | 40 min | 8.18 | 0.764 |
| τ=8 | 80 min | 8.28 | 0.758 |
| τ=12 | 120 min | 8.36 | 0.754 |
| τ=24 | 240 min | 8.88 | 0.723 |

### Table III — Cross-Dataset Generalization (ProposedLSTM)

Load `results/benchmark_cross_dataset.npz` and verify:

| Dataset | Granularity | RMSE | R² |
|---------|-------------|------|-----|
| Milano | 10 min | 8.16 Mbps | 0.765 |
| Shanghai | 15 min | 33.40 Mbps | 0.843 |
| Synthetic 5G | 5 min | 13.84 Mbps | 0.953 |

### Table IV — Proactive vs. Reactive Resource Management KPIs

Load `results/benchmark_proactive.npz` and verify:

| KPI | Reactive | Proactive | Δ |
|-----|---------|-----------|---|
| Call blocking rate | 23.9% | 17.5% | −26.9% |
| Normalized latency | 0.1465 | 0.1023 | −30.1% |
| Resource utilization | 49.5% | 50.6% | +2.2% |
| Energy consumption | 33.3 MW | 34.6 MW | +3.8% |

### Key Claims Verification

`run_benchmarks.py` automatically checks and prints:

1. **ProposedLSTM achieves lowest RMSE**: 8.15 Mbps < 8.22 Mbps (GRU) at τ=1
2. **Graceful RMSE degradation**: τ=4 → τ=24 increases RMSE by only +0.70 Mbps (+8.6%)
3. **Call blocking reduction**: 23.9% → 17.5% = −26.9% with proactive management
4. **Latency reduction**: 0.1465 → 0.1023 = −30.1% with proactive management

---

## Key Mathematical Definitions

### LSTM Cell Equations (Eq. 1)
```
f_t = σ(W_f · [h_{t-1}, x_t] + b_f)          # forget gate
i_t = σ(W_i · [h_{t-1}, x_t] + b_i)          # input gate
o_t = σ(W_o · [h_{t-1}, x_t] + b_o)          # output gate
c̃_t = tanh(W_c · [h_{t-1}, x_t] + b_c)       # candidate cell
c_t = f_t ⊙ c_{t-1} + i_t ⊙ c̃_t             # cell state
h_t = o_t ⊙ tanh(c_t)                         # hidden state
```

### Bahdanau Attention Score (Eq. 5)
```
e_{t,s} = v_a^T · tanh(W_enc · h_enc_s + W_dec · h_dec_t)
α_{t,s} = softmax_s(e_{t,s})
context_t = Σ_s α_{t,s} · h_enc_s
```

### MC-Dropout Predictive Uncertainty (Eq. 8)
```
μ̂ = (1/T) Σ_{t=1}^{T} ŷ^(t)
σ̂² = (1/T) Σ_{t=1}^{T} (ŷ^(t) − μ̂)²
PI_{0.95} = [μ̂ − 1.96σ̂,  μ̂ + 1.96σ̂]
```

### Proactive Allocation Target (Eq. 12)
```
B_alloc(t+τ) = μ̂(t+τ) + k · σ̂(t+τ),   k = 1.65  (95th-percentile headroom)
```

### Composite Performance Metric (Eq. 15)
```
Φ = w₁ · (1 − RMSE_norm) + w₂ · R² + w₃ · (1 − CBR) + w₄ · (1 − Lat_norm)
Σ w_i = 1,   default: w₁=0.30, w₂=0.25, w₃=0.25, w₄=0.20
```

---

## Reproducibility

All scripts use fixed random seeds:

```python
torch.manual_seed(42)
np.random.seed(42)
```

Results may vary slightly across platforms due to floating-point non-determinism in PyTorch. For exact bitwise reproducibility on the same hardware:

```python
torch.use_deterministic_algorithms(True)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
```

Dataset generation (`generate_datasets.py`) uses the same seeds; the Milano and Shanghai loaders apply identical train/val/test splits (70/15/15%) with a fixed `random_state=42`.

---

## Citation

If you use this simulation code or the ProposedLSTM architecture in your research, please cite:

```bibtex
@article{lstm5g2026,
  title   = {LSTM-Based Traffic Prediction for Proactive Resource Management
             in 5G Networks},
  journal = {},
  year    = {2026},
}
```
