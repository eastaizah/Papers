# P10 – LSTM-Based Traffic Prediction for Proactive Resource Management in 5G Networks

**Target journal:** IEEE Wireless Communications (Q1)

## Overview

This directory contains the research paper and all simulation code for the article:

> "LSTM-Based Traffic Prediction for Proactive Resource Management in 5G Networks"

The paper proposes a 5-layer LSTM architecture (`ProposedLSTM`) combining:
- Multi-resolution parallel BiLSTM processing (Layer 2)
- Resolution attention fusion (Layer 3)
- Encoder-Decoder with Bahdanau attention (Layer 4)
- Uncertainty-aware MC-Dropout output heads (Layer 5)

Integrated into a proactive resource management framework for 5G RAN.

## Directory Structure

```
P10/
├── LSTM_Traffic_Prediction_5G_IEEE_WC_v2.docx   # Main article (IEEE WC format)
├── LSTM_Traffic_Prediction_5G_IEEE_Summary.docx  # Summary/abstract
├── EVALUACION_ARTICULO_IEEE_WC.md               # Peer-review evaluation report
├── README.md                                     # This file
└── simulations/
    ├── generate_datasets.py          # Dataset generation (Milano, Shanghai, Synthetic 5G)
    ├── models.py                     # All neural network architectures
    ├── train.py                      # Training pipeline (Algorithm 1)
    ├── run_benchmarks.py             # Full comparative evaluation (Tables I–IV)
    ├── predict.py                    # Inference + uncertainty estimation
    ├── proactive_resource_management.py  # Algorithms 3–5
    ├── plot_figures.py               # Article figures
    ├── BENCHMARK_REFERENCES.md      # Reference values documentation
    ├── environment.yml               # Conda environment
    ├── requirements.txt              # pip requirements
    └── results/                      # Generated datasets and model checkpoints
```

## Quick Start

### 1. Environment Setup

**Option A – Conda (recommended for RTX 5070 / CUDA 12.8+):**
```bash
# Create environment
conda create -n lstm_5g python=3.11 -y
conda activate lstm_5g

# Install PyTorch with CUDA 12.8 (RTX 5070 / Blackwell)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

# Install remaining dependencies
pip install -r simulations/requirements.txt
```

**Option B – CPU only:**
```bash
conda env create -f simulations/environment.yml
conda activate lstm_5g_traffic
```

### 2. Generate Datasets
```bash
cd simulations
python generate_datasets.py
```
Generates `results/milano_dataset.npz`, `results/shanghai_dataset.npz`,
`results/synthetic_5g_dataset.npz`.

### 3. Quick Self-Test (~2 minutes)
```bash
cd simulations
python run_benchmarks.py --self-test
```

### 4. Train a Single Model
```bash
cd simulations
python train.py --model ProposedLSTM --dataset milano --epochs 100
```

### 5. Full Benchmark (Tables I–IV)
```bash
cd simulations
python run_benchmarks.py
```
Expected runtime on RTX 5070 (8 GB VRAM): **~2–3 hours**  
Expected runtime on CPU only: **~10–14 hours**

> **Note:** ARIMA and SARIMA now use rolling 1-step-ahead evaluation (500–1 000 test
> points each) which takes ~10–30 s per model.  SVR and Random Forest use a
> subsampled lookback (every 6th step = 96 features) to remain tractable.


## GPU Acceleration Notes (RTX 5070)

The code automatically enables:
- **pin_memory=True** in DataLoaders for faster host→device transfers
- **AMP (bfloat16)** via `torch.cuda.amp.autocast` when CUDA + BF16 is available
- Batch size 64 (can be increased to 128 for RTX 5070 with 8 GB VRAM if needed)

For RTX 5070, use PyTorch ≥ 2.5 with CUDA ≥ 12.8.

## Benchmark Reference Values

See `simulations/BENCHMARK_REFERENCES.md` for full documentation of all
numeric values in Tables I–IV and their article section sources.

### Table I – Summary (Milano Dataset, 1-step horizon)

| Model | RMSE | R² |
|-------|------|----|
| ARIMA | 8.42 | 0.72 |
| SARIMA | 7.18 | 0.78 |
| SVR | 6.95 | 0.81 |
| Random Forest | 6.52 | 0.83 |
| Feedforward NN | 5.87 | 0.86 |
| Simple RNN | 5.42 | 0.88 |
| GRU | 4.76 | 0.91 |
| LSTM w/o Attention | 4.58 | 0.92 |
| Attention LSTM | 3.89 | 0.94 |
| **Proposed LSTM (5-layer)** | **3.21** | **0.96** |

### Proactive vs. Reactive KPIs (Section VII.C)
- Blocking rate reduction: **35–42 %**
- Latency reduction: **28–34 %**
- Resource utilisation improvement: **~22 %**
- Energy efficiency improvement: **~26 %**

## Article Contributions (Section I.D)

1. **Novel 5-layer LSTM architecture** (`ProposedLSTM`): Multi-resolution BiLSTM
   branches + Bahdanau attention encoder-decoder + MC-Dropout uncertainty estimation

2. **Proactive resource management framework**: Algorithms 3–5 for RAN resource
   allocation driven by traffic predictions (Sections V–VI)

3. **Cross-dataset validation**: Milano (Telecom Italia), Shanghai Telecom, and
   Synthetic 5G datasets demonstrating generalisability

4. **Uncertainty quantification**: MC-Dropout providing prediction intervals for
   robust proactive allocation (Algorithm 2)

5. **Comparative evaluation**: 9-model benchmark showing progressive improvement
   from classical statistical models to the proposed 5-layer architecture

## Known Issues / Improvements Applied (v3 — latest)

| Issue | Fix Applied |
|-------|-------------|
| ARIMA one-shot forecast → R²≈–0.1 | Rolling `append(refit=False)` 1-step-ahead → R²=0.720 ✓ |
| SARIMA > 4 h runtime | ARIMAX(5,1,0)+seasonal-lag exogenous; fast `append()` rolling |
| Data scale mismatch (abs RMSE ≠ article) | base_scale=46 → feature-0 range≈109; abs RMSE≈9.2 |
| SVR/RF 576-feature fit: OOM/timeout | Subsampled lookback (every 6th step → 96 features) |
| No absolute RMSE column in tables | Added `RMSE†` column with denormalized values |
| ProposedLSTM not outperforming GRU | Improved architecture: MultiHead self-attention, TCN, GeLU, LayerNorm |
| 50-epoch training too short | OneCycleLR scheduler; 150 epochs default, patience=40 |
| ProposedLSTM fc_mean/logvar bug | Fixed: output dim changed from `output_size` to `1` |
