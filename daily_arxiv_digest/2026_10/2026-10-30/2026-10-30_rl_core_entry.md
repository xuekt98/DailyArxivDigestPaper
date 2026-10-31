# 2026-10-30 - 强化学习 · 核心算法 / 理论 / MARL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Reinforcement Learning for the Game of Balatro: A Fast Simulator and Two-Policy Training Approach**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39049)
![architecture](https://img.shields.io/badge/Balatro_TwoPolicy_MultiAgent_PPO-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/Duke_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对 Balatro 的 3000 步状态相关动作空间、数百步稀疏奖励与强随机性，论文给出 Rust 高吞吐模拟器加动态合法动作屏蔽，并用多智能体 PPO 把对局拆成盲注与商店两个策略，逐智能体奖励路由缓解长程信用分配，首盲通关率收敛到 99% 以上。**</p>
+ **Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40030)
![architecture](https://img.shields.io/badge/Value_of_Information_Memory_RL-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Technical_University_of_Munich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把 RL 记忆的检索代价与跨序列信用分配统一到信息价值这一个量上，用学习到的 world model 从归档 rollout 估计它，在观测处给出获取动作最优价值的可证下界并为 TD target 设下限，在决策处定义最优检索集合。**</p>
+ **Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39264)
![architecture](https://img.shields.io/badge/GiGPPO_UI_Navigation_Online_RL-red)
![task](https://img.shields.io/badge/PPO-magenta)
![organization](https://img.shields.io/badge/Apple-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在真实 iOS 上做在线稠密 RL，把 agent 解耦为 Planning agent 与 UI Grounding 模型，用 LLM-as-a-Judge 组合步级反馈与终止奖励，以 PPO 加步级优势估计训练并提出 GiGPPO 稳定 critic，8B agent 在 Android 泛化上较 SFT 提升近七倍。**</p>
+ **Timbre: Reliability-aware harmonic consensus for label-free multimodal test-time rexinforcement learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39439)
![architecture](https://img.shields.io/badge/Timbre_Harmonic_Consensus_TTRL-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/University_of_Melbourne-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Timbre 用可靠性感知的调和共识做多模态 test-time RL，构造原始与扰动图像配直接求解与改写模式的 2×2 网格，以加权调和聚合选伪标签并按置信度波动调模态权重，再把共识表述为加权 χ²-barycenter，在六个基准三个模型规模上多数设置超过 TTRV。**</p>
+ **Safe Multi-Objective Reinforcement Learning: Zero Constraint Violation and Primal-Averaging Convergence**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39409)
![architecture](https://img.shields.io/badge/Safe_MORL_Primal_Averaging-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文研究全程零约束违反的安全多目标 RL，结合乐观奖励估计与悲观代价上界学习安全 Pareto 最优策略，保证 T 个回合内执行的每个策略零违反，在光滑 Tchebycheff 标量化下达到 Õ(1/√T) 次优差距，并给出无需预设偏好的探索加规划版本。**</p>
+ **Event2Reward: Learning Robotic Rewards from Progress Relations**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39212)
![architecture](https://img.shields.io/badge/Event2Reward_Progress_Relation-red)
![task](https://img.shields.io/badge/Inverse_RL-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Event2Reward 指出用归一化演示时间当进度标签隐含进度单调的假设，转而从停滞、倒退与恢复中提炼局部相对进度关系，用时间标签锚尺度、相对关系约束局部变化，把进度预测当作 potential 塑形，在 LIBERO 40 个任务上同预算平均提升 18.16 个百分点。**</p>
+ **How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40002)
![architecture](https://img.shields.io/badge/CoC_CFG_Q_Adaptive_Guidance-red)
![task](https://img.shields.io/badge/Offline_RL-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CoC-CFG 不再问推理链对不对，而是问它该以多强力度引导动作：在有无推理段的两个上下文间做 classifier-free guidance，每个 Euler 步一个权重，把权重选择建成 MDP 并用测量的动作价值训练 Q-adaptive 引导，在 Alpasim 闭环通过 300 场景中的 262 个。**</p>
+ **Value Function-Guided MPPI for Hierarchical Planning and Control in Off-Road Autonomous Navigation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38731)
![architecture](https://img.shields.io/badge/Value_MPPI_Hierarchical_Control-red)
![task](https://img.shields.io/badge/Hierarchical_RL-magenta)
![organization](https://img.shields.io/badge/Robotics_Institute,_Carnegie_Mellon_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出信息双向流动的越野导航分层规划控制框架：最高层 MPPI 不再用显式 cost map，而是把预训练低层 RL 控制器的 value function 当作隐式代价来做轨迹探索，并用在线策略评估适配训练与评估间的分布漂移，在高保真模拟器中比基线 MPPI 更安全有效。**</p>
+ **Robotic Data Inoculation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39054)
![architecture](https://img.shields.io/badge/Data_Inoculation_Residual_Policy-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/UC_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Data Inoculation 用共享控制改造数据采集：人类闭环遥操作的同时，一个在线训练的 residual policy 对指令施加扰动，其奖励最大化目标与后续策略抽取一致，使扰动自动指向学习者会犯的偏差，人类纠正则提供恢复演示，在三个真机任务上提升或追平行为克隆与离线 RL 策略。**</p>
+ **VeriCUA: Verification as Agentic Exploration for Computer-Using Agents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40578)
![architecture](https://img.shields.io/badge/VeriCUA_Agentic_Verification-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/Google-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VeriCUA 把 computer-use agent 的任务完成验证做成平台无关的主动取证流程：先检查上下文构造任务评分表，再为未解决要求选择 GUI 或代码检查并按显式证据规则合并，各设置下与参考标签的一致性优于基线，在线时对虚假完成声明拒绝更强。**</p>
