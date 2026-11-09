<!-- direction: world_model -->

+ **MDF++: Visuo-Tactile World Action Model with End-to-end Representation Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09293)
![architecture](https://img.shields.io/badge/MDFpp_Visuo_Tactile_WAM-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Department_of_Robotics_University_of_Michigan-green)
[![project](https://img.shields.io/badge/project-blue)](https://jointmdf.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**端到端学习多传感潜表征的视触觉世界-动作模型，用多任务扩散强制与跨模态选择性梯度流规避特征坍塌，五个仿真操作任务平均成功率从 68.4% 提升到 86.9%。**</p>

+ **Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09625)
![architecture](https://img.shields.io/badge/TT_MBRL-red)
![task](https://img.shields.io/badge/Model_Based_RL-magenta)
![organization](https://img.shields.io/badge/Computer_Vision_Lab_CAIDAS_&_IFI_University_of_Wurzburg-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/burchim/TT-MBRL)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在测试时用梯度下降把每个回合的观测记忆写进世界模型参数，Memory Maze 15×15 上把 R2I 从 42.0 提到 54.1、逼近人类 67.7，同时保持 DeepMind Control 与 Atari 100k 的原有水平。**</p>

+ **JEPAhead: From Inpainting to Causal Forecasting for Urban Driving**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08657)
![architecture](https://img.shields.io/badge/JEPAhead_Causal_Predictor-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/Eldorado_Research_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把预训练 V-JEPA1 预测器从双向潜变量修补改造成无动作因果预测，冻结编码器在 CARLA Town12 上以 69.0% 的 top-1 检索率命中 591 个候选中的正确未来，远超持久性基线的 55.3%。**</p>

+ **FATHOM: World-Model-Guided Diffusion Action-Trajectory Selection for Sparse-Marker AUV Tracking**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08898)
![architecture](https://img.shields.io/badge/FATHOM-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Robotics_and_Control_Laboratory_School_of_Advanced_Manufacturing_and_Robotics_Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向稀疏光标记 AUV 跟踪的世界模型引导扩散轨迹选优框架，用多模态循环状态空间模型融合标记、惯性与动作历史形成预测信念，再由世界模型评估扩散候选轨迹的跟踪后果。**</p>

+ **LEF-JEPA: Denoising-Trained Latent Energy Fields for Spatial Representation Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08989)
![architecture](https://img.shields.io/badge/LEF_JEPA-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/Qinous_Technology_Co._Ltd-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用目标引导的潜变量恢复学习相对能量场，再以相对能量约束把稠密空间结构监督传给视觉编码器，能量模块仅用于预训练，ViT-B 上分类、分割与规划三项均超过 V-JEPA2.1。**</p>

+ **EGT: Execution-Grounded Traversability through Learned Closed-Loop Trajectory Distributions**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09270)
![architecture](https://img.shields.io/badge/EGT_Flow_Matching_Traversability-red)
![task](https://img.shields.io/badge/Traversability_Estimation-magenta)
![organization](https://img.shields.io/badge/Institute_of_Technology_University_of_Tartu-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把越野可通行性重新定义为车辆-控制器对执行候选路径的概率，用条件潜空间流匹配预测闭环轨迹分布，650 次试验中保守拒判降到 2.2%、分类准确率达 97.4%。**</p>

+ **A Stochastic Latent Variable Generalization of Joint-Embedding Predictive Architectures**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09302)
![architecture](https://img.shields.io/badge/S_JEPA-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/Imperial_College_London-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/giakoumoglou/sjepa)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 JEPA 的辅助变量 z 从固定确定性 token 升级为真正的随机潜变量，用后验推断与上下文条件先验建模多种合理补全，匹配架构下超过 I-JEPA 与 LeJEPA，参数仅增约 1%。**</p>

<!-- direction: embodied_ai -->

+ **On Agentic Manipulation Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09892)
![architecture](https://img.shields.io/badge/AMP1_Harness-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Apple-green)
[![project](https://img.shields.io/badge/project-blue)](https://apple-aiml-research.github.io/ml-amp/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**系统性分析智能体式操作策略：让通用大模型直接操控机械臂的 AMP1 harness 在 RoboLab-120 上零样本成功 85.6%，真机 108 次试验成功 104 次，全面超过 VLA 与世界-动作模型。**</p>

+ **STRIDE: Learning Humanoid Locomotion in Minutes with Acceleration-Based Rewards**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08857)
![architecture](https://img.shields.io/badge/STRIDE-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Technical_University_of_Darmstadt-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用只依赖机载 IMU 的加速度奖励训练人形步态，配合高增益关节位置控制与左右对称增强，Unitree G1 与 Booster T1 仅需 14 分钟样本即可学会行走，训练跌倒减少 81%。**</p>

+ **PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08917)
![architecture](https://img.shields.io/badge/PRISM-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Chicago-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把可复用技能做成参数级低秩原语并用 VLM 条件路由逐块调用的 VLA 适配框架，RoboCasa365 上原子技能成功率 56.43%、长时程复合任务 20.00%，显著优于标准 LoRA 两阶段微调。**</p>

+ **RevoSim: Scalable Multimodal Tactile Simulation for Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08939)
![architecture](https://img.shields.io/badge/RevoSim-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/HKUSTGZ-green)
[![project](https://img.shields.io/badge/project-blue)](https://braincotech.github.io/RevoSim-web/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为 BrainCo Revo3 灵巧手打造的多模态触觉仿真器，联合建模 285 个压阻式触觉单元与 5 个视触觉指尖，单张 RTX 5090 上可支撑 4096 个并行环境。**</p>

+ **Goodhart in the Planner: Sampling-Based Control Exploits Rewards Learned from Human Preferences**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09670)
![architecture](https://img.shields.io/badge/Goodhart_In_The_Planner-red)
![task](https://img.shields.io/badge/Planning_with_Reward_Model-magenta)
![organization](https://img.shields.io/badge/Walker_Department_of_Mechanical_Engineering_The_University_of_Texas_at_Austin-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**量化用人类偏好奖励模型做采样式规划时的 Goodhart 效应：加大 MPPI 搜索强度会让真实回报最多下降 76%，抽屉任务 20 次里 0 次打开，而留出标签准确率仍高达 0.75-0.97。**</p>

+ **Computer-Use Agents Are Embodied Generalists**
[![paper](https://img.shields.io/badge/Arxiv_2611.09-blue)](https://arxiv.org/abs/2611.09847)
![architecture](https://img.shields.io/badge/CUA_Embodied_Generalist-red)
![task](https://img.shields.io/badge/Computer_Use_Embodied-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://pranjal2041.github.io/cua-embodied)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论证计算机使用智能体可以充当具身通才：把物理环境渲染成屏幕软件后，仅替换软件环境不改智能体，即在四场 ECCV 工作坊赛事中拿下第一、第二、第三与第六名。**</p>

+ **Lodos: A Lightweight Simulator Designed for Contact-Rich Interactions with Detailed Meshes**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08872)
![architecture](https://img.shields.io/badge/Lodos-red)
![task](https://img.shields.io/badge/Physics_Simulator-magenta)
![organization](https://img.shields.io/badge/University_of_Tubingen-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/martius-lab/lodos)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从零设计的轻量级刚体仿真器，用 3D 样条 SDF 与球-SDF 窄相、盒约束二次规划接触求解把碰撞检测 GPU 化，在复杂网格场景相对 MJWarp 取得约一个数量级的吞吐提升。**</p>

+ **VLA Handover: Failure-Prediction-Based Switching from On-Robot to Server VLA Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08987)
![architecture](https://img.shields.io/badge/VLA_Handover-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/School_of_Engineering_Institute_of_Science_Tokyo-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**让机器人常驻小 VLA、仅在预测小模型将失败时切换到服务器大 VLA，LIBERO 三个套件上成功率比纯本地高 11-22 个点、比纯服务器少发 49%-77% 的请求，单服务器可支撑约 12 台机器人。**</p>

