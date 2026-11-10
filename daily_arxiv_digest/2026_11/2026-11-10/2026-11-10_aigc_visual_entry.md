<!-- direction: aigc_generation -->

+ **IdealCache: Rethinking Cache Scheduling in Diffusion Transformers via Ideal Trajectories**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10340)
![architecture](https://img.shields.io/badge/Ideal_Cache_Scheduler-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher_Santa_Clara_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 DiT 缓存调度从固定间隔改为理想轨迹上的约束最短路搜索：免重训在 Qwen-Image 加速 6.35×、Qwen-Image-Edit 5.84×、HunyuanVideo 4.32×，图像编辑上的语义一致性甚至可略高于 50 步基线。**</p>

+ **Split and Bridge: Multimodal Generation via Diffusion Bridging**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10441)
![architecture](https://img.shields.io/badge/Split_and_Bridge-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_University_of_Vermont-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/AhmadArrabi/SnB)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把预训练单模态扩散模型在采样期耦合起来：共享前段轨迹、在分裂点用桥接模块分叉，CelebAMask-HQ 上无条件 FID 约 59~61，优于 MoPoE 的 151.23，并可零样本做交错共生成与图像编辑。**</p>

+ **On the universal structure in deterministic generative diffusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10338)
![architecture](https://img.shields.io/badge/Hyperbolic_Gaussian_Flow-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/UC_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**理论工作：确定性扩散采样轨迹在图像、音频、文本、3D 点云上共享同一种几何形状，第一主成分解释 99% 以上方差，可用基于 LMMSE 去噪器的高斯流精确刻画其嵌套双曲结构，为采样器设计与加速提供几何参照。**</p>

+ **Can General-Purpose Generative AI Supply Training Data for Medical Vision Models? A Multimodal Retrospective Study**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10484)
![architecture](https://img.shields.io/badge/Nano_Banana_Synthetic_Pipeline-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Oxford-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**使用侧实证：用通用生成与编辑模型造合成胸片、眼底、CT 与颈动脉超声数据，纯合成训练模型 AUROC 达 0.877/0.963/0.711 并能分层 633 例外部受试者，但校准与净收益并不优于真实数据模型。**</p>

<!-- direction: aigc_rl -->

+ **HexIt: Learning Hexahedral Block Decomposition with Expert Iteration on Combinatorial Maps**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10433)
![architecture](https://img.shields.io/badge/Dart_Convolution_Policy-red)
![task](https://img.shields.io/badge/RL_for_3D_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_California_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把六面体块分解写成组合映射上的序列决策，用克隆加专家迭代训练卷积策略：留出倒角实体 20 次采样平均解出 94.4%，大倒角实体 best-of-20 从 0.203 升到 0.355，而 PPO、GRPO、VinePPO 在同算力下全部变差。**</p>

