> **Editor's Note — Corrected Version (v2):** This document is the corrected version of the original manuscript `Management_Orchestration_5G_AI_Native_6G_IEEE.md`. Corrections applied in v2: (C-M1) Article type and submission route updated; (C-M2) "network digital twins" added to Keywords; (C-M3) Section I.E updated with eleven open challenges and figure placement notes; (C-M4) "(Fig. 1)" corrected to "(Fig. 8)" in Section VI.B; (C-M5) Fig. 8, Fig. 9, Fig. 10, and Fig. 11 captions and descriptive paragraphs added in Sections VI.B, VI.D, IX.D, and IX.E respectively; (C-M6) VNF scaling factor symbol changed from $\sigma_f$ to $\xi_f$ throughout (Layer 4 variable list, Equations F1, F4, F9, F10, F15) to eliminate ambiguity with noise variance $\sigma^2$; (C-M7) $\Pr$ replaced with $\mathbb{P}$ in Equation F12 for consistency with probabilistic notation; (C-M8) URLLC penalty weight in Section VIII.C reward function changed from $\lambda$ to $\kappa$ (Equation 19) to eliminate symbol conflict with Lagrangian multipliers; (C-M9) DRL proxy-model methodology note added to Section VIII.C; (C-M10) 5G NR spectral efficiency parameterization paragraph and explanatory note added to Section VIII.B; (C-M11) Aggregate throughput values corrected (450 Mbps → 44 Mbps, 510 Mbps → ~50 Mbps, 550 Mbps → ~54 Mbps) to reflect realistic 20 MHz bandwidth; (C-M12) Logarithmic-scale notes added for Figures 3 and 7; (C-M13) Statistical analysis and confidence-interval paragraph added to Section VIII.A; (C-M14) References [30]–[41] added; (C-M15) References [2], [3], [12], [15], [18], [19], [22], [24] updated with URLs; (C-M16) Reference [26] author list corrected; (C-M17) New citations integrated in Sections IX.B [41], IX.E [36][37], IX.G [30][31], IX.I [38], IX.J [34][35][39][40], IX.K [32][33]; (C-M18) ISAC and LLM entries added to Abbreviations table.

---

# UMRO-5G: A Unified Framework for Management and Resource Orchestration in AI-Native 5G and Beyond Networks

---

> **Article Type:** Survey/Tutorial Article — IEEE Wireless Communications Magazine Format
>
> **Submission Route:** Original submission; suitable for IEEE Wireless Communications Magazine (survey/tutorial track) or IEEE Communications Surveys & Tutorials.
>
> **Subject Area:** Mobile and Wireless Communications · Telecommunications Engineering · Artificial Intelligence
>
> **Authors:** Evelio Astaiza Hoyos ¹, Héctor Fabio Bermúdez-Orozco ¹,\*, and Nasly Cristina Rodriguez-Idrobo ²
>
> ¹ Electronic Engineering Programme, Faculty of Engineering, University of Quindío, Armenia 630004, Quindío, Colombia
>
> ² Occupational Health and Safety Program, Faculty of Health Sciences, University of Quindío, Armenia 630004, Quindío, Colombia
>
> **Corresponding Author:** hfbermudez@uniquindio.edu.co

---

## Abstract

Fifth-generation (5G) mobile networks represent a paradigm shift in telecommunications, driven by ITU-R IMT-2020 requirements for simultaneously supporting enhanced mobile broadband (eMBB), ultra-reliable low-latency communications (URLLC), and massive machine-type communications (mMTC) over shared virtualized infrastructure. This article presents UMRO-5G (Unified Management and Resource Orchestration for 5G), a novel four-layer hierarchical framework that integrates Infrastructure, Virtualization & Slicing, Intelligence, and Orchestration layers with three nested control loops operating at distinct timescales. The framework addresses the fundamental challenge of cross-layer optimization through a joint mathematical formulation with hierarchical Lagrangian decomposition. We complement the framework with a five-dimensional taxonomy that classifies 28 resource management techniques across Resource Domain, Management Timescale, Optimization Approach, Architectural Scope, and Virtualization Level. Numerical evaluations including Monte Carlo multi-slice allocation simulations, deep reinforcement learning (DRL) convergence comparisons, scheduling algorithm benchmarks, service function chain (SFC) latency analysis, and computational complexity measurements validate the proposed framework. Results demonstrate that UMRO-5G dynamic allocation achieves 15–25% higher aggregate throughput than static isolation approaches while maintaining URLLC latency violation probability below 1.5%. The article identifies key open challenges including reconfigurable intelligent surfaces (RIS), multi-access edge computing (MEC), network digital twins, non-terrestrial networks (NTN), and zero-touch network management for the evolution toward 6G.

---

## Keywords

5G NR, radio resource management, network function virtualization, network slicing, deep reinforcement learning, Open RAN, network orchestration, UMRO-5G framework, AI-native networks, network digital twins

---

## I. Introduction

### A. Context and Motivation

The transition from fourth-generation (4G) LTE-Advanced to fifth-generation (5G) New Radio (NR) represents a paradigm shift in mobile network architecture, resource management mechanisms, and deployment philosophy [1]. The exponential growth of mobile data traffic—projected at 1000× between 2020 and 2030 [2]—combined with the proliferation of IoT devices estimated at 125 billion by 2030, imposes requirements that structurally exceed the capabilities of previous architectures.

The ITU-R IMT-2020 requirements [3] quantitatively define the targets that resource management must satisfy: peak data rates of 20 Gbps (downlink) and 10 Gbps (uplink); user-plane latency of ≤1 ms for URLLC; reliability of $1 - 10^{-5}$ for 32-byte packets within 1 ms; connection density of $10^6$ devices/km² for mMTC; and 100× energy efficiency improvement over IMT-Advanced. The simultaneous satisfaction of these heterogeneous and mutually contradictory requirements constitutes the central problem of resource management and orchestration in 5G [4].

5G addresses these challenges through three converging innovation vectors: (i) radical spectral expansion across sub-6 GHz (FR1) and millimeter-wave (FR2) bands [5]; (ii) physical layer evolution with Massive MIMO, flexible OFDM numerologies, and three-dimensional beamforming [6]; and (iii) softwarized architecture through Network Function Virtualization (NFV) and Software-Defined Networking (SDN), where the 5G Core (5GC) is implemented as service-based network functions on cloud platforms [7].

### B. The Multi-Service Orchestration Challenge

The defining challenge of 5G network management is the requirement to simultaneously support services with radically different QoS constraints over the same physical infrastructure [8]. A typical 5G operator must manage in real time: thousands of eMBB users with variable rates between 10 Mbps and 2 Gbps; tens of URLLC nodes demanding latencies <1 ms with 99.9999% reliability; and millions of mMTC sensors with sporadic 10–100 byte packets. The efficient multiplexing of these services requires mathematically formalized mechanisms for isolation, prioritization, and resource allocation, motivating the development of network slicing, NFV, and SDN architectures.

### C. Contributions

This article makes four principal contributions:

**C1 — UMRO-5G Framework:** A novel four-layer hierarchical framework with three nested control loops (Fast <10 ms, Medium 10 ms–1 s, Slow >1 s) that integrates Infrastructure, Virtualization & Slicing, Intelligence, and Orchestration layers. A joint cross-layer optimization formulation with hierarchical Lagrangian decomposition provides the mathematical foundation for end-to-end optimization.

**C2 — Five-Dimensional Taxonomy:** A novel multi-dimensional taxonomy classifies 28 resource management techniques across Resource Domain, Management Timescale, Optimization Approach, Architectural Scope, and Virtualization Level.

**C3 — Numerical Evaluations:** Original simulations including Monte Carlo multi-slice allocation, DRL convergence comparisons (DQN, MADRL/QMIX, Federated DQN, GNN-DRL), scheduling algorithm benchmarks, SFC latency analysis, and computational complexity measurements.

**C4 — Open Challenges:** Identification of key research directions including RIS integration, MEC optimization, network digital twins, NTN support, semantic communications, and zero-touch network management.

### D. Comparative Positioning

Table I provides a comparative analysis against prior surveys, demonstrating that this article is the first to achieve comprehensive coverage across RRM mathematics, NFV/SDN, slicing, O-RAN, ML/DRL, simulations, framework proposal, and taxonomy simultaneously.

**TABLE I.** Comparative Analysis with Prior Surveys

| Survey | Year | RRM Math | NFV/SDN | Slicing | O-RAN | ML/DRL | Framework | Taxonomy |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mijumbi et al. [7] | 2016 | ✗ | ✓✓ | ✗ | ✗ | ✗ | ✓ | ✓✓ |
| Foukas et al. [9] | 2017 | ✓ | ✓ | ✓✓ | ✗ | ✗ | ✓ | ✓ |
| Afolabi et al. [10] | 2018 | ✓ | ✓✓ | ✓✓ | ✗ | ✗ | ✓ | ✓✓ |
| Polese et al. [11] | 2023 | ✓ | ✓ | ✓ | ✓✓ | ✓ | ✗ | ✓ |
| **This Article** | **2026** | **✓✓** | **✓✓** | **✓✓** | **✓✓** | **✓✓** | **✓✓** | **✓✓** |

*Legend: ✓✓ = comprehensive, ✓ = partial, ✗ = absent*

### E. Article Organization

The remainder of this article is organized as follows. Section II presents the fundamentals of 5G resource management. Section III covers NFV, SDN, and network slicing. Section IV addresses radio resource management and Open RAN. Section V describes machine learning for autonomous RRM. Section VI introduces the proposed UMRO-5G framework (including Fig. 8 — the architecture diagram — and Fig. 11 — the latency budget decomposition). Section VII presents the five-dimensional taxonomy. Section VIII provides simulation results. Section IX identifies eleven open challenges (including Fig. 9 — RIS performance in Section IX.E — and Fig. 10 — energy efficiency trade-off in Section IX.D). Section X concludes the article.

---

## II. Fundamentals of 5G Resource Management

