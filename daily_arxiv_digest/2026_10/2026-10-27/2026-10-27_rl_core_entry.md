# 2026-10-27 - 强化学习核心算法与理论 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35736)
![architecture](https://img.shields.io/badge/MIRL_MetaGradient-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/University_of_Edinburgh-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MIRL 提出用目标级反事实信用分配评估各智能体在团队目标上的贡献，再借元梯度让智能体学习个体目标排序与系统级集体优化之间的权衡；在多目标多粒子环境上显著改善 Pareto 前沿质量。**</p>
+ **When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement Learning through Video Editing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35497)
![architecture](https://img.shields.io/badge/Decaying_Process_Rewards-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/University_of_Pennsylvania-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在四类电影预告片剪辑任务上系统检验细粒度信用分配的边界：超过 60 轮的长程任务里衰减过程奖励相对结果-only GRPO 提升 45.4%，30–40 轮的短程任务则至多 10.4%；并发现固定过程奖励权重会陷入过程分升、任务分降的奖励黑客。**</p>
+ **Multi-Horizon Future Discovery for Physics-Informed Exploration**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35468)
![architecture](https://img.shields.io/badge/HTC2_Physics_Exploration-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/University_of_Chinese_Academy_of_Sciences-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HTC² 用时程条件化的对比 critic 学习未来状态对的时序关系，以正样本表征距离作内在奖励、并用有界多步哈密顿变化调制，兼顾时序组织性与物理结构；在六个 DeepMind Control Suite 任务上与 SAC、PPO 集成评测。**</p>
+ **Reinforcement learning for constrained stochastic linear--quadratic control in continuous time**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34995)
![architecture](https://img.shields.io/badge/Constrained_Continuous_Time_LQ-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Fuzhou_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**研究标量状态、非负控制约束下的连续时间随机 LQ 控制：构造不含熵的辅助问题并用矩约化导出两个区域 Riccati 方程，给出控制-代价相容性充分条件与无限时域最优解，并配套模型无关 actor-critic 数值对照。**</p>
+ **Centralized Critics for N-Agent Ad Hoc Teamwork**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34799)
![architecture](https://img.shields.io/badge/Joint_History_Critics-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/Unknown-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对 N 智能体临时协作，比较只条件于自身历史的受控历史 critic 与额外条件于不受控队友历史的联合历史 critic：证明两者均无偏，并刻画联合估计严格降方差的条件，任务上样本效率与最终回报均更优。**</p>
+ **Provably Efficient Q-learning for Robust Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35656)
![architecture](https://img.shields.io/badge/Provably_Efficient_Robust_Q_Learning-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/Chinese_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对鲁棒 RL 中「缺高效模型无关方法」的空白，提出异步 Q-learning：在 TV 不确定集与单条马尔可夫轨迹设定下，其样本复杂度界几乎 minimax 最优、仅多出 1/(1-γ) 因子，显著优于已有界。**</p>
+ **Multi-Objective Reinforcement Learning Using Routed Ensembles and Trajectory Attribution**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35733)
![architecture](https://img.shields.io/badge/Routed_Ensembles_MORL-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/Northeastern_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**引入目标冲突系数并推导近乎最优的遗憾界，量化多目标 RL 中最优策略随权重剧烈变化带来的样本效率代价；据此提出路由集成策略学习（平均提升 4.3%）与核代理轨迹归因（留一法相关性提升 50%、轨迹选择回报提升 27%）。**</p>
+ **Best Policy Tracking in Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34501)
![architecture](https://img.shields.io/badge/Best_Policy_Tracking-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/University_of_the_Basque_Country-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**本文实证指出 RL 单任务训练中的性能非单调性使「取最终或定期评估中最好的策略」这一惯例可能与全程最优相差甚远，导致性能低估与算力浪费；作者提出诊断指标并推荐受成本约束的验证集式选策策略。**</p>
+ **Behavioural Quality Is Not Learning Utility: Objective Mismatch in Human Behaviour Models for Robot Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34839)
![architecture](https://img.shields.io/badge/Behaviour_Quality_vs_Utility-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/Monash_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在高速驾驶与物体交接两个 HRI 领域比较人类行为模型的生成式评测指标与下游 RL 策略表现，发现行为指标无法一致预测下游效用且对轨迹表示敏感；甚至已知真实测试分布时，用不同分布训练反而可能获得更好的下游表现。**</p>
+ **Enhancing Deep Reinforcement Learning for Robotic Motion Planning via Task Decomposition**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35494)
![architecture](https://img.shields.io/badge/Task_Decomposition_DRL-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/Cardiff_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**结合迁移学习与奖励重设计的任务分解框架：只迁移 critic 第一层参数以复用通用状态-动作表示，并把任务拆成分阶段子目标提供稠密信号；Push with obstacle 成功率 0.83（TQC 0.77），稀疏奖励 Pick-and-Place 训练量从 0.75M 降到 0.20M 步。**</p>