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

+ **FloCOS: Predicting Compact Forward Occupancy Sets of Surrounding Vehicles via Conditional Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15488)
![architecture](https://img.shields.io/badge/Flow_Matching_Forward_Occupancy-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/School_of_Future_Science_and_Engineering_Soochow_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FloCOS 用条件流匹配把周围车辆的未来占据表示成半空间凸多边形的时变并集，直接作为规划器的碰撞约束来源：在 Waymo 1000 个测试场景上覆盖率 99.3%、面积比 3.10、交互完成率 85.6%，而面积比高达 8.59 的保守基线完成率只有 3.1%。**</p>

+ **TyphoonWorld: A Residual Token World Model for Probabilistic Forecasting of Typhoon Imagery**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18740)
![architecture](https://img.shields.io/badge/Residual_Token_World_Model-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TyphoonWorld 是残差式离散 token 世界模型，只采样直接回归中心被抹平的那部分误差：在 46 个留出风暴、276 个预报窗口上把 220 K 以下深对流区的 CRPS 相对所有其他集合降低 14%–39%，离散度与误差相关 0.78，参数量仅为无条件世界模型的 56%。**</p>

+ **From Forecasting to World Modeling: Can Temporal Foundation Models Recover Causal Response?**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15009)
![architecture](https://img.shields.io/badge/Causal_Response_Evaluation-red)
![task](https://img.shields.io/badge/Action_Conditioned_Prediction-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**这篇工作系统检验「预测得准」不等于「反事实估得准」：在真值已知的模拟零售数据与真实销量记录上，基础模型的预测误差与价格效应误差常常反向；工具变量以残差形式给可使反事实 WMAPE 从 0.092 降到 0.064，直接喂原始工具变量反而升到 0.153。**</p>

+ **Multi-View 3D Reconstruction Using V-JEPA Features**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15143)
![architecture](https://img.shields.io/badge/VJEPA_Geometry_Adaptation-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Anwarshamim01/multi-view-3d-reconstruction-using-v-jepa-features)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 V-JEPA 2.1 的稠密视频特征接到多视角重建上，收益并不一致：空间相机配置在 168 个 CO3D 窗口上把轨迹误差降 29.3%，但仍比单位位姿基线高 10.03%，联合相对目标让对齐 Chamfer 从 0.6447 降到 0.5573，原始 Chamfer 却从 3.5535 涨到 4.4374。**</p>

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

+ **Autonomous Trail Racing with a Bicycle Robot**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15280)
![architecture](https://img.shields.io/badge/Terrain_Embedded_Navigation-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Robotics_and_AI_Institute_RAI_Zurich-green)
[![project](https://img.shields.io/badge/project-blue)](https://pages.rai-inst.com/autonomous-trail-racing/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把山道路径编码成地形的一个语义层，自行车机器人 UMV 在苏黎世 1 公里非结构化山道上全程自主跑完，平均 3.26 m/s、峰值超 5 m/s，比遥控基线快 2.3 倍；语义管线从 50 Hz 提到约 90 Hz，在 AGX Orin 上以 30 Hz 融合 LiDAR 建图。**</p>

+ **EMS-Nav: Embodied Multi-Scale Navigation**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15589)
![architecture](https://img.shields.io/badge/Region_Centered_Navigation-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EMS-Nav 把区域当作感知、建图与导航的基本单元，用高斯空间交互场做在线分区、周期性多尺度解析构语义层级：在 18628 条覆盖物体、房间、区域、实例四类目标的指令上把首次成功率比最强基线提高 9.39 个百分点，并在 RTX 4060 Ti 上跑到 5.19 FPS。**</p>

+ **DroneDiffusion: Uncertainty-Guided Diffusion Path Planner for UAV Navigation**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15277)
![architecture](https://img.shields.io/badge/Perceptual_Safety_Diffusion_Planner-red)
![task](https://img.shields.io/badge/Diffusion_Policy-magenta)
![organization](https://img.shields.io/badge/Intelligent_Space_Robotics_Laboratory_Skolkovo_Institute_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DroneDiffusion 把传感器失效区做成扩散规划器的一等条件量：AnyTraverse 可靠性图与 RGB、目标点、初速度一起条件化 1D U-Net，推理时再叠加 CHOMP 引导，真实机上把碰撞率从 14.71% 降到 7.77%，轨迹平均感知可靠性 0.714 对几何基线 0.626。**</p>

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

+ **APG-Planner: Learning Vision-Based High-Speed Trajectory Planning via Analytic Policy Gradient**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15296)
![architecture](https://img.shields.io/badge/Analytic_Policy_Gradient_Planner-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**APG-Planner 用微分平坦性把规划轨迹解析成车辆状态，在不建可微动力学模型的前提下做 episode 级解析策略梯度：稀疏林地成功率 94%、均速 8.16 m/s，去掉时序梯度只剩 2.46 m/s 而 PPO 仅 60% 成功率，单卡约 30 分钟训练，真实飞行峰值 11 m/s。**</p>

+ **CARE-Drive: Coupled Alternating Refinement for Ego-trajectories**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15360)
![architecture](https://img.shields.io/badge/Component_Alternating_Refinement-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/NEXTAI_Research_Institute_Chery_Group-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/marshal12138/CARE-Drive)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CARE-Drive 把轨迹精修改写成位置与航向两个物理分工的专家：Qwen3-VL-2B 骨干冻结后交替优化，NAVSIM v1 的 12146 个 navtest 场景上 PDMS 从 86.462 提到 88.837，其中航向专家先贡献 1.100 分、位置专家再贡献 1.110 分。**</p>

+ **From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14981)
![architecture](https://img.shields.io/badge/JMIR_CGRR_Pipeline-red)
![task](https://img.shields.io/badge/Scene_Reconstruction-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Chemical_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**从单张 RGB 图出发的完整管线：SAM 3D Objects 重建米制场景，JMIR 在重定向前校正人—场景几何、GMR 后由 CGRR 修复机器人支撑误差；精修时间从 480 s 降到 87 s（5.5×），仿真成功率 89%，Unitree G1 上 50 次物理试验成功率 70%。**</p>

+ **CrowdMAPS: Crowdsourcing Multiple Actions per State for Real-World Imitation Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15078)
![architecture](https://img.shields.io/badge/Multiple_Actions_Per_State-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/University_of_Minnesota_Twin_Cities-green)
[![project](https://img.shields.io/badge/project-blue)](https://yilongsong.github.io/CrowdMAPS/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CrowdMAPS 用网页 3D 界面让远程标注者给已访问状态补充多个可执行的目标位姿动作：五个真机操作任务上动作宽度从 1 加到 10，关键位姿策略平均成功率从 38.7% 升到 74.2%，轨迹策略提升 33.0 个百分点并优于追加等量专家遥操作。**</p>

