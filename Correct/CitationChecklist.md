# Citation and Reference Verification Checklist
## Paper: Computational Architectures for 6G Networks

### Instructions
For each item below, verify that the cited reference contains the claimed information at the indicated location. Mark ☐ as ☑ when verified.

- For entries with **no citation in the article**, add a source or rewrite the text as an explicitly stated author assumption/estimate.
- For entries where the cited survey/reference is **too general**, replace it with a primary source, standard, benchmark paper, or operator/vendor report.
- For equations labeled below as **author synthesis**, either (i) state that clearly in the manuscript, or (ii) provide a derivation and cite the exact source model.

---

### Category 1: Deployment and Performance Claims

#### Item 1: Commercial MEC deployments by Deutsche Telekom, Verizon, and NTT DOCOMO
- **Article Location:** Section 2 (MEC as a Key Enabler in 6G), L78
- **Claim in Article:** "Major operators including Deutsche Telekom, Verizon, and NTT DOCOMO have deployed MEC servers at cellular base station sites, primarily supporting low-latency video processing, V2X, and industrial automation use cases."
- **Cited Reference(s):** None cited in the article.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** The statement is plausible, but it is operator-specific, deployment-specific, and time-sensitive. It cannot remain uncited.
- **Suggested alternative reference(s):** ETSI MEC overview [28] for MEC context; operator documentation/press releases for Verizon 5G Edge/AWS Wavelength, Deutsche Telekom/T-Systems edge deployments, and NTT DOCOMO MEC/5G Open Partner initiatives.
- **Status:** ☐ Pending verification

#### Item 2: 6G mobility up to 1000 km/h
- **Article Location:** Section 2 (radio-channel constraints on MEC), L92
- **Claim in Article:** "Doppler shifts at high mobility (up to 1000 km/h for 6G [8])"
- **Cited Reference(s):** [8] Li, P.; Fan, J.; Wu, J. *Exploring the Key Technologies and Applications of 6G Wireless Communication Network*. iScience 2025, 28, 112281. doi:10.1016/j.isci.2025.112281.
- **Where to verify in reference:** Likely Introduction or KPI/requirements table discussing 6G targets; also check any subsection comparing 5G and 6G capability requirements.
- **Supporting evidence / assessment:** The 1000 km/h target is a standard 6G KPI, but it is more commonly cited from IMT-2030/6G vision references such as [2] or [76]. [8] may mention it, but this must be verified in the KPI summary/table.
- **Suggested alternative reference(s):** [2] Chen et al., *Vision, Requirements, and Technology Trends of 6G Wireless Networks*; [76] ITU-R M.2160-0.
- **Status:** ☐ Pending verification

#### Item 3: LTE-A and 5G NR handover latency values
- **Article Location:** Section 2 (radio-channel constraints on MEC), L92
- **Claim in Article:** "handover events in high-mobility scenarios introduce additional latency spikes of 10–50 ms in LTE-A and sub-5 ms with 5G NR fast handover"
- **Cited Reference(s):** [34] Chang, L. et al. *6G-Enabled Edge AI for Metaverse: Challenges, Methods, and Future Research Directions*. J. Commun. Inf. Netw. 2022, 7. doi:10.23919/JCIN.2022.9815195.; [35] Shi, W. et al. *Edge Computing: Vision and Challenges*. IEEE Internet Things J. 2016, 3, 637–646. doi:10.1109/JIOT.2016.2579198.
- **Where to verify in reference:** [34] likely sections on metaverse latency constraints or mobility challenges; [35] likely Intro/Challenges sections only.
- **Supporting evidence / assessment:** [35] is very unlikely to contain LTE-A versus 5G NR handover measurements; [34] may discuss mobility qualitatively but is unlikely to give these exact numbers. A dedicated handover measurement paper or 3GPP mobility reference is probably needed.
- **Suggested alternative reference(s):** 3GPP mobility/handover studies; LTE/5G handover performance measurement papers; operator or academic benchmarking papers specific to fast handover.
- **Status:** ☐ Pending verification

#### Item 4: E2E latency decomposition as a “standard formulation”
- **Article Location:** Section 2.3 (Mathematical Latency Model), L98
- **Claim in Article:** "The following E2E latency decomposition is a standard formulation widely used in edge and mobile cloud computing literature [4,34]"
- **Cited Reference(s):** [4] Al-Ansi, A. et al. *Survey on Intelligence Edge Computing in 6G: Characteristics, Challenges, Potential Use Cases, and Market Drivers*. Future Internet 2021, 13. doi:10.3390/fi13050118.; [34] Chang, L. et al. *6G-Enabled Edge AI for Metaverse: Challenges, Methods, and Future Research Directions*. J. Commun. Inf. Netw. 2022, 7. doi:10.23919/JCIN.2022.9815195.
- **Where to verify in reference:** [4] sections reviewing MEC/edge benefits and latency; [34] sections discussing metaverse latency constraints and edge offloading.
- **Supporting evidence / assessment:** These references may support the importance of low latency, but they are unlikely to present the exact decomposition in the manuscript. This looks more like an author synthesis of standard offloading terms. Either mark it as adapted/original or cite a primary mobile-edge offloading model paper.
- **Suggested alternative reference(s):** Standard MEC offloading/system-model papers or surveys focused explicitly on computation-offloading latency models.
- **Status:** ☐ Pending verification

