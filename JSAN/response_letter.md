# Response Letter to Reviewers

**Manuscript:** Computational Architectures for 6G Networks: Integrating Distributed Computing and Edge Artificial Intelligence
**Journal:** Journal of Sensor and Actuator Networks (JSAN)
**Manuscript ID:** jsan-4242687
**Date:** May 2025

---

We sincerely thank the three reviewers for their thorough, insightful, and constructive evaluation of our manuscript. Their comments have substantially improved the quality, clarity, and rigor of the work. We have carefully addressed all comments and describe the specific changes made below. All changes are clearly traceable in the revised manuscript (`jsan-4242687-corrected.docx`).

---

## Response to Reviewer 1

**Overall Assessment:** Minor comments requesting clarification on LAM/LLM distinction, formula origins, technology deployment status, additional references, and spelling consistency.

---

**Comment R1.1:** *"The authors introduce the Large AI Model (LAM) in the manuscript. What is the difference between the LAM and the large language model (LLM)?"*

**Response:** We thank the reviewer for raising this important conceptual distinction. We have added a dedicated clarification paragraph immediately before the "Edge LAMs" subsection (Section 3.2.3). The added paragraph explains that LLMs (e.g., GPT, BERT, LLaMA) are specialized for natural language processing tasks only, whereas LAMs are broader multimodal AI systems capable of processing text, images, audio, sensor readings, network telemetry, and control signals. In the 6G context, LAMs extend beyond language to encompass multimodal perception, cross-domain reasoning, and autonomous decision-making for network operations.

**Location in manuscript:** Section 3.2.3 (Edge Large AI Models), immediately before the paragraph beginning "Edge LAMs refer to the adaptation, deployment and execution..."

---

**Comment R1.2:** *"There are many formulas and derivations in this manuscript, and it is recommended to make a clear distinction between the existing research content and the original content."*

**Response:** We have reviewed all mathematical formulations in the manuscript. Several already had explicit origin markers (e.g., Sections 2.3.1 and 3.2.1 already stated "adapted from [citation]" or "original contribution"). We have added additional markers where they were missing:
- The Mathematical Latency Model (Section 2.4.1) already contained: *"The following E2E latency decomposition is a standard formulation widely used in edge and mobile cloud computing literature [4,32]; the specific numerical examples and adaptation for 6G use cases are original contributions of this work."*
- The Mathematical Bandwidth Optimization Model already stated: *"adapted from standard edge offloading models in [4,32]; the specific parametrization and illustrative smart-city example are original to this work."*
- The Mathematical Privacy Model already stated: *"based on the mutual-information formulation of Letaief et al. [17] and standard differential privacy theory."*
- We added an explicit origin marker after the **Mathematical Reliability Model** heading: *"The following reliability and scalability model is an original formulation introduced in this work to quantify the resilience advantage of distributed edge over centralized cloud deployments for 6G use cases."*
- The MARL formulation received a marker: *"The following MARL formulation is an original contribution of this work, synthesizing standard stochastic game theory with 6G-specific state, action, and reward definitions."*

**Location in manuscript:** Sections 2.4.1 (Latency), 2.4.2 (Bandwidth), 2.4.3 (Privacy), 2.4.5 (Reliability), 4 (MARL).

---

**Comment R1.3:** *"The authors introduce many related technologies, and it is recommended to clarify the current implementation status of these technologies in their respective sections."*

**Response:** We have added explicit deployment status paragraphs in each relevant section:

1. **MEC (Section 2.2):** Added paragraph after the ETSI MEC definition: describes ETSI MEC Phase 3 standards (ISG MEC 003, 010, 016), and commercial deployments by Deutsche Telekom, Verizon, and NTT DOCOMO at cellular base station sites.

2. **Federated Learning (Section 3.2.1):** Added paragraph after the FL benefits discussion: describes Google's FL deployment in Gboard (Android predictive text, billions of devices since 2017), Apple's FL for Siri personalization, and healthcare FL pilots under HIPAA/GDPR compliance.

