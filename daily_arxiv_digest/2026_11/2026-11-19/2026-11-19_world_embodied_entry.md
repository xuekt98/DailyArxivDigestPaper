<!-- direction: world_model -->

+ **JointGV: Structure-Aware Correction of Visual World Models with Parallel Graph Dynamics for Long-Horizon Modeling**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22543)
![architecture](https://img.shields.io/badge/Joint_Graph_Visual_Correction-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Oxford-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/JasonLvernex/Joint_Graph_Vedio_Latent_Dynamic_World_Model)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把任务条件场景图与视觉世界模型并行 rollout，用图运动上下文算出有界残差来校正姿态漂移：32 步关节位置误差下降 11-28%，真实倒立摆 32 步杆角误差从 12.56 度降到 6.69 度。**</p>

+ **Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21782)
![architecture](https://img.shields.io/badge/EyeHeight_Benchmark-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/State_Key_Laboratory_for_Novel_Software_Technology_Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**六个开源交互式视频世界模型在 180 度转弯行走中都会把相机拉向人眼高度，0.15 米起步的片段只有 0-20% 仍守在 1.3 倍高度内；论文给出 EyeHeight 基准与无引导采样加高度均衡微调的修复方向。**</p>

+ **Escaping Latent Traps by Remembering: Training-Free Episodic Kernel Repulsion for World-Model Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22470)
![architecture](https://img.shields.io/badge/Episodic_Kernel_Repulsion-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**免训练的 Episodic Kernel Repulsion 用 top-k 高斯核惩罚与已访问潜状态记忆过近的候选计划，LeWM 平均成功率 31.8% 升到 46.7%、H-JEPA 从 54.7% 升到 64.0%，PointMaze 从 44.7% 到 100.0%。**</p>

+ **Plausible Videos Can Lead to Poor Decisions: Diagnosing and CURE-ing World Models for Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22561)
![architecture](https://img.shields.io/badge/CURE_Certificate_Guidance-red)
![task](https://img.shields.io/badge/Model_Based_RL-magenta)
![organization](https://img.shields.io/badge/Cornell_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CURE 用证书判断动作条件世界模型能否信任：被信任决策的后悔值 0.06 对 0.38，而感知质量却区分不出好坏；据此决定重加权数据、多采样 rollout 还是主动探索，回后悔比最悲观规则再低 10-25%。**</p>

+ **Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22691)
![architecture](https://img.shields.io/badge/Closed_Loop_Interactive_WM-red)
![task](https://img.shields.io/badge/Driving_Simulation-magenta)
![organization](https://img.shields.io/badge/Tongji_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**闭环交互式驾驶世界模型：背景车策略在与渲染视角下的自车规划器对抗中做多智能体 RL，使交互行为偏差下降 85%、新视角车辆 PSNR 提升 2.0 dB，信号灯意图还会影响四分之一场景的自车决策。**</p>

+ **AR-WAM: efficient streaming world-action modeling for autonomous driving**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21851)
![architecture](https://img.shields.io/badge/AR_WAM_Streaming-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Toyota_Motor_North_America_R&D_-_InfoTech_Labs-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AR-WAM 用因果视频骨干增量更新并复用历史视觉上下文，再用单次前向的未来特征条件化轨迹生成，单前置相机在 NAVSIM-v1 上取得 91.5 PDMS，强化学习后升至 94.0。**</p>

+ **WM-Quant: Rollout-Aware Post-Training Quantization for JEPA-Style World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21882)
![architecture](https://img.shields.io/badge/WM_Quant_PTQ-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/University_of_South_Carolina-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WM-Quant 是首个面向 JEPA 式世界模型的后训练量化框架：LeWM PushT 上 W3A3 成功率 58%、W4A4 81.3%，而基线仅 10% 与 20%；关键在早编码器精度、控制路径保浮点与整段 rollout 感知缩放。**</p>

<!-- direction: embodied_ai -->

+ **ReLAP: Latent Action Pretraining through Recurrent Video Prediction in JEPA Space**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22077)
![architecture](https://img.shields.io/badge/ReLAP_Recurrent_Latent_Action-red)
![task](https://img.shields.io/badge/Robot_Foundation_Pretraining-magenta)
![organization](https://img.shields.io/badge/Bagel_Labs-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ReLAP 在冻结 JEPA 空间里用共享逆动力学模型学连续潜动作，并由循环预测未来特征的世界模型把后期误差回传到早期动作；仅 11M 条预训练样本即在 LIBERO 达 97.9%、LIBERO-Plus 扰动下 70.0%。**</p>

+ **From Temperature-Limited to Battery-Limited Legged Locomotion**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22231)
![architecture](https://img.shields.io/badge/Thermal_Aware_Locomotion_Policy-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Woven_by_Toyota-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**不看温度也能训出热感知策略：13 节点集总 RC 热网络（22 参数）跨机型预测 12 路电机温度 RMSE 低于 1 度，Unitree Go2 带 5 kg 载荷 1 m/s 从 19 分钟热关机延到 174 分钟跑完 10.0 km。**</p>

+ **Agile Monoped Hopping on Complex and Discrete Terrain via Kinodynamic Planning with Distilled MPPI Steering**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21905)
![architecture](https://img.shields.io/badge/FlowRRT_CFM_Steering-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/University_of_Michigan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FlowRRT 把转向当作集合值预测：多起点 MPPI 专家离线收集整份可行动作集，再用条件流匹配蒸馏成生成式采样器，1 秒内解出 93% 规划问题（SST 26%、RL-RRT 为零），跟踪误差 1.37 cm。**</p>

+ **RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22138)
![architecture](https://img.shields.io/badge/RoboTeam_MultiArm_Benchmark-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboTeam 让智能体只凭相机图像实时控制 4-16 条机械臂完成 36 个协作长任务：gpt-6.1-sol 完成 28 个却要 3.5 小时与 218 million 输入 token，三分之一步骤至少失败一次，其他模型最多 3 个。**</p>

+ **Reconfiguring Procedural Knowledge for Compositional Robot Skill Adaptation**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22174)
![architecture](https://img.shields.io/badge/RecPo_Procedure_Views-red)
![task](https://img.shields.io/badge/Long_Horizon_Task-magenta)
![organization](https://img.shields.io/badge/Sungkyunkwan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RecPo 用多视角程序知识库把「适配新目标」变成重组既有技能：扩展 Franka Kitchen 长程任务上 91.9% 有序完成率、每回合任务推理仅 1.0 ms，真实机器人上靠局部记忆编辑免重训适配。**</p>

+ **Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22275)
![architecture](https://img.shields.io/badge/Heave_Ho_Decentralized_Control-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Heave-Ho 让多个人形在无网络通信下协作：底层用多智能体后训练把人形基础跟踪模型适配到物理耦合交互，上层用视觉语言规划器加语音 leader-follower 同步，从 2 台扩展到 10 台并泛化到异构队伍。**</p>

+ **Similar Is Not Useful: Selecting In-Context Demonstrations by Closed-Loop Utility**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22295)
![architecture](https://img.shields.io/badge/Closed_Loop_Utility_Retrieval-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在冻结的 RICL（pi0-FAST/LIBERO）上，闭效用最高的五条演示池成功 66.4%，最相似池 55.7%、随机池 55.5%；相似度与成功的 Spearman 相关只有 0.10，相似并不等于有用。**</p>

+ **FIRE-Drive: Feasibility-Informed Risk Evaluation for End-to-End Diffusion Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22297)
![architecture](https://img.shields.io/badge/FIRE_Drive_Risk_Scoring-red)
![task](https://img.shields.io/badge/Diffusion_Policy-magenta)
![organization](https://img.shields.io/badge/Xidian_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FIRE-Drive 为端到端扩散规划补上可行性先验与风险判别：动态可行锚点初始化、候选专属 BEV 风险证据与紧凑监督，使 NAVSIM v1 的 PDMS 达 91.5，220 条 Bench2Drive 路线驾驶分 71.43、成功率 42.73%。**</p>

+ **Hidden Variables Behind Real-Robot Data Quality: Lessons from Hundreds of Thousands of Hours**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22388)
![architecture](https://img.shields.io/badge/Data_Collection_System_Study-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/AgiBot-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把真实机器人数据质量拆成可测隐变量：25 台双臂运动学研究、遥操作对照与 pi0.5 微调三线并行，指出并行控制身体部位可缩短完成时间 43-53%，推理期标定失配会让 30 次试验全部失败。**</p>

+ **CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22395)
![architecture](https://img.shields.io/badge/CoBoVLA_Discrete_Codes-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CoBoVLA 用离散可解释码解耦语言理解、规划与控制，250M 参数在 LIBERO-Goal 达 91.4%、LIBERO-Para 81.1%、单步 17 ms；指令编码正确时成功率 91%，否则只有 27.2%。**</p>

+ **InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22584)
![architecture](https://img.shields.io/badge/InteractVLA_Geometric_Interface-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Renmin_University_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**InteractVLA 把预训练流式 VLA 变成可几何操纵、可检查的工具：正向把末端目标翻译成动作专家输入梯度，反向把动作块与标定重投影交回智能体，LIBERO-Plus 达 99.4%、RoboCasa365 89.4%。**</p>

+ **Task Convergent Flow Matching for Generative Robotics**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22609)
![architecture](https://img.shields.io/badge/Task_Funnel_Flow_Refinement-red)
![task](https://img.shields.io/badge/Policy_Diffusion-magenta)
![organization](https://img.shields.io/badge/Istituto_Italiano_di_Tecnologia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**推理期任务级漏斗精修流匹配策略：用并行物理 rollout 评估候选动作块并要求每个块净进展，PushT 成功率 31.3% 升到 88.5%、三块堆叠 77.0% 升到 86.0%，最大进展损失均值下降 19%。**</p>

+ **Learning Accurate End-Effector Trajectory Tracking with Inertial Feedback for a Quadruped Manipulator**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22695)
![architecture](https://img.shields.io/badge/Inertial_Feedback_Tracking-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Jeonbuk_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把末端惯性测量作为关节编码器之外的观测补偿腿-臂运动链误差：真机上相对名义基线把 MoCap RMSE 降低 17.3% 与 28.0%，并量出 FK 重建与实测末端位置平均相差 12.61 毫米。**</p>

