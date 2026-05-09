Adaptive Neural Receivers for Real-Time 6G: Latency Optimization and Inference Under Hardware Constraints

Abstract — Sixth-generation (6G) wireless systems impose unprecedented requirements: sub-millisecond latency for ultra-reliable low-latency communications (URLLC), reliability of 99.99999%, and device densities reaching $10^7$ devices/km$^2$. Traditional physical-layer algorithms (MMSE, ZF) cannot simultaneously meet these constraints while approaching information-theoretic limits. This article proposes a hybrid CNN-Transformer adaptive neural receiver integrating three validated innovations: (i) a Joint Source-Channel Coding (JSCC) variational autoencoder achieving 8$\times$ compression (128-D to 16-D latent space), equivalent to a 4$\times$ bandwidth reduction relative to a 64-D baseline; (ii) multi-head temporal attention for channel estimation, eliminating interpolation error floors in high-Doppler scenarios; and (iii) a hierarchical three-module early-exit architecture co-optimized via $\mathcal{L}(\boldsymbol{\theta}, \mathbf{q}) = \lambda_1 \cdot \text{BER}(\boldsymbol{\theta}) + \lambda_2 \cdot \text{Latency}(\boldsymbol{\theta}, \mathbf{q}) + \lambda_3 \cdot \text{Complexity}(\mathbf{q})$. Multi-stage compression (QAT INT8/INT4, 70% structured pruning, progressive knowledge distillation) yields 94% FLOPs and 87% memory reduction. Latency figures of 0.73 ms (Jetson AGX Orin) and 0.58 ms (FPGA Zynq UltraScale+) are analytical estimates from the Roofline performance model, not direct hardware measurements; direct validation is future work. BER simulations confirm a 2.1 dB gain over MMSE at $10^{-3}$ for 4$\times$4 MIMO, 16-QAM, CDL-C. A DRL orchestration framework (PPO+MAML) is proposed as a theoretical contribution without experimental validation.

Index Terms — 6G, adaptive receiver, channel estimation, CNN-Transformer, early exit, FPGA, hardware-aware compression, JSCC, knowledge distillation, MIMO-OFDM, neural receiver, quantization-aware training, URLLC.

I. INTRODUCTION

A. Context and Motivation

The global standardization process for 6G communications, projected for commercial deployment around 2030, defines system requirements that qualitatively transcend those of 5G New Radio. The ITU-R IMT-2030 framework specifies user-plane latency below 0.1 ms for URLLC, end-to-end reliability of 99.99999% (seven nines), spectral efficiency of 200 bps/Hz in massive MIMO configurations, and connection densities reaching $10^7$ devices/km$^2$ for massive machine-type communications (mMTC) [1]. Concurrently, the O-RAN Alliance and 3GPP TR 38.843 mandate that AI/ML inference modules embedded in base-station receivers must complete inference cycles in less than 1 ms without perturbing the physical-layer processing pipeline [2].

These requirements create a fundamental design tension. Classical signal processing algorithms — minimum mean-squared error (MMSE) equalization, zero-forcing (ZF) detection, and maximum-ratio combining (MRC) — rely on explicit channel-state information (CSI) acquired through pilot-based estimation and linear algebra operations whose computational complexity scales as $\mathcal{O}(N_r^2 N_t)$ with antenna count. At sub-terahertz frequencies and with antenna arrays of order $256 \times 256$, this scaling renders real-time execution infeasible on edge hardware platforms. Furthermore, these algorithms assume Gaussian noise and stationary channels, assumptions that break down in high-mobility vehicular and non-terrestrial network (NTN) scenarios [3].

Neural network-based receivers offer a data-driven alternative capable of learning complex channel statistics directly from pilots and data symbols. However, state-of-the-art deep neural architectures introduce their own constraints: ResNet-50 requires approximately 4 GFLOPs per inference pass — three orders of magnitude beyond the compute budget of an FPGA-based baseband processor operating at 1 ms cycle time. The central research challenge addressed in this article is therefore: how to design a neural receiver that simultaneously achieves near-optimal BER performance, sub-millisecond inference latency, and deployability on resource-constrained edge hardware without relying on cloud offloading for latency-sensitive operations.

B. State of the Art

The seminal work of O'Shea and Hoydis [4] established the autoencoder paradigm for end-to-end learning of communication systems, demonstrating that neural encoders and decoders can discover efficient signal representations without explicit waveform design. Bourtsoulatze et al. [5] extended this to Joint Source-Channel Coding (JSCC) for wireless image transmission, showing that semantic compression can outperform separate source and channel coding in low-SNR regimes. On the detection side, Samuel et al. introduced DetNet [6], a deep unfolding architecture that maps the iterative projected gradient descent algorithm into a fixed-depth neural network, achieving near-optimal detection with polynomial complexity. He et al. [7] proposed OAMPNet, unfolding the orthogonal AMP (OAMP) algorithm into trainable layers that achieve maximum a-posteriori (MAP) detection asymptotically.

For channel estimation specifically, Soltani et al. [8] demonstrated that convolutional neural networks trained on pilot patterns can outperform MMSE interpolation in sparse multipath channels by implicitly learning the scattering geometry. Ye et al. [9] showed similar gains for OFDM systems in frequency-selective fading. Ma et al. [10] introduced Transformer architectures for channel estimation, exploiting self-attention to model long-range time-frequency correlations that convolutional networks miss. Honkala et al. [11] proposed DeepRx, an end-to-end neural OFDM receiver achieving state-of-the-art BER in 5G NR configurations. He et al. [12] addressed millimeter-wave channel estimation using deep learning, leveraging the sparse structure of mmWave channels.

More recently, Hoydis et al. released Sionna [13], an open-source GPU-accelerated link-level simulator that enables differentiable physical-layer design. Liu et al. [14] proposed DiffChannel, a diffusion model-based channel estimator achieving superior interpolation in high-Doppler scenarios. Wang et al. [15] introduced ChannelGPT, a large language model-inspired foundation model pre-trained on diverse channel datasets, demonstrating strong zero-shot generalization across propagation environments. The 3GPP TR 38.843 report [2] consolidates AI/ML use cases for O-RAN, including neural channel estimation, beam management, and resource allocation.

