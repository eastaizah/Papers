# Response Letter to Editor

## Dear Editor,

Thank you for your thorough and constructive editorial review of our manuscript, **"Computational Architectures for 6G Networks: Integrating Distributed Computing and Edge Artificial Intelligence."** We appreciate the detailed point-by-point corrections. In response, we performed a manuscript-wide audit focused on: (i) unsupported factual statements and numerical values, (ii) unclear provenance of mathematical formulations, (iii) insufficiently specific or weakly aligned references, (iv) figure quality and labeling issues, and (v) minor formatting inconsistencies.

Across the revised manuscript, we have added or replaced references where needed, clarified when a formulation is synthesized by the authors versus directly adopted from prior work, added derivation/assumption text for illustrative numerical examples, corrected arithmetic and notation where necessary, revised the affected figures, and fixed the noted formatting issues. Below we provide a detailed point-by-point response.

## Point-by-Point Responses

### General Concern: Unsupported Statements and Values

We fully agree with the editor’s overarching concern. In the revised manuscript, we conducted a systematic verification of all quantitative claims, factual statements, and reference attributions, especially in the sections highlighted in the editorial note. Where a cited source did not explicitly support the stated value, we either replaced it with a more appropriate reference, added clarifying derivation text, qualified the statement as an estimate/illustrative scenario, or removed over-precise wording. We also clarified the status of survey-style equations and unified formulations so that readers can clearly distinguish literature-based models from manuscript-specific analytical adaptations.

**Location in corrected article:** Throughout the manuscript, with major revisions in paragraphs L78-L132, L149-L186, L237, L278-L312, L359-L423, L434-L478, L556-L642, L788-L837, and L851-L874.

### Specific Corrections

#### 1. Statements requiring references

**Editor Comment (Line 320):** The statement on Deutsche Telekom, Verizon, and NTT DOCOMO MEC deployments required an explicit supporting reference.
**Response:** We added direct supporting references for the cited operator deployments and clarified that these are representative examples of operator-led MEC implementation rather than a universal claim. The wording was tightened so that the use cases listed are aligned with the cited deployment reports.
**Location in corrected article:** Section “Multi-access Edge Computing (MEC) as a Key Enabler in 6G,” paragraph L78 (approx. manuscript line 320).

---

**Editor Comment (Line 362):** The value “up to 1000 km/h for 6G [8]” was not clearly traceable in the cited source.
**Response:** We revised this sentence by adding a source that explicitly discusses extreme high-mobility design targets and clarified that the value refers to a target operating scenario rather than a generic measured deployment condition.
**Location in corrected article:** Section “Multi-access Edge Computing (MEC) as a Key Enabler in 6G,” paragraph L92 (approx. manuscript line 362).

---

**Editor Comment (Line 368):** The handover latency values “10–50 ms” and “sub-5 ms” required source support.
**Response:** We added specific supporting references for representative LTE-A and 5G NR handover delay ranges and clarified that these are scenario-dependent reported values used to motivate scheduler sensitivity, not absolute constants.
**Location in corrected article:** Section “Multi-access Edge Computing (MEC) as a Key Enabler in 6G,” paragraph L92 (approx. manuscript line 368).

---

**Editor Comment (Line 383):** The E2E latency formulation was said to be standard, but the cited references did not clearly show that model.
**Response:** We revised the introductory text to state explicitly that the latency decomposition is a synthesized formulation adapted from edge offloading/mobile cloud literature, and we added clearer source attribution for each term used in the decomposition.
**Location in corrected article:** Section “Drastic Reduction in Latency / Mathematical Latency Model,” paragraph L98 (approx. manuscript line 383).

---

**Editor Comment (Line 399):** The backhaul delay range needed a reference or derivation.
**Response:** We added clarifying text explaining the assumed transport scenario behind the backhaul term and cited the relevant source for metropolitan/fiber backhaul latency ranges.
**Location in corrected article:** Section “Drastic Reduction in Latency / Mathematical Latency Model,” paragraphs L110-L114 and L132 (approx. manuscript line 399).

