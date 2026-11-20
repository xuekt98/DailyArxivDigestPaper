<!-- direction: aigc_generation -->

+ **Spark-H3: Adaptive Block Sparse Attention for Video Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24256)
![architecture](https://img.shields.io/badge/Spark_Attn_Block_Sparse_Attention-red)
![task](https://img.shields.io/badge/Video_Acceleration-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/zechengtang/Spark-H3)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Spark-Attn 用 Spark-Reblock 递归重分块、Spark-Reweight 重标定压缩块注意力，在 MiniMax-H3 上以 10% 精确块密度换来 2.49 倍 DiT 加速与 24.81 dB PSNR，20% 密度可达 26.76 dB。**</p>

+ **Text Lives in the Guidance: Preventing Silent Text Rewriting in Cached Diffusion Transformers**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25382)
![architecture](https://img.shields.io/badge/GuideCache_Split_Cache_Guidance-red)
![task](https://img.shields.io/badge/Diffusion_Model-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**研究发现特征缓存会静默改写 DiT 渲染出的文字：TaylorSeer 在 2.9 倍 FLOPs 节省下把 Z-Image 词准确率从 62% 降到 46%。GuideCache 只在文本 token 上重算 CFG 两支，2.4 倍加速即可恢复全算力保真度。**</p>

+ **Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26040)
![architecture](https://img.shields.io/badge/Streaming_AAA_Causal_Video_Diffusion-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/Tencent_AIPD-green)
[![project](https://img.shields.io/badge/project-blue)](https://streamingaaa.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Streaming-AAA 用重写的因果视频 VAE、Diffusion Forcing 长上下文预训练和 DMD 后训练蒸馏，把 AAA 级游戏视频推到 1080p、43 FPS、198 ms 交互延迟，并在单张 A800 上支持长时流式生成。**</p>

+ **ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26389)
![architecture](https://img.shields.io/badge/ViDecide_Causal_Diffusion_Decisions-red)
![task](https://img.shields.io/badge/Video_Generation-magenta)
![organization](https://img.shields.io/badge/S-Lab_Nanyang_Technological_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://kevin-thu.github.io/ViDecide)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ViDecide 把视频生成训练改造成决策链式的因果状态转移并预测视觉 EOS，配合 Corrective Fine-tuning 无需策略梯度即修正失败决策，多基准平均严格成功率 83.8%，远高于标准微调的 23.3%。**</p>

+ **UltraTex: Aligning Physical Knowledge for High-Fidelity PBR Texture Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24941)
![architecture](https://img.shields.io/badge/UltraTex_Cascaded_MultiView_PBR-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/SSE_CUHKSZ-green)
[![project](https://img.shields.io/badge/project-blue)](https://ultratex.vercel.app/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**UltraTex 用两阶段级联多视图扩散生成 PBR 贴图：先联合预测 albedo 与世界空间着色法线，再以生成 albedo 加 VLM 材质语义 token 预测金属-粗糙度，152 个物体上 FID 111.2，专家盲评 4.31 分领先商用基线。**</p>

+ **Autoregressive View Model**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23417)
![architecture](https://img.shields.io/badge/Autoregressive_View_Model-red)
![task](https://img.shields.io/badge/Scene_Generation-magenta)
![organization](https://img.shields.io/badge/Meta-green)
[![project](https://img.shields.io/badge/project-blue)](https://autoregressive-view-model.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AVM 把场景当作视角流来生成而不构建显式 3D 表示，用 N-in-1-out 流匹配微调 140 亿参数的预训练视频 DiT 并扩到约 800 万训练片段，FID 18.69 领先次优基线 25.04。**</p>

+ **Layer-Matched Sparse Attention for Low-Redundancy 3D Reconstruction**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23554)
![architecture](https://img.shields.io/badge/Layer_Matched_Sparse_Attention-red)
![task](https://img.shields.io/badge/4D_Reconstruction-magenta)
![organization](https://img.shields.io/badge/BRAC_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LMSA 用每层 log-mass 缺失统计量（logit 方差）区分匹配层与扩散层：匹配层保留精确注意力，扩散层改用共享 hub 键，在 13 个低冗余场景 32 视图下与稠密注意力只差 1.4 AUC@5，AVGGT 则差 10.3。**</p>

+ **EyeDiT: Anatomy-Grounded Multi-Modal Eye Generation and Simulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23670)
![architecture](https://img.shields.io/badge/EyeDiT_Anatomy_VAE_Latent_DiT-red)
![task](https://img.shields.io/badge/3D_Generation-magenta)
![organization](https://img.shields.io/badge/Meta_Reality_Labs-green)
[![project](https://img.shields.io/badge/project-blue)](https://lyhan12.github.io/eyedit)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EyeDiT 用多模态解剖 VAE 融合 OCT 体数据、解剖点云与近眼图像，再由 Eye Latent DiT 条件于光轴、瞳孔半径与身份生成潜变量，单视图新视角 24.9 dB，眼动模拟-现实差距仅 3.5°。**</p>

<!-- direction: aigc_editing -->

+ **DAWN: Robust Neural Blind Deconvolution via Alternating Wiener Guidance**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25621)
![architecture](https://img.shields.io/badge/DAWN_Alternating_Wiener_Guidance-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/University_of_Michigan-green)
[![project](https://img.shields.io/badge/project-blue)](https://deepthink-umich.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DAWN 是免训练数据的盲反卷积 DIP 框架，交替把 Wiener 反卷积估计注入网络输入并用网络自身先验精修，同时对图像与核网络施加自编码正则，Levin σ=0.1 上比次优基线高最多 4.5 dB。**</p>

+ **AesDistill: Distilling Generative Aesthetics for Image Color Enhancement**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25635)
![architecture](https://img.shields.io/badge/AesDistill_Confidence_Weighted_Student-red)
![task](https://img.shields.io/badge/Style_Transfer-magenta)
![organization](https://img.shields.io/badge/The_University_of_Sydney-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AesDistill 用四个开源生成模型作教师产出 64,644 张编辑图（约 3,360 H100 GPU-小时），蒸馏出 1.13M 参数的学生模型做色彩增强，在 12 个审美与 4 个画质评估上综合排名仅次于教师，领先全部 20 个基线。**</p>

+ **From Restoration to Redrawing: Revitalizing Ancient Chinese Characters by SVG Code Generation and Editing**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24084)
![architecture](https://img.shields.io/badge/ReDraw_SVG_Code_Generation-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/University_of_Liverpool-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ReDraw 把汉简字修复从图像到图像改写成 SVG 代码生成与编辑，两阶段先用骨架链式思维补全残缺笔画再生成轮廓，配 GRPO 结构感知奖励，600 个合成样本上 SSIM 0.9225、LPIPS 0.0850。**</p>

+ **DetailScale-SR: Decoupling Restoration and Continuous Detail Control for Real-World Super-Resolution**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24212)
![architecture](https://img.shields.io/badge/DetailScale_Preference_Conditioned_SR-red)
![task](https://img.shields.io/badge/Image_Editing-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://modelscope.cn/models/DiffSynth-Studio/Qwen-Image-2.1-SR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DetailScale-SR 把连续细节标量注入冻结修复模型的注意力层，同一低分输入可在保守修复与纹理增强之间连续过渡：RealSR 上 s 从 0 到 1 时 PSNR 由 26.69 降到 25.48、MUSIQ 由 60.94 升到 65.53。**</p>

<!-- direction: aigc_rl -->

+ **RL Post-Training in Diffusion Transformers Is Activation Steering**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26627)
![architecture](https://img.shields.io/badge/Activation_Steering_Vectors-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Virginia_Tech-green)
[![project](https://img.shields.io/badge/project-blue)](https://rl-is-steering.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文证明扩散 Transformer 的 RL 后训练增益大部分只是常数偏移：SD3.5-M 上仅 0.29M 参数的 188 个定长 steering 向量就能复现 RL 微调 LoRA 90.0–96.3% 的奖励增益，且对所有提示词与种子通用。**</p>

+ **CANDOR: Contrastive Self-Denoising Rewards for Label-Free Text-to-Image Post-Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25457)
![architecture](https://img.shields.io/badge/CANDOR_Contrastive_Denoising_LogRatio-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/jhlee0619/candor)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CANDOR 用空提示与条件提示在共享噪声探针下的去噪误差对数比构造无标签内在奖励，同提示词成对排序正确率 60% 与 63%，作为 Flow-GRPO 唯一奖励把 GenEval 从 0.474 提到 0.706。**</p>

+ **Keystone: Judging Previews at Key Steps for Test-Time Search in Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25530)
![architecture](https://img.shields.io/badge/Keystone_Typed_Question_Judge-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/UIUC-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Keystone 把提示词编译成关于物体、数量、颜色与位置的定型问题，交由现成多模态决策模型在早期预览上判定，在 GenEval 加 SD3.5-Medium 上用不到 best-of-8 一半算力即显著超过所有其它验证器。**</p>

+ **Reinforcing Few-Step Diffusion Models via Shadow Posterior Matching**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25998)
![architecture](https://img.shields.io/badge/Shadow_Posterior_Matching-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/shadow-posterior/code)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SPM 通过把少步生成器输出重新加噪成 shadow 输入、从 shadow 后验取奖励信用，解决少步模型不是 score 模型拿不到信用的问题：4 步生成器上 GenEval 0.94、OCR 0.96、PickScore 23.84，均高于最强少步基线。**</p>

+ **EVA-RSI: Recursive Self-Improvement of Video Evaluators for Judging Temporal Quality**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23890)
![architecture](https://img.shields.io/badge/EVA_RSI_Multi_Agent_Evaluator-red)
![task](https://img.shields.io/badge/Reward_Model_Video-magenta)
![organization](https://img.shields.io/badge/Roblox-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EVA-RSI 用时间反转、抽帧等受控改动构造固定目标考卷，配合多智能体提案与纳什谈判做视频评测器的递归自我改进，主维度分数从 0.706 提到 0.906，在 VBench 动态子集上为 21 个受测模型中的最高分。**</p>

