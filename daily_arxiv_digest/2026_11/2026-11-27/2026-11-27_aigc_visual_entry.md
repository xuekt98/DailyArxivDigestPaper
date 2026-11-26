<!-- direction: aigc_generation -->

+ **CoRe: Jointly Learning Contextual Representations for Understanding and Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31397)
![architecture](https://img.shields.io/badge/CoRe_Unified_Contextual_Representation-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Apple-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CoRe 让理解与生成共用同一套上下文表示：383M 参数、仅用 CC12M 训练、无需任何预训练编码器即可在 COCO-30K 拿到 10.10 的 FID，且该表示还能被冻结探针读取与操纵。**</p>

+ **DexOPD: Dual-Extrapolation On-Policy Distillation for Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31969)
![architecture](https://img.shields.io/badge/DexOPD_Dual_Extrapolation_Student-red)
![task](https://img.shields.io/badge/Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/SJTU-DENG-Lab/DexOPD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DexOPD 用教师外推加历史学生自外推的双重外推做多专家 on-policy 蒸馏，把 SD3.5-Medium 统一学生推到 GenEval 0.9736、OCR 0.9515、DrawBench 美学分 6.4875，反超各专家教师。**</p>

+ **Distill to Loop: Turning Pretrained Diffusion Transformers into Looped Models with Adjustable Depth**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31977)
![architecture](https://img.shields.io/badge/Dooop_Looped_DiT_Student-red)
![task](https://img.shields.io/badge/Diffusion_Distillation-magenta)
![organization](https://img.shields.io/badge/Virginia_Tech-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Dooop 把预训练扩散 Transformer 蒸馏成循环模型：SD3-medium 上 0.756B 参数、约教师 37%，两到四次循环追平教师，两次循环只用约 58% 算力，四步采样加 loop guidance 把四项均值从 88.2 抬到 99.2。**</p>

+ **Qwen-Image-HD: Autoregressive Diffusion for High Definition Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32736)
![architecture](https://img.shields.io/badge/Qwen_Image_HD_Blockwise_AR-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Qwen-Image-HD 用局部训练加分块自回归把 Qwen-Image 2.0 推到 4K 以上：每次预测 1K 瓦片并条件化上下左右邻块与压缩历史缩略图，4K 基准上优于 FLUX-3-Image-Klein 的直接生成，还能出 16K 图。**</p>

+ **JetDiffusion: Pushing the Speed Limits of Video Generation with NVFP4 Sparse Attention**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33268)
![architecture](https://img.shields.io/badge/VSQA_Sparse_NVFP4_Attention-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/University_of_California_San_Diego-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**JetDiffusion 用可训练的稀疏量化注意力 VSQA 加速视频生成：90% 稀疏下注意力快 8 到 29 倍，叠加 NVFP4 量化和少步蒸馏后，Wan2.1-14B 在 RTX 5090 上端到端提速 273 倍且画质基本持平。**</p>

+ **ScanAR: Parallel Row-Scan Decoding for Efficient Image Generation in Unified Autoregressive Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33761)
![architecture](https://img.shields.io/badge/ScanAR_Row_Scan_Decoding-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Xiaomi_Robotics-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ScanAR 用行扫描并行解码改造统一自回归模型：只重定义视觉 token 的前驱关系，视觉解码深度从 HW 降到 H+W，Emu3.5-Image-34B 上后训练 GenEval 82.36，512×512 出图快 13.8 倍且不加参数。**</p>

+ **Exploring the Design Factors of Pixel-space Diffusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34093)
![architecture](https://img.shields.io/badge/EiT_Pixel_Diffusion_Transformer-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/Utrecht_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/forever208/EiT)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EiT 系统研究像素空间扩散的三大设计因素，并用 U 形通道瓶颈把表示压缩与去噪统一到一个网络：ImageNet 256×256 上 FID 1.61 对 JiT 的 1.85，512×512 上 1.73 对 1.99，还顺手拿下视频 FVD。**</p>

+ **Spe3DUp: Faithful Trajectory Distillation for Fast Image-to-3D Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34141)
![architecture](https://img.shields.io/badge/Spe3DUp_Faithful_Trajectory_Distill-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Spe3DUp 用忠实轨迹蒸馏把图像到 3D 的生成提速：直接监督教师的输入条件去噪轨迹，粗几何 DiT 加速 10.0 倍、细化 DiT 加速 19.9 倍，整条网格流水线端到端 7.7 倍且仍保持参考对应关系。**</p>

+ **Generation as Reverse Encoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34782)
![architecture](https://img.shields.io/badge/HyC_DiT_Reverse_Encoding_Stages-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ChengShiest/RevFlow)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RevFlow 把生成视为编码的逆过程：沿冻结编码器的中间表示从深到浅逐级生成，ImageNet 256×256 上 690M 训 5 个 epoch 就有 1.96 FID，1.55B 达 1.74，原生匹配适配后每阶段仅需一步。**</p>

+ **Guidance as Variance Matching**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34801)
![architecture](https://img.shields.io/badge/Variance_Matched_Guidance_Scale-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/Massachusetts_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://ottogin.github.io/vmg)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把 Classifier-Free Guidance 重新表述为方差匹配：闭式规则无需调参就能复现十一个常用模型手调的引导尺度，Spearman 相关 0.96，还发现引导并非让后验均值预测更准而是把误差缩放到后验协方差上。**</p>

<!-- direction: aigc_editing -->

+ **EditText: Structure-Aware Generation and Selective Visual Transport for Fine-Grained Text Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32134)
![architecture](https://img.shields.io/badge/EditText_Attention_Transport_Fill-red)
![task](https://img.shields.io/badge/Instruction_Editing-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EditText 把文字替换拆成目标字符生成与源图视觉迁移两部分，用双条件 Fill 输入配合注意力迁移框架搬运细节，在自建 TBench 上非编辑区 SSIM 0.9769、整图 LPIPS 0.0460，并支持字母、文字与阿拉伯数字。**</p>

+ **MYSTIQUE: Few-Shot Facial Identity Transfer with Performance Preservation**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32232)
![architecture](https://img.shields.io/badge/MYSTIQUE_Disentangled_Identity_Streams-red)
![task](https://img.shields.io/badge/Identity_Preservation-magenta)
![organization](https://img.shields.io/badge/Vanderbilt_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MYSTIQUE 用分离的身份、表情与光照三条流解决换脸中的身份泄漏，配合随机块掩码、自增广与人脸随机化三种解耦策略与两遍推理，ArcFace 0.601、脸型泄漏率降到 0.34，人评偏好率达 90%。**</p>

+ **Can You Find the Edit When Nothing Looks Wrong? A Paired Benchmark for Text-Driven Image Manipulation Localization Beyond Semantic Abnormality**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32242)
![architecture](https://img.shields.io/badge/PAPE_Paired_Localization_Benchmark-red)
![task](https://img.shields.io/badge/Instruction_Editing-magenta)
![organization](https://img.shields.io/badge/Shenzhen_Campus_of_Sun_Yat-sen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PAPE 为文本驱动图像篡改定位构建配对基准：同一目标生成语义合理与明显异常两组编辑，含 6500 张照片、47747 条双语三元组、四个编辑器与六类违规，九个定位器有 26 组在合理编辑上 IoU 反而更低。**</p>

+ **Déjà-VAE: Training-Free Consistent Editing with Pseudo-Invertible Encoders and Latent Back-Projection**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32501)
![architecture](https://img.shields.io/badge/Deja_VAE_Pseudo_Invertible_Codec-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Technion_-_Israel_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Déjà-VAE 无需训练就能让多轮编辑保持一致：把预训练 VAE 改造成伪可逆编解码器实现精确潜变量往返，再按标定阈值做每轮一次的自适应小波反投影，25 轮往返后仍有 28.34 dB 与 0.07 LPIPS。**</p>

<!-- direction: aigc_rl -->

+ **How Many Samples Is RL Worth? Best-of-N versus RL Post-Training for Text-to-Image Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33232)
![architecture](https://img.shields.io/badge/Best_of_N_Exchange_Rate-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Bosch_Research_India-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文给 RL 后训练与 best-of-N 之间定了一个「汇率」：在 398 条 GenEval 风格提示上，位置类提示人看 8 张基线图只对 52%，而 1 张 RL 图对 92%；自动评委会把差距夸大到 9.3 个百分点，人评只看到 5.5 与 6.5。**</p>

+ **What Does RL Post-Training Teach Text-to-Image Models? A Skill-Wise Analysis of Flow-GRPO**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33316)
![architecture](https://img.shields.io/badge/Pass_at_k_Skill_Decomposition-red)
![task](https://img.shields.io/badge/GenEval-magenta)
![organization](https://img.shields.io/badge/North_Carolina_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把 Flow-GRPO 的收益拆到 GenEval 的六项技能上：在 553 条提示、共享噪声种子、n=32 下，四项技能其实只是锐化，1 张后训练样本仅值 4 到 10 张基线样本，只有空间关系被真正解锁，pass@32 从 0.69 升到 1.00。**</p>

+ **Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.34-blue)](https://arxiv.org/abs/2611.34907)
![architecture](https://img.shields.io/badge/Agentic_LongLive_Async_Memory-red)
![task](https://img.shields.io/badge/RL_for_Video-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://nvlabs.github.io/LongLive/Agentic-LongLive/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Agentic LongLive 给实时自回归视频生成加上异步智能体记忆：记忆代理只看已披露提示、绝不读已生成视频，并在独立 GPU 上预填注意力汇点，857 个镜头上状态一致性加 26.3 分、身份加 44.9 分，额外耗时约 1%。**</p>

+ **PromptSMC: Enabling Particle Exploration in Flow Matching via LLM-Based Prompt Rejuvenation**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31471)
![architecture](https://img.shields.io/badge/PromptSMC_Rejuvenated_Particle_Filter-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/Uppsala_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/shermanlian/PromptSMC)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PromptSMC 把序列蒙特卡洛与 LLM 提示改写结合，在确定性流匹配采样下恢复粒子探索：SD3、FLUX.1-dev、Z-Image 三个骨干的 GenEval 全部超过 vanilla 与标准 SMC，代价是每提示多花约 9 秒与更多显存。**</p>

