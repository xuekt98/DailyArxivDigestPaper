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

+ **MacroGS: Macro-Pixel Shared Gaussian Primitives for Arbitrary-Scale Light Field Super-Resolutio**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17957)
![architecture](https://img.shields.io/badge/MacroGS_Shared_Gaussian_Decoder-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Capital_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MacroGS 把生成单元从单视角像素换成宏像素，每个宏像素预测 K 个跨全部视角共享的高斯基元并逐基元建模视差，基元数由 UVKhw 降到 Khw，在五个基准的十个编码器-尺度设定中八个取得最高平均 PSNR。**</p>

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

+ **SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17821)
![architecture](https://img.shields.io/badge/SceneAgent_Multi_Agent_Scene_Generator-red)
![task](https://img.shields.io/badge/Scene_Generation-magenta)
![organization](https://img.shields.io/badge/Tencent-green)
[![project](https://img.shields.io/badge/project-blue)](https://xingyi-li.github.io/sceneagent/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SceneAgent 用规范化的 SceneContext 加后端适配器承载游戏场景构造，把人工确认轨迹蒸馏成不含资产 ID 的 Layout 与 Content 技能，在 GameSceneBench 的 69 条提示上对五个基线取得 78.2–89.4% 的平局校正偏好分。**</p>

+ **Vessel2Brain: Edge-Aware Multi-Scale Flow Matching for 3D Brain Image Generation from Vessel Masks**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17919)
![architecture](https://img.shields.io/badge/Vessel2Brain_Edge_Aware_FlowNet-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/School_of_Engineering_College_of_Engineering_and_Physical_Sciences_University_of_Birmingham-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Vessel2Brain 以条件流匹配从稀疏血管标注生成 3D 脑 MRI，边缘加权损失与粗分辨率辅助速度头共同保住血管对齐，在 CereVessMRA 上 SSIM 65.36%、PSNR 26.84、NMI 1.145、MAE 2.97%，四项均优于 GAN、VAE 与扩散基线。**</p>

+ **Analyzing Learning-Dynamics Across Loss and Prediction Choices for Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17967)
![architecture](https://img.shields.io/badge/Diffusion_Loss_Prediction_Theory-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/POSTECH-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文证明固定预测目标时改变损失空间等价于确定性的时间步重加权，并在 U-Net 与 JiT-B 上用瓶颈下界解释不同预测参数化在压缩比低于 1 时的数量级差距：CIFAR-10 上换用 ε-损失让 x-预测的 FID 从 11.79 降到 2.20。**</p>

+ **JaRS: Contrast-Free Localization of Memorized Regions in Diffusion Models via Jacobian Row Sums**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18024)
![architecture](https://img.shields.io/badge/JaRS_Jacobian_Row_Sum_Localization-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/Indian_Institute_of_Science-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**JaRS 用去噪器雅可比的行和而非对角元来定位扩散模型记忆区域，无需 null prompt 或历史 checkpoint；JaRS+ 在 SD v1.4 的 TV 与 TV+N 上取得 0.969 与 0.975 mIoU，在无条件 DiT-B/2 上把 All 设置从 0.666 提到 0.869。**</p>

+ **InfiHall-Bench: A Benchmark for Hallucination Evaluation in Autoregressive Text-to-Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18053)
![architecture](https://img.shields.io/badge/InfiHall_Bench_Confidence_Masking-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology_Shenzhen-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**InfiHall-Bench 用属性绑定、空间关系、动作关系、部件一致与场景一致五类技能系统组合出 411 条提示，平均每条 4.05 项技能；作者据此发现视觉自回归模型的幻觉呈尺度级持久性，并提出按置信度遮蔽的 CMHM 微调加以缓解。**</p>

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

+ **RecurIR: Learning When and How to Revise Restoration Policies via Recursive Self-Improvement**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18006)
![architecture](https://img.shields.io/badge/RecurIR_Recursive_Self_Improvement-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RecurIR 让图像复原智能体通过策略假设发现、规则证伪驱动的任务演化和条件化策略修订来自我改进，平均 PSNR 达 35.58 dB，比最强模型式基线 Defusion 高 2.00 dB，并把回滚率从 0.35 降到 0.12。**</p>

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

