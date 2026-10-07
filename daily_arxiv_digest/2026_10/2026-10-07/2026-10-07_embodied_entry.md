+ **World Models' Last Exam in Physics**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08791)
![architecture](https://img.shields.io/badge/Measurement_Based_Physics_Benchmark-red)
![task](https://img.shields.io/badge/World_Model_Evaluation-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**视频世界模型能生成视觉上可信却物理不自洽的序列，这让人担心它们用于具身系统的预测与规划是否可靠。现有评测多依赖模型判断或参考视频，而直接的物理测试又主要限于力学。这篇提出一个基于实测的基准，含 40 个受控任务。**</p>

+ **DepthWorld: 3D World Model for Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08780)
![architecture](https://img.shields.io/badge/Depth_Conditioned_3D_World_Model-red)
![task](https://img.shields.io/badge/Robot_Manipulation_World_Model-magenta)
![organization](https://img.shields.io/badge/Czech_Institute_of_Informatics_Robotics_and_Cybernetics-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**世界模型为机器人提供了传统模拟器之外的数据驱动替代方案，可用于策略评估、改进与规划，而这些用途都依赖忠实的三维几何。但现有基于视频的世界模型只在 RGB 上训练，产出的 rollout 逐帧看起来正确，却无法组合成一个一致的三维世界。**</p>

+ **Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07540)
![architecture](https://img.shields.io/badge/JEPA_Inverse_Dynamics-red)
![task](https://img.shields.io/badge/World_Model_Control-magenta)
![organization](https://img.shields.io/badge/Columbia_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**机器人系统常存在不稳定模态，沿其方向的小扰动若无反馈修正就会无界增长。从高维视觉观测控制这类系统，要求表征保留这些模态。JEPA 提供了学习此类表征及其动力学的自然框架。**</p>

+ **Parallel Predictive World Models for Accurate and Efficient Long-Horizon Planning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08627)
![architecture](https://img.shields.io/badge/Parallel_Predictive_World_Model-red)
![task](https://img.shields.io/badge/Long_Horizon_Planning-magenta)
![organization](https://img.shields.io/badge/1Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**长时程世界模型规划通常依赖自回归 rollout，预测状态被反复回灌模型。这保住了时间结构，却产生了与时程长度成正比的串行路径，且后期预测暴露在递归的解码状态反馈下。PPWM 并行预测有限时程轨迹，同时保留未来表示之间的因果交互。**</p>

+ **VOMMI: Collecting and Leveraging Portable Demonstrations for Mobile Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08220)
![architecture](https://img.shields.io/badge/VO_Conditioned_Motion_Modeling-red)
![task](https://img.shields.io/badge/Mobile_Manipulation-magenta)
![organization](https://img.shields.io/badge/Zhejiang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**便携式移动操作演示可以缓解具身智能的数据稀缺，但从 RGB 观测中获得可靠、低成本、无需机器人的运动监督仍很困难。遥操作或专用硬件成本高，而直接使用估计的视觉里程计轨迹会因累积漂移和运动监督不完美而引入不一致。**</p>

+ **Commit While Futures Agree: Consequence-Aware Adaptive Action Chunking for Robot Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07949)
![architecture](https://img.shields.io/badge/Consequence_Aware_Action_Chunking-red)
![task](https://img.shields.io/badge/Robot_Manipulation-magenta)
![organization](https://img.shields.io/badge/HKUST_Guangzhou-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**动作分块策略预测多步控制序列，但一个基本问题悬而未决：重新规划前应当执行预测动作块的多大部分？现有系统通常执行固定长度前缀，隐含假设执行时程在不同状态下同样可信；一些自适应方法用预测动作的相似性或稳定性估计时程。**</p>

+ **ViDAL: A Visual Dynamics-Grounded Action Latent Space for Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08150)
![architecture](https://img.shields.io/badge/Visual_Dynamics_Action_Latent-red)
![task](https://img.shields.io/badge/Vision_Language_Action_Model-magenta)
![organization](https://img.shields.io/badge/Alibaba_Group-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VLA 已成为机器人策略学习的中心范式，动作以原始动作块、离散动作 token 或连续动作 latent 三种形式预测。但现有动作表示主要建模动作轨迹，对动作诱发的视觉动力学考虑有限。ViDAL 把连续动作 latent 锚定到动作的未来视觉动力学上。**</p>

+ **SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.07652)
![architecture](https://img.shields.io/badge/Large_Scale_Synthetic_Pretraining-red)
![task](https://img.shields.io/badge/Articulated_Object_Manipulation-magenta)
![organization](https://img.shields.io/badge/Institute_of_AI_China_Telecom-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**与铰接物体交互是具身系统的必备能力，但因涉及精确接触与约束跟随运动，大规模真机演示难以采集。仿真虽是替代方案，既有合成数据只覆盖有限的铰接物体类别，而通用合成管线缺少对部件级语义与铰接约束的显式设计。**</p>

+ **PEARS: Physical-Prior-Guided Efficient Adaptation via Failure Reasoning and Diffusion Steering for Tactile Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08784)
![architecture](https://img.shields.io/badge/Physics_Prior_Hybrid_RL-red)
![task](https://img.shields.io/badge/Tactile_Manipulation-magenta)
![organization](https://img.shields.io/badge/University_of_Hong_Kong-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**预训练机器人策略在部署时遇到分布外条件会严重退化，因此需要通过真实交互做后训练；但基于强化学习的后训练需要大量环境交互，在操作任务里每次试验都可能缓慢、昂贵或具破坏性。PEARS 用物理先验引导的混合强化学习框架应对这一点。**</p>

+ **VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.08133)
![architecture](https://img.shields.io/badge/Action_Consistent_Token_Pruning-red)
![task](https://img.shields.io/badge/Vision_Language_Action_Model-magenta)
![organization](https://img.shields.io/badge/2Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VLA 模型因每个控制步都要处理长 token 序列而计算开销高，限制了实时部署。视觉 token 剪枝是直接的解法，因为视觉 patch 占输入序列主体且冗余大。但既有方法要么依赖注意力分数、运动阈值等间接的训练无关启发式，要么需要昂贵的微调。**</p>

