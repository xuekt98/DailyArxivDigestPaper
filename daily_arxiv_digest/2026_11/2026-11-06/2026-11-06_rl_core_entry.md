# 2026-11-06 - 核心强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Reinforcement Learning Enables Scaling Generalist Robot Policy Improvement**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06905)
![architecture](https://img.shields.io/badge/Generalist_Policy_Improvement-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/ETH_Zurich-green)
[![project](https://img.shields.io/badge/project-blue)](https://lasgroup.github.io/generalist-improvement)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**给出通用机器人基础模型多任务在线 RL 改进的成套配方：系统评估价值估计、策略抽取与资源分配，证明价值型 RL 与训练任务分布多样性是泛化到未见任务的关键。**</p>
+ **Detecting Silent Faults at the Environment-Trainer Boundary in Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08144)
![architecture](https://img.shields.io/badge/Step_Ledger_Fault_Detection-red)
![task](https://img.shields.io/badge/Safe_RL-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/PlugRL)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把环境与训练器的边界做成线协议并注入最多 23 类故障，发现学习曲线阈值最多只抓到十分之一运行，环境侧步骤账本却全部命中并定位故障位置，代价仅为 Pendulum 上中位 3% 的额外训练时间。**</p>
+ **Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07066)
![architecture](https://img.shields.io/badge/Epigraph_Constrained_Exploration-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![project](https://img.shields.io/badge/project-blue)](http://efxplorer-marl.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用上图（epigraph）重构把协作探索写成「任务回报不退化前提下最大化内在奖励」的约束问题，用自适应探索预算取代敏感的对偶乘子，在 SMAX、VMAS、MPE 三套基准上诱导出新的协作策略。**</p>
+ **Finite-Time Convergence and Regret Guarantees for Neural Reinforcement Learning in POMDPs**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07069)
![architecture](https://img.shields.io/badge/Neural_PMD_for_POMDP-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Ohio_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在有限记忆 POMDP 上给出非线性神经价值逼近的首个有限时间次线性 regret 界，critic 误差界同时含 NTK 架构、TD 与历史记忆三段误差，并给出满足该界的超参条件。**</p>
+ **RLGPA: A Reinforcement Learning-Guided Granularity Planning Attack for Decision-Based Sparse Adversarial Examples**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07512)
![architecture](https://img.shields.io/badge/RLGPA_Granularity_Planner-red)
![task](https://img.shields.io/badge/DQN-magenta)
![organization](https://img.shields.io/badge/South_China_Normal_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Acui001/RLGPA.git)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把决策型稀疏对抗攻击的支持集收缩变成在线 RL 调度问题，掩码 Dueling Double DQN 在七类策略-粒度动作间选择，CIFAR-10 上定向攻击率达 61%。**</p>
+ **Monotone Viability Learning for Offline Safe Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07616)
![architecture](https://img.shields.io/badge/Monotone_Viability_Learning-red)
![task](https://img.shields.io/badge/Offline_RL-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用单调有限时域集合递推从离线转移学习 Hamilton-Jacobi 可行集，兼顾安全语义与数值稳定，并在 17 个离线安全 RL 任务上给出最低平均代价。**</p>
+ **PhySA: Decoupling Aesthetic and Physical Rewards for Humanoid Locomotion**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07679)
![architecture](https://img.shields.io/badge/PhySA_Decoupled_Reward_Channels-red)
![task](https://img.shields.io/badge/Reward_Shaping-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发现视觉语言模型给出的美学偏好与物理平滑方向相反，把稀疏异步 VLM 打分与相位触发的物理惩罚校正拆成两条可独立移除的奖励通道，从而稳定人形机器人的步态。**</p>
+ **Accelerating Safe Reinforcement Learning with Massive Parallelism**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08273)
![architecture](https://img.shields.io/badge/Staggered_Reset_Safe_RL-red)
![task](https://img.shields.io/badge/Safe_RL-magenta)
![organization](https://img.shields.io/badge/Pusan_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把大规模并行短 rollout 与 CMDP 的整段 episode 代价约束之间的错配建模成相位混合分布，用相位聚合代价估计器在 GPU 上重获安全训练。**</p>
+ **RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08308)
![architecture](https://img.shields.io/badge/RM_VLM_Reward_Machine-red)
![task](https://img.shields.io/badge/Reward_Shaping-magenta)
![organization](https://img.shields.io/badge/Imperial_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让大语言模型从自然语言任务描述编译奖励机、由视觉语言模型充当命题标注函数，把非马尔可夫任务的时序结构接回标准强化学习流程，并在三个领域全面超过已有的 VLM 奖励方法。**</p>
+ **SHORE: Stability-Hybrid On-Policy Reinforcement Learning for Online Bin Packing**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08364)
![architecture](https://img.shields.io/badge/SHORE_Stability_Hybrid_RL-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/University_of_Texas_at_Austin-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把在线三维装箱的堆叠稳定性学成概率模型并与 on-policy 回报估计融合，用门控限制未训练模型的干扰，在 Isaac Gym 上更快达到更高空间利用率。**</p>
