# 2026-10-30 - 强化学习 · LLM 后训练与对齐 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Aligning Medical Vision Language Models at the Capability Boundary with Entropy Adaptive Rubric Grounding**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39835)
![architecture](https://img.shields.io/badge/MedCBR_DBPO_EGPO-red)
![task](https://img.shields.io/badge/Preference_Optimization-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MedCBR 用两阶段对齐医学视觉语言模型：先在模型能力边界上做难度加权的反事实偏好优化，再按预测 entropy 激活临床 rubric 做接地强化学习，在六个医学 benchmark 上取得 61.2% 平均准确率。**</p>
+ **There Is No Free Lunch in RLVR: Every pass@1 Gain Has a pass@k Price**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39295)
![architecture](https://img.shields.io/badge/RLVR_Exponential_Tilt_Pass1_Passk_Price-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Unknown-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文证明 RLVR 可建模为对基座策略的 exponential tilt，任何抬升 pass@1 的更新都必须付出压低某些 prompt pass@k 的代价，并给出用 sign variation 界定的交叉点数量与可测量的价格。**</p>
+ **Reasoning or Pattern Exploitation? Mechanistic Insights from RL-Trained Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39182)
![architecture](https://img.shields.io/badge/GRPO_SAE_Representation_Tracing-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在可穷举的井字棋域上追踪 GRPO 训练后的 LLM 表征，稀疏自编码器显示模型更依赖 prompt 里的显式信息而非棋盘对称与战术概念，论文据此认为 RL 只是重组了主导特征。**</p>
+ **Distributional Reward Calibration and Budget-Neutral Credit Assignment for Multimodal RLVR**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40250)
![architecture](https://img.shields.io/badge/TACE_OptimalTransport_Baseline_RankCalibrated_Credit-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Shenzhen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TACE 把 GRPO 的 advantage 分解为样本级基线与 token 级信用分配两段，用一维 optimal transport 统一跨任务奖励律并在轨迹内重分配守恒的信用，在多模态推理套件多数 benchmark 上取得最强结果。**</p>
+ **H$^2$R: Hierarchical Hint-Based Reward for Mathematical Reasoning via Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39934)
![architecture](https://img.shields.io/badge/H2R_Hierarchical_Hint_Reward-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/New_York_University_Shanghai-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**H²R 把数学问题的子问题结构当作层级中间条件信号用于 RLVR 训练，并配套提出分层数学基准 HiMath，Qwen2.5-Math-7B 的准确率从 30.4% 提升到 39.1%，Oracle hint 下可达 45.6%。**</p>
+ **Grounding Multimodal Reasoning with Evidence-Ablated Negatives**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39237)
![architecture](https://img.shields.io/badge/EVAN_EvidenceAblated_Negatives-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/University_of_Maryland,_College_Park-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/DawnLIU35/EVAN.git)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EVAN 通过遮蔽最具判别力的图像 patch 构造无视觉依据的负回复，把这些 evidence-ablated negatives 作为有界辅助信号用于多模态 RLVR，在困难推理 benchmark 上缓解模态不平衡并优于强基线。**</p>
+ **SCARL: Sequence Confidence-Aligned Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40407)
![architecture](https://img.shields.io/badge/SCARL_Sequence_Confidence_Aligned_RL-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Baidu_Frontier_Research_Department-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/kezhh163/scarl)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SCARL 指出 RLVR 中策略置信度与奖励认证结果之间存在失配，用 group-relative 置信度与 advantage 的 alignment gap 重塑但不改变符号，在 Qwen3-4B-Base 上相对 DAPO 提升 2.4 点 Pass@32。**</p>
+ **Training language models in simulation for psychiatric intake**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40476)
![architecture](https://img.shields.io/badge/MultiTurn_RL_Simulation_Psychiatric_Intake-red)
![task](https://img.shields.io/badge/RLHF-magenta)
![organization](https://img.shields.io/badge/Google_DeepMind-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在精神科初诊模拟环境中做多轮强化学习，随机双盲交叉实验显示训练后 agent 在 76.7% 的匹配场景对中优于基座模型，并把急性安全风险漏诊率从 30.5% 降到 12.9%。**</p>
+ **When Does Closed-Loop Curriculum Adaptation Help GRPO? An Analysis on Countdown**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39056)
![architecture](https://img.shields.io/badge/ClosedLoopGaussian_Curriculum-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Texas_Christian_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/yuvrajpant56/Closed_Loop_Curriculum)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CLOSEDLOOPGAUSSIAN 用周期性难度探测动态调节 GRPO 训练的课程节奏与采样展宽，在符号算术推理上超过 vanilla GRPO 与固定开环课程，最强增益出现在 group-relative 信号最有信息量的中等难度区间。**</p>
+ **Reward-Adaptive Co-Evolution of Policy and Rubric**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40096)
![architecture](https://img.shields.io/badge/RACE_RewardAdaptive_Policy_Rubric_CoEvolution-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RACE 用奖励自适应的策略与 rubric 协同演化：group 层路由 informative 组并缓存 rubric 失败样本，phase 层在奖励饱和与改进平台期之间自动切换，在全部八个任务上超过最强固定交替基线。**</p>