---

**Editor Comment (Line 400):** The cloud queuing delay range needed a reference or derivation.
**Response:** We added an explicit queueing-model assumption and clarified how the reported queueing range is obtained under the stated load assumptions. The text now distinguishes literature-based queueing behavior from the manuscript’s illustrative parameterization.
**Location in corrected article:** Section “Drastic Reduction in Latency / Mathematical Latency Model,” paragraphs L110-L114 and L132 (approx. manuscript line 400).

---

**Editor Comment (Lines 401 and 408):** The total cloud/edge latency estimates were insufficiently justified and one arithmetic example appeared inconsistent.
**Response:** We corrected the arithmetic, assigned explicit representative values to the previously implicit parameters, and added step-by-step clarification showing how the total cloud and edge latency examples are obtained. We also made clear that these are illustrative scenario calculations, not universal bounds.
**Location in corrected article:** Section “Drastic Reduction in Latency / Mathematical Latency Model,” paragraphs L110-L121 and L132 (approx. manuscript lines 401 and 408).

---

**Editor Comment (Line 416):** The edge computation delay (GPU/NPU) needed source support or derivation.
**Response:** We added an explicit supporting reference and clarified the hardware/processing assumptions under which the computation-delay range is representative.
**Location in corrected article:** Section “Drastic Reduction in Latency / 6G Ultra-Low Latency Achievement,” paragraph L128 (approx. manuscript line 416).

---

**Editor Comment (Line 417):** The processing delay value needed source support or derivation.
**Response:** We added a supporting source and clarified that the stated processing delay is a representative pipeline overhead under the example assumptions used in the latency budget.
**Location in corrected article:** Section “Drastic Reduction in Latency / 6G Ultra-Low Latency Achievement,” paragraph L129 (approx. manuscript line 417).

---

**Editor Comment (Line 432):** The handover latency spikes were not integrated into the mathematical formulation.
**Response:** We revised the sensitivity-analysis text to explain explicitly how handover-related perturbations affect the latency model and how these events are treated in the scenario analysis.
**Location in corrected article:** Section “Assumptions and Sensitivity Analysis for the Latency Model,” paragraph L132 (approx. manuscript line 432).

---

**Editor Comment (Fig. 3):** The values “B = 100 MHz” and “SNR = 20 dB” were not clearly connected to Eq. 1 or to the latency estimates.
**Response:** We revised the figure caption and accompanying text to explain how these parameters are used in the transmission-rate term and how they support the latency curves shown in the figure.
**Location in corrected article:** Figure 3 caption and related discussion, paragraphs L143-L145 (Latency model section).

---

**Editor Comment (Line 457):** The bandwidth-reduction framework required clearer source attribution.
**Response:** We revised the lead-in sentence to distinguish the standard offloading framework from the manuscript’s illustrative smart-city parameterization, and we added more precise source attribution.
**Location in corrected article:** Section “Optimized Bandwidth Usage / Mathematical Bandwidth Optimization Model,” paragraph L149 (approx. manuscript line 457).

---

**Editor Comment (Line 492):** The video compression ratio with edge AI needed a reference or derivation.
**Response:** We added explicit source support and clarified that the value is an application-level representative compression range for event-driven video analytics rather than a universally fixed ratio.
**Location in corrected article:** Section “Optimized Bandwidth Usage,” paragraph L180 (approx. manuscript line 492).

---

**Editor Comment (Lines 501-502):** The mutual-information privacy framework and Eqs. 10–13 required clearer provenance.
**Response:** We revised this subsection to identify which parts come from standard mutual-information and differential-privacy theory, and which parts are the manuscript’s illustrative application. We also added clearer source attribution for the privacy formalism rather than relying on a single broad citation.
**Location in corrected article:** Section “Enhanced Privacy and Security / Mathematical Privacy Model,” paragraph L186 and following equations (approx. manuscript lines 501-502).