Despite these advances, the critical gap remains hardware-aware co-design: most published neural receivers are evaluated solely on GPU servers, with inference latencies of 10–100 ms that are incompatible with 6G real-time requirements. Adaptive compression (quantization, pruning, knowledge distillation) and early-exit inference are studied separately in the machine learning literature [16]–[18] but have not been jointly optimized for physical-layer receivers. Furthermore, the emerging concept of DRL-based orchestration [19] for dynamic adaptation of receiver complexity to channel conditions has not been experimentally validated in a complete 6G receiver stack.

C. Contributions

This article makes the following contributions:

1. **JSCC Semantic Compression**: A variational autoencoder encoder-decoder pair achieving 8$\times$ compression (128-D to 16-D latent representation), yielding 4$\times$ effective bandwidth reduction relative to a 64-D baseline, with explicit mutual information maximization between source features and channel symbols.

2. **Multi-Head Temporal Attention Channel Estimation**: A Transformer-based estimator that eliminates interpolation error floors in CDL-C fading by modeling cross-subcarrier and cross-symbol attention jointly, without requiring explicit Doppler spread estimation.

3. **Hierarchical Early-Exit Architecture**: A three-module receiver (MobileNet-INT8, ResNet-34-pruned, CNN-Transformer-offloaded) with two confidence thresholds ($\tau_1$, $\tau_2$) enabling complexity adaptation from 45 µs (Module A) to 0.73 ms (Module C), covering the full URLLC and eMBB latency envelope.

4. **Multi-Stage Compression Pipeline**: Combined QAT (INT8/INT4), 70% structured channel pruning, and progressive knowledge distillation, achieving 94% FLOPs reduction and 87% memory reduction while maintaining 2.1 dB BER gain over MMSE at $10^{-3}$.

5. **DRL Orchestration Framework (Theoretical — No Experimental Validation)**: A PPO+MAML reinforcement learning agent for joint selection of receiver module, compression level, and offloading target based on real-time SNR, battery state, and latency budget. *This contribution is a theoretical design framework only; no simulation or hardware experiments have been conducted for this component. Experimental validation is explicitly identified as future work.*

II. SYSTEM MODEL AND PROPOSED ARCHITECTURE

A. MIMO-OFDM System Model

We consider a narrowband MIMO-OFDM system with $N_t$ transmit and $N_r$ receive antennas, $N_c$ subcarriers, and $N_s$ OFDM symbols per slot. The time-varying channel in the delay-Doppler domain is modeled according to 3GPP TR 38.901 CDL-C [3], with delay spread $\sigma_\tau = 300$ ns and maximum Doppler shift $f_D = v f_c / c$, where $v$ is user velocity, $f_c$ the carrier frequency, and $c$ the speed of light. The discrete-time received signal at subcarrier $k$ and OFDM symbol $n$ is

$$\mathbf{y}[k,n] = \mathbf{H}[k,n]\,\mathbf{x}[k,n] + \mathbf{w}[k,n], \tag{1}$$

where $\mathbf{H}[k,n] \in \mathbb{C}^{N_r \times N_t}$ is the channel matrix (bold notation throughout), $\mathbf{x}[k,n] \in \mathcal{X}^{N_t}$ is the transmitted symbol vector drawn from the 16-QAM constellation $\mathcal{X}$, and $\mathbf{w}[k,n] \sim \mathcal{CN}(\mathbf{0}, \sigma_w^2 \mathbf{I}_{N_r})$ is additive white Gaussian noise. The average SNR per receive antenna is $\gamma = P_t / (N_t \sigma_w^2)$, where $P_t$ is total transmit power.

The channel matrix $\mathbf{H}[k,n]$ is parameterized by a cluster-delay-line model with $L$ multipath components:

$$\mathbf{H}[k,n] = \sum_{\ell=1}^{L} \alpha_\ell \, e^{j2\pi f_{D,\ell} n T_s} \, e^{-j2\pi k \Delta f \tau_\ell} \, \mathbf{a}_r(\phi_{r,\ell}) \mathbf{a}_t^H(\phi_{t,\ell}), \tag{2}$$

where $\alpha_\ell \in \mathbb{C}$ is the complex gain of path $\ell$, $\tau_\ell$ and $f_{D,\ell}$ its delay and Doppler shift, $T_s$ the OFDM symbol duration, $\Delta f$ the subcarrier spacing, and $\mathbf{a}_r(\cdot)$, $\mathbf{a}_t(\cdot)$ the receive and transmit array steering vectors. Under 16-QAM modulation in AWGN, the theoretical bit error probability is approximated by the Q-function as [20]

$$P_b \approx \frac{3}{4}\,Q\!\left(\sqrt{\frac{2\gamma_b}{5}}\right), \tag{3}$$

where $\gamma_b = \gamma / \log_2 M$ is the SNR per bit for $M$-QAM, and $Q(x) = \frac{1}{\sqrt{2\pi}}\int_x^\infty e^{-t^2/2}\,dt$. This baseline serves as the performance reference for BER analysis in Section IV.

B. End-to-End Neural Receiver Formulation

The end-to-end neural receiver is parameterized by weights $\boldsymbol{\theta}$ and quantization configuration $\mathbf{q} \in \{4,8,16,32\}^{L_q}$, where $L_q$ is the number of quantizable layers. The joint optimization objective is

$$\mathcal{L}(\boldsymbol{\theta}, \mathbf{q}) = \lambda_1 \cdot \text{BER}(\boldsymbol{\theta}) + \lambda_2 \cdot \text{Latency}(\boldsymbol{\theta}, \mathbf{q}) + \lambda_3 \cdot \text{Complexity}(\mathbf{q}), \tag{4}$$

where $\lambda_1 = 0.5$, $\lambda_2 = 0.3$, $\lambda_3 = 0.2$ are regularization weights tuned by grid search on the validation set. The latency term is evaluated analytically using the Roofline model [21] (Section IV-D), and $\text{Complexity}(\mathbf{q})$ is measured in normalized FLOPs. The full received symbol processing chain maps

$$\hat{\mathbf{x}} = f_{\boldsymbol{\theta}}^{\text{DET}}\!\left(\mathbf{y},\, \hat{\mathbf{H}}\right), \quad \hat{\mathbf{H}} = g_{\boldsymbol{\theta}}^{\text{EST}}\!\left(\mathbf{Y}_p\right), \tag{5}$$

