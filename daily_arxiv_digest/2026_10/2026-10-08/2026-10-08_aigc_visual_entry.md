+ **SGF+: Decoupling Gradient Flows for Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10429)
![architecture](https://img.shields.io/badge/Self_Gradient_Forcing-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/1Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频生成需要一边对当前帧去噪、一边把它们的关键-值表示写成后续预测的上下文。这两个角色通常共用参数，作者发现它们的梯度呈现不同模式并存在系统性负对齐，妨碍视觉质量与时序一致性的联合优化。**</p>

+ **Real-Time Joint Audio-Video Generation by Parallel Adapter Composition**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10343)
![architecture](https://img.shields.io/badge/Parallel_Adapter_Composition-red)
![task](https://img.shields.io/badge/Joint_Audio_Video_Generation-magenta)
![organization](https://img.shields.io/badge/LIGHTSPEED-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把联合音视频扩散 transformer 部署成实时交互生成需要两项改造：块自回归注意力（帧能在整段生成完成前输出）与少步采样（让每块足够便宜）。链式流水线按顺序获得这两项能力，但每一步都在微调上一步的权重，后一个目标可以撤销前一个能力；本文改为并行获得。**</p>

+ **QuadTok: Quadtree Visual Tokenizer for Autoregressive Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10497)
![architecture](https://img.shields.io/badge/QuadTok_Quadtree_Tokenizer-red)
![task](https://img.shields.io/badge/Autoregressive_Image_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_California,_San_Diego-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**QuadTok 提出层次化四叉树结构来做视觉 tokenization 与自回归图像生成，在 2D 空间绑定与 1D 序列灵活性之间架桥。tokenizer 会把表示容量动态分配给视觉复杂区域，而同质区域只占少量预算。**</p>

+ **ORCA: Hunting Compositional Failures in Text-to-Image Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09841)
![architecture](https://img.shields.io/badge/Compositional_Failure_Analysis-red)
![task](https://img.shields.io/badge/Text_To_Image_Generation-magenta)
![organization](https://img.shields.io/badge/1Wellcome_Sanger_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**文生图扩散模型在组合提示上可预测地失败：属性绑到错误物体、空间关系反转、多物体场景丢计数。现架构已用 T5 编码器补强 CLIP（因为 CLIP 的对比嵌入丢失组合结构），但这些失败仍在。作者主张绑定问题不是信息缺失而是对齐错位。**</p>

+ **GRACE: Generation-aware latent compression for efficient video generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10524)
![architecture](https://img.shields.io/badge/Generation_Aware_Latent_Compression-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/1KAIST_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**高压缩比视频自编码器能加速视频扩散模型（DiT 处理的 token 少得多），但这类自编码器难训练：压缩比越高重建质量越差，补回来需要更多通道，而这已知会拖慢 DiT 收敛。压缩后的 latent 也与 DiT 所熟悉的分布不同。**</p>

+ **Visual Jev Rewards: Reference-Bound Verification for Multi-Subject Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09328)
![architecture](https://img.shields.io/badge/Reference_Bound_Visual_Rewards-red)
![task](https://img.shields.io/badge/Multi_Subject_Image_Generation-magenta)
![organization](https://img.shields.io/badge/School_of_Artificial_Intelligence,_Beijing_University_of_Posts_and_Telecommunications1-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多主体图像生成需要奖励去验证所请求的属性、动作与关系是否真的在指定参考主体上成立。主体出现本身并不能证明正确的主体参与了所请求的交互。作者提出参考绑定的 Visual Jev 奖励，把这些视觉判断转成生成器的训练信号。**</p>

+ **Position Forcing: Self-Conditioning 3D Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10342)
![architecture](https://img.shields.io/badge/Self_Conditioning_3D_Generation-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/1VCIP,_Nankai_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**近期单阶段 3D 生成模型普遍用 VecSet 表示，把 3D 形状编码成无序的潜 token 集合。相比提供显式位置引导的两阶段方法，这类模型必须在去噪过程中隐式推断 token 位置，限制了生成质量。作者观察到：尽管没有显式位置条件，VecSet token 仍保留可恢复的位置信息。**</p>

+ **MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.10457)
![architecture](https://img.shields.io/badge/Cache_Reuse_Offline_To_Online_RL-red)
![task](https://img.shields.io/badge/Video_Diffusion_Acceleration-magenta)
![organization](https://img.shields.io/badge/1Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频 DiT 的迭代去噪带来高推理延迟，缓存利用步间冗余成为有效加速手段。现有动态缓存方法通常在每一步估计缓存复用会引入的误差（步误差）来指导决策。这篇用离线到在线强化学习做自适应缓存复用。**</p>

+ **DeltaSplat: Iterative Gaussian Refinement for Pose-Free Feed-Forward 3D Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09853)
![architecture](https://img.shields.io/badge/Iterative_Gaussian_Refinement-red)
![task](https://img.shields.io/badge/Feed_Forward_3D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/1Department_of_Electrical_and_Computer_Engineering,_Sungkyunkwan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**无位姿前馈 3DGS 从稀疏无位姿图像单次网络前向重建场景，免去相机标定与逐场景优化。但相机估计误差会传播进预测的 Gaussian，并与单次预测的几何与光度误差复合。DeltaSplat 用轻量的迭代 Gaussian 精化来纠正。**</p>

+ **TileSkipper: Region-Adaptive Tile Pruning for 3D Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.09343)
![architecture](https://img.shields.io/badge/Region_Adaptive_Tile_Pruning-red)
![task](https://img.shields.io/badge/3D_Gaussian_Splatting_Rendering-magenta)
![organization](https://img.shields.io/badge/School_of_Electrical,_Computer_and_Energy_Engineering-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**分块 3DGS 光栅化器通常对 tile 枚举使用一个全场景统一的贡献截断阈值，尽管不同内容对其截断的敏感度不同。TileSkipper 为冻结的 checkpoint 选择一套静态的逐 Gaussian 截断策略。**</p>

