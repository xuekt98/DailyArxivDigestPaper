# 2026-11-03 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **ForceLDM: A Force-aware Latent Dynamics Model for Contact-Rich Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03294)
![architecture](https://img.shields.io/badge/ForceLDM_Future_Dynamics_Distillation-red)
![task](https://img.shields.io/badge/Robotic_Latent_World_Model-magenta)
![organization](https://img.shields.io/badge/Xian_Jiaotong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://tpy001.github.io/ForceLDM/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ForceLDM 用特权教师看未来力矩与光流、把未来接触动力学蒸馏进只看当前观测的学生策略，在五个真机接触丰富任务上平均成功率 87.1%、比最强基线高 14.9 个百分点，USB 插入达 92.0%，且部署时不需要教师与未来输入。**</p>
+ **DexArena: A Unified Benchmark for Long-Horizon Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02629)
![architecture](https://img.shields.io/badge/DexArena_Long_Horizon_Dexterous_Benchmark-red)
![task](https://img.shields.io/badge/Dexterous_Manipulation_Benchmark-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DexArena 提供 10 个长程双手灵巧任务与 30 个阶段级任务及 3000 条、9.1 小时可重放的遥操作演示，六个基线在阶段级平均成功率上从 PPO 27.9% 到 GR00T 61.4% 不等，多个插入与装配任务被多家方法打成 0%。**</p>
+ **Visuo-tactile Diffusion Policy for Robotic Manipulation with Auxiliary Tactile Dynamics Prediction**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02677)
![architecture](https://img.shields.io/badge/Visuotactile_Diffusion_Policy_Tactile_Dynamics-red)
![task](https://img.shields.io/badge/Visu_Tactile_Policy-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该扩散策略融合双视角视觉与双指尖触觉的四步历史，并用仅在训练期生效的辅助目标预测两步后的指尖图像变化，MuJoCo 装配实验三个种子下平均成功率从视觉-only 的 42.7% 提升到 59.0%，推理时无额外开销。**</p>
+ **ReContact: Reconstruct and Retarget Human Contacts from Video for Contact-Rich Humanoid Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02968)
![architecture](https://img.shields.io/badge/ReContact_Object_Centric_Contact_Plan_Retargeting-red)
![task](https://img.shields.io/badge/Contact_Rich_Manipulation-magenta)
![organization](https://img.shields.io/badge/Tohoku_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://recontact-robot.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ReContact 用物体中心的接触计划（阶段、接触对、锚点、施力方向、粘滑模式）从人体视频重建并重定向接触，仿真大腿托举再抓取任务上把计划的双手底部托住做到 83.5% ± 5.2%，最好基线仅 0.16%，并在 Unitree G1 上跑通 9 个任务。**</p>
+ **FineCraft: Enhancing VLA Models for Fine-Grained Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03163)
![architecture](https://img.shields.io/badge/FineCraft_Task_Routed_Policy_Mixture-red)
![task](https://img.shields.io/badge/Vision_Language_Action_Model-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology_Shenzhen-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/eqcy/FineCraft)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FineCraft 把 DINOv2-DiT 与预训练 pi0.5 组织成按任务路由、独立适配并在执行中重规划的策略混合，在 MetaFine 挑战赛五个任务上总分 0.878 排第四，并全面超过均值 0.430 的官方 pi0 参考，领先 44.8 个百分点。**</p>
+ **History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02782)
![architecture](https://img.shields.io/badge/History_Forcing_On_Policy_Video_Distillation-red)
![task](https://img.shields.io/badge/Video_World_Model-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://ziplab.github.io/History-Forcing-Project-Page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**History Forcing 用有无历史上下文的教师预测残差解耦并强化历史监督，在 1.3B 模型上取得 15 秒生成 VBench 85.07、60 秒 VBench-Long 79.82，离开视野再回来时 Evolution Quality 由 2.35 升至 2.70。**</p>
+ **Beyond Policy Patches: Distilling RL Specialists into Vision-Language-Action Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02777)
![architecture](https://img.shields.io/badge/REPAIR_Value_Guided_VLA_Distillation-red)
![task](https://img.shields.io/badge/VLA_Policy_Optimization-magenta)
![organization](https://img.shields.io/badge/University_of_Chinese_Academy_of_Sciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://repair-vla.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**REPAIR 用 RL 专家的 critic 给多候选动作加权构造监督分布，先离线初始化再在线精修，把专家能力蒸进单个流匹配 VLA 并在部署时移除专家与切换逻辑，六个真机任务各 30 次评测全部 100% 成功且末端 jerk 更低。**</p>
+ **Right Ranking, Wrong Scale: Reproducing the Robotic World Model's Dynamics Model and Testing the Uncertainty of Its Follow-up**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02699)
![architecture](https://img.shields.io/badge/RWM_Dynamics_Replication_Uncertainty_Audit-red)
![task](https://img.shields.io/badge/Robotic_Manipulation_World_Model-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该复现研究检验 RWM-U 的集成不确定性：分歧对 rollout 误差的排序能力不错（100 步 Spearman ρ=0.90），但发布 checkpoint 的 1σ 覆盖率仅 4.6%，远低于标定高斯的 68%，并指出样本预测的平方误差损失会把成员方差推向零。**</p>
+ **Control Foundation Models across Changing Block Diagrams: Generalizing Time-Series Prediction to Dynamic Graphs**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02900)
![architecture](https://img.shields.io/badge/Block_Diagram_Transformer_Control_Foundation_Model-red)
![task](https://img.shields.io/badge/World_Model_Control-magenta)
![organization](https://img.shields.io/badge/RIKEN-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文把控制实验的框图连接结构与信号值统一表示为动态图，Block Diagram Transformer 在继承时间序列基础模型权重的同时按连接做通道注意力，在不稳定线性系统上把输入预测 RMSE 从微调 Chronos-2 的 1.68 降到 0.78，并成功稳定被控对象。**</p>
+ **GoalDex: Learning Image-Goal-Conditioned Policies for Dexterous In-Hand Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.02-blue)](https://arxiv.org/abs/2611.02171)
![architecture](https://img.shields.io/badge/GoalDex_Image_Goal_Conditioned_Dexterous_Policy-red)
![task](https://img.shields.io/badge/Dexterous_Manipulation-magenta)
![organization](https://img.shields.io/badge/ETH_Zurich-green)
[![project](https://img.shields.io/badge/project-blue)](https://rffr.leggedrobotics.com/works/goaldex/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GoalDex 用单目 RGB、本体感知与目标图像直接输出关节动作，不做位姿估计，靠特权状态蒸馏与辅助重建联合学习表示，在 5 个真实物体、100 次硬件试验上成功率 80%，最强位姿基线仅 27%，并支持自然语言选目标图。**</p>
