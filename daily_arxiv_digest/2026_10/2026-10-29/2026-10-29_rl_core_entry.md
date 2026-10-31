# 2026-10-29 - 强化学习 · 核心算法 / 理论 / MARL 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Learning from Relative Action Credit for Escaping Local Minima**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38034)
![architecture](https://img.shields.io/badge/Relative_Action_Credit_PPO-red)
![task](https://img.shields.io/badge/PPO-magenta)
![organization](https://img.shields.io/badge/Istituto_Italiano_di_Tecnologia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇论文把 PPO 在长时程接触任务上的停滞归因于 state-value critic 缺少动作区分度，给 PPO 加入 action-conditioned value critic 来比较同状态下的替代动作，从而在同等训练预算内完成精密 peg insertion。**</p>
+ **Cooperative EV Charging Assignment Using Multi-Agent Reinforcement Learning: A Comparison of QMIX and Independent Q-Learning Under Urban Traffic Uncertainty**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38053)
![architecture](https://img.shields.io/badge/QMIX_vs_IQL_EV_Charging-red)
![task](https://img.shields.io/badge/QMIX-magenta)
![organization](https://img.shields.io/badge/Mohammed_V_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把多充电站电动车分配建模为 Dec-POMDP，在 SUMO 六站城市网、五个种子、200 回合的四档流量下比较 QMIX 与独立 Q-learning，QMIX 平均奖励 +0.776 对 +0.578，接受率从 72.4% 升到 94.0%。**</p>
+ **Multi-Agent Reinforcement Learning for Global Climate Policy Cooperation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37870)
![architecture](https://img.shields.io/badge/Negotiation_MARL_Climate-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/Technical_University_of_Denmark-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在 MARL 气候框架中加入多阶段谈判机制，让智能体提出并裁决协议承诺并承担违约惩罚；在四个同质智能体的理想化设定中，中等惩罚改善合作并降低增温，过强惩罚却抑制了承诺力度。**</p>
+ **EARS-Info: Information-Aware Event-Driven Reallocation for Multi-Robot Exploration**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38040)
![architecture](https://img.shields.io/badge/EARS_Info-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/University_of_Klagenfurt-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EARS-Info 在 OpenStreetMap 栅格上把边际感知增益、可行重分配、返回感知路径与感知预约组合进多机器人探索控制器，8 张城市地图 168000 回合中全面领先，8 机器人 3% 丢包时加权发现率从 88.88% 升至 98.46%。**</p>
+ **GARDEN: Generalist Autonomous Reward Design Through Evidence Navigation for Cooperative Multi-Agent Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37926)
![architecture](https://img.shields.io/badge/GARDEN_Evidence_Navigation_Reward_Design-red)
![task](https://img.shields.io/badge/MARL-magenta)
![organization](https://img.shields.io/badge/Karabuk_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/DoganUrgun/GARDEN)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GARDEN 让 LLM reward engineer 依据环境代码、训练记录与行为证据为一个任务族开发奖励程序，再原封不动迁移到未见场景，在 Overcooked 两个布局上把回报提升 58.2% 与 52.5%，SMAX 战斗场景胜率从 51.0% 升到 89.9%。**</p>
+ **Variational Consequence-Driven Offline Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38238)
![architecture](https://img.shields.io/badge/StBR_Structural_Behavior_Regularization-red)
![task](https://img.shields.io/badge/Offline_RL-magenta)
![organization](https://img.shields.io/badge/Nanjing_University_of_Aeronautics_and_Astronautics-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**StBR 指出离线 RL 只匹配动作分布无法保证动态一致性，转而约束策略诱导的状态后果分布，并用按转移动力学组织的结构化高斯潜空间中的闭式 KL 散度替代不可解目标，让行为约束在敏感区域自动收紧。**</p>
+ **CSO: Refining Robotic Policies via Skill Distribution Alignment and Skill-Grained Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38357)
![architecture](https://img.shields.io/badge/CSO_Cascaded_Skills_Optimization-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology_(Shenzhen)-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CSO 用两阶段后训练修补 skill 量化策略：先以拒绝采样监督微调对齐成功轨迹分布，再冻结编码器按整段 skill 计算裁剪重要性比，把 LIBERO 成功率从 80.1% 提到 97.5%，并在五个实体单臂任务上取得 61.0% 成功率。**</p>
+ **Game-Theoretic Foundations for Undiscounted Bisimulation Metrics**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38313)
![architecture](https://img.shields.io/badge/Game_Centric_Bisimulation-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/University_of_Wisconsin–Madison-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇论文把双模拟度量从算子中心改写为零和轮次博弈的 Bellman-Shapley 价值函数视角，使 γ=1 的 total-reward 与 average-reward 设定下度量依然唯一，并证明其可界定 total-reward 与状态无关最优增益下的相对价值差。**</p>
+ **Echo: Scaling Visual Reinforcement Learning with Off-policy Experience**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37865)
![architecture](https://img.shields.io/badge/Echo_Inverse_Distillation-red)
![task](https://img.shields.io/badge/Model_Free_RL-magenta)
![organization](https://img.shields.io/badge/Columbia_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Echo 是单阶段 off-policy 视觉 RL 框架，通过逆向蒸馏让 state-based 辅助策略模仿视觉策略并收集不渲染的廉价经验，再用共享 privileged critic 做价值学习，在 Genesis 上把达到参考回报的时间平均缩短 60% 与 56%。**</p>
+ **Transportable Offline Reinforcement Learning in Presence of Unmeasured Confounding**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38253)
![architecture](https://img.shields.io/badge/CAT_Causal_Transportability-red)
![task](https://img.shields.io/badge/Offline_RL-magenta)
![organization](https://img.shields.io/badge/Duke_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文针对离线 RL 中域差异与未测混淆并存的情形，把 transportability 理论与工具变量、负对照和代理变量结合识别目标域因果量，对 contextual bandit 得到 CAT-CCB、对 episodic MDP 得到 CAT-CMDP，并给出有限样本次优性保证。**</p>
