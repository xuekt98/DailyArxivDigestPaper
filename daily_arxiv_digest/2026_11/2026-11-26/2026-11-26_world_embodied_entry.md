<!-- direction: world_model -->

+ **FoveaWAM: Role-Aware 4D World-Action Modeling for Dynamic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31705)
![architecture](https://img.shields.io/badge/Role_Aware_4D_World_Model-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Beijing_Zhongguancun_Academy-green)
[![project](https://img.shields.io/badge/project-blue)](https://foveawam.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FoveaWAM 按角色分配预测精度：目标用 SE(3) 轨迹、环境用稀疏 3D 流、静态沿用当前帧，在 14 个动态任务的 OnTimeBench 上以 15.1 ms 的 p95 延迟取得 82.1% 成功率，比最强基线高 20.8 个百分点。**</p>

+ **LeanWAM: Learning Latent World Action Models from Frozen Video Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31740)
![architecture](https://img.shields.io/badge/Latent_World_Action_Model-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Michigan-green)
[![project](https://img.shields.io/badge/project-blue)](https://shaolonl-16.github.io/leanwam/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LeanWAM 从冻结视频生成器中把未来先验压进 32 个预测 token 并蒸馏给 1.4B 参数策略，在 LIBERO、LIBERO-Plus、RoboTwin 2.0 上超过 VLA 与 WAM 基线，25.1 ms 出一个动作块，比代表性 WAM 快 12.3–41.5 倍。**</p>

+ **MOVER: Planning Beyond Motion**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30022)
![architecture](https://img.shields.io/badge/Complementary_Event_Routing-red)
![task](https://img.shields.io/badge/Driving_Simulation-magenta)
![organization](https://img.shields.io/badge/University_of_Texas_at_Austin-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MOVER 用训练期教师为残差 BEV 世界模型补充低时间变化但高历史依赖的事件证据，在 nuScenes 上把平均 L2 从 0.65 m 降到 0.55 m、碰撞率从 0.23% 降到 0.12%，每帧仅增加 4.1 ms 且推理零额外成本。**</p>

+ **JEPA-ICL: Progress-Aligned Latent Plans for In-Context Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30516)
![architecture](https://img.shields.io/badge/Progress_Aligned_Latent_Plan-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/University_of_Technology_Sydney-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**JEPA-ICL 在 JEPA 特征空间预测当前子任务剩余的 4 个有序检查点，用这份进度对齐的隐式计划同时指导动作生成与演示检索，Imitator Game 已见任务 80.0%、比 Zero-WAM 高 12.0 个百分点，LIBERO-Plus 提到 73.2% 再至 75.2%。**</p>

+ **Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30666)
![architecture](https://img.shields.io/badge/Pole_Based_Action_Response-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/Beijing_Freedo_Technology_Co._Ltd.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Zhengrong 把隐式轨迹分解为初始锚点、自由响应与动作创新的延迟响应，用共享稳定共轭极点约束时间演化，四个离线图像目标控制基准宏平均成功率 90.83%，比最强基线高 6.08 个百分点，30 步搜索中位延迟均值 77.5 ms。**</p>

+ **World Models as Native Latent Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30898)
![architecture](https://img.shields.io/badge/Native_Latent_Action_Model-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/SenseTime_Research-green)
[![project](https://img.shields.io/badge/project-blue)](https://pawteam-eai.github.io/native-lam/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Native LAM 把预训练视频扩散 transformer 同时用作逆动力学与前向动力学模型，只用可学习动力学寄存器做因果桥接；由此得到的 PAWlicy 以 3.8B 模型在 RoboTwin 2.0 达到 93.6% 平均成功率，全程只用公开数据。**</p>

+ **DexLatentWorld: 3D Cross-Embodiment Latent Action World Models for Zero-Shot Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30907)
![architecture](https://img.shields.io/badge/Cross_Embodiment_Latent_World_Model-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Embodied_Dexterity_Lab_DexLab-green)
[![project](https://img.shields.io/badge/project-blue)](https://vinaymohan0409.github.io/DexLatentWorld/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DexLatentWorld 从重定向人类演示的点云中学习连续潜动作，用对比学习跨本体对齐并直接作为 MPC 搜索空间，抓取与放置分别达到 92% 与 60%（DexWM 为 58% 与 28%），未知灵巧手上真实操作 50 次试验成功 86%。**</p>

<!-- direction: embodied_ai -->

+ **RoboAda: Adapting Frozen Robot Policies at Test Time to Physics They Cannot See**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30209)
![architecture](https://img.shields.io/badge/Test_Time_Body_Inference-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/Tulane_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://RoboAda.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboAda 保持冻结策略与计划不变，用逆动力学模型从机器人自身运动反推隐藏的身体变化并据此重写下一段命令，在 11 种物理偏移下把 5 个冻结策略平均成功率从 27.8% 提到 62.9%，全程无需奖励与梯度步。**</p>

+ **Hi3R-VLA: Grounding Semantics and Actions in 3D**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31535)
![architecture](https://img.shields.io/badge/Geometry_Grounded_VLA-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Inria-green)
[![project](https://img.shields.io/badge/project-blue)](https://cshizhe.github.io/projects/hi3r_vla.html)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Hi3R-VLA 把视觉、语言与动作统一锚定到显式 3D 点云，用 3D-RoPE 注意力建模动作目标与场景点的几何关系，训练参数少于 250M，在 DexJoCo 上 77.3%、DexSuite 上 86%，空间锚点比无锚点变体高 9.2 个百分点。**</p>

+ **FabricBench: A Standardized Policy Benchmark for Bimanual Fabric Manipulation with a Contact-Driven Deformable Simulator**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31577)
![architecture](https://img.shields.io/badge/Contact_Driven_Cloth_Solver-red)
![task](https://img.shields.io/badge/Physics_Simulator-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://fabricbench.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FabricBench 提供 6 个双臂布料任务与 10000 个仿真资产，并配套改良的布料接触求解器，45 次抓取保持释放全部成功而对照基线 0 次；最好的策略平均仅 77%，长时程 T 恤折叠无一超过 36%。**</p>

+ **One Phase Is Enough: Sim-to-Real Transfer with Direct Visual Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31588)
![architecture](https://img.shields.io/badge/One_Phase_Visual_RL-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/Massachusetts_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://jmarangola.github.io/one-phase-visual-rl/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DRIFT 冻结预训练视觉编码器，直接用测试时可见的图像做单阶段视觉 RL，三个真机任务平均相对成功率比两阶段蒸馏高 58.8%，分布外相对优势从约 9% 扩大到 61% 以上，且训练无需反传视觉骨干。**</p>

+ **G0.7: Scaling Up a Fast World Action Model with Long Context**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31822)
![architecture](https://img.shields.io/badge/Long_Context_World_Action_Model-red)
![task](https://img.shields.io/badge/Robot_Foundation_Model-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**G0.7 把世界动作模型的上下文扩到最长 5 分钟并大规模预训练遥操作与人类第一视角视频，Fast 模式在单卡 RTX 5090 上 60 ms 输出 16 步动作块、比 IDM 快 7.6 倍，五个仿真套件平均 70.8 分，RMBench 达 86.2%。**</p>

+ **ReFocus: Progress-Guided Adaptive Practice for Long-Horizon Robotic Manipulation Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32639)
![architecture](https://img.shields.io/badge/Progress_Guided_Adaptive_Practice-red)
![task](https://img.shields.io/badge/Long_Horizon_Task-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://refocus-robotics.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ReFocus 在 Global RL 中用任务 DAG 的进度奖励定位瓶颈子任务，再在 Local RL 把额外交互投给自适应练习窗口，LIBERO-Long 与 RoboCasa365 上取得 97.8% 与 51.3%（π0.5 为 90.6% 与 39.3%），真机 BreadBaker 达 95%。**</p>

+ **DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.32-blue)](https://arxiv.org/abs/2611.32654)
![architecture](https://img.shields.io/badge/Unified_World_Actor_Critic-red)
![task](https://img.shields.io/badge/Planning_with_Reward_Model-magenta)
![organization](https://img.shields.io/badge/University_of_California_San_Diego-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DexWAC 在一次预训练里联合学出 actor、动作条件世界模型与 bootstrapped critic，世界模型只预测动作块终点的视觉潜变量与本体感知，RoboTwin 2.0 平均 88.1%、DexJoCo 65.50%，两个真机任务平均 75% 对 π0.5 的 45%。**</p>

+ **Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33010)
![architecture](https://img.shields.io/badge/Mirror_Robustness_Benchmark-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/iPPLab/robodojo-mirror)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboDojo-Mirror 在保持任务目标、判定标准与策略权重不变的前提下加入单镜、双镜和镜面桌面条件，5 个策略的成功率平均下降 10.8–56.7 个百分点，镜面桌面最多降 62.5 点，且多数失效并未发生机器人与镜面接触。**</p>

+ **PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33144)
![architecture](https://img.shields.io/badge/Programmatic_Coding_Agent_Policy-red)
![task](https://img.shields.io/badge/Dexterity-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://vme0522.github.io/PyRUA-Dex/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PyRUA-Dex 让编码 agent 在仿真中并行探索技能并蒸馏成一个可执行程序，全程不需要专家演示，Bench2Dex 得分 72.9 刷新 SOTA，全随机化 DexJoCo 成功率 81.0%（最强训练策略 40.3%），真机学新曲约 30 分钟。**</p>

+ **OmniAct: One Policy, One Million Embodiments**
[![paper](https://img.shields.io/badge/Arxiv_2611.33-blue)](https://arxiv.org/abs/2611.33158)
![architecture](https://img.shields.io/badge/Scene_Grounded_Kinematic_Graph-red)
![task](https://img.shields.io/badge/Policy_Diffusion-magenta)
![organization](https://img.shields.io/badge/University_of_Washington-green)
[![project](https://img.shields.io/badge/project-blue)](https://omniact.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**OmniAct 用场景坐标下的运动学图直接条件化策略，并程序化生成筛选 100 万个物理可行的机器人形态，在 2000 个未见形态与场景的留出回合上成功率 63.0%，最强基线 57.9%、π0.5 仅 17.8%。**</p>

+ **FlexWAM: Learning Flexible Visual Routing for World Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30024)
![architecture](https://img.shields.io/badge/View_Routed_Action_Attention-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://flexwam.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FlexWAM 用观测条件化路由器在动作注意力中动态挑选关键视角，并以抑制单视角后动作损失的敏感度作为反事实信用训练 critic，两个真实机器人平台 5 个任务上平均成功率分别比最强基线高 16.4 与 23.0 个百分点。**</p>

+ **RoboLiveMem: Is Robot Memory Solved When the World Does Not Wait?**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30047)
![architecture](https://img.shields.io/badge/Live_Clock_Memory_Benchmark-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Tulane-green)
[![project](https://img.shields.io/badge/project-blue)](https://robolivemem.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboLiveMem 让同一批记忆任务分别在世界暂停与世界继续走两种时钟下运行，29 个任务族覆盖 16 个 BEHAVIOR-1K 场景，8 个 Claude 与 GPT 模型平均成功率从暂停时的 97% 掉到实时的 50%，Claude Opus 5.5 仅 44%。**</p>

+ **RMR-VLA: Recurrent Memory Reasoning for Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30145)
![architecture](https://img.shields.io/badge/Recurrent_Memory_Reasoning-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RMR-VLA 在 VLA 内部插入显式记忆推理：先从视觉证据推断事件，再修正任务状态并把子目标落到当前场景，RoboMME 总体 66.46%、Reference 类 79.83%，LIBERO-Mem 90.08%，比同架构无循环版本直接翻倍。**</p>