#### Item 5: Backhaul and queuing delay ranges in cloud latency model
- **Article Location:** Section 2.3 (Cloud vs. Edge Latency Comparison), L112–L113
- **Claim in Article:** "Backhaul: ≈10−50 ms [4,34]" and "Queuing: ≈5−20 ms [4,34]"
- **Cited Reference(s):** [4] Al-Ansi et al., *Survey on Intelligence Edge Computing in 6G*; [34] Chang et al., *6G-Enabled Edge AI for Metaverse*.
- **Where to verify in reference:** [4] tables or narrative on edge/cloud latency components; [34] any latency-budget discussion for immersive applications.
- **Supporting evidence / assessment:** Exact numerical ranges of this kind are unlikely to be directly tabulated in either survey. The manuscript should either show a derivation from an explicit scenario or replace the citations with studies that measure backhaul and queueing delay.
- **Suggested alternative reference(s):** Primary MEC latency measurement papers; transport/backhaul latency studies; queueing-based edge-offloading papers.
- **Status:** ☐ Pending verification

#### Item 6: Total cloud and edge latency values
- **Article Location:** Section 2.3 (Cloud vs. Edge Latency Comparison), L114–L121
- **Claim in Article:** "Total: cloud≈20−80 ms" and "Total: edge≈0.5−5 ms"
- **Cited Reference(s):** No direct citation attached to the totals; upstream context cites [4,34].
- **Full bibliographic details of cited reference(s):** [4] Al-Ansi et al., *Survey on Intelligence Edge Computing in 6G*; [34] Chang et al., *6G-Enabled Edge AI for Metaverse*.
- **Where to verify in reference:** N/A unless these totals are explicitly derived there.
- **Supporting evidence / assessment:** This is primarily a derivation/consistency issue, not only a citation issue. The article must specify the missing parameter values (D, R, C, f), show the arithmetic, and correct any mismatch between the stated sum and the reported total.
- **Suggested alternative reference(s):** None required if authors provide a transparent derivation and label the values as illustrative assumptions.
- **Status:** ☐ Pending verification

#### Item 7: Edge computation delay of 0.2–0.5 ms
- **Article Location:** Section 2.3 (6G Ultra-Low Latency Achievement), L128
- **Claim in Article:** "Edge computation (GPU/NPU): ≈0.2−0.5 ms [34,35]"
- **Cited Reference(s):** [34] Chang et al., *6G-Enabled Edge AI for Metaverse*; [35] Shi et al., *Edge Computing: Vision and Challenges*.
- **Where to verify in reference:** [34] edge-AI processing latency discussions; [35] general challenge overview.
- **Supporting evidence / assessment:** [35] is very unlikely to support a sub-millisecond GPU/NPU benchmark. [34] may discuss stringent latency targets, but exact compute-delay values should come from benchmark or hardware-performance studies.
- **Suggested alternative reference(s):** Edge AI inference benchmarking papers or hardware vendor benchmark reports.
- **Status:** ☐ Pending verification

#### Item 8: Processing delay of 0.1 ms
- **Article Location:** Section 2.3 (6G Ultra-Low Latency Achievement), L129
- **Claim in Article:** "Processing delay: ≈0.1 ms [34]"
- **Cited Reference(s):** [34] Chang, L. et al. *6G-Enabled Edge AI for Metaverse: Challenges, Methods, and Future Research Directions*. J. Commun. Inf. Netw. 2022, 7. doi:10.23919/JCIN.2022.9815195.
- **Where to verify in reference:** Likely any section on end-to-end latency budget for metaverse services.
- **Supporting evidence / assessment:** This appears too specific for a broad survey unless an explicit latency table is present. If the value is an engineering assumption, it should be labeled as such; otherwise a primary benchmark reference is needed.
- **Suggested alternative reference(s):** Real-time edge-processing benchmark papers or 5G/6G application latency-budget studies.
- **Status:** ☐ Pending verification

#### Item 9: Handover latency spikes of 5–50 ms in sensitivity analysis
- **Article Location:** Section 2.3 (Assumptions and Sensitivity Analysis), L132
- **Claim in Article:** "handover latency spikes of 5-50 ms"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** The number needs a source, and the model should also show where the handover term enters the E2E latency equation. As written, it is neither cited nor mathematically integrated.
- **Suggested alternative reference(s):** Dedicated LTE/5G handover-latency measurement studies or 3GPP technical reports.
- **Status:** ☐ Pending verification

#### Item 10: Figure 3 assumptions B = 100 MHz and SNR = 20 dB
- **Article Location:** Figure 3 / Section 2.3, L143–L145
- **Claim in Article:** "B=100MHz; SNR = 20dB"
- **Cited Reference(s):** No explicit citation tied to these assumptions.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This is best treated as a modeling assumption, not a literature claim, unless the authors can point to a specific 5G/6G scenario definition. The manuscript should explain exactly how these parameters are used in Eq. (1).
- **Suggested alternative reference(s):** 3GPP/ITU scenario documents if the intention is to present a standardized radio configuration; otherwise label as illustrative assumptions.
- **Status:** ☐ Pending verification

