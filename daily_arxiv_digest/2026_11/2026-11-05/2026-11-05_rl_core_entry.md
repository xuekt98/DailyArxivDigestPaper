# 2026-11-05 - 核心强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **GSBR: Geometric Support Behavior Regularization for Online RL**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05295)
![architecture](https://img.shields.io/badge/Geometric_Support_Behavior_Regularization-red)
![task](https://img.shields.io/badge/Policy_Regularization-magenta)
![organization](https://img.shields.io/badge/UC_Berkeley-green)
[![project](https://img.shields.io/badge/project-blue)](https://charlesxu0124.github.io/gsbr/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把在线 RL 的基策略正则项从「行为克隆匹配」换成「到基策略支撑集的几何距离」惩罚：支撑集内不罚、区外按距离平滑加重，在 4 个机器人基准的 19 个任务上把平均成功率从 33% 提到 95%，归一化吞吐 0.95 领先次优基线的 0.77。**</p>
+ **Revisiting Critic Estimation in Soft Actor-Critic Algorithms**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05666)
![architecture](https://img.shields.io/badge/Replay_Soft_Lambda_Return_Critic-red)
![task](https://img.shields.io/badge/SAC-magenta)
![organization](https://img.shields.io/badge/Leiden_Institute_of_Advanced_Computer_Science_LIACS_Leiden_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**系统比较 SAC 的三种 critic 设计选择并拆成 6 个变体，在 3 个基准套件的 14 个任务上做完整随机超参搜索：软优势与软 GAE 均无增益，真正有效的是在 replay 轨迹段上训练 λ-回报 critic，连续控制上迁移后仍保留约 75% 峰值。**</p>
+ **On Convergence of Gradient Temporal-Difference Learning with Regularized Corrections and Eligibility Traces**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05869)
![architecture](https://img.shields.io/badge/Regularized_Corrected_TD_Lambda_Huber-red)
![task](https://img.shields.io/badge/Eligibility_Traces-magenta)
![organization](https://img.shields.io/badge/University_of_Alberta-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 TD with Regularized Corrections 的收敛理论从一步 i.i.d. 情形扩展到带资格迹的 TDRC(λ)，并提出保持同一不动点的 TDRC(λ)-Huber：覆盖状态相关与历史相关两种 λ 参数，给出积分型小增益条件与可计算的收敛充分条件。**</p>
+ **PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05372)
![architecture](https://img.shields.io/badge/Goal_Conditioned_Joint_Reference_Control-red)
![task](https://img.shields.io/badge/Inverse_Kinematics-magenta)
![organization](https://img.shields.io/badge/New_York_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Tinaliu0123/PolicyIK)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把高精度逆运动学做成目标条件 RL 策略，用累积关节参考加误差相关增益处理冗余与奇异点：仿真单次尝试在 93.5% 的留出任务上把误差压到 1 mm 与 0.2° 内，部署协议下升到 98.9%，并能执行 π0.5 VLA 的取放指令达 95.7%。**</p>
+ **Correct Robots Before They Make Mistakes: Proactive Human-in-the-Loop Intervention via Preference Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05667)
![architecture](https://img.shields.io/badge/Proactive_Human_In_Loop_Preference-red)
![task](https://img.shields.io/badge/Human_Feedback_RL-magenta)
![organization](https://img.shields.io/badge/Karlsruhe_Institute_of_Technology_KIT_Germany-green)
[![project](https://img.shields.io/badge/project-blue)](https://intuitive-robots.github.io/PHIL-page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把人类介入从事后纠错改成事前干预：用 XR 预览策略预测轨迹，把被拒绝的预测与同一状态下执行的纠正动作配成偏好对；4 个真机任务、每条件 5 次纠正预算下，扩散策略成功率从 44.0% 升到 70.3%，X-VLA 从 57.8% 升到 76.9%。**</p>
+ **TwinBridge: Digital Twin-Driven Policy and Reward Transfer for Real-World Reinforcement Learning in Laboratory Robotics**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06442)
![architecture](https://img.shields.io/badge/Digital_Twin_Visual_Reward_Bridge-red)
![task](https://img.shields.io/badge/Digital_Twin-magenta)
![organization](https://img.shields.io/badge/Suzhou_Institute_for_Advanced_Research_University_of_Science_and_Technology_of_China_Suzhou_Jiangsu_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 3D Gaussian Splatting 加物理仿真搭数字孪生，为真机在线 RL 同时提供策略初始化与稠密视觉过程奖励：5 个实验室真机任务上最终平均自主成功率 98%、每任务交互不超过 25 分钟，去掉仿真初始化后仍有 92%，对照 HIL-ConRFT 仅 44%。**</p>
+ **Near-Minimax Sample Complexity for Multi-Objective Reinforcement Learning under Generative Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05562)
![architecture](https://img.shields.io/badge/Near_Minimax_Multi_Objective_Planning-red)
![task](https://img.shields.io/badge/Multi_Objective_RL-magenta)
![organization](https://img.shields.io/badge/University_of_Central_Florida-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**给出多目标 RL 在生成模型下的近 minimax 样本复杂度 Θ(SAH³/ε²·min{S, log(em)})：一份数据即可同时支撑所有偏好组合的最坏 ε-最优策略，最坏统计代价只随目标个数对数增长，并在状态数处饱和，上界由均匀采样加经验规划达到。**</p>
+ **Diversity-Aware Experience Replay via Statistical Leverage Scores**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05929)
![architecture](https://img.shields.io/badge/Kurtosis_Leverage_Mixture_Replay-red)
![task](https://img.shields.io/badge/Experience_Replay-magenta)
![organization](https://img.shields.io/badge/Instrumentation_&_Controls_Group_at_Los_Alamos_National_Laboratory_Los_Alamos_New_Mexico_USA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用回放缓冲区自身的统计杠杆分数给转移打分并与均匀采样混合成 mini-batch：靠最大峰度而非最大方差挑选特征列以绕开 one-hot 动作陷阱，在三关节臂推物体绕障任务上把稀有任务成功率从 0.49 提到 0.69，逼近标注 oracle 上限 0.74。**</p>
+ **Traffic-VL: Reinforced Vision-Language Models for Generalizable End-to-End Traffic Signal Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06353)
![architecture](https://img.shields.io/badge/Reinforced_Vision_Language_Traffic_Control-red)
![task](https://img.shields.io/badge/Vision_Language_Control-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 80 亿参数视觉语言模型把同步多视角路侧图像与自然语言相位描述直接映射为配时决策，不经过结构化交通状态；视觉编码器离线 RL 适配后冻结并做闭环逐步轨迹优化，在 10 个路口完成 3 周部署，表现追平结构化状态的 Traffic-R1。**</p>
+ **H^2MARL: Hierarchical Heterogeneous Multi-agent Reinforcement Learning for Humanoid Robot Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06523)
![architecture](https://img.shields.io/badge/JDoF_Heterogeneous_Policy_Factorization-red)
![task](https://img.shields.io/badge/MARL-magenta)
![organization](https://img.shields.io/badge/School_of_Artificial_Intelligence_Hubei_University_Wuhan_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把人形机器人的每个扭矩驱动关节自由度当作独立异质智能体，并让高层位姿规划器与低层关节执行器在同一闭环轨迹上联合优化：在 MuJoCo 与 Isaac Gym 上相对最强的 MAPPO，接地稳定性、躯干稳定性与步态对称性分别提升 7.3%、35.0% 与 14.8%。**</p>
