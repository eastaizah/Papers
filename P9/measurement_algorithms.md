# Measurement Algorithms for Semantic Communication Metrics in 6G Networks

> **IEEE-Style Pseudocode Specification — 16 Metrics across 4 Dimensions**

---

## Dimension 1 — Semantic Fidelity

---

### **Algorithm 1: Relative Semantic Entropy (RSE)**

**Purpose:** Quantify the fraction of task-relevant semantic information preserved after transmission, using the Kraskov *k*-NN mutual information estimator on embedding vectors.

**Inputs:**
- $\mathbf{X} = \{x_1, \dots, x_N\}$: source semantic embedding vectors, $x_i \in \mathbb{R}^d$
- $\mathbf{Y} = \{y_1, \dots, y_N\}$: received semantic embedding vectors, $y_i \in \mathbb{R}^d$
- $T$: task descriptor (used to select task-conditioned encoder $f_T$)
- $k$: number of nearest neighbours (default $k = 6$)

**Output:**
- $\mathrm{RSE} \in [0,1]$: relative semantic entropy

```
Algorithm 1  RSE — Relative Semantic Entropy
─────────────────────────────────────────────
Input : X = {x₁,…,x_N}, Y = {y₁,…,y_N}, task T, neighbours k
Output: RSE ∈ [0, 1]

 1:  // ── Step 1: Task-conditioned projection ──
 2:  for i ← 1 to N do
 3:      x̃_i ← f_T(x_i)                          ▷ project source into task subspace
 4:      ỹ_i ← f_T(y_i)                          ▷ project received into task subspace
 5:  end for

 6:  // ── Step 2: Kraskov k-NN MI estimator I_s(X;Y|T) ──
 7:  ψ(·) ← digamma function
 8:  for i ← 1 to N do
 9:      z_i ← [x̃_i ; ỹ_i]                       ▷ concatenate into joint space ℝ^{2d}
10:  end for
11:  for i ← 1 to N do
12:      ε_i ← distance to k-th nearest neighbour of z_i in {z_j}_{j≠i}
13:                                                  using Chebyshev (L∞) norm
14:      n_x(i) ← |{j ≠ i : ‖x̃_i − x̃_j‖_∞ < ε_i}|
15:      n_y(i) ← |{j ≠ i : ‖ỹ_i − ỹ_j‖_∞ < ε_i}|
16:  end for
17:  I_s ← ψ(k) − (1/N) Σ_{i=1}^{N} [ψ(n_x(i)+1) + ψ(n_y(i)+1)] + ψ(N)

18:  // ── Step 3: Semantic entropy H_s(X|T) via k-NN ──
19:  for i ← 1 to N do
20:      ρ_i ← distance to k-th nearest neighbour of x̃_i in {x̃_j}_{j≠i}
21:  end for
22:  c_d ← volume of unit ball in ℝ^d   ▷ π^{d/2} / Γ(d/2 + 1)
23:  H_s ← (d/N) Σ_{i=1}^{N} ln(ρ_i) + ln(N − 1) − ψ(k) + ln(c_d)

24:  // ── Step 4: Compute RSE ──
25:  if H_s ≤ 0 then
26:      return RSE ← 0                            ▷ degenerate case guard
27:  end if
28:  RSE ← clamp(I_s / H_s, 0, 1)

29:  return RSE
```

**Complexity:** $\mathcal{O}(N \log N \cdot d)$ using a KD-tree for nearest-neighbour queries; $\mathcal{O}(N^2 d)$ with brute-force search.

---

### **Algorithm 2: Semantic Wasserstein Distance (SWD)**

**Purpose:** Measure the optimal-transport cost between source and received semantic distributions using Sinkhorn entropic-regularized approximation.

**Inputs:**
- $\mathbf{X} = \{x_1, \dots, x_N\}$: source embeddings, $x_i \in \mathbb{R}^d$
- $\mathbf{Y} = \{y_1, \dots, y_M\}$: received embeddings, $y_j \in \mathbb{R}^d$
- $\mu \in \Delta^N$, $\nu \in \Delta^M$: marginal weight vectors (default: uniform)
- $\varepsilon > 0$: entropic regularization parameter
- $L$: maximum Sinkhorn iterations
- $\tau$: convergence tolerance

**Output:**
- $\mathrm{SWD} \geq 0$: semantic Wasserstein distance

