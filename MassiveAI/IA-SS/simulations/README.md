# Scripts de Simulación — Massive AI Model Orchestration para 6G

Scripts Python de validación numérica que reproducen los resultados del artículo:

> **Massive AI Model Orchestration para 6G: Arquitectura Federada para Gestión Dinámica de Foundation Models en Capa Física mediante Cloud-Edge-Device Collaboration**

---

## Requisitos

```bash
pip install numpy matplotlib scikit-learn torch
```

---

## Scripts incluidos

### `script_01_main_comparison.py`
**Comparación principal + análisis de escalabilidad y sensibilidad**

Simula 1 000 usuarios móviles en área urbana de 1 km² con tráfico mixto (40 % eMBB | 30 % URLLC | 30 % mMTC). Compara cuatro estrategias de orquestación:

| Estrategia | Latencia (ms) | Accuracy | Energía (kWh) | SLA viol. (%) |
|---|---|---|---|---|
| Cloud-Only | 78 | 0.95 | 45.0 | 12.0 |
| Edge-Static | 22 | 0.82 | 28.0 | 18.0 |
| Device-Local | 8 | 0.68 | 18.0 | 35.0 |
| **Hybrid-Adaptive** | **12** | **0.89** | **23.0** | **4.0** |

**Figuras generadas:**
- `fig1_baseline_comparison.png` — Comparación de métricas principales
- `fig2_scalability_users.png` — Escalabilidad con número de usuarios (10–2 000)
- `fig3_pareto_frontier.png` — Frontera de Pareto latencia vs. energía
- `fig4_sensitivity_analysis.png` — Análisis de sensibilidad (velocidad, SNR)

**Ejecución:**
```bash
python script_01_main_comparison.py
```

---

### `script_02_handover_prediction_lstm.py`
**Predicción de Handover con LSTM Bidireccional y Atención Temporal**

Implementa un sistema de predicción multi-horizonte de handover. Arquitectura:
1. Embedding (Dense → ReLU, dim=32)
2. Bidirectional LSTM (hidden=128, ventana W=10 pasos)
3. Atención temporal
4. Cabezas multi-horizonte (Softmax para Δt ∈ {1s, 2s, 5s, 10s})

**Resultados clave:**
- Accuracy de predicción >85 % para Δt=5 s (artículo: 87 %)
- Cache hit rate: LRU baseline ≈ 45 % → LRU Predictivo ≈ 78 %

**Figuras generadas:**
- `fig_accuracy_vs_horizon.png` — Accuracy vs horizonte de predicción
- `fig_cache_hit_rate.png` — Tasa de acierto de caché
- `fig_training_curves.png` — Curvas de entrenamiento (loss / accuracy)
- `fig_confusion_matrix.png` — Matriz de confusión para Δt=5 s

**Ejecución:**
```bash
python script_02_handover_prediction_lstm.py
```

---

### `script_03_channel_estimation_vit.py`
**Estimación de Canal en 6G Massive MIMO con Vision Transformer (ViT)**

Modelo de sistema (inspirado en 3GPP CDL-C):
- MIMO: Nt=4 TX, Nr=4 RX antenas
- OFDM: 64 subportadoras, 8 pilotos
- Canal doblemente dispersivo, L=8 paths, fc=3.5 GHz

Compara: LS, MMSE, DNN y **ViT (propuesto)**

**Resultados clave:**
- Mejora MSE de 8–12 dB vs MMSE a alta velocidad Doppler (>100 km/h)
- Mejora de eficiencia espectral del 15–20 %
- Latencia total: 12 ms (8 ms edge + 4 ms comunicación)

**Ejecución:**
```bash
python script_03_channel_estimation_vit.py
```

---

## Figuras generadas

| Figura | Script | Descripción |
|---|---|---|
| `fig1_baseline_comparison.png` | script_01 | Comparación de 4 estrategias (latencia, accuracy, energía, SLA) |
| `fig2_scalability_users.png` | script_01 | Latencia vs número de usuarios |
| `fig3_pareto_frontier.png` | script_01 | Frontera de Pareto latencia-energía |
| `fig4_sensitivity_analysis.png` | script_01 | Análisis de sensibilidad |
| `fig_accuracy_vs_horizon.png` | script_02 | Accuracy de handover por horizonte |
| `fig_cache_hit_rate.png` | script_02 | Tasa de acierto de caché con predicción |
| `fig_training_curves.png` | script_02 | Curvas de pérdida y accuracy durante entrenamiento |
| `fig_confusion_matrix.png` | script_02 | Matriz de confusión (handover, Δt=5 s) |

---

## Ejecutar todos los scripts

```bash
python script_01_main_comparison.py
python script_02_handover_prediction_lstm.py
python script_03_channel_estimation_vit.py
```

Cada script imprime una tabla de resultados con validación PASS/FAIL comparando los valores simulados con los reportados en el artículo (tolerancia ±5 %).