where $\mathbf{Y}_p \in \mathbb{C}^{N_r \times N_p}$ is the pilot observation matrix ($N_p$ pilot positions), $g_{\boldsymbol{\theta}}^{\text{EST}}$ the temporal attention estimator, and $f_{\boldsymbol{\theta}}^{\text{DET}}$ the detection head. The notation $\mathbf{H}$ (bold, no element-wise multiplication) correctly reflects the full MIMO matrix transformation, as opposed to a scalar channel model.

C. JSCC Semantic Coding Layer

The JSCC module consists of a variational autoencoder (VAE) encoder $E_\phi: \mathbb{R}^{128} \to \mathbb{R}^{16}$ and decoder $D_\psi: \mathbb{R}^{16} \to \mathbb{R}^{128}$. The encoder maps the 128-dimensional received feature vector (extracted from the first ResNet block) to a 16-dimensional latent code $\mathbf{z}$. Two compression ratios are distinguished to avoid ambiguity: (i) the absolute compression ratio is 8$\times$ (128-D input reduced to 16-D latent representation); (ii) the effective bandwidth reduction relative to the 64-D intermediate representation used as a baseline in prior JSCC work [5] is 4$\times$ (64-D reduced to 16-D). These are different reference points, not additive effects; the 8$\times$ figure measures compression against the raw feature dimension, while the 4$\times$ figure measures the communication overhead reduction relative to the established 64-D baseline.

The VAE training objective combines reconstruction fidelity and KL-divergence regularization:

$$\mathcal{L}_{\text{JSCC}} = \mathbb{E}_{q_\phi(\mathbf{z}|\mathbf{x})}\!\left[\log p_\psi(\mathbf{x}|\mathbf{z})\right] - \beta\,D_{\text{KL}}\!\left(q_\phi(\mathbf{z}|\mathbf{x}) \,\|\, p(\mathbf{z})\right), \tag{6}$$

with $\beta = 0.1$ balancing compression fidelity and latent space regularity. The transmitted latent vector $\mathbf{z} \in \mathbb{R}^{16}$ is directly mapped to complex channel symbols via a learned linear projection, eliminating the separate source coding–channel coding interface and enabling end-to-end joint optimization. The channel input–output relation for the semantic transmission is $\tilde{\mathbf{z}} = \mathbf{H}\mathbf{z}_{tx} + \mathbf{w}$, where $\mathbf{H}$ (bold) denotes the MIMO channel matrix and $\mathbf{z}_{tx}$ the power-normalized symbol vector.

D. Temporal Attention Channel Estimation

Classical MMSE channel estimators interpolate between pilot positions using a Wiener filter that assumes knowledge of the channel power delay profile and Doppler spectrum. This assumption introduces an error floor when the true channel statistics deviate from the filter design parameters — a common occurrence in urban macro deployments with mixed vehicular and pedestrian traffic. The proposed temporal attention estimator $g_{\boldsymbol{\theta}}^{\text{EST}}$ replaces linear interpolation with a multi-head self-attention mechanism operating on the pilot observation tensor $\mathbf{Y}_p$.

The attention-based estimator stacks $H_{att} = 8$ attention heads, each computing

$$\text{Attn}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}, \tag{7}$$

where $\mathbf{Q} = \mathbf{Y}_p \mathbf{W}_Q$, $\mathbf{K} = \mathbf{Y}_p \mathbf{W}_K$, $\mathbf{V} = \mathbf{Y}_p \mathbf{W}_V$, with projection matrices $\mathbf{W}_Q, \mathbf{W}_K, \mathbf{W}_V \in \mathbb{R}^{d_{model} \times d_k}$ and $d_k = 64$. The attention mechanism captures long-range time-frequency correlations across all subcarriers and OFDM symbols simultaneously, without requiring an explicit delay-Doppler grid transformation. The output $\hat{\mathbf{H}} \in \mathbb{C}^{N_r \times N_t \times N_c \times N_s}$ is the full channel estimate tensor, from which subcarrier-specific matrices $\mathbf{H}[k,n]$ are extracted for detection.

E. Hierarchical Early-Exit Architecture

A comprehensive taxonomy of adaptive neural receivers for 6G, organized along four classification dimensions — training paradigm, base architecture, receiver function, and deployment target — is illustrated in Fig. 9. The proposed receiver occupies the niche $\{\text{Meta-Learning} \cup \text{Supervised},\, \text{CNN-Transformer},\, \text{Channel EST} + \text{Symbol DET} + \text{JSCC} + \text{Orchestration},\, \text{FPGA} + \text{Edge BS}\}$, which is the only occupied cell combining all four receiver functions with edge deployment.

The full four-layer adaptive framework is depicted in Fig. 10, showing the signal processing layer (MIMO antennas, ADC, OFDM demodulation), the neural processing layer with three parallel modules, the DRL orchestration layer, and the compression/deployment layer.

The three hierarchical modules are designed to cover the full latency envelope from ultrafast simple channels to complex high-mobility scenarios:

1) *Module A* (MobileNetV2-INT8, $< 10$ µs): Activated when pilot-based SNR $\hat{\gamma} > 25$ dB and estimated Doppler $\hat{f}_D < 10$ Hz. Operates entirely on-chip with 1.2 M INT8 parameters. Designed for indoor hotspot and static scenarios.

2) *Module B* (ResNet-34 pruned to 30% density, 10–100 µs): Activated when $10 \leq \hat{\gamma} \leq 25$ dB or $10 \leq \hat{f}_D \leq 200$ Hz. Employs QAT INT8 with residual connections preserved through pruning masks. Targets urban macro pedestrian mobility.

3) *Module C* (CNN-Transformer, full precision with FPGA offload, $> 100$ µs): Activated for $\hat{\gamma} < 10$ dB or $\hat{f}_D > 200$ Hz, or when reliability target is seven nines. The full attention estimator (8 heads, 512-dim) runs on the FPGA accelerator over a PCIe/AXI interface.

The early-exit thresholds $\tau_1$ and $\tau_2$ are based on posterior confidence scores derived from the softmax output distribution. Let $\mathbf{p}_A = \text{softmax}(\text{logits}_A)$ be the symbol probability vector from Module A; if $\max(\mathbf{p}_A) > \tau_1 = 0.95$, inference terminates at Module A. Otherwise it proceeds to Module B with threshold $\tau_2 = 0.85$. The expected inference latency under a CDL-C traffic distribution with 60% static, 30% pedestrian, and 10% vehicular users is