#### Item 11: Bandwidth reduction framework adapted from [4,34]
- **Article Location:** Section 2.4 (Bandwidth Optimization Model), L149
- **Claim in Article:** "The following bandwidth reduction framework is adapted from standard edge offloading models in [4,34]"
- **Cited Reference(s):** [4] Al-Ansi et al., *Survey on Intelligence Edge Computing in 6G*; [34] Chang et al., *6G-Enabled Edge AI for Metaverse*.
- **Where to verify in reference:** [4] sections on traffic reduction/use cases; [34] sections on edge-AI offloading for immersive services.
- **Supporting evidence / assessment:** The high-level idea is supported, but the exact framework/equations are unlikely to appear verbatim in those surveys. This should be labeled as an adapted or original illustrative model unless a primary source is added.
- **Suggested alternative reference(s):** MEC offloading and edge-video analytics papers with explicit traffic/bandwidth equations.
- **Status:** ☐ Pending verification

#### Item 12: Video compression ratio with edge AI
- **Article Location:** Section 2.4 (Typical compression ratios), L180
- **Claim in Article:** "Video (with edge AI): ≈0.001−0.01 (…) [4,16]"
- **Cited Reference(s):** [4] Al-Ansi, A. et al. *Survey on Intelligence Edge Computing in 6G*; [16] Wang, X. et al. *Convergence of Edge Computing and Deep Learning: A Comprehensive Survey*. IEEE Commun. Surv. Tutor. 2020, 22, 869–904. doi:10.1109/COMST.2020.2970550.
- **Where to verify in reference:** [16] sections on edge video analytics, inference-at-edge, or data reduction benefits; [4] use-case discussion/tables.
- **Supporting evidence / assessment:** The intuition is reasonable for metadata/event-only transmission, but the exact 0.001–0.01 ratio is very specific and likely not directly stated in either survey. A primary smart-surveillance or edge-video analytics reference is preferable.
- **Suggested alternative reference(s):** Edge video analytics / intelligent surveillance studies measuring metadata-only uplink reduction.
- **Status:** ☐ Pending verification

#### Item 13: Mutual-information privacy formulation from Letaief et al.
- **Article Location:** Section 2.4 (Mathematical Privacy Model), L186
- **Claim in Article:** "The following information-theoretic privacy framework is based on the mutual-information formulation of Letaief et al. [17]"
- **Cited Reference(s):** [17] Letaief, K.B.; Shi, Y.; Lu, J.; Lu, J. *Edge Artificial Intelligence for 6G: Vision, Enabling Technologies, and Applications*. IEEE J. Sel. Areas Commun. 2022, 40, 5–36. doi:10.1109/JSAC.2021.3126076.
- **Where to verify in reference:** Likely privacy/security discussion in challenge or enabling-technology sections.
- **Supporting evidence / assessment:** [17] is a vision/enabling-technologies paper and may discuss privacy conceptually, but it is unlikely to present the exact mutual-information equations used here. The manuscript probably needs an information-theoretic privacy reference in addition to [17].
- **Suggested alternative reference(s):** A primary mutual-information privacy or information bottleneck reference; differential privacy references for the DP portion.
- **Status:** ☐ Pending verification

#### Item 14: Poisoning success reduced to <5% with 30% malicious clients
- **Article Location:** Section 2.6 (New Attack Surfaces in Distributed Edge AI), L237
- **Claim in Article:** "reducing poisoning success rates to less than 5% even with 30% malicious clients"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This is highly algorithm- and threat-model-dependent. It needs a direct citation to robust FL literature; otherwise it should be removed or softened.
- **Suggested alternative reference(s):** Krum, coordinate-wise median, FLTrust, and Byzantine-robust FL evaluation papers.
- **Status:** ☐ Pending verification

#### Item 15: Adversarial defenses increase inference latency by 10–30%
- **Article Location:** Section 2.6 (New Attack Surfaces in Distributed Edge AI), L237
- **Claim in Article:** "Adversarial training and certified robustness techniques provide defences but increase inference latency by 10-30%."
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** Plausible, but too specific to remain uncited. The exact overhead depends on the model, defense method, and hardware.
- **Suggested alternative reference(s):** Adversarial training / certified robustness benchmark papers reporting inference-time or end-to-end overhead.
- **Status:** ☐ Pending verification

---

### Category 2: Federated Learning, Split Learning, and Communication-Reduction Claims

#### Item 16: Communication overhead reduction of up to 99%
- **Article Location:** Section 3.1 (FL scalability under heterogeneity), L304
- **Claim in Article:** "The communication overhead reduction of up to 99% via top-k gradient sparsification…"
- **Cited Reference(s):** No direct citation in the sentence; nearby FL discussion cites [18], [20], [45], [46].
- **Full bibliographic details of cited reference(s):** [18] Abreha, H.G. et al. *Federated Learning in Edge Computing: A Systematic Survey*. Sensors 2022, 22, 450. doi:10.3390/s22020450.; [20] Kairouz, P. et al. *Advances and Open Problems in Federated Learning*. Found. Trends Mach. Learn. 2021, 14, 1–210. doi:10.1561/2200000083.; [45] McMahan, B. et al. *Communication-Efficient Learning of Deep Networks from Decentralized Data*. AISTATS 2017.; [46] Zhu, F. et al. *Wireless Large AI Model: Shaping the AI-Native Future of 6G and Beyond*. arXiv 2025, arXiv:2504.14653.
- **Where to verify in reference:** [20] survey sections on communication efficiency/compression; [45] FedAvg original paper for communication rounds, not necessarily sparsification; [46] likely too general for this claim.
- **Supporting evidence / assessment:** The 99% figure is plausible if it literally means retaining 1% of gradient entries, but it should be tied to a compression paper, not left implicit. As written, it is under-cited.
- **Suggested alternative reference(s):** Gradient sparsification / Deep Gradient Compression / Top-k SGD papers.
- **Status:** ☐ Pending verification

