<!-- direction: world_model -->

+ **Building World Models from Intrinsic Motivation**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13113)
![architecture](https://img.shields.io/badge/Intrinsic_Motivation_Dreamer-red)
![task](https://img.shields.io/badge/Dreamer-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://neuroagents-lab.github.io/ssrl-agent)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 24 个内在动机目标与 3 种表征学习策略统一到 DreamerV3 框架内系统对比，在 DMC 25 个任务与 Craftax 上发现「好奇加观察重建」整体最强，NGU 组合零样本迁移与少样本适应最佳。**</p>

+ **OnlyAct: Extracting Action Representations from Foundation Models for World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14420)
![architecture](https://img.shields.io/badge/OnlyAct_Contrastive_Action_Encoder-red)
![task](https://img.shields.io/badge/Action_Conditioned_Prediction-magenta)
![organization](https://img.shields.io/badge/University_of_Oxford-green)
[![project](https://img.shields.io/badge/project-blue)](https://runjiali-rl.github.io/onlyact/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**不从零学动作空间，而是用对比学习从冻结的 V-JEPA 2 帧对嵌入中剥离场景、只留动作：13 个基准上平均线性探针 R² 从 0.211 提升到 0.490，并追平隐式动作方法的场景不变性。**</p>

+ **Few-Shot Residual Adaptation of Pretrained Latent World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13592)
![architecture](https://img.shields.io/badge/Dual_Site_Latent_Correction-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/Karlsruhe_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对部署期物理动力学漂移，提出冻结预训练权重、仅从隐空间预测误差自监督学残差的双点校正法：3 段交互共 24 帧即把质心偏移与摩擦变化下的成功率从近零救回 90% 与 100%。**</p>

+ **LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14048)
![architecture](https://img.shields.io/badge/MoT_World_Latent_Action_Experts-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以 14k 小时机器人数据预训练的世界动作模型，用交互中心隐空间在 Mixture-of-Transformers 里桥接世界专家与动作专家，LIBERO 99.5%、RLBench 十任务 88.0%，真机双臂平均成功率 63.8%。**</p>

+ **From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14365)
![architecture](https://img.shields.io/badge/Unified_Meta_Frame-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/showlab/MetaWAM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把机器人信号注入重述为与预训练视频扩散先验的分布对齐问题，用互不重叠的 DCT 频带打包成单帧 meta-frame：RoboCasa 68.9%、LIBERO 98.1%，同时把推理延迟砍掉 39%。**</p>

+ **Koopman Model-Based Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14186)
![architecture](https://img.shields.io/badge/Deep_Koopman_Model-red)
![task](https://img.shields.io/badge/Model_Based_RL-magenta)
![organization](https://img.shields.io/badge/Purdue_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 Koopman 算子把未知非线性动力学线性化，配合一步模型传播与 critic 近似策略目标，策略梯度退化成常数矩阵积；在摆荡、HalfCheetah 与四足任务上比模型式基线收敛更快，并完成真机双足行走。**</p>

+ **Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14419)
![architecture](https://img.shields.io/badge/LLM_Generated_POSG-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/PRISM_AI_Safety_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以 44 个场景、5 个大模型、410 次生成为基准，检验形式化世界模型的机械有效性是否等于忠实性：游戏赛道 134/135 通过审计，结构 F1 却仅 0.366，只有 28 个与参考完全一致。**</p>

<!-- direction: embodied_ai -->

+ **How Much of Your VLA Is kNN**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13160)
![architecture](https://img.shields.io/badge/Training_Free_KNN_Policy-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Sereact_GmbH-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/sereact/lerobot_knn)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**不做任何策略训练，仅检索 1693 条示范的相近状态并复用后继动作块，就在 LIBERO 拿到 91.7%、LIBERO-Plus 拿到 82.4%，扰动下掉幅在九个公开 VLA 中最小，并提出离线指标 LAC。**</p>

+ **DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14092)
![architecture](https://img.shields.io/badge/InteractionMesh_Retargeting-red)
![task](https://img.shields.io/badge/Dexterity-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://robbyant-research.github.io/DexSeed/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 GRAB 的 19 段人手-物序列按 8 种抓取模式扩展成 25270 条物理可执行的机器人示范，用 IsaacLab 的强化学习手指策略生成 rollout，微调出的 VLA 在 pick-and-place 上成功率 97.50%。**</p>

+ **ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13482)
![architecture](https://img.shields.io/badge/Execution_Length_Adapter-red)
![task](https://img.shields.io/badge/Action_Chunking-magenta)
![organization](https://img.shields.io/badge/Tongji_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 ExRL：把长动作块的在线适应从优化动作改为优化执行长度，适配维度不随块长增长；LIBERO 上 20 万步把 π0.5 从近 0% 拉到 90% 以上，真机堆方块约十分钟交互即接近满分。**</p>

+ **From Egocentric Human Video to Robot Manipulation in the Era of Embodied Intelligence**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13610)
![architecture](https://img.shields.io/badge/Ego2Robot_Taxonomy-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_Polytechnic_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://mikewu597.github.io/Ego2Robot_Learning/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**39 页综述把从第一人称人视频学习机器人操作整理为显式本体迁移、显式动作监督、视觉表征预训练、隐式动作与动力学建模四个范式，并配套梳理数据资源与五个开放挑战。**</p>

+ **Ego Guidance: Enhancing Robot Policy Learning with Action-Free Human Egocentric Videos**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13685)
![architecture](https://img.shields.io/badge/SPAR_MoT_Architecture-red)
![task](https://img.shields.io/badge/Robot_Foundation_Pretraining-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://llong-cs.github.io/EgoGuidance)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 SPAR：在 MoT 架构里让生成专家与动作专家共享 VLM 主干、联合预测未来视觉表征，使无动作第一人称视频可与机器人数据共训；视频从 0 增到 1500 小时后 LIBERO-Plus 由 75% 升到 78%。**</p>

+ **Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14488)
![architecture](https://img.shields.io/badge/Event_Indexed_Memory_VLA-red)
![task](https://img.shields.io/badge/Long_Horizon_Task-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**揭示按时间戳填充记忆的 VLA 会被空事件欺骗：两次 5 秒停顿使 RoboMME 计数任务成功率从 47/50 掉到 16、44 掉到 10，去掉时间编码也无效，改按事件索引可免重训恢复半数损失。**</p>

+ **ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric Loads**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13929)
![architecture](https://img.shields.io/badge/Reflection_Consistent_Modulation-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_Polytechnic_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向人形机器人单手负重造成的持续跟踪漂移，提出反射一致的扰动调制与跨负载一致性训练：Unitree G1 上偏航 MAE 下降 81.6%–84.4%，真机 40 次带载导航全部无碰撞抵达目标。**</p>

+ **LEASH: Stay Safe in Agentic Robotics**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14115)
![architecture](https://img.shields.io/badge/Lease_Enforced_Safety_Harness-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Xian_Jiaotong-Liverpool_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 92 个仿真加 13 个真机任务、五类风险的 RoboRisk 基准，测得六个基础模型伤害率 9.06%–76.92%；再用任务、动作、提交三道门的 LEASH 把 GPT-6 Astra 伤害率压到 0.00% 且几乎不损成功率。**</p>