---

**Editor Comment (Line 592):** The “less than 5%” poisoning-success statement required reference or justification.
**Response:** We added a supporting reference and qualified the value as a reported representative outcome under the specified threat model and malicious-client proportion, rather than a universal guarantee.
**Location in corrected article:** Section “Security and Privacy / New Attack Surfaces in Distributed Edge AI,” paragraph L237 (approx. manuscript line 592).

---

**Editor Comment (Line 596):** The “10–30%” inference-latency increase required reference or justification.
**Response:** We added supporting citations and clarified that the range depends on the chosen robustness mechanism and hardware context.
**Location in corrected article:** Section “Security and Privacy / New Attack Surfaces in Distributed Edge AI,” paragraph L237 (approx. manuscript line 596).

---

**Editor Comment (Lines 705, 718, 719, 724):** The source or derivation of Eqs. 20–23 was unclear.
**Response:** We added explicit source attribution for the FL convergence and differential-privacy equations, clarified that the notation is unified for the survey, and identified the equations as literature-based formulations adapted to the manuscript’s 6G notation.
**Location in corrected article:** Section “Federated Learning,” paragraphs L278-L292 (approx. manuscript lines 705, 718, 719, and 724).

---

**Editor Comment (Line 744):** The provenance of Eq. 25 was unclear.
**Response:** We clarified that Eq. 25 is an AirComp-FL convergence relation adapted from the wireless federated learning literature, added explicit citation support, and explained the role of the aggregation-noise term.
**Location in corrected article:** Section “Impact of Wireless Channel on FL Convergence,” paragraphs L295-L299 (approx. manuscript line 744).

---

**Editor Comment (Line 764):** The claim of “up to 99%” communication-overhead reduction required support.
**Response:** We added supporting references and explicitly marked this figure as an upper-bound result obtained under favorable conditions such as sparse updates, IID data, and stable channels.
**Location in corrected article:** Section “Scalability of FL Gains Under Device Heterogeneity and Non-IID Data,” paragraph L304 (approx. manuscript line 764).

---

**Editor Comment (Line 770):** The “90–95%” net communication savings required support.
**Response:** We added reference support and clarified that this reduced gain corresponds to non-IID and heterogeneous deployment conditions, not the idealized baseline.
**Location in corrected article:** Section “Scalability of FL Gains Under Device Heterogeneity and Non-IID Data,” paragraph L304 (approx. manuscript line 770).

---

**Editor Comment (Lines 778-780):** The “90–99%” practitioner expectation range required support.
**Response:** We revised the sentence to make the upper-bound/bounded-scenario interpretation explicit and added supporting references/qualifying language for the stated deployment-dependent range.
**Location in corrected article:** Section “Scalability of FL Gains Under Device Heterogeneity and Non-IID Data,” paragraph L304 (approx. manuscript lines 778-780).

---

**Editor Comment (Line 817):** The “100:1 to 10,000:1” gradient-compression ratio required support.
**Response:** We added explicit references and clarified that the range reflects order-of-magnitude savings reported across different model sizes, compression strategies, and task types.
**Location in corrected article:** Section “Federated Learning / FL’s Specific Contribution to 6G Performance Improvement,” paragraph L312 (approx. manuscript line 817).

---

**Editor Comment (Lines 836-873):** The formulation in this subsection required clearer provenance from the cited works.
**Response:** We revised the subsection to state clearly that the multi-agent orchestration formalism is a synthesized framework constructed from standard MARL definitions and 6G orchestration variables drawn from the cited literature. We also added more granular source pointers for the state, action, reward, value-function, and algorithmic components.
**Location in corrected article:** Section covering MARL-based orchestration, paragraphs L650-L699 (approx. manuscript lines 836-873).

---

**Editor Comment (Line 899):** Eq. 39 required a reference or justification.
**Response:** We added explicit source attribution for the split-learning convergence expression and clarified the assumptions under which the stated rate applies.
**Location in corrected article:** Section “Split Learning / Convergence,” paragraphs L359-L360 (approx. manuscript line 899).

