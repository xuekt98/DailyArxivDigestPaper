<!-- direction: world_model -->

+ **ResWAM: Learning What Changes, Not What Stays, for World-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19559)
![architecture](https://img.shields.io/badge/ResWAM_Residual_Dual_Branch_DiT-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Michigan_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ResWAM 用冻结 DINOv3 空间里的当前帧到未来帧特征残差替代完整未来特征监督，0.5B 双分支 DiT 以条件 flow matching 同时去噪动作与残差；总参数 2.3B，在 LIBERO-Plus、RoboTwin 2.0、RoboDojo 上取得 81.1%、93.8%、9.40% 的最优平均成功率。**</p>

+ **The Sense Paradigm for World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19796)
![architecture](https://img.shields.io/badge/Sense_Directed_Distance_Cross_Entropy-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/University_of_Jinan-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Sense 用有向距离 d(x→y)=Σ ReLU(y−x) 上的单一交叉熵损失替代 target network、方差惩罚与高斯惩罚，靠一个损失同时避免表征塌缩并让嵌入距离带上物理含义；四个像素环境上不可逆转移的 AUC 达 0.95–1.00，TwoRoom 规划 100% 到达目标。**</p>

+ **PanDWM: Panoramic 4D Driving World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19857)
![architecture](https://img.shields.io/badge/PanDWM_Panoramic_Causal_Diffusion-red)
![task](https://img.shields.io/badge/Driving_Simulation-magenta)
![organization](https://img.shields.io/badge/Shenzhen_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://aigeeksgroup.github.io/PanDWM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PanDWM 把六个针孔相机的画面拼成一条 360° 全景带，让相机边界落进同一张图，使跨视角一致性变成图像连续性；因果学生每窗口 4 步生成 16 帧，在 nuScenes 上 FID/FVD 均优于多相机基线且快 8–46 倍，同时把 50 步教师的 FVD 再降 22–25%。**</p>

+ **DiffWAM: Learning World Action Model from Consecutive Visual Difference**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19904)
![architecture](https://img.shields.io/badge/DiffWAM_MoE_Three_Expert-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://zgca-hmi-lab.github.io/DiffWAM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DiffWAM 用 World、Action、Diff 三专家混合架构学习未来状态、动作与相邻观测潜变量差，三专家只看当前帧且互不注意，推理时可摘除辅助专家；LIBERO 与 RoboTwin 2.0 平均成功率 98.8% 与 92.65%，真实操作 88.3%，比 FastWAM 高 1.75、1.55 与 15.0 点。**</p>

+ **SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20107)
![architecture](https://img.shields.io/badge/SAFER_Chunked_Latent_World_Model-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Purdue_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://ys-qu.github.io/safer-website)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SAFER 针对世界模型只在自己训练数据覆盖内可靠这一探索-利用困境，离线用脚本化可恢复扰动制造失败并由专家逐状态标注动作与价值，在线持续精化模型；CARLA 上路线完成率 0.95、每步回报 0.77，MetaDrive 回合回报 53.4 与 49.0。**</p>

+ **ThinkWAM: Rethinking Latent Futures for Action Refinement**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21258)
![architecture](https://img.shields.io/badge/ThinkWAM_Proposal_Rethink_Refine-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Xi’an_Jiaotong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://thinkwam-project.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ThinkWAM 用 propose–rethink–refine 回路让动作块提案修正多尺度未来潜变量，再回灌动作头生成动作块；LIBERO 成功率 98.70%，LIBERO-Plus 未微调 84.76%，RoboTwin 2.0 Clean/Random 85.75% 与 65.85%，真实 OOD 平均 64.4%。**</p>

+ **Lazy-MOSAIC: Accelerating Skill-Centric Manipulation Planning with Learned Skill-Effect World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21517)
![architecture](https://img.shields.io/badge/Lazy_MOSAIC_Skill_Effect_Model-red)
![task](https://img.shields.io/badge/Learned_Simulator-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://skill-mosaic.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Lazy-MOSAIC 用毫秒级的技能-效果世界模型替代高保真物理仿真来筛选候选技能：K=128 条提案约 0.7 毫秒打完分，只对有希望的提案跑昂贵仿真，160 次试验解出 104 次（MOSAIC 81 次），仿真查询由 46.4/67.9/134.5 降到 16.9/21.7/41.3。**</p>

<!-- direction: embodied_ai -->

+ **ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18176)
![architecture](https://img.shields.io/badge/ESI_Embodied_Self_Improvement_Flywheel-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ZERITH-ZLab/ESI)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ESI 把模块化具身 agent 本身当作后训练单位，每轮用环境交互同时改进 LLM 的决策提示、共享技能接口与 VLA 参数再整体重新部署，并用协作过程自产监督；RoboDojo 十个任务上平均 Score 62.03、成功率 49.41%，超过包括 GO-3 Nano Preview 在内的所有对照。**</p>

+ **Leaning Over to Reach Far-Away Objects**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19100)
![architecture](https://img.shields.io/badge/Supported_Reaching_Sampling_MPC-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/University_of_Colorado_Boulder-green)
[![project](https://img.shields.io/badge/project-blue)](https://h12leaner.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 Unitree H1-2 上，作者用纯本地感知与视觉标记的采样式全身 MPC 做倚靠-支撑-伸手-回收，把不可及目标变成可及：工作空间向外扩展约 50 厘米，笔记本上实时 34 Hz，54 次试验中 89% 到达指令目标、81% 完成完整回收循环。**</p>

+ **Ego2Sim2Humanoid: Agentic Real-to-Sim for Learning Loco-Manipulation VLAs without Robot Demonstrations**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19196)
![architecture](https://img.shields.io/badge/Ego2Sim2Humanoid_Agentic_Real_to_Sim-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/University_of_Notre_Dame-green)
[![project](https://img.shields.io/badge/project-blue)](https://robonana.github.io/ego2sim2humanoid/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Ego2Sim2Humanoid 把第一视角眼镜录像转成物理可验证的机器人训练轨迹：重建碰撞与纹理资产、预测目标接触带，再用抓取规划与双层站姿优化生成可行接触，最后训 RL 追踪策略；仅用转换数据微调的 GR00T N1.7 在 Unitree G1 上自主完成 loco-manipulation。**</p>

+ **MARS: Dynamic Routing of Reinforcement-Learned Atomic Skills for Multi-Stage Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19324)
![architecture](https://img.shields.io/badge/MARS_Mamba_Skill_Router-red)
![task](https://img.shields.io/badge/Long_Horizon_Task-magenta)
![organization](https://img.shields.io/badge/Chongqing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MARS 把冻结的通用 VLA 与逐阶段强化学习训练的原子技能并联，用 Mamba 时序编码加技能语义注意力做动态路由；四个 LIBERO 套件上 Macro-F1 平均 90.47%、成功率 89.25%，仿真 Tube Transport 任务成功率由 20.04% 提升到 85.67%。**</p>

+ **MoViC: Real-Time Humanoid Whole-Body Control from Monocular Video Streams**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19998)
![architecture](https://img.shields.io/badge/MoViC_Frequency_Domain_Transformer_Tracker-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://movicproject.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MoViC 用单目 RGB 直播视频作为人形机器人的控制信号，免去动捕设备：SAM 3D Body 约 10 Hz 重建动作、重定向到 24 自由度机器人后再外推到 50 Hz 参考；策略输入仅 810 维本体历史、52 维下一步参考与 320 维频域参考表示。**</p>

+ **DAPPT: Domain-Aware Policies from Procedural Trajectories for Sim-to-Real Dexterous Tool Use**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20202)
![architecture](https://img.shields.io/badge/DAPPT_Procedural_Trajectory_Tracking-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/Princeton_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/princeton-vl/DAPPT)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DAPPT 绕开对非刚体材料的高成本仿真，用域参数化的程序轨迹训练域感知 RL 策略并蒸馏成端到端传感动作策略；在 19 自由度手-臂上覆盖铲沙、搓橡皮泥棒等六个灵巧工具任务，最佳域参数下任务指标提升 1.5–3.8 倍并零样本迁移到真实机器人。**</p>

+ **DexFormer 2.0: Towards a Cross-Embodiment Foundation Policy for Dexterous Grasping**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20273)
![architecture](https://img.shields.io/badge/DexFormer_Canonical_Joint_Interface-red)
![task](https://img.shields.io/badge/Robot_Foundation_Model-magenta)
![organization](https://img.shields.io/badge/HKUSTGZ-green)
[![project](https://img.shields.io/badge/project-blue)](https://davidlxu.github.io/dexformer2-web/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DexFormer 2.0 把每台机器人映射到统一关节槽位并加有效掩码，用运动学树偏置注意力与 Transformer-XL 记忆推断本体相关动力学；单一 RL 策略在 4 臂 6 手的 18 个组合上训练，已见组合稳定成功率 89.01%，六个留出臂手对 51.18%，并零样本迁移到两种新手型。**</p>

+ **Stochastic Self-Distillation for Flow-Based Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20460)
![architecture](https://img.shields.io/badge/VLA_SSD_Stochastic_One_Step-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Imperial_College_London-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/llexieguo/VLA-SSD)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VLA-SSD 把 flow-matching 动作头自蒸馏成以布朗路径为条件的一步随机策略，同时解决 GRPO 的低延迟与低方差两大痛点；蒸馏后动作头前向快 7.7 倍，零方差组从 63% 降到 35%，再上 GRPO 在 LIBERO 达 93.0%、比 SFT 提升 15.9 个点。**</p>

+ **Lift, See, Act: Hierarchical Robot Policy Pretraining with 3D Foundation Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20481)
![architecture](https://img.shields.io/badge/LSA_Lift_See_Act-red)
![task](https://img.shields.io/badge/Robot_Foundation_Pretraining-magenta)
![organization](https://img.shields.io/badge/South_China_University_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://yiyuan00.github.io/Lift-See-Act)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LSA 用 Lift-See-Act 三阶段预训练机器人策略：先把 2D 视频抬升为稠密 3D 表征（对齐多个 3D 基础模型的中间表征），再用深度重建与手部热点引导注意力，最后落到策略学习；仿真成功率 92.2%，比无预训练基线高 18.9 个点，真实任务上比最强基线高 26.6 个点。**</p>

+ **AsymEEF: Bimanual Manipulation with Asymmetric End Effectors**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20557)
![architecture](https://img.shields.io/badge/AsymEEF_Cross_End_Effector_Interface-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://asymeef.vercel.app/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AsymEEF 用少量同构末端执行器的遥操作演示，迁移出二指、三指、五指等异构双臂组合的可执行轨迹：运动学教师给几何监督、稀疏真实 X-Calib 锚点修正抓取误差，共享编码器把腕部位姿与执行器状态映到形态无关潜空间，模拟中 replay-valid 扩展增益平均 16.6 倍。**</p>

+ **ARMFUL: Learning Whole-Arm Grasp Configurations for Single-Arm Pickup of Large Objects**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20692)
![architecture](https://img.shields.io/badge/ARMFUL_Whole_Arm_Grasp_Diffusion-red)
![task](https://img.shields.io/badge/Dexterity-magenta)
![organization](https://img.shields.io/badge/University_of_Southern_California-green)
[![project](https://img.shields.io/badge/project-blue)](https://manipulation-armful.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ARMFUL 配套发布首个单臂搬运大件物体的整臂抓取数据集 WAG，覆盖 793 个物体、约 170 万条经外力压力测试的关节配置；基于它的扩散抓取模型在训练物体上 85.4%、留出物体 69.9% 的抬升成功率，真实 Franka 臂在 10 个 IKEA 物体上 100 次试验抬起 70 次。**</p>

+ **TaF-Foundation: Wrench-Grounded Cross-Sensor Tactile Representations**
[![paper](https://img.shields.io/badge/Arxiv_2611.20-blue)](https://arxiv.org/abs/2611.20718)
![architecture](https://img.shields.io/badge/TaF_Wrench_Grounded_Encoder-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/ShanghaiTech_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://mrjiangjm.github.io/TaF-Foundation/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**TaF-Foundation 把触觉表征锚定在六维力矩这一共同物理参考上，从而无需传感器两两配对：自建平台从 24 个传感器、四大感测原理采到超过 1 亿条配对数据，单帧力 RMSE 降低 17.1%，跨传感器检索 R@1 提升 13.11 个点，真机操作成功率 46.25% 对最强基线 23.75%。**</p>

+ **ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21099)
![architecture](https://img.shields.io/badge/ForceHarness_Physics_Translation_Layer-red)
![task](https://img.shields.io/badge/Computer_Use_Embodied-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![project](https://img.shields.io/badge/project-blue)](https://showlab.github.io/ForceHarness)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ForceHarness 让只能发工具调用的冻结前沿模型也能用上力：标定手部力后由自终止力原语在模型之下闭环调力，物理量翻译层把力曲线转成带不确定性的物理量返回；真机上 GPT-6 Astra 零样本成功率从 3.3% 提到 90.0%，HiddenPhys 上由 62.1% 提到 96.4%。**</p>

