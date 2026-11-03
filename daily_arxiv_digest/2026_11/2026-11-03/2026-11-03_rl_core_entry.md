# 2026-11-03 - 核心强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Value Forcing: Aligning Return Distributions at All Noise Levels**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02160)
![architecture](https://img.shields.io/badge/Flow_Matching_Distributional_Value_Learning-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Princeton_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://chongyi-zheng.github.io/value-forcing)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 flow matching 在每个噪声级别强制 Bellman 一致性来估计回报分布，提出显式 VF 与隐式 IVF 两种价值学习算法，在 OGBench 20 个加 OCBench 6 个共 26 个长程离线 RL 任务上回报分布误差低于 Value Flows、FlowCritic、PCBF，且数据越少优势越大。**</p>
+ **Neural Actor--Critic Learning with Minimax Critics and Reflected Langevin Sampling**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03352)
![architecture](https://img.shields.io/badge/Minimax_Bellman_Critic_Reflected_Langevin_Actor-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/Wuhan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 actor-critic 的有限样本保证推进到动作梯度层面：用 sigmoid 网络上的正则化 minimax Bellman 估计配反射 Langevin 采样器，给出值风险与动作梯度风险的经典非参数 minimax 指数界，并在受控仿真、六个记录型连续控制数据集与建筑能耗决策上验证更优的回报与更低的预测误差。**</p>
+ **SGR-OPSD: Learning from Subgoal Plans with Graph-Regularized Credit Assignment for Agentic Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02414)
![architecture](https://img.shields.io/badge/Subgoal_Graph_Regularized_OPSD-red)
![task](https://img.shields.io/badge/Hierarchical_RL-magenta)
![organization](https://img.shields.io/badge/East_China_Normal_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 LLM 生成的子目标计划转成动作级优势权重，再用子目标进展图从采样转移频率估计的经验回报校准教师信用，在 ALFWorld、WebShop、Search-QA 上以 Qwen2.5-3B/7B 相对 GRPO 最多提升 7.4 个百分点，Qwen2.5-7B 在 ALFWorld 达到 85.8%。**</p>
+ **ANCHOR: KL-Anchored Adaptation for Stable Offline-to-Online RL**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02177)
![architecture](https://img.shields.io/badge/KL_Anchored_Offline_To_Online_Adaptation-red)
![task](https://img.shields.io/badge/Offline_RL-magenta)
![organization](https://img.shields.io/badge/University_of_Michigan-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Cho-Geonwoo/ANCHOR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**离线预训练后在线微调早期常出现灾难性性能崩溃，这篇用受控实验定位根因是占据分布漂移破坏 critic 可靠性，提出 KL 锚定并退火、只留极小保守正则的 ANCHOR，在 FrankaKitchen、AntMaze、Adroit 六个任务上同时压低早期崩溃并保持最强渐近性能。**</p>
+ **KlaskTron-IL: A Contact-Rich Adversarial Imitation Learning Benchmark with a Validated Sim-to-Real Bridge**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03091)
![architecture](https://img.shields.io/badge/Contact_Rich_Imitation_Learning_Benchmark-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/ETH_Zurich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**开源硬件平台 KlaskTron 上构建接触丰富的对抗模仿学习基准，给出 80k 真机人工示范、320k 对称增强与最多 5M 步合成专家轨迹的分层数据，并量化标准 IL 的三种失效：BC 数据规模饱和、GAIL 判别器 logit 跨度低于 0.1、BC 先验与奖励密度交互不对称。**</p>
+ **An Axiomatic Framework for Reinforcement Learning in Open Multi-Agent Systems**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03301)
![architecture](https://img.shields.io/badge/Shapley_Axiom_Value_Function_Multi_Agent_RL-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/University_of_Bristol-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/hsvgbkhgbv/axiomatic-rl-naht)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 Shapley 三公理推导开放多智能体系统的价值函数学习，给出新的 NAHT 分解并证明可还原 Dec-POMDP 的 Shapley 值，落地为 Shapley Machines 与 Banzhaf Machines 两个可插拔模板，在 MPE-PP 与 SMAC 的 NAHT 任务上提升学习效率与对未见约定的泛化。**</p>
+ **Inferring Transferable Rewards via Active Inverse Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03296)
![architecture](https://img.shields.io/badge/Active_Dynamics_Selection_Transferable_Inverse_RL-red)
![task](https://img.shields.io/badge/Inverse_RL-magenta)
![organization](https://img.shields.io/badge/EPFL-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让学习者自己挑选专家演示所处的动力学，用两阶段主动 IRL 先轮转热身再按信息增益选点，给出与可用动力学个数无关的可迁移次优性速率 Õ(d⋆dU/(nm))，在 1000 个未见动力场上最坏次优性显著低于固定动力学 IRL 与 GAIL。**</p>
+ **Behavior-Discriminative Reward Shaping for Reward-Robust Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02415)
![architecture](https://img.shields.io/badge/PBRS_Canonicalized_Robust_Objective-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Tulane_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出奖励鲁棒 RL 的不确定集里塞满了势函数塑形下行为等价的冗余奖励，这篇把每个奖励投影到其 PBRS 等价类的规范代表，证明投影不改变最优鲁棒值且收紧对手搜索空间，在九个基准上让 PPO 相对标准鲁棒 RL 平均提升 17.6% 与 39.0%。**</p>
+ **Iterative Gumbel Planning for Continuous Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02236)
![architecture](https://img.shields.io/badge/Factorized_Categorical_Gumbel_TopK_Planning-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/Texas_A&M_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://liushaohuai5.github.io/ez_igp/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**搜索式规划搬进连续控制会因高斯策略与候选错配而产生投影误差与方差膨胀，提出逐维因子化 categorical 策略加 Gumbel Top-K 与 MPPI 多轮迭代的 IGP，在 DMC-Hard 上把 EZ-M 的 dog-run 从 405.9 提到 613.3、humanoid-run 从 259.0 提到 369.5。**</p>
+ **MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02613)
![architecture](https://img.shields.io/badge/Mixture_of_Experts_Alternating_Policy_Optimization-red)
![task](https://img.shields.io/badge/PPO-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![project](https://img.shields.io/badge/project-blue)](https://mapo-corl2026.github.io/MAPO/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出 MoE 策略的动态路由会让旧策略与更新后策略的散度被误估，进而使基于散度的策略梯度更新走向过度保守或过大更新，提出交替优化 router 与 experts 的 MAPO，在通用人形运动跟踪上多跟住 182 个 PPO+MoE 失败的动作。**</p>
