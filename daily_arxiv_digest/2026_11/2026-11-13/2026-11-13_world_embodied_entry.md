<!-- direction: world_model -->

+ **Fast Inference-Time Policy Refinement via Action-Affine World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15011)
![architecture](https://img.shields.io/badge/Action_Affine_World_Model-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**动作仿射世界模型 A²WM 只学策略的小动作修正如何改变结果，用一次模型评估加一次凸 QP 完成在线精修：四个仿真操作任务平均成功率从 27.18% 提到 59.51%，每控制步额外开销仅 3.80 ms，PushT 上以 3.40 ms 追平 GPC-OPT 的 346.47 ms。**</p>

+ **The Posterior-Prior Epistemic Gap: When World Model Imagination Fails to Carry Task-Relevant Signals**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14955)
![architecture](https://img.shields.io/badge/Posterior_Prior_Epistemic_Gap-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Michigan-Dearborn-green)
[![project](https://img.shields.io/badge/project-blue)](https://bimilab.github.io/paper-posterior-prior-epistemic-gap/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RSSM 世界模型加主动推断规划在 CARLA 上被直接体检：同一障碍物探针在后验状态 AUC 0.85，15 步想象后掉到 0.71、logit 间隔降 57%，无特权坐标时避障率归零，而集成分歧只有 AUC 0.52 的随机水平。**</p>

+ **FOE-Dreamer: Deployment-Efficient Learning of Cyber Defense Policies in Operational Networks**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14880)
![architecture](https://img.shields.io/badge/Factored_Opponent_Enhanced_Dreamer-red)
![task](https://img.shields.io/badge/Dreamer-magenta)
![organization](https://img.shields.io/badge/University_of_Texas_at_El_Paso-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FOE-Dreamer 把潜状态拆成防御者可控分量、外生用户活动与对手嵌入三部分，在 8 主机 OpenStack 实网上单 GPU 训练三天，把回合损失做到 Rainbow 与 IQN 的一半左右，无需仿真器预训练阶段，适合交互代价高的真实系统。**</p>

<!-- direction: embodied_ai -->

+ **Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14834)
![architecture](https://img.shields.io/badge/Hindsight_Decision_Model-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/University_of_California_Berkeley-green)
[![project](https://img.shields.io/badge/project-blue)](https://wen-hanhsieh.github.io/hdh/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用冻结 VLA 自身的 rollout 终局成败训练轻量动作验证器：LIBERO-10 四个任务平均成功率 78.8%→82.3%，三个真机任务从 44.7%→67.3%（毛绒玩具摆放 64%→94%），每次查询中位时延只增加 5.4%，GPT-5 验证器则需 27,674 ms。**</p>

+ **Scaling VLA Serving Under Robotic Execution Constraints**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14969)
![architecture](https://img.shields.io/badge/XInfer-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/X_Square_Robot-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/X-Square-Robot/xinfer)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**生产部署的 VLA 服务系统 XInfer 用异步执行引擎与执行感知的跨阶段调度，把异构算力与机器人响应需求耦合调度：三个 VLA 模型上单卡有效机器人容量达 vLLM-Omni 的 1.26–3.75 倍（VLA-2B 18 台对 10 台、π0.5 24 台对 15 台），ERC 判据为 P50<150 ms 且零错误。**</p>

+ **ILA: A Transferable Interface-Level Adapter for Compliant Humanoid Motion Tracking**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14985)
![architecture](https://img.shields.io/badge/Interface_Level_Adapter-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology_Shenzhen-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ILA 把柔顺引导做成接口层适配器：只用机器人观测历史预测参考动作的修正量，接在 MotionTracking、MimicLite、Sonic 三个预训练跟踪器前且权重全冻结、无需力传感器，指导目标误差分别下降 63.6% 与 75.4%，无外力时跟踪误差仅增 0.5%。**</p>

+ **Genie Sim Benchmark: Real-to-Sim Fidelity and Evaluation**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15020)
![architecture](https://img.shields.io/badge/Genie_Sim_Benchmark-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**真机—仿真双轨基准：22 个机器人-任务对跨 16 个任务名，真机微调 π0.5 的仿真—真机 Score 相关 r=0.9686、MAE 0.0405、RMSE 0.0520；32.6503 s 遥操作轨迹标定逐关节位置 RMSE 0.00614–0.03522 rad、力矩 RMSE 0.73545–4.00099 N·m。**</p>

+ **SPIRE: Task-agnostic embodied continual learning through autonomous situation inference and causal motor-primitive reuse**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14840)
![architecture](https://img.shields.io/badge/SPIRE-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/University_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SPIRE 用递归脉冲网络从动作—结果证据自行推断情境，把成熟 motor actor 保护起来并与情境残差组合驱动运动种群：坐标、三关节与隐藏力三类控制中，达标所需交互次数从 109.25 次降到 66.00 次，先修优势为最强无任务替代方法的 2.4 倍。**</p>

+ **Can I join you? Extended Social Force Based Model with Predictive Control and Barrier Functions for Humanoid Group Repositioning Amidst Obstacles**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14853)
![architecture](https://img.shields.io/badge/Extended_Social_Force_MPC_CBF-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Simon_Fraser_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ESFFM 用扩展社会力场给出名义加速度，再由 MPC 前瞻规划、控制障碍函数兜底安全：四类 Gazebo 布局共 8 个条件里含 CBF 的控制器有 7 个零碰撞（纯 ESFFM 仅 1 个），平均 jerk 再降 1.22%–39.63%，并有 40 人在线用户研究佐证社交恰当性。**</p>

+ **From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14981)
![architecture](https://img.shields.io/badge/JMIR_CGRR_Pipeline-red)
![task](https://img.shields.io/badge/Scene_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Chemical_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从单张 RGB 图出发的完整管线：SAM 3D Objects 重建米制场景，JMIR 在重定向前校正人—场景几何、GMR 后由 CGRR 修复机器人支撑误差；精修时间从 480 s 降到 87 s（5.5×），仿真成功率 89%，Unitree G1 上 50 次物理试验成功率 70%。**</p>

+ **HeadIO: Body-Frame Heading Decomposition for Neural Inertial Odometry on Head-Mounted Devices**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14895)
![architecture](https://img.shields.io/badge/HeadIO-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Northwestern_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HeadIO 把机体系 heading 分解与双向 Mamba 结合，用于头戴设备的无摄像头惯性里程计：Nymeria 上 RTE-5s 从 0.260 m 降到 0.239 m（改善 8.1%），参数 0.97M 对等变方法的 7.59M、算力 444 对 1227 MFLOPs，且可与任意骨干组合。**</p>

+ **Adapting Monocular Depth Estimation in Novel Scenes through Disparity Refinement and Robot Ego-Motion**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14958)
![architecture](https://img.shields.io/badge/EM_ViT-red)
![task](https://img.shields.io/badge/Scene_Reconstruction-magenta)
![organization](https://img.shields.io/badge/University_of_California_Riverside-green)
[![project](https://img.shields.io/badge/project-blue)](https://emvit-mde.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EM-ViT 把仿射不变的单目相对深度在线适配成米制深度，按立体相机参数化拆成稠密视差精化与有效基线标量两个头，用稀疏 LiDAR 与可选自运动训练轻量 ViT：KITTI 上 δ1 0.822、AbsRel 0.14、适配 57.48 s，均在 Jetson AGX Orin 上测得。**</p>

+ **DIVAL: Diffeomorphic Vector-Field Alignment for Nonholonomic Motion Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14918)
![architecture](https://img.shields.io/badge/Diffeomorphic_Vector_Field_Alignment-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DIVAL 对工作空间做微分同胚形变，把向量场方向在起点扭到机器人当前朝向上、区域外保持原场：非完整机器人数值仿真所有试验均无碰撞收敛且无控制不连续，实机地面车在扰动下同样无碰撞收敛，过渡函数用 12 系数五次 B 样条优化。**</p>

