# 2026-11-06 - LLM 后训练 RL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **$D^2$-OPD: Separating Direction and Distance in Extrapolative On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07241)
![architecture](https://img.shields.io/badge/D2_OPD_Direction_Distance-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/Columbia_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**解耦外推式 on-policy 蒸馏的目标方向与移动距离：逐前缀硬 KL 约束限距、教师后训练偏移与师生差距定方向，在有无教师参考的三种设定下均取得最高平均分。**</p>
+ **Reinforcing What the Student Has Learned: Teacher-Guided On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07722)
![architecture](https://img.shields.io/badge/Student_Delta_OPD-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/State_Key_Lab_of_CAD_&_CG_Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/aim-uofa/sd-opd)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以学生与其预训练底座的差异作为参考，只在符号与教师反馈一致时保留更新系数，避免 OPD 把大部分更新强度花在模仿教师表达风格上而损失推理收益，覆盖 1.7B 到 8B 学生。**</p>
+ **CoRD: Coupled Rollouts Fill the Blind Spot of On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07959)
![architecture](https://img.shields.io/badge/Coupled_Rollout_Distillation-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用推测解码的最大耦合在师生分布间做几何插值采样，把训练状态分布拉向教师，补上 on-policy 蒸馏对教师可达路径监督不足的盲区，同时把采样干预压到尽可能少。**</p>
+ **SAVeR$^2$: Reasoning-based Safety Alignment for Large Reasoning Models via Verifiable Rewards**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07482)
![architecture](https://img.shields.io/badge/SAVeR2_Verifiable_Rewards-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/State_Key_Laboratory_of_Blockchain_and_Data_Security_Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把大型推理模型的安全目标拆成四条可验证奖励信号，用保推理的梯度投影解析解决安全与推理梯度的冲突，在 1.5B 到 671B 全尺度上同时提升安全与思考能力。**</p>
+ **Learning Multi-Agent Orchestration:Higher-Order Interactions in Policy Improvement**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07495)
![architecture](https://img.shields.io/badge/Interaction_Aware_Policy_Optimization-red)
![task](https://img.shields.io/badge/Multi_Turn_RL-magenta)
![organization](https://img.shields.io/badge/Emory_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**精确分解两套编排策略间的性能差，把决策间的高阶交互与单决策效应同时优化并做认证式筛选，纠正按各自 advantage 记账的错误假设，支持多智能体协作编排。**</p>
+ **Provable Zeroth-Order Safe Exploration for Reinforcement Learning from Human Feedback**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07561)
![architecture](https://img.shields.io/badge/Zeroth_Order_Log_Barrier-red)
![task](https://img.shields.io/badge/RLHF-magenta)
![organization](https://img.shields.io/badge/Purdue_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用对数障碍目标与零阶梯度估计从人类偏好直接学 RLHF，给出所有迭代点与探索策略都严格可行的高概率保证，以及与策略维度无关的样本复杂度界，覆盖合成 CMDP 与语言模型对齐两类实验。**</p>
+ **Measuring the Marginal Value of Verifier-Based RL Beyond Supervised Fine-Tuning**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07639)
![architecture](https://img.shields.io/badge/Verifier_RL_Marginal_Value_Audit-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/saloni-garg/gpu-train-debug)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 1,877 题的确定性 GPU 与大模型训练故障诊断基准直接测量验证器 RL 相对监督微调的边际价值，发现同分布增量几乎为零而分布外仅 +0.33 分。**</p>
+ **O$^2$PD: Overlap-Gated On-Policy Distillation on Reliable Prefix**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07731)
![architecture](https://img.shields.io/badge/Overlap_Gated_On_Policy_Distillation-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/Renmin_University_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**只对每条学生 rollout 的前 20% 前缀做蒸馏对齐，并用重叠度门控的 α-散度在模式覆盖与模式寻求之间切换支撑集，整体优于常规的 top-k OPD。**</p>
+ **Learning Dynamics of On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08016)
![architecture](https://img.shields.io/badge/OPD_Learning_Dynamics-red)
![task](https://img.shields.io/badge/On_Policy_Distillation-magenta)
![organization](https://img.shields.io/badge/University_of_Oxford-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 OPD 的反馈环拆成信号转换与更新广播两段做机制分析，解释教师越强学生反而越学不动的原因，并给出先离线备好续写能力再上 OPD 的实用处方与退化诊断。**</p>
+ **AttnSR: Attention Step Reward for Long-Horizon Agentic RL**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07932)
![architecture](https://img.shields.io/badge/Attention_Step_Reward-red)
![task](https://img.shields.io/badge/Process_Reward-magenta)
![organization](https://img.shields.io/badge/East_China_Normal_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/fairyshine/AttnSR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**不训额外奖励模型也不追加 rollout，直接用策略注意力反推各步对终局的相关性来分配步级奖励，长时序 agentic RL 的成功率与交互成本同时得到改善。**</p>