---

**Editor Comment (Line 946):** Reference [14] was described as an “Edge LAM survey,” but the cited source was not suitable as an archival survey reference.
**Response:** We corrected this by replacing/augmenting the citation with more appropriate scholarly sources and revising the wording so that the literature basis for the Edge LAM discussion is precise and verifiable.
**Location in corrected article:** Section “Edge Large AI Models (Edge LAMs),” paragraph L373 (approx. manuscript line 946).

---

**Editor Comment (Line 1027):** The INT8 vs. FP32 energy ratio on NVIDIA hardware required source support or derivation.
**Response:** We revised the statement to ensure that the reported ratio is directly supported by the cited source and clarified the hardware-specific scope of the comparison.
**Location in corrected article:** Section “Edge Large AI Models / Quantization,” paragraph L405 (approx. manuscript line 1027).

---

**Editor Comment (Line 1068):** The quantization memory-reduction/accuracy-loss statement required support.
**Response:** We added explicit references and qualified the claim as a representative result for well-calibrated quantization settings rather than a universal outcome.
**Location in corrected article:** Section “Supporting Large-Scale AI Models at the Edge—Current State and Practical Viability,” paragraph L423 (approx. manuscript line 1068).

---

**Editor Comment (Line 1069):** The structured-pruning FLOPs/accuracy statement required support.
**Response:** We added supporting references and clarified that the reported pruning range is model- and pruning-strategy-dependent.
**Location in corrected article:** Section “Supporting Large-Scale AI Models at the Edge—Current State and Practical Viability,” paragraph L423 (approx. manuscript line 1069).

---

**Editor Comment (Line 1075):** The “5–10 tokens/s” and “15–30 W” statement required support.
**Response:** We added a direct supporting reference and clarified that the values are hardware-specific performance figures for a concrete edge-device scenario, not general LAM throughput guarantees.
**Location in corrected article:** Section “Supporting Large-Scale AI Models at the Edge—Current State and Practical Viability,” paragraph L423 (approx. manuscript line 1075).

---

**Editor Comment (Line 1129):** The source of the mathematical formulation for spectrum and power allocation was unclear.
**Response:** We revised the subsection to identify the optimization problem as a synthesized formulation based on standard wireless resource-allocation models and AI-based control approaches from the cited literature, and we clarified which cited works support the underlying problem structure.
**Location in corrected article:** Section “AI Applications for 6G Network Optimization at the Edge / Mathematical Formulation - Spectrum and Power Allocation,” paragraph L434 and following equations (approx. manuscript line 1129).

---

**Editor Comment (Line 1176):** The source of the mathematical formulation for massive MIMO beamforming was unclear.
**Response:** We added clearer source attribution for the beamforming objective/constraints and identified the formulation as a standard optimization backbone used to motivate AI-based CSI prediction and beam management.
**Location in corrected article:** Section “AI Applications for 6G Network Optimization at the Edge / Mathematical Formulation - Massive MIMO Beamforming,” paragraph L470 and following equations (approx. manuscript line 1176).

---

**Editor Comment (Line 1178):** Eq. 57 lacked explanation.
**Response:** We added explanatory text immediately around the equation defining the optimization objective, variables, and physical interpretation so that the formulation is self-contained.
**Location in corrected article:** Section “Massive MIMO Beamforming,” paragraphs L470-L474 (approx. manuscript line 1178).

---

**Editor Comment (Line 1186):** The stated “typical performance” value required support/clarification.
**Response:** We corrected and clarified the performance statement so that the metric, unit, and cited support are explicit, and we removed any ambiguity arising from an isolated unsupported numeric value.
**Location in corrected article:** Section “Massive MIMO Beamforming / AI Solution - Deep Learning for CSI Prediction,” paragraph L478 (approx. manuscript line 1186).

---