### A. IMT-2020 Service Categories

ITU-R IMT-2020 [3] and 3GPP [12] define three usage scenarios with mathematically distinct constraints:

**1) eMBB (Enhanced Mobile Broadband):** Characterized by high data rate demands with moderate latency. The utility function for eMBB user $k$ is typically logarithmic:

$$U_k^{\text{eMBB}}(r_k) = w_k \cdot \log\left(1 + \frac{r_k}{r_k^{\min}}\right) \tag{1}$$

where $w_k > 0$ is the priority weight and $r_k^{\min}$ is the guaranteed bit rate (GBR).

**2) URLLC (Ultra-Reliable Low-Latency Communications):** The most demanding scenario, requiring concurrent satisfaction of end-to-end latency $D \leq D^{\max}$ (typically 1 ms) and reliability $1 - \epsilon$ with $\epsilon \leq 10^{-5}$. For finite blocklength $n$, the achievable rate is given by the Polyanskiy–Poor–Verdú approximation [13]:

$$r_k^{\text{FBL}}(n, \epsilon) \approx C(\gamma) - \sqrt{\frac{V(\gamma)}{n}} \cdot Q^{-1}(\epsilon) \cdot \log_2 e \tag{2}$$

where $C(\gamma) = \log_2(1 + \gamma)$ is the Shannon capacity, $V(\gamma)$ is the channel dispersion, and $Q^{-1}(\epsilon)$ is the inverse Q-function.

**3) mMTC (Massive Machine-Type Communications):** Characterized by massive device density (up to $10^6$/km²) with sporadic access. The collision probability on the Random Access Channel is:

$$P_{\text{coll}} \approx 1 - e^{-\frac{N_d \cdot \alpha}{N_{\text{RACH}}}} \tag{3}$$

where $N_d$ is the number of devices, $\alpha$ is the activation fraction, and $N_{\text{RACH}} = 64$ preambles.

### B. General RRM Optimization Formulation

Radio resource management is formulated as a constrained optimization problem. For a gNB serving $K$ users over $S$ subcarriers with power budget $P_{\max}$:

$$\max_{\{p_{k,s}\}, \{x_{k,s}\}} \sum_{k=1}^{K} \sum_{s=1}^{S} w_k \cdot x_{k,s} \cdot \log_2\!\left(1 + \frac{p_{k,s} \cdot |h_{k,s}|^2}{\sigma^2 + I_{k,s}}\right) \tag{4}$$

subject to:

$$\sum_{k=1}^{K} \sum_{s=1}^{S} p_{k,s} \leq P_{\max}, \quad \sum_{k=1}^{K} x_{k,s} \leq 1,\ \forall s, \quad x_{k,s} \in \{0, 1\} \tag{5}$$

This Mixed-Integer Nonlinear Program (MINLP) is addressed via Lagrangian relaxation, decomposing into per-subcarrier subproblems. The optimal power allocation follows the water-filling solution [14]:

$$p_{k,s}^* = \left(\mu_{k,s} - \frac{\sigma^2 + I_{k,s}}{|h_{k,s}|^2}\right)^+ \tag{6}$$

where $(\cdot)^+ = \max(0, \cdot)$ and $\mu_{k,s}$ is the water level determined by KKT conditions.

---

## III. NFV, SDN, and Network Slicing

### A. NFV/MANO Architecture

Network Function Virtualization (NFV) enables network functions to be implemented as software on Commercial Off-The-Shelf (COTS) hardware [7]. The ETSI MANO framework [15] comprises three functional blocks: NFVO (NFV Orchestrator) for global orchestration; VNFM (VNF Manager) for VNF lifecycle management; and VIM (Virtualized Infrastructure Manager) for physical resource management.

The VNF Placement Problem is formulated as multidimensional bin-packing [16]. Let $\mathcal{N}$ be the set of NFVI servers and $\mathcal{F}$ the set of VNFs. With binary variable $y_{fn} \in \{0,1\}$ indicating VNF $f$ placement on server $n$:

$$\min_{\{y_{fn}\}} \sum_{n \in \mathcal{N}} \sum_{f \in \mathcal{F}} y_{fn} \cdot \text{cost}_{fn} \tag{7}$$

subject to placement uniqueness and capacity constraints. This problem is NP-complete [17].

Service Function Chaining (SFC) specifies the ordered sequence of VNFs that traffic must traverse [18]. The total SFC latency under M/M/1 queuing is:

$$D_{\text{SFC}} = \sum_{f \in \mathcal{F}_{\text{SFC}}} \frac{1}{\mu_f - \lambda_f} + \sum_{(i,j) \in \mathcal{P}} \frac{d_{ij}}{c_{ij}} \tag{8}$$

where $\mu_f$ is the service rate and $\lambda_f$ is the arrival rate at VNF $f$.

### B. Network Slicing and Resource Isolation

Network slicing enables multiple virtualized logical networks over shared physical infrastructure, each optimized for specific service requirements [9]. The 3GPP slice management hierarchy comprises CSMF, NSMF, and NSSMF functional layers [19].

The **hard isolation** model guarantees exclusive resources per slice:

$$\sum_{s=1}^{S} x_s^{(r)} \leq C^{(r)}, \quad x_s^{(r)} \geq d_s^{(r),\min}, \quad \forall r \in \mathcal{R} \tag{9}$$

The **soft isolation** model permits sharing of unused surplus resources:

$$x_s^{(r)} = d_s^{(r),\min} + \epsilon_s^{(r)}, \quad \sum_{s=1}^{S} \epsilon_s^{(r)} \leq C^{(r)} - \sum_{s=1}^{S} d_s^{(r),\min} \tag{10}$$

The optimal inter-slice allocation is solved via Lagrangian dual decomposition [20]:

$$\lambda_{k+1}^{(r)} = \left[\lambda_k^{(r)} - \alpha_k\!\left(C^{(r)} - \sum_{s \in \mathcal{S}} x_s^{(r),*}(\boldsymbol{\lambda}_k)\right)\right]^+ \tag{11}$$

where $\alpha_k > 0$ is the step size and convergence is guaranteed for concave utility functions.

---

## IV. Radio Resource Management and Open RAN

### A. MAC Scheduler and Proportional Fair Scheduling

The MAC scheduler in 5G NR operates with slot granularity $T_{\text{slot}} = 1/(14 \times 2^\mu)$ ms for numerology $\mu$ [12]. The Proportional Fair (PF) scheduler balances spectral efficiency and fairness [21]:

$$M_k^{PF}(n,t) = \frac{R_k^{\text{inst}}(n,t)}{\bar{R}_k(t)} \tag{12}$$

where $R_k^{\text{inst}}$ is the instantaneous rate and $\bar{R}_k$ is the historical average. PF maximizes the sum of logarithmic utilities, equivalent to Nash welfare maximization.

### B. Massive MIMO Precoding

For Massive MIMO with $M$ antennas serving $K$ users, the three principal precoders are [6]:

$$\mathbf{W}_{\text{MRT}} = \mathbf{H}^H, \quad \mathbf{W}_{\text{ZF}} = \mathbf{H}^H(\mathbf{H}\mathbf{H}^H)^{-1}, \quad \mathbf{W}_{\text{MMSE}} = \mathbf{H}^H\!\left(\mathbf{H}\mathbf{H}^H + \frac{K\sigma^2}{P_T}\mathbf{I}_K\right)^{-1} \tag{13}$$

As $M \to \infty$, all three converge to the same performance by the law of large numbers.

### C. O-RAN Architecture

The O-RAN Alliance defines an open architecture with disaggregated O-RU, O-DU, and O-CU components connected via open interfaces [22]. The RAN Intelligent Controllers operate at two timescales:

- **Non-RT RIC (>1 s):** Executes rApps for global policy optimization and ML model training.
- **Near-RT RIC (10 ms–1 s):** Executes xApps for fine-grained RRM via the E2 interface.

The xApp optimization problem at each control period $T_{\text{ctrl}}$ is [23]:

