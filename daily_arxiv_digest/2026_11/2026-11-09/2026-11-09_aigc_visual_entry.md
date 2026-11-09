<!-- direction: aigc_generation -->

+ **Scale as a Modality: Multi-Scale Pixel-Space Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08802)
![architecture](https://img.shields.io/badge/MS_pDiT-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/TikTok-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把空间尺度当作模态的多尺度像素空间扩散 Transformer，各尺度独立流配合紧凑联合注意力实现双向交互，ImageNet 256 上尺度数从 2 增到 5 可使 FID 从 4.39 降到 1.43。**</p>

+ **InstaGen: Group-Shared Importance Sampling for Fast Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08610)
![architecture](https://img.shields.io/badge/InstaGen-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/IIT_Bombay-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把块稀疏注意力的块选择重述为重要性采样，精确块全算加按注意力比例抽样并用逆概率重加权，在 Wan2.1 视频扩散上同等密度下比 SVG2 高 3.4 dB PSNR。**</p>

+ **Trajectory Forcing: Exploiting Diffusion Trajectories for Autoregressive Long Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09096)
![architecture](https://img.shields.io/badge/Trajectory_Forcing-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Huawei_Noah_Research_Institute-green)
[![project](https://img.shields.io/badge/project-blue)](https://wangbohan97.github.io/Trajectory-Forcing/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自回归视频扩散不再只以上一 chunk 为条件，而是让模型条件化前一 chunk 的完整去噪轨迹，5 秒 VBench 总分 85.15，30 秒长视频达到 73.98。**</p>

+ **MotionCore: A Latent Neural Simulator for Video Generation with Rigid-Body Dynamics**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08904)
![architecture](https://img.shields.io/badge/MotionCore-red)
![task](https://img.shields.io/badge/Motion_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Tokyo-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用隐空间神经模拟器预测刚体物体级物理状态，再转成空间对齐的潜变量控制信号驱动可控视频扩散，兼顾物理一致性与轨迹服从，并在 Physics-IQ-Verified 严格子集上做量化对照。**</p>

+ **Align3D: Image-Structure Co-Aligned 3D Scene Generation with Observability-Aware Fidelity-Preserving Guidance**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08861)
![architecture](https://img.shields.io/badge/Align3D-red)
![task](https://img.shields.io/badge/Scene_Generation-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**图像条件的室内布局扩散模型，按预测置信度在图像与场景图间做共对齐，并用可观测性引导让欠观测区域吸收物理先验，3D-FRONT 上 CLIP 0.925 且推理最快。**</p>

+ **OmniLatent: Unified Latent for 3D Part Modeling**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09055)
![architecture](https://img.shields.io/badge/OmniLatent-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把几何、形变、外观与二值部件 ID 一起编码进统一潜空间，单张输入图一次前向即生成带部件的 3D 资产，无需再做网格后处理分割，并支持点提示分割与遮挡部件补全。**</p>

+ **UniRGBA: Unifying RGB and Alpha in Pretrained Video Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09069)
![architecture](https://img.shields.io/badge/UniRGBA-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/ByteDance-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把视频扩散的 RGB 通路最小化扩展为原生 4 通道 RGBA，VAE 零初始化扩通道且仅微调约 5% 参数，下游用标准 DoRA 适配，透明度与画质双双提升。**</p>

+ **Emo-LiveSync: Real-Time Universal Lip Synchronization with Explicit Emotion Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09074)
![architecture](https://img.shields.io/badge/Emo_LiveSync-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Klleon_AI_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**基于 LivePortrait 的变形式肖像动画框架，把音频对齐到蒸馏自视频到运动模型的隐式运动空间，兼顾实时推理、跨风格角色泛化与显式情绪控制，覆盖多语种非人类角色。**</p>

+ **Video2Asset: Online Construction of Persistent 3D Street-Scene Assets**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09661)
![architecture](https://img.shields.io/badge/Video2Asset-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Cooperative_Medianet_Innovation_Center-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以占用率为中间表示在线把多视角视频累积为持久可编辑的 3D 街景资产，靠历史载体引导与累积证据关联在遮挡下守住物体身份，nuScenes 上碎片率下降 15.4%。**</p>

<!-- direction: aigc_editing -->

+ **AR-Edit: Training-Free Autoregressive Video Editing without Inversion**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09795)
![architecture](https://img.shields.io/badge/AR_Edit-red)
![task](https://img.shields.io/badge/Video_Editing-magenta)
![organization](https://img.shields.io/badge/Team_ARAI_Universite_Paris-Saclay_CNRS_LISN-green)
[![project](https://img.shields.io/badge/project-blue)](https://marghovo.github.io/AR-Edit/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**分析蒸馏自回归视频扩散的自注意力动态，发现查询与键跨时间步稳定而值发散，据此一次前向缓存源视频的值并选择性注入，即可免训练、免反演地做流式视频编辑并保住源内容。**</p>

+ **A Bridge from Paste to Place: Physics-Guided One-Step Image Composition via Object-Scene Interaction**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09387)
![architecture](https://img.shields.io/badge/Paste2Place-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Transsion-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**物理引导的流匹配一步图像合成模型，用反照率-着色-残差分解重合成同时完成重光照与场景效果，配套 86,273 对训练数据与 1,500 例评测基准，质量与速度双优。**</p>

+ **How are viral trends different from educational and commercial uses of LLM image generation and editing? A privacy-preserving descriptive analysis**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08749)
![architecture](https://img.shields.io/badge/Urania-red)
![task](https://img.shields.io/badge/Instruction_Editing-magenta)
![organization](https://img.shields.io/badge/Google_Behavioral_Economics-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用带严格差分隐私的聚类框架分析 210 万条 Nano Banana 图像生成与编辑对话，划分五类场景并在 21 项使用特征上比较，不暴露任何单条提示，给出真实编辑用例的分布基线。**</p>

<!-- direction: aigc_rl -->

+ **SIFR: Stable Signed Flow Reinforcement**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09175)
![architecture](https://img.shields.io/badge/SIFR-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://research.nvidia.com/labs/cosmos-lab/sifr/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把流模型的在线奖励微调写成带约束的优化问题，用带符号优势补上解拟合信号，再用拉格朗日乘子把速度漂移限制在预算内，12 组骨干-奖励组合上持平或更优且长训不塌。**</p>

+ **PhyCAD: Physics-Aware Text-to-CAD Generation via Hierarchical Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09401)
![architecture](https://img.shields.io/badge/PhyCAD-red)
![task](https://img.shields.io/badge/RL_for_3D_Generation-magenta)
![organization](https://img.shields.io/badge/USTC-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/PhysAGI/PhyCAD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让语言模型在几何与物理约束下生成可执行 CadQuery 程序，用自动 CAD-CAE 验证器反馈，并以分层平衡优势改进 GRPO 的约束满足，覆盖几何与有限元两类约束。**</p>

+ **Video-Coder: Reinforcing Agentic Coding for Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09894)
![architecture](https://img.shields.io/badge/Video_Coder-red)
![task](https://img.shields.io/badge/RL_for_Video-magenta)
![organization](https://img.shields.io/badge/University_of_Central_Florida-green)
[![project](https://img.shields.io/badge/project-blue)](https://cywang735.github.io/Video-Coder/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**训练一个会写代码搭 3D 场景并渲染草稿视频的智能体，把结构与运动信号交给下游生成器，配合执行与视频双奖励及退火策略，在 PhyGenBench 与 VBench-2.0 上大幅提升可控性。**</p>

