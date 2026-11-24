<!-- direction: world_model -->

+ **What Test-Time Training Corrects in Latent World Models? A Slow-Fast Approach**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29453)
![architecture](https://img.shields.io/badge/sft_JEPA_Slow_Fast-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**sft-JEPA 把潜空间世界模型的测试时训练误差拆成跨动作共享的 offset 与动作相关项，发现 AdaJEPA 主要在追 offset：单独加回 offset 就恢复了 91% 的规划增益；据此用每回合重置的快学习器加累积跨回合知识的 LoRA 慢学习器，比 AdaJEPA 高出 4 到 22 点。**</p>

+ **Latent Space Planning with Sequential Monte Carlo**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26706)
![architecture](https://img.shields.io/badge/SMC_Latent_Planning-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_Purdue_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/HrishikeshVish/smcplan)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把潜空间规划重写成由序列蒙特卡洛引导的优化：粒子携带整条动作序列并按中间分布序列演化，再叠加一个由 PDE 导出的 cost-to-go 表达潜空间连通性；在十二个设置上平均成功率 79.8%，固定 150 次迭代预算下比 GD、CEM、MPPI 分别高 28.8、34.5 和 7.4 个百分点。**</p>

+ **SonoAtlasWorld: Anatomy-Grounded Ultrasound World Models for Wide-Range Scanning**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26867)
![architecture](https://img.shields.io/badge/SonoAtlasWorld_Anatomy_Grounded-red)
![task](https://img.shields.io/badge/Neural_Simulator-magenta)
![organization](https://img.shields.io/badge/United_Imaging_Intelligence-green)
[![project](https://img.shields.io/badge/project-blue)](https://sonoatlasworld.github.io/SonoAtlasWorld)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SonoAtlasWorld 把 3D 解剖结构当作世界状态，探头动作只决定解剖与声学可见性，从而在宽范围扫查中保持解剖一致性；配套的 Action-Following Index 在 40 个留出体数据上把肝脏 AFI 做到 0.428（受测基线最高 0.117），并把 40 次重复扫查末端的亮度漂移压低 3.46 倍。**</p>

+ **PACE-WM: Parallel World Modeling with Action History for Visual Planning**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27173)
![architecture](https://img.shields.io/badge/PACE_WM_Action_Memory-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/LHS180/PACE-WM)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**PACE-WM 用循环编码器把已执行动作汇成持久记忆，条件化因果 Transformer 一次并行预测多个未来表征，再用 RAMP 按相对共同参考的最小目标进展给候选动作打分；四个视觉规划任务平均成功率从 95.83% 升到 98.00%，在匹配的 CEM 设置下比自回归 LeWM 快约 7 到 9 倍。**</p>

+ **Non-penetrating World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27963)
![architecture](https://img.shields.io/badge/NoPeWorld_Penetration_Guard-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/Learning_&_Generation_Lab_The_Hong_Kong_Polytechnic_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/yuhangdai427/NoPeWorld)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**交互式视频世界模型普遍会让物体穿墙，NoPeWorld 用 NoPeBench 把这一失效模式量化，并发现冻结 DiT 的隐状态已能预测候选动作是否穿透；于是在其上训轻量安全读头并把不安全动作投影回安全集合，六个模型上的平均违规率从 74% 降到 16%，还能零样本迁移到开放域与移动障碍。**</p>

+ **Two Actions from One State: Fork Futures Teach JEPA World Models to Compare**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28350)
![architecture](https://img.shields.io/badge/Fork_JEPA_Lookback_Head-red)
![task](https://img.shields.io/badge/JEPA-magenta)
![organization](https://img.shields.io/badge/Purdue_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://fork-jepa.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Fork-JEPA 指出 JEPA 用行为数据训练却要比较反事实动作的结构性缺陷：策略在同一状态不变的方向上，动作响应根本不可辨识；它用从同一恢复状态执行两个动作的 fork future 抵消状态项来识别动作响应，再加 lookback 头保住前驱，三个视觉控制任务上比 LeWM 最多提高 14% 规划成功率。**</p>

+ **RecallWorld: Episodic Memory for Persistent Embodied Video World Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28666)
![architecture](https://img.shields.io/badge/RecallWorld_Scenelet_Memory-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/Amazon-green)
[![project](https://img.shields.io/badge/project-blue)](https://recallworld.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RecallWorld 用分集 Scenelet 记忆解决视频世界模型回到旧地就认不出的问题：短多视角片段联合重建保证几何约束，射线提升统一透视与鱼眼输入，检索按覆盖率取互补子集并在融合前先判定可见性；四个数据集上回访 PSNR 比最强基线高 2.6 dB 到 3.9 dB。**</p>

+ **Learning How a Body Moves: Few-Shot Body Inference for Visual World Models of Animated Characters**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28842)
![architecture](https://img.shields.io/badge/InContext_Body_Code-red)
![task](https://img.shields.io/badge/Latent_Dynamics-magenta)
![organization](https://img.shields.io/badge/Department_of_Information_Technology_United_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**两个外表相同但身体动力学不同的卡通角色，会对同一指令给出完全不同的结果，而只看首帧的模型无从分辨；论文提出在上下文世界模型里把角色其他动作片段编码成身体表征并用对比损失分开孪生，配套 144 角色、36 组外观组的 ToonTwins 基准，新形状上正确识别率 85.9%，比无身体摘要基线的 76.7% 明显更高。**</p>

+ **SilentWAM: Planning in the Masked State of a Diffusion World Model**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29125)
![architecture](https://img.shields.io/badge/SilentWAM_Masked_Future-red)
![task](https://img.shields.io/badge/World_Action_Model-magenta)
![organization](https://img.shields.io/badge/Zoox-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**世界动作模型的规划需要未来信息，但生成未来帧意味着额外前向开销；SilentWAM 用帧级掩码世界建模预训练，直接读被掩码未来 token 的隐状态而不解码未来帧，在同一次前向内回归轨迹，单相机下 NAVSIM v1 达 92.0 PDMS、端到端延迟 60.3 ms，消融中碰撞率从 0.18% 降到 0.06%。**</p>

+ **What Should World Models Plan Over? Learning Geometry-Aligned Representations of Body Motion**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29759)
![architecture](https://img.shields.io/badge/MotionPort_Body_Trajectory-red)
![task](https://img.shields.io/badge/Planning_with_World_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Massachusetts-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MotionPort 指出世界模型规划的一个反直觉失配：预测精度高不等于优化能找到成功轨迹，因为规划器搜索的是为预测而学的动作块表征；改为表征身体轨迹并按运动相似性组织搜索空间后，三个骨干、七个设置、四个域的平均到达成功率从 37.9% 提到 87.8%，AntMaze-OGBench 上 72% 对基线 4%。**</p>

+ **One Latent World for Heterogeneous LiDARs: A Scan Pattern Agnostic 4D World Model via Direct Ray Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30007)
![architecture](https://img.shields.io/badge/OneLatentWorld_Ray_Decoder-red)
![task](https://img.shields.io/badge/Driving_Simulation-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://minwoo0611.github.io/OneLatentWorld)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**OneLatentWorld 把场景与传感器观测解耦：解码器直接从空间潜变量预测射线的命中概率与深度，不经中间表面渲染，故一个 KITTI-360 潜变量可被多个异构 LiDAR 共享；在 KITTI-360 与 nuScenes 上，预测帧间配准误差比最优对比模型降低 66% 到 72%，深度误差低 19% 到 28%。**</p>

<!-- direction: embodied_ai -->

+ **SANA-Robot: Efficient World Action Model with Hybrid Memory**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28943)
![architecture](https://img.shields.io/badge/SANA_Robot_Hybrid_Memory-red)
![task](https://img.shields.io/badge/Robot_Foundation_Model-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![project](https://img.shields.io/badge/project-blue)](https://nvlabs.github.io/Sana/Robot)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SANA-Robot 用线性注意力维护定长全局记忆、滑窗 softmax 注意力传播历史，把 4.5B 世界动作模型的记忆覆盖到约一分钟的完整回合且每块成本恒定；RTX 5090 上 FP8 每动作块 135 ms、NVFP4 115 ms，边缘端异步控制 30 Hz，RoboDojo 记忆维度得分 52.73 为同规模最高。**</p>

+ **Foresight Forcing: Learning Spatial Foresight for Robotic Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30963)
![architecture](https://img.shields.io/badge/Foresight_Forcing_Spatial_Transition-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://anson2333.github.io/foresight-forcing)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Foresight Forcing 让世界动作模型学到空间转移：训练时用冻结 VGGT 从对齐的前后观测抽 patch 特征差作稠密几何监督，蒸馏成由当前观测、指令和本体状态细化的空间转移 query，推理时不需未来观测与 3D 教师；RoboTwin 2.0 Full 平均成功率 95.01%，六个真机任务平均分 85.8%。**</p>

+ **RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments**
[![paper](https://img.shields.io/badge/Arxiv_2611.31-blue)](https://arxiv.org/abs/2611.31002)
![architecture](https://img.shields.io/badge/RoboUniverse_Real2Sim_Harness-red)
![task](https://img.shields.io/badge/Physics_Simulator-magenta)
![organization](https://img.shields.io/badge/THU-green)
[![project](https://img.shields.io/badge/project-blue)](https://lab.einsia.ai/robo-universe)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboUniverse-10K 用 Real2Sim 流水线从真实机器人视频造出 10,807 个可自动验证的 Isaac Sim 环境，另留出 500 个专家校验任务做零样本基准；评测 11 个模型时前沿最高 85.8%、开源只有 2.6% 到 10.0%，17K 条多轮轨迹全参微调后成功率从 0.8% 升到 21.2%。**</p>

+ **Entangle: Scaling Human-Video In-Context World-Action Models across Unseen Tasks and Contexts**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28732)
![architecture](https://img.shields.io/badge/Entangle_Context_World_Action-red)
![task](https://img.shields.io/badge/Imitation_Learning-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Entangle 用单段人类视频作为上下文驱动未见任务，靠两步摆脱捷径：用视频到视频生成加真人同步录制把人与机器人轨迹在时序上对齐，再用任务内对比目标把配对轨迹与其他同任务执行区分开；不做任务微调，六个未见任务平均 83.5/100，RoboTwin 七个未见任务平均成功率 69.5%，比 Zero-WAM 高 22.6 点。**</p>

+ **FunGrasp-Zero: Field-Conditioned Graph Attention Policy for Zero-Shot Cross-Embodiment Dexterous Functional Grasping**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29195)
![architecture](https://img.shields.io/badge/FunGrasp_Zero_Field_GAT-red)
![task](https://img.shields.io/badge/Dexterity-magenta)
![organization](https://img.shields.io/badge/Sun_Yat-sen_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://linyh0525.github.io/FunGrasp-Zero/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**灵巧手形态差异让功能性抓取难以跨手泛化，FunGrasp-Zero 改用物体中心、跨形态一致的接触图，经形态映射生成势场引导，由图注意力策略协调多指并用势场奖励惩罚非目标碰撞；四种手联合训练后在五只未见手的仿真上平均成功率 86%，部署到四只未见真机手平均 80%。**</p>

+ **SparQ4D: Learning to Act through Sparse 4D Queries**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29682)
![architecture](https://img.shields.io/badge/SparQ4D_Sparse_Query_Decoder-red)
![task](https://img.shields.io/badge/Scene_Reconstruction-magenta)
![organization](https://img.shields.io/badge/ShanghaiTech_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**稠密预测整个未来太贵，SparQ4D 在预训练策略的中间表示上挂轻量 query 解码器，用统一接口把深度、点运动、多视角对应和手眼关系都变成可回答的稀疏问题，训练时只采样少量查询、推理时解码器直接摘掉；以 π0.5 为底座时训练快 3 到 5 倍、推理快 1.7 到 6.6 倍，参数约为 WAM 基线的四分之一。**</p>

+ **Into My Arms: Structured reinforcement learning for autonomous transport of objects and humans**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29771)
![architecture](https://img.shields.io/badge/Into_My_Arms_Structured_RL-red)
![task](https://img.shields.io/badge/Humanoid_Control-magenta)
![organization](https://img.shields.io/badge/University_of_Edinburgh-green)
[![project](https://img.shields.io/badge/project-blue)](https://elle-miller.github.io/into_my_arms)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Into My Arms 用稀疏交互边、交互门控传输和提示物体路径三件套为全身人形 RL 补上刚好够用的结构，让策略仍可自由发现操作方式；其核心展示是首个执行中无人干预的人形机器人床到轮椅人偶转移，人偶高 155 厘米重 15 千克，训练在单张消费级 GPU、2048 个并行环境下不到一小时完成。**</p>

+ **Hierarchical Reasoning Action Head for Tiny Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29813)
![architecture](https://img.shields.io/badge/HR_AH_Hierarchical_Action_Head-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Department_of_Computer_Science_University_of_Alabama_at_Birmingham-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VLA 缩小后就没时间推理，HR-AH 在紧凑动作头里维护两个不同频率的潜状态：低层由动作 token 与本体感觉高频驱动，高层由视觉理解与指令慢速驱动，二者通过嵌套推理循环交换信息；所有迭代都在单次骨干前向之后完成，22.5M 参数头比 RD-VLA 小 3 到 4.3 倍，LIBERO 成功率 97.0%，延迟为同类最低。**</p>

+ **RoboThink: Let the Agent Think, Let the Policy Act**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30111)
![architecture](https://img.shields.io/badge/RoboThink_Agent_Policy_Split-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Tulane_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://Robo-Think.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoboThink 让推理智能体只负责想、机器人策略负责动：指令通道让策略撤销自身动作改目标，反馈通道用智能体标注的 DAgger、角色 token 与反事实反馈教策略怎么动；LIBERO 上未知恒定漂移下成功率从 0.09 升到 0.87，智能体单独行动要 2.1 分钟每成功而它只需 55 秒。**</p>

