# 2026-10-23 - RL 算法与理论、多智能体 RL、Sim-to-Real 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31544)
![architecture](https://img.shields.io/badge/TWICE-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/University_of_Sheffield-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TWICE 按 turn 与 line 键控 Gumbel 噪声，让反事实孪生体继承事实 episode 的下游噪声，从而把决策效应与后续运气分开；解析优势所需 rollout 从 Θ(Δ⁻²) 降到 Θ(Δ⁻¹)，GRPO 精确匹配提升 4.5–5.3 点且少用 68% 辅助 token。**</p>
+ **METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31656)
![architecture](https://img.shields.io/badge/METTA-red)
![task](https://img.shields.io/badge/Meta_RL-magenta)
![organization](https://img.shields.io/badge/Sharif_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**METTA 把元 RL 的快速适应拆成两个时间尺度：因果神经记忆以线性复杂度做回合内适应，回合级摘要做长程跨回合推断，在未见的 Meta-World ML10/45 上成功率超 50%，并在 PointMaze 上展现更有结构的探索。**</p>
+ **SpecMAGIC: Specification-Guided Multi-Task Generalization in Multi-Agent Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30443)
![architecture](https://img.shields.io/badge/SpecMAGIC-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/Boston_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SpecMAGIC 用时序逻辑规格语言与自动机结构做子任务分解：集中式高层规划器分配兼容子任务序列、去中心化低层策略执行，从而在新规格上零样本泛化且无需重训，并给出可靠性与概率完备性证明。**</p>
+ **TerraTransfer++: Demonstration-Free End-to-End Planner**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30319)
![architecture](https://img.shields.io/badge/TerraTransfer++-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/University_of_California,_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TerraTransfer++ 用向量化仿真器自博弈预训练单一策略，再蒸馏成流匹配轨迹教师，并在冻结视觉骨干上训练轻量适配器；每个目标都可追溯到自博弈策略，全程无需人工示范，在 HUGSim 超越所有模仿式方法并在 NAVSIM navhard 达 59.4 EPDMS。**</p>
+ **MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30334)
![architecture](https://img.shields.io/badge/MPBRS-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/University_of_Nevada,_Reno-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MPBRS 用多势函数奖励塑造为九台人形机器人提供统一奖励配置，只需关节 / 连杆映射与默认姿态等元数据；相比标准塑造，它在保证不改变最优策略的前提下获得更一致的缩放行为与更低的调参敏感度。**</p>
+ **Ground-Truth-First Benchmarking of Reinforcement Learning via Converse Optimality: From Smooth, Fully Observed Systems to Non-Smooth or Partially Observed Tasks**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30954)
![architecture](https://img.shields.io/badge/Converse_Optimality_Benchmarking-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Sirius_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇提出 ground-truth-first 的 RL 基准框架：基于逆向最优性为每个任务构造带认证最优值函数与最优策略的环境（仅用于评测），统一敏感性基准与 oracle 参考比较两种模式，并覆盖非光滑、部分可观测与连续 / 离散时间情形。**</p>
+ **DRILL: Training World Models to Improve Policies, Not Predict Pixels**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30814)
![architecture](https://img.shields.io/badge/DRILL-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/Tencent_Hunyuan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DRILL 用双层框架按「策略回报」而非像素 MSE 来训练用于 RL 的世界模型：更低像素 MSE 可能带来更差策略梯度，而为策略效用训练的世界模型在下一帧 MSE 高 17% 时下游策略反而更好，成功率相对 WMPO 提升 13.1 点。**</p>
+ **SABLE: Scalable Affine Bayesian Latent-space Exploration**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31495)
![architecture](https://img.shields.io/badge/SABLE-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/Lancaster_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SABLE 用贝叶斯仿射代理处理高维潜空间（维度远超评估预算），把高阶结构建模为代理残差；每次查询分解为张成内的 EI 优化与张成外范数，后者用有限视野调度规定以避免探索不足。**</p>
+ **Primal-Dual Representation Learning for Low-Rank Constrained MDPs**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30756)
![architecture](https://img.shields.io/badge/REP-PD-TEG-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**REP-PD-TEG 用衰减 ε-贪心混合策略学习转移特征、以乐观拉格朗日目标规划，实现低秩连续状态约束 MDP 的表征学习：达到最优 Õ(√K) 回报界与 Õ(K^{3/4}) 整体样本界；硬约束版本 REP-PD-H-TEG 另给可行性认证。**</p>
+ **PATH: Preference-Aware Traversability Estimation for Robotic Teleoperation in Off-Road Navigation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30605)
![architecture](https://img.shields.io/badge/PATH-Net-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_Polytechnic_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PATH-Net 用最大熵逆强化学习与稀疏速度监督，从遥操作轨迹中学习偏好条件的可通行性代价图与速度剖面；15 名操作者 225 条轨迹上与各自导航策略对齐，NASA-TLX 工作负荷从 34.7 降至 22.2。**</p>
