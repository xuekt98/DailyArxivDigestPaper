+ **EvoMem-VLA: State-Evolution Memory for Long-Horizon Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05418)
![architecture](https://img.shields.io/badge/State_Evolution_Memory_VLA-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Xian_Jiaotong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EvoMem-VLA's central claim is that history VLAs store is wrong in kind, not just too small: existing memories record *what was observed*, but long-horizon control needs remembered states related to *how they changed*. Conditional delta tokenization encodes an ordered source-target frame pair into one directional, source-conditioned token.**</p>

+ **H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06805)
![architecture](https://img.shields.io/badge/Hierarchical_JEPA-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Brown_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**H-JEPA learns hierarchical world models end-to-end for visual planning, and the headline is that a 3-level hierarchy lifts Visual AntMaze planning success from 18% to 73% over flat LeWM - at *lower* planner compute, not higher.**</p>

+ **Beyond LLM Serving: Characterizing Vision-Language-Action Workloads for Embodied AI System Design** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05062)
![architecture](https://img.shields.io/badge/VLA_Serving_Characterization-red)
![task](https://img.shields.io/badge/Evaluation-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Characterizes VLA serving workloads the way LLM serving has been characterized, across 43,200 closed-loop episodes on four VLA models and three platforms - measuring the request patterns, batching behaviour and latency structure that actually differ from text LLMs.**</p>

+ **InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06850)
![architecture](https://img.shields.io/badge/Self_Evolving_Motion_Imitation-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Urbana_Champaign-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**InterMimicGen scales humanoid loco-manipulation by self-evolving motion imitation - a finite set of human interaction captures grows into an expanding repertoire of executable robot skills rather than requiring per-skill data collection.**</p>

+ **TUCO: Curating Simulation Demonstrations for Sim-to-Real Robot Policy Co-Training**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05407)
![architecture](https://img.shields.io/badge/Influence_Decomposition_Curation-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/Stanford_University_2Nanyang-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TUCO curates simulation demonstrations for sim-to-real robot policy co-training, and its contribution is an influence-decomposition criterion for which simulation demonstrations to keep rather than a new control architecture.**</p>

+ **VLA-ZO: Fast Zeroth-Order Adaptation for Vision-Language-Action Models** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06271)
![architecture](https://img.shields.io/badge/Action_Side_Zeroth_Order_Adapter-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Success_Rate_-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VLA-ZO performs zeroth-order adaptation for vision-language-action models - no backpropagation through the backbone - which cuts adaptation memory and compute relative to first-order fine-tuning of the same models.**</p>

+ **PWM: Personalized World Models with Online Reinforcement Learning** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.04920)
![architecture](https://img.shields.io/badge/LoRA_GRPO_Personalization-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_Peking-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PWM learns personalized world models with online reinforcement learning - the personalization signal is LoRA-based and the improvement comes from RL in the loop rather than from better offline personalization.**</p>

+ **Recursive Video In-Context Learning for Agentic Robot** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06843)
![architecture](https://img.shields.io/badge/Recursive_Demo_Hierarchy-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/University_of_Central_Florida-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Recursive Video In-Context Learning (RV-ICL) gives a robot agent one demonstration and segments it offline at its sub-events into a four-level hierarchy, then recurses over that structure to adapt to new tasks.**</p>

+ **Mind the Execution Gap: Action-Semantic Mismatch in World-Model Control** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.06582)
![architecture](https://img.shields.io/badge/Execution_Consistency_Interfaces-red)
![task](https://img.shields.io/badge/Model_Based_RL-magenta)
![organization](https://img.shields.io/badge/Nanjing_University_of_Aeronautics_and-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Diagnoses an action-semantic mismatch in world-model control - the world model can be accurate about what will happen and still be driven by a policy that acts on the wrong abstraction, so good prediction does not imply good control.**</p>

+ **When Does Retrieval Help? A Study of In-Context Adaptation in Vision-Language-Action Models** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.05492)
![architecture](https://img.shields.io/badge/Retrieval_Conditioned_Context-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_Tulane-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Studies when retrieval actually helps in-context adaptation in VLAs, and finds the benefit is conditional rather than universal - retrieval-conditioned context is not a free improvement.**</p>