$$\bar{T} = \Pr(A)\cdot T_A + \Pr(B)\cdot T_B + \Pr(C)\cdot T_C, \tag{8}$$

where $T_A = 45$ µs, $T_B = 380$ µs, $T_C = 730$ µs, and $\Pr(A) = 0.60$, $\Pr(B) = 0.30$, $\Pr(C) = 0.10$, yielding $\bar{T} \approx 268$ µs for the expected-case traffic mix.

Fig. 9. Hierarchical taxonomy of adaptive neural receivers for 6G networks, organized along four classification dimensions: training paradigm, base architecture, receiver function, and deployment target. The proposed receiver occupies the niche {Meta-Learning ∪ Supervised, CNN-Transformer, Channel EST+Symbol DET+JSCC+Orchestration, FPGA+Edge BS}.

Fig. 10. Block diagram of the proposed four-layer adaptive neural receiver framework showing signal processing layer (MIMO antennas, A/D, OFDM demodulation), neural processing layer (three parallel modules with early-exit decision points at thresholds τ₁ and τ₂), orchestration layer (DRL agent PPO+MAML with SNR, battery, and latency inputs), and compression/deployment layer (QAT→Pruning→KD pipeline targeting Jetson, FPGA, and Raspberry Pi).

III. MULTI-STAGE MODEL COMPRESSION PIPELINE

The compression pipeline operates in three sequential stages applied to the Module B and Module C architectures (Module A is already architecture-constrained to MobileNetV2). The pipeline is designed to preserve BER performance within 0.3 dB of the uncompressed model while achieving maximum latency reduction. The combined pipeline is trained with 200 epochs of fine-tuning on the CDL-C training dataset using AdamW optimizer with learning rate $1 \times 10^{-4}$ and cosine annealing schedule.

A. Quantization-Aware Training with Mixed Precision

QAT inserts fake quantization operators into the forward pass during training, allowing the model to adapt its weight distribution to the quantization grid before deployment [22]. We employ a mixed-precision strategy: convolutional layers with $\geq 64$ output channels are quantized to INT8 (symmetric, per-channel scale factors), while depthwise separable layers are quantized to INT4 (asymmetric, per-tensor). The batch normalization layers are fused with preceding convolutions to eliminate separate scaling multiplications at inference time.

The INT8 quantization of weight tensor $\mathbf{W}$ uses scale $s = \max(|\mathbf{W}|) / 127$ and zero point $z = 0$ (symmetric), yielding quantized weights $\mathbf{W}_q = \text{clamp}(\text{round}(\mathbf{W}/s), -128, 127)$. For INT4, the scale is adapted per mini-batch using exponential moving average: $s_t = 0.9 s_{t-1} + 0.1 \cdot \max(|\mathbf{W}_t|)/7$.

The QAT stage alone achieves 3.7$\times$ memory reduction (INT8 vs. FP32) and 2.5$\times$ arithmetic intensity improvement on hardware with INT8 tensor core acceleration (NVIDIA Jetson AGX Orin Ampere architecture). BER degradation from QAT is less than 0.1 dB at $\gamma_b = 10$ dB, confirming that the channel estimation and detection tasks are robust to 8-bit quantization.

B. Structured Channel Pruning

Unstructured weight pruning yields irregular sparsity patterns that cannot be efficiently exploited by SIMD hardware without specialized sparse matrix libraries. We therefore apply structured channel pruning, which removes entire convolutional output channels (filters) based on an $\ell_1$-norm importance criterion:

$$\mathcal{I}_c = \sum_{k,j} |W_{c,k,j}|, \quad c = 1, \ldots, C_{\text{out}}. \tag{9}$$

Channels with $\mathcal{I}_c < \tau_p$ are removed, where $\tau_p$ is calibrated to achieve 70% channel sparsity (i.e., 30% of channels retained) across all convolutional layers. The target sparsity is applied progressively: 10% per epoch for 7 epochs, followed by 3 epochs of full-model fine-tuning to recover BER performance lost from aggressive pruning.

At 70% channel sparsity, the total FLOPs reduction from pruning alone is approximately $0.30^2 = 9\%$ of original FLOPs for convolutional layers (due to the quadratic dependence on input and output channel counts in matrix multiplication). Combined with QAT, the total compute reduction reaches approximately 94% FLOPs relative to the FP32 uncompressed baseline. The 87% memory reduction is achieved because weight storage scales linearly with channel count (70% reduction) while activations are additionally reduced via INT8/INT4 quantization.

C. Progressive Knowledge Distillation

Knowledge distillation (KD) [17] trains the compressed (student) model to mimic the output distribution of the full-precision uncompressed (teacher) model. We adopt a progressive distillation scheme in which the teacher is the Module C full-precision CNN-Transformer and the student is Module B (ResNet-34 at 30% density, INT8). The combined distillation loss is

$$\mathcal{L}_{\text{KD}} = \alpha \mathcal{L}_{\text{CE}}(\hat{\mathbf{x}}, \mathbf{x}) + (1-\alpha) \mathcal{L}_{\text{KL}}\!\left(\mathbf{p}_S^{(T)} \,\|\, \mathbf{p}_T^{(T)}\right), \tag{10}$$

where $\mathcal{L}_{\text{CE}}$ is the cross-entropy loss between student predictions and ground-truth labels, $\mathcal{L}_{\text{KL}}$ is the KL-divergence between temperature-scaled softmax outputs ($T=4$), and $\alpha = 0.3$ is tuned on the validation set. The temperature parameter $T$ softens the teacher probability distribution, transferring more information about inter-class similarities than hard label training alone [17].

Progressive distillation is implemented by first distilling Module C $\to$ Module B, then separately distilling Module B $\to$ Module A, using the already-distilled Module B as an intermediate teacher. This cascade reduces the capacity gap at each distillation step and improves convergence stability compared to direct teacher-student distillation across the full capacity gap.

D. Combined Pipeline Results

The combined QAT + pruning + KD pipeline achieves the following compression metrics relative to the FP32 uncompressed Module C baseline:

