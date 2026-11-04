# 2026-11-04 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **TAMPAgent: Agentic Belief-Space Planning for Mobile Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03584)
![architecture](https://img.shields.io/badge/Belief_Space_Agentic_TAMP-red)
![task](https://img.shields.io/badge/Robot_Manipulation_Planning-magenta)
![organization](https://img.shields.io/badge/NVIDIA_Research-green)
[![project](https://img.shields.io/badge/project-blue)](https://umishra.me/TAMPAgent/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**英伟达等提出 TAMPAgent，用 LVLM 写参数化部分任务计划再由 TAMP 编译器绑定合法参数，MuJoCo 仿真的 RBY1 厨房任务达 77.2% 成功率，CaP 57.2%、GaP 61.1%，真机仅给出定性演示。**</p>
+ **Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.03-blue)](https://arxiv.org/abs/2611.03648)
![architecture](https://img.shields.io/badge/Co_Designed_Wheeled_Humanoid_Stack-red)
![task](https://img.shields.io/badge/Mobile_Manipulation-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://pixel-robot.com/pixel)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CMU 的 Pixel 把硬件、采集接口与学习栈协同设计，整车低于 1.5 万美元、人形比例 17 自由度上半身，用传感器化人体演示训出的策略在三个移动操作任务上达 82.0% 平均任务进度。**</p>
+ **ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04424)
![architecture](https://img.shields.io/badge/Instantaneous_Tactile_Reflex_Integration-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://minusmodulo.github.io/reflexarc-website/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**清华等提出 ARC 自底向上把瞬时触觉反射接入 50Hz 全身控制，反射 10ms 内送达电机，Unitree G1 上首次力峰值降 34.1%、接触冲量由 0.2632 降至 0.1225 N·s。**</p>
+ **Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04839)
![architecture](https://img.shields.io/badge/Action_Conditioned_Latent_World_Action_Model-red)
![task](https://img.shields.io/badge/Humanoid_Loco_Manipulation-magenta)
![organization](https://img.shields.io/badge/University_of_Hamburg_Hamburg_Germany-green)
[![project](https://img.shields.io/badge/project-blue)](https://ju6276.github.io/Action-Grounded-Foresight/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**汉堡大学等用动作条件化潜在前瞻让世界-动作模型在执行前给命令序列打分，SIMPLE 仿真 10 任务 89.7%、7 个真机任务 85.7%，未见物体配置下降至 65.7%，而 GR00T N1.7 为 70.0%/48.6%。**</p>
+ **FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04080)
![architecture](https://img.shields.io/badge/Task_Driven_Grounding_Agent-red)
![task](https://img.shields.io/badge/Mobile_Manipulation-magenta)
![organization](https://img.shields.io/badge/MIT_CSAIL-green)
[![project](https://img.shields.io/badge/project-blue)](https://williamshen-nz.github.io/feijoa/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MIT CSAIL 的 FEIJOA 把 grounding 移到测试时刻反复查询与精化，103 条开放式查询精确解析率 94.2%（预构建表征 68.0%），Spot 真机 50 次试验完成 35 个任务，且失败多归因于物理技能而非推理。**</p>
+ **Spectrally Routed Diffusion Policy for Multi-Task Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04477)
![architecture](https://img.shields.io/badge/Spectrally_Routed_Diffusion_Policy-red)
![task](https://img.shields.io/badge/Diffusion_Policy-magenta)
![organization](https://img.shields.io/badge/School_of_Automation_Beijing_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**清华等提出 SR-DP，把去噪器线性层做 SVD 分解为正交 rank-1 专家并用谱路由适配，6 个 RoboTwin 任务平均成功率 68.4%，超多任务 VO-DP 21.8 点，真实双臂任务 Stage 2 达 43.0%。**</p>
+ **Future Representation Distillation for Imagination-Free World Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04527)
![architecture](https://img.shields.io/badge/Representation_Distilled_Predictive_Encoder-red)
![task](https://img.shields.io/badge/Video_World_Model-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![project](https://img.shields.io/badge/project-blue)](https://harryjo97.github.io/dreamfree/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**KAIST 提出 DreamFree，用表征蒸馏把视频扩散骨干变为预测性视觉编码器，14B 下 11Hz 实时闭环提速 17.8 倍，RoboCasa-Kitchen 成功率 71.7%、真机 10 类任务 64%，优于 DreamZero 与 π0.5。**</p>
+ **DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05119)
![architecture](https://img.shields.io/badge/Hand_Object_Configuration_Transfer-red)
![task](https://img.shields.io/badge/Dexterous_Manipulation-magenta)
![organization](https://img.shields.io/badge/CFCS_School_of_CS_Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://dex-hot.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**北大提出 DexHOT，把灵巧操作表述为手-物配置迁移并学习可复用的迁移原语，DexHOTBench 120 个物体上已见 80.5%、未见 69.4%，真实灵巧手 200 次迁移 61.5%、6 个任务 90%。**</p>
+ **FloMo: 3D Scene Flow as a World Action Model Intermediate for Learning from Human Video**
[![paper](https://img.shields.io/badge/Arxiv_2611.05-blue)](https://arxiv.org/abs/2611.05062)
![architecture](https://img.shields.io/badge/Scene_Flow_World_Action_Model-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://flomo-wam.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**佐治亚理工提出 FloMo，把 3D 场景流渲染进视频潜空间、用 5B 视频骨干预测运动与动作 token，消融显示附加视频预测目标反而拉低策略成功率，动作 token 关注运动远多于视频。**</p>
+ **PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations**
[![paper](https://img.shields.io/badge/Arxiv_2611.04-blue)](https://arxiv.org/abs/2611.04870)
![architecture](https://img.shields.io/badge/Cross_Embodiment_Multiview_World_Model-red)
![task](https://img.shields.io/badge/Neural_Simulator-magenta)
![organization](https://img.shields.io/badge/PrimeBot_Research-green)
[![project](https://img.shields.io/badge/project-blue)](https://primebottech.github.io/PrimeSim-website)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PrimeBot 等提出 PrimeSim，在 22 个平台、30,110 小时演示上中途训练并后训练为自回归模拟器，10.1 FPS 且长程 rollout 稳定，留出平台 100–200 梯度步即可迁移，领先五个开源世界模型但局部标定仍落后。**</p>