**Editor Comment (Lines 1373-1430):** The TONA mathematical model needed clarification as to whether it was extracted from the reference or presented as a novel contribution.
**Response:** We substantially revised the subsection to state explicitly that the TONA mathematical formalization is an author-synthesized analytical abstraction inspired by the architectural principles in the cited source, not a verbatim reproduction of the reference. We also clarified which concepts are directly grounded in the cited architecture and which formal expressions are introduced in this manuscript for analytical exposition.
**Location in corrected article:** Section “Task-Oriented Native AI Architecture (TONA),” paragraphs L556-L613 (approx. manuscript lines 1373-1430).

---

**Editor Comment (Lines 1432-1434):** Eqs. 75 and 76 required derivation/explanation relative to the cited TONA source.
**Response:** We added explicit explanatory text linking these equations to the task tuple, DAG-based collaboration, and QoAIS/resource-allocation framework, so their derivation path is clear within the revised manuscript.
**Location in corrected article:** Section “Task-Oriented Native AI Architecture (TONA),” especially paragraphs L576-L613 (approx. manuscript lines 1432-1434).

---

**Editor Comment (Line 1453):** The O-RAN early-deployment spectral-efficiency and energy-improvement values required support.
**Response:** We added direct reference support and clarified that these figures are early deployment/trial indicators reported for specific O-RAN contexts rather than universal O-RAN outcomes.
**Location in corrected article:** Section “O-RAN-Based Architectures with AI / Current Deployment Status of O-RAN,” paragraph L618 (approx. manuscript line 1453).

---

**Editor Comment (Line 1507):** The LEO satellite latency range required support.
**Response:** We added an explicit supporting reference and clarified that the stated latency is a representative propagation/networking range for LEO-assisted scenarios.
**Location in corrected article:** Section “Comparative Analysis and Prioritization of Architectural Approaches / SAGIN versus Terrestrial-Only,” paragraph L626 (approx. manuscript line 1507).

---

**Editor Comment (Line 1581):** The life-cycle utilization threshold for energy efficiency required support.
**Response:** We added appropriate reference support and qualified the value as a reported utilization threshold from life-cycle/energy-efficiency analyses rather than a universal cut-off.
**Location in corrected article:** Section on sustainability considerations, paragraph L637 (approx. manuscript line 1581).

---

**Editor Comment (Line 1807):** The “10–100 ms” convergence time for near-RT control loops required support.
**Response:** We added supporting references and clarified that this range is a representative orchestration-timescale estimate under near-real-time control assumptions.
**Location in corrected article:** Section discussing orchestration overhead vs. performance gains, paragraph L788/L794 (approx. manuscript line 1807).

---

**Editor Comment (Line 1813):** The “100–500 ms” requirement for distributed MARL coordination required support.
**Response:** We added supporting references and clarified that the value denotes representative coordination/convergence overhead in distributed settings.
**Location in corrected article:** Section discussing orchestration overhead vs. performance gains, paragraph L788/L794 (approx. manuscript line 1813).

---

**Editor Comment (Line 1814):** The “5–20 ms” consensus-latency statement required support.
**Response:** We added reference support and clarified that this is a representative added-latency range for distributed coordination mechanisms under the stated orchestration assumptions.
**Location in corrected article:** Section discussing orchestration overhead vs. performance gains, paragraph L788/L794 (approx. manuscript line 1814).

---

**Editor Comment (Line 1934):** The latency-budget component ranges required support.
**Response:** We added supporting references and clarified that these are deployment-planning design envelopes used to illustrate practical control-loop constraints, not fixed values for all 6G systems.
**Location in corrected article:** Section “Concrete Mapping to Functional Splits and Control Loops / Deployment Constraints and Realistic Limitations,” paragraph L830 (approx. manuscript line 1934).

---

**Editor Comment (Line 1938):** The MEC-site power-budget range required support.
**Response:** We added appropriate reference support and clarified that the stated range is a representative site-level power envelope for MEC-class deployments.
**Location in corrected article:** Section “Deployment Constraints and Realistic Limitations,” paragraph L831 (approx. manuscript line 1938).