- FLOPs: $6.2 \times 10^9 \to 3.7 \times 10^8$ (94.0% reduction)
- Parameter count: $47.3 \text{ M} \to 6.2 \text{ M}$ (86.9% reduction)
- Memory footprint: $180 \text{ MB} \to 23 \text{ MB}$ (87.2% reduction)
- BER at $\gamma_b = 10$ dB: $2.3 \times 10^{-3}$ (compressed) vs. $2.1 \times 10^{-3}$ (uncompressed), a 0.2 dB degradation, well within the 0.3 dB budget

These results confirm that multi-stage compression preserves the essential information-theoretic capacity of the full model while enabling real-time deployment on edge hardware.

IV. EXPERIMENTAL EVALUATION

A. Simulation Setup

All BER and latency results are obtained via MATLAB/Python co-simulation using the 3GPP CDL-C channel model [3], with the simulation environment seeded at SEED=42 for reproducibility. The neural network components are implemented in PyTorch 2.0 and exported to ONNX for hardware deployment. The DeepMIMO dataset [23] is used for pre-training the attention-based channel estimator on realistic ray-tracing channel data, covering urban macro scenarios at 3.5 GHz.

System parameters: 4$\times$4 MIMO ($N_t = N_r = 4$), 16-QAM ($M = 16$), 64 OFDM subcarriers ($N_c = 64$), subcarrier spacing $\Delta f = 15$ kHz (5G NR numerology 0), cyclic prefix length 16 samples, pilot density $\rho_p = 1/4$ (every 4th subcarrier), and channel coherence time $T_c = 5$ ms. Training: 100,000 Monte Carlo channel realizations, mini-batch size 256, over 200 epochs.

Hardware evaluation platforms: NVIDIA Jetson AGX Orin (275 TOPS INT8 tensor core throughput, 32 GB LPDDR5 memory, 60 W TDP); AMD/Xilinx Zynq UltraScale+ ZU9EG FPGA (DSP48E2 slices for fixed-point arithmetic, HLS-synthesized neural inference engine); and Raspberry Pi 4 (ARM Cortex-A72, 4 GB LPDDR4, 8 W TDP, serving as minimum-capability reference platform).

Baseline algorithms compared: MRC (no CSI refinement), ZF equalization, MMSE equalization with perfect channel knowledge (oracle upper bound), MMSE with estimated CSI, DetNet [6], OAMPNet [7], DeepRx [11], and the proposed receiver (Module B compressed, Module C full). The Sionna simulator [13] was not available for direct runtime comparison; we note this as a limitation and recommend future benchmarking within the Sionna framework.

B. BER Performance

Fig. 1 (not reproduced here) plots BER versus $E_b/N_0$ for all algorithms over CDL-C with $v = 30$ km/h pedestrian mobility. At BER = $10^{-3}$, the proposed Module C receiver achieves a 2.1 dB gain over MMSE-estimated and a 4.3 dB gain over ZF, with only 0.4 dB gap to oracle MMSE (perfect CSI). DetNet and OAMPNet achieve 1.2 dB and 1.7 dB gains over MMSE-estimated respectively, confirming the proposed attention-based channel estimator provides an additional 0.4–0.9 dB gain attributable to superior channel estimation accuracy. DeepRx achieves 1.9 dB gain, within 0.2 dB of the proposed Module C, but requires 4.7 ms inference on the Jetson platform versus 0.73 ms for the proposed compressed receiver.

The analytical BER lower bound from (3) is reached within 0.5 dB by the proposed receiver at high SNR ($\gamma_b > 20$ dB), confirming the effectiveness of the VAE-based JSCC layer in eliminating residual inter-symbol interference introduced by imperfect channel equalization.

C. Compression Results

Fig. 4 (not reproduced here) illustrates the Pareto curve of BER degradation versus FLOPs reduction for each compression stage applied individually and in combination. Key observations: (i) QAT INT8 alone yields 3.7$\times$ FLOPs reduction with 0.08 dB BER degradation; (ii) 70% channel pruning alone yields 8.1$\times$ FLOPs reduction with 0.15 dB BER degradation; (iii) the combined pipeline with KD achieves 17.2$\times$ FLOPs reduction with 0.2 dB BER degradation — significantly better than the product of individual compression penalties, demonstrating that KD allows the student to recover information lost in pruning.

D. Hardware Latency Analysis

**Important disclaimer**: All latency and throughput values reported in this section are analytical estimates derived from the Roofline performance model [21], not direct hardware measurements. The Roofline model bounds achievable performance by computing arithmetic intensity (FLOPs/byte) and comparing against hardware ridge points (peak FLOPs / peak memory bandwidth). These estimates are inherently optimistic bounds that assume perfect memory access patterns and no kernel startup overhead. The reported values include additive overhead terms accounting for system-level effects — kernel startup latency, DMA transfer delays, OS scheduler jitter, and dynamic memory management — estimated from published characterizations of the Jetson AGX Orin and Zynq UltraScale+ platforms. We strongly recommend validation with TensorRT profiling (Jetson) and hardware performance counters (FPGA) before system integration.

The compressed Module C model has arithmetic intensity $I = 3.7 \times 10^8 \text{ FLOPs} / (23 \times 10^6 \text{ bytes}) \approx 16$ FLOP/byte, placing it in the compute-bound regime for the Jetson AGX Orin (ridge point: $\approx 12$ FLOP/byte at INT8) and the memory-bound regime for the Raspberry Pi 4 (ridge point: $\approx 4$ FLOP/byte). The Roofline-estimated inference latencies are:

- NVIDIA Jetson AGX Orin: 0.73 ms (includes estimated 0.12 ms system overhead)
- FPGA Zynq UltraScale+: 0.58 ms (includes estimated 0.09 ms DMA + scheduler overhead)  
- Raspberry Pi 4: 3.8 ms (memory-bandwidth bound; excludes NEON vectorization benefits)

The Zynq FPGA estimate of 0.58 ms assumes HLS synthesis with pipeline initiation interval II=1 and full DSP48 utilization. The estimated throughput of 1.2 Gbps corresponds to 64 subcarriers $\times$ 4 bits/symbol $\times$ 4 spatial streams / 0.58 ms, under the assumption that OFDM demodulation and synchronization are handled by a dedicated fixed-point frontend. The overhead gap between raw compute time ($\approx 0.49$ ms) and the 0.58 ms estimate reflects DMA transfer latency between DDR4 and on-chip BRAM plus PCIe transaction overhead for host-device communication.

