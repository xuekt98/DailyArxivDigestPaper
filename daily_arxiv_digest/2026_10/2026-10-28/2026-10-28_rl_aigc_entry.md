# 2026-10-28 - 生成式内容模型强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **How Much Can Best-of-N Help a World Action Model? Measuring Selectable Headroom and Realizing It in Closed Loop**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37196)
![architecture](https://img.shields.io/badge/Selectable_Headroom_Counterfactual_Protocol-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**量化 Best-of-N 到底能带来多少收益：论文提出基于逐位可复现分支、重复续跑、留出 oracle 与共同随机数的去噪反事实协议，测得三个世界动作模型的可选择份额仅 24%–66%（标准估计高估），并据此构建失效门控选择器，把闭环成功率从 76.9% 提到 81.6%、未见任务从 62.6% 提到 69.8%。**</p>
+ **From Structural Feedback to Prompt Policies: Learning Faithful Text-to-Image Prompt Editors**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36146)
![architecture](https://img.shields.io/badge/StruPO_Scene_Graph_GRPO-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**StruPO 用校准场景图作为策略条件与图像监督的共享表征，把外部结构批评转成可复用编辑策略的训练信号：删除/重排/插入提供 token 对齐修改，平滑奖励塑形保留定位置信度并在计算组相对优势前平均多张生成图，在四个冻结骨干上改善忠实度-美感折中与关系保真度。**</p>
+ **ExecDiffuser: Closing the Sample-to-Execution Gap in Diffusion Planning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36837)
![architecture](https://img.shields.io/badge/ExecDiffuser_Execution_Grounded_Selection-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Beijing_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出「样本到执行差距」：生成式规划器常按能生成的轨迹评估，但闭环结果取决于提交给控制的那一条，只提升提案质量反而可能让执行更差；ExecDiffuser 用共享执行语义耦合候选生成、轨迹选择与后续重规划，并用学习到的候选条件发布效用挑选轨迹，在 nuPlan/InterPlan/NAVSIM 上统一五种子协议平均 85.62。**</p>
+ **Nemotron-Labs-Diffusion-Uni: Elastic Self-Refining Unified Diffusion LLM with Cross-Paradigm On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36466)
![architecture](https://img.shields.io/badge/NLD_Uni_Cross_Paradigm_OnPolicy_Distillation-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**NLD-Uni 是统一的离散扩散大语言模型：跨范式在线蒸馏把自回归 VLM 的理解能力与连续流模型的生成能力迁移到同一 DLLM，渐进自精炼扩散过程逐步加噪每个 token 并允许推理中间提交，Elastic-MoT 架构提供统一模型的多个弹性视图，在问答、推理、定位、文生图与编辑上达到统一 DLLM 最优。**</p>
+ **Live-OPSD: On-Policy Self-Distillation for Proactive Streaming Large Video Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36959)
![architecture](https://img.shields.io/badge/Live_OPSD_Privileged_Hint_Distillation-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Alibaba_(Qwen_Business_Unit)-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向流式多模态助手的主动响应决策：Live-OPSD 用仅训练期可得的特权提示来监督策略自己的输出——策略先仅凭上下文生成续写，同一模型带着证据提示重评该续写并据此指导无提示策略；在 Qwen3-Omni-30B-A3B 上 LiveProBench 平均 59.64，比最强 continued-SFT 基线高 5.26 分。**</p>
+ **MVRCap: Towards Comprehensive Video Captioning via Hierarchical Multi-Dimensional Verifiable Rewards**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36838)
![architecture](https://img.shields.io/badge/MVRCap_Hierarchical_Verifiable_Rewards-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/Xiamen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把视频字幕生成重构为由结构化验证引导的 RL 任务：核心的细粒度可验证奖励由层级概念覆盖、事实性验证与简洁性约束三根支柱构成，辅以六维度结构化标注的 MVRCap-SFT 数据集初始化策略，在 VDC、CAPability 与 VC4VG 上取得当前最优。**</p>
+ **ScIntBench: Physical Interaction Plausibility in 3D Scene Generation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37326)
![architecture](https://img.shields.io/badge/ScIntBench_Simulation_Readiness-red)
![task](https://img.shields.io/badge/GenEval-magenta)
![organization](https://img.shields.io/badge/The_University_of_Western_Australia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向文本条件 3D 室内场景生成的综合基准 ScIntBench：把评测从语义与静态物理扩展到交互期物理可靠性，提出标准化物理交互测试以评估动作可执行性、交互后物理完整性与动态合理性，对比 DiffuScene、LayoutVLM、Holodeck、SAGE 等多种生成范式。**</p>
+ **ALADDIN: Adversarial Latent Diffusion Distillation for One-Step Identity Swapping**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37503)
![architecture](https://img.shields.io/badge/ALADDIN_Adversarial_Latent_Distillation-red)
![task](https://img.shields.io/badge/CFG_Distillation-magenta)
![organization](https://img.shields.io/badge/Constructor_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**一步人脸交换模型 ALADDIN：直接从预训练多步流匹配模型初始化，在身份保持与目标保持约束下做对抗训练，无需预先获得蒸馏模型，因而能直接使用更大的 FLUX 与 PuLID 获得更好的身份条件，在一步模型中取得当前最优质量。**</p>
+ **Taming Noise Initialization for Zero-shot Video Restoration with Image Diffusion Priors**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37290)
![architecture](https://img.shields.io/badge/TINDER_Noise_Init_Trajectory_Attention-red)
![task](https://img.shields.io/badge/Classifier_Guidance-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**零样本视频复原方法 TINDER：直接对受损视频帧做 DDIM 反演生成初始噪声以保留内在时序相关性，再用自适应噪声混合抑制反演中编码的退化模式并逐步导向高斯分布，配合度量引导的轨迹注意力强化跨帧一致性，在 DAVIS、REDS4 与 Set8 上优于既有零样本方法。**</p>
+ **Provenance Signatures for Low Rank Adaptations of Image Diffusion Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36933)
![architecture](https://img.shields.io/badge/Provenance_Signatures_LoRA_Scores-red)
![task](https://img.shields.io/badge/Aesthetic_Scoring-magenta)
![organization](https://img.shields.io/badge/University_of_Edinburgh-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向模型审计的黑盒溯源协议：只依据模型生成图像集合的内在维度构造签名，用于判断某服务是否在标准模型的 LoRA 适配版上运行；论文发现非常接近真实图像处不同模型的打分函数行为存在差异，为闭源生成服务的合规审计提供了不依赖参数访问的检测手段。**</p>