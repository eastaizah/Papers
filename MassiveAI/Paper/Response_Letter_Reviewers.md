# Response Letter to the Reviewers

**Manuscript:** Native Artificial Intelligence at the Physical Layer of 6G Networks: Foundations, Architectures, and Perspectives

**Journal:** Future Internet (MDPI), Manuscript ID: futureinternet-4294720

**Date:** April 30, 2026

---

Dear Editor and Reviewers,

We thank the reviewers for their detailed, constructive, and insightful comments. The critiques have substantially improved the scientific rigor and critical balance of the manuscript. Below we address each comment individually, describing the specific changes made and their location in the revised article.

---

## Responses to Reviewer 2

> **R2-C1.** *"The manuscript repeatedly claims that AI-native PHY 'significantly enhances reliability, spectral efficiency, and latency' and 'can exceed conventional communication schemes', but then the provided benchmark contradicts these claims: Autoencoder requires 11.54 dB vs. 3.89 dB (Polar) for n=7; Fails to converge for n≥16; Large gap vs. PPV bound (>7–14 dB)."*

**Response:** We thank the reviewer for this precise and valid critique. The benchmark results in Table II are indeed inconsistent with sweeping claims of superiority, and we have taken care to restructure the narrative throughout the paper to reflect this honestly.

**Corrections made:**

1. **Abstract** (line 5, revised): The abstract has been rewritten to replace "Results demonstrate that AI-native physical layer not only improves conventional performance metrics" with a nuanced statement: *"Published results from the literature demonstrate that AI-native physical layer can improve conventional performance metrics [...]. However, such gains are conditional on adequate training resources, robust channel-matched data, and careful consideration of known limitations including generalisation across channel distributions, sample inefficiency, model interpretability, and hardware implementation constraints — all of which are critically analyzed in this survey. A reproducible proof-of-concept benchmark (Section III.A.7) confirms that, under severe resource constraints, autoencoder-based codes currently underperform conventional schemes."*

2. **Section III.A.4** (paragraph on performance comparison, following the line "Turbo and LDPC codes achieve gaps < 1 dB"): A caveat sentence has been added explicitly noting that "competitive or superior performance" is conditional on GPU-scale training and that Table II shows current under-optimized results.

3. **Section VII.A (Synthesis, point 7)**: The benchmark description in the conclusions has been updated to explicitly state the numerical gap (3.91–>14.67 dB from PPV bound) and characterize it as evidence of training-resource sensitivity, not architectural inferiority, while acknowledging it as a practical barrier.

4. **Section VII.B (Potential Impact)**: The heading "Improved Performance" has been changed to "Conditional Performance Improvements" with a rewritten bullet for short block-length coding that reports both the literature-based GPU-trained results AND our CPU-constrained benchmark, with explicit dB values from Table II.

---

> **R2-C2.** *"The paper reads as advocacy rather than critical survey where AI methods are presented as superior without sufficient caveats and known limitations are underdeveloped, i.e., generalisation across channels, sample inefficiencies, interpretability and hardware constraints."*

**Response:** We agree with this critique. The manuscript now includes a structured critical assessment section and balanced language throughout.

**Corrections made:**

5. **Section VI, new Preamble subsection** (inserted before Section VI.A): A new subsection titled "Preamble: Critical Assessment of Known Limitations" has been added at the beginning of Section VI. This preamble provides a structured, evidence-based assessment of five documented limitations: (1) generalisation across channel distributions — with a pointer to Table III showing BER degradation under Rayleigh fading; (2) sample inefficiency — with reference to Table II showing convergence failure; (3) interpretability and certification — explicitly noting this as a blocking obstacle for safety-critical URLLC applications; (4) hardware and energy constraints — with reference to the 1–2 order-of-magnitude energy gap from Section V.D; and (5) training instability and hyperparameter sensitivity.