#### Item 17: Non-IID conditions reduce net savings to 90–95%
- **Article Location:** Section 3.1 (FL scalability under heterogeneity), L304
- **Claim in Article:** "Under highly non-IID conditions… reducing net communication savings to approximately 90-95%."
- **Cited Reference(s):** No direct citation in the sentence.
- **Full bibliographic details of cited reference(s):** None directly attached.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This sounds like an author estimate rather than a generally established number. It needs either a study that quantifies this degradation or a rewrite indicating it is an illustrative expectation.
- **Suggested alternative reference(s):** FedProx, SCAFFOLD, and non-IID FL experimental papers reporting extra rounds/communication cost.
- **Status:** ☐ Pending verification

#### Item 18: Practitioners should expect 90–99% reduction
- **Article Location:** Section 3.1 (FL scalability under heterogeneity), L304
- **Claim in Article:** "practitioners should expect 90-99% reduction depending on deployment scenario"
- **Cited Reference(s):** No direct citation in the sentence.
- **Full bibliographic details of cited reference(s):** None directly attached.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This is a generalized recommendation and should either be derived explicitly from cited studies or rewritten as a qualitative takeaway.
- **Suggested alternative reference(s):** Compression studies plus FL-in-wireless testbed papers that show scenario-dependent savings.
- **Status:** ☐ Pending verification

#### Item 19: Raw-data-to-gradient reduction ratio of 100:1 to 10,000:1
- **Article Location:** Section 3.1 (FL contribution to 6G), L312
- **Claim in Article:** "(typically 100:1 to 10,000:1 with gradient compression)"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** The range is very broad and strongly depends on the application, dataset size, model dimension, and compression ratio. It needs a derivation or a narrower, application-specific citation.
- **Suggested alternative reference(s):** FL communication-efficiency surveys or case studies comparing raw-data transfer versus model-update transfer.
- **Status:** ☐ Pending verification

#### Item 20: Source of Equations (20)–(23)
- **Article Location:** Section 3.1 (FL convergence and differential privacy), roughly L278–L292
- **Claim in Article:** Equations (20)–(23) are presented near references [18], [20], [45], [46].
- **Cited Reference(s):** [18] Abreha et al., *Federated Learning in Edge Computing: A Systematic Survey*.; [20] Kairouz et al., *Advances and Open Problems in Federated Learning*.; [45] McMahan et al., *Communication-Efficient Learning of Deep Networks from Decentralized Data*.; [46] Zhu et al., *Wireless Large AI Model*.
- **Where to verify in reference:** [20] for general FL objective/convergence discussion; [45] for FedAvg formulation; privacy equations would need DP-specific sections or separate DP references.
- **Supporting evidence / assessment:** Eq. (20) likely resembles standard FL convergence bounds and may be traceable to FL surveys. Eqs. (21)–(23) look like clipped-gradient + Gaussian-noise DP-SGD/basic composition formulas, which are not the core contribution of [45] or [46]. These equations need explicit source separation.
- **Suggested alternative reference(s):** Add a differential privacy reference (e.g., DP-SGD/basic composition) for Eqs. (21)–(23).
- **Status:** ☐ Pending verification

#### Item 21: Source of Eq. (25) from Amiri & Gündüz
- **Article Location:** Section 3.1 (AirComp-FL convergence), L298–L299
- **Claim in Article:** "The convergence bound for AirComp-FL incorporates an additional noise term" in Eq. (25), cited to [49].
- **Cited Reference(s):** [49] Mohammadi Amiri, M.; Gündüz, D. *Machine Learning at the Wireless Edge: Distributed Stochastic Gradient Descent over the Air*. IEEE Trans. Signal Process. 2020, 68, 2155–2169. doi:10.1109/TSP.2020.2981904.
- **Where to verify in reference:** System model, convergence analysis, and theorem/proposition sections on analog DSGD over-the-air.
- **Supporting evidence / assessment:** [49] is a plausible source for an AirComp/analog-SGD convergence expression. However, the manuscript should point to the exact theorem/proposition or state that Eq. (25) is adapted notation, not a verbatim restatement.
- **Suggested alternative reference(s):** None if the exact theorem/section is identified; otherwise add a sentence showing the derivation from [49].
- **Status:** ☐ Pending verification

#### Item 22: “Edge LAM survey [14]” as a source
- **Article Location:** Section 3.3 (Edge LAM frameworks), L373
- **Claim in Article:** "the Edge LAM survey [14]"
- **Cited Reference(s):** [14] Yan, X.; Wang, J.; Zhang, X.; Zhang, Y. *Data Plane Design for AI-Native 6G Networks*; Huawei, 2025.
- **Where to verify in reference:** Entire document/site.
- **Supporting evidence / assessment:** The editor is correct: [14] does not appear to be a peer-reviewed survey and may be a website/industry document without a traceable reference apparatus. It is not a strong source for survey-style claims or detailed mathematical formulations.
- **Suggested alternative reference(s):** [62] Wang et al., *Edge Large AI Models: Revolutionizing 6G Networks*; [19] Chen et al., *Toward 6G Native-AI Network*; other peer-reviewed LLM/LAM-at-the-edge surveys.
- **Status:** ☐ Pending verification

