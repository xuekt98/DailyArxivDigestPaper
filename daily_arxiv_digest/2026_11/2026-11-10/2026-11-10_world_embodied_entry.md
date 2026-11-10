<!-- direction: world_model -->

+ **The World Model Planning Accelerator (WMPA): Hardware-Algorithm Co-Design for Embedded AI in Robotics**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10316)
![architecture](https://img.shields.io/badge/WMPA_Near_Memory_Accelerator-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/American_University_of_Sharjah-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Prk10/world-models-theoretical-min)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从信息论与布尔电路复杂度推出世界模型潜状态转移的算术与能耗下限，实测 DreamerV3 式 RSSM 在 T4 上单次规划能耗比 12nm CMOS 下限高 5.91×10^10 倍，并据此提出近存计算加可变精度、实时熵估计与写时复制暂存的 WMPA 加速器。**</p>

+ **Multi-Objective Adaptation After Deployment: A Position on World Models for Remote Robot Teams**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10435)
![architecture](https://img.shields.io/badge/Shared_World_Model_Pipeline-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Collaborative_Robotics_and_Intelligent_Systems_CoRIS_Institute_Oregon_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**立场论文指出，远程机器人团队在部署后若环境、硬件或编队发生变化，会重排已有的 Pareto 解集；作者主张用世界模型在不实际执行的前提下重估策略，并给出模型化重评估、预测与实测对照验证、共享信息并入世界模型三项研究优先级。**</p>

<!-- direction: embodied_ai -->

+ **GUARD: Anomaly-Informed Q-Steering for Generative Robot Policies in Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10343)
![architecture](https://img.shields.io/badge/Anomaly_Q_Steering-red)
![task](https://img.shields.io/badge/Policy_Diffusion-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GUARD 把策略训练分布上学到的稠密异常分数与稀疏任务奖励一并送入 Q 函数，用其梯度在去噪阶段把扩散与流匹配策略推回高支撑区域且不改动预训练权重，在四个 Adroit 任务上把扰动动力学成功率提到 80.0%，并完成真机螺丝刀旋转迁移。**</p>

+ **SimDuoReal: Object-Centric Bimanual Policy for Emergent Dexterity**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10410)
![architecture](https://img.shields.io/badge/Object_Centric_Bimanual_Policy-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Amazon_FAR-green)
[![project](https://img.shields.io/badge/project-blue)](https://simduoreal.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SimDuoReal 只用共享的物体中心奖励、不为抓取、交接、重抓分别设计奖励，就让策略涌现出双臂协调与手内调整，再用 DAgger 与强化学习把三个专家蒸馏成单一策略，真机四个任务 80 次试验成功 61 次。**</p>

+ **Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10443)
![architecture](https://img.shields.io/badge/SPARK_VLA-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/DGIST-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/park-jungin/spark-vla)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SPARK-VLA 用「保留—特化—路由」框架改造 VLA：把冻结三维专家的空间表征蒸馏进 LoRA 视觉分支，并按动作损失梯度路由 token，在 0.5B 骨干加 53M 可训练参数下于 LIBERO 取得 98.5%、LIBERO-Plus 取得 78.6%。**</p>

+ **CPNav: Calibrated Vision-Language Navigation for Object-Goal Search in Unseen Environments**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10366)
![architecture](https://img.shields.io/badge/Conformal_VLM_Navigation-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/University_of_California_Los_Angeles-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/practice-lab-ucla/CPnav)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CPNav 在无地图的目标物导航中，把 VLM 的动作打分用保形预测离线校准，再与碰撞感知规划、带回溯的树搜索结合，HM3D v0.2 成功率 86.0%、真机 Hiwonder 上从 66.7% 提到 83.3%，且校准层不改动底层策略。**</p>

+ **Grip, Trace, Write: Force-Aware Imitation and Reinforcement Learning for High-DoF Robotic Handwriting**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10451)
![architecture](https://img.shields.io/badge/Two_Branch_Grasp_Writing-red)
![task](https://img.shields.io/badge/Dexterity-magenta)
![organization](https://img.shields.io/badge/Daxo_Robotics-green)
[![project](https://img.shields.io/badge/project-blue)](https://dexwriting.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Grip、Trace、Write 把自由持笔的手写建模为抓握与书写两分支的力感知仿真环境，用抓握学习加逆解行为克隆初始化、再用结果导向强化学习精修，把平均完成率提到 94.8%，接触力误差降低 53%。**</p>

+ **Tactile Sensors Are an Effective Substitute for Wrist Cameras in Contact-Rich or Occluded Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10490)
![architecture](https://img.shields.io/badge/Visuotactile_ACT_Policy-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Toyota_Research_Institute-green)
[![project](https://img.shields.io/badge/project-blue)](https://annieyaj.github.io/tactile-vs-vision/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把两片低成本 FlexiTac 阵列接入视触觉 ACT 策略，在固定演示与固定架构下逐一开关腕部相机与触觉：触觉带来的成功率增益为 31.7–60.0 个百分点，高于腕部相机的 18.3–28.3 个百分点，并在三个接触密集任务上全面胜出。**</p>

+ **Detecting and Explaining Robot Policy Failures from Sparse Internal Features**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10400)
![architecture](https://img.shields.io/badge/MIND_SAE_Diagnosis-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/CARL_Lab_Department_of_Computer_Science_University_of_New_Hampshire-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MIND 用逐 token 拟合的稀疏自编码器把 VLA 策略内部激活拆成人可读概念并加以命名，闭环夹紧实验证实策略确实经由这些概念动作，同一套特征既做失效检测（AUROC 0.991）又给出失效原因归因。**</p>

+ **Look Only Where You Plan for Real-Time End-to-End Urban Driving**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10264)
![architecture](https://img.shields.io/badge/LOWP_Query_Planner-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/University_of_Georgia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LOWP 用两组各 16 个可学习查询按标定直接采样相机特征，取代密集 BEV 构建，nuScenes 平均 L2 从 0.302 m 仅变到 0.296 m 却省下一半参数、提速 1.7 倍，Bench2Drive 闭环 218 条路线取得 65.51 分。**</p>

+ **Who Taught the Robot That? Removing One User's Corrections from a Robot Policy That Learns Online**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10280)
![architecture](https://img.shields.io/badge/Ordered_Unlearning_Replay-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Urbana-Champaign-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在两个仿真任务上精确算出「某用户从未出现」的机器人作为遗忘目标，发现接管式纠错只要保留有序更新日志并按原序重训即可近似复现，而轻推式纠错下测试过的方法都恢复不了，且日志只能识别明显有害者、无法可靠排序影响力。**</p>

+ **SituRecBench: Evaluating Frontier Models as Situated Recommendation Assistants in 3D Environments**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10349)
![architecture](https://img.shields.io/badge/SituRecBench_Protocol-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_Polytechnic_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://siturec.github.io/SituRecBench/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SituRecBench 在 UE5 搭的超市与家居店 3D 场景中，让七个前沿 VLM 与用户共享第一人称视角做多轮购物推荐，用成功率、对话质量、推荐效用与导航有效性四个维度统一评测，并暴露模型在空间定位与偏好澄清上的短板。**</p>

+ **Deploying Physically and Epistemically Compliant Agents by Distilling Belief-Space Task and Motion Planners**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10430)
![architecture](https://img.shields.io/badge/Belief_Space_Planner_Distillation-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/MIT_CSAIL-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文把信念空间任务与运动规划器离线规划的轨迹蒸馏成只看原始观测的策略，并提出 Dual Averaging 损失与 ρ-最优强化两项改进，在 Scavenger 上成功率 94%，而给足 24 小时算力与稠密奖励的 RL 基线最高只有 5%。**</p>

+ **EmbodiedIntentBench: Benchmarking Intent-Driven Runtime Adaptation for Mobile Robotic Missions**
[![paper](https://img.shields.io/badge/Arxiv_2611.10-blue)](https://arxiv.org/abs/2611.10498)
![architecture](https://img.shields.io/badge/Intent_Contract_Runtime-red)
![task](https://img.shields.io/badge/Long_Horizon_Task-magenta)
![organization](https://img.shields.io/badge/University_of_California_Irvine-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/rajatbh21/EmbodiedIntentBench-artifact)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EmbodiedIntentBench 用结构化任务契约表达覆盖、时序证据、上报、紧迫度与资源约束，在因果且计入资源消耗的执行下评测无人机运行时自适应，并指出全库召回 0.875 的感知配置只完成 1/16 任务而召回 0.807 的配置完成 14/16。**</p>

