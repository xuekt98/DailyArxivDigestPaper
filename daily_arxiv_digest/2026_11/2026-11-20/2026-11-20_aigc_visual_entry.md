<!-- direction: aigc_generation -->

+ **CueSplat: Learning to Schedule Sparse Deformation for Dynamic Gaussian Splatting on Edge Devices**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22095)
![architecture](https://img.shields.io/badge/CueSplat_Sparse_Deformation_Router-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiaotong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CueSplat 冻结预训练 4DGS 骨干，用轻量路由器挑选需要精确变形更新的高斯子集，其余走时序预测，在 Jetson AGX Orin 上最高加速 6.74×、Orin NX 8.15×，数据集平均 PSNR 最多只降 0.16 dB。**</p>

+ **ARG-Avatar: Animation-Rendering Guidance for Efficient Feedforward Avatar Reconstruction**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22207)
![architecture](https://img.shields.io/badge/ARGAvatar_FACRoPE_ITR-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University_Robotics_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ARG-Avatar 用 FACRoPE 注意力与中间 token 渲染，把 3D 动画渲染自带的几何对应关系显式注入前馈式 avatar 重建，仅 68M 参数即在 NeuMan 取得 30.82 dB，较 LHM++ 少 9× 参数、14× 算力却快约 6×。**</p>

+ **ProxySearch: Decoupled Inference-Time Scaling for Diffusion Models via Asymmetric Noise-Rank Transfer**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23929)
![architecture](https://img.shields.io/badge/ProxySearch_Asymmetric_Noise_Rank-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/GenGenAI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ProxySearch 测出蒸馏代理与教师在排序上高度不对称：闭式图像统计的 Spearman ρ 最高 0.80，语义打分只有 0.12 以内，于是用代理 1 步筛统计、教师做语义择优，在 FLUX-1024 上把统计目标收紧 21–23%。**</p>

+ **TRoPE: Topology-aware Relative Positional Encoding for 4D Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23933)
![architecture](https://img.shields.io/badge/TRoPE_Topology_Aware_RoPE-red)
![task](https://img.shields.io/badge/4D_Generation-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://akui1321.github.io/TRoPE)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TRoPE 用图拉普拉斯谱特征与多尺度扩散特征距离构造拓扑关系，通过旋转相位调制顶点与锚点注意力来抑制前馈式 video-to-4D 的粘连伪影，最差顶点误差降低 39.4%、分离失败率由 49.35% 降至 34.90%。**</p>

+ **Dual-Manifold Variational Autoencoders**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23964)
![architecture](https://img.shields.io/badge/DM_VAE_TRA_IGTS-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**双流形 VAE 把高维重建分支与低维拓扑骨架分支配对，用内部表示而非 DINOv2 等外部先验做拓扑正则，在 ImageNet-1K 上取得 rFID 0.12 与生成 FID50K 1.28，并能与 DINOv2 正交组合到 1.11。**</p>

+ **Freeforward4d: Annotation-free feed-forward 4d reconstruction of driving scenes**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24007)
![architecture](https://img.shields.io/badge/FreeForward4D_Prior_Reconciliation-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/East_China_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FreeForward4D 把冻结视觉先验的窗口相机、伪深度与 2D 轨迹统一校准进同一度量坐标系，无需数据集相机、激光雷达或 3D 框标注，在 Waymo 上取得 27.66 dB PSNR / 0.836 SSIM 并超过依赖标注的基线。**</p>

+ **PhysResponse: Probing the Physics of Video Generation with Controlled Interventions**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24419)
![architecture](https://img.shields.io/badge/PhysResponse_Physics_Probing-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Sun_Yat-sen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PhysResponse 用 20 类交互、72,000 条仿真视频构造物理参数响应基准，从生成视频反演重力、摩擦与初速：10 个图生视频模型的最优参数误差仍比物理正确视频高一个数量级以上，转折对双结果难同时复现。**</p>

+ **Jeveration: System One Models Now Generate**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24738)
![architecture](https://img.shields.io/badge/Jeveration_Typed_Decision_VLM-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Jeveration 把 System One 的并行决策范式用于图像生成，冻结 Qwen3.5-4B 只加 LoRA 并用共享随机状态协调并行预测，单次前向 78 ms 出一张 512×512 图，最高比 Janus-Pro-7B 快 122×，三种任务共用同一权重。**</p>

+ **Isthmus: Bridging Supervision Islands Restores Uncertainty and Stability in One-Step Flows**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23616)
![architecture](https://img.shields.io/badge/Isthmus_Landing_Edge_Supervision-red)
![task](https://img.shields.io/badge/Flow_Matching-magenta)
![organization](https://img.shields.io/badge/The_Ohio_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Isthmus 指出一步流采样器的失败来自训练时间对的「监督孤岛」：只把 5% 的训练对移到落地边接上对角线，不改网络与损失，脑 MRI 上一采样校准从 0.67 回到 0.96、与 64 步样本相关性从 0.58 回到 0.93。**</p>

<!-- direction: aigc_editing -->

+ **What Does Weight-Space Programming Add to Diffusion Editing? Program Construction versus Score-Guided Refinement**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22228)
![architecture](https://img.shields.io/badge/WSP_Program_Construction_Pipeline-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文用 24 个 TIMED 测试编辑做预注册对比，区分权重空间编程的程序构造与分数引导改写两阶段：一次性程序把 VLM 联合成功率抬高 10.0 分，而改写虽让 CLIP 涨 6.2 分却使联合成功率跌 9.7 分。**</p>

+ **Fast Training-Free Low-Light Video Enhancement with a Frozen Image Diffusion Prior**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22551)
![architecture](https://img.shields.io/badge/Temporal_Fusion_Offset_Propagation-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/City_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该方法在冻结的图像扩散先验上加时序输入融合与延迟启动的偏移传播：256×256 上比唯一的免训练视频方法 ZVRD 快 261× 且五项指标全面更优，1280×720 上较逐帧 8 步处理高 0.55 dB PSNR 并省 10% 时间。**</p>

+ **REVEAL: Reconstructing Video Amodal Content via Language and Flow Guidance**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22645)
![architecture](https://img.shields.io/badge/REVEAL_Flow_Guided_Amodal-red)
![task](https://img.shields.io/badge/Video_Inpainting-magenta)
![organization](https://img.shields.io/badge/University_of_Arkansas-green)
[![project](https://img.shields.io/badge/project-blue)](https://uark-aicv.github.io/REVEAL/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**REVEAL 用光流把前帧可见掩码 warp 进遮挡区充当形状先验、用文本同时驱动开放词表分割与纹理约束，在 Kubric 上取得 29.92 dB PSNR / 0.921 SSIM（基线 TACO 23.51 dB），并发布含 2,658 段视频的 LAVAT 长序列基准。**</p>

+ **LUTBench: Benchmarking Text-Driven Photographic Look Transfer**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23113)
![architecture](https://img.shields.io/badge/LUTBench_3DLUT_Look_Transfer-red)
![task](https://img.shields.io/badge/Style_Transfer-magenta)
![organization](https://img.shields.io/badge/The_University_of_Sydney-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LUTBench 收集 91 个 3D LUT 定义 91 种摄影外观，在 5,000 张 MIT-Adobe FiveK 照片上构造 455,000 组可复现输入-目标对，系统评测 16 种方法的 22 种配置，结论是更强的文本对齐并不保证更好的目标保真度。**</p>

+ **Beyond Additive Composition: Interventional Modeling of State-Dependent Cross-Degradation Responses for Composite Image Restoration**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23889)
![architecture](https://img.shields.io/badge/PROBE_Interventional_Cross_Degradation-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Xidian_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PROBE 指出复合退化在像素与 VAE 潜空间都违反可加性——非加性残差达复合潜变量偏移的 33.0%（雾-雪）与 35.7%（雾-雨），据此用状态相关的跨退化响应建模，在 CDD-11 上取得 30.77 dB / 0.898 SSIM 且显存仅 128 MiB。**</p>

<!-- direction: aigc_rl -->

+ **H3Remover: Reinforcing Video Object Removal without Paired Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24633)
![architecture](https://img.shields.io/badge/H3Remover_Source_Conditioned_Reward-red)
![task](https://img.shields.io/badge/RL_for_Video-magenta)
![organization](https://img.shields.io/badge/XPENG-green)
[![project](https://img.shields.io/badge/project-blue)](https://chenkangjie1123.github.io/H3Remover/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**H3Remover 用源条件奖励（目标移除、背景几何次序、保护区域外观）加冻结 HPSv3 感知反馈，在无配对目标下只调 LoRA 强化 MiniMax-H3 的视频移除：PSNR 提升 7.151 dB、确认移除从 40/80 升到 73/80。**</p>