```
Algorithm 2  SWD — Semantic Wasserstein Distance (Sinkhorn)
───────────────────────────────────────────────────────────
Input : X ∈ ℝ^{N×d}, Y ∈ ℝ^{M×d}, μ ∈ Δ^N, ν ∈ Δ^M, ε, L, τ
Output: SWD ≥ 0

 1:  // ── Step 1: Ground cost matrix ──
 2:  for i ← 1 to N do
 3:      for j ← 1 to M do
 4:          C_{i,j} ← ‖x_i − y_j‖₂²                ▷ squared Euclidean in embedding space
 5:      end for
 6:  end for

 7:  // ── Step 2: Gibbs kernel ──
 8:  K ← exp(−C / ε)                                  ▷ element-wise; K ∈ ℝ^{N×M}

 9:  // ── Step 3: Sinkhorn iterations ──
10:  u ← 𝟏_N                                          ▷ initialise scaling vectors
11:  v ← 𝟏_M
12:  for ℓ ← 1 to L do
13:      u_prev ← u
14:      u ← μ ⊘ (K v)                                ▷ element-wise division
15:      v ← ν ⊘ (Kᵀ u)
16:      if ‖u − u_prev‖₁ / ‖u‖₁ < τ then
17:          break                                      ▷ convergence reached
18:      end if
19:  end for

20:  // ── Step 4: Recover transport plan and cost ──
21:  Π ← diag(u) · K · diag(v)                        ▷ optimal coupling
22:  SWD ← ⟨Π, C⟩_F                                   ▷ Frobenius inner product = Σ Π_{ij} C_{ij}

23:  return SWD
```

**Complexity:** $\mathcal{O}(N M \cdot L)$ for $L$ Sinkhorn iterations; matrix–vector products dominate. Typical $L = \mathcal{O}(1/\varepsilon)$.

---

### **Algorithm 3: Semantic Structural Similarity Index (S³I)**

**Purpose:** Extend the classical SSIM framework to operate over semantic embedding patches, comparing luminance (magnitude), contrast (variance), and structure (correlation) in embedding space.

**Inputs:**
- $\mathbf{X}, \mathbf{Y} \in \mathbb{R}^{N \times d}$: paired source and received embedding sequences
- $w$: sliding window size (number of embedding vectors per patch)
- $\alpha, \beta, \gamma > 0$: exponents for luminance, contrast, structure (default: all 1)
- $c_1, c_2, c_3 > 0$: stability constants

**Output:**
- $\mathrm{S^3I} \in [-1, 1]$: semantic structural similarity

```
Algorithm 3  S³I — Semantic Structural Similarity Index
───────────────────────────────────────────────────────
Input : X, Y ∈ ℝ^{N×d}, window w, exponents α,β,γ, constants c₁,c₂,c₃
Output: S³I ∈ [−1, 1]

 1:  P ← N − w + 1                                     ▷ number of sliding patches
 2:  scores ← empty array of size P

 3:  for p ← 0 to P − 1 do
 4:      // ── Extract patch embeddings ──
 5:      X_p ← X[p : p+w, :]                           ▷ sub-matrix ∈ ℝ^{w×d}
 6:      Y_p ← Y[p : p+w, :]

 7:      // ── Patch-level statistics (operate on flattened wd-vectors) ──
 8:      μ_x ← (1/wd) Σ X_p                            ▷ scalar mean of all elements
 9:      μ_y ← (1/wd) Σ Y_p
10:      σ²_x ← (1/(wd−1)) Σ (X_p − μ_x)²
11:      σ²_y ← (1/(wd−1)) Σ (Y_p − μ_y)²
12:      σ_xy ← (1/(wd−1)) Σ (X_p − μ_x)(Y_p − μ_y)

13:      // ── Luminance comparison ──
14:      l_p ← (2 μ_x μ_y + c₁) / (μ_x² + μ_y² + c₁)

15:      // ── Contrast comparison ──
16:      cs_p ← (2 √(σ²_x) √(σ²_y) + c₂) / (σ²_x + σ²_y + c₂)

17:      // ── Structure comparison ──
18:      s_p ← (σ_xy + c₃) / (√(σ²_x) √(σ²_y) + c₃)

19:      scores[p] ← l_p^α · cs_p^β · s_p^γ
20:  end for

21:  S³I ← (1/P) Σ_{p=0}^{P−1} scores[p]              ▷ mean over all patches

22:  return S³I
```

**Complexity:** $\mathcal{O}(N \cdot w \cdot d)$ — linear scan over $N$ with $\mathcal{O}(wd)$ work per patch.

---

### **Algorithm 4: Normalized Semantic Mutual Information (NSMI)**