#### Item 23: INT8 vs. FP32 energy ratio of ~27–35× on NVIDIA hardware
- **Article Location:** Section 3.3 (Quantization), L405
- **Claim in Article:** "INT8 vs. FP32 energy ratio measured on NVIDIA hardware: ~27–35× [19]"
- **Cited Reference(s):** [19] Chen, X. et al. *Toward 6G Native-AI Network: Foundation Model Based Cloud-Edge-End Collaboration Framework*. arXiv 2023, arXiv:2310.17471.
- **Where to verify in reference:** Likely sections on model efficiency, edge deployment, or cloud-edge-end collaboration.
- **Supporting evidence / assessment:** [19] is likely to discuss model efficiency at a framework level, but the phrase "measured on NVIDIA hardware" suggests a hardware benchmark source rather than a conceptual arXiv framework paper. This citation is probably weak.
- **Suggested alternative reference(s):** NVIDIA performance/energy benchmark documentation, TensorRT/Jetson benchmark reports, or hardware-aware inference papers.
- **Status:** ☐ Pending verification

#### Item 24: Quantization gives 4–8× memory reduction with <2% accuracy loss
- **Article Location:** Section 3.3 (Practical viability of large models at edge), L423
- **Claim in Article:** "quantization (INT8/INT4) achieves 4-8x memory reduction with less than 2% accuracy loss"
- **Cited Reference(s):** None directly cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** The claim is broadly plausible, but it requires a quantization paper or survey. It should not remain uncited.
- **Suggested alternative reference(s):** LLM.int8(), QLoRA, or recent model-quantization surveys/benchmarks.
- **Status:** ☐ Pending verification

#### Item 25: Structured pruning cuts FLOPs by 50–70% with 1–3% accuracy loss
- **Article Location:** Section 3.3 (Practical viability of large models at edge), L423
- **Claim in Article:** "structured pruning reduces FLOPs by 50-70% with 1-3% accuracy degradation"
- **Cited Reference(s):** None directly cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This is again plausible but highly model-dependent. A pruning benchmark or pruning survey is required.
- **Suggested alternative reference(s):** Structured pruning benchmark papers or pruning surveys for edge inference.
- **Status:** ☐ Pending verification

#### Item 26: 7B model runs at 5–10 tokens/s and 15–30W on Jetson AGX Orin
- **Article Location:** Section 3.3 (Practical viability of large models at edge), L423
- **Claim in Article:** "INT8 inference on an NVIDIA Jetson AGX Orin achieves approximately 5-10 tokens per second for a 7B model, consuming 15-30W"
- **Cited Reference(s):** None directly cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This is a hardware-specific benchmark and must be cited to a reproducible benchmark source. Without a direct source it should be removed or labeled as an internal estimate.
- **Suggested alternative reference(s):** NVIDIA Jetson benchmark reports, vendor documentation, or peer-reviewed edge-LLM deployment papers.
- **Status:** ☐ Pending verification

---

### Category 3: Wireless Optimization, Beamforming, and Architectural Formulations

#### Item 27: Source of spectrum and power allocation formulation
- **Article Location:** Section 3.4 (Mathematical Formulation - Spectrum and Power Allocation), L434–L450
- **Claim in Article:** The formulation is presented as part of the standard wireless optimization literature and nearby text cites [4], [17], [57]–[59].
- **Cited Reference(s):** [4] Al-Ansi et al., *Survey on Intelligence Edge Computing in 6G*.; [17] Letaief et al., *Edge Artificial Intelligence for 6G*.; [57] Alhashimi et al., *Survey on AI-Enabled Resource Management for 6G Heterogeneous Networks*.; [58] Cui et al., *Overview of AI and Communication for 6G Network*.; [59] Yang et al., *Artificial Intelligence-Enabled Intelligent 6G Networks*.
- **Where to verify in reference:** [57]–[59] are the most likely sources; look for sections on radio resource management, power allocation, and DRL-based allocation formulations.
- **Supporting evidence / assessment:** [57]–[59] likely support the general optimization problem class. [4] and [17] are probably too broad to justify the exact formulation. The manuscript should identify which reference provides the objective, which provides Shannon-rate constraints, and which supports the AI solution method.
- **Suggested alternative reference(s):** Dedicated resource-allocation optimization papers if the exact mixed-integer formulation is intended to be standard rather than synthesized.
- **Status:** ☐ Pending verification

#### Item 28: Source of massive MIMO beamforming formulation
- **Article Location:** Section 3.4 (Mathematical Formulation - Massive MIMO Beamforming), L470 onward
- **Claim in Article:** The beamforming problem is introduced without a clearly pinned source.
- **Cited Reference(s):** Nearby context cites [1], [58], [14], and later [59]/[61] in this subsection.
- **Full bibliographic details of cited reference(s):** [1] Pennanen et al., *6G: The Intelligent Network of Everything—A Comprehensive Vision, Survey, and Tutorial*. IEEE Access 2024.; [58] Cui et al., *Overview of AI and Communication for 6G Network*. Sci. China Inf. Sci. 2025.; [59] Yang et al., *Artificial Intelligence-Enabled Intelligent 6G Networks*. IEEE Netw. 2020.; [61] Mao, Q.; Hu, F.; Hao, Q. *Deep Learning for Intelligent Wireless Networks: A Comprehensive Survey*. IEEE Commun. Surv. Tutor. 2018, 20, 2595–2621. doi:10.1109/COMST.2018.2846401.
- **Where to verify in reference:** Search the cited surveys for sections on beamforming, CSI prediction, and massive-MIMO AI methods.
- **Supporting evidence / assessment:** A standard beamforming optimization problem certainly exists in the literature, but the manuscript should cite a specific beamforming source instead of only adjacent surveys. As written, the provenance is ambiguous.
- **Suggested alternative reference(s):** Massive-MIMO beamforming textbooks/surveys or AI-for-beamforming primary papers.
- **Status:** ☐ Pending verification

