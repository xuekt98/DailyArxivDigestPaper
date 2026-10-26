# 2026-10-26 - RL 算法与理论、多智能体 RL、Sim-to-Real 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Regularised RL improves sim-to-real transfer**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32855)
![architecture](https://img.shields.io/badge/Soft_MellowMax_AC-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/McGill_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出 PPO 这一弱正则算法仍是 sim-to-real 流水线的事实默认；据此推导基于 soft mellowmax 价值函数的 SMM-AC，MuJoCo 上与 SAC 相当，真机上回报更高且对观测/环境/动力学扰动都更鲁棒。**</p>
+ **Conditional Flow Models for Offline Maximum Entropy Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32125)
![architecture](https://img.shields.io/badge/Conditional_Flow_Offline_MaxEnt-red)
![task](https://img.shields.io/badge/Offline_RL-magenta)
![organization](https://img.shields.io/badge/Wuhan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把离线最大熵 RL 拆成建模与值学习两层：用概率流 ODE 条件扩散模型估计奖励分布与转移核，再在深度网络上最小化经验 Bellman 残差；给出非渐近界，且不要求 Bellman 完备性。**</p>
+ **When to Stop Penalizing Actions? Martingale GRPO for VLA Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32431)
![architecture](https://img.shields.io/badge/Martingale_GRPO-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出 GRPO 把整条轨迹的成败均摊给每个动作，连「本来在纠错」的动作也被惩罚；用成功率与策略分数鞅刻画该何时停止，截断既保持组梯度估计量的期望又能降低协方差。**</p>
+ **Reinforcement Learning with Multi-Step Transition Predictions: A Bellman Theory**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32887)
![architecture](https://img.shields.io/badge/Block_Feedback_Bayesian_Bellman-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Cornell_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多步转移预测塞进状态会让状态空间爆炸，但作者证明在块反馈协议下最优值在原状态空间上满足贝叶斯 Bellman 方程，并给出 BF-BOLA 的上下界样本复杂度。**</p>
+ **RobustRLlib: A Unified Library and Benchmark for Robust Reinforcement Learning Algorithms**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32971)
![architecture](https://img.shields.io/badge/Robust_RL_Library_Benchmark-red)
![task](https://img.shields.io/badge/Model_Free_RL-magenta)
![organization](https://img.shields.io/badge/UC_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 17 个鲁棒在线/离线/安全 RL 算法统一到一个接口下，配套覆盖真实世界偏移、人形与 VLA 任务的评测平台；273 种扰动配置下的系统评测给出当前算法的最新能力地图。**</p>
+ **Dual-Adaptive Z-Score PPO: Dynamic Clipping Using Action Confidence and Normalized Advantage Magnitude**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32194)
![architecture](https://img.shields.io/badge/Dual_Adaptive_Z_Score_PPO-red)
![task](https://img.shields.io/badge/PPO-magenta)
![organization](https://img.shields.io/badge/University_of_North_Dakota-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PPO 的固定裁剪阈值对所有样本一视同仁；这篇按动作置信度与归一化优势幅度动态设定裁剪区间，在三个经典控制基准上时好时坏，作者明确指出自适应裁剪主要在较难任务上有效。**</p>
+ **Effectiveness of Curriculum Learning Depends on Reward Sparsity and Competing Optima**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31884)
![architecture](https://img.shields.io/badge/Minimal_Model_Of_Curriculum-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/Harvard_Medical_School-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用最小策略学习模型解释课程学习为何在 RL 中远比监督学习有效：稠密奖励下只有边际收益，稀疏奖励下课程可能是学习能否发生的前提，尤其当「省力」与「高回报」两个目标造出互相竞争的极值。**</p>
+ **Emergent Cooperative Thermoregulation in Lunar Swarm Robotics**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31868)
![architecture](https://img.shields.io/badge/Evolution_Strategies_Swarm-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/MIT_Center_for_Bits_and_Atoms-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用进化策略训练一个由 20 台月面机器人共享的策略，奖励只在夜末给一次（五台最冷机器人的平均温度），不含任何位置或运动信息，却涌现出聚集与核心-边缘轮换；存活阈值比静止抱团低 37%，且可零样本扩到 40 台。**</p>
+ **SEVI: Safe Evidential Real-World Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31829)
![architecture](https://img.shields.io/badge/Evidential_Safety_Critic-red)
![task](https://img.shields.io/badge/Model_Free_RL-magenta)
![organization](https://img.shields.io/badge/Indiana_University_Luddy_School_of_Informatics-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**真实世界 RL 的安全判断要同时给出危险程度与判断的可信度：Evidential Safety Critic 一次前向同时估计约束违反风险与认知不确定性，证据不足时用离线恢复策略覆盖动作，不安全事件减少 13.4%–57.1%。**</p>
+ **PrefO2O: Zero-Shot Preference-Based Reinforcement Learning via Offline-to-Online Latent Preference Transfer**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31812)
![architecture](https://img.shields.io/badge/Offline_To_Online_Preference_Transfer-red)
![task](https://img.shields.io/badge/Inverse_RL-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**偏好 RL 被「每个新任务都要重新收人类标注」卡死；从源任务的少量离线偏好学出任务不变的隐式偏好空间，再用置信度加权的最优传输生成伪偏好监督，零样本达到甚至超过用真实人类反馈训练的 PbRL。**</p>
