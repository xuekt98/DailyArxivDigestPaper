# 2026-10-30 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **PRIME W0: Physical Priors from World Models for Embodied Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39528)
![architecture](https://img.shields.io/badge/PRIME_W0_Hierarchical_Flow_Matching-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Lumos_SZ_Lab_Team-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PRIME W0 把预训练 VLM 的逐层 KV 注入 Adaptive MoE 动作专家，用异步 world model 子目标图像与 DINOv2 历史帧语义桥做动力学条件，再用带协方差结构噪声的 Action Dynamic Manifold 流匹配贴合运动学耦合，在 LIBERO 与真机基准取得 SOTA。**</p>
+ **TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40349)
![architecture](https://img.shields.io/badge/TouchBridge_Tac_Retarget-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TouchBridge 用可穿戴人类接口与机器人接口建立跨 embodiment 的视觉与指尖触觉对应，Tac-Retarget 依据实测接触对齐指尖接触区域，无需物体网格、位姿估计或物理仿真即可把人类演示转成机器人域数据，微调 VLA 后四个真机接触任务平均成功率 72.5%。**</p>
+ **AcrossDEX 1.0: From Human Motion Pretraining to Bimanual Dexterous Manipulation across Hand Embodiments**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40210)
![architecture](https://img.shields.io/badge/AcrossDEX_Human_Motion_Pretraining-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Unknown-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AcrossDEX 1.0 打通人类动作预训练、仿真专家学习、机器人演示采集与视觉闭环执行，在 HOT3D Aria 上预训练后保留视觉编码器与腕部参数，共享腕部表示配合分离手指场同时支持 Inspire 与 Allegro 两种手，并以前缀执行加观测重规划提升连续性。**</p>
+ **CAPTURER: A Dexterous Aerial Manipulator for Dynamic and Precise Grasping across Diverse Environments**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39119)
![architecture](https://img.shields.io/badge/CAPTURER_Aerial_Manipulator-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CAPTURER 是面向厘米级抓取的空中灵巧机械臂，用机载感知做状态估计与目标检测，靠漂移修正和全局位姿变换稳定定位，并以协同运动规划协调平台机动与机械臂灵巧、用抗扰控制器应对动态耦合与外部扰动，在 1.5 m/s 以上飞行速度下抓取直径 1.5 cm 的马克笔。**</p>
+ **From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39543)
![architecture](https://img.shields.io/badge/CoRAct_Consequence_Grounded_Alignment-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://onlyxingxingzyx.github.io/CoRAct/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CoRAct 把 VLA 的 ECoT 推理拆成 movement 与 waypoints 可验证成分，用 Mixture-of-Transformers 联合建模推理、动作与未来预测，以对齐奖励在动作噪声空间做 group-relative 优化，在 RoboCasa、VLABench 与真机上提升成功率与推理-执行一致性。**</p>
+ **OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39287)
![architecture](https://img.shields.io/badge/OpenFlyV2_Onboard_VLA-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Artificial_Intelligence_Laboratory-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Ideal-ljl/AeroBrain)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**OpenFlyV2 用共享视觉语言表示把语义理解、语言锚定感知、空间推理与连续空中控制统一进单个机载 VLA，紧凑动作专家输出 12 个航点的短时域 chunk，在 Jetson Orin NX 上全机载 10 Hz 运行，并从仿真零样本迁移到真实四旋翼取得 48% 成功率。**</p>
+ **Tactus: Tactile & Pose Sensing Glove for Natural Dexterity Data Collection**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39076)
![architecture](https://img.shields.io/badge/Tactus_Tactile_Pose_Glove-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Meta_Reality_Labs_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Tactus 是织物集成的触觉与姿态传感手套，用 1.5 mm 指尖叠层的 3D 针织形态、电容式触觉传感器与 IMU 融合追踪三支柱采集自然操作演示，最小可检测力 0.59 N、跨被试一致性 0.87，并给出首个触觉手套跨平台定量基准协议。**</p>
+ **Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39232)
![architecture](https://img.shields.io/badge/GenSight_Unified_Video_Diffusion-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/RoboScience-green)
[![project](https://img.shields.io/badge/project-blue)](https://gensight-rbs.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GenSight 把未来视频生成与稠密感知统一进同一个预训练视频扩散 transformer，用统一时空表示承载视频、深度、embodiment 分割与首帧相对光流，共享 DiT 骨干在统一 velocity prediction 空间联合优化，支持多步生成与单步稠密感知两种模式。**</p>
+ **Improving Fine-Grained Manipulation through Demonstration Expansion and Execution Design**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.40430)
![architecture](https://img.shields.io/badge/DEED_Demonstration_Expansion-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DEED 通过结构化的演示扩展与执行设计把预训练 VLA 策略适配到五个 MetaFine 任务，从同一初始场景生成不同指令的演示并渲染多相机位置与光照，部署时用逆运动学、逐任务夹爪映射与闭环重规划落地动作 chunk，取得官方 Overall 85.55%。**</p>
+ **Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.39044)
![architecture](https://img.shields.io/badge/CatchItAll_Sim_to_Real_Catching-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/UC_San_Diego-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Catch It All! 是面向人形机器人的 sim-to-real 接球框架，只用一个 egocentric 相机，靠细致设计的抓取奖励实时适应物体位姿与形状，并用安全感知课程在低至 5 Nm 的手腕力矩上限下高频执行，零样本部署到 Unitree G1 成功接住 9 种未见物体。**</p>