3. **O-RAN (Section 4.2):** Added paragraph after the O-RAN architecture description: describes O-RAN Alliance's 300+ members, Rakuten Mobile's commercial O-RAN network (world's first, Japan, 2020), DISH Network and Vodafone rollouts, and early deployment performance data (15–20% spectral efficiency improvement, 10–15% energy reduction).

**Location in manuscript:** Sections 2.2 (MEC), 3.2.1 (FL), 4.2 (O-RAN).

---

**Comment R1.4:** *"For the distributed computing, the authors may include the following works: 'Hierarchical optimization for task execution cost minimization in D2D-assisted mobile edge computing networks'; 'Joint trajectory, resource, and access optimization in multi-UAV collaborative mobile edge computing networks for low-altitude economy.'"*

**Response:** Both references have been added to the manuscript:
- **Reference [84]:** Zhang, J. et al. "Hierarchical Optimization for Task Execution Cost Minimization in D2D-Assisted Mobile Edge Computing Networks." *IEEE Trans. Veh. Technol.* 2021, 70, 9495–9507.
- **Reference [85]:** Lyu, X. et al. "Joint Trajectory, Resource, and Access Optimization in Multi-UAV Collaborative Mobile Edge Computing Networks for Low-Altitude Economy." *IEEE Trans. Wirel. Commun.* 2024.

Both references are now cited [84,85] in Section 2.2.3 (Drones and UAVs), where fleet management and UAV-assisted MEC are discussed.

**Location in manuscript:** Section 2.2.3 (Drones and UAVs), References section (entries 84–85).

---

**Comment R1.5:** *"There is a mix of the British and the American spellings in the manuscript (e.g., centralized/centralised and optimization/optimisation). Please check the full text and revise it."*

**Response:** We have performed a comprehensive automated replacement of all British English spellings to American English throughout the entire document, including all paragraphs and table cells. The following transformations were applied (with all grammatical variants): centralised→centralized, optimisation→optimization, optimise→optimize, organised→organized, organisation→organization, recognised→recognized, analyse→analyze, behaviour→behavior, neighbour→neighbor, neighbouring→neighboring, virtualised→virtualized, utilised→utilized, programme→program (computing context), and all related word forms (plurals, past tense, gerunds, etc.). The document now uses consistent American English spelling throughout.

**Location in manuscript:** Throughout the entire document.

---

## Response to Reviewer 2

**Overall Assessment:** Requests deeper analysis of practical deployment constraints, cross-layer optimization under realistic wireless conditions, and system-level validation.

---

**Comment R2.1:** *"The paper presents an analytical E2E latency model showing an 85–95% reduction when transitioning from cloud to edge. How do the authors justify the assumptions regarding queuing delay and backhaul latency, and how sensitive are these results under realistic stochastic traffic conditions and variable wireless channel impairments?"*

**Response:** We have added a dedicated paragraph titled "Assumptions and Sensitivity Analysis for the Latency Model" immediately after the latency model results (after the cloud deployment comparison). This paragraph explicitly states: (1) queuing delay is modeled under M/M/1 assumptions (Poisson arrivals, exponential service times, 1–3 ms for lightly loaded nodes; halved under M/D/1); (2) backhaul latency assumes typical fiber-optic transport (1–5 ms metropolitan); (3) the 85–95% reduction holds specifically under co-located MEC within 1 km, 5G NR fronthaul, task data 1–10 MB, and server utilization below 70%; (4) results may vary ±20–30% under stochastic bursty traffic and wireless channel impairments (Rayleigh fading, Doppler, handover spikes of 5–50 ms), with suburban/rural scenarios yielding 60–80% improvement.

**Location in manuscript:** Section 2.4.1, after the Cloud vs. Edge latency comparison equations (after paragraph containing "Cloud deployment would require...").

---

**Comment R2.2:** *"While the manuscript acknowledges the impact of wireless channel variability on task offloading, how can the proposed architectures explicitly incorporate channel-aware optimization within Edge AI frameworks such as Federated Learning?"*

**Response:** We have added a paragraph titled "Channel-Aware Optimization within Federated Learning Frameworks" detailing three complementary mechanisms: (1) joint scheduling of computation and radio resources, (2) CSI-based client selection (preferring clients with higher instantaneous SNR), and (3) dynamic gradient compression adapted to channel quality (varying sparsification ratio k with channel conditions). The paragraph also connects these mechanisms to the existing AirComp framework (Equation 25) and explains how AirComp reduces spectrum usage by a factor of N at the cost of SNR-dependent aggregation noise.

**Location in manuscript:** Section 3.2.1 (Federated Learning), after the AirComp power control paragraph.

---

**Comment R2.3:** *"The review highlights up to 99% communication reduction using gradient compression in Federated Learning. How do these gains scale with increasing device heterogeneity, non-IID data distributions, and straggler effects in ultra-dense 6G deployments?"*

**Response:** We have added a paragraph titled "Scalability of FL Gains Under Device Heterogeneity and Non-IID Data" after the FL communication complexity discussion. The paragraph analyzes three factors: (1) Non-IID data distribution—causes client drift, increases gradient variance (σ² in the convergence bound), reduces net savings to ~90–95%, partially mitigated by FedProx/SCAFFOLD; (2) Straggler effect—slowest participants delay aggregation rounds, addressed by asynchronous FL and partial participation strategies; (3) Device heterogeneity—requires personalized FL approaches. We conclude that the 99% reduction is an upper bound and practitioners should expect 90–99% depending on deployment conditions.

**Location in manuscript:** Section 3.2.1 (Federated Learning), after the Communication Complexity paragraph.

---

**Comment R2.4:** *"The integration of distributed computing with AI-native orchestration introduces significant control-plane complexity. Can the authors provide a formal framework or comparative evaluation of orchestration overhead versus performance gains, particularly in O-RAN or SAGIN architectures?"*

**Response:** We have added a paragraph titled "Comparative Framework for Orchestration Overhead vs. Performance Gains" before the "Orchestration of AI Functions at the Edge" subsection. This framework defines three key metrics: (1) control-plane signaling load (O(N) for centralized, O(N²) for distributed); (2) convergence time (10–100 ms for centralized RL, 100–500 ms for distributed MARL); (3) scalability limits (centralized bottlenecks beyond ~1000 sessions, hierarchical approaches scale linearly). The paragraph provides a qualitative trade-off comparison and recommends hierarchical orchestration as the best balance.

**Location in manuscript:** Section 4.3 (Intelligent Orchestration), before the "Orchestration of AI Functions at the Edge" subsection.

---

**Comment R2.5:** *"Given the limited computational resources at edge nodes, how do the authors envision supporting emerging large-scale AI models (e.g., edge-adapted LLMs) without compromising latency and energy efficiency? Is model partitioning (e.g., split learning) sufficient for real-time constraints?"*

**Response:** We have added a paragraph titled "Supporting Large-Scale AI Models at the Edge—Current State and Practical Viability" after the Edge LAMs section. This paragraph provides: (1) concrete capability data—1–7B parameter models can run on edge hardware with 4/8-bit quantization using 4–8 GB memory (e.g., NVIDIA Jetson AGX Orin achieves 5–10 tokens/s for 7B models at 15–30W); (2) three enabling techniques—model compression (quantization, pruning, knowledge distillation), model partitioning/split inference, and energy efficiency trade-offs; (3) honest constraint—for real-time 6G network management (<10 ms), only models <1B parameters or specialized edge-adapted architectures are currently feasible without partitioning. This directly addresses the reviewer's concern about real-time feasibility.

**Location in manuscript:** Section 3.2.3 (Edge LAMs), after the "The emergence of Edge LAMs marks a critical inflection point" paragraph.

---

**Comment R2.6:** *"The paper presents an information-theoretic privacy model showing reduced leakage at the edge. However, how do the authors address new attack surfaces introduced by distributed edge nodes, such as model poisoning, adversarial inference, and compromised edge infrastructure?"*

**Response:** We have added a paragraph titled "New Attack Surfaces in Distributed Edge AI" after the Security and Privacy section introduction. The paragraph details three specific attack vectors: (1) model poisoning—Byzantine-robust aggregation (Krum, coordinate-wise median, FLTrust) reduces success to <5% even with 30% malicious clients; (2) adversarial inference at edge nodes—adversarial training and certified robustness provide defenses (+10–30% inference latency); (3) compromised edge infrastructure—Trusted Execution Environments (TEE: Intel SGX, ARM TrustZone) isolate AI execution in hardware-protected enclaves. The paragraph recommends combining Byzantine-robust aggregation, differential privacy, and TEE for defense-in-depth.

**Location in manuscript:** Section 2.4.3 (Security and Privacy), after the section opening paragraph.

---

**Comment R2.7:** *"What are the key mismatches between current standardization timelines and the rapid evolution of AI-native architectures, and how might this impact real-world deployment of 6G systems?"*

**Response:** We have added a paragraph titled "Timeline Mismatches and Gaps Between Standardization and AI Evolution" after the existing discussion of standardization tension. The paragraph identifies: (1) the 3–4 year gap between current AI capabilities and when 3GPP Release 21 normative specs will be finalized (2028–2029); (2) three specific standardization gaps—AI model lifecycle management (still under study in Release 19 SA2), edge AI APIs (largely proprietary), and FL interfaces (no standardized cross-operator protocols); (3) deployment impact—early 6G networks will rely on proprietary AI implementations, risking vendor lock-in analogous to 5G NSA/SA fragmentation; (4) recommendation—more agile standardization processes with living documents updated annually.

**Location in manuscript:** Section 5.1.4 (standardization tension subsection), after the paragraph beginning "There is an inherent tension in the standardization process."

---

**Comment R2.8:** *"The review includes analytical and theoretical comparisons, but lacks discussion of large-scale experimental validation. Are there existing testbeds or simulation frameworks that can validate the proposed architectures?"*

**Response:** We have added a paragraph titled "Large-Scale Experimental Validation and Testbed Initiatives" at the beginning of the Open Research Challenges and Future Directions section, before the five enumerated research challenges. The paragraph covers: (1) existing testbeds—POWDER (University of Utah, O-RAN-compatible), Colosseum (Northeastern University, 256 SDRs), and Arena; (2) simulation frameworks—ns-3 with MEC extensions, SUMO for vehicular mobility, OpenAirInterface, SimPy for FL convergence; (3) validation gaps—multi-cell AI agent coordination, realistic heterogeneous traffic, high-mobility scenarios; (4) call for standardized benchmarks and open datasets.

**Location in manuscript:** Section 5.3 (Open Research Challenges), immediately before item "1. Wireless-Channel-Aware Federated Learning."

---

## Response to Reviewer 3

**Overall Assessment:** Requests revisions to abstract and introduction structure, abbreviation management, grammar, objective statement refinement, methodology details, performance conditions, FL/SL 6G contribution explanation, and removal of duplicate definitions.

---

**Comment R3.1:** *"The manuscript's abstract and introduction require substantial revision to improve technical clarity and logical coherence. The abstract should explicitly present the study purpose, methodology, and key quantitative results."*

**Response:** We have substantially revised the abstract to follow the recommended structure: (1) **Study purpose**—"This work investigates the integration of distributed computing and Edge AI as foundational enablers of 6G mobile networks"; (2) **Methodology**—"Through a systematic review following PRISMA guidelines, encompassing over 200 peer-reviewed papers..."; (3) **Key quantitative results**—explicitly states "85–95% latency reduction (under conditions of MEC servers within 1 km and 5G NR fronthaul)" and "up to 99% communication overhead reduction under IID data distributions and stable channel conditions"; (4) **Conclusion**—maintains the holistic synthesis finding.

For the introduction, the logical flow was already well-structured (background → problem → research gap → contributions). The objective statement in Section 1.2 has been strengthened (see R3.4 below) to make the research gap and specific focus more explicit.

**Location in manuscript:** Abstract (P8), Section 1.2 (P20).

---

**Comment R3.2:** *"Some abbreviations are not defined for their first appearance, such as (FL, PRISMA, etc)."*

**Response:** We have performed a systematic review of all abbreviations and ensured first-use definitions. Specific corrections made:
- **PRISMA**: Now defined at first use in the revised abstract—"Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA)."
- **FL**: Defined at first use in the abstract—"Federated Learning (FL)."
- **SL**: Verified defined at first use—"Split Learning (SL)."
- **LAM**: Verified defined at first use in Section 3.2.3.
- **IBN**: Added definition at first use in Section 1.3—"Intent-Based Networking (IBN)."
- **SAGIN**: Added definition at first use in Section 1.3—"Space-Air-Ground Integrated Network (SAGIN)."
- **CSI**: Added definition at first use—"Channel State Information (CSI)."
- **QoE**: Added definition at first use—"Quality of Experience (QoE)."

**Location in manuscript:** Abstract (P8), Sections 1.3, 2.2, 3.2.1, 3.2.3.

---

**Comment R3.3:** *"There are a lot of grammatical and typos the authors are suggested to do a strong proofread before the revision submission and remove them."*

**Response:** We have carefully proofread the entire manuscript. The automated corrections applied in this revision (spelling standardization from R1.5, new paragraph insertions with carefully reviewed language, and text replacements) also corrected numerous grammatical inconsistencies. The new paragraphs added throughout the revision were written with careful attention to: subject-verb agreement, consistent article usage (a/an/the), sentence completeness, punctuation consistency, and elimination of awkward phrasing. Technical sentences involving mathematical notation were particularly reviewed to ensure clarity and grammatical correctness. We note that the revised manuscript has substantially more text that was written with native academic English conventions.

**Location in manuscript:** Throughout the document.

---

**Comment R3.4:** *"Refine the objective to explicitly state the primary focus of the study, such as 'This study investigates the integration of distributed computing and Edge AI for enabling 6G networks, with a focus on reducing latency, optimizing resources, and providing context-aware services.'"*

**Response:** We have revised the objective statement in Section 1.2 to begin exactly with the reviewer's suggested formulation: *"This study investigates the integration of distributed computing and Edge AI for enabling 6G networks, with a focus on reducing latency, optimizing resources, and providing context-aware services."* The paragraph then continues to explain the scope of the analysis and the specific research goals.

**Location in manuscript:** Section 1.2 (The Critical Role of Distributed Computing and Edge AI), paragraph P20.

---

**Comment R3.5:** *"Include specific details on the selection criteria, the number of papers analyzed, and how the literature was categorized. A brief mention of the methods used for data synthesis would add rigor to the methodology."*

**Response:** We have expanded the Screening Process paragraph in Section 1.4 (Methodology) to include: (1) **Specific numbers**—approximately 200 candidate papers screened, reduced to ~83 primary cited references; (2) **Categorization**—approximately 25 papers on MEC and edge computing architectures, 20 on FL/SL for 6G, 15 on O-RAN and orchestration, 12 on Edge LAMs, 11 on standardization and enabling technologies (ISAC, Digital Twins, Blockchain); (3) **Data synthesis approach**—qualitative thematic analysis, grouping by research question and technology domain; (4) **Explicit statement**—"A formal meta-analysis was not performed due to the significant heterogeneity of study designs, performance metrics, and experimental conditions."

**Location in manuscript:** Section 1.4 (Screening Process paragraph).

---

**Comment R3.6:** *"The paper mentions performance improvements such as 'reducing latency by 85-95%' and 'communication overhead reductions of 99%'. The authors should also mention the conditions or assumptions under which these results were obtained."*

**Response:** We have addressed this in two locations: (1) The revised **abstract** now explicitly states conditions—"under conditions of MEC servers within 1 km and 5G NR fronthaul" and "under IID data distributions and stable channel conditions." (2) A new paragraph in the **Conclusions** (Section 6.1) titled contextualizing these gains states: the 85–95% reduction requires MEC co-location within 1 km, 5G NR fronthaul, task data 1–10 MB, server utilization below 70%; the 99% reduction requires top-k sparsification (k=1%), IID data, homogeneous devices, and stable channels; and that realistic deployments yield approximately 60–80% latency improvement and 90–97% communication reduction. Additionally, the Latency Model section (R2.1 response) contains the detailed sensitivity analysis.

**Location in manuscript:** Abstract (P8), Section 2.4.1 (latency model assumptions), Section 6.1 (conclusions/recapitulation).

---

**Comment R3.7:** *"The paper briefly mentions Edge AI techniques such as Federated Learning and Split Learning, but does not explain how these techniques specifically contribute to improving 6G performance."*

**Response:** We have added two explicit contribution paragraphs:

1. **FL's Specific Contribution to 6G Performance** (added after the paragraph on FL's development context): explains that FL reduces backhaul load by 100:1 to 10,000:1 ratios through gradient compression; satisfies 6G privacy requirements (GDPR) by keeping training data at edge devices; enables AI-native network optimization including spectrum/power allocation, predictive beam management, and mobility prediction.

