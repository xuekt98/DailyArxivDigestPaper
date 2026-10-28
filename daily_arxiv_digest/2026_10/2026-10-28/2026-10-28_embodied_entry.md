# 2026-10-28 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **CARD: Contact-Anchored Retargeting for Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36539)
![architecture](https://img.shields.io/badge/CARD_Hand_Contact_Retargeting-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://card-retargeting.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把接触力当作一等公民的重定向框架 CARD：用统一的「手-接触」表征把单目视频（经 Vid-HACO 视频到接触模型）、触觉手套与动捕统一成带逐区域接触力目标的 MANO 网格序列，并证明触觉追踪器对硬件回放复现演示力不可或缺。**</p>
+ **GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37091)
![architecture](https://img.shields.io/badge/GAWM_DINOv3_Latent_World_Model-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Genisom_AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/gaoxiang12/ga-wm)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GAWM 用冻结 DINOv3 潜空间做紧凑多任务世界动作模型：每视角特征压成少量 token，轻量预测器以任务码为条件在两个未来跨度上预测并以未来帧密集 patch 特征为监督，动作解码器再回归动作段；不足 1 亿参数即在 RoboTwin 2.0 上超过十亿参数 WAM。**</p>
+ **Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37330)
![architecture](https://img.shields.io/badge/M_PACT_Primitive_Motion_Factorization-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Purdue_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**M-PACT 在原语运动层把可迁移的交互结构与场景、本体相关的具体实现因子化，从人类视频学习局部原语运动，再分离可复用运动结构、任务上下文与机器人控制，显著减少昂贵机器人演示需求并提升跨任务与跨场景泛化。**</p>
+ **World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37518)
![architecture](https://img.shields.io/badge/World_Dreamer_V5_Lite_Multi_Robot-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/World_Agents-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多机器人世界动作模型 World Dreamer v5-lite：预训练视频编码器的校准特征以工作空间坐标构建共享世界状态，视觉语言模型给出场景上下文与每机器人一个 query，掩码视角协同训练促使模型利用跨机器人共享观测；RoboFactory 平均成功率 74.0%（+23.7），真实机器人任务 78.8%（+13.8）。**</p>
+ **Rollback: Experience Backtracking in World Models for Policy Improvement**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36068)
![architecture](https://img.shields.io/badge/Rollback_Experience_Backtracking-red)
![task](https://img.shields.io/badge/Model_Based_RL-magenta)
![organization](https://img.shields.io/badge/AgiBot-green)
[![project](https://img.shields.io/badge/project-blue)](https://rollback-wm.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把世界模型从被动模拟器变成反事实引擎：Rollback 回滚到关键决策点、分叉替代动作并对比结果以归因成功，统一分布式世界模型搜索与异步真实机器人执行形成自强化循环，三个真实任务上绝对成功率提升 10.67%/11.11%/11.85%，并在 8 小时内超过人类玩家平均水平。**</p>
+ **Keeping Contact: Task-Adaptive Friction Margins for Bimanual Non-Prehensile Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36961)
![architecture](https://img.shields.io/badge/Task_Adaptive_Friction_Margins_SOCP-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对非抓取操作中「可行不等于稳」的问题，用带符号摩擦距离在力空间度量裕度，并从平衡倾转枢轴力矩偏差所需的力修正导出任务自适应裕度，再把裕度嵌入一系列二阶锥规划，在每个倾转角上给出全局最优接触力解。**</p>
+ **A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36789)
![architecture](https://img.shields.io/badge/Torch_Hand_Linkage_Actuation-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Torch-Hand：完全铰接的 21 自由度人形灵巧手，复刻人手关节结构与动作层级（拇指五自由度、其余每指四自由度），用紧凑的全连杆驱动拟人架构规避灵巧-精度-负载三角难题，并给出解耦机械架构与四指/拇指模块设计。**</p>
+ **PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37381)
![architecture](https://img.shields.io/badge/PDRVLA_Physical_Dynamics_Module-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PDRVLA 用轻量物理动力学模块从视觉语言特征抽取物理 token 条件化动作，不做在线视频生成；模块直接预测未来 RGB、深度与光流并接受冻结视频世界模型的辅助监督，在 LIBERO/LIBERO-Plus/RoboTwin2.0/SimplerEnv 上达 99.3%/89.9%/93.6%/81.5%。**</p>
+ **ActiveAlign: Aligning Egocentric Manipulation via Active Perception**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.36859)
![architecture](https://img.shields.io/badge/ActiveAlign_Waving_Touching-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用主动感知弥合 Real2Sim2Real 差距：ActiveAlign-Waving 用主动手部运动加可微渲染完成手眼标定，ActiveAlign-Touching 用触觉反馈把物体对齐精修到毫米级，形成离线重建加在线反馈的闭环，并在真实 Unitree G1 上完成按按钮、推滑块等毫米级精细操作。**</p>
+ **MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37175)
![architecture](https://img.shields.io/badge/MLE_World_World_Model_TTS-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Washington-green)
[![project](https://img.shields.io/badge/project-blue)](https://mle-world.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MLE-World 从 Qwen3.5-4B 微调出可预测程序终端输出并自带置信度的世界模型，让一次预测替代一次真实训练成为可能；据此构建顺序修订、Best-of-N、成对评判、融合与 UCB 五种测试时扩展策略，在 17 个 MLE-bench Lite 任务上匹配真实输出 77.9%（提示模型仅 41.1%）。**</p>