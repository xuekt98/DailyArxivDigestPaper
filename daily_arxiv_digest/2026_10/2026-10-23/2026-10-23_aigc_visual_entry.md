# 2026-10-23 - AIGC 图像 / 视频 / 3D 生成与编辑 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Direct Forcing: A Single-Stage Training Recipe for Few-Step Autoregressive Text-to-Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30861)
![architecture](https://img.shields.io/badge/Direct_Forcing-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Direct Forcing 把因果适配与分布匹配合并成单阶段训练，用 MMD 对齐自生成 rollout 与参考视频分布，250 次更新即从 Wan2.1-1.3B 得到四步自回归生成器，VBench Total 达 84.63。**</p>
+ **Making MLLM Latents Matter: Factor-Aware Predictive Learning for Cinematic Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30926)
![architecture](https://img.shields.io/badge/Factor-Aware_Predictive_Learning-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/MMLab@HKUST,_The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FAPL 先用 latent-only grounding 确认 DiT 真的在用 MLLM 潜变量，再分别用 factor-span replacement 实现因子级控制、冻结 DiT 反训 MLLM 实现稀疏时间推理，在三项电影级视频任务上均优于基线。**</p>
+ **WorldForge V2: Eliciting Camera-Trajectory Alignment in Video Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31640)
![architecture](https://img.shields.io/badge/WorldForge_V2-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Westlake_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WorldForge V2 用训练无关的 warped-reference 引导实现精确相机控制，以光流定位运动潜通道做选择性引导，并用 Trajectory LoRA 把适应集中到敏感网络块，单个训练场景即可泛化到未见场景。**</p>
+ **Latent Space Jam: Layout Guided Video Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30390)
![architecture](https://img.shields.io/badge/Latent_Space_Jam-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/CANVAS_Lab,_Reichman_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Latent Space Jam 用两遍式训练无关方法为预训练视频扩散模型加布局控制：第一遍靠 prompt 引导的 cross-attention 生成粗布局与运动，第二遍再做精化，无需额外训练。**</p>
+ **SciFusion: Physics-Guided Compositional Diffusion for Multimodal 3D Scientific Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30313)
![architecture](https://img.shields.io/badge/SciFusion-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Princeton_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SciFusion 用 latent diffusion 统一 15 种科学影像模态的 3D 生成：把条件分解为 domain / object / contrast 并可推理时零样本重组，同时为 MRI、CT、电子 microscopy 分别加入物理一致性约束。**</p>
+ **Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images for 3D Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31649)
![architecture](https://img.shields.io/badge/Gate3DGen-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://supra-3d.github.io/gate3dgen)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Gate3DGen 是一个门控式 3D 生成前置净化器：degradation-aware router 跳过干净输入，一步净化器保留物体身份与轮廓，平均 2.3 秒把 TRELLIS.2 的 mesh 距离相对退化输入降低 61.5%。**</p>
+ **GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31222)
![architecture](https://img.shields.io/badge/GLOW-FM-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Arm_AI_Research_(AAIR),_Arm_Ltd-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GLOW-FM 用 Terminal Velocity Matching 在冻结 Tiny-VAE 潜空间做一步流匹配式低光增强，首次把 TVM 用于图像恢复，小变体仅需一次函数求值与 34 GFLOPs，并取得最优跨数据集泛化。**</p>
+ **R4DGS: Referring Segmentation in 4D Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30326)
![architecture](https://img.shields.io/badge/ReferGaussian-red)
![task](https://img.shields.io/badge/4D_Generation-magenta)
![organization](https://img.shields.io/badge/China_University_of_Geosciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://chenbangpu.github.io/R4DGS/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**R4DGS 首次把语言指代引入 4D 高斯泼溅：ReferGaussian 用 EntityBank 把动态高斯变成可语言寻址的实体，由 MLLM 分解查询并做约束感知定位，无需场景专属语义训练。**</p>
+ **One Evaluation Is Enough: Inversion-Free Image Editing with Trajectory Correction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30827)
![architecture](https://img.shields.io/badge/Endpoint-Calibrated_Transport-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/State_Key_Lab_of_CAD&CG,_Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ECT 用 VP 一步模型中「一次源-目标查询同时决定语义切向与端点位移」的对偶性，构造闭式、无反演、训练无关的图像编辑器：只需一个噪声水平、一次去噪 batch 与一次潜变量更新。**</p>
+ **A Unified Framework for Image-to-3D Part Generation via Variable Granularity**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31671)
![architecture](https://img.shields.io/badge/FlexPart-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Tongji_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Gucci233/FlexPart)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FlexPart 用门控自适应调制与非对称几何引导，在单个模型内统一稀疏点、边界框与掩码三种控制粒度，做可变粒度图像到 3D 部件生成，Part CD 相对 TripoSG+SAM3D 降低 16.6%。**</p>
