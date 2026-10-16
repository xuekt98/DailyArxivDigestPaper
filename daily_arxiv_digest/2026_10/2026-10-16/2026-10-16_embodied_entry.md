+ **What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21915)
![architecture](https://img.shields.io/badge/Supervision_Target_Reassessment-red)
![task](https://img.shields.io/badge/Vision_Language_Action_Model-magenta)
![organization](https://img.shields.io/badge/1Renmin_University_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视觉语言动作策略通常以动作预测为主要监督信号，因为机器人最终执行动作。latent-action（LA）与未来视觉（FV）预测等辅助目标常被加入以改进策略学习，然而它们会与动作预测**竞争表示容量**（摘要在此处截断）。**</p>

+ **Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22342)
![architecture](https://img.shields.io/badge/Spatially_Aligned_Tactile_Pretraining-red)
![task](https://img.shields.io/badge/VTLA_Model-magenta)
![organization](https://img.shields.io/badge/Tian_Nian1,∗,_Zijian_Cai1,_Kehe_Ye1,_Chenze_Yu1,_Wenxuan_Zhu1,_Eric_J._Chen1,_Yan_Qin4,_Yue_Chen5,-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**通才机器人策略受益于大规模视觉预训练，但在接触丰富的灵巧操作上仍显吃力——力、顺应性与初始滑移难以从图像中观察。Spark-0 是一个空间对齐的视觉-触觉-语言-动作模型，以两种互补方式使用触觉（摘要在此处截断）。**</p>

+ **Dexterity from Supervised Play**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22340)
![architecture](https://img.shields.io/badge/Supervised_Play_Then_Autonomous_Play-red)
![task](https://img.shields.io/badge/Dexterous_Manipulation_Data-magenta)
![organization](https://img.shields.io/badge/1Amazon_Frontier_AI_&_Robotics_(FAR).-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**机器人如何自主采集学习灵巧操作所需的接触丰富经验？DSP（Dexterity from supervised play）提出一个框架：机器人通过行为克隆从**几分钟人类玩耍**中学习一个玩耍策略，然后自主部署去采集**数小时**交互数据来训练（摘要在此处截断）。**</p>

+ **MAIA: Anticipating Interaction Anomalies in Contact-Rich Manipulation via Multimodal World Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21686)
![architecture](https://img.shields.io/badge/Multimodal_Anomaly_Anticipation-red)
![task](https://img.shields.io/badge/Contact_Rich_Monitoring-magenta)
![organization](https://img.shields.io/badge/1School_of_Artificial_Intelligence,_Shanghai_Jiao_Tong_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**可靠的接触丰富操作要求足够早地检测执行偏差以便纠正。然而多数监控方法是**被动的**——只在异常变得可观测之后才识别。预判异常很困难，因为视觉观测只部分揭示物理交互（摘要在此处截断）。**</p>

+ **VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21985)
![architecture](https://img.shields.io/badge/Test_Time_Verification-red)
![task](https://img.shields.io/badge/Flow_VLA_Policy-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**基于流的视觉语言动作策略本质上是**随机的**：不同噪声种子会在同一观测下产生质量各异的动作块。然而在测试时，策略通常提交单个样本而没有对其质量的显式估计。在细粒度操作中，执行一个次优……（摘要在此处截断）。**</p>

+ **Fast-VLA: You Only Think Once for Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21389)
![architecture](https://img.shields.io/badge/Once_Per_Episode_Context-red)
![task](https://img.shields.io/badge/VLA_Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/1Huawei_Technologies_Co.,_Ltd-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视觉语言动作策略通常把一个数十亿参数模型放在反馈回路内，在每次预测新动作块时**反复重算任务上下文**。然而任务理解的变化远慢于机器人状态。Fast-VLA 在每个 episode 只调用一次冻结的 4B VLM（摘要在此处截断）。**</p>

+ **Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22363)
![architecture](https://img.shields.io/badge/Tri_Mode_World_Action_Model-red)
![task](https://img.shields.io/badge/Egocentric_Dexterous_Manipulation-magenta)
![organization](https://img.shields.io/badge/1_HKUST_(GZ)-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**P³-WAM 是面向第一人称灵巧操作的统一世界动作模型，通过三种互补模式学习三维感知、动作条件预测与目标导向规划：Perceive 从视频重建关节手部运动与相机轨迹；Predict 生成视觉……（摘要在此处截断）。**</p>

+ **MuSTMM: Learning Sound-Triggered Mobile Manipulation across Multiple Scenes**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21429)
![architecture](https://img.shields.io/badge/Sound_Triggered_Mobile_Manipulation-red)
![task](https://img.shields.io/badge/Mobile_Manipulation-magenta)
![organization](https://img.shields.io/badge/University_of_Macau-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**声音触发的移动操作要求机器人对声音事件作出反应：导航到相关物体并执行恰当的物理交互。既有 STMM 评测主要在有限的建筑结构内变化物体布局，对未见场景的挑战探索不足（摘要在此处截断）。**</p>

+ **Evo-DexBench: Benchmarking Generalization across Related Tasks for Dexterous Manipulation** `[wild-card]`
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.21180)
![architecture](https://img.shields.io/badge/Related_Task_Generalization_Benchmark-red)
![task](https://img.shields.io/badge/Dexterous_Manipulation_Benchmark-magenta)
![organization](https://img.shields.io/badge/1School_of_AI,_Shanghai_Jiao_Tong_University;_2Nanjing_University;_3Central_South_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**通用灵巧操作要求策略把知识从相关任务迁移到仅有少量目标演示的新任务。既有基准往往提供**过多**目标演示，且未控制源任务与目标任务之间的差异，因此无法清晰地区分（摘要在此处截断）。**</p>

+ **Velox: Spatial Memory Makes World Models Efficient**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.22311)
![architecture](https://img.shields.io/badge/Spatial_Memory_Compression-red)
![task](https://img.shields.io/badge/Video_World_Model-magenta)
![organization](https://img.shields.io/badge/National_University_of_Singapore-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频世界模型把动作与相机运动转为长视觉 rollout，使视频成为交互式仿真的自然接口。这种交互要求响应式生成，然而连贯的 rollout 必须**保留已经生成过什么的视觉记忆**。分块视频扩散模型通常把这一上下文保存在……（摘要在此处截断）。**</p>

