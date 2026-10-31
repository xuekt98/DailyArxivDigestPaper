# 2026-10-29 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Embodied at Sea: Imitation Learning for Multi-Task Underwater Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38199)
![architecture](https://img.shields.io/badge/DynamicVLA_Underwater_Imitation-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/New_York_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://lair-research-nyu.github.io/Embodied-at-Sea/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DynamicVLA 用平静与湍流水域采集的 1616 条水下操作数据训练 14 个 generalist VLA，池中 1260 次实机 rollout 里最佳模型成功率达 93.3%，而沉船现场的 ACT 策略以 47.9% 远胜通用 SmolVLA 的 7.9%。**</p>
+ **DexSuite: An All-in-One Framework for Dexterous Manipulation Across Arms, Hands, and Tasks**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37799)
![architecture](https://img.shields.io/badge/DexSuite-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Mila-green)
[![project](https://img.shields.io/badge/project-blue)](https://dexsuiteorg.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DexSuite 是基于 Genesis 的灵巧操作一体化仿真框架，提供 30 个任务、10 条手臂与 12 种末端执行器组成的 100 多个单臂机器人和数千个双臂组合，并附 16 组 task-embodiment 基准与 4700 条成功演示数据。**</p>
+ **SaiVLA-JEPA: Evaluating Future Latent Prediction in JEPA-Conditioned VLA Control**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38508)
![architecture](https://img.shields.io/badge/SaiVLA_JEPA-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Synthoid.ai_(VLA_Research_Team),_Shanghai,_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SaiVLA-JEPA 让 diffusion transformer 动作专家读取冻结 V-JEPA 特征，并用训练期辅助头预测未来表征；在 10030 对 LIBERO-Plus episode 上当前 JEPA 条件把成功率从 71.6% 抬到 82.5%，未来监督却无额外增益。**</p>
+ **Recursive Self-Improvement in Physical AI: Mechanisms, Evidence, and Evaluation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38266)
![architecture](https://img.shields.io/badge/Physical_AI_RSI_Rubric-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Institute_of_Automation,_Chinese_Academy_of_Sciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/nkd-lkz/physical-ai-rsi-survey)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇综述从「能力持久性与改进过程」的角度梳理物理 AI 的递归自我改进，区分 learner 与 improver，提出 L0–L3 四级 rubric 判定任务内适应、持久能力增益与流程修订，并给出共享 learner 起点的对照评测协议。**</p>
+ **FORGE: Feasible Online Reduced-Order Reference Generation and Whole-Body Execution for Agile Humanoid Locomotion**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37974)
![architecture](https://img.shields.io/badge/FORGE_ROM_WholeBody_Tracking-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/California_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FORGE 用两阶段框架把降阶模型的在线参考生成与全阶模型的全身体追踪控制耦合起来，在 Unitree G1 上以单一参考策略加单一追踪策略达成 -2.0 到 2.8 m/s 纵向速度、±1.0 m/s 横向速度、±3.0 rad/s 角速度与单腿跳。**</p>
+ **When More Planning Hurts: Learned Planners for World Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37891)
![architecture](https://img.shields.io/badge/Learned_Action_Updater-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇论文记录了一个反直觉的负结果：在 PushT 上给动作更新器增加更新预算到 4、8、12 次，成功数从 9 降到 7，额外更新降低了 latent world-model 轨迹代价，却把原本成功的任务变成失败。**</p>
+ **Proprioceptive Finger Force Estimation for Reliable Box Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38351)
![architecture](https://img.shields.io/badge/FEEL_VirtualSpring_MDN-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Korea_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://finger-force-estimation.pages.dev/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FEEL 用标定的虚拟弹簧加 Mixture Density Network 残差，从本体感知历史估计每指外力且部署无需接触传感器，在 0–20 N 范围取得 0.251 N 的平均 RMSE，并把箱子搬运的无损成功率从 7/10 提升到 10/10。**</p>
+ **Self-Labeled Preference Transfer for Steerable Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38000)
![architecture](https://img.shields.io/badge/SPT_SelfLabeled_Preference-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/UC_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SPT 先联合训练偏好条件动作预测与偏好识别，再冻结识别器给目标演示自标注以免去人工偏好标注，仿真中偏好遵循 84.8%、多偏好 93.8%，真机跨任务迁移从 52.5% 提升到 92.5%。**</p>
+ **An Empirical Study of Wrist-Target Construction and Joint-Angle Limits in Humanoid Arm Retargeting**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37801)
![architecture](https://img.shields.io/badge/Wrist_Target_Construction_Study-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这项实证研究在 Unitree H1-2 上比较重建腕部目标与 reach 归一化目标：前伸扫描 20 次中重建目标 10 次触及关节角边界而归一化目标 0 次，硬件回放的 16 条方向匹配记录中 12 条触限、归一化记录全部未触限。**</p>
+ **ELEVATE: Agentic Controller Acquisition from Task Failure for Quadrupedal Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38388)
![architecture](https://img.shields.io/badge/ELEVATE_Agentic_Controller_Acquisition-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://agentic-quad-elevate.github.io/public/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ELEVATE 用任务程序精炼中的持续失败定位缺失的全身控制能力，由 coding agent 自动构造并精炼带奖励、课程与终止条件的 RL 问题，训得的控制器在零真机训练下迁移到实体四足机器人，抓取货架物品成功 18/20。**</p>