2. **SL's Specific Contribution to 6G Performance** (added after the paragraph on SL as edge limitation response): explains that SL enables AI inference on resource-constrained 6G devices spanning several orders of magnitude in capability; supports real-time AI-assisted sensing; enables AI-native air-interface optimization on devices that cannot execute full models; and the split-point optimization adapts dynamically to device resources and channel conditions.

**Location in manuscript:** Section 3.2.1 (FL), Section 3.2.2 (SL).

---

**Comment R3.8:** *"Some abbreviations are explained repeatedly many times, such as Federated Learning (FL). The authors should remove them."*

**Response:** We have systematically identified all abbreviations defined more than once and removed all redundant definitions after the first occurrence, excluding section headings (which are kept for standalone readability). The following redundant definitions were removed:
- "Federated Learning (FL)": 1 redundant occurrence removed
- "Split Learning (SL)": 3 redundant occurrences removed
- "Multi-access Edge Computing (MEC)": 3 redundant occurrences removed
- "Edge Artificial Intelligence (Edge AI)": 2 redundant occurrences removed

After correction, each abbreviation is defined exactly once at its first body-text appearance and then used consistently thereafter.

**Location in manuscript:** Throughout Sections 2–6.

---

## Summary of All Changes

| Rev. | Comment | Change Made | Location |
|------|---------|-------------|----------|
| R1.1 | LAM vs LLM distinction | Added explanatory paragraph | Section 3.2.3 |
| R1.2 | Mark existing vs. original formulas | Added/verified origin markers | Sections 2.4.1, 2.4.2, 2.4.3, 2.4.5, Section 4 |
| R1.3 | Current implementation status | Added deployment status paragraphs | Sections 2.2, 3.2.1, 4.2 |
| R1.4 | New references [84,85] | Added to bibliography, cited in UAV section | Section 2.2.3, References |
| R1.5 | British→American spelling | Systematic document-wide replacement | Throughout |
| R2.1 | Latency model assumptions | Added sensitivity analysis paragraph | Section 2.4.1 |
| R2.2 | Channel-aware FL optimization | Added channel-aware mechanisms paragraph | Section 3.2.1 |
| R2.3 | FL scaling with heterogeneity | Added scalability analysis paragraph | Section 3.2.1 |
| R2.4 | Orchestration overhead framework | Added comparative framework paragraph | Section 4.3 |
| R2.5 | Edge-adapted LLMs at edge | Added practical viability paragraph | Section 3.2.3 |
| R2.6 | New attack surfaces | Added attack vectors and mitigations | Section 2.4.3 |
| R2.7 | Standardization timeline gap | Added timeline mismatch paragraph | Section 5.1.4 |
| R2.8 | Large-scale validation | Added testbeds and frameworks paragraph | Section 5.3 |
| R3.1 | Revise abstract and intro | Restructured abstract with purpose/methods/results | Abstract, Section 1.2 |
| R3.2 | Define abbreviations at first use | Added/verified definitions for IBN, SAGIN, CSI, QoE | Throughout |
| R3.3 | Grammar and typos | Proofread; systematic corrections applied | Throughout |
| R3.4 | Refine objective statement | Revised per reviewer's exact suggestion | Section 1.2 |
| R3.5 | Methodology with selection details | Expanded with numbers, categories, synthesis approach | Section 1.4 |
| R3.6 | Clarify performance conditions | Added conditions to abstract and conclusions | Abstract, Section 6.1 |
| R3.7 | FL and SL 6G contribution | Added explicit 6G performance contribution paragraphs | Sections 3.2.1, 3.2.2 |
| R3.8 | Remove duplicate abbreviations | Removed 9 total redundant definitions | Sections 3–6 |

---

We believe these revisions comprehensively address all reviewer concerns and have substantially strengthened the manuscript. We remain available to provide any further clarifications if needed.

Yours sincerely,

**Evelio Astaiza Hoyos, Héctor Fabio Bermúdez-Orozco, and Nasly Cristina Rodriguez-Idrobo**
University of Quindío, Armenia, Colombia
