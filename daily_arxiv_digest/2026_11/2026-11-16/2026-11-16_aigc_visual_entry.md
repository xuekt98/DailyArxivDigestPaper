<!-- direction: aigc_generation -->

+ **Learning Anisotropic Prediction Targets for Flow Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17767)
![architecture](https://img.shields.io/badge/AnisoFlow_Target-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://hanshengchen.com/anisoflow)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AnisoFlow 把 flow 模型的预测目标本身变成可学习的各向异性正半定算子，用闭式映射精确还原速度，架构与采样器不变，ImageNet 256×256 的 JiT-H/16 FID 由 1.90 降到 1.55，像素空间 T2I 的 HPSv3 与 COCO-10k 同步提升，8-bit 推理下消除 patch 接缝。**</p>

+ **Speed-Variation Distillation for Generative Modeling**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17868)
![architecture](https://img.shields.io/badge/Diversification_Operator-red)
![task](https://img.shields.io/badge/Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/VISTEC_Thailand-green)
[![project](https://img.shields.io/badge/project-blue)](https://speed-variance-modeling.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Speed-Variation Distillation 先用生成先验做图像 morphing，把多样图像沿 50 步轨迹收缩到共享原型，再把这段反向过程蒸馏成多样化算子，使推理全程每一步都输出可识别图像，从而支持提前终止并显式控制速度与多样性的折中。**</p>

+ **Finite speed Ornstein-Uhlenbeck-Kac processes and their applications in generative modeling**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17625)
![architecture](https://img.shields.io/badge/OU_K_Flow_Model-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Institute_of_Mathematics_Technische_Universität_Berlin-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把 Ornstein-Uhlenbeck 过程的布朗驱动换成有限速率的 Kac 过程，用 Riemann 方法写出时非齐次 Kac 过程的显式分布（两个 Legendre 多项式），据此在 PDMP 框架下推导概率流速度场并构造 OU-K 生成模型，消除了扩散模型所需的时间截断。**</p>

+ **Creative Product Design under Brand Image Constraints**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17762)
![architecture](https://img.shields.io/badge/Brand_Survey_Self_Enhancement-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/TOYOTA_CENTRAL_R&D_LABS._INC.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把品牌印象当作工业设计中的隐式约束，先用 Deep Research 自动生成品牌调查报告并从中提炼创作方向，再把方向注入「生成—批判—改写提示词」的自增强闭环，在 5 类 50 个产品上用 VLM-as-Judge 权衡创新性与品牌可识别性。**</p>

+ **Training-Free Acceleration of Multi-View 3D Transformers via Regime-Aware Attention Approximation**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17629)
![architecture](https://img.shields.io/badge/RAWATTA-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文实测多视图 3D transformer 的全局注意力只有平均、匹配与锚定三种角色，据此提出免训练的 RAWATTA：按角色套用不同近似算子，注意力跑 8-bit、只在必要层保留 16-bit，在 12 GB 显卡上把 VGGT-Ω 加速 2.08 倍而位姿精度只掉约一点。**</p>

+ **Stage-wise Lineage-aware Dropout for Sparse-View 3D Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17752)
![architecture](https://img.shields.io/badge/Stagewise_Lineage_Dropout-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Hefei_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出「血统家族」概念刻画由克隆或分裂产生的 Gaussian 族群，用分阶段的族级 dropout 替代单点 dropout 抑制稀疏视角 3DGS 过拟合，并用族级平衡稠密化重分配预算，在 LLFF、MipNeRF360 与 Blender 上取得有竞争力的重建指标。**</p>

<!-- direction: aigc_editing -->

+ **Open-World Scene Deocclusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17695)
![architecture](https://img.shields.io/badge/Layered_Amodal_Deocclusion-red)
![task](https://img.shields.io/badge/Inpainting-magenta)
![organization](https://img.shields.io/badge/Victoria_University_of_Wellington-green)
[![project](https://img.shields.io/badge/project-blue)](https://sashjk.github.io/owsd/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出免训练的开世界场景去遮挡框架，从单张 RGB 图中检测或指定目标物体，按深度顺序拆成 RGBA 层，逐层用扩散模型补全被遮挡部分，并以边界连续、颜色保真等四种子分数迭代收敛，输出可组合的图层。**</p>

+ **HarmonyText: Harmonious Scene Text Editing via Reverse-to-Refined Pair Synthesis and Region-Decoupled Frequency Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17733)
![architecture](https://img.shields.io/badge/Region_Decoupled_Frequency_Learning-red)
![task](https://img.shields.io/badge/Instruction_Editing-magenta)
![organization](https://img.shields.io/badge/South_China_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HarmonyText 用反向合成构造 25K 对场景文字编辑伪配对数据 STE25K，再以区域解耦优化区分编辑区与保留区的监督，用级联小波域高频引导保住字形边缘，并在 500 张评测图上提出颜色分布散度与和谐度两个免真值指标。**</p>

+ **Real-Time Diffusion Relighting as a Neural Sensor: Closing the Low-Light Domain Gap for Robotic Perception**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17438)
![architecture](https://img.shields.io/badge/Async_Generative_Neural_Sensor-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/University_of_Maryland_College_Park-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把扩散重光照包装成嵌入控制回路的生成式神经传感器，用检测置信度滞回触发后台线程异步增强：ExDark 上 mAP 87.1%，CARLA 闭环导航碰撞率从 32.75% 降到 21.44%，同时 GPU 占用由 95.0% 降到 0.4%。**</p>

<!-- direction: aigc_rl -->

+ **Rethinking Visual Reasoning in Text-to-Image Reward Modeling**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17585)
![architecture](https://img.shields.io/badge/CrossPairs_Reward_Model-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ssu53/crosspairs-rm)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文发现 T2I 奖励模型在偏好微调后会牺牲视觉理解，于是提出 CrossPairs：保留同一张图像、只翻转提示词，把现有视觉推理评测集转成偏好对与人类偏好数据混合训练，在 GenEval 上带来 4.0% 与 5.5% 的平均提升。**</p>

