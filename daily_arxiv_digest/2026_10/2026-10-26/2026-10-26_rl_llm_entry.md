# 2026-10-26 - LLM 后训练的 RL（RLHF / DPO / GRPO / RLAIF / RLVR） 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Direction-Aware Token Credit Assignment with Reward-Model Gradients**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32772)
![architecture](https://img.shields.io/badge/Reward_Gradient_Credit-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出 GRPO 的共享优势更新并不总是指向提高该 token 的奖励；DATC 把冻结奖励模型的梯度映射到策略 logit 空间，用奖励方向与采样动作更新方向的对齐度分配 token 权重，同时保持优势的符号与均值。**</p>
+ **SOPO: Socratic Guided Policy Optimization for Span-Level Hallucination Detection**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32212)
![architecture](https://img.shields.io/badge/Socratic_Multi_Turn_RL-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Patsnap_Pte._Ltd.-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/patsnap/SOPO)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把「苏格拉底式提问」做成 rollout 期的教师干预来缓解跨度级幻觉检测的奖励稀疏，再用轮次级优势缩放压制长度膨胀；4B 模型在 RAGTruth 上超过 GPT-5，并开源 1.7B/4B 权重。**</p>
+ **From Visual Affinity to Learning Credit in Multimodal Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32324)
![architecture](https://img.shields.io/badge/Outcome_Conditioned_Visual_Credit-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/HKUST_Guangzhou-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出仅凭视觉亲和度加权是危险的：视觉观察在后续推理失败时会被放大负优势更新。OVC 改用正负优势响应的均值对比来标定视觉证据，形成保持符号的 token 权重，零额外奖励模型即可提升六个基准均分 1.86–2.39 个百分点。**</p>
+ **MS-TTRL: Breaking the Frequency Conflict in Multiple-Solution Test-Time Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32234)
![architecture](https://img.shields.io/badge/Outcome_Level_Self_Verification-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多解任务里「生成频率」同时被用于估正确性与保多样性，二者天然冲突；MS-TTRL 用结果层面自验证获得与频率无关的正确性估计，频率只留给多样性，Recovery Rate 平均提升 19.13 个百分点。**</p>
+ **Pseudo-Labels as Rewards, Not Targets: Group-Relative Policy Optimization for Semi-Supervised ASR**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32572)
![architecture](https://img.shields.io/badge/GRPO_For_Semi_Supervised_ASR-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Idiap_Research_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**同一份伪标签，改当 GRPO 的奖励参考而不是 SFT 的目标：银行领域相对 WER 改善 29.3%–56.2%，且机制清楚——SFT 几乎 100% 复现教师错误，GRPO 只传过去 27%。**</p>
+ **Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32951)
![architecture](https://img.shields.io/badge/Rounding_Location_Alignment-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/ByteDance_Seed-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出即便权重与 BF16 张量相同，推理与训练端的实现差异也会让 on-policy 更新变成 off-policy；只需把 RoPE、SwiGLU、residual RMSNorm 三处的取整位置对齐，即可阻止训练崩溃。**</p>
+ **PEAR: Adaptive Advantage Reshaping for Perception and Exploration in Large Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32216)
![architecture](https://img.shields.io/badge/Adaptive_Advantage_Reshaping-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Northeastern_University_Shenyang-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**按视觉依赖度缩放 token 熵会压低「高熵但不看图」的探索 token；PEAR 改为只在高熵位置加探索增益、且视觉依赖越低增益越大，在 Qwen2.5-VL 上多模态与文本推理基准均领先。**</p>
+ **NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32881)
![architecture](https://img.shields.io/badge/Ngram_Speculative_Drafter-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/University_of_California_San_Diego-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RL 训练的 rollout 常占七成以上时间；NgramRL 直接用同一 prompt 的近期 rollout 当 n-gram 草稿源，无需辅助模型与 GPU 常驻状态，配合 fan-out 预取器使每次目标模型前向提交 3.60–7.77 个 token。**</p>
+ **$R^2E:$ A Role-driven Reward Evolutionary Framework for Automated Reward Function Design**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32439)
![architecture](https://img.shields.io/badge/Role_Driven_Reward_Evolution-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Hunan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**自动奖励函数设计交给三个分工明确的 LLM 角色：Explorer 拓边界、Guardian 求稳、Evolver 交叉变异重组，再用动态调度从探索转向利用、全局精英池承担跨角色信息交换。**</p>
+ **Profile-Driven User Simulation via Reinforcement Learning with Hierarchical Rewards for Task-Oriented Dialogues**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32435)
![architecture](https://img.shields.io/badge/Hierarchical_Reward_User_Sim-red)
![task](https://img.shields.io/badge/RLHF-magenta)
![organization](https://img.shields.io/badge/Bairong_Inc.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**金融营销场景的用户模拟器：同时建模人口统计/Big Five 用户画像与从真实通话日志反推的业务画像，用带对话级与话语级分层奖励的 GRPO 精修，长尾意图上最稳且生成的话语显著更短。**</p>
