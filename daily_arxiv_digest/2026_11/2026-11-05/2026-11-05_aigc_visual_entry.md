# 2026-11-05 - AIGC 视觉生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Context-Aware Autoregressive Image Generation for Emerging Reasoning Properties**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06838)
![architecture](https://img.shields.io/badge/Context_Aware_Autoregressive_Decoding-red)
![task](https://img.shields.io/badge/Autoregressive_Generation-magenta)
![organization](https://img.shields.io/badge/Johns_Hopkins_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Hpesojyjx/Saccades-AR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出上下文感知的自回归图像生成，模型依据全局上下文动态决定下一个 token 的位置。GenEval 总通过率在 MaskGen-XL 上由 56.22% 提升到 59.99%，2000 条长提示基准平均分也提高约 0.5 分。**</p>
+ **NextGAN: Towards Simple and Scalable GAN Training for Image and Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06270)
![architecture](https://img.shields.io/badge/Displacement_Supervised_Adversarial_Critic-red)
![task](https://img.shields.io/badge/Few_Step_Generation-magenta)
![organization](https://img.shields.io/badge/Westlake_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/LINs-lab/NextGAN.git)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 NEXTGAN，用参考特征与生成特征的位移监督标量 critic 的输入梯度，等价于带梯度能量惩罚的对抗目标。ImageNet 一步 FID 达 1.54（对抗式 1.36），文本生成视频两步 VBench 总分 83.13。**</p>
+ **TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06741)
![architecture](https://img.shields.io/badge/Trajectory_Tail_Steering-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/MMLab_CUHK-green)
[![project](https://img.shields.io/badge/project-blue)](https://lyricccco.github.io/tailsteer/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出尾舵式的最终阶段训练框架，只在去噪轨迹尾部学习保持校正，并从编辑器自身的 on-policy 轨迹中取监督。在 FLUX、SenseNova、Qwen 四个骨干上，15-20 轮连续编辑的累积漂移大幅下降。**</p>
+ **DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05917)
![architecture](https://img.shields.io/badge/Decoupled_Sparse_Attention-red)
![task](https://img.shields.io/badge/Diffusion_Acceleration-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Urbana-Champaign-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出解耦稀疏注意力范式：语义簇补偿每一个 key，精确注意力只在离线按位置固定的少数块上纠错。10 个模型上平均 PSNR 30.02 dB、加速 1.31×，训练无关且零额外损失。**</p>
+ **CrossPressor: Scalable Cross-View Fusion for Feed-Forward 3D Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06258)
![architecture](https://img.shields.io/badge/Coverage_Cycled_Evidence_Routing-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Graz_University_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://yuhsihu.github.io/CrossPressor)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出免训练的可扩展 anchor 融合方法，用覆盖循环的证据路由把不断增长的支撑视角分摊到各融合层。256 视角下跨视角融合加速 26.12×、端到端 1.43×，p5 ΔPSNR 仅 -0.0063 dB。**</p>
+ **NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06377)
![architecture](https://img.shields.io/badge/Cluster_Residual_KV_Codec-red)
![task](https://img.shields.io/badge/KV_Cache_Compression-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://jiacheng-lu03.github.io/NanoKV/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出面向生成感知的自回归视频 KV 压缩框架，簇中心保存共享内容、头通道残差编码成低位系数，并按 Key 与 Value 的不同角色分别拟合。HY-WorldPlay 上有效压缩 26.09× 且 PSNR 提升 1.0 dB。**</p>
+ **Chronos: Sequential Identity-Preserving Video Generation by Temporal Anchoring**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05893)
![architecture](https://img.shields.io/badge/Temporal_Anchoring_Identity_Routing-red)
![task](https://img.shields.io/badge/Identity_Preservation-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出免训练的身份保持视频生成框架，用语义提示锚定、视觉帧锚定和度量引导候选路由统一单段人脸与多段动作生成。拿下 ACM MM 2026 挑战赛 Track 1 与 Track 2 双第一，总分 0.6769 与 0.6102。**</p>
+ **Quo Vadis, Driving Scene Reconstruction? Occlusion-Aware Gaussian Densification**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06273)
![architecture](https://img.shields.io/badge/Occlusion_Aware_Gaussian_Densification-red)
![task](https://img.shields.io/badge/Scene_Reconstruction-magenta)
![organization](https://img.shields.io/badge/AITech_Lab._Ho_Chi_Minh_City_University_of_Technology_HCMUT-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出前馈式的驾驶场景重建框架，针对被遮挡区域直接预测新的高斯基元补齐几何。nuScenes 验证集上 PSNR 达 23.50，比 DrivingForward 高 1.74 dB，LPIPS 从 0.194 降到 0.182。**</p>
+ **EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06748)
![architecture](https://img.shields.io/badge/Brain_Renderer_Collaboration-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 Out-of-Sight Causal Evolution 问题与对应方案 EvoWorld，由视觉语言模型充当世界大脑维护状态并推理后果，段自回归渲染器负责视觉实现。基准上核心任务成功率 90.8%，领先次优基线 69.1 个百分点。**</p>
+ **DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05825)
![architecture](https://img.shields.io/badge/Role_Addressed_Dual_Image_Conditioning-red)
![task](https://img.shields.io/badge/Multi_Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/State_Key_Lab_of_CAD&CG_Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出角色寻址的双图条件视频生成框架，把商品图与人物图分别编码后分置 DiT 序列首尾，并配合区域加权损失与条件 dropout。11 项指标平均排名 1.73，人脸一致性 0.8517，训练集为 1 万条电商视频。**</p>