#### Item 29: Eq. (57) lacks definition and source
- **Article Location:** Section 3.4 (Massive MIMO Beamforming), near L470–L474
- **Claim in Article:** Eq. (57) is presented with insufficient explanation.
- **Cited Reference(s):** No explicit source identified for Eq. (57).
- **Full bibliographic details of cited reference(s):** None explicitly tied to the equation.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This requires both a citation and explanatory text. The equation should be identified as, e.g., sum-rate maximization, SINR-constrained beamforming, MMSE beamforming, etc., with variables defined.
- **Suggested alternative reference(s):** The primary beamforming reference actually used by the authors.
- **Status:** ☐ Pending verification

#### Item 30: Beamforming/CSI prediction performance value near ref. [61]
- **Article Location:** Section 3.4 (AI solution for CSI prediction), current extract L478; editor note refers to the beamforming area near line 1186
- **Claim in Article:** Editor flagged a performance statement around this area ("prediction error 0.99 [61]"); current extract instead reads: "Typical performance: prediction error < -20 dB SNR for … ms."
- **Cited Reference(s):** [61] Mao, Q.; Hu, F.; Hao, Q. *Deep Learning for Intelligent Wireless Networks: A Comprehensive Survey*. IEEE Commun. Surv. Tutor. 2018, 20, 2595–2621. doi:10.1109/COMST.2018.2846401.
- **Where to verify in reference:** Sections surveying DL for channel estimation/prediction and mobility prediction.
- **Supporting evidence / assessment:** [61] is a survey and may not contain the exact benchmark value used in the manuscript. The claim likely needs a primary CSI prediction paper rather than a survey citation.
- **Suggested alternative reference(s):** A specific CSI prediction or beam prediction paper reporting the exact metric and horizon.
- **Status:** ☐ Pending verification

#### Item 31: TONA mathematical model extracted from ref. [5]
- **Article Location:** Section 4.2.2 (Task-Oriented Native AI Architecture), L556–L617
- **Claim in Article:** The TONA subsection presents task tuples, QoAIS vectors, optimization objectives, DAG-based collaboration, and control-plane equations as if extracted from [5].
- **Cited Reference(s):** [5] Yang, Y. et al. *Task-Oriented 6G Native-AI Network Architecture*. IEEE Network 2024, 38, 219–227. doi:10.1109/MNET.2023.3321464.
- **Where to verify in reference:** Conceptual architecture description, QoAIS/task-oriented design sections, figures, and any system-model discussion.
- **Supporting evidence / assessment:** [5] very likely supports the task-oriented architectural concepts and QoAIS idea, but it may not present the exact mathematical tuple/objective/DAG notation used here. The article should explicitly say which equations are restatements, which are abstractions, and which are new.
- **Suggested alternative reference(s):** None if authors clearly mark the equations as author-derived formalizations of the concepts in [5].
- **Status:** ☐ Pending verification

#### Item 32: Source/derivation of TONA Equations (75)–(76)
- **Article Location:** Section 4.2.2 (TONA privacy/task constraints), around L609–L613 in the extract; editor maps this to Eqs. 75–76
- **Claim in Article:** Equations (75)–(76) are presented as part of the TONA model.
- **Cited Reference(s):** [5] Yang, Y. et al. *Task-Oriented 6G Native-AI Network Architecture*. IEEE Network 2024, 38, 219–227. doi:10.1109/MNET.2023.3321464.
- **Where to verify in reference:** Sections on task orchestration, QoAIS, privacy/security constraints, and any formal problem statement.
- **Supporting evidence / assessment:** These equations appear more detailed than a typical IEEE Network architecture article would provide. Most likely they are author-derived formal constraints inspired by [5], not directly extracted.
- **Suggested alternative reference(s):** State explicitly that Eqs. (75)–(76) are new formalizations, unless an exact source can be cited.
- **Status:** ☐ Pending verification

#### Item 33: O-RAN deployment gains of 15–20% spectral efficiency and 10–15% energy reduction
- **Article Location:** Section 4.2 (Current Deployment Status of O-RAN), L618
- **Claim in Article:** "Early deployment data indicate 15-20% spectral efficiency improvements and 10-15% energy consumption reductions"
- **Cited Reference(s):** None in this sentence.
- **Full bibliographic details of cited reference(s):** None directly attached.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This must be sourced. The percentages are plausible for some vendor/operator trials but cannot be stated generally without a field report.
- **Suggested alternative reference(s):** [78] Rakuten Mobile white paper for deployment context; operator/vendor O-RAN case studies; O-RAN Alliance or vendor trial reports with measured KPIs.
- **Status:** ☐ Pending verification

#### Item 34: LEO satellite latency of ~25–50 ms
- **Article Location:** Section 4.3 (SAGIN vs. terrestrial-only), L628
- **Claim in Article:** "LEO satellite latency ~25-50ms"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** The range is plausible for LEO RTT estimates, but it needs a satellite/NTN reference. Since the section already discusses SAGIN, a NTN/SAGIN survey should be cited.
- **Suggested alternative reference(s):** [63] Dalai et al., *Satellite-6G Network Integration Roadmap on Reference Architectures*; NTN latency/propagation studies.
- **Status:** ☐ Pending verification

