REVIEWER 1

I just have the following minor comments.

1. The authors introduce the Large AI Model (LAM) in the manuscript. What is the difference between the LAM and the large language model (LLM)?
2. There are many formulas and derivations in this manuscript, and it is recommended to make a clear distinction between the existing research content and the original content.
3. The authors introduce many related technologies, and it is recommended to clarify the current implementation status of these technologies in their respective sections.
4. For the distributed computing, the authors may include the following works. Hierarchical optimization for task execution cost minimization in D2D-assisted mobile edge computing networks; Joint trajectory, resource, and access optimization in multi-UAV collaborative mobile edge computing networks for low-altitude economy.
5. There is a mix of the British and the American spellings in the manuscript (e.g., centralized/centralised and optimization/optimisation). Please check the full text and revise it.


REVIEWER 2

However, while the paper is technically rich and broad in scope, certain areas, such as practical deployment constraints, cross-layer optimization under realistic wireless impairments, and system-level validation, require deeper critical analysis. Overall, the paper is a strong contribution but would benefit from further refinement in bridging theoretical models with real-world implementation challenges.

1. The paper presents an analytical E2E latency model showing an 85–95% reduction when transitioning from cloud to edge. How do the authors justify the assumptions regarding queuing delay and backhaul latency, and how sensitive are these results under realistic stochastic traffic conditions and variable wireless channel impairments (e.g., fading, interference, and handovers)?
2. While the manuscript acknowledges the impact of wireless channel variability on task offloading, how can the proposed architectures explicitly incorporate channel-aware optimization (e.g., joint scheduling of computation and radio resources) within Edge AI frameworks such as Federated Learning?
3. The review highlights up to 99% communication reduction using gradient compression in Federated Learning. How do these gains scale with increasing device heterogeneity, non-IID data distributions, and straggler effects in ultra-dense 6G deployments?
4. The integration of distributed computing with AI-native orchestration introduces significant control-plane complexity. Can the authors provide a formal framework or comparative evaluation of orchestration overhead versus performance gains, particularly in O-RAN or SAGIN architectures?
5. Given the limited computational resources at edge nodes, how do the authors envision supporting emerging large-scale AI models (e.g., edge-adapted LLMs) without compromising latency and energy efficiency? Is model partitioning (e.g., split learning) sufficient for real-time constraints?
6. The paper presents an information-theoretic privacy model showing reduced leakage at the edge. However, how do the authors address new attack surfaces introduced by distributed edge nodes, such as model poisoning, adversarial inference, and compromised edge infrastructure?
7. The manuscript provides a strong overview of ITU-R, 3GPP, and ETSI efforts. What are the key mismatches between current standardization timelines and the rapid evolution of AI-native architectures, and how might this impact real-world deployment of 6G systems?
8. The review includes analytical and theoretical comparisons, but lacks discussion of large-scale experimental validation. Are there existing testbeds or simulation frameworks that can validate the proposed architectures under realistic 6G workloads, mobility patterns, and heterogeneous network conditions?


REVIEWER 3

1. The manuscript’s abstract and introduction require substantial revision to improve technical clarity and logical coherence. The abstract should be restructured to explicitly present the study purpose, the proposed methodology, and the key quantitative results, so that the contribution and findings are immediately clear to the reader. In addition, the introduction is currently weak in flow and integration; the background, problem statement, research gap, and motivation are not connected in a clear progression. The authors are encouraged to revise this section by following the organizational style of the suggested reference papers, ensuring a more coherent transition from prior work to the identified gap and then to the specific contribution of the present study.
Localization in ISAC: A review
Quantifying Risk with AI: Models and Frameworks
Energy-Efficient, Multi-Agent Deep Reinforcement Learning Approach for Adaptive Beacon Selection in AUV-Based Underwater Localization
2. Some abbreviations are not defined for their first appearance, such as (FL, PRISMA, etc).
3. There are a lot of grammatical and typos the authors are suggested to do a strong proofread before the revision submission and remove them.
4. Refine the objective to explicitly state the primary focus of the study, such as "This study investigates the integration of distributed computing and Edge AI for enabling 6G networks, with a focus on reducing latency, optimizing resources, and providing context-aware services.
5. Include specific details on the selection criteria, the number of papers analyzed, and how the literature was categorized (e.g., types of architectural proposals, Edge AI techniques, etc.). A brief mention of the methods used for data synthesis (e.g., meta-analysis, qualitative analysis) would add rigor to the methodology.
6. The paper mentions several performance improvements such as "reducing latency by 85-95%" and "communication overhead reductions of 99%". While these are impressive numbers, the context in which these improvements are measured is not clear. The authors should also mention the conditions or assumptions under which these results were obtained.
7. The paper briefly mentions Edge AI techniques such as Federated Learning and Split Learning, but does not explain how these techniques specifically contribute to improving 6G performance. A clearer link between these techniques and their real-world applicability would strengthen the impact of the study.
8. Some abbreviations are explained repeatedly many times, such as Federated Learning (FL). The authors should remove them and follow the given papers to solve these problems and take help from them.