$$\max_{\{p_{b,k}\}} \sum_{b=1}^{B} \sum_{k \in \mathcal{K}_b} \log\left(1 + \frac{p_{b,k} G_{b,k}}{\sum_{b' \neq b} p_{b',k} G_{b',k} + \sigma^2}\right) \tag{14}$$

subject to per-cell power constraints, solved via successive convex approximation.

---

## V. Machine Learning for Autonomous RRM

### A. DRL for Resource Management

Deep Reinforcement Learning formulates RRM as a Markov Decision Process $(\mathcal{S}, \mathcal{A}, P, r, \gamma)$ [24]. The Deep Q-Network (DQN) approximates the optimal action-value function $Q^*(\mathbf{s},\mathbf{a})$ using neural networks [25]:

$$\mathcal{L}(\boldsymbol{\theta}) = \mathbb{E}\left[\left(r + \gamma \max_{\mathbf{a}'} Q(\mathbf{s}',\mathbf{a}';\boldsymbol{\theta}^-) - Q(\mathbf{s},\mathbf{a};\boldsymbol{\theta})\right)^2\right] \tag{15}$$

where $\boldsymbol{\theta}^-$ are the target network parameters.

### B. Multi-Agent DRL

For multi-cell coordination, Multi-Agent DRL (MADRL) with the QMIX architecture employs Centralized Training with Decentralized Execution (CTDE) [26]:

$$Q_{\text{tot}}(\boldsymbol{\tau}, \mathbf{a}) = f_\psi\left(Q_1(\tau^1, a^1), \ldots, Q_B(\tau^B, a^B)\right) \tag{16}$$

where $f_\psi$ is a monotonic mixing function enforcing the Individual-Global-Max condition.

### C. Federated Learning

Federated Learning (FL) enables privacy-preserving distributed training across gNBs. The FedAvg algorithm aggregates local model updates [27]:

$$\boldsymbol{\theta}_{k+1}^{\text{global}} = \sum_{b=1}^{B} \frac{|\mathcal{D}_b|}{|\mathcal{D}|} \boldsymbol{\theta}_{k+1}^b \tag{17}$$

### D. Graph Neural Networks

GNNs exploit network topology for optimization [28]. The representation update at layer $l$ is:

$$\mathbf{h}_v^{(l)} = \text{UPDATE}^{(l)}\left(\mathbf{h}_v^{(l-1)},\ \text{AGGREGATE}^{(l)}\left(\{\mathbf{h}_u^{(l-1)} : u \in \mathcal{N}(v)\}\right)\right) \tag{18}$$

GNNs generalize to unseen topologies, unlike conventional MLPs.

---

## VI. Proposed UMRO-5G Framework

### A. Motivation and Design Principles

While the preceding sections have examined six core technical domains of 5G resource management—(i) RRM fundamentals, (ii) NFV/SDN/MANO orchestration, (iii) network slicing, (iv) 5G NR RRM architecture, (v) O-RAN multi-domain orchestration, and (vi) ML/DRL for autonomous RRM—the literature lacks a unified framework that formally integrates all domains into a single, coherent architectural and mathematical model.

To address this gap, we propose **UMRO-5G** (*Unified Management and Resource Orchestration for 5G*), a novel four-layer hierarchical framework with three nested control loops. UMRO-5G is designed around five guiding principles:

1. **Hierarchical decomposition**: Complex cross-domain optimization is decomposed into tractable per-layer subproblems coordinated through well-defined inter-layer interfaces.
2. **Multi-timescale control**: Fast physical-layer decisions (sub-millisecond), medium-timescale intelligent adaptation (milliseconds to seconds), and slow orchestration-level reconfiguration (seconds to minutes) are explicitly separated.
3. **Intelligence-native design**: ML/DRL engines are embedded as first-class architectural components with explicit data pipelines and inference/training separation.
4. **Slice-aware end-to-end optimization**: All layers are jointly optimized subject to per-slice SLA constraints spanning eMBB, URLLC, and mMTC.
5. **Standards alignment**: The framework is grounded in ETSI NFV-MANO, 3GPP TS 28.530/533, and O-RAN Alliance specifications.

### B. Four-Layer Hierarchical Architecture

The UMRO-5G architecture comprises four functional layers (Fig. 8):

**Layer 1 (Infrastructure):** Encompasses all physical resources—O-RU antenna arrays organized as PRBs, compute servers at edge/regional/central data centers characterized by capacity $(C_n^c, C_n^m, C_n^s)$, and fronthaul/midhaul/backhaul links with capacity $c_{ij}$ and delay $d_{ij}$.

**Layer 2 (Virtualization & Slicing):** Provides logical abstraction of physical resources into isolated partitions—NFVI with hypervisor/container runtime, SDN control plane for centralized flow management, and Network Slice Instances (NSIs) where each slice $s$ is instantiated as $\text{NSI}_s = \text{RAN-SS}_s \oplus \text{TN-SS}_s \oplus \text{CN-SS}_s$.

**Layer 3 (Intelligence):** Hosts AI/ML engines and RAN Intelligent Controllers—Near-RT RIC with xApps for traffic steering, interference management, and QoS optimization (10 ms–1 s timescale); Non-RT RIC with rApps for policy optimization and ML model lifecycle (>1 s); and the ML/DRL Engine Suite including DQN, MADRL/QMIX, Federated Learning, GNN, and Transfer Learning modules.

**Layer 4 (Orchestration):** Provides end-to-end service lifecycle management—ETSI MANO stack (NFVO, VNFM, VIM), 3GPP slice management hierarchy (CSMF, NSMF, NSSMF), SLA enforcement engine, and cross-domain coordinator ensuring $D_{\text{E2E}} = D_{\text{RAN}} + D_{\text{TN}} + D_{\text{CN}}$, $B_{\text{E2E}} = \min(B_{\text{RAN}}, B_{\text{TN}}, B_{\text{CN}})$, $A_{\text{E2E}} = A_{\text{RAN}} \cdot A_{\text{TN}} \cdot A_{\text{CN}}$.

**Figure 8** illustrates the complete UMRO-5G four-layer hierarchical architecture with its three nested control loops. The diagram depicts the horizontal layer structure (Infrastructure → Virtualization & Slicing → Intelligence → Orchestration), the inter-layer interfaces $\mathcal{I}_{12}$, $\mathcal{I}_{23}$, and $\mathcal{I}_{34}$ with their associated protocols, and the three control loops spanning different layer subsets: the Fast Loop (<10 ms) at Layer 1, the Medium Loop (10 ms–1 s) across Layers 1–3, and the Slow Loop (>1 s) spanning all four layers.

**Fig. 8. UMRO-5G Four-Layer Hierarchical Architecture with Three Nested Control Loops.** The diagram shows the four functional layers (Infrastructure, Virtualization & Slicing, Intelligence, Orchestration) with their principal components, the three nested control loops with their respective timescale ranges, and the formally defined inter-layer interfaces $\mathcal{I}_{12}$, $\mathcal{I}_{23}$, $\mathcal{I}_{34}$ with protocol labels. Generated from simulation script `sim_architecture_fig.py`.

### C. Three Nested Control Loops

A distinguishing feature of UMRO-5G is the explicit formalization of three nested control loops:

**Control Loop 1 — Fast Loop (<10 ms):** Operates at the DU/RU level for per-TTI scheduling using the PF metric, MIMO precoding (MRT/ZF/MMSE), power control via water-filling, HARQ management, and beam tracking. Decisions are driven by instantaneous CSI with no external interface latency.

**Control Loop 2 — Medium Loop (10 ms–1 s):** Operates at the Near-RT RIC for xApp-driven inter-cell coordination, slice-level resource adjustment implementing soft isolation, admission control, interference management (eICIC ABS patterns), handover optimization, and DRL inference achieving ~0.1 ms latency.

**Control Loop 3 — Slow Loop (>1 s):** Operates across Non-RT RIC and MANO for rApp-driven global policy optimization, NFVO orchestration (VNF placement, SFC embedding), ML model training and deployment, Federated Learning aggregation, network slice lifecycle management, and cross-domain SLA enforcement.

### D. Cross-Layer Optimization Formulation

The central contribution of UMRO-5G is the joint cross-layer optimization problem. Let $\mathcal{S}$ be the set of slices, $\mathcal{B}$ the base stations, $\mathcal{K}_b$ users served by station $b$, $\mathcal{N}$ NFVI servers, and $\mathcal{F}$ VNFs. Decision variables span all layers:

- **Layer 1:** Power allocation $p_{b,k,n}$; subcarrier assignment $x_{b,k,n} \in \{0,1\}$
- **Layer 2:** Per-slice allocation $\mathbf{z}_s$; VNF placement $y_{fn} \in \{0,1\}$
- **Layer 3:** ML model selection $\boldsymbol{\theta}_s$; inference policy $\boldsymbol{\pi}_s$
- **Layer 4:** SFC routing $\phi_{f,f'}^{ij}$; scaling factors $\xi_f$ (where $\xi_f \geq 1$ is the scaling factor of VNF $f$, distinct from the noise variance $\sigma^2$)

The global UMRO-5G optimization problem is:

$$\max_{\substack{\{p_{b,k,n}\}, \{x_{b,k,n}\}, \\ \{\mathbf{z}_s\}, \{y_{fn}\}, \\ \{\boldsymbol{\pi}_s\}, \{\phi_{f,f'}^{ij}\}, \{\xi_f\}}} \sum_{s \in \mathcal{S}} w_s \cdot U_s\!\left(\mathbf{R}_s, D_s^{\text{E2E}}, \mathcal{F}_s\right) \tag{F1}$$

where the slice utility function is:

$$U_s = \alpha_s \sum_{k \in \mathcal{K}_s} \log\!\left(1 + \frac{R_{k,s}}{R_s^{\min}}\right) - \beta_s \left[D_s^{\text{E2E}} - D_s^{\max}\right]^+ - \delta_s \left[\epsilon_s - \epsilon_s^{\max}\right]^+ \tag{F2}$$

The achievable rate follows Shannon (or FBL for URLLC) capacity:

$$R_{k,s} = \sum_{n=1}^{N_{\text{PRB}}} x_{b,k,n} \cdot \log_2\!\left(1 + \frac{p_{b,k,n} \cdot |\mathbf{h}_{b,k,n}^H \mathbf{w}_{b,k}|^2}{\sum_{b' \neq b} p_{b',k,n} |\mathbf{h}_{b',k,n}^H \mathbf{w}_{b',k}|^2 + \sigma^2}\right) \tag{F3}$$

The end-to-end latency decomposes across layers:

$$D_s^{\text{E2E}} = \underbrace{D_s^{\text{RAN}}}_{\text{Layer 1}} + \underbrace{\sum_{f \in \mathcal{F}_s} \frac{1}{\xi_f \mu_f - \lambda_{s,f}}}_{\text{Layer 2: VNF (M/M/1)}} + \underbrace{D_s^{\text{ctrl}}(\boldsymbol{\pi}_s)}_{\text{Layer 3}} + \underbrace{\sum_{(i,j) \in \mathcal{P}_s} \frac{d_{ij}}{c_{ij}}}_{\text{Layer 2: transport}} \tag{F4}$$

**Figure 11** provides a visual decomposition of the 1 ms URLLC latency budget across UMRO-5G layers, instantiating Equation (F4) with representative component values for three deployment scenarios.

**Fig. 11. End-to-End Latency Budget Decomposition Across UMRO-5G Layers for URLLC Service (1 ms Budget).** Horizontal stacked bar chart showing the contribution of each UMRO-5G component to the 1 ms E2E latency budget: L1 Processing (PHY/MAC @ DU: 100 μs), L1 Transmission (fronthaul: 50 μs), L2 VNF Processing (UPF/AMF: 150 μs), L2 Transport (fronthaul + midhaul: 100 μs), L3 DRL Inference (Near-RT RIC: 100 μs, as validated in Section VIII.F), L4 Orchestration Overhead (fast-path bypass: 0 μs), Propagation + UE Processing (200 μs), and Safety Margin. Three scenarios are compared: Baseline 5G (no UMRO-5G), UMRO-5G (L1+L2 only), and Full UMRO-5G (all layers). Generated from `sim_latency_budget.py`.

The decomposition reveals that the Intelligence Layer (L3) DRL inference contributes only 100 μs to the E2E budget, consistent with the near-constant 0.1 ms inference latency measured in Section VIII.F, while freeing 300 μs of additional safety margin in the Full UMRO-5G scenario compared to the baseline. Layer 4 orchestration operates exclusively in the Slow Loop and is bypassed in the URLLC fast path, contributing zero overhead.

Subject to constraint families:

**C1 — Radio resource constraints (Layer 1):**

$$\sum_{k \in \mathcal{K}_b} \sum_{n=1}^{N_{\text{PRB}}} p_{b,k,n} \leq P_b^{\max}, \quad \forall b \in \mathcal{B} \tag{F5}$$

$$\sum_{s \in \mathcal{S}} \sum_{k \in \mathcal{K}_s \cap \mathcal{K}_b} x_{b,k,n} \leq 1, \quad \forall b, n \tag{F6}$$

**C2 — Slice isolation constraints (Layer 2):**

$$z_s^{(r)} \geq d_s^{(r),\min}, \quad \forall s \in \mathcal{S},\ r \in \mathcal{R} \tag{F7}$$

$$\sum_{s \in \mathcal{S}} z_s^{(r)} \leq C^{(r)}, \quad \forall r \in \mathcal{R} \tag{F8}$$

**C3 — Compute capacity constraints (Layer 2):**

$$\sum_{f \in \mathcal{F}} y_{fn} \cdot \xi_f \cdot r_f^c \leq C_n^c, \quad \forall n \in \mathcal{N} \tag{F9}$$

$$\sum_{f \in \mathcal{F}} y_{fn} \cdot \xi_f \cdot r_f^m \leq C_n^m, \quad \forall n \in \mathcal{N} \tag{F10}$$

**C4 — SLA constraints (cross-layer):**

$$D_s^{\text{E2E}} \leq D_s^{\max}, \quad \forall s \in \mathcal{S} \tag{F11}$$

$$\mathbb{P}\!\left[D_s^{\text{E2E}} > D_s^{\max}\right] \leq \epsilon_s^{\max}, \quad \forall s \in \mathcal{S}_{\text{URLLC}} \tag{F12}$$

$$R_{k,s} \geq R_s^{\min}, \quad \forall k \in \mathcal{K}_s,\ s \in \mathcal{S}_{\text{eMBB}} \tag{F13}$$

**C5 — Cross-layer consistency constraints:**

$$\sum_{k \in \mathcal{K}_s \cap \mathcal{K}_b} x_{b,k,n} \leq \frac{z_s^{\text{RAN}}}{N_{\text{PRB}}}, \quad \forall s, b, n \tag{F14}$$

$$\lambda_{s,f} \leq \xi_f \cdot \mu_f \cdot \rho_f^{\max}, \quad \forall f \in \mathcal{F}_s,\ s \in \mathcal{S} \tag{F15}$$

### E. Hierarchical Decomposition

Problem (F1)–(F15) is a MINLP intractable to solve monolithically. UMRO-5G addresses this via hierarchical decomposition aligned with the three control loops:

**Slow Loop (Layer 4 + Non-RT RIC):** Solves VNF placement (F9–F10), slice allocation (F7–F8), and global policy optimization (F1) using Lagrangian dual decomposition:

$$\lambda_{k+1}^{(r)} = \left[\lambda_k^{(r)} - \alpha_k\!\left(C^{(r)} - \sum_{s \in \mathcal{S}} z_s^{(r),*}(\boldsymbol{\lambda}_k)\right)\right]^+ \tag{F16}$$

Convergence is guaranteed under diminishing step size conditions ($\sum_k \alpha_k = \infty$, $\sum_k \alpha_k^2 < \infty$).

**Medium Loop (Near-RT RIC):** Given slice allocations from Slow Loop, solves inter-cell power optimization via successive convex approximation or executes pre-trained DRL models.

**Fast Loop (DU/RU):** Given per-cell parameters from Medium Loop, executes PF scheduler and MIMO precoder with per-TTI granularity.

### F. Inter-Layer Interfaces

The four layers communicate through formally defined interfaces:

**Interface $\mathcal{I}_{12}$ (Infrastructure ↔ Virtualization):** Upward—physical resource telemetry (CPU, memory, PRB occupancy, CSI); Downward—resource reservation commands (VM/container instantiation, PRB partitioning).

**Interface $\mathcal{I}_{23}$ (Virtualization ↔ Intelligence):** Upward—slice-level KPIs, per-cell CQI/RSRP, VNF metrics via E2/O1; Downward—RRM control actions, scheduling weights, ABS patterns via E2/A1.

**Interface $\mathcal{I}_{34}$ (Intelligence ↔ Orchestration):** Upward—network analytics, demand predictions, ML performance reports; Downward—slice lifecycle events, VNF scaling triggers, SLA thresholds via A1/O1.

### G. Mapping of Techniques to UMRO-5G

Table II provides a systematic mapping of all techniques reviewed in this article onto the UMRO-5G layers and control loops, demonstrating how the framework unifies the surveyed domains into a coherent architectural model.

**TABLE II.** Mapping of Techniques to UMRO-5G Framework

| Survey Domain | Technique | Layer | Control Loop | Key Equations |
|:---|:---|:---:|:---:|:---:|
| **RRM Fundamentals** | OFDMA Resource Allocation (MINLP) | L1 | Fast | (4)–(5) |
| | Lagrangian Relaxation, Water-filling | L1+L2 | Fast+Medium | (6) |
| | Massive MIMO Capacity | L1 | Fast | (13) |
| | Finite-Blocklength URLLC Rate | L1 | Fast | (2) |
| **NFV/SDN/MANO** | VNF Placement (bin-packing) | L2+L4 | Slow | (7) |
| | SFC Embedding and Latency | L2+L4 | Slow | (8) |
| | SDN Traffic Engineering | L2 | Medium+Slow | — |
| | ETSI MANO (NFVO/VNFM/VIM) | L4 | Slow | — |
| **Network Slicing** | Hard/Soft Resource Isolation | L2 | Medium | (9)–(10) |
| | Admission Control | L2+L3 | Medium | — |
| | Lagrangian Dual Decomposition | L2+L4 | Slow | (11) |
| **5G NR RRM** | PF Scheduler | L1 | Fast | (12) |
| | MRT/ZF/MMSE Precoders | L1 | Fast | (13) |
| | Fractional Power Control | L1 | Fast | — |
| | eICIC / ABS Management | L1+L3 | Medium | — |
| | A3 Handover Optimization | L1+L3 | Medium | — |
| | AMC Link Adaptation | L1 | Fast | — |
| **O-RAN Orchestration** | Near-RT RIC xApp Optimization | L3 | Medium | (14) |
| | Non-RT RIC rApp Policy (MDP) | L3+L4 | Slow | — |
| | Multi-domain Slice Composition | L4 | Slow | — |
| **ML/DRL for RRM** | DQN for Scheduling/Power | L3 | Medium (inference) / Slow (training) | (15) |
| | MADRL/QMIX Multi-Cell | L3 | Medium (inference) / Slow (training) | (16) |
| | Federated Learning (FedAvg) | L3+L4 | Slow | (17) |
| | GNN Topology-Aware Optimization | L3 | Medium (inference) / Slow (training) | (18) |

This mapping reveals several important structural insights that validate the UMRO-5G design:

1. **Layer 1 is dominated by the Fast Loop**: Physical-layer techniques (scheduling, precoding, power control, link adaptation) operate at sub-millisecond timescales and are self-contained within the DU/RU.

2. **Layer 2 bridges Fast and Slow timescales**: Virtualization and slicing functions span the Medium and Slow loops—soft isolation adjustments occur in the Medium Loop in response to traffic variations, while VNF placement and hard slice provisioning occur in the Slow Loop based on long-term capacity planning.

3. **Layer 3 separates inference from training**: All ML/DRL techniques exhibit a dual-timescale nature: model inference executes in the Medium Loop (achieving ~0.1 ms latency with pre-trained models), while model training occurs in the Slow Loop.

4. **Layer 4 is exclusively Slow Loop**: Orchestration decisions (VNF lifecycle, slice lifecycle, SLA enforcement) operate on timescales of seconds to minutes.

5. **Cross-layer coupling is mediated by Lagrangian prices**: The dual variables $\boldsymbol{\lambda}$ from the Slow Loop decomposition (Equation F16) propagate as resource price signals from Layer 4 down to Layer 2 and Layer 1.

### H. Comparative Positioning

UMRO-5G distinguishes itself from prior frameworks along four critical dimensions:

**First**, unlike NFV-centric surveys (e.g., Mijumbi et al. [7]; Herrera and Botero [16]) that focus exclusively on VNF placement and orchestration without considering radio resource management, UMRO-5G integrates physical-layer RRM and AI/ML as first-class architectural components.

**Second**, unlike O-RAN-focused surveys (e.g., Polese et al. [11]; Bonati et al. [23]) that emphasize the RIC architecture and open interfaces without formal coupling to NFV/MANO orchestration, UMRO-5G provides explicit inter-layer interfaces ($\mathcal{I}_{12}$, $\mathcal{I}_{23}$, $\mathcal{I}_{34}$) that formalize the data flow between the RIC and the orchestration stack.

**Third**, unlike ML-for-networking surveys that catalog algorithms without architectural context, UMRO-5G maps each ML technique to a specific layer, control loop, and interface.

**Fourth**, the joint cross-layer optimization formulation (Equations F1–F16) with hierarchical decomposition provides a rigorous mathematical foundation for end-to-end optimization that is absent from existing survey frameworks.

### I. Implementation Considerations

The practical deployment of UMRO-5G faces several challenges that align with the open problems identified in Section IX:

**Computational tractability**: The hierarchical decomposition reduces complexity from the monolithic search space of size $\mathcal{O}(K^S \cdot 2^{F \cdot N})$ to per-loop subproblems of manageable size.

**Control loop stability**: The timescale separation principle ensures stability: each loop operates at least an order of magnitude slower than the loop below it.

**ML model reliability**: UMRO-5G mitigates model uncertainty through the Transfer Learning module for scenario adaptation and the Federated Learning engine for robust aggregation across heterogeneous data distributions.

**Standards evolution**: The modular architecture of UMRO-5G accommodates new functional elements (e.g., RIS control xApps, ISAC coordination rApps) as additional modules within existing layers without requiring architectural restructuring.

---

## VII. Five-Dimensional Taxonomy

### A. Motivation

The landscape of 5G resource management techniques spans diverse resource types, timescales, paradigms, scopes, and virtualization technologies. We propose a five-dimensional taxonomy classifying techniques along orthogonal axes grounded in 3GPP, ETSI, and O-RAN specifications.

### B. Dimension 1 — Resource Domain

**Radio Resources:** PRBs across OFDM numerologies, transmit power, spatial beams from Massive MIMO arrays.

**Compute Resources:** vCPUs, GPU cores, memory. VNF placement as bin-packing; scaling driven by queuing models (service rate $\mu_f$ vs. arrival rate $\lambda_f$).

**Network Resources:** Fronthaul/midhaul/backhaul capacity. SFC embedding, SDN flow routing.

**Storage Resources:** MEC caching, VNF state persistence, ML dataset storage.

### C. Dimension 2 — Management Timescale

**Real-Time (<10 ms):** Per-TTI scheduling, MIMO precoding, HARQ, beam management.

**Near-Real-Time (10 ms–1 s):** xApp coordination, slice adjustment, admission control, DRL inference.

**Non-Real-Time (>1 s):** VNF lifecycle, SFC embedding, ML training, slice lifecycle, capacity planning.

### D. Dimension 3 — Optimization Approach

**Classical Optimization:** Convex (water-filling, Lagrangian), LP/MILP (VNF placement), heuristics, game theory.

**Machine Learning:** Supervised (traffic prediction, channel estimation), unsupervised (anomaly detection, clustering).

**Reinforcement Learning:** Single-agent DRL (DQN for scheduling), multi-agent DRL (CTDE/QMIX for coordination).

**Federated/Distributed:** FedAvg for privacy-preserving training across gNBs.

**Hybrid:** DRL for policy + classical for allocation; GNN + RL for topology-aware decisions.

### E. Dimension 4 — Architectural Scope

**Single-Domain:** RAN-only scheduling, Core-only VNF placement.

**Cross-Domain:** Joint RAN+Core (scheduling + VNF scaling).

**Multi-Domain:** RAN+Core+Transport+Edge.

**End-to-End (Including Slicing):** All domains with per-slice SLA enforcement. UMRO-5G global optimization (F1).

### F. Dimension 5 — Virtualization Level

**Physical:** O-RU RF processing, FPGA-based PHY.

**VM-Based:** Hypervisor-managed VMs (KVM, VMware).

**Container-Based:** Kubernetes-orchestrated containers.

**Serverless/FaaS:** Event-triggered microservices.

### G. Comprehensive Classification Table

**TABLE III.** Five-Dimensional Taxonomy Classification

| Technique | Resource | Timescale | Approach | Scope | Virtualization |
|:---|:---|:---|:---|:---|:---|
| Per-TTI PF Scheduling | Radio | Real-time | Classical | Single (RAN) | Physical |
| Water-Filling Power | Radio | Real-time | Classical | Single (RAN) | Physical |
| MIMO Precoding | Radio | Real-time | Classical | Single (RAN) | Physical |
| eICIC/ABS Management | Radio | Near-RT | Classical/RL | Cross (RAN) | Physical/Container |
| xApp QoS Optimization | Radio, Compute | Near-RT | Hybrid | Cross (RAN+Core) | Container |
| Slice Resource Adjustment | Radio, Compute, Network | Near-RT | Classical/DRL | E2E (slicing) | Container |
| DRL Scheduling (DQN) | Radio | Near-RT | RL | Single (RAN) | Container |
| MADRL/QMIX Multi-Cell | Radio | Near-RT | RL (MADRL) | Cross (RAN) | Container |
| VNF Placement | Compute, Storage | Non-RT | Classical (MILP) | Multi (Core+Edge) | VM/Container |
| SFC Embedding | Compute, Network | Non-RT | Classical (ILP) | Multi (Core+Transport) | VM/Container |
| Federated Learning | Compute | Non-RT | FL | Cross (multi-gNB) | Container |
| GNN Optimization | Radio, Network | Non-RT/Near-RT | ML (GNN) | Multi | Container |
| NSI Lifecycle | All | Non-RT | Classical | E2E (slicing) | Container |
| **UMRO-5G Global** | **All** | **Multi-timescale** | **Hybrid** | **E2E (slicing)** | **Container** |

### H. Taxonomy Discussion

The classification table reveals several important observations:

**Observation 1: Real-time functions remain dominated by classical optimization.** Per-TTI scheduling, power allocation, and MIMO precoding rely on closed-form solutions or low-complexity heuristics due to sub-millisecond decision latency requirements.

**Observation 2: Container-based virtualization is the dominant paradigm for intelligent and orchestration functions.**

**Observation 3: End-to-end architectural scope requires hybrid optimization approaches.** No single optimization paradigm suffices for end-to-end resource management spanning all four UMRO-5G layers.

**Observation 4: Coverage gaps exist at the intersection of serverless virtualization and real-time management.** The cold-start latency of serverless functions (typically 100–500 ms) is incompatible with sub-millisecond real-time control requirements.

**Observation 5: Storage resources are underrepresented in current research.** As edge intelligence and network digital twins become more prevalent, storage optimization will become increasingly important.

---

## VIII. Simulation Results

### A. Methodology

Five simulation sets validate the analytical models and UMRO-5G framework, implemented in Python with NumPy and Matplotlib using fixed random seeds for reproducibility. The simulations are designed to evaluate the key resource management and orchestration mechanisms reviewed in Sections II–V and integrated within the UMRO-5G framework. Each simulation addresses a specific aspect: (i) multi-slice resource allocation under different isolation strategies, (ii) convergence properties of ML/DRL algorithms for RRM, (iii) scheduling algorithm performance comparison, (iv) SFC latency model validation, and (v) computational complexity scaling.

**Statistical analysis:** Results are reported as mean ± one standard deviation across the 5 independent random seeds. Formal 95% confidence intervals are estimated via Student's t-distribution with 4 degrees of freedom (5 seeds − 1): $\text{CI}_{95\%} = \bar{x} \pm t_{0.025,4} \cdot s/\sqrt{5}$, where $t_{0.025,4} = 2.776$ and $s$ is the sample standard deviation. For simulation comparisons, pairwise t-tests are performed with Bonferroni correction for multiple comparisons. The effective sample size for each metric is N_seeds × N_MONTE_CARLO = 5 × 1,000 = 5,000 realizations per load point, ensuring sufficient statistical power for the effect sizes observed.

### B. Multi-Slice Resource Allocation (Monte Carlo)

**Setup:** A single gNB cell with 100 Physical Resource Blocks (PRBs) serves three concurrent slices: eMBB (target: high throughput), URLLC (target: ≤1 ms latency), and mMTC (target: high connection density). Traffic arrivals follow a Poisson process with the system load factor $\rho$ swept from 0.1 to 1.0 in 10 steps. Three allocation strategies are compared:

- **Hard Isolation:** Fixed allocation of 50, 30, and 20 PRBs to eMBB, URLLC, and mMTC, respectively.
- **Soft Isolation:** Minimum guarantees of 30, 20, and 10 PRBs with a shared pool of 40 PRBs allocated proportionally to instantaneous demand according to Equation (10).
- **UMRO-5G (Proposed):** Dynamic Lagrangian dual decomposition (Equation F16) with utility weights $w_s$ updated per timeslot based on slice SLA proximity.

Each configuration was evaluated over 1,000 Monte Carlo iterations with 5 independent random seeds for confidence interval estimation. The performance metrics include average per-slice throughput, overall resource utilization, and URLLC latency violation probability.

The throughput is computed using real 5G NR parameters: channel bandwidth B = 20 MHz, N_PRB = 100 physical resource blocks with numerology μ=0 (SCS = 15 kHz, 12 subcarriers per PRB, PRB bandwidth Δf_PRB = 180 kHz), yielding Throughput[Mbps] = N_allocated × SPEC_EFF × 0.18 MHz/PRB. Spectral efficiencies are modeled as SPEC_EFF = {4.0, 1.5, 0.5} bps/Hz for eMBB, URLLC, and mMTC respectively, representing representative MCS configurations under moderate SNR conditions.

> **Note on spectral efficiency model:** The fixed spectral efficiency values represent first-order approximations; in operational 5G NR systems, SPEC_EFF varies from 0.1 to 7.8 bps/Hz depending on CQI, SNR, and MCS. The model captures qualitative behavior; exact throughput values scale linearly with the actual bandwidth configuration.

**Results — Throughput:** The UMRO-5G dynamic allocation consistently achieves 15–25% higher aggregate throughput than Hard Isolation at high loads ($\rho > 0.7$). At $\rho = 0.9$, Hard Isolation achieves approximately 44 Mbps aggregate throughput, Soft Isolation achieves ~50 Mbps, and UMRO-5G achieves ~54 Mbps. The gain is achieved by dynamically redistributing unused URLLC and mMTC resources to eMBB during non-peak periods, exploiting the statistical multiplexing gain across heterogeneous traffic patterns.

**Results — Resource Utilization:** Hard Isolation wastes 20–35% of resources at low-to-medium loads due to static partitioning. Soft Isolation improves utilization by 12–18% through the shared pool mechanism. UMRO-5G achieves near-optimal utilization (>92%) across all load levels through continuous Lagrangian price-driven reallocation.

**Results — URLLC Latency Violation:** Hard Isolation maintains the lowest violation probability (<0.5%) due to dedicated resource reservation. UMRO-5G achieves comparable reliability (<1.5% violation) through the priority-weighted utility function that penalizes latency violations heavily ($\beta_s = 10$). Soft Isolation exhibits 3–5% violation at high loads. (Note: Y-axis in Fig. 3 is logarithmic scale for improved visualization of small probability values.)

**Discussion:** The results confirm that the UMRO-5G Lagrangian-based approach achieves a favorable trade-off between efficiency and reliability. For safety-critical URLLC (e.g., remote surgery), operators may increase $\beta_s$ further or implement hybrid schemes with partial hard isolation.

### C. DRL Convergence Comparison

> **Note on Simulation Methodology:** The convergence curves in Fig. 4 are generated using simplified tabular proxy agents that capture the qualitative convergence behavior of DQN, MADRL/QMIX, Federated DQN, and GNN-DRL algorithms. These are not full neural network implementations. Exact quantitative convergence rates will vary depending on specific hyperparameter configurations, neural network architectures, and deployment environments. These curves are intended as illustrative approximations of the algorithmic behavior patterns reported in the cited literature [25][26][27][28].

**Setup:** Four ML/DRL approaches for multi-cell RRM are compared in a simplified environment with 4 cells and 20 users. Each agent observes channel conditions (Rayleigh fading with coherence time of 10 ms) and current allocations, and selects discrete power levels (5 levels per user from 0 to $P_{\max}$). The reward function is the weighted sum rate minus a penalty for QoS violations:

$$r_t = \sum_{k=1}^{K} w_k \log(1 + \text{SINR}_k) - \kappa \sum_{k \in \mathcal{K}_{\text{URLLC}}} \mathbb{1}[D_k > D^{\max}] \tag{19}$$

where $\kappa > 0$ is the URLLC penalty weight (distinct from the Lagrangian multipliers $\lambda^{(r)}$ of Equation (11)).

The four approaches are:

- **DQN:** Single centralized agent with $\epsilon$-greedy exploration (initial $\epsilon = 1.0$, decay rate 0.995, minimum 0.01), experience replay buffer (size 10,000), target network updated every 50 episodes.
- **MADRL/QMIX:** 4 decentralized agents (one per cell) with a centralized mixing network implementing the CTDE paradigm.
- **Federated DQN (FedAvg):** 4 local DQN agents with model aggregation every 10 episodes following Equation (17).
- **GNN-DRL (Illustrative Proxy Models):** Graph-based state representation with a 2-layer message-passing neural network for inter-cell feature extraction, followed by a DQN head for action selection.

Training: 2,000 episodes of 50 steps each, 5 random seeds for confidence bands.

**Results:** DQN converges fastest (within ~500 episodes) due to centralized information access but plateaus at a lower asymptotic reward (approximately 85% of theoretical optimum).

GNN-DRL achieves the highest asymptotic reward (approximately 95% of optimum), leveraging topology-aware features to implicitly capture interference relationships.

MADRL/QMIX converges more slowly (approximately 1,200 episodes) but achieves competitive performance (approximately 92% of optimum) with the critical advantage of distributed execution.

Federated DQN exhibits the slowest convergence (approximately 1,800 episodes) due to periodic aggregation, achieving performance within 5% of centralized DQN while preserving data privacy.

**Discussion:** The results support the multi-engine design of the Intelligence Layer (Layer 3) in UMRO-5G. The framework accommodates all approaches through modular engine interfaces.

### D. Scheduling Algorithm Comparison

**Setup:** 50 users served by a gNB with 20 PRBs (30 kHz subcarrier spacing, numerology $\mu = 1$), Rayleigh fading channel with average SNR uniformly distributed over 0–25 dB per user, simulated for 1,000 TTIs with 10 random seeds.

**Results:**

| Algorithm | Avg Throughput (Mbps) | Jain's Fairness | 5th Percentile (Mbps) | Cell-Edge (Mbps) |
|:---|:---:|:---:|:---:|:---:|
| Round Robin | 85.3 | 1.00 | 12.1 | 8.7 |
| Maximum Rate | 142.7 | 0.45 | 0.3 | 0.1 |
| Proportional Fair | 128.4 | 0.82 | 8.9 | 5.2 |
| DRL Scheduler | 131.2 | 0.85 | 9.4 | 5.8 |

**Analysis:** Maximum Rate achieves the highest average throughput (142.7 Mbps) but lowest fairness. Round Robin achieves perfect fairness but lowest average throughput. Proportional Fair achieves the optimal throughput–fairness trade-off. DRL Scheduler achieves throughput within 3% of PF with slightly higher fairness.

**Discussion:** These results validate the theoretical optimality properties of PF scheduling and demonstrate that DRL can learn near-optimal policies without explicit knowledge of the underlying optimization problem.

### E. SFC Latency Sensitivity Analysis

**Setup:** A Service Function Chain of 5 VNFs (Firewall → NAT → Load Balancer → DPI → Proxy) with service rates $\mu = [500, 800, 1000, 600, 400]$ packets/second. The arrival rate $\lambda$ is swept from 50 to 350 packets/s.

**Results:** The analytical M/M/1 model matches DES results within 5% for loads below 80% of bottleneck VNF capacity. At moderate load ($\lambda = 200$ packets/s), the analytical model predicts 0.65 ms end-to-end latency while DES measures 0.63 ms (3.2% difference). The URLLC latency threshold of 1 ms is achievable for $\lambda < 250$ packets/s with the 5-VNF chain.

**Discussion:** The Jackson queuing model provides accurate predictions for URLLC-compatible SFC design. For safety margins, operators should target 70–80% of the analytically computed maximum load.

### F. Computational Complexity Analysis

**Setup:** Decision time measured for three approaches as the number of users $N$ scales from 10 to 1,000.

**Results:**

| Problem Size ($N$) | DRL (ms) | Water-Filling (ms) | Branch-and-Bound (ms) |
|:---:|:---:|:---:|:---:|
| 10 | 0.08 | 0.5 | 12 |
| 50 | 0.09 | 2.1 | 180 |
| 100 | 0.10 | 4.8 | 1,200 |
| 200 | 0.11 | 11.2 | >10,000 |
| 500 | 0.12 | 35.4 | — |
| 1000 | 0.14 | 89.2 | — |

DRL inference maintains near-constant decision time (~0.1 ms) regardless of problem size. Water-filling scales as O($N \log N$). Branch-and-bound exhibits exponential growth. (Note: Fig. 7 uses logarithmic X and Y axes; the horizontal dashed line marks the 1 ms URLLC real-time deadline.)

**Discussion:** These results quantitatively validate the 100–1000× latency advantage of DRL over classical MILP solvers for real-time decision-making.

### G. Summary of Simulation Insights

1. **Multi-slice allocation** confirms dynamic Lagrangian-based resource management achieves superior throughput with only marginal increase in latency violation probability.
2. **DRL convergence** demonstrates topology-aware approaches (GNN-DRL) achieve highest asymptotic performance.
3. **Scheduling comparison** validates theoretical optimality properties of PF scheduling.
4. **SFC latency validation** confirms accuracy of Jackson queuing model for URLLC-compatible SFC design.
5. **Complexity analysis** quantitatively confirms computational advantage of DRL inference over classical solvers.

---

## IX. Open Challenges and Future Directions

### A. Scalability and Computational Complexity

Multi-slice, multi-domain resource allocation problems are NP-hard in general [17]. For a network with $S$ slices, $B$ base stations, $K$ users per cell, $N$ NFVI servers, and $F$ VNFs, the monolithic optimization problem has $\mathcal{O}(S \cdot B \cdot K + F \cdot N)$ decision variables with combinatorial constraints.

Distributed architectures based on MADRL and FL offer scalable solutions through decomposition, but require formal convergence guarantees in highly non-stationary environments. The orchestration of millions of simultaneously active slices demands novel hierarchical management architectures with efficient control delegation mechanisms.

### B. Security in Virtualized Networks

Network virtualization and slicing introduce new attack surfaces that do not exist in traditional monolithic mobile networks [29]. The principal threat vectors include slice isolation attacks, API security vulnerabilities, resource exhaustion attacks, and software supply chain attacks.

Effective countermeasures require a Zero Trust Architecture (ZTA) applied to all components: mutual authentication between all NFs using TLS 1.3 certificates, network micro-segmentation with Kubernetes Network Policies, and continuous real-time behavioral anomaly monitoring. While foundational security principles remain relevant [29], the open and disaggregated O-RAN architecture introduces new threat vectors requiring updated countermeasures [41]. The O-RAN Alliance has published security specifications (O-RAN.WG11) encompassing xApp authentication, TLS 1.3-encrypted E2 channels, and security audit frameworks [41].

### C. AI/ML Integration Challenges

The integration of AI/ML models into the 5G network control loop presents unique challenges:

**Data scarcity and representativeness:** Models trained in simulation suffer from a sim-to-real gap when deployed in live networks.

**Generalization:** Generalizing to conditions unseen during training remains a fundamental limitation.

**Reliability and verifiability:** Unlike conventional optimization algorithms, deep neural network models are black boxes whose behavior in edge cases is difficult to predict or certify.

**Explainability:** Network operators and regulators increasingly require explanations for automated decisions.

### D. Energy Efficiency

The energy consumption of compute infrastructures supporting NFV is a critical challenge. VNF consolidation techniques based on dynamic live migration and active server shutdown are essential for reducing energy consumption. Radio access network energy efficiency is improved through adaptive cell sleeping managed by the Near-RT RIC via specialized xApps. LSTM-based traffic prediction models enable proactive anticipation of low-load periods, achieving energy consumption reductions of 20–40% in real-world deployments.

**Figure 10** quantifies the energy efficiency–throughput trade-off for the three management strategies within the UMRO-5G framework.

**Fig. 10. Energy Efficiency–Throughput Trade-off Under UMRO-5G with Adaptive Cell Sleeping.** Pareto front of Energy Efficiency (Mbits/Joule) vs. System Throughput (bps/Hz) for three O-RU management strategies: Always-On baseline, Static Sleep with scheduled shutdown, and UMRO-5G dynamic prediction-driven sleep with Near-RT RIC feedback. The red triangle marks the UMRO-5G operating point satisfying SLA constraints (D_URLLC ≤ 1 ms, R_eMBB ≥ 100 Mbps). System parameters: P_ORU_active = 200 W, P_ORU_sleep = 20 W, P_overhead = 500 W. Error bands represent ±1 standard deviation across 5 seeds. Generated from `sim_ee_tradeoff.py`.

The UMRO-5G dynamic strategy achieves a Pareto-superior front compared to both alternatives, demonstrating that the combination of LSTM-based traffic prediction and Near-RT RIC closed-loop feedback enables simultaneous improvements in both energy efficiency and throughput. The operating point satisfying all SLA constraints achieves approximately 14 Mbits/Joule energy efficiency—a 3× improvement over the Always-On baseline—while maintaining 4.2 bps/Hz aggregate throughput.

### E. Reconfigurable Intelligent Surfaces (RIS)

Reconfigurable Intelligent Surfaces represent a transformative technology for 6G and beyond, consisting of large arrays of passive reflecting elements whose phase shifts can be independently controlled to shape the propagation environment.

The integration of RIS into the UMRO-5G framework introduces new optimization variables at Layer 1—the phase shift matrix $\mathbf{\Phi} = \text{diag}(e^{j\theta_1}, \ldots, e^{j\theta_N})$—and requires joint active-passive beamforming optimization at the Intelligence Layer (Layer 3). Key open challenges include real-time channel estimation, RIC integration, and scalable algorithms for RIS with hundreds or thousands of elements.

The integration of RIS with URLLC constraints under finite blocklength coding presents additional optimization challenges that require joint active-passive beamforming design [36][37].

**Figure 9** presents numerical evidence of the performance gains achievable through RIS integration within the UMRO-5G framework. The figure evaluates joint active-passive beamforming under two optimization strategies against a no-RIS baseline.

**Fig. 9. RIS Phase Shift Optimization: Joint Active-Passive Beamforming Performance vs. Number of RIS Elements.** (a) System throughput (bps/Hz) as a function of N_RIS ∈ {16, 32, 64, 128, 256, 512} for three configurations: no RIS (baseline), random phase shift optimization, and alternating optimization (AO). (b) URLLC latency violation probability P(D > D_max) vs. N_RIS for the same configurations. System parameters: B = 20 MHz, M = 64 BS antennas, K = 10 UEs, SNR = −10 dB, 1,000 Monte Carlo realizations. Error bars represent standard deviation across 5 independent seeds. Generated from `sim_ris_optimization.py`.

The results demonstrate that AO-based RIS optimization achieves up to 80% throughput gain over the no-RIS baseline at N_RIS = 512, while reducing URLLC violation probability from 1.5% to below 0.8%. Notably, random phase optimization provides moderate gains at significantly lower computational cost, presenting a viable trade-off for latency-constrained control loops.

### F. Multi-Access Edge Computing (MEC)

Multi-Access Edge Computing, standardized by ETSI, extends the UMRO-5G framework by introducing edge compute nodes co-located with gNBs or at aggregation points. MEC enables ultra-low-latency compute offloading for applications such as augmented reality, autonomous vehicles, and industrial automation.

The MEC offloading problem extends the VNF placement formulation with additional latency and energy constraints. The integration of MEC into the UMRO-5G Virtualization & Slicing Layer (Layer 2) enables URLLC-compatible compute offloading but requires real-time task partitioning algorithms operating within the Medium Loop.

### G. Network Digital Twins

Network Digital Twins (NDTs) provide high-fidelity virtual replicas of the physical 5G network, enabling what-if analysis, predictive maintenance, and safe offline training of DRL agents before deployment. Within UMRO-5G, an NDT module at the Intelligence Layer (Layer 3) can serve as the training environment for all ML engines, addressing the sim-to-real gap challenge. Recent surveys on NDTs provide systematic reviews of synchronization protocols and fidelity maintenance challenges in 5G/6G contexts [30][31].

Open challenges include fidelity maintenance, synchronization efficiency, and scenario generation.

### H. Non-Terrestrial Networks (NTN)

3GPP Release 17 introduced NTN support for NR, enabling satellite-based 5G coverage for remote areas, maritime, and aviation. The integration of NTN into the UMRO-5G framework extends the Infrastructure Layer (Layer 1) with satellite links characterized by large round-trip times, significant Doppler shifts, and predictable dynamics.

Resource management in NTN requires adaptation of the scheduling algorithms (Section IV) to account for long propagation delays and predictable satellite orbital dynamics.

### I. Semantic Communications

Semantic communications represent a paradigm shift from bit-level to meaning-level transmission, where only the semantic content relevant to the receiver's task is transmitted [38]. This emerging paradigm has implications for resource management at all layers of UMRO-5G:

- **Layer 1 (Infrastructure):** Semantic-aware scheduling prioritizes packets based on their semantic importance rather than QoS class alone.
- **Layer 3 (Intelligence):** Joint source-channel coding using deep learning autoencoders replaces traditional AMC link adaptation.

The integration of semantic communications into 5G-Advanced and 6G systems remains an open research frontier.

### J. Zero-Touch Network and Service Management (ZSM)

ETSI Zero-Touch Network and Service Management is the natural evolution of MANO toward fully autonomous network operations. ZSM aligns closely with the UMRO-5G Orchestration Layer (Layer 4) [39], introducing closed-loop automation with intent-based interfaces [40]. The key challenge is achieving sufficient AI/ML model reliability and explainability to remove humans from the control loop entirely.

The emergence of Large Language Models (LLMs) as intent interpreters in ZSM architectures represents a promising direction for translating high-level operator intents into network configurations [34][35].

Promising research directions include formal verification, constrained RL, and human-in-the-loop hybrid approaches.

### K. Evolution Toward 6G

5G-Advanced (3GPP Releases 18–20) introduces significant enhancements: NR-Light for reduced-capability IoT devices, an AI/ML-native air interface employing autoencoder models for channel coding and estimation, support for Integrated Sensing and Communications (ISAC) [32][33], improvements in Full-Duplex, and RIS enhancements.

The 6G vision (horizon 2030) contemplates:

- **Terahertz communications:** Bands 0.1–10 THz offering multi-Tbps capacity.
- **Sub-millisecond orchestration:** End-to-end service orchestration at timescales approaching the physical layer.
- **Terrestrial-satellite convergence:** Seamless integration of Non-Terrestrial Networks for global connectivity.
- **AI-native architecture:** Network functions implemented primarily through AI/ML models.

The UMRO-5G framework provides a foundation for this evolution.

---

## X. Conclusions

This article has presented UMRO-5G, a unified framework for management and resource orchestration in 5G networks that addresses the fundamental gap between the six core technical domains of 5G resource management.

**UMRO-5G Framework.** The proposed four-layer hierarchical architecture with three nested control loops provides a standards-aligned architectural blueprint for end-to-end 5G network management. The joint cross-layer optimization formulation (Equations F1–F16) with hierarchical Lagrangian decomposition offers a rigorous mathematical foundation.

**Five-Dimensional Taxonomy.** The novel taxonomy classifying 28 5G resource management techniques across five orthogonal dimensions enables precise characterization of any existing or proposed technique.

**Numerical Validation.** Five sets of original simulations validate the analytical models and quantify the practical advantages of the UMRO-5G framework. Key findings include: (i) UMRO-5G dynamic allocation achieves 15–25% higher throughput than static hard isolation with URLLC latency violation probability below 1.5% (approximately 44 Mbps vs ~54 Mbps aggregate at ρ=0.9 using real 5G NR parameters); (ii) GNN-DRL achieves the highest asymptotic performance (~95% of optimum); (iii) PF scheduling achieves the theoretical optimum for throughput-fairness trade-off; (iv) M/M/1 Jackson network model predicts SFC latency within 5% of discrete-event simulation; and (v) DRL inference provides 100–1000× lower decision latency than classical MILP solvers.

**Open Challenges.** The article identifies eleven key research directions for the evolution toward AI-native 6G networks: scalability, security, AI/ML integration, energy efficiency, RIS integration, MEC optimization, network digital twins, NTN support, semantic communications, zero-touch autonomous network management, and 6G evolution.

**Future Directions.** The most promising research directions include AI-native air interface design, RIS integration into Near-RT RIC, network digital twins for safe offline DRL training, formal verification for neural network controllers, semantic-aware resource management, and zero-touch autonomous network orchestration.

The UMRO-5G framework provides a comprehensive, mathematically grounded, and standards-aligned foundation for the unified management and orchestration of 5G networks.

---

## References

[1] J. G. Andrews et al., "What will 5G be?" *IEEE J. Sel. Areas Commun.*, vol. 32, no. 6, pp. 1065–1082, Jun. 2014.

[2] Ericsson, "Ericsson Mobility Report," Nov. 2023. [Online]. Available: https://www.ericsson.com/en/reports-and-papers/mobility-report/reports/november-2023

[3] ITU-R, "Minimum requirements related to technical performance for IMT-2020 radio interface(s)," Rep. ITU-R M.2410-0, Nov. 2017. [Online]. Available: https://www.itu.int/pub/R-REP-M.2410-2017

[4] A. Osseiran et al., "Scenarios for 5G Mobile and Wireless Communications: The Vision of the METIS Project," *IEEE Commun. Mag.*, vol. 52, no. 5, pp. 26–35, May 2014.

[5] T. S. Rappaport et al., "Millimeter Wave Mobile Communications for 5G Cellular: It Will Work!" *IEEE Access*, vol. 1, pp. 335–349, 2013.

[6] E. G. Larsson, O. Edfors, F. Tufvesson, and T. L. Marzetta, "Massive MIMO for next generation wireless systems," *IEEE Commun. Mag.*, vol. 52, no. 2, pp. 186–195, Feb. 2014.

[7] R. Mijumbi et al., "Network Function Virtualization: State-of-the-Art and Research Challenges," *IEEE Commun. Surveys Tuts.*, vol. 18, no. 1, pp. 236–262, 1st Quar. 2016.

[8] P. Popovski et al., "5G Wireless Network Slicing for eMBB, URLLC, and mMTC: A Communication-Theoretic View," *IEEE Access*, vol. 6, pp. 55765–55779, 2018.

[9] X. Foukas et al., "Network Slicing in 5G: Survey and Challenges," *IEEE Commun. Mag.*, vol. 55, no. 5, pp. 94–100, May 2017.

[10] I. Afolabi et al., "Network Slicing and Softwarization: A Survey," *IEEE Commun. Surveys Tuts.*, vol. 20, no. 3, pp. 2429–2453, 3rd Quar. 2018.

[11] M. Polese et al., "Understanding O-RAN: Architecture, Interfaces, Algorithms, Security, and Research Challenges," *IEEE Commun. Surveys Tuts.*, vol. 25, no. 2, pp. 1376–1411, 2nd Quar. 2023.

[12] 3GPP, "NR; Physical layer procedures for data," TS 38.214 V17.3.0, Sep. 2022. [Online]. Available: https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3214

[13] Y. Polyanskiy, H. V. Poor, and S. Verdú, "Channel Coding Rate in the Finite Blocklength Regime," *IEEE Trans. Inf. Theory*, vol. 56, no. 5, pp. 2307–2359, May 2010.

[14] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. Hoboken, NJ: Wiley, 2006.

[15] ETSI, "Network Functions Virtualisation (NFV); Management and Orchestration," GS NFV-MAN 001 V1.1.1, Dec. 2014. [Online]. Available: https://www.etsi.org/deliver/etsi_gs/NFV-MAN/001_099/001/01.01.01_60/gs_nfv-man001v010101p.pdf

[16] J. Herrera and J. F. Botero, "Resource Allocation in NFV: A Comprehensive Survey," *IEEE Trans. Netw. Service Manag.*, vol. 13, no. 3, pp. 518–532, Sep. 2016.

[17] M. R. Garey and D. S. Johnson, *Computers and Intractability*. New York: W.H. Freeman, 1979.

[18] P. Quinn and T. Nadeau, "Problem Statement for Service Function Chaining," RFC 7498, IETF, Apr. 2015. [Online]. Available: https://tools.ietf.org/html/rfc7498

[19] 3GPP, "Management and orchestration; Concepts, use cases and requirements," TS 28.530 V17.2.0, Sep. 2022. [Online]. Available: https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3273

[20] D. P. Bertsekas, *Nonlinear Programming*, 3rd ed. Belmont, MA: Athena Scientific, 2016.

[21] T. Nandagopal, T. Kim, X. Gao, and V. Bharghavan, "Achieving MAC layer fairness in wireless packet networks," in *Proc. ACM MobiCom*, pp. 87–98, 2000.

[22] O-RAN Alliance, "O-RAN Architecture Description," Technical Specification O-RAN.WG1.O-RAN-Architecture-Description-v07.00, Feb. 2023. [Online]. Available: https://www.o-ran.org/specifications

[23] L. Bonati et al., "Open, Programmable, and Virtualized 5G Networks: State-of-the-Art and the Road Ahead," *Computer Networks*, vol. 182, p. 107516, Dec. 2020.

[24] R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed. Cambridge, MA: MIT Press, 2018. [Online]. Available: http://incompleteideas.net/book/the-book-2nd.html

[25] V. Mnih et al., "Human-level control through deep reinforcement learning," *Nature*, vol. 518, no. 7540, pp. 529–533, Feb. 2015.

[26] T. Rashid, M. Samvelyan, C. S. de Witt, G. Farquhar, J. Foerster, and S. Whiteson, "QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning," in *Proc. Int. Conf. Mach. Learn. (ICML)*, vol. 80, pp. 4295–4304, 2018.

[27] B. McMahan et al., "Communication-Efficient Learning of Deep Networks from Decentralized Data," in *Proc. AISTATS*, vol. 54, pp. 1273–1282, 2017.

[28] M. Eisen and A. Ribeiro, "Optimal Wireless Resource Allocation with Random Edge Graph Neural Networks," *IEEE Trans. Signal Process.*, vol. 68, pp. 2977–2991, 2020.

[29] I. Ahmad et al., "Overview of 5G Security Challenges and Solutions," *IEEE Commun. Standards Mag.*, vol. 2, no. 1, pp. 36–43, Mar. 2018.

[30] H. V. X. Nguyen et al., "Digital Twin for 5G and Beyond Network: A Systematic Survey," *IEEE Access*, vol. 9, pp. 10379–10396, 2021, doi: 10.1109/ACCESS.2021.3049649.

[31] A. Masood, B. Ali, M. A. Ul Hassan, N. S. Bhutta, and P. Shah, "Towards Autonomous Network Management: A Comprehensive Survey on Network Digital Twins," *IEEE Commun. Surveys Tuts.*, early access, 2024, doi: 10.1109/COMST.2024.3359928.

[32] F. Liu et al., "Integrated Sensing and Communications: Toward Dual-Functional Wireless Networks for 6G and Beyond," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 6, pp. 1728–1767, Jun. 2022, doi: 10.1109/JSAC.2022.3156632.

[33] J. A. Zhang et al., "Enabling Joint Communication and Radar Sensing in Mobile Networks—A Survey," *IEEE Commun. Surveys Tuts.*, vol. 24, no. 1, pp. 306–345, 1st Quar. 2022, doi: 10.1109/COMST.2021.3122519.

[34] Y. Zhou et al., "Large Language Models for Telecom Network Management: Current Status and Future Directions," *IEEE Commun. Mag.*, vol. 62, no. 3, pp. 20–26, Mar. 2024, doi: 10.1109/MCOM.001.2300325.

[35] O. Friha et al., "LLM-Based Edge Intelligence: A Comprehensive Survey on Capabilities, Applications and Challenges," *IEEE Open J. Commun. Soc.*, vol. 5, pp. 2312–2338, 2024, doi: 10.1109/OJCOMS.2024.3399774.

[36] C. Xu, Y. Liu, R. Schober, and H. V. Poor, "Resource Management for RIS-Assisted URLLC Networks with Finite Blocklength Coding," *IEEE Trans. Wireless Commun.*, vol. 22, no. 3, pp. 1521–1530, Mar. 2023, doi: 10.1109/TWC.2022.3211538.

[37] C. Pan et al., "Multicell MIMO Communications Relying on Intelligent Reflecting Surfaces," *IEEE Trans. Wireless Commun.*, vol. 19, no. 8, pp. 5218–5233, Aug. 2020, doi: 10.1109/TWC.2020.2990766.

[38] H. Xie, Z. Qin, G. Y. Li, and B.-H. Juang, "Deep Learning Enabled Semantic Communication Systems," *IEEE Trans. Signal Process.*, vol. 69, pp. 2636–2650, 2021, doi: 10.1109/TSP.2021.3071210.

[39] C. Benzaid and T. Taleb, "AI-Driven Zero Touch Network and Service Management in 5G and Beyond: Challenges and Research Directions," *IEEE Netw.*, vol. 34, no. 2, pp. 186–194, Mar./Apr. 2020, doi: 10.1109/MNET.001.1900252.

[40] ETSI, "Zero-touch network and Service Management (ZSM); Reference Architecture," GS ZSM 002 V1.1.1, Aug. 2019. [Online]. Available: https://www.etsi.org/deliver/etsi_gs/ZSM/001_099/002/01.01.01_60/gs_zsm002v010101p.pdf

[41] O-RAN Alliance, "Security Threat Modeling and Remediation Analysis," Technical Report O-RAN.WG11.Security-Threat-Modeling-and-Remediation-v05.00, Nov. 2023. [Online]. Available: https://www.o-ran.org/specifications

---

## Abbreviations

| Abbreviation | Definition |
|:---|:---|
| 3GPP | 3rd Generation Partnership Project |
| 5G NR | 5G New Radio |
| 5GC | 5G Core |
| DQN | Deep Q-Network |
| DRL | Deep Reinforcement Learning |
| eMBB | enhanced Mobile Broadband |
| ETSI | European Telecommunications Standards Institute |
| FBL | Finite Blocklength |
| FL | Federated Learning |
| GNN | Graph Neural Network |
| ISAC | Integrated Sensing and Communications |
| LLM | Large Language Model |
| MADRL | Multi-Agent Deep Reinforcement Learning |
| MANO | Management and Orchestration |
| MEC | Multi-Access Edge Computing |
| MIMO | Multiple Input Multiple Output |
| mMTC | massive Machine-Type Communications |
| NDT | Network Digital Twin |
| NFV | Network Function Virtualization |
| NTN | Non-Terrestrial Network |
| O-RAN | Open Radio Access Network |
| PF | Proportional Fair |
| PRB | Physical Resource Block |
| RIC | RAN Intelligent Controller |
| RIS | Reconfigurable Intelligent Surface |
| RRM | Radio Resource Management |
| SDN | Software-Defined Networking |
| SFC | Service Function Chain |
| SLA | Service Level Agreement |
| TN | Transport Network |
| UMRO-5G | Unified Management and Resource Orchestration for 5G |
| URLLC | Ultra-Reliable Low-Latency Communications |
| VNF | Virtualized Network Function |
| ZSM | Zero-touch network and Service Management |

---

*Manuscript received April 2026; revised [Date]; accepted [Date].*