#### Item 35: Edge is energy-efficient only above 40–50% utilization
- **Article Location:** Section 4.3 (Sustainability Considerations), L637
- **Claim in Article:** "Life-cycle analysis suggests that edge deployment is energy-efficient only when utilization rates exceed 40-50%"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This is a strong, quantitative sustainability threshold and needs a life-cycle-analysis source. Without a citation it should be removed or softened.
- **Suggested alternative reference(s):** Sustainability / LCA studies comparing centralized cloud and edge infrastructures.
- **Status:** ☐ Pending verification

#### Item 36: Centralized RL orchestration converges in 10–100 ms
- **Article Location:** Section 4.4 (Comparative Framework for Orchestration Overhead), L788
- **Claim in Article:** "centralized RL-based orchestrators converge in 10-100 ms for near-RT control loops"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This is implementation-dependent and needs a benchmark or testbed reference. As stated, it reads like an estimate.
- **Suggested alternative reference(s):** O-RAN near-RT RIC xApp/rApp benchmark papers or orchestration testbed studies.
- **Status:** ☐ Pending verification

#### Item 37: Distributed MARL schemes require 100–500 ms
- **Article Location:** Section 4.4 (Comparative Framework for Orchestration Overhead), L788
- **Claim in Article:** "distributed MARL schemes require 100-500 ms due to inter-agent coordination"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** Plausible but too specific to remain unsupported. The value should be tied to a specific MARL/orchestration experiment.
- **Suggested alternative reference(s):** MARL-for-wireless/network-orchestration papers with wall-clock or control-loop timing results.
- **Status:** ☐ Pending verification

#### Item 38: Consensus mechanisms add 5–20 ms latency
- **Article Location:** Section 4.4 (Comparative Framework for Orchestration Overhead), L788
- **Claim in Article:** "consensus mechanisms (adding 5-20 ms latency)"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This is platform/protocol dependent. The article needs either a distributed-systems source or should present it as an order-of-magnitude assumption.
- **Suggested alternative reference(s):** Distributed orchestration / consensus benchmark studies.
- **Status:** ☐ Pending verification

#### Item 39: Latency budget components for radio, edge, backhaul, and application processing
- **Article Location:** Section 4.5 (Deployment Constraints and Realistic Limitations), L830
- **Claim in Article:** "radio access (~1-5ms), edge processing (~1-10ms), backhaul (~1-20ms depending on distance), application processing (~1-50ms depending on complexity)"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** These look like engineering-rule-of-thumb latency budgets. They are useful, but they need either a source or an explicit statement that they are illustrative planning values.
- **Suggested alternative reference(s):** MEC latency-budget papers, URLLC architecture papers, or industry white papers with end-to-end latency breakdowns.
- **Status:** ☐ Pending verification

#### Item 40: MEC server power budget of 500 W–2 kW per site
- **Article Location:** Section 4.5 (Deployment Constraints and Realistic Limitations), L831
- **Claim in Article:** "(typically 500W-2kW per site for MEC servers)"
- **Cited Reference(s):** None cited in the sentence.
- **Full bibliographic details of cited reference(s):** None.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** This is plausible for some site/server configurations, but it must be backed by operator deployment documentation, ETSI/GSMA guidance, or hardware datasheets.
- **Suggested alternative reference(s):** Operator MEC deployment documents, edge-server vendor datasheets, or energy-consumption studies for edge nodes.
- **Status:** ☐ Pending verification

#### Item 41: Source of Figure 8 (6G standardization roadmap)
- **Article Location:** Section 5, L837
- **Claim in Article:** "Figure 8. 6G standardization Roadmap (2020–2030)"
- **Cited Reference(s):** No source given in the figure caption.
- **Full bibliographic details of cited reference(s):** None explicitly tied to the figure.
- **Where to verify in reference:** N/A.
- **Supporting evidence / assessment:** The figure source must be disclosed. If the figure is author-created, the caption should say "Authors’ compilation based on [7], [72], [73], [74], [75], [76], [79]" (or whichever sources were used).
- **Suggested alternative reference(s):** ITU-R IMT-2030 [7], ITU-R M.2160-0 [76], Ericsson [73], 3GPP timelines [74,75], O-RAN Alliance roadmap materials.
- **Status:** ☐ Pending verification

#### Item 42: CSI feedback can be reduced by 3× to 32×
- **Article Location:** Section 5 (3GPP AI/ML for NR Air Interface), L857 / current extract L851
- **Claim in Article:** "encoder–decoder neural architectures (e.g., CsiNet) can reduce uplink CSI feedback by 3x to 32x at comparable reconstruction accuracy"
- **Cited Reference(s):** General section cites [74] Chen, W. *RAN Rel-19 Status and a Look Beyond 2025*. Available online: https://www.3gpp.org/technologies/ran-rel-19 (accessed on 8 April 2026).; [75] 3GPP. *Overview of AI/ML Related Work in 3GPP*. 2025. Available online: https://www.3gpp.org/news-events/3gpp-news/ai-ml-2025.
- **Where to verify in reference:** [75] is the most likely place if it summarizes AI/ML air-interface examples; otherwise look in 3GPP TR 38.843 or the original CsiNet literature.
- **Supporting evidence / assessment:** The numeric 3×–32× range sounds more like the original CSI-compression literature than a high-level 3GPP news/overview page. The current references may support the work item, but probably not the exact numbers.
- **Suggested alternative reference(s):** 3GPP TR 38.843 and original CsiNet / AI-based CSI compression papers.
- **Status:** ☐ Pending verification