6. **Section I.B (State of the Art)** (immediately after the paragraph on O'Shea and Hoydis): A critical balance paragraph has been inserted listing the four major known limitations: generalisation, sample inefficiency, interpretability, and hardware constraints — each linked to the relevant section where they are addressed in depth.

---

> **R2-C3.** *"Several sections are overly dense and verbose, redundant explanations of basic concepts (e.g., neural networks) and figures are referenced but not analysed."*

**Response:** We acknowledge this concern. The note in Section II (line 159) already directs expert readers to skip the standard neural network derivations and proceed to Section II.D. The figure captions have been substantially expanded to include quantitative analysis and explicit connections to the theoretical framework.

**Corrections made:**

7. **Figure 1 caption** (Section I.D): Substantially expanded with explicit labels for each block, a description of what each neural network computes (input/output dimensions, power constraint), and a comparative annotation distinguishing block-wise local optimization from joint end-to-end optimization.

8. **Figure 3 caption** (Section III.A.4): Expanded to explicitly note the simulation source (authors' own Python/PyTorch code in the repository) and to cross-reference Table II results, enabling in-figure analysis without requiring the reader to navigate to the table.

---

> **R2-C4.** *"I would also suggest that authors clarify distinction between Semantic communications vs. representation learning."*

**Response:** An explicit clarification has been added.

**Correction made:**

9. **Section IV.C.1** (after the "Example" sentence): A new paragraph titled "Distinction from Representation Learning" has been inserted. It explains: (a) representation learning is channel-agnostic and targets feature space quality; (b) semantic communications jointly optimises representation AND channel transmission under power/bandwidth constraints; (c) the key distinguishing elements are the physical channel model, the power constraint, and the task-oriented loss — all absent from standalone representation learning frameworks. The section maps these distinctions explicitly to the formal notation used in Section IV.C.2.

---

> **R2-C5.** *"Expand discussion on energy efficiency (critical for 6G)."*

**Response:** Energy efficiency has been substantially expanded.

**Correction made:**

10. **Section V.D.4, new subsection** (added after Section V.D.3 "Energy Efficiency Techniques"): A new subsection titled "Energy Efficiency as a 6G Design Requirement" has been added. It explicitly links to ITU-R IMT-2030 [81] (100× energy efficiency improvement requirement), discusses training-time energy (with a recommendation for federated learning to amortize costs), inference energy for IoT devices (< 1 nJ/bit target vs. current 50–100 pJ/bit for quantized neural models), system-level energy trade-offs (RF power savings vs. inference overhead), and explicitly flags the uncharacterised system-level energy balance as an important open problem for 6G deployment.

---

> **R2-C6.** *"Expand discussion on hardware-aware learning (quantization, RF impairments)."*

**Response:** The quantization section has been substantially expanded to include a comprehensive treatment of hardware-aware learning with RF impairments.

**Correction made:**

11. **Section V.A.3** (retitled "Quantization, Model Optimization, and Hardware-Aware Learning"): A new subsection "Hardware-Aware Learning: RF Impairments and Practical Transceiver Constraints" has been added. This covers: (a) Power Amplifier non-linearity with the AM/AM and AM/PM model, PAPR-aware training, and differentiable PA layer; (b) Phase noise at mmWave/sub-THz frequencies and Transformer-based robustness; (c) I/Q imbalance and implicit adaptation via hardware-in-the-loop training; (d) ADC quantization with the straight-through estimator; (e) DAC constraints for 1-bit massive MIMO. The subsection concludes with an explicit statement of the sim-to-real gap as a primary obstacle to deployment.

---

## Responses to Reviewer 4

> **R4-C1.** *"In 6G with native AI there are also procedures that belong to layers 2-3 and that will be controlled by AI, for example handover or scheduling. It would be nice if these were also mentioned and introduced in the general context."*

**Response:** We thank the reviewer for this contextualisation note. A scope clarification has been added.

**Correction made:**

12. **Section I.D (Article Organization)**: A clearly delimited note box titled "Note on Scope (Layers 2–3)" has been added immediately after the article structure description. This note: (a) explicitly acknowledges that native AI plays a role in Layer 2–3 procedures (handover, MAC scheduling, interference coordination, routing) in 6G; (b) references the NWDAF and AI-RAN frameworks in 3GPP Release 18/19; (c) provides references [39]–[40] for readers interested in AI-based scheduling and multi-cell coordination; and (d) explains that a full treatment with the mathematical rigour applied to PHY is beyond the scope of this survey.

---

> **R4-C2.** *"Fig. 1 needs some additional explanations."*

**Response:** Figure 1's description has been substantially expanded.

**Correction made:**

13. **Figure 1 caption** (Section I.D): The figure description now includes: (a) explicit labels for all blocks in the traditional system (with functional descriptions of what each block does); (b) explicit dimensionality labels for the AI-native system ($x \in \mathbb{C}^M$, power constraint $\mathbb{E}[\|x\|^2] \leq P$); (c) explicit labeling of the gradient flow arrows $\nabla_\theta$ and $\nabla_\phi$ indicating what is being optimized; (d) a comparative annotation box "Traditional: 7 separate blocks, each independently designed | AI-Native: 2 neural networks, jointly trained end-to-end"; (e) explicit color coding specification.

---

> **R4-C3.** *"Fig. 2: why Multi-user detection appears twice?"*

**Response:** The figure description had an inconsistency that could lead to duplication in rendered figures. The figure description has been corrected.

**Correction made:**

14. **Figure 2 description** (Section III introduction): The figure description has been rewritten to explicitly list **five distinct main branches** and include the annotation **"Note: Branch (3) 'Signal Detection (Multi-User)' appears only once in this figure and is distinct from Branch (4) 'Intelligent Beamforming' — do not duplicate."** Additionally, the fifth branch has been corrected from "End-to-End Systems" (which did not correspond to Section III.E) to "Radio Resource Management" (which accurately reflects Section III.E), resolving the structural ambiguity that may have caused the duplication.

---

> **R4-C4.** *"Fig. 3, 5 and 6: mouse over figure shows a dark gray box with white text: 'Diagrama El contenido generado por IA puede ser incorrecto.' In this view, the graphs in Fig. 3 are obtained through your own simulations or generated with AI? In the repository on github, the run_ber_curves.py script produces 'Experiment 3 – Complete BER vs Eb/N0 curves (Figure 5 in the article)', but in the paper fig. 5 is 'MIMO Communication Autoencoder Architecture with Differentiable Channel'."*

**Response:** This comment identifies two issues: (a) ambiguity about whether the curves in Fig. 3 are from authors' simulations or AI-generated; and (b) a figure numbering mismatch between the repository script and the paper.

**Corrections made:**

15. **Figure 3 caption** (Section III.A.4): The caption now begins with an explicit statement: **"These curves are generated by the authors' own simulations using the Python script `run_ber_curves.py` (PyTorch, CPU, fixed random seed), available in the repository associated with this article. The graphs are *not* AI-generated; they are produced deterministically by the simulation code."**

16. **Figure 3 caption (continued)**: A note has been added clarifying the figure numbering: *"Note: the script internally labels the output as 'Experiment 3 – Complete BER vs Eb/N0 curves' with a legacy reference to 'Figure 5'; the correct figure number in this article is **Figure 3**."* The repository script should be updated in a future revision to replace "Figure 5" with "Figure 3".

17. **Figure 6 caption** (Section IV.B.4): An explicit note has been added: **"Note: the PSNR curves in subfigure (b) are reproduced from the literature results of [45],[48] and are not AI-generated; they represent published simulation data from the referenced papers, not output from an AI image-generation tool."**

---

> **R4-C5.** *"Fig. 5, please correct: in the left side of fig. the vertical text is unreadable; also is not very clear what is in the upper left corner and below the arrow between transmitter and channel."*

**Response:** The Figure 5 description has been substantially revised to prevent these rendering issues.

**Correction made:**

18. **Figure 5 description** (Section IV.A.3): The figure description has been rewritten with three explicit layout requirements: (a) *"All axis labels and layer labels must use horizontal text only — no vertical/rotated text, as vertical text at the left side of this figure is unreadable in print"*; (b) *"The upper-left corner of the figure must include a clear legend box identifying the block naming convention (Transmitter=red, Channel=gray, Receiver=blue)"*; (c) *"The arrow between 'Transmitter' and 'Channel' must be labeled explicitly: top of arrow → '$\mathbf{x} \in \mathbb{C}^{N_t \times n}$ (transmitted signal, power-normalized)'; below the arrow → 'Power constraint: $\mathbb{E}[\|\mathbf{x}\|^2] \leq P$'"*. All layer labels in the description now include explicit human-readable names (e.g., "Message Embedding", "FC-1", "Power Norm.", "I/Q Split + Flatten").

---

> **R4-C6.** *"Section 3.1.7, Experimental setup, last point: Polyanskiy-Poor-Verdú (PPV) Bound: Finite block-length bound from equation (4). But (4) gives the received signal, after propagation through the channel (lines 205-206). Please check."*

**Response:** The reviewer is entirely correct. Equation (4) in the manuscript is indeed the received signal model $\mathbf{y} = h(f_{\theta}(\mathbf{s})) + \mathbf{n}$ (Section II.A.2), not the PPV bound. The PPV bound is $P_e \geq Q\!\left(\frac{nC-k}{\sqrt{nV}}+\frac{\log n}{2\sqrt{nV}}\right)$, which appears in Section II.B.2. We apologise for this error.

**Correction made:**

19. **Section III.A.7 Experimental Setup, last bullet** (PPV Bound): The incorrect reference "Finite block-length bound from equation (4)" has been replaced with: *"Finite block-length bound from [5] (see Section II.B.2, equation $P_e \geq Q\!\left(\frac{nC-k}{\sqrt{nV}}+\frac{\log n}{2\sqrt{nV}}\right)$). Note: this is distinct from equation (4) of this paper, which gives the received signal model $\mathbf{y} = h(f_{\theta}(\mathbf{s}))+\mathbf{n}$; the PPV bound is derived in [5] and reproduced in Section II.B.2."*

---

## Summary of All Changes

| Item | Reviewer | Location in Revised Article | Type of Change |
|------|----------|---------------------------|----------------|
| 1 | R2-C1 | Abstract | Rewritten — added caveats and benchmark result summary |
| 2 | R2-C1 | Section III.A.4 | Added caveat to "competitive or superior" claim |
| 3 | R2-C1 | Section VII.A point 7 | Updated benchmark description with explicit dB gaps |
| 4 | R2-C1 | Section VII.B | Changed heading; rewrote performance bullet with conditional framing |
| 5 | R2-C2 | Section VI, new Preamble | New subsection: Critical Assessment of Known Limitations |
| 6 | R2-C2 | Section I.B | Added limitations paragraph after O'Shea/Hoydis |
| 7 | R2-C3 | Figure 1 caption | Substantially expanded with labels, annotations, color coding |
| 8 | R2-C3 | Figure 3 caption | Added simulation source, cross-reference to Table II |
| 9 | R2-C4 | Section IV.C.1 | New paragraph: Distinction from Representation Learning |
| 10 | R2-C5 | Section V.D.4 | New subsection: Energy Efficiency as a 6G Design Requirement |
| 11 | R2-C6 | Section V.A.3 | Expanded to include RF impairments and hardware-aware learning |
| 12 | R4-C1 | Section I.D (Note box) | New scope note on Layer 2-3 AI procedures |
| 13 | R4-C2 | Figure 1 caption | Substantially expanded (same as item 7 above) |
| 14 | R4-C3 | Figure 2 description | Fixed duplicate; corrected 5th branch; added "do not duplicate" note |
| 15 | R4-C4 | Figure 3 caption | Added explicit statement: own simulations, not AI-generated |
| 16 | R4-C4 | Figure 3 caption | Added figure number correction note (script legacy "Figure 5" → correct "Figure 3") |
| 17 | R4-C4 | Figure 6 caption | Added note: PSNR curves from literature, not AI-generated |
| 18 | R4-C5 | Figure 5 description | Rewritten with layout requirements: horizontal text, legend box, arrow labels |
| 19 | R4-C6 | Section III.A.7, last bullet | Corrected equation reference from wrong "(4)" to Section II.B.2 with PPV formula |

---

We believe these revisions address all raised concerns and have resulted in a more rigorous, critically balanced, and technically complete survey. We look forward to the reviewers' evaluation of the revised manuscript.

Sincerely,

*The Authors*
