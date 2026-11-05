# 2026-11-05 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Time-to-Goal: Learned Temporal Metrics for Long-Horizon Planning with JEPA World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05847)
![architecture](https://img.shields.io/badge/Time_to_Goal-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Electronic_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为 JEPA 世界模型补上时间序：只用 0.18M 参数的度量网络替换欧氏目标代价，四个导航与操作基准的平均规划成功率从扁平 LeWM 的 32.7% 升到 63.0%，追平甚至超过层级式 H-JEPA 基线。**</p>
+ **Ctrl-F: Force as an Interface for Humanoid Loco-Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05507)
![architecture](https://img.shields.io/badge/Ctrl_F-red)
![task](https://img.shields.io/badge/Force_Control-magenta)
![organization](https://img.shields.io/badge/University_of_California_Berkeley-green)
[![project](https://img.shields.io/badge/project-blue)](https://forcectrl.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把三维力作为人形机器人运动与物体交互的命令通道：统一运动-力控制器跟踪参考动作并施加力，高层规划器按物体状态在线改力；真机推箱与踢球可搬运 20 公斤箱体，力盲基线全部失败。**</p>
+ **Robocasa-Mem: Benchmarking Environment and Process Memory in Long-Horizon Mobile Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06475)
![architecture](https://img.shields.io/badge/RoboCasa_Mem-red)
![task](https://img.shields.io/badge/Memory_Benchmark-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**长程移动操作记忆基准，含九个任务、五类记忆与 1,800 条成功演示，并用行为条件评测从机器人自身历史推出后续约束；HMAP 基线把 π0.5 的平均成功率从 16.2% 提到 24.2%，真机 10 次试验完成 8 次。**</p>
+ **Open-HumanScale: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06817)
![architecture](https://img.shields.io/badge/Open_HumanScale-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://dagroup-pku.github.io/open-humanscale/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**首个把第一人称人类视频预训练扩到 5 万小时的完全开放配方：HumanWAM-Vanilla 后训练在 RoboTwin 2.0 Clean2Random 达 68.88%，混合人类与机器人数据的 HumanWAM-Goal 进一步推到 84.60%，并实现零样本跨域泛化。**</p>
+ **Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05979)
![architecture](https://img.shields.io/badge/HOI_Motion_Predictor-red)
![task](https://img.shields.io/badge/Motion_Priors-magenta)
![organization](https://img.shields.io/badge/State_Key_Lab_of_CAD&CG_Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**不做动作模仿，而是从人类与物体交互数据自回归预测未来手-物状态并当作通用奖励项；YCB 抓取仿真平均成功率 0.84、真机 0.77，优于最好基线 HOP 的 0.59 与 0.48，且能跨手型部署。**</p>
+ **$A^3$-VLA: Automatic Perception-Guided Attention Alignment for Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06447)
![architecture](https://img.shields.io/badge/A3_VLA-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_and_Technology_University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从交互引起的视觉变化自动生成目标物体与机器人的候选区域，离线用分割模型精修后，以注意力分配损失与对比损失对齐视觉表征；多个 VLA 骨干在基准上平均成功率提升 6.5% 到 25.2%。**</p>
+ **Playing Soccer Like Humans Do: Learning Versatile and Agile Humanoid Soccer via Latent Motion Priors**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06564)
![architecture](https://img.shields.io/badge/SoccerBot-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://soccerbot-humanoid.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从人类足球动捕蒸馏出约 2.5 小时结构化潜在运动先验，单一技能条件策略统一完成移动、盘带、停球与射门；仿真踢球成功率 97.04%、盘带 89.88%，零样本迁移到 Unitree G1 后移动速度误差仅从 19.14% 升到 21.53%。**</p>
+ **DreamX: Video Diffusion Model is a Universal Latent Action Learner**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05377)
![architecture](https://img.shields.io/badge/DreamX-red)
![task](https://img.shields.io/badge/Latent_Action-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![project](https://img.shields.io/badge/project-blue)](https://cvlab-kaist.github.io/DreamX/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把预训练视频扩散模型改造成通用潜在动作学习器，每帧潜在动作从 1,200 压到 4 个 token；LARYBench 上动作回归归一化 MSE 平均 0.17、动作分类准确率 69.67%，优于 DiLA 的 0.38 与 62.25%。**</p>
+ **ReactWorld: Structuring Interaction Responses for Embodied Video Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06120)
![architecture](https://img.shields.io/badge/ReactWorld-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/Huawei_Technologies_Co._Ltd.-green)
[![project](https://img.shields.io/badge/project-blue)](https://metaengine-world.github.io/ReactWorld/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在生成骨干的特征空间显式预测交互响应场，描述参与者角色、局部运动强度与时间区间，再把预测位移转成注意力位置偏置；RBench 平均 77.51、比 PhysisForcing 高 3.29 分，EZS-Bench 平均 81.87。**</p>
+ **Beyond Infraction Scores: Failure-Boundary Profiles for Closed-Loop Evaluation of Driving and Robot Navigation Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.06-blue)](https://arxiv.org/abs/2611.06453)
![architecture](https://img.shields.io/badge/Failure_Boundary_Profiles-red)
![task](https://img.shields.io/badge/Closed_Loop_Evaluation-magenta)
![organization](https://img.shields.io/badge/Social_Chaos_Lab-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/speedym/failure-boundary-profiles)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用失败边界剖面替代单一违规分数：每个场景族只变一个可测因素并标注该通过还是该停，估计承诺度与胜任度两条曲线；规则专家决策准确率 0.74，分数最高的学习智能体 TFv6 只有 0.60。**</p>