**Purpose:** Provide a symmetric, scale-invariant measure of shared semantic information between source and received embeddings, normalised by marginal entropies.

**Inputs:**
- $\mathbf{X} = \{x_1, \dots, x_N\}$, $\mathbf{Y} = \{y_1, \dots, y_N\}$: paired embeddings in $\mathbb{R}^d$
- $k$: *k*-NN parameter for differential entropy and MI estimation

**Output:**
- $\mathrm{NSMI} \in [0, 1]$: normalised semantic mutual information

```
Algorithm 4  NSMI — Normalized Semantic Mutual Information
──────────────────────────────────────────────────────────
Input : X, Y ∈ ℝ^{N×d}, neighbours k
Output: NSMI ∈ [0, 1]

 1:  // ── Step 1: Estimate I_s(X;Y) via Kraskov (see Algorithm 1, Steps 6–17) ──
 2:  I_s ← KraskovMI(X, Y, k)

 3:  // ── Step 2: Estimate differential entropies via Kozachenko–Leonenko ──
 4:  c_d ← π^{d/2} / Γ(d/2 + 1)
 5:  for i ← 1 to N do
 6:      ρ^X_i ← k-NN distance of x_i in X \ {x_i}
 7:      ρ^Y_i ← k-NN distance of y_i in Y \ {y_i}
 8:  end for
 9:  H_X ← (d/N) Σ ln(ρ^X_i) + ln(N−1) − ψ(k) + ln(c_d)
10:  H_Y ← (d/N) Σ ln(ρ^Y_i) + ln(N−1) − ψ(k) + ln(c_d)

11:  // ── Step 3: Normalise ──
12:  denom ← √(H_X · H_Y)
13:  if denom ≤ 0 then
14:      return NSMI ← 0                               ▷ degenerate guard
15:  end if
16:  NSMI ← clamp(I_s / denom, 0, 1)

17:  return NSMI
```

**Complexity:** $\mathcal{O}(N \log N \cdot d)$ with KD-tree acceleration; dominated by three independent *k*-NN searches.

---

## Dimension 2 — Task Completion

---

### **Algorithm 5: Task Success Rate (TSR)**

**Purpose:** Estimate the probability that the semantic communication system enables successful task completion, with a Wilson score confidence interval.

**Inputs:**
- $\mathcal{D} = \{(x_i, y_i, t_i, r_i)\}_{i=1}^{N}$: evaluation dataset where $r_i \in \{0,1\}$ is the task result
- $\alpha$: significance level (default 0.05 for 95 % CI)

**Output:**
- $\widehat{\mathrm{TSR}}$: point estimate
- $[\mathrm{TSR}_L, \mathrm{TSR}_U]$: Wilson score confidence interval

```
Algorithm 5  TSR — Task Success Rate with Wilson Score CI
─────────────────────────────────────────────────────────
Input : results R = {r₁,…,r_N} with r_i ∈ {0,1}, significance α
Output: TSR̂, [TSR_L, TSR_U]

 1:  // ── Step 1: Point estimate ──
 2:  S ← Σ_{i=1}^{N} r_i                              ▷ number of successes
 3:  TSR̂ ← S / N

 4:  // ── Step 2: Wilson score interval ──
 5:  z ← Φ⁻¹(1 − α/2)                                ▷ standard normal quantile
 6:  denominator ← 1 + z²/N
 7:  centre ← (TSR̂ + z²/(2N)) / denominator
 8:  margin ← (z / denominator) · √(TSR̂(1−TSR̂)/N + z²/(4N²))
 9:  TSR_L ← max(0, centre − margin)
10:  TSR_U ← min(1, centre + margin)

11:  return TSR̂, [TSR_L, TSR_U]
```

**Complexity:** $\mathcal{O}(N)$ — single pass to count successes, constant-time CI computation.

---

### **Algorithm 6: Action Precision (AP)**

**Purpose:** Measure how close the executed action is to the task-optimal action in a normalised action metric space.

**Inputs:**
- $a_{\text{exec}}$: action executed by receiver (vector in action space $\mathcal{A} \subseteq \mathbb{R}^m$)
- $a_{\text{opt}}$: task-optimal action
- $d_A^{\max}$: maximum possible action distance (diameter of $\mathcal{A}$)
- $d_A(\cdot,\cdot)$: distance function on action space (e.g., weighted $\ell_2$)

**Output:**
- $\mathrm{AP} \in [0, 1]$: action precision