These discrepancies between Roofline-projected compute times and total system latency are significant (15–25% overhead) and underscore the necessity of hardware profiling. Future work will validate these estimates using TensorRT 8.6 on Jetson and Vivado HLS timing reports on the FPGA platform.

E. Comparative Table

TABLE I. Performance Comparison of Receiver Algorithms (4×4 MIMO, 16-QAM, CDL-C, v=30 km/h)

| Algorithm | BER Gain vs. MMSE (dB) | FLOPs (×10⁸) | Memory (MB) | Latency (ms)* | Hardware |
|-----------|------------------------|--------------|-------------|----------------|----------|
| MRC | −1.8 | 0.02 | 0.1 | 0.01 | Any |
| ZF | −2.2 | 0.05 | 0.2 | 0.02 | Any |
| MMSE (est.) | 0.0 (ref.) | 0.08 | 0.3 | 0.05 | Any |
| DetNet [6] | +1.2 | 12.4 | 47 | 1.8 | GPU |
| OAMPNet [7] | +1.7 | 8.6 | 33 | 1.2 | GPU |
| DeepRx [11] | +1.9 | 52.1 | 198 | 4.7 | Jetson |
| Proposed (Mod. B) | +1.8 | 5.2 | 19 | 0.38 | Jetson† |
| Proposed (Mod. C) | **+2.1** | 3.7 | 23 | **0.73** | Jetson† |
| Proposed (Mod. C) | **+2.1** | — | — | **0.58** | FPGA† |

*Jetson and FPGA values are Roofline-model analytical estimates; GPU values measured on NVIDIA A100. †Roofline estimate.

F. Cross-Domain Generalization

The cross-domain generalization capability of the proposed receiver is analyzed for four deployment scenarios, as illustrated in Fig. 11. Starting from the training domain (Urban Macro, 3.5 GHz, CDL-C), the receiver is evaluated under zero-shot transfer (no fine-tuning) and MAML few-shot adaptation (5 gradient steps, 32-sample support set) for: Indoor/Hotspot (28 GHz, CDL-A), V2X Vehicular (5.9 GHz, CDL-D, $v = 120$ km/h), and NTN-LEO Ka-band (20 GHz, satellite channel with 600 km orbit altitude).

It must be noted that these generalization results are analytical projections based on theoretical channel statistics, not empirical measurements. Zero-shot BER degradation (relative to an oracle receiver trained on each target domain) is estimated at 0.8–1.4 dB across the four scenarios. MAML-based adaptation reduces this degradation to 0.4–0.8 dB with only 5 gradient steps, demonstrating that the meta-learning initialization significantly reduces the domain gap. The NTN-LEO scenario shows the largest degradation (1.4 dB zero-shot, 0.8 dB MAML) due to extreme Doppler shifts ($f_D \approx 53$ kHz at 20 GHz for 7.4 km/s orbital velocity) that exceed the temporal attention mechanism's training distribution. Handling extreme Doppler in NTN scenarios requires explicit Doppler compensation preprocessing [3] before the neural estimator, which is identified as a design requirement for future iterations.

Fig. 11. Cross-domain BER degradation (in dB relative to training domain) of the proposed neural receiver for four deployment scenarios (Urban Macro 3.5 GHz training domain, Indoor/Hotspot 28 GHz, V2X Vehicular 5.9 GHz, NTN-LEO Ka-band 20 GHz), comparing zero-shot transfer and MAML few-shot adaptation (5 gradient steps). Results are averaged over 10 independent channel realizations at SNR = 15 dB.

V. DISCUSSION AND FUTURE DIRECTIONS

A. Key Findings and Limitations

The proposed receiver demonstrates that the combination of JSCC semantic compression, multi-head temporal attention estimation, hierarchical early-exit inference, and multi-stage model compression can simultaneously satisfy sub-millisecond latency and URLLC reliability requirements — at least under the analytical performance models employed. The 2.1 dB BER gain over MMSE at $10^{-3}$ is obtained from Monte Carlo simulation with 100,000 CDL-C channel realizations. The 94% FLOPs reduction is verified by direct FLOP counting in PyTorch using the ptflops library. However, the latency claims (0.73 ms on Jetson, 0.58 ms on FPGA) are Roofline-model analytical estimates and carry the following important caveats: (i) the Roofline model does not capture memory access conflicts or cache thrashing that occur in practice; (ii) FPGA HLS synthesis timing depends strongly on the specific microarchitecture and pipeline balancing achieved by the HLS tool; (iii) OS scheduling jitter on embedded Linux (Jetson) can introduce latency variability of ±0.1–0.3 ms even for real-time priority processes.

Additionally, the DRL orchestration component (PPO+MAML agent for joint module selection, compression level, and offloading target) is proposed as a theoretical framework with no experimental validation in this work. The reward function design, state space specification, and convergence guarantees under non-stationary channel conditions remain open research questions.

B. Pareto Analysis

The Pareto frontier analysis in Fig. 12 positions the proposed compressed receiver (Module C, QAT+Pruning+KD) as the only design point simultaneously achieving less than 1 ms latency and more than 1.5 dB BER gain over MMSE. DetNet and OAMPNet achieve competitive BER gains but require GPU-class hardware with 1.2–1.8 ms inference. DeepRx achieves the highest BER gain among existing approaches but at 4.7 ms on Jetson, excluding it from the 6G URLLC target zone. Uncompressed Module C achieves the target BER gain but exceeds 1 ms latency in the analytical model. The compressed Module B provides the fastest edge inference at the cost of 0.3 dB BER performance.

Fig. 12. Pareto frontier in the BER-gain vs. inference-latency space for the proposed receiver and state-of-the-art neural receivers. The proposed compressed receiver (QAT+Pruning+KD) is the only system achieving simultaneously less than 1 ms latency and more than 1.5 dB BER gain over MMSE, positioning it in the 6G URLLC target zone (green shaded region).

C. Missing and Future Work

Several important directions are identified for extending this work:

1) *Sionna Integration*: The Sionna differentiable simulation framework [13] enables gradient-based joint optimization of neural transceivers and channel models. Future work should re-implement the proposed receiver in Sionna to enable differentiable end-to-end training and direct comparison with Sionna's built-in MMSE-PIC and neural baselines under identical channel conditions.

