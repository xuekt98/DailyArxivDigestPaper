# 2026-10-28 - 强化学习核心 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36270)
![architecture](https://img.shields.io/badge/Phase_Conditioned_Critic_PPO-red)
![task](https://img.shields.io/badge/PPO-magenta)
![organization](https://img.shields.io/badge/ETH_Zurich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把任务序性写进 PPO：相位条件化 critic 配合相位门控奖励函数与多相位重置课程引导探索，使每个环境只产出一条统一策略即可执行搬箱子等复杂多阶段 loco-操作行为，并在 Spot 四足操纵轮胎与 Unitree G1 人形搬箱两个平台上验证。**</p>
+ **VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37378)
![architecture](https://img.shields.io/badge/VLA_Stem_Brainstem_Safety_RL-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**受脑干启发的轻量 RL 安全机制 VLA-Stem：把 VLA 的逻辑推理与运动协调通路同「反射与安全」通路分离并耦合，用在线 RL 训练独立安全分支、教师经参考轨迹跟随到静态再到动态避障的课程学习，在保持主策略任务能力的同时提供快速物理风险响应。**</p>
+ **Multi-Agent Reinforcement Learning of Co-Adaptive Hip Exoskeleton Control (MARL-Exo) for Metabolic Energy Reduction**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37441)
![architecture](https://img.shields.io/badge/MARL_Exo_Hip_Exoskeleton-red)
![task](https://img.shields.io/badge/MARL-magenta)
![organization](https://img.shields.io/badge/New_Jersey_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MARL-Exo 把 304 个肌肉驱动、随机化解剖步态速度的人体模型与双侧髋外骨骼策略作为两个智能体在共享物理仿真中并发两阶段训练，并以稳定 PD 通道传递人体动作；目标直指代谢能耗降低，并给出含伦理审批的人体实验协议与两个主动控制器的对比。**</p>
+ **Bridging Exploration and Loss of Plasticity in On-Policy Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36309)
![architecture](https://img.shields.io/badge/Sigma_Loss_Of_Plasticity-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/Politecnico_di_Torino-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**系统分析 PPO 配各向同性高斯策略时的可塑性丧失：报告多个刻画策略标准差 σ 影响的指标，观察到 σ 对 LoP 程度有显著影响并给出理论与实验论证，同时解释了多种流行 LoP 缓解技术为何有效，在 7 自由度机械臂上完成真实部署验证。**</p>
+ **Repulsive Population Policy Gradients for Behaviorally Diverse Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36425)
![architecture](https://img.shields.io/badge/RePPO_Population_Policy_Gradients-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**基于 Soft QD 视角提出 RePPO：用群体依赖、动态塑形的奖励把 PPO 改造为联合优化一组紧凑的高质量多样策略，无需行为空间离散化与进化算子；在连续控制上取得强质量-多样性折中，在像素任务上质量持平 PPO 而多样性显著更高，并首次把 QD-RL 扩展到大语言模型微调域。**</p>
+ **Action-Value Calibration via Continuation Sharing for Long-Horizon Agentic Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37195)
![architecture](https://img.shields.io/badge/ConCal_Continuation_Calibration-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/Sun_Yat-sen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对 GiGPO 用单次续跑估计动作价值的问题，ConCal 按状态-动作-状态转移匹配同任务的访问，共享续跑证据并把校准值向后传播以修正更早的动作价值，无需额外 rollout；在 Qwen2.5-1.5B-Instruct 上于 ALFWorld 与 WebShop 比 GiGPO 提升 3.39 与 5.86 个百分点。**</p>
+ **Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37543)
![architecture](https://img.shields.io/badge/Event_Proxy_Analytic_Simulator-red)
![task](https://img.shields.io/badge/Sim_to_Real_RL-magenta)
![organization](https://img.shields.io/badge/Delft_University_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对事件相机导航 RL 训练过慢，论文提出完全免渲染的解析式事件模拟器：利用事件只响应运动对比边缘的物理特性，从场景几何的 3D 边缘点与自运动直接合成事件流，从而以极低算力支撑导航策略训练。**</p>
+ **Freeze, Don't Clone: Fine-Tuning with Expressive Policies Without Retaining Offline Data**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36247)
![architecture](https://img.shields.io/badge/Freeze_Behavioral_Prior_No_Retention-red)
![task](https://img.shields.io/badge/Offline_RL-magenta)
![organization](https://img.shields.io/badge/Mila_-_Quebec_AI_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在离线数据无法全程留存的 offline-to-online 设定下，论文主张「Freeze, Don't Clone」：离线预训练后冻结行为先验、只用在线数据继续更新 critic；消融显示 BC 损失权重在 0.1×–10× 范围内性能均不敏感，反驳了防遗忘必须持续混合 BC 损失的直觉。**</p>
+ **Frequency-Uniform Log-Regret Reinforcement Learning for Diffusions**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36758)
![architecture](https://img.shields.io/badge/Frequency_Uniform_Log_Regret_Diffusions-red)
![task](https://img.shields.io/badge/RL_Theory-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对时间离散步长 δ 增大使标准有限视界遗憾界恶化的问题，论文为受控扩散的回合式值型 RL 证明 O(log K) 遗憾界且常数对 δ 均匀（漂移线性于未知参数、协方差未知常量时为高概率 O(log K log log K)），并给出受约束的模型基拟合 Q 算法 CD-FQ。**</p>
+ **CONCUR: Concordant Auxiliary Rewards for Multi-Task, Multi-Reward Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36437)
![architecture](https://img.shields.io/badge/CONCUR_Concordant_Auxiliary_Rewards-red)
![task](https://img.shields.io/badge/Policy_Gradient-magenta)
![organization](https://img.shields.io/badge/Google_DeepMind-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CONCUR 用优势估计替换门控辅助奖励的标准化分数：取满足「主奖励更高者不得更低分、触顶者等分」两条件的最近分数，把辅助信号投影回与主奖励一致的方向；在 Qwen3-4B-Base 上通过余弦、排序能量占比与触顶占比等诊断量逐对分析辅助奖励偏离主奖励的位置与幅度。**</p>