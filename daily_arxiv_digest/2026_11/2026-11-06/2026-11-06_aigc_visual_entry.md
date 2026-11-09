# 2026-11-06 - AIGC 视觉生成与编辑 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **WeLM-Image: A Unified Image Generation Model towards Visual Intelligence**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07392)
![architecture](https://img.shields.io/badge/WeLM_Image_MoT_MoE-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/WeChat_Vision_Tencent_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**腾讯微信视觉团队提出 WeLM-Image，用 Mixture-of-Transformers 骨干把多模态理解与文生图、指令编辑、多参考合成统一进一条交错序列，并以 MoE 稀疏激活把 31.7B 参数压到每 token 约 5.4B。**</p>
+ **Generator-Aligned Reward Modeling with Target-Aware Bounded Optimization for Visual Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07648)
![architecture](https://img.shields.io/badge/GARM_TABO_TA_GRPO-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/China_Telecom_TeleAI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把奖励建模与奖励强度控制拆成两步：GARM 用生成器原生锚点匹配真实数据分布并引入内容匹配的真实对比样本，TABO 用真实正例标定平滑上界奖励函数，TA-GRPO 再以固定分阶段优势缩放保住目标感知尺度，同时适用于直接奖励梯度与策略优化两类更新方式。**</p>
+ **FewStepRL: Fine-tuning Few-step Diffusion Models with Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08240)
![architecture](https://img.shields.io/badge/FewStep_RL_Three_Phase_Adapter-red)
![task](https://img.shields.io/badge/Few_Step_Generation-magenta)
![organization](https://img.shields.io/badge/Tencent_Hunyuan-green)
[![project](https://img.shields.io/badge/project-blue)](https://fewsteprl.page)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对少步扩散模型建模区间平均速度、而现有 RL 目标假设瞬时速度这一错配，论文给出变换、分解、适配三阶段流程，把每个目标的梯度拆成朝参考的自回归项与奖励增广项，并在一个代码库里统一实现 FlowGRPO、AWM、DiffusionNFT、DiffusionOPSD 与 ReFL 的少步版本。**</p>
+ **Householder Motion Embedding: Noise Modulation for Motion-Controllable Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07294)
![architecture](https://img.shields.io/badge/Householder_Motion_Embedding-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/The_Australian_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Householder 运动嵌入把运动信号编码成一串通道空间正交反射，在构造上精确保持每帧噪声的高斯结构，从而免去噪声扭曲方法所需的 Jacobian 分布校正；默认 K=2 时噪声处理 2.80 ms/latent，比 GWTF 快 2.7 倍、比 HIWYN 快 13.6 倍，额外峰值显存仅 0.5-6 MB。**</p>
+ **ArtiVidRM: Verifiable Artifact-as-Rubric Reward Modeling for Explicit Quality Articulation in Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07301)
![architecture](https://img.shields.io/badge/ArtiVidRM_Observe_Then_Score-red)
![task](https://img.shields.io/badge/Reward_Model_Video-magenta)
![organization](https://img.shields.io/badge/Southeast_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ArtiVidRM 用「先观察后打分」范式把视频奖励模型的可解释性做实：先识别可见生成伪影并组织成结构化清单，再以这些伪影为显式评分依据，配合联合优化伪影预测与成对偏好的多目标强化学习，标注流水线从 22,640 对视频偏好样本出发并由接地复核剔除 26.8% 幻觉候选。**</p>
+ **Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07551)
![architecture](https://img.shields.io/badge/PreSTP_Token_Pruning-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PreSTP 指出少步自回归视频扩散的冗余主要来自跨帧共享的静态内容与去噪早期即已收敛的 token，并利用模型自身去噪轨迹上的早期干净估计在线构建统一的 token 级冗余掩码，免训练即可剪枝计算，在 5 秒生成上取得 1.52-3.20 倍加速且画质损失极小。**</p>
+ **ArtCrafter: Feed-Forward Generation of Articulated 3D Object with Analytic Joint Derivation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07658)
![architecture](https://img.shields.io/badge/ArtCrafter_Triplet_Attention-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Qualcomm_AI_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ArtCrafter 从一对「静息态＋张开态」图像前馈生成铰接 3D 资产：以 1+2N 个槽位联合去噪两种状态的部件网格，用 Triplet Attention 强制跨状态几何一致并以排斥损失避免部件互穿，最后由配对网格的刚体变换解析反推 URDF 的关节类型、轴、原点与行程。**</p>
+ **Bri3D: Bridging the Object-Scene Gap in Single-Image 3D Generation via Scene-Anchor**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07961)
![architecture](https://img.shields.io/badge/Bri3D_Scene_Anchor-red)
![task](https://img.shields.io/badge/Scene_Reconstruction-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology_Guangzhou-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Bri3D 用实例感知的体素场景锚点搭桥单图到复合 3D 场景：先预测编码粗几何与空间排布的颜色化场景脚手架，再把每个实例细化为保位姿、兼容冻结先验的体素支撑，最后交给冻结的物体生成器合成带纹理的细节几何，在 3D-FRONT 上把场景级 Chamfer 距离降到 0.87。**</p>
+ **StitchEdit: Stitching Depth Priors into Image Editors via Per-Layer Gradient Probing**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07922)
![architecture](https://img.shields.io/badge/StitchEdit_Gradient_Probing-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://guoqincode.github.io/StitchEdit/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**StitchEdit 通过逐层梯度探针发现深度与编辑目标在早期层相容、晚期层冲突，据此把深度 LoRA 分层处理：相容层全速训练、过渡层用余弦倍率降学习率、冲突层直接剪除适配器，在自建的 150 例 StitchEditBench 上同时提升几何一致性与感知质量。**</p>
+ **IDPrior: Decoupling Identity Generation from Facial Image Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07941)
![architecture](https://img.shields.io/badge/IDPrior_Diffusion_Prior-red)
![task](https://img.shields.io/badge/Identity_Preservation-magenta)
![organization](https://img.shields.io/badge/Fraunhofer_Institute_for_Computer_Graphics_Research_IGD-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/fdbtrs/IDperturb)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**IDPrior 把身份生成与人脸图像合成解耦：先在人脸识别模型的嵌入空间学一个覆盖真实身份分布的扩散先验并据此生成新身份嵌入，再用它条件化预训练的身份可控扩散模型，使同一身份的多种图像可被合成，兼顾身份多样性与分布真实性。**</p>
