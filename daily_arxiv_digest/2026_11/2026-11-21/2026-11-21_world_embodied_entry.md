<!-- direction: world_model -->

+ **How Uncertain Is My Action? Self-Correcting Visual Planning with Frozen World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23620)
![architecture](https://img.shields.io/badge/ACTUS_Shift_Score_Self_Correction-red)
![task](https://img.shields.io/badge/Action_Conditioned_Prediction-magenta)
![organization](https://img.shields.io/badge/The_Ohio_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把冻结潜空间世界模型倒着跑：对假设的驱动偏移预测「本应观测到」什么，与实际观测之差构成只保留偏移可解释分量的 shift score；PushT 成功率 0.650→0.862，真机 reach 误差 36 mm→3–5 mm。**</p>

+ **JEPA Dots: Dual-Latent World Model for Language-Guided Robot Control**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24062)
![architecture](https://img.shields.io/badge/JEPA_Dots_Dual_Latent_Policy-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/Z_Robotics-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**JEPA Dots 用掩码注意力把语言条件挡在世界预测之外，另开 task 表征驱动流匹配策略；40 个 LIBERO 任务上成功率 84.9%、参数仅约 39.1M，同协议下把基线 76.0% 提升到 84.9%。**</p>

+ **WM^MLLM: Turning MLLMs into World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24193)
![architecture](https://img.shields.io/badge/WMMLLM_Panorama_State_Editor-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Princeton_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://ztmotalee.github.io/wmmllm/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WM^MLLM 把世界状态外置成带修订历史的全景图，MLLM 负责把请求翻译成对状态的操作并检查候选，生成器只提议视角；MBench-A 的 Epipolar 指标 91.5、相机往返完成率 85.3%，均高于六个基线。**</p>

+ **MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25105)
![architecture](https://img.shields.io/badge/MAWAM_Cross_Agent_World_Action-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://research-staging.nvidia.com/labs/lpr/mawam)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MAWAM 在单次采样里同时去噪全队机器人的动作 token 与未来视角 token，靠跨机器人注意力把「队友先动」的后果写进自己的采样；真机三任务平均成功率 67.8%，比 MA-VLA 高 18.9 个百分点。**</p>

+ **GEMS: Generation and Experience Memory for Subgoal-Guided Long-Horizon World Model Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25134)
![architecture](https://img.shields.io/badge/GEMS_Subgoal_Memory_Latent_Planning-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Minnesota_Twin_Cities-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GEMS 生成带时间结构的子目标，再用距离门在子目标与潜经验记忆选出的状态之间取舍，配合冻结世界模型做 CEM 规划；Cube 成功率 92.8%、Push-T 68.4%，比最强基线高 24.0 与 7.3 个百分点。**</p>

+ **Verify2Act: Critic-Guided Latent World Models for Verifying Language-Conditioned Manipulation Plans**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25243)
![architecture](https://img.shields.io/badge/Verify2Act_Critic_Latent_World_Model-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_Oklahoma_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Verify2Act 让 VLM 只提候选计划、潜世界模型 V2A-WM 在 DINOv2 特征空间想象 rollout，再由双头 critic 校验时序一致性与目标达成后才执行；六个语言条件任务成功率 83.3%，纯 VLM 仅 53.3%。**</p>

+ **Search or Scoring? Diagnosing Why Visual World-Model Planners Fail**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25347)
![architecture](https://img.shields.io/badge/Search_Scoring_Failure_Diagnosis-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**该文用已知解探针把世界模型规划失败拆成搜索失败与打分失败：Metaworld 上代价在真实结果 AUROC 0.94、预测上仅 0.54，平均 demo 窗口因此解出 168 个新任务中的 127 个，远多于让模型自己选的 87 个。**</p>

<!-- direction: embodied_ai -->

+ **Bridging vision-language reasoning and learned control for legged navigation in the wild**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25215)
![architecture](https://img.shields.io/badge/ROAM_VLM_Risk_Map_Nav-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/ETH_Zurich-green)
[![project](https://img.shields.io/badge/project-blue)](https://roam-hiking.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ROAM 用 VLM 的常识推理产出语义标签与导航代价，开词表分割转成稠密实时风险图，再条件化两条仿真 RL 策略；机器人在阿尔卑斯完成 10.1 km、落差 1220 m 的徒步且几乎无需干预。**</p>

+ **Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26420)
![architecture](https://img.shields.io/badge/Awaken_HI_Shared_Action_Expert-red)
![task](https://img.shields.io/badge/Robot_Foundation_Pretraining-magenta)
![organization](https://img.shields.io/badge/EngineAI-green)
[![project](https://img.shields.io/badge/project-blue)](https://engineai-robotics.github.io/Awaken-HI)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Awaken-Human 用约 5 万小时第一人称立体视频配同步全身人体动作，Awaken-HI 以共享 action expert 同时预测人体动作与重定向机器人动作；全量预训练加 T800 适配后 8 个任务平均成功率 93.75%。**</p>

+ **GRID-UAV: Geometry and Ray-depth Integrated Decision-making for Unmanned Aerial Vehicles**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23491)
![architecture](https://img.shields.io/badge/GRID_Ray_Depth_Aligned_VLA-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Mohamed_bin_Zayed_University_of_Artificial_Intelligence-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/anas2908/GRID-UAV)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**GRID 把单目深度经射线校正抬升到无人机坐标系的 3D 位置，训练期再对齐冻结的多视图几何模型、推理期零开销；到达率 61.5%→69.5%，TravelUAV 未见地图划分相对 SOTA 提升 25.4%。**</p>

+ **RageVLA: Augmentation-Trained Perception and Action for State-of-the-Art Robustness on LIBERO**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23517)
![architecture](https://img.shields.io/badge/RageVLA_Augmented_Grounded_Encoding-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/ragento.ai-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RageVLA 用通用规则重排 LIBERO 示教（物体移位旋转、任务换环境、指令改写），再以冻结 DINOv3 感知引擎解耦场景交给流匹配扩散 transformer；0.21B 参数在 LIBERO-PRO 上得 0.72，超越已发表的 0.53。**</p>

+ **RecallFlow: Episodic Memory as the Source Distribution of Generative Robot Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23731)
![architecture](https://img.shields.io/badge/RecallFlow_Memory_Source_Distribution-red)
![task](https://img.shields.io/badge/Diffusion_Policy-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RecallFlow 用少量 recall slot 把情节记忆与当前视角重定位，再把每个 slot 变成流匹配源分布的一个高斯分量，让生成从接近正确动作处起步；MIKASA-Robo 上平均成功率 80.4%，比最强基线高 20.3 个百分点。**</p>

+ **LAGR: Language-Aware Grasp Re-Ranking for Task Oriented Grasping**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23858)
![architecture](https://img.shields.io/badge/LAGR_Language_Reranked_Grasp-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Purdue_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LAGR 用 268 万条带分数的 5-DoF 抓取标注训练，先生成带物理可行性分数的提案，再用语言条件重排序器整体打分；比次优方法高 9.3 个百分点，并在 Franka Research 3 上真机执行验证。**</p>

+ **ReLoco: Unified Humanoid Locomotion and Fall Recovery via Behavior-Conditioned Motion Priors**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23916)
![architecture](https://img.shields.io/badge/ReLoco_Behavior_Conditioned_AMP-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/Huazhong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ReLoco 用行为条件化的对抗运动先验：姿态选专家池、共享判别器接两个行为专属输出头，一个本体感知策略同时学出行走、跑步、任意姿态起身与指令恢复；起身成功率 96.80%、被推恢复 96.96%。**</p>

+ **BEV-Diffusion: Camera-Only Traversability Navigation with BEV Memory and Efficient Cross-Robot Adaptation**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24155)
![architecture](https://img.shields.io/badge/BEV_Diffusion_Traversability_Planner-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/Intelligent_Space_Robotics_Laboratory_Skolkovo_Institute_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**BEV-Diffusion 用冻结 DINOv2 与逆透视融合学出分级可通行性、其不确定性与路径，去噪器少量 DDIM 步生成极坐标路点；未见庭院中轮腿机器人自主行 120 m、96% 无干预，换机器人只重训约 3% 的 BEV 头。**</p>

+ **Towards Pose-Robust Few-Shot Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24360)
![architecture](https://img.shields.io/badge/WACO_World_Anchored_Canonicalization-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/School_of_Software_Shandong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://peacelwh.github.io/WACO/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WACO 用正运动学放出的机械臂作度量标定靶、静态场景作世界锚，从单张 RGB-D 帧同时估出相机与基座偏移并把观测统一回标定坐标系；仿真受扰动成功率提升 13.2 个点，真机提升 36.7 个点。**</p>

+ **SHAPE: Discrete Supervision and Parallel Continuous Streams for Learning Dexterous Manipulation from Egocentric Human Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24585)
![architecture](https://img.shields.io/badge/SHAPE_Discrete_Tokens_Dual_Stream-red)
![task](https://img.shields.io/badge/Dexterity-magenta)
![organization](https://img.shields.io/badge/Sharpa_Robotics-green)
[![project](https://img.shields.io/badge/project-blue)](https://li-yaping.github.io/SHAPE/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SHAPE 让骨干把每个 EEF chunk 预测成离散 FAST token 作辅助监督，并行的流匹配 expert 同时输出 EEF 与关节两条可执行流；22 自由度双手机器人上关节读出六任务得 0.80，π0.5 为 0.63。**</p>

+ **F$^3$: What Makes Good Experience in World-Action Models?**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24708)
![architecture](https://img.shields.io/badge/F3_Form_Fit_Fusion_Experience-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**F3 用 Form、Fit、Fusion 三步管理世界-动作模型的经验：压成已验证的操作记录、教会策略判断何时有用、再以前缀加动作先验注入；只用 200 个样本训练即在两个套件上比原生模型高 12.0 与 10.8 个百分点。**</p>

+ **RoboMorpher: Scaling Robot Morphology Representations for Cross-Embodiment Action Prediction**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24816)
![architecture](https://img.shields.io/badge/RoboMorpher_Morphology_Tokenizer-red)
![task](https://img.shields.io/badge/Robot_Foundation_Model-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://robomorpher.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboMorpher 是形态条件化的动作 tokenizer，联合重建关节角与连杆位姿，用 4000 万条形态-状态对预训练并冻结接入 VLA；RoboTwin 2.0 上成功率 56.40%，比连续关节空间控制高 9.73 个百分点。**</p>

+ **NereidVLA: Learning to Understand and Navigate the Underwater World**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24864)
![architecture](https://img.shields.io/badge/NereidVLA_Sea2Know_Two_Stage-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**NereidVLA 先用约 200 万条无轨迹海洋样本训 Sea2Know 学空间接地，再用模拟水下动力学的专家轨迹适配为离散运动 token 导航；仿真成功率 72.4%→84.4%，水池真机 78.75% 对 InternVLA-N1 的 47.50%。**</p>

