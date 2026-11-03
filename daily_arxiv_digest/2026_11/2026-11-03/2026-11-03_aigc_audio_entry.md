# 2026-11-03 - AIGC 音频生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Zero-Shot Voice Cloning for Synthetic Data Augmentation in Children's ASR**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03050)
![architecture](https://img.shields.io/badge/Zero_Shot_Voice_Cloning_ASR_Augmentation-red)
![task](https://img.shields.io/badge/Voice_Cloning-magenta)
![organization](https://img.shields.io/badge/Fraunhofer_Institute_for_Digital_Media_Technology_IDMT-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该研究用零样本音色克隆 TTS 从两个儿童语料合成至多 1.6 万条童声，用来微调 Whisper-small：ENNI 上 WER 从 19.8% 降到 16.4%，合成加真实混合达到 9.2%，与真实数据微调的 8.8% 几乎持平。**</p>
+ **Spatial Transfusion: From Structured Spatial Scene Understanding to Generation and Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02330)
![architecture](https://img.shields.io/badge/Flow_Matching_FOA_Spatial_Audio_Generator-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://microsoft.github.io/spatial-transfusion/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Spatial Transfusion 把预训练空间音频理解模型扩展成首阶 ambisonics 的生成与编辑统一框架，用 VAE 潜空间的流匹配加模态路由 LoRA，生成 FAD-PSELD 从全量微调的 3.82 降到 0.964，编辑 EditFLAM 达 17.8 并保留原空间理解能力。**</p>
+ **High Frequency Safeguard and Weighted Objective Scoring Bandwidth Extension**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02235)
![architecture](https://img.shields.io/badge/Dual_Stream_Swin_BWE_With_HF_Discriminators-red)
![task](https://img.shields.io/badge/Speech_Bandwidth_Extension-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HFSWO 用紧凑的复频谱 Swin 双流对抗框架做语音带宽扩展，并新增高频保护判别器与加权目标评分判别器直接约束高频能量的位置与频谱形态，在 VCTK 英文与 MLS 法文上以少 74.6% 参数、少 63.6% MACs/FLOPs 超过 AP-BWE 基线。**</p>
+ **Q-BWE: Quantum Chaos-Informed Speech Bandwidth Extension**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02250)
![architecture](https://img.shields.io/badge/Quantum_Chaos_Discriminator_BWE-red)
![task](https://img.shields.io/badge/Speech_Bandwidth_Extension-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Q-BWE 用五量子比特 Quantum Chaos Discriminator 建模非线性特征间的联合交互，从 26 维语音动力学特征库中自动选出 5 个送入可训练 CNOT 的数据重上传线路，产出 31 维状态矢量测量，并让生成器参数量比 CIS-BWE 基线少约 1.72 倍。**</p>
+ **A Compact Statistical View of Musical-Instrument Directivity**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02927)
![architecture](https://img.shields.io/badge/Statistical_Directivity_Descriptor_Compression-red)
![task](https://img.shields.io/badge/Instrument_Directivity-magenta)
![organization](https://img.shields.io/badge/Politecnico_di_Milano-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇工作提出以统计描述子压缩乐器随频率变化的指向性图案，在 41 件管弦乐器、四阶 30 频带的语料上把双精度存储从约 492 kB 压到约 100 kB，同时较好保留距离几何，为空间音频渲染与声场仿真提供可跨乐器比较的中间表示。**</p>
+ **Ananas: A Networked Audio System for Distributed Spatial Audio Applications**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03077)
![architecture](https://img.shields.io/badge/Networked_Nanosecond_Sync_Spatial_Audio_System-red)
![task](https://img.shields.io/badge/Audio_Generation-magenta)
![organization](https://img.shields.io/badge/Inria-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Ananas 是一套面向空间音频的网络化系统：用 Faust 编程的低成本微控制器开发板，经 IEEE 1588 精密时间协议做到纳秒级同步，配合 DAW 控制工具，并以多播 UDP 实现媒体时钟与呈现时间恢复，可模块化扩展到波场合成与高阶 ambisonics。**</p>
+ **VidDub: Replacement-Aware Distillation for Two-Step Video Dubbing**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03404)
![architecture](https://img.shields.io/badge/Replacement_Aware_Two_Step_Dubbing_Editor-red)
![task](https://img.shields.io/badge/Audio_Visual_Editing-magenta)
![organization](https://img.shields.io/badge/HKUST-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/LAW1223/VidDub)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VidDub 提出替换感知的跨音频监督：成对音频用全帧重建，替换音频则屏蔽源嘴部重建损失、只靠音视同步监督嘴部，并把全上下文扩散编辑器蒸馏到两步，在三个随机种子上把跨音频 Sync-C 提升 0.833。**</p>
+ **ReplayFactor: Replay-Aware Dual-Attribute Learning for Practical Speech Deepfake Detection**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02628)
![architecture](https://img.shields.io/badge/SSL_Acoustic_Prior_Replay_Deepfake_Detector-red)
![task](https://img.shields.io/badge/Speech_Deepfake_Detection-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ReplayFactor 针对物理重放这一低成本威胁，把自监督表征与声学先验融合做双属性判别，并用多任务与监督对比学习提升泛化；在 EchoFake 开集上宏 F1 从 60.99% 提到 76.44%、EER 从 11.86% 降到 3.05%，并公开约 18.5 万条中文重放语料。**</p>
+ **A Human-Verified AI Workflow for Annotating Environmental Sound Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03271)
![architecture](https://img.shields.io/badge/Human_Verified_AST_Annotation_Workflow-red)
![task](https://img.shields.io/badge/Audio_Evaluation-magenta)
![organization](https://img.shields.io/badge/Strathmore_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该工作记录了一套人机协同的环境声标注流程：微调 AST 在 Person talking 二分类上达 89.36% 准确率，低于 95% 自治标注阈值遂转为人工核验，核验 2337 条零误报、每条约 4.2 秒，把剩余队列工时从 48.9 人时降到 28.9 人时。**</p>
+ **CrowdForge: Effects of Audio and Visual Audience Participation Modalities on Agency, Collaboration, and Engagement in AI-Mediated MR Performances**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03389)
![architecture](https://img.shields.io/badge/Audience_Co_Controlled_Generative_Music_System-red)
![task](https://img.shields.io/badge/Music_Generation-magenta)
![organization](https://img.shields.io/badge/SolJAMM_Research_and_ATLAS_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CrowdForge 让观众在 AI 生成音乐与 MR 虚拟环境中共同投票控制演出，在音频、视觉、音视三种交互条件的现场研究（N=19）中观察到可观测性才是掌控感的主要来源，而音频参数提供宏观结构控制并与乐手形成对抗性张力。**</p>