```
Algorithm 6  AP — Action Precision
───────────────────────────────────
Input : a_exec, a_opt ∈ ℝ^m, metric d_A(·,·), diameter d_A^max
Output: AP ∈ [0, 1]

 1:  // ── Step 1: Compute action distance ──
 2:  Δ ← d_A(a_exec, a_opt)                           ▷ e.g., ‖a_exec − a_opt‖₂

 3:  // ── Step 2: Normalise and invert ──
 4:  if d_A^max ≤ 0 then
 5:      return AP ← 1.0                               ▷ trivial action space
 6:  end if
 7:  AP ← 1 − Δ / d_A^max

 8:  // ── Step 3: Batch mode (optional) ──
 9:  // If evaluating over N action pairs:
10:  //   AP̄ ← (1/N) Σ_{i=1}^{N} (1 − d_A(a_exec^i, a_opt^i) / d_A^max)

11:  return clamp(AP, 0, 1)
```

**Complexity:** $\mathcal{O}(m)$ per action pair; $\mathcal{O}(Nm)$ in batch mode.

---

### **Algorithm 7: Semantic Utility (SU)**

**Purpose:** Compute the expected task-conditioned utility of the received semantic representation, combining cosine similarity with a latency decay factor.

**Inputs:**
- $\{(x_i, \hat{x}_i, T_i, \Delta_i)\}_{i=1}^{N}$: source embedding, received embedding, task, and latency for each sample
- $\lambda > 0$: latency decay rate
- $f_T$: task-specific encoder (optional; identity if pre-embedded)

**Output:**
- $\mathrm{SU} \in [0, 1]$: expected semantic utility

```
Algorithm 7  SU — Semantic Utility
───────────────────────────────────
Input : pairs {(x_i, x̂_i, T_i, Δ_i)}_{i=1}^N, decay rate λ
Output: SU ∈ [0, 1]

 1:  U_sum ← 0

 2:  for i ← 1 to N do
 3:      // ── Step 2a: Task-conditioned similarity ──
 4:      s_i ← f_{T_i}(x_i)                           ▷ task-projected source
 5:      ŝ_i ← f_{T_i}(x̂_i)                          ▷ task-projected received
 6:      cos_i ← ⟨s_i, ŝ_i⟩ / (‖s_i‖₂ · ‖ŝ_i‖₂)    ▷ cosine similarity

 7:      // ── Step 2b: Latency penalty ──
 8:      decay_i ← exp(−λ · Δ_i)

 9:      // ── Step 2c: Sample utility ──
10:      U_i ← max(0, cos_i) · decay_i                ▷ clamp negative cosine to 0
11:      U_sum ← U_sum + U_i
12:  end for

13:  SU ← U_sum / N                                    ▷ Monte-Carlo expectation

14:  return SU
```

**Complexity:** $\mathcal{O}(N d)$ where $d$ is the embedding dimension.

---

### **Algorithm 8: Completion Efficiency (CE)**

**Purpose:** Normalise the task success rate by the amount of information transmitted, measuring how efficiently semantic bandwidth achieves task completion.

**Inputs:**
- $\mathrm{TSR}$: task success rate (from Algorithm 5)
- $R_{\text{tx}}$: transmitted information rate (bits per semantic unit, or bits/s)

**Output:**
- $\mathrm{CE} \geq 0$: completion efficiency (success per unit of transmitted information)

```
Algorithm 8  CE — Completion Efficiency
───────────────────────────────────────
Input : results R = {r₁,…,r_N}, transmission log {b₁,…,b_N} (bits per sample)
Output: CE ≥ 0

 1:  // ── Step 1: Compute TSR ──
 2:  TSR̂ ← (1/N) Σ_{i=1}^{N} r_i

 3:  // ── Step 2: Compute average transmitted info rate ──
 4:  R_tx ← (1/N) Σ_{i=1}^{N} b_i                    ▷ mean bits per semantic unit

 5:  // ── Step 3: Guard against division by zero ──
 6:  if R_tx ≤ 0 then
 7:      return CE ← +∞ if TSR̂ > 0, else 0            ▷ zero-rate edge case
 8:  end if

 9:  // ── Step 4: Completion Efficiency ──
10:  CE ← TSR̂ / R_tx

11:  return CE
```

**Complexity:** $\mathcal{O}(N)$ — two summations over the dataset.

---

## Dimension 3 — Intent Alignment

---

### **Algorithm 9: Intent Divergence (ID)**

**Purpose:** Quantify the divergence between the transmitter's intended semantic distribution and the receiver's inferred intent distribution using KL divergence.

