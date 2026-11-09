# 2026-11-06 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **La-JEPA: Compact Robot Policies with Latent World Modeling**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08156)
![architecture](https://img.shields.io/badge/La_JEPA-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/Huawei_Technologies_Ltd.-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/mt-clemente/lajepa)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**La-JEPA 把策略 transformer 直接建在预训练 V-JEPA 2.1 特征空间里从零训练，训练时联合预测未来特征与动作、推理时只产出动作，在 LIBERO-Plus 修正指令下达到 88.0%，部署参数约为同场竞品的四分之一。**</p>
+ **Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08577)
![architecture](https://img.shields.io/badge/Meituan_Robotics_0-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Meituan_Robotics-green)
[![project](https://img.shields.io/badge/project-blue)](https://meituan-robotics.github.io/Meituan-Robotics-0/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**美团机器人团队发布 MR0 桌面操作 VLA 基础模型，用 1.47 亿视觉语言样本与 15060 小时跨 12 种本体的轨迹做三阶段训练，并提出 Rollback 把被替换的策略片段与人工纠正配对来支撑 CFG-DAgger，RoboTwin 2.0 成功率 93.6%。**</p>
+ **Spatial-UMI-Dream: Scaling World Action Models with Metric Geometry for UMI Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07229)
![architecture](https://img.shields.io/badge/Spatial_UMI_Dream-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/USC_Physical_Superintelligence_Lab-green)
[![project](https://img.shields.io/badge/project-blue)](https://weiduoyuan.com/spatial-umi-dream/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Spatial-UMI-Dream 是 5B 规模的空间世界动作模型，用 605 小时 RGB-D 的 UMI 数据两阶段预训练，联合预测未来 RGB、鱼眼对齐公制深度与动作；配套二十任务 RoboTwin-UMI 基准，真实六任务平均成功率 85.0%。**</p>
+ **Learning Robotic World Models with Semantic and Visual Feedback**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07850)
![architecture](https://img.shields.io/badge/RoboImagine-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/The_City_College_of_New_York-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Alexander-wu/RoboImagine)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboImagine 用多样化候选未来搜索加上冻结多模态评判器的语义偏好与像素、感知一致性反馈，对自回归机器人世界模型做后训练，把语义对比信号转成组相对优势，RT-1 上 PSNR 提升 1.26 dB、LPIPS 下降 11.93%。**</p>
+ **TactileLab: Sim-to-Real Dexterous Robot Manipulation with Efficient Shear-Sensitive Tactile Simulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07881)
![architecture](https://img.shields.io/badge/TactileLab-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Beijing_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TactileLab 基于 IsaacLab 构建 GPU 并行的多模态触觉仿真，用刚体求解而非软体物理估计接触界面的稠密切向运动，得到 simulated tactile flow，并配套 PETS-Net 融合长时序本体感知与触觉观测，支持真实触觉流到仿真流场的迁移。**</p>
+ **MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08372)
![architecture](https://img.shields.io/badge/MOMASPLAT-red)
![task](https://img.shields.io/badge/Mobile_Manipulation-magenta)
![organization](https://img.shields.io/badge/The_University_of_Texas_at_Austin-green)
[![project](https://img.shields.io/badge/project-blue)](https://robin-lab.cs.utexas.edu/momasplat)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MOMASPLAT 用 3D 高斯泼溅与前馈三维基础模型分别重建静态场景和被操作物体，再做运动学动作重定向，从未见机器人底座位姿合成完整操作轨迹，在五个真实移动操作任务上把成功率提升到最强基线的两倍以上。**</p>
+ **Latent RL Priors for Data-Efficient Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08458)
![architecture](https://img.shields.io/badge/Latent_RL_Prior-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/University_of_California_Berkeley-green)
[![project](https://img.shields.io/badge/project-blue)](https://yixiaowang7.github.io/latent-rl-prior-page/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Latent RL Prior 先在特权状态下用大规模 RL 轨迹蒸馏出以流匹配动作解码器形式存在的控制先验，再冻结解码器只用动作监督学习视觉接口到隐任务上下文的映射，50 条示范即可超过用 500 条数据的 VLA 基线。**</p>
+ **PhySA: Decoupling Aesthetic and Physical Rewards for Humanoid Locomotion**
[![paper](https://img.shields.io/badge/Arxiv_2611.07-blue)](https://arxiv.org/abs/2611.07679)
![architecture](https://img.shields.io/badge/PhySA-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PhySA 指出美学偏好与物理平滑方向相反：四个商用 VLM 上关节加速度越高美学分越高（Pearson r=+0.66）。方法把稀疏异步 VLM 打分与相位触发的物理修正拆成两条独立可移除的奖励通道，在 MuJoCo Humanoid-v5 上把关节加速度降低 26% 到 32%。**</p>
+ **GPWM: Modeling the World as 3D Particle Motion**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08338)
![architecture](https://img.shields.io/badge/GPWM-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://robertren1122.github.io/gpwm/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GPWM 把三维场景表示为粒子与刚体的运动，用流匹配加扩散强制训练多分辨率 Transformer 生成物理轨迹，在 2550 万帧 ParticleWorlds 的六个物理域上把预测误差平均降低 31%，并支持在隐噪声空间直接规划接触操作。**</p>
+ **RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines**
[![paper](https://img.shields.io/badge/Arxiv_2611.08-blue)](https://arxiv.org/abs/2611.08308)
![architecture](https://img.shields.io/badge/RM_VLM-red)
![task](https://img.shields.io/badge/Reward_Model_Embodied-magenta)
![organization](https://img.shields.io/badge/Imperial_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RM-VLM 让大模型从自然语言任务描述编译出自动机形式的奖励机，再让视觉语言模型充当标注函数在图像观测上落地原子命题，并用 VLM 价值估计器给出稠密奖励，在网格导航、机器人操作与三维收集三个域上全面超过已有 VLM 奖励方法。**</p>
