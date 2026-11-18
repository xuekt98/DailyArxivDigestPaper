<!-- direction: aigc_generation -->

+ **FaceRiff: Data-Efficient Unified Text-to-3D Face Asset Synthesis via Geometric Conditioning**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21867)
![architecture](https://img.shields.io/badge/FaceRiff_UV_Asset_Diffusion-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Electronic_Arts-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在共享 UV 空间用文本直接生成网格、光照无关反照率与孔隙级位移，只需 2,049 张扫描、单卡训练且每任务只动 2.93% 参数，盲测中 45 位从业者认为其真实感明显优于 DreamFace。**</p>

+ **Hierarchical Diffusion Transformer for End-to-End Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22962)
![architecture](https://img.shields.io/badge/Hierarchical_Diffusion_Transformer-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://nicholas0228.github.io/HiT-webpage/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让像素空间扩散自己长出视觉层级：两级 2 倍分组把 token 数逐级压缩，ImageNet 256 拿到 1.48 FID 且只用 JiT 约 40% 的训练 FLOPs，文生图以约 6 倍更少参数超过 UniLiP-3B。**</p>

+ **FastFrames: Video Generation at Interactive Latency**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23226)
![architecture](https://img.shields.io/badge/FastFrames_AR_Video_Diffusion-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/Apple-green)
[![project](https://img.shields.io/badge/project-blue)](https://apple-aiml-research.github.io/ml-fastframes/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**拆掉自回归视频扩散的隐性开销：VAE 解码从 147 ms 降到 0.9 ms、DiT 评估从 41.6 ms 降到 16.4 ms，1.3B 版每帧 36 ms 进入 50 ms 交互区并支持相机与物理条件生成。**</p>

+ **Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22287)
![architecture](https://img.shields.io/badge/DWD_Dual_Head_Diffusion_Transformer-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://hanshengchen.com/dwd)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让扩散 Transformer 直接吐像素：保留去噪头负责采样、并联线性头做最终渲染，免掉 VAE 解码器，ImageNet FID 降到 1.43、Wan 视频形变误差减少 23%，FLUX.2 每图省 10.47 TFLOPs。**</p>

+ **Sample-Aligned Decoders for Latent Generative Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22458)
![architecture](https://img.shields.io/badge/Sample_Aligned_Decoder-red)
![task](https://img.shields.io/badge/Tokenizer_Compression-magenta)
![organization](https://img.shields.io/badge/Institute_of_Computing_Technology_Chinese_Academy_of_Sciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://torpedo2003.github.io/SAD/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**冻结生成器、只后训练解码器来对齐生成潜变量的分布：REPA-E 的 FID-50K 从 1.15 降到 0.98，DiT-XL/2 从 2.30 降到 2.13，训练仅 0.9 GPU 小时且推理零额外开销。**</p>

+ **MAVE: Reconstructing Editable 3D Blockouts from Film Shots**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22464)
![architecture](https://img.shields.io/badge/MAVE_Agentic_Blockout_Reconstruction-red)
![task](https://img.shields.io/badge/Scene_Generation-magenta)
![organization](https://img.shields.io/badge/GigaAI-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/yfChang-cv/MAVE)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把电影镜头还原成可编辑的 Blender 灰模场景：度量观测加 agent 建模与程序化校验，MAVEBench 上比原生基线高 27.5–41.1 分，每镜头 API 成本仅 0.054 美元，并公开 3000 对训练数据。**</p>

+ **PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22717)
![architecture](https://img.shields.io/badge/PCRG_Reference_Token_Pruning-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/Anorak_Games-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**无需训练就能剪掉参考视频 token：按潜变量冗余度与 VLM 注意力分成剪枝、缓存、保留三档，MiniMax-H3 上端到端加速 1.57 倍而 VBench 质量仅降 0.24%。**</p>

+ **Pixel is All You Need**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22820)
![architecture](https://img.shields.io/badge/PixelSpace_Canvas_Reasoner-red)
![task](https://img.shields.io/badge/Image_Generation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://bxzzcj.github.io/pixel-is-all-you-need)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**只用像素、不给任何文本 token 的一族生成模型：能读题、逐帧写中间步骤再作答，误差随规模按幂律下降，130M 参数时 GRPO 把应用题准确率从 23.7% 推到 84.6%。**</p>

+ **LOCUS: Causal Support Windows for Attribute Control in Autoregressive Image Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22867)
![architecture](https://img.shields.io/badge/LOCUS_Causal_Support_Window-red)
![task](https://img.shields.io/badge/Controllable_Generation-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用因果支撑窗口定位该改哪一段：结构属性在前 48–84 步、外观属性在 163–232 步才可干预，据此路由的测试时优化把 Janus-Pro 的 GenEval++ 从 24.6% 提到 46.8%，单轮修复率 48.1%。**</p>

+ **BRepA: Graph-Based B-Rep Pretraining for Unified CAD Understanding and Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22903)
![architecture](https://img.shields.io/badge/BRepA_Dual_MAE_BRep_Encoder-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Technical_University_of_Munich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为 CAD 边界表示做几何加拓扑双路掩码预训练：13.5M 参数在 1% 标注下把 mIoU 从 35.06 提到 67.58，并让规模大 20 倍的 BrepDiff 训练速度接近翻倍、收敛质量更好。**</p>

<!-- direction: aigc_editing -->

+ **PromptPack: Training-Free Augmentation of Diffusion Editors for Intent-Aligned Spatial and Semantic Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21865)
![architecture](https://img.shields.io/badge/PromptPack_Regional_Prompt_Packing-red)
![task](https://img.shields.io/badge/Layout_Control-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**免训练给扩散编辑器补上空间语义控制：Keep/Permit/Modify 三态门控加区域提示词打包路由，三套集成上受保护区像素误差降到 10^-6 量级，用户偏好率 87.2%。**</p>

+ **Diagnosing and Correcting Skin-Tone Color Casts in Ultra-Lightweight Photo Retouching Networks**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22106)
![architecture](https://img.shields.io/badge/UltraLight_HistCond_Retouch_Net-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/SNOW_Corporation-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**诊断并修正超轻量修图网络残留的肤色绿偏：零参数的肤色蒙版非对称绿偏损失把 FFHQ 上的异常率从 68.1% 降到 2.2%，整帧 PSNR/SSIM 只变 0.13 dB 与 0.004。**</p>

+ **SandBAR: A Band-Asymmetric Architecture for Underwater Image Restoration with Removable Frequency Scaffolding**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22355)
![architecture](https://img.shields.io/badge/SandBAR_SPARK_Band_Asymmetric-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Kings_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**按频带不对称组织的水下恢复架构：低频修色、高频保细节，三域均值 27.19 dB 领先已发表结果约 1.0 dB，训练期的频域脚手架在推理期被完全移除，参数与 FLOPs 反而更省。**</p>

+ **ConserveEdit: Source-Anchored Transactions for Drift-Bounded Iterative Image Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22724)
![architecture](https://img.shields.io/badge/ConserveEdit_Source_Anchored_Contract-red)
![task](https://img.shields.io/badge/Instruction_Editing-magenta)
![organization](https://img.shields.io/badge/University_of_California_Los_Angeles-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把迭代编辑当成对着源图的事务：每步分别判定目标进展、漂移与画质，失败即回滚，1,053 条 MagicBrush 测试上受保护内容的违规率从 48% 降到 2%，约束成功率升到 53%。**</p>

<!-- direction: aigc_rl -->

+ **RiDEx: Reward-Informed Directional Exploration for Diffusion Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22052)
![architecture](https://img.shields.io/badge/RiDEx_Directional_Exploration-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](http://gary.ac.cn/RiDEX/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让扩散后训练朝奖励相关的方向探索：在速度场子空间内做等幅正负扰动并用奖励差构造局部监督，四个任务峰值奖励均为第一，HPSv2 追平目标快 15 倍、PickScore 快 29 倍。**</p>

+ **Motion-Aware Reward Modeling for Instruction-Guided Video Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22495)
![architecture](https://img.shields.io/badge/MotionAware_Reward_Model-red)
![task](https://img.shields.io/badge/Reward_Model_Video-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**修掉视频编辑奖励模型的运动塌陷：显式输入帧间动态并用运动抑制与伪造运动负样本训练，VE-Bench 上偏好被压制候选的比例从 97% 降到 0%，人类 MOS 相关仍保持 0.57。**</p>

+ **When Anchors Shift the Target: Advantage-Gated Adaptation for Diffusion Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23038)
![architecture](https://img.shields.io/badge/AGA_Advantage_Gated_Anchoring-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Posts_and_Telecommunications-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用无参数门控拆开扩散 RL 的正负反馈：负优势走移动策略切线、正优势保留原回归目标，三项任务分最高且 DrawBench 画质不塌，额外代价只有零新增超参。**</p>

