# 2026-11-04 - 核心强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Finite-Sample Convergence in Networked Average Reward MARL: Decentralization Pitfalls and Entropy Remedies**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04072)
![architecture](https://img.shields.io/badge/Networked_Average_Reward_Actor_Critic-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/California_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向网络化平均奖励 MARL，给出去中心化收敛到全局最优联合策略的不可能性结果，并证明加入定态熵正则后线性逼近 actor-critic 可获得更强全局收敛保证。**</p>
+ **Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04774)
![architecture](https://img.shields.io/badge/Greedy_Windowed_Policy_Optimization-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/EPFL_Switzerland-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对联合轨迹上的单调次模奖励，提出用 pre-window curvature 控制截断误差的贪心算法 GWPO，得到 (1-c_m)/(2-c_m) 近似保证与多项式计算量，并在交通监控场景验证记忆长度的收益。**</p>
+ **Safeguarding Multi-Agent Reinforcement Learning for Connected and Automated Vehicles with Recursively Feasible Control Barrier Functions**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04957)
![architecture](https://img.shields.io/badge/Backup_Horizon_Control_Barrier_Filter-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_RWTH_Aachen_University_Germany-green)
[![project](https://img.shields.io/badge/project-blue)](https://bassamlab.github.io/BH-CBF)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 Backup-Horizon 控制障碍函数，在控制界下递归可行且考虑精确车辆几何，用每步一次广播的去中心化滤波器加固 MARL 策略，实录交通中把中位通行时间缩短 14% 且零碰撞。**</p>
+ **Reconstructing Fraudulent Strategies in Online Payments via Interpretable Inverse Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04819)
![architecture](https://img.shields.io/badge/Alternating_Reward_Policy_Optimized_IRL-red)
![task](https://img.shields.io/badge/Inverse_RL-magenta)
![organization](https://img.shields.io/badge/Tongji_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在蚂蚁国际真实线上支付场景中，用可解释逆强化学习反推欺诈策略并生成训练样本，生产检测器 AUC 提升 0.393 个百分点、Recall@2 提升 1.621 个百分点，并优于全部生成类基线。**</p>
+ **Decision Transformer with Task-Aware Representations for Offline Meta-Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04010)
![architecture](https://img.shields.io/badge/Contrastive_Task_Aware_Decision_Transformer-red)
![task](https://img.shields.io/badge/Meta_RL-magenta)
![organization](https://img.shields.io/badge/State_University_of_New_York_at_Binghamton-green)
[![project](https://img.shields.io/badge/project-blue)](https://anonymous.4open.science/r/CotaDT-35DB)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出对比式任务感知 Decision Transformer，把对比学习、任务描述对齐、任务条件世界模型与 Q 函数四路监督合一，零样本 Meta-World 回报相对次优基线绝对提升 189.0 并在四个基准全部最优。**</p>
+ **On the Feature Evolution of Temporal Difference Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04158)
![architecture](https://img.shields.io/badge/Two_Layer_ReLU_TD_Feature_Analysis-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/University_of_North_Carolina_at_Chapel_Hill-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在有限宽两层 ReLU critic 上刻画 TD 学习的特征演化：隐层与读出头同时更新带来 2(d+1) 倍二次响应与严格预测风险改善，并推出 Õ(d³H^{1/3}T^{2/3}) 的 explore-then-commit 遗憾界。**</p>
+ **Language Model Augmented Decision Transformer for Multi-Task Offline Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04031)
![architecture](https://img.shields.io/badge/Language_Augmented_Decision_Transformer-red)
![task](https://img.shields.io/badge/Offline_RL-magenta)
![organization](https://img.shields.io/badge/State_University_of_New_York_at_Binghamton-green)
[![project](https://img.shields.io/badge/project-blue)](https://anonymous.4open.science/r/o33zlamadt-6587)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用同一个 LLM 同时承担任务对齐的轨迹增强与语言条件 Decision Transformer 学习，配合似然打分过滤，在 Meta-World 与 MuJoCo 上平均提升 5.5% 与 6.8%，低数据区间收益最显著。**</p>
+ **CANDO: Conservative Action-Noise Directional Optimization for Residual Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04543)
![architecture](https://img.shields.io/badge/Conservative_Action_Noise_Residual_RL-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/School_of_Data_Science_Fudan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://cando-rl.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 CNDO/CANDO 残差强化学习，用保守价值估计与门控执行替代固定隐空间可行域并叠加动作空间残差，取得 76.1 NAUC 与 91.4% 最终成功率，比最优单空间方法高 6.6 与 4.1 个百分点。**</p>
+ **CRONOS: Benchmarking Non-Episodic Reinforcement Learning for Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05080)
![architecture](https://img.shields.io/badge/Non_Episodic_VLA_RL_Benchmark-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_and_Information_Engineering_National_Taiwan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://embodiedai-ntu.github.io/cronos/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 CRONOS 基准评测非情节式场景重置下的 VLA 微调：启发式强制重置把成功率从 14% 拉到 64%，非情节式训练还把重叠与杂乱配置成功率分别提升到 0.643 与 0.550。**</p>
+ **D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03622)
![architecture](https://img.shields.io/badge/Decoupled_Describe_Assess_VLM_Reward-red)
![task](https://img.shields.io/badge/Zero_Shot_Reward_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Washington-green)
[![project](https://img.shields.io/badge/project-blue)](https://weirdlabuw.github.io/dna)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出纯提示的 D&A 框架，把视频任务进度估计拆成客观描述与基于 rubric 的评估两步，抑制 VLM 奖励模型的确认偏误，Kendall τ 在 RBM-EVAL-OOD 上从 0.349 提升到 0.583。**</p>
