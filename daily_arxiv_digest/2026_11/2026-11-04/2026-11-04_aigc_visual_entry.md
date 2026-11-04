# 2026-11-04 - AIGC 视觉生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04303)
![architecture](https://img.shields.io/badge/Flow_Based_Training_Free_IIMT-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Institute_of_Trustworthy_Embodied_AI_Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**免训练的图内机器翻译框架 FlowTranslator：把 T2I 的多语言文字生成迁移到图内翻译，靠区域噪声解耦与编辑位移放大两条轨迹控制，在 EasyOCR 回读协议下取得 PRIM BLEU 20.6、COMET 57.2，整图译为中文精确匹配 40.1%，优于训练型基线 UniTranslator。**</p>
+ **Pixel-space video generation with U-JiT**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04764)
![architecture](https://img.shields.io/badge/U_Shaped_Pixel_Space_Video_Transformer-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/FAIR_Meta-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**像素空间视频生成模型 U-JiT：在 Kinetics-600 上从头对照训练潜空间与像素空间方案，128 分辨率 frames-to-video 的 FVD 相对先前 SOTA 改善 27%、相对 JiT 像素基线改善 14%，256 分辨率 per-frame FID 相对潜空间改善 27%、相对像素模型改善 61%。**</p>
+ **FlowRig: Unified Skeleton Generation for 3D and 4D Meshes via Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03775)
![architecture](https://img.shields.io/badge/Flow_Matching_3D4D_Skeleton_Generator-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Texas_A&M_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://tamu-visual-ai.github.io/FlowRig/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**统一 3D/4D 骨骼生成的 FlowRig：基于 flow matching 模板无关建模，单次前馈输出整段时间对齐的骨架，支持显式骨骼数控制、不确定性估计与掩码式插值预测，并用 3D 到 4D 课程学习缓解配对数据稀缺，静态任务上超过全部基线。**</p>
+ **Efficient and Faithful High-Resolution Image Editing with Sparse Cross-Resolution Denoising**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04416)
![architecture](https://img.shields.io/badge/Sparse_Cross_Resolution_HighRes_Editor-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Shanghai_Innovation_Institute-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/FDUPeter/FLASH)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**原生高分辨率指令编辑模型 FLASH：用稀疏跨分辨率去噪在同一个 Transformer 内兼顾 1K 语义锚定与目标分辨率细节重建，在 VINS-4KEval 上 2K/4K 结构保真最强，4K 前向总执行快 4.2 倍、attention 快 25.3 倍，渐进推理再降 30.5% 端到端延迟。**</p>
+ **ScoreDial: Precise Control of Visual Attributes in Image Generation via Regressor Guidance from Limited Human Ratings**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05004)
![architecture](https://img.shields.io/badge/Regressor_Guided_Attribute_Control-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Keio_University_Japan-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Kamijo-Gen/ScoreDial)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**属性数值可控生成框架 ScoreDial：先用 100–479 张人工评分图拟合可微回归器 R，把请求值定义在 R 刻度上并用误差自适应引导持续修正偏差，四个属性统一设置下 R-MAE 不超过 0.013、Spearman ρ=0.980，15 人盲评线性 R² 达 0.665 与 0.786。**</p>
+ **What Remains in Sight? Autoregressive Video Decoding as Representation-Guided Context Rewriting**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04164)
![architecture](https://img.shields.io/badge/Representation_Guided_Context_Rewriting-red)
![task](https://img.shields.io/badge/Autoregressive_Video_Generation-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/lixuan27/ReCR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**免训练的长视频解码策略 ReCR：把给解码器看哪段历史变成显式的测试期决策，用内部表征按效用、边界覆盖与冗余度挑选上下文单元，在匹配可见 token 预算下跨多种自回归骨干稳定提升，30 秒与 60 秒 rollout 平均涨 1.41 与 1.94 分。**</p>
+ **Phase-DGS: Phase-guided Dynamic Gaussian Splatting from Unsynchronized Multi-view Video**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04666)
![architecture](https://img.shields.io/badge/Phase_Guided_Dynamic_Gaussian_Splatting-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Electronics_and_Telecommunications_Research_Institute_ETRI_Daejeon_Republic_of_Korea-green)
[![project](https://img.shields.io/badge/project-blue)](https://oc-dev74.github.io/Phase-DGS/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**非同步多视角视频的动态高斯重建框架 Phase-DGS：用运动周期中的语义相位替代绝对时间戳，使同一运动状态的帧跨相机自然建立时空对应，在时间偏移、丢帧与相机冻结下最高提升 +8.5 dB PSNR，并可接入现有 4DGS 骨干。**</p>
+ **3DGS-VBench+ and 3DGSV-Assessor: A Multi-Dimensional Subjective Benchmark and a Reference-Flexible Objective Model for 3D Gaussian Splatting Video Quality Assessment**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04498)
![architecture](https://img.shields.io/badge/LMM_3DGS_Quality_Assessor-red)
![task](https://img.shields.io/badge/3D_Gaussian_Splatting_Rendering-magenta)
![organization](https://img.shields.io/badge/School_of_Information_Science_and_Electronic_Engineering_Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/YukeXing/3DGSV-Assessor)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向压缩 3DGS 的主观质量基准 3DGS-VBench+ 与评测模型 3DGSV-Assessor：3036 个重建、11 个真实加 22 个合成场景、9108 个整体与几何与颜色 MOS，评测器单次生成同时给三个维度打分，并支持有参考与无参考两种设定。**</p>
+ **CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04244)
![architecture](https://img.shields.io/badge/Physics_Grounded_Sketch_To_Video-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Science_Ho_Chi_Minh_City_Vietnam-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**物理接地的反事实草图视频框架 CounterSketch：把自然语言 What if 查询转成场景图更新、连续轨迹与约束校验，再用验证过的轨迹引导草图合成；在 80 问的 CounterSketchBench 上，物理轨迹比 VLM 直出带来更强运动引导。**</p>
+ **IGSW: Multi-Weather Urban Scene Reconstruction with Intrinsic-Decoupled Gaussian Splatting**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04374)
![architecture](https://img.shields.io/badge/Intrinsic_Decoupled_Weather_4D_Gaussian-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/College_of_Mechanical_and_Vehicle_Engineering_Chongqing_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://akaxi6.github.io/IGSW/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多天气城市场景重建框架 IGSW：先做本征解耦的 4D 高斯建模把外观拆成天气共享与天气特有成分，再用结构保持门控抑制扩散教师图的结构错误，在 nuScenes 与 Waymo 上取得最高内容相似度与最低时序误差，nuScenes 雨天 Ewarp 仅 0.0021。**</p>
