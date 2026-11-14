<!-- direction: aigc_generation -->

+ **Back to Pixels: Lifting Latent Video Diffusion into Pixel Space**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17336)
![architecture](https://img.shields.io/badge/PixVid_Pixel_Space_Video_Diffusion-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Roblox-green)
[![project](https://img.shields.io/badge/project-blue)](https://chenshuo20.github.io/PixVid/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PixVid 把预训练的视频潜扩散模型搬回像素空间，用卷积头逐帧渲染 DiT 输出，仅用约 1.3M 训练片段微调即在 VBench 拿到 84.78 分，并以相同的每帧 token 数生成 960×1664 高分辨率视频。**</p>

+ **UniSpark: Exploring Hybrid Attention for Multimodal Understanding and Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16517)
![architecture](https://img.shields.io/badge/UniSpark_Hybrid_Attention_MoT-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Lucaria_Academy-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UniSpark-9B 用 Mixture-of-Transformer-Experts 骨干混合全注意力与 GatedDeltaNet 线性注意力，视觉分支走 flow matching，以 1.597 亿生成样本与 2.134 亿理解样本训练出 MME-S 2470.3、GenEval 0.83 的多模态统一模型。**</p>

+ **TokenStream: Multi-Subject Personalized Video Generation with Token-wise LoRA and Guided Attention**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16897)
![architecture](https://img.shields.io/badge/TokenStream_Token_Wise_LoRA-red)
![task](https://img.shields.io/badge/Multi_Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TokenStream 用 token-wise LoRA 把每个主体的低秩更新限制在其文本 token 的交叉注意力 value 投影上，配合冻结基模型的引导注意力流，在 30 主体 122 条 prompt 的 Multi-DB 上把身份保持从 0.422 提升到 0.467。**</p>

+ **K2V: Generative Keyframing For Physically Plausible Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17324)
![architecture](https://img.shields.io/badge/K2V_Generative_Keyframing-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Cambridge-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**K2V 把物理推理从扩散采样中卸载给 LLM 驱动的关键帧生成模块，视频模型只负责在物理正确的关键帧之间插值，在 Physics-IQ Verified 图生视频轨道把 Wan2.2-14B 的 32.2 分提升到 55.0 分。**</p>

+ **CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15101)
![architecture](https://img.shields.io/badge/CFGComposer_Copula_Score_Correction-red)
![task](https://img.shields.io/badge/Motion_Generation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CFGComposer 指出朴素混合两个独立扩散模型等于 Product-of-Experts，会丢掉音频与文本之间的 copula 交互项，于是联合训练模型估计该交互并注入 ε 空间，在 BEAT 上取得 SRGR 0.9916 与 76-83% 盲测胜率。**</p>

+ **From Seeing to Remembering: Brain-Informed Agentic Text-to-Video Generation for Enhancing Memorability**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15107)
![architecture](https://img.shields.io/badge/MemCrafter_Neuro_Memorability_Agent-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Tongji_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MemCrafter 用皮层分区构造神经记忆信号预测视频记忆性，并以智能体方式迭代改写提示词，在 Seedance-2.5 上把记忆分从 0.848 提升到 0.908，同时把语义对齐从 0.252 提升到 0.261。**</p>

+ **From Concepts to Interactions: Dynamic Graph Semantic Recomposition for Safe Visual Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15149)
![architecture](https://img.shields.io/badge/DGSR_Dynamic_Semantic_Graph-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Southwest_Jiaotong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DGSR 在采样过程中动态构建语义交互图，把安全控制从静态概念擦除转向关系级干预，在 FLUX.1-dev 上把裸露概念的 I2P 攻击成功率压到 3.2%，并把 T2V 平均不安全帧率相对最强基线降低 41.2%。**</p>

+ **Track4D: Representing Dense 3D Tracking for Video Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15287)
![architecture](https://img.shields.io/badge/Track4D_RTV_NCMV_Representations-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Visual_Geometry_Group_University_of_Oxford-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Track4D 系统比较了把稠密三维轨迹表示成视频的两种方案：逐像素 3D 偏移的 RTV 与时不变规范坐标图的 NCMV，并用 LoRA 适配冻结 Wan 骨干，在四个跟踪基准上取得有竞争力的零样本三维跟踪效果。**</p>

+ **VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15789)
![architecture](https://img.shields.io/badge/VibePrevisBench_4D_Scene_Benchmark-red)
![task](https://img.shields.io/badge/Scene_Generation-magenta)
![organization](https://img.shields.io/badge/Tianjin_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://vibeprevisbench.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VibePrevisBench 评测编码智能体在 Blender 中重建 4D 场景并渲染灰盒代理视频的能力，242 个任务覆盖四类输入，用规则场景核查与 VLM 屏幕核查双维度打分，揭示智能体普遍不会据自己的渲染结果纠错。**</p>

+ **PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16748)
![architecture](https://img.shields.io/badge/PhysLoop_LLM_Physics_Harness-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PhysLoop 用 LLM 充当视频生成的物理审查与纠错中枢，在可执行仿真约束下产出物理正确的训练视频，发布 10 万条视频与 PhysLoop-Gen、PhysLoop-Repair 两个评测集，修复成功率达 86.00% 而最强基线仅 19.33%。**</p>

+ **eDMD: Endpoint Distribution Matching for Few-Step Diffusion Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17194)
![architecture](https://img.shields.io/badge/eDMD_Endpoint_Distribution_Matching-red)
![task](https://img.shields.io/badge/Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**eDMD 提出终点分布匹配蒸馏，只用学生模型的最终输出训练一个共享 fake 模型并用它纠正每一步去噪，配套精度教师与校准过的中间步查询密度，在 SD3-Medium 上让 4 步学生的 HPSv3++ 达到 11.171。**</p>

+ **WorldDraft: If Code Builds the World, Can Video Models Just Render It?**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16217)
![architecture](https://img.shields.io/badge/WorldDraft_Generative_Renderer_Benchmark-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Southern_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://haroldchen19.github.io/WorldDraft-site/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WorldDraft 用 48 个可执行 4D 世界族与 3×3 因子设计构造 432 个配对用例，系统评测 12 个视频模型作为「草稿到视频」渲染器的世界保持与外观实现能力，并给出免训练的 WorldDraft-Primer 改进策略。**</p>

<!-- direction: aigc_editing -->

+ **WaveletLoRA: Frequency-Aware Content-Style Decomposition for Personalized Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15617)
![architecture](https://img.shields.io/badge/WaveletLoRA_Frequency_Disentanglement-red)
![task](https://img.shields.io/badge/Style_Transfer-magenta)
![organization](https://img.shields.io/badge/Institute_of_Automation_Chinese_Academy_of_Sciences-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WaveletLoRA 用两级离散小波变换把参考图拆成 1 个低频与 6 个高频子带，各配一条 LoRA 分支分别承载风格与内容，并建立 1,000 张图的 WaveBench 用 VLM 协议度量属性相似度与属性分离度。**</p>

+ **AIFR: Adaptive Identity Feature Recovery for Diffusion-Based Makeup and Anime Portraits**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15764)
![architecture](https://img.shields.io/badge/AIFR_Adaptive_Identity_Recovery-red)
![task](https://img.shields.io/badge/Identity_Preservation-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_Polytechnic_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AIFR 在冻结人脸识别网络的单个中间层插入仅 1.22M 参数的恢复模块，预测样本级校正强度与空间自适应残差，把 FAR=1e-4 下平均 TAR 从原 ArcFace 的 66.1% 提到 90.2%，且无需重编码既有模板。**</p>

+ **ReliaGuard: Reconstruction-Aware Watermarking for Source Attribution and Blind Edit Localization**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16368)
![architecture](https://img.shields.io/badge/ReliaGuard_Reconstruction_Aware_Watermark-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/College_of_Cyber_Security_Jinan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ReliaGuard 在写入水印时同时优化原图与其 VAE 重建，使得背景重建削弱空间证据后仍可溯源与盲定位编辑区域，在 900 个编辑用例上取得 85.61% 与 94.90% 的编辑区域 IoU，标识比特准确率达 100%。**</p>

