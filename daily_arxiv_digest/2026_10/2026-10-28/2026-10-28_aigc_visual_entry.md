# 2026-10-28 - AIGC 视觉生成 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36545)
![architecture](https://img.shields.io/badge/FrameForge_MoTE_CoTR-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://lyne1.github.io/FrameForge-page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把统一条件图像生成重写为目标帧预测，直接复用预训练视频扩散模型：用 MoTE 动态选择不同虚拟间隔的 RoPE 专家刻画条件与目标的距离，用 CoTR 的推理瓶颈掩码迫使信息经中间潜状态传播，在 DreamBench、COCO2017、GEdit-Bench 上超越对比方法。**</p>
+ **MoI-Bench: A Benchmark for Image Generation and Editing on Mobile Devices**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37599)
![architecture](https://img.shields.io/badge/MoI_Bench_Quality_Deployability_Map-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/University_College_London-green)
[![project](https://img.shields.io/badge/project-blue)](https://carlofkl.github.io/MoI-Bench-project/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向移动端的图像生成与编辑评测基准，提出二维「质量-可部署性」能力图取代单一分数；配套 MoI-Eval 用稀疏的 Operation×Target×Criteria 评分立方，把指令遵循、视觉质量与细节保持绑定到各自适用的子任务上。**</p>
+ **SpeeDiff: Scalable Pixel-Anchored End-to-End Latent Diffusion Model**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36419)
![architecture](https://img.shields.io/badge/SpeeDiff_Tweedie_Pixel_Reconstruction-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/ByteDance_Seed-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 VAE 与扩散模型从零联合训练，用 Tweedie 公式从中间噪声态解码干净潜变量，构造 TPR 损失给潜空间提供像素级锚点以避免坍缩；SpeeDiff-XL 训练比 SiT 快 140 倍、比 REPA 快 61 倍，ImageNet 512×512 无引导 FID 达 1.53。**</p>
+ **Repurposing Video Diffusion Transformers for Cross-View Temporal Object Correspondence**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37633)
![architecture](https://img.shields.io/badge/XTrack_Joint_View_Time_Mask-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/KAIST_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://cvlab-kaist.github.io/XTrack/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出跨视角时序物体对应任务，并把预训练视频 DiT 的语义与时空先验迁移过来：XTrack 在潜空间做 RGB 到掩码的传输，用联合视角-时间掩码预测同时建模跨视角匹配与时序跟踪，绕开先传播再匹配或先匹配再跟踪两种传统范式的缺陷。**</p>
+ **A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37110)
![architecture](https://img.shields.io/badge/ReSeed_First_Step_Bias_Adapter-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Graz_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**诊断出少步扩散蒸馏丢失的多样性几乎全部发生在第一个去噪步：保持学生第 2–4 步不变、仅把第一步换成教师，即可在 SD3-Medium 上让 98/100 个 prompt 的多样性回升；ReSeed 据此只训一个极小的 bias adapter 并把速度对齐教师第一区间割线速度。**</p>
+ **GraftRay: Physically Based Mesh Insertion into Gaussian Splatting Scenes via Path Tracing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37036)
![architecture](https://img.shields.io/badge/GraftRay_Hybrid_Path_Tracing-red)
![task](https://img.shields.io/badge/3D_Editing-magenta)
![organization](https://img.shields.io/badge/Technical_University_of_Munich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向 2D/3D 高斯场景的物理一致物体插入：用扩散先验恢复材质与法向，显式建模窗口、台灯这类空间延展光源并闭式求解辐射度，再以混合路径追踪联合渲染场景高斯与插入网格，得到视角一致的着色、互反射与软阴影，在 FIPT 上超越 ComGS 与 EAG-PT。**</p>
+ **Haste Makes Waste? Towards Safe Few-Step Text-to-Image Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36665)
![architecture](https://img.shields.io/badge/DICE_Distillation_Integrated_Erasure-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Tel_Aviv_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发现少步蒸馏 T2I 模型比教师更不安全、且不安全概念更难被擦除；DICE 让擦除的潜变量构造与生成保持损失都对齐产生该模型的蒸馏方法，在 FLUX Schnell 上把不安全生成率降到 0.046（既有方法≥0.161）且基本保留良性生成质量。**</p>
+ **Know, then Draw: A New Learning Paradigm for Visual Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37626)
![architecture](https://img.shields.io/badge/Know_Then_Draw_AR_Pretrain_Diffusion_Posttrain-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_California,_San_Diego-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把视觉生成拆成两段训练：自回归预训练负责知识获取、扩散后训练负责高保真渲染，并据此提出不带重建损失的纯语义 tokenizer；论文建立两条 compute-optimal 缩放律，用 6,600 H100 小时训出 3B 模型，GenEval 86、DPG-Bench 87。**</p>
+ **LociArt: A Unified Paradigm for Free-Style Local Video Stylization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36456)
![architecture](https://img.shields.io/badge/GRNStyle_Local_Video_Stylization-red)
![task](https://img.shields.io/badge/Style_Transfer-magenta)
![organization](https://img.shields.io/badge/MiLM_Plus,_Xiaomi_Inc.-green)
[![project](https://img.shields.io/badge/project-blue)](https://higherhu.github.io/lociart/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把自由风格局部视频风格化拆成「改哪里」与「改成什么样」两个显式输入，配套 GRNStyle 模型支持多区域共享或差异化风格及风格组合；作者用全局风格化→目标移除→抠像→合成的自动化流水线构造了 10 万条配对数据 LociArt-100K 与配套基准。**</p>
+ **ReferStream: Interactive Subject Injection for Streaming Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37566)
![architecture](https://img.shields.io/badge/ReferStream_Joint_Latent_Cache_Restoration-red)
![task](https://img.shields.io/badge/Multi_Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/Bournemouth_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://xushuolin.github.io/ReferStream/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向流式视频生成的交互式主体注入：ReferStream 免训练地用当前场景自行构造参考，以瞬态缓存注入把中途出现的主体接进已建立的场景，在冻结的 LongLive2 骨干上配合 Joint Latent 与 Cache Restoration，在含参考到达时序的 ReferStream Bench 上优于对比基线。**</p>