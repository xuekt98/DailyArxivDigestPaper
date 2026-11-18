<!-- direction: llm_core -->

+ **Computed Permutation Trellis Coding: Near-Optimal Quantization from Two Multiplications and a 64-Byte Table**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22019)
![architecture](https://img.shields.io/badge/Computed_Permutation_Trellis_Coding-red)
![task](https://img.shields.io/badge/Quantization-magenta)
![organization](https://img.shields.io/badge/Amazon_Annapurna_Labs-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**CPTC 用两次乘法和一张 64 字节查表实现 1 至 6 bit 的 trellis 解码，4 bit 时距信息论理想仅差 0.07 bit，并在 Llama 3.1 8B/70B Instruct 权重量化上把对 QTIP 的 KL 散度最多压低 27%。**</p>

+ **The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22947)
![architecture](https://img.shields.io/badge/LARA_Plus_Importance_Sampling-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/Concordia_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/firatoncel/KernelRealityCheckNeurIPS2026)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以内存、速度与蒸馏质量三条线基准评测 kernelized attention：训练与 ViT 上 FlashAttention 反而更快更省，现有方法在统一蒸馏下落后 softmax 2 到 10 分，LARA++ 用自适应重要性采样最多追回 99%。**</p>

+ **Language Models Can Rewrite Their Own Weights**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21885)
![architecture](https://img.shields.io/badge/Self_Rewriting_Weights-red)
![task](https://img.shields.io/badge/Model_Editing-magenta)
![organization](https://img.shields.io/badge/UIUC-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**27B 模型用自身推理、无梯度无训练地改写权重，在 490 道未见题上提升 6.6 分；还能自行定位并重写被损坏的矩阵，把六个图像基准从 7% 修到 70%，达到完好模型 83% 的水平。**</p>

+ **Conserved Verdicts, Drifting Commitments: Identifying Harmful Overthinking**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21946)
![architecture](https://img.shields.io/badge/Commitment_Verdict_Gap-red)
![task](https://img.shields.io/badge/Test_Time_Compute-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用「承诺概率 vs 判决概率」拆解有害过度思考：在 MATH-500 的 379 个已答对检查点上继续推理平均掉 3.6 分，oracle 停止规则在 1.5B 与 7B 上最多也只赚 1.8 与 2.5 分。**</p>

+ **VisHead-Spec: Head-Routed Visual Attention for Multimodal Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21839)
![architecture](https://img.shields.io/badge/VisHead_Spec-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/Meta-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**按 KV 头路由视觉注意力：草稿模型 40 个头里只放 8 个读图，接受长度与 DSpark 差距不超过 0.3%，batch 64 时相对自回归的吞吐增益达 16.0%，高于 DSpark 的 9.5%。**</p>

+ **DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21925)
![architecture](https://img.shields.io/badge/Mixture_of_Features_Attention-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/University_of_Virginia-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**诊断并行草稿模型的三处特征编码缺陷（residual mixing、无记忆、层采样不均），提出带拒绝记忆的 MoFA；DNeo 在 H100 上以 Qwen3-4B 取得 DFlash-2 的 1.3 倍速度且草稿足迹不变。**</p>

+ **DiscoveryAgent: A Framework for Scientist-centric Agentic AI**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21950)
![architecture](https://img.shields.io/badge/Discovery_Agent-red)
![task](https://img.shields.io/badge/Agent-magenta)
![organization](https://img.shields.io/badge/Stanford_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**面向科学家的 agent 系统：自主调查之外保留假设改写权与检查点审计，与审计代理协作的科学家发现的有效错误是纯人工的 14 倍，蛋白变体效应预测在 106 个 ProteinGym 基线中仅次于一个。**</p>

+ **Beyond Bitwidth: Deployment-Constrained Mixed-Precision Quantization for Multilingual LLM Inference on NVIDIA Blackwell**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21974)
![architecture](https://img.shields.io/badge/Mixed_Precision_Deployment_Config-red)
![task](https://img.shields.io/badge/Quantization-magenta)
![organization](https://img.shields.io/badge/ThakiCloud-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 B200 与 vLLM 上按预注册门槛评估 Qwen3-8B 的 144 个融合线性模块，最终以 16 位激活加 98 个 NVFP4、46 个 INT8 模块通过 5168 条 FINAL-81 验收，加载 5.917 GiB、TPOT 比 0.939。**</p>

<!-- direction: vlm_core -->

+ **CueClash: Frontier Vision-Language Models Judge 3-D Relations Close to the Picture Plane**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22180)
![architecture](https://img.shields.io/badge/Cue_Clash_Benchmark-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/Scale_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用渲染场景把五种三维关系的二维线索正确率压到恰好 50%，测出前沿 VLM 的捷径差距高达 18 到 37 个百分点，而给定地面坐标后又能答对 99% 以上，暴露其三维判断依赖画面线索。**</p>

+ **Sketch, Don't Paint: Allocating Test-Time Compute in Generative Visual Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21812)
![architecture](https://img.shields.io/badge/Sketch_And_Vote-red)
![task](https://img.shields.io/badge/Multimodal_Reasoning-magenta)
![organization](https://img.shields.io/badge/State_Key_Laboratory_for_Novel_Software_Technology_Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把视觉思维的测试时算力拆成何时渲染与渲几步两轴：14 组模型-基准配对里直答赢下 9 组，10 条标注即可把平均准确率从 60.7% 提到 65.1%，8 步草图投票在迷阵上最多赢 22.1 分。**</p>

+ **SARVIA: Fast-Adapting the Strong SAR Foundation Models That Are Already in Your MLLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22273)
![architecture](https://img.shields.io/badge/SARVIA_Adaptive_Post_Pretraining-red)
![task](https://img.shields.io/badge/MLLM-magenta)
![organization](https://img.shields.io/badge/Singapore_Management_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/zcablii/SARVIA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用答案可算的自监督视觉问答把 MLLM 适配成 SAR 编码器：600 步、约 2 个 RTX PRO 6000 GPU 小时后，导出的 ViT-L 在 RSAR、SARDet-100K 等六个 SAR 基准全面领先。**</p>

+ **Scaling Laws for Vision-Language Fusion**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22351)
![architecture](https://img.shields.io/badge/Vision_Language_Fusion_Scaling_Law-red)
![task](https://img.shields.io/badge/VLM_Architecture-magenta)
![organization](https://img.shields.io/badge/Noetra_Corp.-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把视觉语言融合的学习动态拆成基线轨迹与模态竞争偏移，拟合 RMSE 0.0022 到 0.0099；晚融合的文本惩罚 gamma 约 0.02 与规模无关，视觉优势却按 N 的 -0.5 次方衰减，故规模越大越偏向早期融合。**</p>

+ **Can Vision-Language Models Truly Understand Images? A Benchmark Beyond Commonsense Bias**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22360)
![architecture](https://img.shields.io/badge/ContraSense_Benchmark-red)
![task](https://img.shields.io/badge/VQA-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/datasets/LingLin00/ContraSense)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出反常识图问基准 ContraSense：4698 个 1024×1024 手工校准样本覆盖五类违背常识场景，最强闭源模型仅约 60%（GPT-4o 60.03%），远低于人类的 96.04%，暴露 MLLM 依赖图文共现而非视觉证据。**</p>

<!-- direction: llm_vlm_rl -->

+ **M3OPD-Reasoner: An Open Recipe for Post-Training Multimodal Reasoning with Multi-Teacher On-Policy Distillation**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23034)
![architecture](https://img.shields.io/badge/Multi_Teacher_On_Policy_Distillation-red)
![task](https://img.shields.io/badge/Multimodal_GRPO-magenta)
![organization](https://img.shields.io/badge/A*STAR-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**多教师 on-policy 蒸馏的 VLM 后训练全开配方：三个领域各训一个 GSPO 教师后蒸馏成单学生，再叠一轮 MixRL，21 个 benchmark 上 avg@8 从 69.4 提到 75.9。**</p>

+ **Regularized Score Centering**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21791)
![architecture](https://img.shields.io/badge/Regularized_Score_Centering-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/UIUC-green)
[![project](https://img.shields.io/badge/project-blue)](https://biechi.github.io/blog/rsc/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**给 score centering 加反向 KL 正则的异步 RL 方法 RSC：限制 learner 偏离 behavior policy，原始 IS 的极端梯度从 25.928 降到 2.415，六个 agentic 任务全优、AppWorld 提升 14.3%。**</p>

+ **What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22161)
![architecture](https://img.shields.io/badge/Rubric_Graded_CISPO_Adapter-red)
![task](https://img.shields.io/badge/RLAIF-magenta)
![organization](https://img.shields.io/badge/Surge_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 120B 总参、12B 激活的 Nemotron 3.5 Super 用 CISPO + rank-32 LoRA 在五个专家任务集上分别做纯 RL：12 个 benchmark 增益 +4.5~+13.8 分，GDP.pdf 从 10.4% 升到 24.2%。**</p>

+ **Eyes in the Update? Learning Where Rewards Land in Multimodal Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22438)
![architecture](https://img.shields.io/badge/Gaze_Reward_Landing_Field-red)
![task](https://img.shields.io/badge/Reward_Model_Multimodal-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/lixuan27/Gaze-RL-main)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Gaze-RL 用模型自身的跨模态几何与预测熵构造奖励落点场，把轨迹级优势重新分配到真正用到视觉证据的 token 上，Qwen2.5-VL-7B 的 MathVista 从 67.2 升到 70.4。**</p>

+ **Margin Dynamics for Large Language Model Alignment**
[![paper](https://img.shields.io/badge/Arxiv_2611.21-blue)](https://arxiv.org/abs/2611.21766)
![architecture](https://img.shields.io/badge/Margin_Dynamics_Framework-red)
![task](https://img.shields.io/badge/Preference_Optimization-magenta)
![organization](https://img.shields.io/badge/Amazon-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把成对对齐方法统一成一维 margin ODE：DPO 无界增长、IPO 收敛到 1/(2τ)，标签噪声让 DPO 出现相变；据此推出 TPO-S，三个 8B–9B 模型上 IFEval 均值最高。**</p>

+ **Sample-efficient Personalization of Large Language Model Alignment with Multidimensional User Preference Data**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22210)
![architecture](https://img.shields.io/badge/Preference_Cone_Online_DPO-red)
![task](https://img.shields.io/badge/DPO-magenta)
![organization](https://img.shields.io/badge/Universite_de_Montreal-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在线 DPO 的样本效率方法 MPG-DPO：用自动验证器的多维打分估出用户偏好锥，先剔除被锥支配的响应再挑分歧最强的一对，Qwen2.5-7B 的 ARENA-HARD 胜率从 54.68 升到 56.04。**</p>

+ **Learning to Edit IFC Building Models: Verifiable Checkers as the Training Signal for Dependency-Aware Editing Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.22-blue)](https://arxiv.org/abs/2611.22307)
![architecture](https://img.shields.io/badge/IfcGym_Checker_Gated_GRPO-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Nanchang_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 IFC 建筑模型编辑的合法性、意图、依赖与保持写成四个可执行检查器并用作 GRPO 奖励，Qwen3.5-9B 在 1,990 个真实项目编辑任务上从 16.08% 提到 86.78%。**</p>