---

### Category 4: Real-World Deployments, O-RAN Evidence, and Remaining Equation Provenance

#### Item 43: BMW industrial MEC deployment with 99.7% accuracy and 8 ms inference latency
- **Article Location:** Section 5 (Real-world Testbeds and Early Deployments), L864
- **Claim in Article:** "achieving 99.7% defect detection accuracy with 8 ms inference latency [4]"
- **Cited Reference(s):** [4] Al-Ansi, A. et al. *Survey on Intelligence Edge Computing in 6G: Characteristics, Challenges, Potential Use Cases, and Market Drivers*. Future Internet 2021, 13. doi:10.3390/fi13050118.
- **Where to verify in reference:** Search case-study/use-case sections for industrial automation, manufacturing, or quality inspection.
- **Supporting evidence / assessment:** A broad 2021 survey is unlikely to contain this specific BMW deployment metric. This almost certainly needs a primary industrial testbed/case-study source.
- **Suggested alternative reference(s):** 5G-ACIA industrial testbed reports, BMW/industrial MEC case-study publications, factory computer-vision deployment papers.
- **Status:** ☐ Pending verification

#### Item 44: O-RAN performance gains cited to O-RAN WG1 document
- **Article Location:** Section 5 (O-RAN Trials), L874
- **Claim in Article:** "15–20% improvement in spectral efficiency and 10–15% reduction in energy consumption compared to traditional RAN architectures [79]"
- **Cited Reference(s):** [79] O-RAN Alliance. *O-RAN Working Group 1: Use Cases and Overall Architecture*; O-RAN Alliance, 2023.
- **Where to verify in reference:** Use-case descriptions and any annexes/tables with expected or reported benefits.
- **Supporting evidence / assessment:** WG1 architecture/use-case documents usually describe architecture and use cases, not operator field-trial measurements. The citation may support the O-RAN concept, but likely not the specific performance percentages.
- **Suggested alternative reference(s):** Operator/vendor O-RAN field-trial papers or white papers reporting measured spectral-efficiency and energy results.
- **Status:** ☐ Pending verification

#### Item 45: Source of formulations in the block tied to refs [42], [46], [53]
- **Article Location:** Section 3.2–3.3 (Split Learning / Edge LAM mathematical block), approximately L314–L428; editor maps this concern to lines 836–873 in the manuscript
- **Claim in Article:** The manuscript presents a sequence of SL/Edge-LAM equations while citing nearby references [42], [46], [53].
- **Cited Reference(s):** [42] Zhang, M. et al. *Semantic Edge Computing and Semantic Communications in 6G Networks: A Unifying Survey and Research Challenges*. arXiv 2024, arXiv:2411.18199.; [46] Zhu, F. et al. *Wireless Large AI Model: Shaping the AI-Native Future of 6G and Beyond*. arXiv 2025, arXiv:2504.14653.; [53] Lin, Z. et al. *Split Learning in 6G Edge Networks*. arXiv 2023, arXiv:2306.12194. doi:10.48550/arXiv.2306.12194.
- **Where to verify in reference:** [53] for split-learning system models and optimization issues; [46] for wireless large-model deployment concepts; [42] for semantic edge/communication framing.
- **Supporting evidence / assessment:** [53] likely supports the SL concept and perhaps some latency/communication trade-off structure. [46] likely supports edge LAM deployment motivations. [42] supports semantic/edge framing. However, the full equation block appears to be a synthesis rather than a direct restatement from any single source.
- **Suggested alternative reference(s):** Keep the existing refs for context, but explicitly label the equations as synthesized or provide equation-by-equation citations.
- **Status:** ☐ Pending verification

#### Item 46: Reference/justification for Eq. (39)
- **Article Location:** Section 3.2 (Split Learning convergence), L359–L360; editor maps this to the Eq. 39 area
- **Claim in Article:** Eq. (39) gives a convergence-rate expression for split learning with privacy-preserving noise.
- **Cited Reference(s):** Immediate subsection cites [53] Lin, Z. et al. *Split Learning in 6G Edge Networks*. arXiv 2023, arXiv:2306.12194.; nearby discussion also uses [42] and [20].
- **Where to verify in reference:** [53] for SL training dynamics and optimization trade-offs; [20] for general optimization/privacy background.
- **Supporting evidence / assessment:** The exact convergence expression in Eq. (39) looks more specialized than the surrounding references likely provide. Unless the authors can point to an exact theorem, it should be labeled as an author-derived illustrative bound.
- **Suggested alternative reference(s):** A primary split-learning optimization/convergence paper if the authors want to keep Eq. (39) as a literature-based result.
- **Status:** ☐ Pending verification

---

### High-priority revision notes for the authors

1. **Replace vague survey citations with primary sources** for benchmark numbers, deployment percentages, hardware energy ratios, and operator-specific claims.
2. **Label synthesized equations as such.** Several mathematical blocks look like reasonable author formalizations, but they are not clearly attributable to the cited references.
3. **Separate “literature-based facts” from “illustrative assumptions.”** Values such as B = 100 MHz, SNR = 20 dB, latency-budget components, and some overhead ranges may be kept if explicitly marked as scenario assumptions.
4. **Use the references already in the manuscript more precisely.** In many cases the cited paper likely supports the topic but not the exact number.
5. **For every retained quantitative claim, add one of the following:** exact page, section, table, theorem, figure, or appendix location in the source.

