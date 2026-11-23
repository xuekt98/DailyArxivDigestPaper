<!-- direction: aigc_generation -->

+ **Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26334)
![architecture](https://img.shields.io/badge/Temporal_Rotation_Quantization-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/Massachusetts_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频扩散在去噪步之间复用 KV 缓存，缓存体积很快成为长视频生成的瓶颈。TRQ 先对时间相邻的缓存块拟合正交旋转，把逐通道均值压平后再量化到 2 bit，在 LongCat-Video-13B 上把 VBench 主体一致性从 90.38 提升到 92.02。**</p>

+ **Asuka-FM: A System-Architectural Co-Design Framework for Efficient Text-to-Image Pretraining on Consumer Hardware**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26437)
![architecture](https://img.shields.io/badge/Asuka_FM_Dual_Stream_DiT-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Universidad_Carlos_III_de_Madrid_Spain-green)
[![project](https://img.shields.io/badge/project-blue)](https://deeplearningcafe.github.io/projects/asuka-fm)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向消费级硬件的文生图预训练系统与架构协同设计。Asuka-FM 用 206M 双流 DiT、SPRINT 序列稀疏化、连续纵横比 RoPE 与像素适配段，在单张 RTX 4090 上约 160 GPU 小时、不到 55 美元训完，256px 拿到 GenEval 0.588 与 DPG 78.96。**</p>

+ **AURA: AUdio-dRiven streaming Avatar**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26540)
![architecture](https://img.shields.io/badge/AURA_Causal_S2V-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Kyutai_Paris_France-green)
[![project](https://img.shields.io/badge/project-blue)](https://kyutai.org/aura)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向语音助手与虚拟形象的流式数字人。AURA 用滚动 KV 缓存逐块生成，只需当前块的音频即可起算，1.3B 在单卡上以 20.7 fps 输出 576p，5B 输出 720p 达 9.7 fps，分别比双向教师快 23 倍与 17 倍，每块仅 4 步去噪。**</p>

+ **Posterior Matching Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26629)
![architecture](https://img.shields.io/badge/Posterior_Matching_Distillation-red)
![task](https://img.shields.io/badge/Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/Virginia_Tech-green)
[![project](https://img.shields.io/badge/project-blue)](https://pmd-distillation.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散蒸馏的分布匹配多受 reverse-KL 主导，偏向教师主模态而牺牲多样性。PMD 改为匹配学生样本的指数重加权均值与教师平移后验均值，在零总体损失下恢复完整后验，并在 SDXL 与 FLUX.2 上取得四步方法中最好的 FID 24.12。**</p>

+ **PP-CFG: Polarity-Preserving Guidance for Controllable Few-Step Image and Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27266)
![architecture](https://img.shields.io/badge/Polarity_Preserving_CFG-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://pp-cfg.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**少步蒸馏常让可调 CFG 与运行时负向提示失效。PP-CFG 在共享视觉主干内以相反符号合成正负文本条件的注意力响应，并用尺度与时间混合器精修，四步 Wan2.1 达到 VBench 81.46，负向目标移除率图像 12.08%、视频 22.00%，均高于对应教师。**</p>

+ **Zing-1.0: A Playable World System Built on Controllable Rendering**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27336)
![architecture](https://img.shields.io/badge/Zing_Controllable_Rendering-red)
![task](https://img.shields.io/badge/Scene_Generation-magenta)
![organization](https://img.shields.io/badge/Zing_Team_SeedLeap.ai-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把可玩世界系统落到可控渲染上的完整实现。Zing-1.0 用可执行引擎产生 proxy 帧约束结构与运动，流式渲染器据此合成玩家视角，OpenVE 3.90、LongV2VBench 3.44，StreamEval 指令编辑 57.86、参考编辑 54.06，832×480 下稳态吞吐 23.82 FPS。**</p>

+ **CalibCache: Cache-to-Full Feature Dynamics Calibration for Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25296)
![architecture](https://img.shields.io/badge/CalibCache_Acceleration_Calibration-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**特征缓存加速扩散 Transformer 时，短采样步与粗缓存网格会放大外推误差。CalibCache 只用一对全量与朴素缓存轨迹，离线拟合特征加速度的标量校正图，N=5 时把 FLUX.1-dev 的 LPIPS 从 0.563 降到 0.429，同时取得 2.86 倍去噪加速。**</p>

+ **VideoRNG: Relightable Neural Gaussians from Generative Video Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25338)
![architecture](https://img.shields.io/badge/Relightable_Neural_Gaussians-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从文本或单张图生成可重光照 3D 资产的两阶段方法。VideoRNG 先微调视频扩散模型产出 81 帧 RGBA 转台，再把其中 29 帧编成 8 个 VAE latent 帧，一次前向重建出百万级各向异性高斯，渲染约 50 ms 每帧（1280×720、1 spp）。**</p>

+ **CaT-Movie: Balancing Global Planning and Local Rendering for Long Multi-Shot Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25620)
![architecture](https://img.shields.io/badge/CaT_Movie_Storyboard_System-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://jinplu.github.io/CaT-Movie/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**长篇多镜视频生成的全局规划与局部渲染协同系统。CaT-Movie 由 LLM 规划器写分镜、确定性代码维护跨镜状态，渲染器用参考路由稀疏自注意力分发身份，在 CaT-MBench 的 92 个测试故事上取得最高平均分 0.597，高于 HoloCine 的 0.571。**</p>

+ **D3-Cache: Accelerating Diffusion Models with Dynamic Mode Decomposition**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25689)
![architecture](https://img.shields.io/badge/DMD_Velocity_Forecasting-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Chinese_Academy_of_Sciences-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把动态模态分解用于扩散采样的免训练加速器。D3-Cache 用最近几次精确速度拟合 DMD 并只外推调度器真正消费的速度，再由已实现误差反推风险决定跳步，四个模型共享 H=3、τ=0.56 即拿到2.6 到 3.8 倍加速。**</p>

+ **Why Flat Drafts Stay Flat: Region-Mean Latents Govern Texture in Flow-Based Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25930)
![architecture](https://img.shields.io/badge/Region_Mean_Latent_Analysis-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Institute_of_Information_Engineering_Chinese_Academy_of_Sciences-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**平涂色块草图为何在照片级提示下仍保持平坦？论文把原因定位到 VAE 潜空间里的区域均值偏移：照片与草图的偏移有 78%（FLUX.1-dev）到 95%（Qwen-Image）集中在一个共享通道方向上，据此提出编码前抖动加均值场缩放等免训练修正。**</p>

+ **StreamEgo: Streaming Exocentric-to-Egocentric Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26165)
![architecture](https://img.shields.io/badge/StreamEgo_Dual_Branch_Prior-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把第三人称录制实时转成第一人称视频的流式框架。StreamEgo 用流式双分支先验分别对齐外观与骨骼运动，配区域感知损失课程并蒸馏成分块自回归模型，在单张 H100 上达到 24.3 FPS，而离线的 EgoX 只有 0.08 FPS。**</p>

<!-- direction: aigc_editing -->

+ **What Stays in the Picture? From Redundant Instructions to Dependency-Aware Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27388)
![architecture](https://img.shields.io/badge/CRIE_Intent_Execution_Agent-red)
![task](https://img.shields.io/badge/Instruction_Editing-magenta)
![organization](https://img.shields.io/badge/Sun_Yat-sen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**一条指令同时指定多个物体、属性与空间关系，并修订或取消早期要求。CRIE-Agent 先把修订历史解析成对象级最终意图，再按参考优先的依赖顺序执行并从原图整体重做，在 10000 条 CRIE-S 基准上把完整编辑成功率从 0% 提到 27.5% 至 50.0%。**</p>

+ **GameScrub: Learning HUD Removal from Real Gameplay with Recovered Targets**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27547)
![architecture](https://img.shields.io/badge/GameScrub_Data_Recovery_Pipeline-red)
![task](https://img.shields.io/badge/Video_Inpainting-magenta)
![organization](https://img.shields.io/badge/Institute_of_Foundation_Models-green)
[![project](https://img.shields.io/badge/project-blue)](https://areeb2735.github.io/gamescrub/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**真实游戏录屏只有带 HUD 的画面，缺少干净配对目标。GameScrub-Data 用预训练视频扩散模型在真实录屏上反推伪干净目标，训练出的 GameScrub 在 Game2World 上取得 71.95 的去 HUD 分数（GameCleaner 57.86），标注 HUD 移除率 90.06% 对 59.07%。**</p>

<!-- direction: aigc_rl -->

+ **Zero to Four Views: Unified Panorama Generation and Preference RL for Unobserved Regions**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25389)
![architecture](https://img.shields.io/badge/UR_GRPO_Panorama_Model-red)
![task](https://img.shields.io/badge/Preference_Optimization_Visual-magenta)
![organization](https://img.shields.io/badge/George_Mason_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**一个模型从文本加 0 到 4 个透视条件视角生成整幅等距柱状全景。第二阶段 UR-GRPO 用视觉语言模型对未覆盖区域的裁剪块做两两偏好比较并据此强化学习，Laval Indoor 上 K=1 的 crop FID 从 34.25 降到 13.44。**</p>

