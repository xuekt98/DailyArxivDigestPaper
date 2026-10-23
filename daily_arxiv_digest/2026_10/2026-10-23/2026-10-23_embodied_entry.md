# 2026-10-23 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30781)
![architecture](https://img.shields.io/badge/DeXplicit-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/S-Lab,_Nanyang_Technological_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://dexplicit.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DeXplicit 先用轻量 3D 动力学网络在度量空间中显式预测物体运动与形变，再把预测作为脚手架驱动视频渲染；移动点误差降低 27–40%，HOT3D 物体保真 IoU+ 提升 47%，两步因果生成较 14B 双向配置快 57 倍。**</p>
+ **In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30988)
![architecture](https://img.shields.io/badge/Soft-Object_World_Model-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Institute_of_Advanced_Engineering,_The_Chinese_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Soft-Object World Model 用 transformer 骨干在变长部分点云历史上做上下文学习，推断潜在形状与材质线索，无需权重更新即可跨机器人本体、材质与衣物类型泛化，并接入目标条件规划器完成双臂衣物折叠。**</p>
+ **Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30438)
![architecture](https://img.shields.io/badge/Tactile_Manipulation_Review-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Siebel_School_of_Computing_and_Data_Science,_University_of_Illinois-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇 Annual Reviews 级别的综述以「力学驱动 vs 数据驱动」为主轴梳理触觉操作研究，涵盖触觉传感基础、接触力学解释状态表征的路径，以及模仿学习、强化学习与 VLA 等数据驱动进展。**</p>
+ **Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31166)
![architecture](https://img.shields.io/badge/WholeBodyMem-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Mohamed_bin_Zayed_University_of_Artificial_Intelligence-green)
[![project](https://img.shields.io/badge/project-blue)](https://memory-before-goal.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WholeBodyMem 用 SAM3 跟踪任务物体并因果性地挑选关键帧，把目标之前的事件历史作为物体引导的感知记忆喂给全身 VLA；仿真成功率从 29.1% 升至 72.6%，Unitree G1 真机从 36.7% 升至 88.3%。**</p>
+ **DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31617)
![architecture](https://img.shields.io/badge/DiffDreamer-red)
![task](https://img.shields.io/badge/Model_Based_RL-magenta)
![organization](https://img.shields.io/badge/[unverified]-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DiffDreamer 把学到的世界模型与可微仿真耦合：世界模型传播捕捉外部动态的隐状态、可微仿真器传播显式物理状态，actor 目标拆为 critic 驱动的不可微任务奖励通路与仿真器驱动的可微运动奖励通路，在四旋翼动态门竞速上优于各类基线。**</p>
+ **Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30540)
![architecture](https://img.shields.io/badge/Spatiotemporal_Retargeting-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/Physical_Intelligence_Lab,_Tongji_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**STR 用视觉语言模型挑选关键运动信号与身体部位，据此给关键帧分配更多求解器迭代并给所选部位更高交互权重，配合力学感知接触锚定精修接触位置，在 Unitree G1/R1 上以更低算力改善接触覆盖与连续性。**</p>
+ **LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30876)
![architecture](https://img.shields.io/badge/LocoManiLab-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LocoManiLab 是人形 loco-manipulation 的一体化试验台：五类家居场景 234 个任务、51.5 小时仿真遥操作数据、共享控制器下评测 12 个策略，并验证仿真与真实世界的策略排序一致。**</p>
+ **PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31299)
![architecture](https://img.shields.io/badge/PiHand-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Max_Planck_Institute_for_Informatics-green)
[![project](https://img.shields.io/badge/project-blue)](https://virtualhumans.mpi-inf.mpg.de/PiHand/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PiHand 先在仿真中训练跟踪 mocap 的专家策略，再蒸馏成目标条件 VAE 的统一手-物交互先验，并在潜空间用有界残差探索解任务：仅用单一奖励、无课程训练，即可泛化到未见物体并迁移到双手交接。**</p>
+ **FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.31427)
![architecture](https://img.shields.io/badge/FastHarness-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/FastHarness/fast-harness)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FastHarness 按经验自适应调度大模型对 π0.5 策略的监督：快路径随经验积累降低审查频率，恢复路径集中纠错；策略保持冻结，审查 token 下降 57.2%，episode 时长从 85.5 降到 52.0 分钟，成功率从 80% 升到 97.19%。**</p>
+ **SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.30732)
![architecture](https://img.shields.io/badge/SmolVLA-MoE-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Huazhong_Agricultural_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/dudu435/smolvla-moe)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SmolVLA-MoE 把稀疏 MoE 引入 VLA 动作专家的 FFN 层，用 token 级路由器选专家、并以可调权重的共享专家平衡预训练能力继承；激活参数约 500M，LIBERO 四套件平均成功率 84.25%，超过 SmolVLA 与 OpenVLA-7B。**</p>