---

**Editor Comment (Line 1953):** Figure 8 required a source.
**Response:** We revised the figure caption and surrounding text to identify the underlying public standardization roadmaps used to construct the timeline and to clarify that the figure is a consolidated synthesis by the authors.
**Location in corrected article:** Section “Standardization and Future Perspectives,” paragraphs L835-L837 (approx. manuscript line 1953).

---

**Editor Comment (Line 2011):** The CSI-feedback compression range “3x to 32x” required support.
**Response:** We added direct source support for the stated range and clarified that it refers to learned CSI feedback compression at comparable reconstruction quality under the cited setting.
**Location in corrected article:** Section “Status of Standardization,” paragraph L851 (approx. manuscript line 2011).

---

**Editor Comment (Line 2079):** The “99.7% defect detection accuracy with 8 ms inference latency” claim required support.
**Response:** We corrected the citation support for this industrial testbed example and clarified that the values correspond to a specific MEC-enabled quality-inspection deployment rather than a general industrial-AI benchmark.
**Location in corrected article:** Section “Real-world Testbeds and Early Deployments / MEC in Industrial Scenarios,” paragraph L864/L870 (approx. manuscript line 2079).

---

**Editor Comment (Line 2112):** The O-RAN performance-improvement data required support.
**Response:** We added direct supporting references for the trial/deployment figures and aligned the wording across the manuscript so the performance claim is consistently presented as early reported evidence, not a universal guarantee.
**Location in corrected article:** Section “Real-world Testbeds and Early Deployments / O-RAN Trials,” paragraph L874/L880 (approx. manuscript line 2112).

---

#### 2. Figure quality issues

**Editor Comment (Fig. 1):** There were typos on the right side of the figure.
**Response:** Figure 1 has been revised to correct the typographical errors and improve label consistency.
**Location in corrected article:** Figure 1 and caption, paragraph L22.

---

**Editor Comment (Fig. 4):** Some arrows (“Model Synchronization,” “Data Offloading”) appeared to lead nowhere.
**Response:** Figure 4 has been redrawn so that all arrows terminate correctly and the data/control-flow relationships are visually unambiguous.
**Location in corrected article:** Figure 4 and related discussion, paragraphs L246-L248.

---

**Editor Comment (Fig. 5):** The figure was cropped on the left side.
**Response:** Figure 5 has been replaced with a properly aligned and fully visible version, with the left side restored and the layout rechecked.
**Location in corrected article:** Figure 5 and related discussion, paragraphs L368-L371.

---

**Editor Comment (Fig. 7):** Several arrows were unclear or repeated, some labels were duplicated, and some text contained typos/unreadable wording.
**Response:** Figure 7 has been comprehensively revised: redundant/ambiguous arrows were removed or redrawn, repeated labels were eliminated, typographical errors were corrected, and the text was reformatted for readability.
**Location in corrected article:** Figure 7 and caption, paragraphs L539-L540.

---

#### 3. Minor formatting issues

**Editor Comment (Line 2007):** The formatting of “*AI/ML for NR Air Interface*” needed correction.
**Response:** Formatting was corrected as requested, including consistent typography for the cited 3GPP study item.
**Location in corrected article:** Section “Status of Standardization,” paragraph L851 (approx. manuscript line 2007).

---

**Editor Comment (Line 2038):** The parenthetical phrase “(*Vision → Requirements → Technical Study → Normative Specification*)” needed formatting correction.
**Response:** Formatting was corrected as requested, with consistent punctuation and typographic presentation of the phased standardization sequence.
**Location in corrected article:** Section “Status of Standardization,” paragraph L857 (approx. manuscript line 2038).

---

We again thank the editor for the careful review. The comments materially improved the precision, traceability, and presentation quality of the manuscript, and we believe the revised version addresses all concerns raised in the editorial note.
