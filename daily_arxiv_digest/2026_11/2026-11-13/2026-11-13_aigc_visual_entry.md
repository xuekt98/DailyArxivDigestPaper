<!-- direction: aigc_generation -->

+ **ThermalSplat: Generalizable Pose-Free Gaussian Splatting for Sparse-View Thermal 3D Reconstruction**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15435)
![architecture](https://img.shields.io/badge/ThermalSplat-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Indian_Institute_of_Technology_Madras-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**首个无需相机位姿与 RGB 引导的前馈高斯泼溅框架，仅凭两张稀疏热成像图一次前向重建 3D 场景，平均 24.964 dB 优于同条件下的逐场景优化基线。**</p>

+ **CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15602)
![architecture](https://img.shields.io/badge/CoCode_World-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://iapple233.github.io/CCW/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以共享 3D proxy 视频加 RGB 外观参考联合生成两个玩家视角，把双方画面沿宽度拼进同一条分支，用预训练视频模型的原生注意力完成跨视角外观通信，跨视角身份一致性达 3.847。**</p>

+ **MatrixSplat: Matrix-Parallel and Feature-Scalable 3D Gaussian Splatting Rendering on GPUs**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15153)
![architecture](https://img.shields.io/badge/MatrixSplat-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/The_University_of_Texas_at_Arlington-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 3D 高斯泼溅的深度排序 alpha 合成改写为顺序无关的加权累加，使特征累积在 warp 级映射到 Tensor Core 的 MMA 指令，并支持高维语义特征的可扩展实时渲染。**</p>

+ **Escaping the Curse of Dimensionality in One-Step Flow-Based Generative Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15447)
![architecture](https://img.shields.io/badge/Self_Distilled_Flow_Map_Network-red)
![task](https://img.shields.io/badge/Consistency_Model-magenta)
![organization](https://img.shields.io/badge/HSE_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在数据分布由低维流形加高斯噪声生成的假设下，导出单步 flow map 估计的逼近与泛化误差界，收敛率只依赖内在维度，为一步生成模型避开维度灾难提供首个有原则的解释。**</p>

+ **Where to Generate Touch: Do Image Latents Preserve Material Recognition?**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15834)
![architecture](https://img.shields.io/badge/Photo_To_Touch_Generator-red)
![task](https://img.shields.io/badge/Tokenizer_Compression-magenta)
![organization](https://img.shields.io/badge/University_of_Maryland_College_Park-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在训练触觉生成器之前，用真实 GelSight 按压逐一测试各图像模型的编解码潜空间能否保住材质识别，最终选定 SD-VAE 连续潜空间并训练照片到触觉的生成器。**</p>

<!-- direction: aigc_editing -->

+ **Reframing Video Inverse Tone Mapping as Blind Posterior Inference via Latent Luminance Supervision**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15146)
![architecture](https://img.shields.io/badge/ReITM-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把视频逆色调映射重述为未知色调算子下的盲后验推断，用视频扩散潜变量的固定仿射泛函直读对数亮度，再以可观测性门控的非对称 expectile 损失在裁剪区选后验分位。**</p>

+ **Learning Motion-Appearance Coupling Priors for Solving Video Inverse Problems**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15420)
![architecture](https://img.shields.io/badge/Motion_Appearance_Coupling_Diffusion-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/School_of_Computation_Information_and_Technology_Technical_University_of_Munich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把运动引导的视频逆问题重述为学习运动与帧外观的概率耦合，用条件扩散模型建模光流解释不了的外观残差分布，作为即插即用的正则项接入扩散式视频重建，覆盖动态压缩感知与心脏 MRI。**</p>

+ **Reading the Unreadable: Text-Aware Image Super-Resolution Needs Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15449)
![architecture](https://img.shields.io/badge/Reasoning_Transfer_Captioning-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/CIPLAB_Yonsei_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://jasonleex1995.github.io/TAISR_needs_Reasoning)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用人工标注的 ReasonText 基准和免检测误差的 GTTCA 指标证明文字感知超分缺少推理能力，并提出免训练的 RTC 插件，让外部 MLLM 先读出模糊文字再写进 caption 引导文本条件模型。**</p>

+ **Image Deblending with Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15760)
![architecture](https://img.shields.io/badge/Two_Stage_Diffusion_Deblending-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Reichman_University_Herzliya_Israel-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/DanBotchan/image-deblending-diffusion)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把图像 alpha 混合分解表述为联合逆问题，用冻结扩散先验同时重建两张源图并把 alpha 重参数化为二阶多项式，配合文本引导的潜域语义分离与像素域精修实现免训练分解。**</p>

+ **WaveFlow-UIE: A Single-Pipeline Wavelet-Domain Flow Model for Efficient Underwater Image Restoration**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15457)
![architecture](https://img.shields.io/badge/WaveFlow_UIE-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/King_Fahd_University_of_Petroleum_&_Minerals_Dhahran_Saudi_Arabia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在小波域用流匹配直接学习从退化水下小波表示到干净表示的映射，并注入透射率与环境光等物理先验，配合频域加权、感知与物理一致性损失实现单管线高效率增强，并支持单步推理。**</p>

<!-- direction: aigc_rl -->

+ **Verifier Choice is a Benchmark Design Variable: Auditing Structural Counting Evaluation in Text-to-Image Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15433)
![architecture](https://img.shields.io/badge/Verifier_Centric_Audit_Suite-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/REASONS_Lab_Institute_for_Network_Sciences_and_Cyberspace_Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/AzusaCat1111/verifier-choice-audit)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 verifier 选择视为基准设计变量，在 6,240 张生成图上系统审计不同 MLLM 验证器与使用协议对计数类评测的影响，并提出分解式的 verifier 可靠性画像作为报告规范。**</p>

+ **Estimating Image Creativity**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15044)
![architecture](https://img.shields.io/badge/Creativity_Dimension_VLM_Pipeline-red)
![task](https://img.shields.io/badge/Aesthetic_Scoring-magenta)
![organization](https://img.shields.io/badge/NC_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**先估计图像在新颖性、惊讶、唤醒三个心理学创造力维度上的强度，再用监督模型合成创造力总分；基于视觉语言模型的方案在 135 张图上与人类评分无统计显著差异。**</p>

