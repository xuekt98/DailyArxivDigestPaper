# 2026-11-02 - 强化学习 · 核心算法 / 理论 / MARL / sim-to-real 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Statistical Foundations of Reinforcement Learning: A Non-Asymptotic Perspective**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41903)
![architecture](https://img.shields.io/badge/Non_Asymptotic_Tabular_RL_Monograph-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/University_of_Pennsylvania-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**一部 326 页的 RL 统计基础专著，以表格型 MDP 为对象，系统处理生成模型、在线与离线三种采样机制及 model-based / model-free 两条范式，围绕非渐近样本复杂度给出极小极大最优的算法设计与常用算法的锐利刻画。**</p>
+ **Hyperbolic Inverse Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42104)
![architecture](https://img.shields.io/badge/Hyperbolic_IRL_Distance_Reward-red)
![task](https://img.shields.io/badge/Inverse_RL-magenta)
![organization](https://img.shields.io/badge/University_of_California_San_Diego-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 IRL 奖励参数化为特征向量与学习参数之间的双曲距离，在标准基准上与线性、非线性基线相当，却在低数据与稠密环境中更优；在 LACMA 陶瓷展厅的 HUMEX 人类轨迹上，双曲模型仅用 15 个奖励参数即取得最佳 ADE/FDE，并拟合出不可分的合取奖励结构。**</p>
+ **Continual Reinforcement Learning Is an Integration Problem**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41809)
![architecture](https://img.shields.io/badge/Ten_Desiderata_Continual_RL-red)
![task](https://img.shields.io/badge/Meta_RL-magenta)
![organization](https://img.shields.io/badge/University_College_London-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/fractalbrain-ai/10d-game)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出持续强化学习的十条设计准则，按协议层、系统层与行为层划分证据类型并用已有工作逐条检验；作者指出尚无任何已发表评测能证明这些能力在同一个 agent 的一次连续生命周期内共存，并附上可玩的持久世界场景与基准提案。**</p>
+ **When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41962)
![architecture](https://img.shields.io/badge/Game_MDP_Correspondence_Monograph-red)
![task](https://img.shields.io/badge/Multi_Agent_RL-magenta)
![organization](https://img.shields.io/badge/Universidad_Pontificia_Comillas-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**一部 145 页的对照专著，把「博弈是否就是 MDP」拆成定义等价、值与解保持的精确归约、以及会在可识别条件下失效的结构类比三层，逐条标注到正规式、重复博弈、扩展式、贝叶斯、Stackelberg、均场与演化博弈，并收录不成立的对应。**</p>
+ **Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41022)
![architecture](https://img.shields.io/badge/Density_Guided_Bootstrap_Boundary-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/University_of_Michigan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为潜在世界模型 RL 提出密度引导的 bootstrap 边界：用一个分数修正的辅助场累积散度作为轨迹相关的密度代理，据此在硬边界处截断回报展开或在软边界处平滑回归到 critic 自举，并在 DreamerV3 中证明门控 Bellman 算子为严格压缩映射。**</p>
+ **Risk-Sensitive Mission Planning for Multi-Target On-Orbit Inspection via Distributional Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41647)
![architecture](https://img.shields.io/badge/QR_DQN_Mean_Variance_Mission_Planning-red)
![task](https://img.shields.io/badge/DQN-magenta)
![organization](https://img.shields.io/badge/Université_Paris-Saclay,_CentraleSupélec-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用分位数回归 DQN 学习在轨服务任务的完整回报分布，在低地球轨道多目标巡检中以 mean-variance 准则同时权衡期望与方差；五个目标卫星的实验显示单一风险厌恶权重即可在不变环境与奖励下移动策略，使回合回报方差约减半并降低任务失败概率。**</p>
+ **TalentRL: Strategy-Guided Reinforcement Learning for Hierarchical Skill Routing**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41143)
![architecture](https://img.shields.io/badge/TalentRL_Hierarchical_Skill_Routing-red)
![task](https://img.shields.io/badge/Hierarchical_RL-magenta)
![organization](https://img.shields.io/badge/Microsoft_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TalentRL 把程序性记忆拆成粗粒度策略与细粒度技能两层，用同任务下匹配干预的奖励对比训练策略选择、用 group-relative 优势优化下游执行；在七个问答基准与 ALFWorld、WebShop 上相对零样本基线提升 7.53%–9.21%，RL 阶段再提升 7.58%–9.32%。**</p>
+ **Joint-Health-Aware Reinforcement Learning for Robust Robot Control Under Actuator Degradation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41348)
![architecture](https://img.shields.io/badge/Joint_Health_Aware_RL-red)
![task](https://img.shields.io/badge/PPO-magenta)
![organization](https://img.shields.io/badge/Tianjin_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把执行器退化建模为动作的乘性衰减，用 HealthNet 从近期的观测与动作推断逐关节健康向量并作为策略输入，使控制力在健康与退化关节间重新分配；在 Walker、Go2、Cassie 与 ManiSkill 上，移动任务回报最高提升 250.1%，操作成功率最高提升 15.2 个百分点。**</p>
+ **Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42100)
![architecture](https://img.shields.io/badge/Plasticity_Loss_Noise_Study-red)
![task](https://img.shields.io/badge/SAC-magenta)
![organization](https://img.shields.io/badge/University_of_Freiburg-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在加入受控观测与动作噪声的三个 DeepMind Control 任务上训练 SAC，系统刻画噪声与可塑性流失的双向关系：更难的任务上噪声加速可塑性流失，而 periodic reset 相对基线的优势随噪声增大；resets 加 layer norm 在所有噪声水平上都弱于单独 resets。**</p>
+ **CausalXRL: Explainable Reinforcement Learning through Causal Graph Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42028)
![architecture](https://img.shields.io/badge/CausalXRL_Causal_Graph_Reasoning-red)
![task](https://img.shields.io/badge/Model_Free_RL-magenta)
![organization](https://img.shields.io/badge/Stony_Brook_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CausalXRL 用可解释表征与 Rubin 因果模型在无预定义因果结构的条件下学习决策的因果结构，在 CartPole、LunarLander、PongDuel 与 MicroRTS-Lite 上给出保真度与结构学习耗时，并用 RTS 专家定性研究验证其高层策略可读性。**</p>
