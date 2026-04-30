Reviewer 2
This manuscript addresses a high-impact and strategically important topic, however, currently, it leans too much towards visionary narrative and non-validated claims, rather than a balanced, critical, and evidence-driven survey.
Framing of AI as a design primitive is well aligned with current discourse in 3GPP and IMT-2030. 
The manuscript repeatedly claims that AI-native PHY “significantly enhances reliability, spectral efficiency, and latency” and “can exceed conventional communication schemes”, but then the provided benchmark contradicts these claims:
•	Autoencoder requires 11.54 dB vs. 3.89 dB (Polar) for n=7
•	Fails to converge for n \geq 16
•	Large gap vs. PPV bound (>7–14 dB)
The paper reads as advocacy rather than critical survey where AI methods are presented as superior without sufficient caveats and known limitations are underdeveloped, i.e., generalisation across channels, sample inefficiencies, interpretability and hardware constraints. 
Several sections are overly dense and verbose, redundant explanations of basic concepts (e.g., neural networks) and figures are referenced but not analysed
I would also suggest that authors clarify distinction between Semantic communications vs. representation learning and expand discussion on energy efficiency (critical for 6G) and hardware-aware learning (quantization, RF impairments). 
With some revision, particularly around scientific rigor and critical analysis, the paper could become a valuable contribution to the 6G and AI-for-communications literature.

Reviewer 4
In the era of artificial intelligence and the future 6G network currently in the standardization stage, a synthesis paper that systematically analyzes all aspects of native artificial intelligence included in the 6G network is certainly welcome.
As the authors state, the paper is a unified and systematic synthesis, unlike other similar papers that only deal with certain specific components.
In addition, the value of the paper is high due to the coherent and complex mathematical apparatus that addresses all relevant aspects of AI in the physical level of 6G and due to the authors' own simulations, which allow a fair comparison with similar results in the literature. The simulation environment created is available online and allows on the one hand to verify the results obtained by the authors and on the other hand constitutes a starting point for researchers who want to delve deeper into different aspects of native AI in 6G.
However, in 6G with native AI there are also procedures that belong to layers 2-3 and that will be controlled by AI, for example handover or scheduling. It would be nice if these were also mentioned and introduced in the general context, even if they are only listed and not deepened with a complex mathematical framework.
**********
Fig. 1 needs some additional explanations.
Fig. 2: why Multi-user detection appears twice?
Fig. 3, 5 and 6: mouse over figure shows a dark gray box with white text: “Diagrama El contenido generado por IA puede ser incorrecto.” In this view, the graphs in Fig. 3 are obtained through your own simulations or generated with AI? In the repository on github, the run_ber_curves.py script produces  “Experiment 3 – Complete BER vs Eb/N0 curves (Figure 5 in the article).”, but in the paper fig. 5 is “MIMO Communication Autoencoder Architecture with Differentiable Channel”
Fig. 5, please correct: in the left side of fig. the vertical text is unreadable; also is not very clear what is in the upper left corner and below the arrow between transmitter and channel.
Section 3.1.7, Experimental setup, last point: Polyanskiy-Poor-Verdú (PPV) Bound: Finite block-length bound from equation (4). But (4) gives the received signal, after propagation through the channel (lines 205-206). Please check.