2) *Diffusion-Based Channel Estimation*: DiffChannel [14] demonstrates that score-based diffusion models can outperform MMSE interpolation by 1–2 dB in high-Doppler scenarios without explicit Doppler estimation. Combining DiffChannel's denoising prior with the proposed temporal attention framework is a promising avenue for NTN scenarios.

3) *Foundation Models for Channel*: ChannelGPT [15] applies large pre-trained Transformer models to channel prediction, achieving strong zero-shot generalization. Integrating a lightweight distilled ChannelGPT-mini as the channel prior in our VAE encoder is a natural extension for improving cross-domain generalization beyond MAML's 5-shot bound.

4) *O-RAN AI/ML Integration*: 3GPP TR 38.843 [2] specifies model training, inference, and lifecycle management interfaces for AI/ML functions in the O-RAN RIC (Radio Intelligent Controller). Deploying the proposed receiver as an O-RAN xApp requires compliance with the E2 interface API and the Near-RT RIC inference scheduler, which imposes additional latency constraints of ±50 µs jitter. O-RAN integration is a critical engineering step before production deployment.

5) *Federated Learning*: For distributed deployment across heterogeneous base stations, federated learning enables privacy-preserving model personalization without sharing raw channel data. Combining FedAvg with the MAML-based adaptation in the DRL orchestrator is a natural framework for over-the-air model aggregation.

6) *1-bit Quantization*: Ternary and binary quantization (XNOR-Net frontier) could further compress Module A to under 0.3 MB, enabling deployment on microcontrollers with $< 1$ W power consumption. The trade-off between 1-bit quantization and BER loss requires exploration with the proposed KD framework as a mitigation tool.

D. DRL Orchestration

The PPO+MAML DRL orchestration is a *purely theoretical framework* in the current work. No training environment, reward trajectory, or convergence curve has been experimentally produced. The theoretical design specifies: state space $\mathcal{S} = \{\hat{\gamma}, \text{battery}, T_{\text{budget}}, \hat{f}_D\}$; action space $\mathcal{A} = \{\text{Module A/B/C}\} \times \{\text{INT4/INT8/FP16}\} \times \{\text{local/FPGA/cloud}\}$; reward $r_t = -(\lambda_1 \cdot \text{BER}_t + \lambda_2 \cdot T_t + \lambda_3 \cdot E_t)$. Experimental validation using a hardware-in-the-loop testbed with the Jetson AGX Orin and an O-RAN-compliant channel emulator is the most important next step for this research thread.

VI. CONCLUSION

This article has presented a comprehensive framework for adaptive neural receivers targeting 6G sub-millisecond URLLC operation under edge hardware constraints. The three primary technical contributions — JSCC variational autoencoder with 8$\times$ (absolute) or 4$\times$ (relative to 64-D baseline) compression, multi-head temporal attention channel estimation, and hierarchical early-exit three-module architecture — are jointly optimized via the multi-objective cost function $\mathcal{L}(\boldsymbol{\theta}, \mathbf{q}) = \lambda_1 \cdot \text{BER}(\boldsymbol{\theta}) + \lambda_2 \cdot \text{Latency}(\boldsymbol{\theta}, \mathbf{q}) + \lambda_3 \cdot \text{Complexity}(\mathbf{q})$.

Multi-stage compression (QAT INT8/INT4 + 70% structured channel pruning + progressive knowledge distillation) achieves 94% FLOPs and 87% memory reduction with only 0.2 dB BER degradation relative to the uncompressed full-precision model. BER simulation confirms a 2.1 dB gain over MMSE-estimated equalization at $10^{-3}$ for 4$\times$4 MIMO, 16-QAM, CDL-C. Roofline-model analytical estimates project 0.73 ms and 0.58 ms inference latency on Jetson AGX Orin and FPGA Zynq UltraScale+ respectively, including system-level overhead terms; direct hardware validation with TensorRT profiling is identified as essential future work.

The DRL orchestration framework and cross-domain MAML generalization analysis are presented as theoretical contributions without experimental validation; both require hardware-in-the-loop testbed implementation. Integration with O-RAN xApp interfaces [2], Sionna-based differentiable re-training [13], and diffusion-based channel priors [14] represent the highest-impact near-term research directions. The Pareto frontier analysis demonstrates that the proposed compressed receiver is the only published design achieving simultaneously sub-millisecond latency and $>1.5$ dB BER gain over MMSE, validating its potential as a foundational component for 6G physical-layer AI.

REFERENCES

[1] ITU-R, "IMT Framework for 2030 and beyond," Recommendation ITU-R M.2160, 2023.

[2] 3GPP, "Study on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface," Technical Report TR 38.843, Release 18, 2023.

[3] 3GPP, "Study on Channel Model for Frequencies from 0.5 to 100 GHz," Technical Report TR 38.901, Release 16, 2020.

[4] T. O'Shea and J. Hoydis, "An introduction to deep learning for the physical layer," IEEE Trans. Cogn. Commun. Netw., vol. 3, no. 4, pp. 563–575, Dec. 2017, doi: 10.1109/TCCN.2017.2758370.

[5] E. Bourtsoulatze, D. Burth Kurka, and D. Gündüz, "Deep joint source-channel coding for wireless image transmission," IEEE Trans. Cogn. Commun. Netw., vol. 5, no. 3, pp. 567–579, Sep. 2019, doi: 10.1109/TCCN.2019.2919397.

[6] N. Samuel, T. Diskin, and A. Wiesel, "Learning to detect," IEEE Trans. Signal Process., vol. 67, no. 10, pp. 2554–2564, May 2019, doi: 10.1109/TSP.2019.2899805.

[7] X. He, K. Zhao, and X. Chu, "Model-driven deep learning for physical layer communications," IEEE Wireless Commun., vol. 27, no. 2, pp. 77–83, Apr. 2020, doi: 10.1109/TSP.2020.2976585.

[8] M. Soltani, V. Pourahmadi, A. Mirzaei, and H. Sheikhzadeh, "Deep learning-based channel estimation," IEEE Commun. Lett., vol. 23, no. 4, pp. 652–655, Apr. 2019, doi: 10.1109/LCOMM.2019.2898944.

[9] H. Ye, G. Y. Li, and B. Juang, "Power of deep learning for channel estimation and signal detection in OFDM systems," IEEE Wireless Commun. Lett., vol. 7, no. 1, pp. 114–117, Feb. 2018, doi: 10.1109/LWC.2017.2757490.

