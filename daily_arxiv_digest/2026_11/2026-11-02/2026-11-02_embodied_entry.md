# 2026-11-02 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40828)
![architecture](https://img.shields.io/badge/Imitation_Learning_Representation_Ablation-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Analog_Devices,_Inc.,_EdgeAI_Robotics-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在五指机械手 RJ45 插入任务上评测 281 个模仿学习策略、约 1700 次真机试验，证明点云裁剪、基座坐标系表征与编码器内归一化等表征选择比优化器与采样设置更能决定成功率，而 67 个离线指标中仅 5 个可用于候选策略筛选。**</p>
+ **A Capability-Aware Backup-Recoverability Filter for Heterogeneous Multi-Robot Navigation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41188)
![architecture](https://img.shields.io/badge/Capability_Aware_Backup_Recoverability_Filter-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Chicago-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为异构多机器人导航提出能力感知的备份可恢复性滤波器：先在共享笛卡尔空间认证各机型专属的备份机动，再在名义安全优化不可行时按交互连通分量插值回退动作，从而在最多 30 台机器人与五类运动学上同时保住递归可行性与零安全违规。**</p>
+ **HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41336)
![architecture](https://img.shields.io/badge/HandMimicX_Object_Centric_RL-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以物体运动而非手部轨迹定义强化学习目标，从单段第一视角人类 RGB-D 视频重建手物交互与几何先验，训练可操纵物体到任意 6-DoF 位姿的灵巧策略，并通过 DAgger 蒸馏到真实机器人，仿真平均成功率达 85.4%。**</p>
+ **$\nabla$Mimic: Ultra-Efficient Humanoid Control with Differentiable Simulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41654)
![architecture](https://img.shields.io/badge/NablaMimic_Differentiable_Simulation-red)
![task](https://img.shields.io/badge/Neural_Simulator-magenta)
![organization](https://img.shields.io/badge/UC_Davis-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对接触丰富的全身控制中精确梯度爆炸的问题，用逐步中值相对梯度裁剪与动作目标多步回归抑制离群样本，并以面向 Unitree G1 的可微 GPU 引擎 NablaEngine 把单步伴随计算融合成一个 megakernel，在 40 段 LAFAN1 动作上把分数 0.82 的达成时间从 1.2 小时压到 20 分钟。**</p>
+ **Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41330)
![architecture](https://img.shields.io/badge/Hourglass_World_Model_Ego_Dynamics-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Hourglass 架构把跨本体运动规划拆成身体无关的世界模型与各机器人带物理参数的微分自运动学，二者只通过相机自运动耦合；一个参数条件化的通用策略在七台五类运动学的仿真机器人上超过模仿学习与扩散基线 3.8–10.6 个百分点，并零样本迁移到真实滑移转向机器人。**</p>
+ **Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42021)
![architecture](https://img.shields.io/badge/Nexus_VLA_Hierarchical_Semantic_Latent-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Xi'an_Jiaotong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Nexus-VLA 用分层跨本体语义对齐把人类第一视角视频与机器人演示放在同一训练回路中，再以共享操作潜表征直接驱动连续动作生成；在 RoboCasa-GR1 上取得 80.5% 任务成功率，并展示更强的人类数据利用率与跨场景泛化。**</p>
+ **Hierarchical World Models with Implicit Dynamics**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42146)
![architecture](https://img.shields.io/badge/ID_WM_Hierarchical_Implicit_Dynamics-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/New_York_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ID-WM 用高层模型在状态流形上采样可行转移、低层世界模型充当逆动力求解器把转移落成精确动作，在 Wall、PushT、Maze 三套导航与操作环境上比最强离线与扩散规划器提升 38.5%，相对单层世界模型 MPC 提升 135%。**</p>
+ **Geometry-Aware Humanoid Retargeting via Manifold ODEs**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41349)
![architecture](https://img.shields.io/badge/TaSP_KKT_Manifold_ODE_Retargeting-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Southern_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 OmniRetarget 逐帧的 KKT 条件写成机器人位形流形上的常微分方程，并由此得到前向离散的 TaSP-KKT：每步只需一次加权切锥投影与闭式流形更新，在 OMOMO 人-物交互动作重定向到 Unitree G1 时比 OmniRetarget 少算 38%–63% 的时间。**</p>
+ **Contact Imitation Interface: Transferring Dexterous Skills by Showing How Contact Unfolds**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41028)
![architecture](https://img.shields.io/badge/CIMI_Contact_Imitation_Interface-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://nus-lins-lab.github.io/CIMIWeb/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CIMI 用共享接触几何与指尖 RGB 视角、接触优先的重定向与重投影构造人机对齐的演示接口，再以接触面规划器加腕指协调的分层策略学习，在 LEAP 与 Wuji 六个手-任务组合上把最终阶段平均成功率相对基线提升至少 50 个百分点。**</p>
+ **VLA Policies Do Not Know When Not to Act: Unintended Task Execution and Start Suppression**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41609)
![architecture](https://img.shields.io/badge/Paired_Protocol_Start_Suppression-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Electronics_and_Telecommunications_Research_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用配对协议在 LIBERO-Goal 上只改变指令来测试六个 VLA 检查点：即使指令为空，六个模型每一轮都会启动动作，其中五个还会完成未被指定的任务；前缀提示在六个模型上都没能抑制启动，门控方案则在五个上生效。**</p>
