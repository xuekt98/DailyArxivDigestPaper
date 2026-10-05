+ **Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric Rewards**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.02967)
![architecture](https://img.shields.io/badge/Reward_Composition-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Arena_Intelligence_Inc-green)
[![project](https://img.shields.io/badge/project-blue)](https://arena.ai/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Composes two heterogeneous reward signals for T2I post-training - a preference reward trained with a Bradley-Terry objective on large-scale human preference data, and rubric-based rewards that score prompt faithfulness and act as a safeguard against reward hacking.**</p>

+ **VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.03221)
![architecture](https://img.shields.io/badge/Optimal_Transport_Distillation-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Sydney-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Identifies that balanced optimal-transport distillation fails for T2V and I2V, where one condition admits many valid outputs so spatial tokens need not align across different realizations.**</p>

+ **In-Distribution Forcing for Long Video Generation at Test Time**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.03120)
![architecture](https://img.shields.io/badge/Autoregressive_KV_Conditioning-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University_2Korea-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Names the KV-provenance problem - existing KV conditioning assumes cached KV entries stay in-distribution, but beyond the training horizon nothing constrains how rollout KV entries are built, so they themselves become OOD.**</p>

+ **Parasitic Co-Denoising: Unlocking 3D Human Motion Generation in a Frozen Video Diffusion Model**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.03047)
![architecture](https://img.shields.io/badge/Flow_Matching_Decoder-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Probing a frozen Wan2.1 text-to-video model shows a recoverable motion signal is present in its intermediate states across the *entire* denoising schedule, not confined to the clean output - despite the model never being supervised on explicit 3D motion.**</p>

+ **MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.02153)
![architecture](https://img.shields.io/badge/KV_Memory_Routing-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Cornell_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Long-horizon AR video loses fine visual detail when an object leaves the finite context window. MosaiChunk composes a mosaic of selected historical KV entries across space and time.**</p>

+ **TerraVis: Towards Evaluation of World-Grounded Visual Consistency in Text-to-Image Generation via MLLM Workflows**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.02959)
![architecture](https://img.shields.io/badge/MLLM_Evaluation_Pipeline-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/AIML_Adelaide_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ShyFoo/TerraVis)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Argues that photorealistic-looking T2I output can still violate real-world plausibility - malformed object structures, impossible anatomy, physically implausible interactions, inconsistent spatial relations - and that fidelity, aesthetics, preference and alignment metrics do not capture this.**</p>

+ **OuroReward: Sequential Reward Scheduling for Reinforcement Learning in Text-to-3D Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.03423)
![architecture](https://img.shields.io/badge/Reward_Scheduling-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Text-to-3D RL typically optimizes semantic alignment, texture clarity and other dimensions *simultaneously* through reward aggregation, without modelling inter-dimension dependencies - causing imbalanced optimization and persistent interference.**</p>

+ **AREX: Affine-Residual Exponential Integrator for Few-Step Sampling in Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.03483)
![architecture](https://img.shields.io/badge/Exponential_Integrator_Sampler-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Department_of_Mathematics_KTH_Royal-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Shows the velocity field of the moment-matched Gaussian target is the $L^2$-optimal affine approximation to the marginal velocity field, motivating decomposition of learned dynamics into an affine component over the whole sampling path plus a neural residual term.**</p>

+ **TRAC: Trajectory-aware Reuse and Adaptive Correction for Efficient Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.02779)
![architecture](https://img.shields.io/badge/Cache_Reuse_Scheduling-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Argues AR video acceleration differs from single-trajectory bidirectional generation: AR sequentially couples chunk-level denoising trajectories, so approximation errors accumulate and propagate through the generation process.**</p>

+ **Weave Forcing: Compositional Memory Routing for Interactive Long Video Generation** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.03510)
![architecture](https://img.shields.io/badge/Compositional_Memory_Routing-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Electronic_Science_and-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Interactive storytelling needs more than continuous scene extension - a new shot may combine characters and backgrounds from *different* historical shots. Whole-prompt retrieval overlooks per-component reference needs; combining all historical memory introduces unrelated content.**</p>

