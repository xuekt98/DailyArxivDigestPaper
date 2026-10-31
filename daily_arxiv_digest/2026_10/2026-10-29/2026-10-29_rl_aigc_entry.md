# 2026-10-29 - 生成式内容模型强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **Multi-Draft On-Policy Distillation for Diffusion Drafters**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37778)
![architecture](https://img.shields.io/badge/MDraft_MultiDraft_OnPolicy_Distillation-red)
![task](https://img.shields.io/badge/RL_for_Diffusion-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MDraft 指出并行草稿使 verifier 目标随已采前缀漂移，改为采样多个草稿块并聚合各前缀下的全词表 verifier 条件分布；只改训练不改架构，接受长度超过预训练水平，也长于既有蒸馏方法。**</p>
+ **Estimating Implicit Expected Log Density Ratios**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38151)
![architecture](https://img.shields.io/badge/ELDR_Expected_Log_Density_Ratio-red)
![task](https://img.shields.io/badge/Preference_Alignment-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出 expected log density ratio 这一被第三个测度积分的密度比概念，证明有限样本下的根本局限，指出朴素 DRE 方法并不适用，并给出让训练数据覆盖积分分布的简单改法以降低估计误差。**</p>
+ **MiniMMD: Minimization of MMD for Sampling, Inference and Integration**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38122)
![architecture](https://img.shields.io/badge/MiniMMD_Minimum_MMD_Framework-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/University_College_London-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MiniMMD 学位论文把数值积分、采样、生成建模与统计推断统一为在受限候选分布族上最小化 MMD，强调 MMD 既是统计上有意义的距离，也是可用于设计实用算法的可优化目标。**</p>
+ **AtomSteer: Test-Time Constraint Steering for Atomistic Generative Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38517)
![architecture](https://img.shields.io/badge/AtomSteer_TestTime_Structural_Projection-red)
![task](https://img.shields.io/badge/Classifier_Guidance-magenta)
![organization](https://img.shields.io/badge/Massachusetts_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AtomSteer 在采样过程中用有界局部投影、图刚性立体化学变换与周期对称性投影纠正原子结构预测，只接受改善约束满足度的更新；在 FlowMM、ET-Flow 与 Boltz-2 上无需重训即提升对称性与立体化学准确率。**</p>
+ **Finite-Step Geometry of Marginal-Preserving Velocity Fields in Generative Flows**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.37936)
![architecture](https://img.shields.io/badge/Projected_Modified_Equation_Finite_Step_Analysis-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/FusionBrain_Lab-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文在固定边缘路径与数值方法的前提下刻画生成流的有限步非等价性，用修正后的修正方程给出更高收敛阶的充分条件，并导出仿射分布下的谱障碍与最近可达 Wasserstein 误差，还构造保持边缘路径的 skew-score 扰动。**</p>
+ **Beyond Reachability: When Edit Order Preserves Couplings in Graph Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38486)
![architecture](https://img.shields.io/badge/EditOrder_Coupling_Recovery_GraphFM-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_Polytechnic_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文给出图上 flow matching 的端点耦合可恢复性精确判据：通往不同目标的路径不共享图状态时可达时钟误差下界，并导出有限状态路由表述与带恢复证书的保合法调度，还证明边缘误差相同也可能出现成对误差的尖锐分离。**</p>
+ **Logical Guidance of Stochastic Interpolants**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38648)
![architecture](https://img.shields.io/badge/LOGSI_ScoreReequilibration_LogicalGuidance-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/NEC_Laboratories_Europe-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文证明否定与析取在任何 interpolant 上都能精确组合条件 velocity，而合取只在高斯路径上精确、一般情形会引入 drift-interaction error；LOGSI 用 score 再平衡与高斯路径 velocity 规则兜底，在图像迁移与分子编辑上同预算下更符合规则。**</p>
+ **WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38352)
![architecture](https://img.shields.io/badge/WeVisCut_ScriptToVideo_Agent_Policy-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/Xidian_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://tencent.github.io/WeVisCut)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WeVisCut 把工具执行与策略学习连成一体，用 editing inversion 加 verified replay 的四阶段管线从 3750 个成品视频合成 13 万条训练样本，训出单个 9B 策略，每成功输出分钟生成的 token 约为 Claude Opus 5 的三分之一。**</p>
+ **Compositional Diffusion Planning with Chunk Selection and Reachability Measure**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38291)
![architecture](https://img.shields.io/badge/SCD_Reachability_Selective_Compositional_Diffuser-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Seoul_National_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SCD 用自监督学到的 reachability 判别器给相邻 chunk 是否可达打分，据此建图遍历出有效路线，再生成桥接轨迹细化合成结果，在 OGBench stitching 任务上减少 mode-averaging 并在 HumanoidMaze-Large 与 Giant 达到最好成功率。**</p>
+ **Structure-retained low-rank adapters for weather synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.38413)
![architecture](https://img.shields.io/badge/StructureLoRA_SDXL_Weather_Synthesis-red)
![task](https://img.shields.io/badge/Classifier_Guidance-magenta)
![organization](https://img.shields.io/badge/Unknown-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**作者先分析 SDXL 注意力块定位结构信息被处理的位置，再为对应块学习结构保持的 LoRA 矩阵做天气合成，无需 ControlNet 等外部条件即可在提升真实感的同时保住结构，为室外视觉提供高保真训练数据。**</p>
