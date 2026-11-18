<!-- direction: world_model -->

+ **V-JEPA-LM: Video-Language Models That Read Dynamics Beyond Static, Text-Aligned Representations**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17831)
![architecture](https://img.shields.io/badge/VJEPA_LM-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/Hanyang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/kkt94/Llama-V-JEPA-LM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把像素反事实变换做成答案受控的训练变体，让语言模型真正读取 V-JEPA 隐含的动力学子空间；单阶段 4.53M 样本、每帧 32 个视觉 token，4B 模型在 11 个视频基准上得 72.1 分。**</p>

+ **Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17529)
![architecture](https://img.shields.io/badge/Latent_Goal_Cost_Adapter-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Technical_University_of_Crete-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在冻结 I-JEPA 嵌入上拟合一个残差适配器，用逐步扩大的初始状态课程学出潜目标代价：DotWall 成功率 54% 提到 98%，PointMaze 82% 提到 96%，未见布局上排序一致性 71.9% 提到 85.8%。**</p>

+ **Joint World Action Models through Differentiable Trajectory Optimization**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17626)
![architecture](https://img.shields.io/badge/WATO_Trajectory_Optimization-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Hybrid_Robotics_BAIR_UC_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把生成的动作与未来状态同时作为参考做可微轨迹优化，再把优化结果摊销进生成器：7 个视觉控制环境平均成功率从 79.9% 提到 91.7%，部署时比 CEM 快 11.5 倍、世界模型评估少 600.5 倍。**</p>

+ **Beyond Prediction Gain: LASR as a Metric for Action-Grounded Latents in World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17775)
![architecture](https://img.shields.io/badge/LASR_Latent_Action_Audit-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出无量纲指标 LASR，衡量潜变量在扣除当前状态与非动作对照后还剩多少动作预测支持，并给出 GeoLASR 与 WorstLASR 两个摘要；真实动作正对照为 0 与 0.174，可用于审计世界模型的潜变量。**</p>

+ **Ego2Flow: Benchmarking the Traffic-System Impact of Autonomous Driving on Maps Distilled from Real-World Roads**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17720)
![architecture](https://img.shields.io/badge/Ego2Flow_Map_Distillation-red)
![task](https://img.shields.io/badge/Driving_Simulation-magenta)
![organization](https://img.shields.io/badge/University_of_Wisconsin-Madison-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Fisher-007/Ego2Flow)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出闭环交通基准 Ego2Flow：借交通信息图与迭代反馈把 Argoverse 2 观测蒸馏为 6 张 CARLA 地图，六城平均 ADE 0.7966 m，用于评估驾驶策略对车流效率、安全与能耗的系统级影响。**</p>

+ **Recovered or Memorized? Investigating Dynamical Consistency and Faithfulness in World Model Latents**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18807)
![architecture](https://img.shields.io/badge/ARC_Discrete_Frechet_Certification-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/Southern_Alberta_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/jfran03/dynamical-investigation)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ARC 用离散 Fréchet 距离为世界模型划出记忆型 null 的地板与真值天花板，检验 TD-MPC2 学到的是钟摆动力学还是轨迹记忆：k=10 时 7 个约束平均全部越界、校正后 6 个显著，k=25 则一个都无法认证。**</p>

+ **When to Trust Simulated Patient Responses:Support-Gated World Models for Vasopressor Decision Support**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18458)
![architecture](https://img.shields.io/badge/SGWM_Support_Gated_Clinical_Sim-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Sun_Yat-sen_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SG-WM 在 propose–simulate–refine 临床 agent 前加了一层支撑与分歧双闸门，只在有观测支撑且集成一致时放行预测，其余显式弃权：在 eICU-CRD 上覆盖 62.0% 的转移把 MAP 误差从 9.2 降到 7.3 mmHg，同时把无支撑动作选择率从 12.0% 清零。**</p>

<!-- direction: embodied_ai -->

+ **Heavy Metal Acrobatics: Learning Dynamic Control for Skid-Steer Loaders**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18365)
![architecture](https://img.shields.io/badge/SSL_Acrobatic_SimToReal_Policy-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/Robotic_Systems_Lab_RSL_ETH_Zürich-green)
[![project](https://img.shields.io/badge/project-blue)](https://sites.google.com/leggedrobotics.com/heavy-metal-acrobatics)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文在仿真里用 RL 训练策略，再迁移到真实 5 吨 John Deere 332G 滑移装载机，完成两轮起立、轮上越野、原地旋转与铲斗摆动：臂角 28° 与 31° 时 11/11、12/12 全成功，抬到 34° 时降到 78.6%。**</p>

+ **Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17394)
![architecture](https://img.shields.io/badge/Agentic_Teacher_Data_Engine-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向 VLA 后训练的智能体数据引擎：编码智能体读失败回放、迭代写闭环代码策略补齐失败状态，π0 在 LIBERO-10 从 79.4% 提到 87.8%，MetaWorld-10 从 80.4% 提到 90.6%。**</p>

+ **X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17598)
![architecture](https://img.shields.io/badge/XNav_Long_Horizon_Navigation-red)
![task](https://img.shields.io/badge/Long_Horizon_Task-magenta)
![organization](https://img.shields.io/badge/AgiBot_X-Lab_Boson_Lab-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**人形机器人长程导航全链路系统：MELIOR 只用内置 RGB 相机，X-Navarch 把指令拆成子任务并显式避障；灵犀 X2 上跑完 96.6 米跨楼任务，R2R-CE 成功率 70.5%。**</p>

+ **Reusing Locomotion Training Recipes Across Humanoids via Body-Aligned Virtual Joints**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18003)
![architecture](https://img.shields.io/badge/BodyAligned_Virtual_Joint_Interface-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Center_for_Humanoid_Research_Korea_Institute_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文在原生传动层之上插入身体对齐的虚拟关节坐标层，让同一套未改动的训练配方跨 Unitree G1、PND Adam 与自建平台都能跑：Adam 上脚步朝向角从 4.8° 降到 0.5%，G1 真机上偏航漂移从 5.31 降到 0.89 度每秒。**</p>

+ **When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18491)
![architecture](https://img.shields.io/badge/HSD_Hidden_Start_Delay_Handover-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Toyota_Motor_North_America-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/mkhoshnam/Selfplay-PPO-handover)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文诊断出自博弈交接策略在陌生伙伴上崩溃的原因是对方起手时机（延迟 1 秒就让成功率从 95% 掉到 6%），再用接收方看不见的隐藏起始延迟随机化修复：再训 300 步后对陌生脚本伙伴的成功率从 31% 升到 80%。**</p>

+ **PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18305)
![architecture](https://img.shields.io/badge/PROOF_Uncertainty_Gated_Locomotion-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Southern_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://syw-robotics.github.io/proof-loco/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PROOF 用带不确定度头的教师-学生蒸馏，让 Unitree Go2 在深度视觉失效时自动退回纯本体感知：强视觉扰动下五类地形通过率 99–100%，没有教师掩码的基线全部为 0%，真机上只剩强运动模糊的两档速度仍会失败。**</p>

+ **Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18397)
![architecture](https://img.shields.io/badge/Gamer_Generalist_Game_VLA-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/miHoYo_Honkai_AI_R&D_Team-green)
[![project](https://img.shields.io/badge/project-blue)](https://mihoyo-gamer.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Gamer 是面向长时程交互的通用视觉-语言-动作基础模型：用数万小时键鼠操作做继续预训练、统一成 5 Hz 观测加 30 Hz 动作序列，配合记忆压缩与时序感知 GRPO，把跨游戏操作与长程任务放进同一套训练与部署管线。**</p>

+ **Racing the Clock: Teaching VLNs Budget-Conditioned Object Search**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17442)
![architecture](https://img.shields.io/badge/Budget_Conditioned_Bellman_Expert-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/University_of_California_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**研究预算条件化物体搜索：用同一个预算索引的 Bellman 递归套不同场景抽象造专家。房间级专家蒸馏到 Uni-NaVid 后在 2000 步收集率 72.7%，高于专家回报更高的对象级监督的 65.5%。**</p>

+ **TouchTwin: Scaling Human Touch Data via Real-to-Sim-to-Real**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17619)
![architecture](https://img.shields.io/badge/TouchTwin_Tactile_Replay-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 880 税元件手套的实测触觉重建 MuJoCo 回放，补上视觉重建缺失的力信息：抓握力从 0.31 倍修正到 0.99 倍记录值，留出录像 20/20，接触漏检从 32.2% 降到 13.1%。**</p>

+ **Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18372)
![architecture](https://img.shields.io/badge/VLA_LifeCycle_Survey-red)
![task](https://img.shields.io/badge/Robot_Foundation_Model-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_University_of_Huddersfield-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该综述沿七条生命周期轴梳理 2022 年 12 月至 2026 年 10 月的 88 篇 VLA 工作并逐轴分析 22 个主模型，给出三条趋势：数据从 π0 的一万小时扩到两万人类视频、参数分成 3–7B 与 1B 以下两派、同时操作与导航的通用 VLA 开始出现。**</p>

+ **Grounding Object-to-Object Hazard Reasoning into 3D Risk Fields for Task-Conditioned Safety**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17566)
![architecture](https://img.shields.io/badge/VLM_Hazard_Risk_Field_Framework-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_McGill_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://vlm-hazard-riskfield.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该框架让 VLM 先判断任务是否必须拒接、再定位可预防的物体对危害，并用开放词汇分割与深度把危害落成 3D 风险场交给避障模块修正轨迹：可预防危险上成功率与安全成功率同为 90.9%，纯几何避障的安全成功率则是 0。**</p>

+ **A Generalizable Approach to Safety-Aware Robotic Behavior Planning with an Explicit Constraint Space**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18026)
![architecture](https://img.shields.io/badge/ConstraintSpace_Safety_Planning-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该框架把安全规则存成显式的 Constraint Space，由查询条件化双塔模型按任务与环境选约束，再让多模态 Safety Inspector 闭环纠错：在 93 条规则、150 条留出查询上召回 37.48% 对 24.32%，检验器判定准确率最高 97.7%。**</p>

+ **Objectives as Policies: Vision-Language Model Cost Programs for Contact-Rich Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18298)
![architecture](https://img.shields.io/badge/ObjectivesAsPolicies_Cost_Program-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/University_of_Illinois_Chicago-green)
[![project](https://img.shields.io/badge/project-blue)](https://zihaolu001.github.io/oap-project/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**OaP 用可编辑的目标程序把预训练 VLM 与采样式 MPC 接起来：每个程序按阶段组合代价库中的运行与终端项，VLM 依据仿真 rollout 迭代修改程序，四个桌面任务上 2 轮反馈拿到 36/40（90%），真机迁移 32/40（80%）。**</p>

