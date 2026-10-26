# 2026-10-26 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32312)
![architecture](https://img.shields.io/badge/LoRA_MoE_Skill_Conditioning-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Shanghai_Innovation_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把「用哪个技能」与「在哪里接触物体」拆成两级条件：技能查询 token 驱动的 LoRA 专家混合做技能路由，affordance 热力图转成 patch 级轨迹可供性先验；CALVIN ABC→D 长时程多技能泛化达 SOTA。**</p>
+ **From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32271)
![architecture](https://img.shields.io/badge/Loco_Manipulation_Pipeline-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Istituto_Italiano_di_Tecnologia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 VLA 从固定基座机械臂搬到 Unitree Go2 + AgileX Piper 上做闭环 loco-manipulation，系统报告模型变体、动作时域与示范约定等关键选择；扩大示范覆盖使留出末端误差降低 30%。**</p>
+ **UniAction: Unified Action Conditioning for World Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32977)
![architecture](https://img.shields.io/badge/Unified_Action_Conditioning-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把任意动作统一成「离散语义 + 连续时空坐标」的稀疏元素集并直接映射进预训练视频模型的位置空间，配基数校准注意力应对粒度偏差；单一联合训练模型反超四种动作各自的专用专家。**</p>
+ **UniWorld: A Unified World Model for Real-Time Visual World Simulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32381)
![architecture](https://img.shields.io/badge/Unified_Video_Depth_World_Model-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在同一个视频生成模型里耦合深度轨迹与参考外观，视觉与几何历史共用一条时间轴；噪声对齐的重叠续写只提交新生成的 latent，缓存与增量两条路径逐比特一致，实测达实时生成吞吐。**</p>
+ **DT-JEPA: Learning to Predict Future Representations for Decision-Making**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32657)
![architecture](https://img.shields.io/badge/Probabilistic_JEPA_Predictor-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Southeast_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用概率化的 JEPA 预测器建模未来表征在隐空间的条件分布，同时刻画预测信息与不确定性，从无奖励离线数据预训练再在线微调；给出互信息变分下界与有限样本界，D4RL 上适配效率优于 DT 类方法。**</p>
+ **WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31834)
![architecture](https://img.shields.io/badge/Agentic_Real_to_Sim-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 real-to-sim 重构为「迭代精修一个可执行世界程序」：coding agent 分解场景、编排图像与 3D 生成工具、靠验证反馈纠错；以相机位姿为锚的表示让生成场景仍能物理一致地回放轨迹。**</p>
+ **SceneBloom: Agentic Indoor Environment Generation with Realistic and Diverse Layouts for Embodied Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32978)
![architecture](https://img.shields.io/badge/Contract_Guided_3D_Compilation-red)
![task](https://img.shields.io/badge/Neural_Simulator-magenta)
![organization](https://img.shields.io/badge/New_York_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**扩散先验做功能分区的家具布局采样，编译器再按提案中抽取的关系做几何拟合与位姿修正；五种房型里唯一做到零 mesh 碰撞、零越界物体，用其训练的目标导航策略在真实扫描上成功率更高。**</p>
+ **HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.32554)
![architecture](https://img.shields.io/badge/Hierarchical_Graph_World_Model-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**零样本物体导航：LLM 生成房间锚点先验 + 持久空间语义记忆，粗阶段打视觉语义分、细阶段度量符号兼容性，按阶段与 LLM 方向建议融合；HM3D v0.1 报 62.6% SR，作者自陈无逐 episode 重跑记录。**</p>
+ **Multimodal MPC via Bayesian Set Optimization for Dynamic Manipulation of Deformable Linear Objects**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31852)
![architecture](https://img.shields.io/badge/Bayesian_Set_Optimization_MPC-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Istituto_Italiano_di_Tecnologia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**基于控制即推断后验把多模态 MPC 写成集合优化，增量维持多个控制模式，并用执行动力学模型补偿快速操作中的执行偏差；最长绳索跟踪任务 RMSE 降 44.0%，规划时间省 29%–66%。**</p>
+ **EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31845)
![architecture](https://img.shields.io/badge/Reliability_Aware_Flow_Policy-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**同时从机器人示范与噪声第一视角视频学习：按来源可靠性分配动作监督、用 EMA 教师做特权未来表征蒸馏；3 万小时预训练下真机开环动作 MSE 降 20.5%，RoboCasa 少样本成功率提升 8.1 个百分点。**</p>
