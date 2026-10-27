# 2026-10-27 - 具身智能与世界模型 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **The Language of Deformation: Semantic Failure Analysis as a Prerequisite for Dexterous Manipulation of Deformable Objects**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35103)
![architecture](https://img.shields.io/badge/Semantic_Failure_Analysis-red)
![task](https://img.shields.io/badge/Manipulation-magenta)
![organization](https://img.shields.io/badge/Clermont_Auvergne_INP-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出刚性物体的灵巧操作已可落地，而可变形物体（线缆、布料）因屈曲、塑性变形与撕裂等多样失效模式长期受阻；本文把语义失效分析定义为其前置环节，给出关键组件与概念验证实验。**</p>
+ **Learning Force-Reactive Humanoid Loco-Manipulation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35862)
![architecture](https://img.shields.io/badge/FLORE_Force_Reactive-red)
![task](https://img.shields.io/badge/Robot_Learning-magenta)
![organization](https://img.shields.io/badge/Amazon_FAR-green)
[![project](https://img.shields.io/badge/project-blue)](https://louis-leee.github.io/FLoRe/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FLORE 用两把力感知 UMI 式手持夹爪与可穿戴追踪采集无机器人演示，训练同时输出动作与双手力指令的扩散策略，再由混合柔顺全身控制器执行；三个富接触任务成功率 80%，对照的位置-only 策略仅 26.7%。**</p>
+ **Zero-HLM: Generalizable Humanoid Loco-Manipulation without Real Robot Data**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35075)
![architecture](https://img.shields.io/badge/Zero_HLM-red)
![task](https://img.shields.io/badge/Sim_to_Real-magenta)
![organization](https://img.shields.io/badge/Beijing_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://young-bit.github.io/zero-hlm/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Zero-HLM 用高斯引导的 agentic real-to-sim 重建加运动-环境协同适应，把手机拍摄与仿真演示转成 4,800 条物理验证的人形 loco-manipulation 演示；仿真训练的 GR00T N1.7 整任务成功率 66.7%，泛化配置汇总成功率从 23% 升到 69%。**</p>
+ **Adapt for Planning, Not just Prediction: Optimistic Test-Time World Model Adaptation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35636)
![architecture](https://img.shields.io/badge/OpTTA_Optimistic_Adaptation-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/Texas_A&M_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**OpTTA 指出纯预测目标的测试时自适应会让模型「对错误的动作预测得很准」，因此在预测损失之外加入规划器候选 rollout 的到达目标代价；操作、到达与导航的分布偏移任务上，规划成功率平均提升 13.5 个百分点，而纯预测目标仅 6.9。**</p>
+ **Differentiable Contact Dynamics for Legged Locomotion: Policy Learning and Contact-Implicit Trajectory Optimization**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35852)
![architecture](https://img.shields.io/badge/Differentiable_Contact_Dynamics-red)
![task](https://img.shields.io/badge/Neural_Simulator-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![project](https://img.shields.io/badge/project-blue)](https://diffcontact.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为摩擦接触提出跨接触模式连续的光滑解析梯度：只在反向传播时替换敏感度、前向硬接触求解保持不变；用 10 万样本、桌面 PC 不到 2 分钟训得的策略无需微调即可上真机抗推越障。**</p>
+ **Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34674)
![architecture](https://img.shields.io/badge/OSMA_Bench-red)
![task](https://img.shields.io/badge/Visual_Navigation-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**OSMA-Bench 用只改障碍物类型的空间配对场景集评测家居导航安全，并提出语义敏感度指数；结果显示 VLM 与 VLA 策略虽能分清障碍物安全相关性，却无法让间距与速度体现该差异，暴露出语义到运动的落地断层。**</p>
+ **Robot-Aligned 3D Gaussian Splatting for Precise Reaching with Wrist-Camera VLA Policies**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35626)
![architecture](https://img.shields.io/badge/PrecisionReach_3DGS-red)
![task](https://img.shields.io/badge/VLA_Model-magenta)
![organization](https://img.shields.io/badge/Texas_A&M_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://001-wang.github.io/PrecisionReach-GS/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 3DGS 重建真实工作空间并从机器人对齐位姿渲染腕部相机观测，配对结构化触及轨迹微调 VLA 并加指令条件化触及验证器；π0.5 用 1,500 条生成轨迹达成 80.0% 精确触及成功率，高于 150 条遥操作演示的 58.7%。**</p>
+ **Video World Models Need Predictable Latents**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.34663)
![architecture](https://img.shields.io/badge/Predictable_Latent_Video_WM-red)
![task](https://img.shields.io/badge/Video_as_World_Model-magenta)
![organization](https://img.shields.io/badge/New_York_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**为视频世界模型的自编码器加入时间性表征目标与过去条件化解码器，让隐空间几何同时服务动力学与重建；在同等训练预算下推理最多便宜 5 倍、训练快 7 倍，分布外与长程场景的像素与感知误差降低 15%–24%。**</p>
+ **WorldPager: Zero-Stall Tiered Memory for Long-Horizon World Models on a Single Consumer GPU**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35529)
![architecture](https://img.shields.io/badge/WorldPager_NVMe_Tier-red)
![task](https://img.shields.io/badge/World_Model-magenta)
![organization](https://img.shields.io/badge/University_of_Electronic_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WorldPager 证明交互式世界模型的 KV 记忆是容量受限且访问集合可提前获知（相机位姿即输入），据此把 int4 KV 存入 GPU/DRAM/NVMe 层级并零停顿预取，在单张 RTX 4090 上连续生成 37.5 分钟视频、约 9.5 FPS 且主机内存恒定。**</p>
+ **Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.35817)
![architecture](https://img.shields.io/badge/ZAP_Sim_Trained_Agent-red)
![task](https://img.shields.io/badge/Embodied_Agent-magenta)
![organization](https://img.shields.io/badge/Luma_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ZAP 用预训练 27B 模型加仿真任务上的 SFT 与 GRPO、配合简单工具 harness，在零真机数据下把真实机器人任务成功率做到 96.7%，比 GPT-6 Astra 快 3 倍、便宜 17 倍，并泛化到全新物体、本体与目标（Franka 上 55.9%）。**</p>