<!-- direction: aigc_generation -->

+ **Few-Step Streaming Video Generation via Condition Shifting**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14033)
![architecture](https://img.shields.io/badge/Apex_Condition_Shifting-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把假分数网络并入生成器的 condition shifting 写法，APEX 在 180 秒流式视频上只用 3 次骨干 NFE 即让指令达成与视觉美感双双超过 S2-Avatar，训练峰值显存还降 4.4%、迭代时间短 9.2%。**</p>

+ **UGG: Unified Generative Geometry Model**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14440)
![architecture](https://img.shields.io/badge/UGG_Unified_Generative_Geometry-red)
![task](https://img.shields.io/badge/4D_Generation-magenta)
![organization](https://img.shields.io/badge/Harvard_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://ugg-model.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UGG 把 RGB 视频、深度与相机位姿统一成一个生成式模型，按模态与时间分配不同噪声级做条件补全，在 ScanNet++ 上深度 Abs Rel 0.073、位姿 ATE 0.087，并支持推理期多假设搜索。**</p>

+ **Continuous Angular Control in Text-to-Image Generation via Geometric Token Encoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13172)
![architecture](https://img.shields.io/badge/Geometric_Token_Encoding-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Bilkent_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://furkanguzelant.github.io/angular_control/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把角度量编码成周期特征并投影为角色专属 token 注入冻结文本编码器，配合随机定位松弛与手别交换目标，把模拟钟双指针 6 度内命中率从不足 1% 提升到 63%–78%，分数任务达 89.5%。**</p>

+ **Robust Flow Matching under Target Corruption and Label Noise**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13324)
![architecture](https://img.shields.io/badge/TRS_CCS_Robust_Flow_Matching-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/KTH_Royal_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/mertcankurucu/robust-flow-matching)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把流匹配训练重述为时间依赖回归，用时间残差打分 TRS 处理目标污染、用类间对比打分 CCS 处理标签噪声，W2 从 1.199 降到 0.434、MMD 从 0.279 降到 0.048，类均 W2 最多再降 87%。**</p>

+ **UniWeaver: Harnessing Unified Multimodal Models for Interleaved Text-Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13530)
![architecture](https://img.shields.io/badge/UniWeaver_Harness-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Ohio_State_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://poscape.github.io/UniWeaver/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UniWeaver 把多模态规划、生成与视觉反馈做成模型无关的 harness，配 1 万条 20 类任务的训练集与 120 任务评测集，不改参数就把 BAGEL 总分从 27.7 拉到 58.9、TokenFlow 拉到 60.5。**</p>

+ **FlashMotion: Ultra-Fast Long-Term 3D Motion Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13626)
![architecture](https://img.shields.io/badge/FlashMotion_BiMamba_MeanFlow-red)
![task](https://img.shields.io/badge/Motion_Generation-magenta)
![organization](https://img.shields.io/badge/Tencent_IEG_Motus_Group-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Sun-Happy-YKX/FlashMotion)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FlashMotion 用 3D 运动空间 MeanFlow 做少步采样，配约 60M 参数的非自回归 BiMamba 骨干，在 BABEL 上 4 步即达 R@3 29.134、FID 0.907，长序列吞吐 FPS@10K 高达 46303，是 MMM 的三十余倍。**</p>

+ **Plug-and-Play ADMM for Inverse Problems with Flow Matching Denoiser**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13742)
![architecture](https://img.shields.io/badge/PnP_ADMM_Flow_Prior-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/TH_Wurzburg-Schweinfurt_CAIRO-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/dibyanshu100/flow_admm.git)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 ADMM 辅助变量与轨迹修正把流匹配先验更紧地嵌进即插即用逆问题求解，AFHQ-Cat 超分单批 4 图仅 12.81 秒、1.79GB 显存，而 Flow Priors 需要 75.59 秒、34.21GB。**</p>

+ **TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14307)
![architecture](https://img.shields.io/badge/TaoMate_R1_Temporal_Role_Specialization-red)
![task](https://img.shields.io/badge/Multi_Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/Alibaba_Group-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/TaoLiveAIGC/TaoMate-H3)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TaoMate-R1 用时间角色专精替代操作专精，在同一骨干上按场景建立与续写各挂一个 rank-128 适配器，十条约两分钟长流的指令边界亮度跳变由 1.96 降到 0.613，时序相似度同步提升。**</p>

+ **Forward-Value Discretization: Faster Stochastic Diffusion Sampling Without High-Order Approximation**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14328)
![architecture](https://img.shields.io/badge/Forward_Value_Discretization-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/Chinese_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Na-Li66/F-DDPM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**证明高阶近似的随机扩散采样器仍是一阶收敛后，作者改用训练无关的前瞻值离散化：每次迭代仅一次模型评估，四个数据集同 NFE 下 FID 一致更低，1.5 倍 NFE 即可追平确定性采样器。**</p>

+ **RB-LDC: Redundancy-Balanced Latent Coding for Noise-Robust Diffusion Latents**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13955)
![architecture](https://img.shields.io/badge/RB_LDC_Redundancy_Balanced_Coding-red)
![task](https://img.shields.io/badge/Tokenizer_Compression-magenta)
![organization](https://img.shields.io/badge/DGIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RB-LDC 在编码器与扩散之间插一层可逆线性层，按解码器敏感度重分配各方向 log-SNR，在 ImageNet 256 上相对等预算各向同性编码把平均扰动 FID 降低 17.1，同时保持干净重建不变。**</p>

+ **RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13772)
![architecture](https://img.shields.io/badge/RF3DGS_Reflection_Free_3DGS-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RF3DGS 把多视角最小像素强度这一光度先验搬到 3D 高斯泼溅上，用几何先验估深度、3D warping 构造干净透射伪标签并以自适应双渲染损失监督，同时给出含 45 个样例的首个 3D 去反射基准。**</p>

<!-- direction: aigc_editing -->

+ **Hint, Not Hole: Localization-Robust Video Overlay Removal**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13711)
![architecture](https://img.shields.io/badge/HintErase-red)
![task](https://img.shields.io/badge/Video_Inpainting-magenta)
![organization](https://img.shields.io/badge/Malanshan_Audio_&_Video_Laboratory-green)
[![project](https://img.shields.io/badge/project-blue)](https://zdyshine.github.io/HintErase)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HintErase 把检测器定位当成提示而非洞，训练时按真实定位器的漏框与误盖方式污染提示通道，使模型既能补上漏掉的叠加层又不误伤被误盖的背景与真实场景文字，交付用 81 帧窗口流式处理。**</p>

+ **DroneSegEdit: Adapting Pretrained Generative Editors for UAV Segmentation with Language-Grounded Verification**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13890)
![architecture](https://img.shields.io/badge/DroneSegEdit_LGSV-red)
![task](https://img.shields.io/badge/Instruction_Editing-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DroneSegEdit 用任务专属 LoRA 把开源图像编辑器改造成无人机分割工具，渲染 RGB 提案后由语言接地空间验证器在提案内筛选，RIS-LAD 上取得 52.78 mIoU，比此前最好方法高 7.16 个点。**</p>

+ **Location Matters: Sparse Latent-Variance Attacks for Face Privacy against Diffusion Personalization**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14254)
![architecture](https://img.shields.io/badge/SEAL_Sparse_Latent_Variance_Attack-red)
![task](https://img.shields.io/badge/Subject_Personalization-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Lvxan/SEAL)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SEAL 用可微 top-k 掩码只改动人脸图像 5% 的空间位置，目标是打散冻结 VAE 编码器的潜变量方差，使扩散个性化后的身份相似度降到 0.15 以下，同时保住 41dB 以上的 PSNR 与 0.97 的 SSIM。**</p>

+ **Multimodal Judges Flag, Humans Decide: A Review-and-Edit Framework for AI-Generated Product Video Ads**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13178)
![architecture](https://img.shields.io/badge/Review_And_Edit_Harness-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/Anoki_Inc.-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/anoubhav/ad-review-and-edit)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 AI 产品短视频审片拆成产品、场景、发音、脚本、声音、字幕六个问题，由多模态判官按问题归类线索、人工逐条裁决并触发对应编辑工具，120 条广告 562 场景中人工判产品错占 60%，判官 AUC 0.84。**</p>