**Inputs:**
- $I_T \in \Delta^K$: transmitter intent distribution over $K$ intent classes
- $I_R \in \Delta^K$: receiver-inferred intent distribution
- $\epsilon$: smoothing constant for zero-probability protection (default $10^{-10}$)

**Output:**
- $\mathrm{ID} \geq 0$: intent divergence (nats)

```
Algorithm 9  ID — Intent Divergence
────────────────────────────────────
Input : I_T, I_R ∈ Δ^K, smoothing ε
Output: ID ≥ 0

 1:  // ── Step 1: Laplace smoothing to avoid log(0) ──
 2:  for k ← 1 to K do
 3:      I_T[k] ← I_T[k] + ε
 4:      I_R[k] ← I_R[k] + ε
 5:  end for
 6:  I_T ← I_T / Σ I_T                                ▷ re-normalise
 7:  I_R ← I_R / Σ I_R

 8:  // ── Step 2: KL divergence D_KL(I_T ‖ I_R) ──
 9:  ID ← 0
10:  for k ← 1 to K do
11:      ID ← ID + I_T[k] · ln(I_T[k] / I_R[k])
12:  end for

13:  return ID
```

**Complexity:** $\mathcal{O}(K)$ — linear in the number of intent classes.

---

### **Algorithm 10: Intentional-Context Coherence (ICC)**

**Purpose:** Measure how much the receiver's inferred intent is supported by the context, using the log-likelihood gain of the intent given context versus its prior, compressed through a `tanh` activation.

**Inputs:**
- $I_R$: receiver-inferred intent
- $C$: context representation
- $p(I_R | C)$: contextual intent model (e.g., neural classifier)
- $p(I_R)$: prior intent model

**Output:**
- $\mathrm{ICC} \in (-1, 1)$: intentional-context coherence

```
Algorithm 10  ICC — Intentional-Context Coherence
──────────────────────────────────────────────────
Input : intent I_R, context C, models p(·|C) and p(·)
Output: ICC ∈ (−1, 1)

 1:  // ── Step 1: Evaluate log-probabilities ──
 2:  log_posterior ← ln p(I_R | C)                     ▷ forward pass through context model
 3:  log_prior     ← ln p(I_R)                         ▷ marginal intent probability

 4:  // ── Step 2: Pointwise mutual information (PMI) ──
 5:  PMI ← log_posterior − log_prior                   ▷ = ln [p(I_R|C) / p(I_R)]

 6:  // ── Step 3: Compress to bounded range ──
 7:  ICC ← tanh(PMI)

 8:  // ── Step 4: Batch mode ──
 9:  // If N samples: ICC̄ ← (1/N) Σ tanh(ln p(I_R^i | C_i) − ln p(I_R^i))

10:  return ICC
```

**Complexity:** $\mathcal{O}(T_{\text{model}})$ per sample, where $T_{\text{model}}$ is the inference cost of the intent models. Typically $\mathcal{O}(d^2)$ for a single dense layer.

---

### **Algorithm 11: Semantic Consensus Index (SCI)**

**Purpose:** Measure agreement among multiple receivers' inferred intents, evaluating broadcast semantic coherence.

**Inputs:**
- $\mathcal{I} = \{I_1, \dots, I_{|R|}\}$: intent distributions from $|R|$ receivers, each $I_i \in \Delta^K$
- $D(\cdot, \cdot)$: divergence function (e.g., Jensen–Shannon divergence)
- $D_{\max}$: normalisation constant (maximum possible divergence)

**Output:**
- $\mathrm{SCI} \in [0, 1]$: semantic consensus index ($1$ = perfect consensus)

```
Algorithm 11  SCI — Semantic Consensus Index
─────────────────────────────────────────────
Input : intent set I = {I₁,…,I_{|R|}} ∈ (Δ^K)^{|R|}, divergence D, D_max
Output: SCI ∈ [0, 1]

 1:  n ← |R|                                           ▷ number of receivers
 2:  S ← 0                                             ▷ accumulator

 3:  // ── Step 1: Pairwise normalised divergence ──
 4:  for i ← 1 to n do
 5:      for j ← 1 to n do
 6:          D_norm ← D(I_i, I_j) / D_max             ▷ normalise to [0,1]
 7:          S ← S + D_norm
 8:      end for
 9:  end for

10:  // ── Step 2: Average and invert ──
11:  SCI ← 1 − S / n²

12:  return SCI
```

**Note:** If using JSD, $D_{\max} = \ln 2$ (binary logarithm yields $D_{\max} = 1$).

