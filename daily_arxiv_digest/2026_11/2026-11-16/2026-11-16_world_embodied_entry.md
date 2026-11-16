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

<!-- direction: embodied_ai -->

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

+ **Imitation Policies Learn a Proprioceptive Anchor: A Predictive Law for Perception Noise and Its Closed Loop Cost**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17658)
![architecture](https://img.shields.io/badge/Proprioceptive_Anchor_Law-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/Arizona_State_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**揭示模仿策略对噪声读数的折价定律 α=V/(V+s²)，锚点方差一次实测即可预测 10 组留出灵敏度（平均绝对误差 0.025，经典 EIV 为 0.37），但闭环下 15 个策略的偏移响应全部超过 α。**</p>

+ **VACO: Vertex-Aligned Decoding for Dense Hand Contact Estimation from a Single Image**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17755)
![architecture](https://img.shields.io/badge/VACO_Vertex_Aligned_Decoder-red)
![task](https://img.shields.io/badge/Tactile_Sensing-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**顶点对齐解码器 VACO：每个 MANO 顶点在自己的投影位置采样多尺度图像特征再预测接触，五个基准上单检查点即达 SOTA，Hi4D 上 F1 0.860，相对最强直接预测器提升 20.7 个百分点。**</p>

+ **Talk to Act: A Synthetic Multi-Turn Dialogue Benchmark for Human Intent Extraction and Action Planning in Robotics**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17549)
![architecture](https://img.shields.io/badge/Tool_Calling_Intent_Parser-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Reutlingen_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/datasets/deepukr007/hri_human_intent_from_conversation)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**合成多轮人机对话数据集并把意图抽取化为结构化函数调用：270M 到 8B 的开权重模型在无微调下可用，Gemma4:E4B 目标准确率 63.6%、动作级 F1 74.2%，为端侧对话机器人给出基线。**</p>

+ **On the Utility of Pre-Trained Visual Representations for Policy Learning of Contact-Rich Insertion Tasks**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17631)
![architecture](https://img.shields.io/badge/Contact_Centric_Feature_Policy-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/University_of_Pennsylvania_GRASP_Laboratory-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把接触密集插入任务放大镜化评测视觉表征：真值接触特征在全部设定下最优，DINOv2 与 Theia 在仿真书插上反而不及从零训练、在真实书插上却有效，说明表征效用高度依赖任务条件。**</p>

+ **ERA: Error-Resistant Autonomous Object Navigation with Predicted Depth**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17730)
![architecture](https://img.shields.io/badge/ERA_Revisable_Occupancy_Navigation-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**免训练的无深度传感器物体导航系统：用可修正占据加可达视点探索对冲预测深度的视相关误差，把 VLFM 在预测深度下的成功率从 10.8% 抬到 61.7%，ERA 本身达 70.1%。**</p>

+ **When Does Cross-View Consistency Matter in Multi-View Appearance Augmentation? A Controlled Study for Visuomotor Policies**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17751)
![architecture](https://img.shields.io/badge/State_Replay_Cross_View_Augmentation-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/PKUJZX/xview-consistency-augmentation)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用状态回放受控拆解多视角增强里的跨视角耦合：七个 LIBERO 任务上外观耦合对扩散策略代价近乎为零（可信区间上端 2.55 个百分点），几何反耦合却掉 3.30 个百分点。**</p>

