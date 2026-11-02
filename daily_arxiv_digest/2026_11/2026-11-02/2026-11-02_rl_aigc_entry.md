# 2026-11-02 - 生成式内容模型强化学习 条目目录（10 篇）

每条一行，shields.io 徽章格式；task 徽章取自该线专属词表。

+ **A Better Critic Matters for Distribution Matching Distillation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42135)
![architecture](https://img.shields.io/badge/STAC_JointScaling_DMD_Critic-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/Adobe-green)
[![project](https://img.shields.io/badge/project-blue)](https://peppaking8.github.io/critic-matters/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**系统研究 DMD 中 critic 需要多大容量与多少信息：七种 SiT 尺寸实验显示小 critic 配大教师会崩塌或变差，据此提出 joint scaling 与按生成步条件化的 STAC，在 ImageNet、SDXL、FLUX.2 与 Wan2.1 上一致提升。**</p>
+ **Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41949)
![architecture](https://img.shields.io/badge/GeoFSRL_PolicyGeometry_ClosedForm-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/Beihang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Geo-FSRL 把少步流模型的随机策略选择归结为一个几何因子：最小化该因子即可最小化任意速度更新诱导的条件 KL，并给出唯一闭式最优解与闭式的策略梯度与 KL 权重，4 步设定下奖励高于 Flow-GRPO 与 Flow-CPS。**</p>
+ **Latent Reasoning in Continuous Space for Unified Multimodal Models**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.42149)
![architecture](https://img.shields.io/badge/LARC_LatentReasoning_InformationGainRL-red)
![task](https://img.shields.io/badge/RL_for_Flow_Matching-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LARC 针对推理在离散 token 空间、图像生成在连续空间的模态错配，让统一多模态模型在连续隐状态上做隐式推理，并以信息增益与崩塌预防两项奖励做无真值 RL，在 GenEval 上超过 BAGEL 7 个百分点并具备并行与串行测试时扩展能力。**</p>
+ **Coarse-Graining Optimal Transport for Rollout-Free Post-Training of Flow Matching**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41269)
![architecture](https://img.shields.io/badge/ReCouple_CoarseGrained_OTCouping-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/KTH_Royal_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 ReCouple 系列：用分块分配构造粗粒度 OT 耦合以研究 rollout-free 的 flow matching 后训练，ReCouple+ 提高源分辨率逼近半离散 OT、ReCouple++ 再加空间正则化，并厘清耦合最优性、可实现性与 NFE 之间的取舍。**</p>
+ **Scout-Refine-Correct: Teaching Flow Models to Refine Their Own Samples**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41598)
![architecture](https://img.shields.io/badge/SRC_ScoutRefineCorrect_SelfConditioning-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/FusionBrain-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Scout-Refine-Correct 训练配方让 flow matching 生成器具备真正的推理期精修能力：先做 K 步 scout rollout 外推样本估计再回灌自条件，在 ImageNet-256 上把 LightningDiT-B 的 FID 从约 14.5 降到约 7.26 且不需校验器与奖励信号。**</p>
+ **MATS: A Multi-Agent Framework for Controllable and Reflective Tumor Synthesis**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41159)
![architecture](https://img.shields.io/badge/MATS_MultiAgent_Reflective_TumorSynthesis-red)
![task](https://img.shields.io/badge/Classifier_Guidance-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MATS 先在细粒度属性空间上画像目标疾病的形态分布并据此规划生成，再用两阶段扩散合成肿瘤掩膜与纹理，闭环机制在三个检查点校验属性对齐，同时贡献含 740 例 CT 的 PNETS 数据集。**</p>
+ **StrictPRMBench: A Replayable Evaluation Benchmark for Auditing Fixed-Score PRM Aggregation**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41333)
![architecture](https://img.shields.io/badge/StrictPRMBench_Reducer_Audit_Replayable-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Independent_Researcher-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**StrictPRMBench 把 PRM 分数聚合规则当作独立评估对象：固定题池、打分证据与删除干预，在 14 个单元里乘积聚合的选择不稳定性都高于几何平均（等单元差 +0.0965，区间 [0.0846, 0.1086]），并提供可重放记录。**</p>
+ **When Does Test-Time Search Help World Action Models? An Empirical Audit of Candidate Selection and Simulator Integrity**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41970)
![architecture](https://img.shields.io/badge/TestTimeSearch_PremiseFirst_Audit-red)
![task](https://img.shields.io/badge/Best_of_N-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**对 Cosmos Policy 与 RoboCasa 上的测试时搜索做前提优先审计：干净数据上学到的价值选择器比随机差 1.66 个百分点、82% 状态候选结果相同，token 剪枝最多 47% FLOPs 但端到端加速仅 1.15 倍。**</p>
+ **ART of PIV: Agentic Real-Time Particle Image Velocimetry for Active Flow Control**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41304)
![architecture](https://img.shields.io/badge/ARTofPIV_Agentic_PipelineSelection-red)
![task](https://img.shields.io/badge/Reward_Model_Image-magenta)
![organization](https://img.shields.io/badge/ETH_Zurich-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ART of PIV 让学习到的 agent 按测量目标为每一对图像挑选 PIV 估计流程，在同等速度下把端点误差降低 12.2–22.4%，并直接在水上训练 DreamerV3 控制器跟踪流体陀螺尾流。**</p>
+ **OT-CAL: Optimal-Transport-Guided Adaptive Sample Selection for Efficient Visual Learning**
[![paper](https://img.shields.io/badge/Arxiv_26.10-blue)](https://arxiv.org/abs/2610.41677)
![architecture](https://img.shields.io/badge/OTCAL_Curriculum_SampleSelection-red)
![task](https://img.shields.io/badge/Reward_Weighted_Regression-magenta)
![organization](https://img.shields.io/badge/Purdue_University_Fort_Wayne-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**OT-CAL 用五个信息量特征与最优传输匹配为每个样本分配选择权重，并由被选样本反向更新课程向量，形成自动演化的采样偏好，在三个视觉基准上比 AdaSelection 高 1.3–2.1 个点且训练快 1.18–1.24 倍。**</p>