**Complexity:** $\mathcal{O}(|R|^2 \cdot K)$ — pairwise comparison over receivers.

---

### **Algorithm 12: Purpose Fidelity (PF)**

**Purpose:** Estimate the probability that the purpose originally intended by the transmitter is achieved after the receiver acts on its inferred intent.

**Inputs:**
- $\mathcal{D} = \{(I_R^i, a_i, g_i)\}_{i=1}^{N}$: inferred intents, executed actions, and ground-truth purpose outcomes $g_i \in \{0,1\}$
- $\alpha$: significance level for optional CI

**Output:**
- $\mathrm{PF} \in [0, 1]$: purpose fidelity

```
Algorithm 12  PF — Purpose Fidelity
────────────────────────────────────
Input : dataset D = {(I_R^i, a_i, g_i)}_{i=1}^N with g_i ∈ {0,1}, level α
Output: PF ∈ [0, 1], optional [PF_L, PF_U]

 1:  // ── Step 1: Execute purpose verification ──
 2:  S ← 0
 3:  for i ← 1 to N do
 4:      a_i ← action_policy(I_R^i)                   ▷ receiver maps intent → action
 5:      g_i ← purpose_oracle(a_i)                     ▷ binary: was purpose achieved?
 6:      S ← S + g_i
 7:  end for

 8:  // ── Step 2: Point estimate ──
 9:  PF ← S / N                                        ▷ = P̂(purpose achieved | action(I_R))

10:  // ── Step 3: Wilson CI (identical to Algorithm 5, Steps 5–10) ──
11:  z ← Φ⁻¹(1 − α/2)
12:  denominator ← 1 + z²/N
13:  centre ← (PF + z²/(2N)) / denominator
14:  margin ← (z / denominator) · √(PF(1−PF)/N + z²/(4N²))
15:  PF_L ← max(0, centre − margin)
16:  PF_U ← min(1, centre + margin)

17:  return PF, [PF_L, PF_U]
```

**Complexity:** $\mathcal{O}(N \cdot T_{\text{oracle}})$, where $T_{\text{oracle}}$ is the cost of the purpose verification oracle.

---

## Dimension 4 — Resilience

---

### **Algorithm 13: Adversarial Robustness Radius (ARR)**

**Purpose:** Find the minimum perturbation magnitude that causes a semantic misclassification, using binary search over PGD attack strengths.

**Inputs:**
- $x \in \mathbb{R}^d$: clean input embedding
- $S(\cdot)$: semantic encoder / classifier
- $\varepsilon_{\min}, \varepsilon_{\max}$: search bounds for perturbation radius
- $T_{\text{PGD}}$: number of PGD steps per trial
- $\eta$: PGD step size
- $B$: number of binary search iterations

**Output:**
- $\mathrm{ARR} \geq 0$: adversarial robustness radius

```
Algorithm 13  ARR — Adversarial Robustness Radius (Binary-Search PGD)
─────────────────────────────────────────────────────────────────────
Input : x ∈ ℝ^d, classifier S(·), bounds [ε_min, ε_max], PGD params (T, η), bisections B
Output: ARR ≥ 0

 1:  s_clean ← S(x)                                    ▷ clean semantic label
 2:  lo ← ε_min
 3:  hi ← ε_max

 4:  // ── Binary search for minimal ε ──
 5:  for b ← 1 to B do
 6:      ε_mid ← (lo + hi) / 2

 7:      // ── PGD attack at radius ε_mid ──
 8:      δ ← Uniform(−ε_mid, ε_mid)^d                 ▷ random initialisation
 9:      for t ← 1 to T do
10:          g ← ∇_δ L_CE(S(x + δ), s_clean)          ▷ gradient of cross-entropy loss
11:          δ ← δ + η · sign(g)                       ▷ FGSM step
12:          δ ← Π_{‖·‖_∞ ≤ ε_mid}(δ)                 ▷ project onto ℓ∞ ball
13:      end for

14:      // ── Check if attack succeeded ──
15:      if S(x + δ) ≠ s_clean then
16:          hi ← ε_mid                                ▷ adversarial example found; shrink upper
17:      else
18:          lo ← ε_mid                                ▷ robust at this radius; raise lower
19:      end if
20:  end for

21:  ARR ← hi                                          ▷ smallest ε where attack succeeds

22:  return ARR
```

**Complexity:** $\mathcal{O}(B \cdot T_{\text{PGD}} \cdot T_{\nabla})$, where $T_{\nabla}$ is the cost of one gradient computation through $S$.

---