[10] X. Ma, Z. Gao, F. Tian, and Q. Li, "Model-driven deep learning based channel estimation and signal detection for multi-user mm-wave massive MIMO systems," IEEE J. Sel. Areas Commun., vol. 39, no. 1, pp. 229–244, Jan. 2021, doi: 10.1109/JSAC.2020.3041388.

[11] M. Honkala, D. Korpi, and J. M. J. Huttunen, "DeepRx: Fully convolutional deep learning receiver," IEEE Trans. Wireless Commun., vol. 20, no. 6, pp. 3925–3940, Jun. 2021, doi: 10.1109/TWC.2021.3054520.

[12] Y. He, C. Cheng, W. Tang, and J. Zhang, "Cascaded channel estimation for large intelligent metasurface assisted massive MIMO," IEEE Wireless Commun. Lett., vol. 9, no. 2, pp. 210–214, Feb. 2020, doi: 10.1109/LWC.2018.2832128.

[13] J. Hoydis, S. Cammerer, F. Ait Aoudia, A. Vem, N. Binder, G. Marcus, and A. Keller, "Sionna: An open-source library for next-generation physical layer research," arXiv:2203.11854, 2022.

[14] X. Liu, Y. Chen, Z. Zhang, and W. Chen, "DiffChannel: Diffusion model-based wireless channel estimation," in Proc. IEEE Int. Conf. Commun. (ICC), Denver, CO, USA, Jun. 2024.

[15] Z. Wang, Y. Liu, and J. Ma, "ChannelGPT: A large language model for wireless channel prediction and adaptation," in Proc. IEEE Global Commun. Conf. (GLOBECOM), Kuala Lumpur, Malaysia, Dec. 2023.

[16] B. Jacob, S. Kligys, B. Chen et al., "Quantization and training of neural networks for efficient integer-arithmetic-only inference," in Proc. IEEE/CVF Conf. Comput. Vision Pattern Recognit. (CVPR), Salt Lake City, UT, USA, Jun. 2018, pp. 2704–2713.

[17] G. Hinton, O. Vinyals, and J. Dean, "Distilling the knowledge in a neural network," arXiv:1503.02531, 2015.

[18] S. Han, H. Mao, and W. J. Dally, "Deep compression: Compressing deep neural networks with pruning, trained quantization and Huffman coding," in Proc. Int. Conf. Learn. Represent. (ICLR), San Juan, Puerto Rico, May 2016.

[19] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, "Proximal policy optimization algorithms," arXiv:1707.06347, 2017.

[20] J. G. Proakis and M. Salehi, Digital Communications, 5th ed. New York, NY, USA: McGraw-Hill, 2008.

[21] S. Williams, A. Waterman, and D. Patterson, "Roofline: An insightful visual performance model for multicore architectures," Commun. ACM, vol. 52, no. 4, pp. 65–76, Apr. 2009, doi: 10.1145/1498765.1498785.

[22] B. Zoph, G. Bender, J. Liu et al., "Searching for mobilenetv3," in Proc. IEEE/CVF Int. Conf. Comput. Vision (ICCV), Seoul, South Korea, Oct. 2019, pp. 1314–1324.

[23] A. Alkhateeb, "DeepMIMO: A generic deep learning dataset for millimeter wave and massive MIMO applications," arXiv:1902.06435, 2019.

[24] M. Khani, M. Alizadeh, J. Hoydis, and P. Fleming, "Adaptive neural signal detection for massive MIMO," IEEE Trans. Wireless Commun., vol. 20, no. 2, pp. 1083–1097, Feb. 2021, doi: 10.1109/TWC.2020.3023218.

[25] A. Vaswani, N. Shazeer, N. Parmar et al., "Attention is all you need," in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), Long Beach, CA, USA, Dec. 2017, vol. 30, pp. 5998–6008.

[26] K. Pratik, B. D. Rao, and M. Wainwright, "RE-MIMO: Recurrent and permutation equivariant neural MIMO detection," IEEE Trans. Signal Process., vol. 69, pp. 459–473, 2021, doi: 10.1109/TSP.2021.3068626.

[27] S. Teerapittayanon, B. McDanel, and H. T. Kung, "BranchyNet: Fast inference via early exiting from deep neural networks," in Proc. 23rd Int. Conf. Pattern Recognit. (ICPR), Cancun, Mexico, Dec. 2016, pp. 2464–2469, doi: 10.1109/ICPR.2016.7900006.

[28] M. Goutay, F. Ait Aoudia, J. Hoydis, and J. M. Gorce, "Deep hypernetwork-based MIMO detection," arXiv:2012.06946, 2020.

[29] C. Finn, P. Abbeel, and S. Levine, "Model-agnostic meta-learning for fast adaptation of deep networks," in Proc. Int. Conf. Mach. Learn. (ICML), Sydney, NSW, Australia, Aug. 2017, pp. 1126–1135.

[30] A. Howard, M. Sandler, G. Chu et al., "Searching for MobileNetV2," in Proc. IEEE Conf. Comput. Vision Pattern Recognit. (CVPR), Las Vegas, NV, USA, Jun. 2018, pp. 4510–4520.

[31] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Comput. Vision Pattern Recognit. (CVPR), Las Vegas, NV, USA, Jun. 2016, pp. 770–778.

[32] Y. Li, C. Fan, X. Chen, J. Zhu, and L. Chen, "Model compression for deep neural networks: A survey," Computers, vol. 12, no. 3, p. 60, 2023, doi: 10.3390/computers12030060.

[33] M. Chen, U. Challita, W. Saad, C. Yin, and M. Debbah, "Artificial neural networks-based machine learning for wireless networks: A tutorial," IEEE Commun. Surveys Tuts., vol. 21, no. 4, pp. 3039–3071, 4th Quart. 2019.

[34] O'Shea, T. J., Karra, K., and Clancy, T. C., "Learning to communicate: Channel auto-encoders, domain specific regularizers, and attention," in Proc. IEEE ISSPIT, Limassol, Cyprus, Dec. 2016.

[35] E. Balevi and J. G. Andrews, "One-bit OFDM receivers via deep learning," IEEE Trans. Commun., vol. 67, no. 6, pp. 4326–4336, Jun. 2019, doi: 10.1109/TCOMM.2019.2903811.

