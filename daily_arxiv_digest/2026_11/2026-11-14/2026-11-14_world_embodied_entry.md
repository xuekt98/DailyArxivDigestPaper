<!-- direction: world_model -->

+ **Does Your World Model Know Actions Have Consequences?**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15048)
![architecture](https://img.shields.io/badge/Action_Perturbation_Sensitivity-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Northwestern_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文为具身世界模型提出动作扰动灵敏度指标 AP，用 86 个初始状态、8 个扰动方向与 50 条轨迹共 34,400 次扰动量化动力学是否建模了动作后果，发现加噪动力学头状态误差与模仿学习头相当，灵敏度精度却高约 16% 与 48%。**</p>

+ **Prediction or Persistence? What Future-Prediction Scores Miss About World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15082)
![architecture](https://img.shields.io/badge/Persistence_Control_Probe-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/Deccan_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文用 27,000 次未来检索试验（11 选 1，随机基线 0.091）把每个视频世界模型与一个从不调用预测器的持久性对照配对，发现 V-JEPA 2.1 的预测器贡献 +0.291、V-JEPA 2 仅 +0.028~0.041，建议所有未来预测分数都附带持久性基线。**</p>

+ **AFTER: A World Model with Adaptive Fast--Slow Timescales for Error-Driven Retention**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15215)
![architecture](https://img.shields.io/badge/Fast_Slow_Error_Driven_Adaptation-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/Tongji_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AFTER-WM 用预测误差驱动一快一慢两路修正并只调整预训练专家的组合权重，在 6 个数据集（含真实 UAV 数据）上多步平均误差比 10 个对比模型中最强者低 16%–34%，且变化后 1–4 步与第 40 步误差均为最低。**</p>

+ **What World Model Does Active Object Search Need? A Study under Imperfect Detection**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15689)
![architecture](https://img.shields.io/badge/Bayesian_Miss_Aware_Belief-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Superb_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出只预测检测与否的贝叶斯世界模型 BAMOS，在 Isaac Sim 的 345 个回合与 HSSD 的 1,248 个 ObjectNav 回合上消融目标信念与占据信念，发现目标信念贡献最大且随检测错误增多而上升，误报最多让成功率下降 0.402。**</p>

+ **ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16579)
![architecture](https://img.shields.io/badge/Plan_Conditioned_JEPA_Reranking-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://adept-thu.github.io/ActWorld-JEPA/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ActWorld-JEPA 用计划条件潜预测 PC-JEPA 与计划—未来关系残差重排 R³ 把 JEPA 接到候选式驾驶排序上，NAVSIM v1 navtest 达 94.1 PDMS（Drive-JEPA 93.7），v2 navtest/navhard 为 91.6 与 42.7 EPDMS。**</p>

+ **BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14815)
![architecture](https://img.shields.io/badge/Joint_Perspective_BEV_Diffusion-red)
![task](https://img.shields.io/badge/Driving_Simulation-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://research.nvidia.com/labs/sil/projects/birddreams/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BirdDreams 用因果视频扩散 Transformer 联合生成透视视频与固定尺度鸟瞰视频，把场景布局纳入被预测的未来；在 PhysicalAI-AV 与 nuScenes 上无自车条件时 minADE 为 6.15/3.91、minDTW 258/205，优于 OmniDreams 的 7.76/6.20。**</p>

+ **Driving World Models Move the Camera, Not the Scene**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15260)
![architecture](https://img.shields.io/badge/ReTime_Compose_Transport-red)
![task](https://img.shields.io/badge/Video_Prediction-magenta)
![organization](https://img.shields.io/badge/Chongqing_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://joefeng0571.github.io/retime-compose/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文用重定时录像与立体双目构造真实反事实参照，提出场景响应 α 指标：已发布驾驶世界模型的 α 最高仅 0.23（Orbis 2），真实视频为 0.64–0.73，轨迹分还分不出执行与忽略指令；免训练的 ReTime-Compose 可让冻结模型跟随 0.54 m 横移。**</p>

<!-- direction: embodied_ai -->

+ **Embedded Sim-to-Real Visual Servoing: Learned Reaching and Force-Guided Placement**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15658)
![architecture](https://img.shields.io/badge/Force_Guided_Visu_Servoing-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/University_of_Twente-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在 Jetson AGX Orin 上打通感知到控制的整链路：RLBench 中 PPO 策略各 1000 回合成功率 87.2% 与 83.1%，真机 50 次试验完成率 70.0% 与 74.0%，约 2 N 法向接触配螺旋搜索，TensorRT 感知延迟 34.55 ms。**</p>

+ **What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16246)
![architecture](https://img.shields.io/badge/Task_Level_Experience_Distill-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Tsinghua_Shenzhen_International_Graduate_School_Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出 H2E，把调用 VLA 的智能体会话转成训练数据：每个运动在原任务指令下成为 VLA 动作目标，背离目标的步骤屏蔽损失、距目标 1 m 内标停止，再用 LoRA 更新；在 REVERIE-CE 的 3,189 个 val-unseen 回合上 8B VLA 成功率由 35.0% 升至 44.9%。**</p>

+ **VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16423)
![architecture](https://img.shields.io/badge/Pluggable_Kinematics_Pose_Refine-red)
![task](https://img.shields.io/badge/Dexterity-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://voke-project.pages.dev/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VOKE 在现有位姿估计器上插入运动学模块预测物体线角速度与加速度，并用二阶运动先验修正逐帧位姿；DexYCB 上平移 RPE 从 2.50 降到 0.89 cm，整体平移 RPE 降 41.0%–64.4%，下游运动学增强策略成功率 78.90% 对 68.20%。**</p>

+ **FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17142)
![architecture](https://img.shields.io/badge/Multi_Granularity_Force_Aware_Control-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Shanghai_AI_Laboratory-green)
[![project](https://img.shields.io/badge/project-blue)](https://bb0928.github.io/forge/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FORGE 用粗到细的多粒度命令空间做人形 loco-manipulation，训练无需全身人体动作参考，部署只吃双腕位姿与可选载荷；混合力估计三轴 RMSE 为 0.81/1.97/0.87 N，0–2 kg 载荷搬运 20 次试验分别成功 20/20、20/20、18/20、18/20。**</p>

+ **PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15117)
![architecture](https://img.shields.io/badge/Trajectory_Conditioned_Morphology_Routing-red)
![task](https://img.shields.io/badge/Mobile_Manipulation-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PolyMorphWBC 以短时域末端轨迹为唯一任务指令，用轨迹条件协调器决定基座运动、臂专属 IK 跟踪、冻结 locomotion 后端执行，覆盖 4 类 6 自由度安装臂；IsaacLab 完成率 93.95%、位置误差 2.30 cm，MuJoCo 位置误差较 UMI-on-Legs 降 69%–72%。**</p>

+ **What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15491)
![architecture](https://img.shields.io/badge/Prediction_Execution_Horizon_Study-red)
![task](https://img.shields.io/badge/Action_Chunking-magenta)
![organization](https://img.shields.io/badge/Karlsruhe_Institute_of_Technology_KIT-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在两个动态仿真基准与三个真机任务上拆解 VLA 的反应性：最佳预测时域约为 1 秒（DOM 25 步、DOMINO 30 步），最佳执行时域随检查点变化（1k 取 s=5、5k 取 s=15），保持轨迹连续优于单纯降延迟，熵自适应时域从未胜出。**</p>

+ **Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated Force Authority**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15928)
![architecture](https://img.shields.io/badge/Independent_Safety_Layer_EStop-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/University_of_Colorado_Boulder-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文拆解 Unitree H1-2 的独立安全层：它强制关节位置、速度与力矩上限并在急停按下或状态估计过期时停机；推挤试验中 MJPC 下操作员每次都需按急停（4.68±2.86 s），ALMI 15 次中 14 次恢复，急停倒地可释放约 600 J 能量。**</p>

+ **Robot Navigation and Obstacle Avoidance from Randomly Positioned External Cameras**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16282)
![architecture](https://img.shields.io/badge/Viewpoint_Invariant_Obstacle_Map-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/University_of_Tsukuba-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出 VINE，用监督学习的外置相机障碍物地图估计网络产出视角无关地图，再交给 PPO 或 A*：地图验证 IoU 单/双相机 0.909/0.913，导航成功率 92.3%/93.5%，高于机载 PPO 的 83.9%，而固定世界相机的 PPO 只有 24.7%。**</p>