### **Algorithm 14: Semantic Attack Success Rate (SASR)**

**Purpose:** Estimate the fraction of inputs for which an adversary can change the semantic output within a given perturbation budget.

**Inputs:**
- $\mathcal{X} = \{x_1, \dots, x_N\}$: test inputs
- $S(\cdot)$: semantic encoder/classifier
- $\varepsilon$: perturbation budget ($\ell_p$ norm)
- $\mathcal{A}_{\text{attack}}$: attack algorithm (e.g., PGD, CW, AutoAttack)

**Output:**
- $\mathrm{SASR} \in [0, 1]$: semantic attack success rate

```
Algorithm 14  SASR — Semantic Attack Success Rate
──────────────────────────────────────────────────
Input : X = {x₁,…,x_N}, classifier S(·), budget ε, attack A
Output: SASR ∈ [0, 1]

 1:  n_success ← 0

 2:  for i ← 1 to N do
 3:      s_clean ← S(x_i)                             ▷ clean semantic output

 4:      // ── Generate adversarial perturbation ──
 5:      x_adv ← A(x_i, S, ε)                         ▷ attack algorithm returns x_adv
 6:                                                      with ‖x_adv − x_i‖_p ≤ ε

 7:      // ── Verify semantic change ──
 8:      s_adv ← S(x_adv)
 9:      if s_adv ≠ s_clean then
10:          n_success ← n_success + 1
11:      end if
12:  end for

13:  SASR ← n_success / N

14:  return SASR
```

**Complexity:** $\mathcal{O}(N \cdot T_{\mathcal{A}})$, where $T_{\mathcal{A}}$ is the per-sample cost of the attack algorithm.

---

### **Algorithm 15: Certification Cost (CertCost)**

**Purpose:** Measure the wall-clock time required to certify a semantic encoder's robustness at input $x$ within radius $\varepsilon$ via randomised smoothing.

**Inputs:**
- $x \in \mathbb{R}^d$: input to certify
- $f_\theta$: base semantic classifier
- $\sigma$: Gaussian noise standard deviation for smoothing
- $\varepsilon$: certification radius
- $n_0$: number of preliminary samples (for top-class selection)
- $n$: number of certification samples
- $\alpha$: failure probability (e.g., 0.001)

**Output:**
- $\mathrm{CertCost}$: verification wall-clock time (seconds)
- $\mathrm{certified}$: Boolean — whether $f_\theta$ is certifiably robust at $(x, \varepsilon)$

```
Algorithm 15  CertCost — Certification Cost via Randomised Smoothing
────────────────────────────────────────────────────────────────────
Input : x ∈ ℝ^d, classifier f_θ, noise σ, radius ε, samples n₀,n, level α
Output: CertCost (seconds), certified ∈ {True, False}

 1:  t_start ← CLOCK()

 2:  // ── Step 1: Identify most likely class (preliminary) ──
 3:  counts₀ ← zero vector of size |C|                ▷ |C| = number of classes
 4:  for j ← 1 to n₀ do
 5:      η ← 𝒩(0, σ²I_d)
 6:      counts₀[f_θ(x + η)] += 1
 7:  end for
 8:  ĉ_A ← argmax_c counts₀[c]                       ▷ candidate top class

 9:  // ── Step 2: Certification sampling ──
10:  n_A ← 0                                           ▷ count of top-class predictions
11:  for j ← 1 to n do
12:      η ← 𝒩(0, σ²I_d)
13:      if f_θ(x + η) = ĉ_A then
14:          n_A ← n_A + 1
15:      end if
16:  end for

17:  // ── Step 3: Clopper–Pearson lower bound on p_A ──
18:  p̲_A ← BetaInv(α, n_A, n − n_A + 1)              ▷ lower confidence bound

19:  // ── Step 4: Compute certified radius via Neyman–Pearson ──
20:  r_cert ← σ · Φ⁻¹(p̲_A)                           ▷ certified ℓ₂ radius

21:  // ── Step 5: Certification decision ──
22:  certified ← (r_cert ≥ ε) and (p̲_A > 0.5)

23:  t_end ← CLOCK()
24:  CertCost ← t_end − t_start

25:  return CertCost, certified
```

**Complexity:** $\mathcal{O}((n_0 + n) \cdot T_{f_\theta})$ — dominated by $(n_0 + n)$ forward passes of the base classifier. Typical $n \approx 10^4\text{–}10^5$.

---

### **Algorithm 16: Maximum Semantic Degradation (MSD)**

**Purpose:** Find the worst-case normalised task loss under bounded adversarial perturbation, quantifying the maximum performance drop from clean to adversarial conditions.

**Inputs:**
- $x \in \mathbb{R}^d$: clean input
- $f_\theta$: semantic model
- $L_T(\cdot, \cdot)$: task-specific loss function
- $y_{\text{true}}$: ground-truth label/target
- $\varepsilon$: perturbation budget
- $T_{\text{PGD}}, \eta$: PGD parameters
- $n_{\text{restarts}}$: number of random restarts

**Output:**
- $\mathrm{MSD} \in [0, 1]$: maximum semantic degradation

```
Algorithm 16  MSD — Maximum Semantic Degradation
─────────────────────────────────────────────────
Input : x ∈ ℝ^d, model f_θ, loss L_T, label y_true, budget ε, PGD (T,η), restarts R
Output: MSD ∈ [0, 1]

 1:  // ── Step 1: Clean loss baseline ──
 2:  L_clean ← L_T(f_θ(x), y_true)

 3:  // ── Step 2: Maximum achievable loss (model-agnostic upper bound) ──
 4:  L_max ← sup_{ŷ} L_T(ŷ, y_true)                  ▷ e.g., for CE loss: −ln(ε_floor)
 5:  //   Alternatively: L_max estimated empirically over the dataset

 6:  // ── Step 3: Multi-restart PGD to maximise loss ──
 7:  L_worst ← L_clean                                 ▷ initialise with clean loss
 8:  for r ← 1 to R do
 9:      δ ← Uniform(−ε, ε)^d                         ▷ random initialisation
10:      for t ← 1 to T do
11:          g ← ∇_δ L_T(f_θ(x + δ), y_true)          ▷ gradient ascent on loss
12:          δ ← δ + η · sign(g)
13:          δ ← Π_{‖·‖_∞ ≤ ε}(δ)                     ▷ project back onto ℓ∞ ball
14:      end for
15:      L_adv ← L_T(f_θ(x + δ), y_true)
16:      L_worst ← max(L_worst, L_adv)
17:  end for

18:  // ── Step 4: Normalise degradation ──
19:  if L_max ≤ L_clean then
20:      return MSD ← 0                                ▷ no room for degradation
21:  end if
22:  MSD ← (L_worst − L_clean) / (L_max − L_clean)

23:  return clamp(MSD, 0, 1)
```

**Complexity:** $\mathcal{O}(R \cdot T_{\text{PGD}} \cdot T_{\nabla})$ — $R$ restarts of $T$ PGD steps each.

---

## Summary Table

| # | Metric | Dimension | Range | Complexity |
|---|--------|-----------|-------|------------|
| 1 | RSE | Fidelity | $[0,1]$ | $\mathcal{O}(N \log N \cdot d)$ |
| 2 | SWD | Fidelity | $[0,+\infty)$ | $\mathcal{O}(NML)$ |
| 3 | S³I | Fidelity | $[-1,1]$ | $\mathcal{O}(Nwd)$ |
| 4 | NSMI | Fidelity | $[0,1]$ | $\mathcal{O}(N \log N \cdot d)$ |
| 5 | TSR | Task | $[0,1]$ | $\mathcal{O}(N)$ |
| 6 | AP | Task | $[0,1]$ | $\mathcal{O}(m)$ |
| 7 | SU | Task | $[0,1]$ | $\mathcal{O}(Nd)$ |
| 8 | CE | Task | $[0,+\infty)$ | $\mathcal{O}(N)$ |
| 9 | ID | Intent | $[0,+\infty)$ | $\mathcal{O}(K)$ |
| 10 | ICC | Intent | $(-1,1)$ | $\mathcal{O}(T_{\text{model}})$ |
| 11 | SCI | Intent | $[0,1]$ | $\mathcal{O}(\|R\|^2 K)$ |
| 12 | PF | Intent | $[0,1]$ | $\mathcal{O}(N \cdot T_{\text{oracle}})$ |
| 13 | ARR | Resilience | $[0,+\infty)$ | $\mathcal{O}(B \cdot T \cdot T_{\nabla})$ |
| 14 | SASR | Resilience | $[0,1]$ | $\mathcal{O}(N \cdot T_{\mathcal{A}})$ |
| 15 | CertCost | Resilience | $[0,+\infty)$ s | $\mathcal{O}(n \cdot T_{f_\theta})$ |
| 16 | MSD | Resilience | $[0,1]$ | $\mathcal{O}(R \cdot T \cdot T_{\nabla})$ |
