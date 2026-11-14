<!-- direction: llm_core -->

+ **Knowledge in the Harness, Reliability in the Weights: Teacher-Free Co-Evolution of an LLM Agent**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15268)
![architecture](https://img.shields.io/badge/Harness_CoEvolution_GRPO-red)
![task](https://img.shields.io/badge/Agent-magenta)
![organization](https://img.shields.io/badge/Brightendata-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Brightendata/knowledge-in-the-harness)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**研究无教师模型条件下开源 agent 的自举闭环：Gemma 4 12B 从部署日志中诊断失败对话并写入技能规则，规则须通过代码检查、反例自审、配对复测与噪声校准门控，随后用 GRPO 训练 LoRA。τ²-bench 两轮后零售域提升 12.5 个 pass¹ 分、航空域 19.5 分。**</p>

+ **Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15538)
![architecture](https://img.shields.io/badge/QDRAG_Query_Decomposition_Rerank-red)
![task](https://img.shields.io/badge/RAG-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 QDRAG 框架：用零样本查询分解（QD-C 基于上下文知识、QD-R 基于检索奖励）把问题拆成原子子问以识别隐式实体，再用重排器裁剪干扰上下文。四个多模态 QA 基准上超过全部基线，7B 版本在 InfoSeek 上的 EM 达 46.0，远高于 Gemini-Pro 的 9.8。**</p>

+ **DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15729)
![architecture](https://img.shields.io/badge/DISCERN_BiTemporal_Memory_Graph-red)
![task](https://img.shields.io/badge/Agent_Memory-magenta)
![organization](https://img.shields.io/badge/Amazon-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 DISCERN 记忆框架：写入时构建严格可加的双时态溯源图，永不合并易混实体、永不丢弃被取代的旧值；读取时用零 LLM 工具面导航该图谱，并在作答、更新、澄清、弃答四个受控动作中只提交一个。ENT-310 上弃答 F1 达 0.924，宏平均答案正确率 0.861。**</p>

+ **KVPath: Connecting Key-Value Representations Across Transformer Layers**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16072)
![architecture](https://img.shields.io/badge/KVPath_InterLayer_Delta_KV-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/University_of_California_Santa_Barbara-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/luoxuan-cs/KVPath)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 KVPath：把每个 token 的 KV 表示连成一条跨层路径，首层缓存全维基座 KV、后续层只缓存低维增量 KV，分残差更新与滚动更新两个变体。参数量对齐下 GQA 变体在 32K 上下文减少 68.65% 缓存占用、MLA 变体减少 54.90%，困惑度不升反降。**</p>

+ **daVinci-Prover: Agent-Native Mid-Training for Formal Theorem Proving**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16433)
![architecture](https://img.shields.io/badge/daVinci_Prover_Agent_Native_Midtrain-red)
![task](https://img.shields.io/badge/Reasoning-magenta)
![organization](https://img.shields.io/badge/Shanghai_Innovation_Institute-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 daVinci-Prover 的 agent-native 中训配方：合成 33.7B token 覆盖分解、搜索、自验证与修改，用 Lean 验证器 harness 收集约 3.6 万条轨迹做 SFT；Qwen3-8B 的 pass@1 在三个基准上平均高出同规模 SFT 基线 13.7 分。**</p>

+ **Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16661)
![architecture](https://img.shields.io/badge/CAAS_Batch_Makespan_Coordination-red)
![task](https://img.shields.io/badge/Training_Infrastructure-magenta)
![organization](https://img.shields.io/badge/Ling_Team_Ant_Group-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对 LLM agent 批量执行的推理–环境协同优化：按工作负载在 KV cache 与循环状态间分配显存，用轨迹感知路由复用缓存，并提出链式推进动作调度按已观测进度优先推进长链以缩短批次长尾。四个基准上批完成时间缩短 10.4%–65.0%，评测分数保持对齐。**</p>

+ **Towards Green Text Generation: Memory-Based Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16714)
![architecture](https://img.shields.io/badge/Olifant_Memory_Spec_Decoder-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/Utrecht_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/antalvdb/olifant-speculative)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 Olifant：基于内存分类器的草稿模型，从四 token 窗口在 CPU 上以低于 0.3 毫秒的延迟预测下一个 token，无需 GPU 与加速器显存。无 KV cache 的验证器下接受率 38.1%、吞吐 2.43 倍、每 token 能耗降 2.51 倍。**</p>

+ **DRAMA: Dissecting Attention Redundancy for Accelerating Multimodal Diffusion Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16345)
![architecture](https://img.shields.io/badge/DRAMA_SVTP_SGAS_Acceleration-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/National_Taiwan_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/CindyHung20/DRAMA)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 DRAMA 免训练加速框架，先沿空间与时间两条轴系统剖析多模态扩散语言模型的注意力冗余，再据此设计空间冗余感知视觉 token 剪枝与充分性引导自适应早停。在 LLaDA-V 六个视觉语言基准上取得平均 18.67 倍推理加速，准确率保持竞争力。**</p>

+ **CURATOR: Scalable Fine-grained Evidence Selection for Retrieval-Augmented Generation using Decision Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16366)
![architecture](https://img.shields.io/badge/CURATOR_Joint_Evidence_Decider-red)
![task](https://img.shields.io/badge/Retrieval-magenta)
![organization](https://img.shields.io/badge/AWS_AI_Labs-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 CURATOR：可联合判定大量候选 span 的微调决策模型，用于 RAG 的细粒度证据选择。相对预训练联合决策模型，它在 QAMPARI 上把证据召回平均提高 25.8%，在 128 token 预算的未见数据集与领域上提高 17.0%，下游 RAG 答案质量提高 17.4%。**</p>

+ **Beyond Compressing Everything: Contrastive Memory Learning for Selective Context Compression**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16384)
![architecture](https://img.shields.io/badge/CoMem_Contrastive_Compressor-red)
![task](https://img.shields.io/badge/Long_Context_Compression-magenta)
![organization](https://img.shields.io/badge/Institute_of_Automation_Chinese_Academy_of_Sciences-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/scar-on/CoMem)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 CoMem 查询引导的选择性上下文压缩：用同文档多查询构造硬负例做对比式压缩器学习，并把记忆槽之间的注意力改为双向。在四个长文档 QA 基准与 RULER-NIAH 上，4 倍压缩准确率 0.972、32 倍压缩 0.612，均优于现有压缩方法。**</p>

<!-- direction: vlm_core -->

+ **CineMME: From Dialogue Grounding to Narrative Reasoning in Multimodal Video Understanding**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15161)
![architecture](https://img.shields.io/badge/CineMME_Dialogue_Plot_Benchmark-red)
![task](https://img.shields.io/badge/Video_QA-magenta)
![organization](https://img.shields.io/badge/ShanghaiTech_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://cinemme.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发布 CineMME 基准：975 段叙事短片、13,554 段时间戳语音片段、33,083 张说话人脸框与约 1600 专家人时标注，分设对话定位与剧情推理两条互链赛道。评测显示 Gemini-3 Pro 时序定位 68.34% tIoU，但活跃说话人定位仅 7.74% vIoU。**</p>

+ **SpaceMCP: Vision Language Model Spatial Reasoning via Model Context Protocol**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15680)
![architecture](https://img.shields.io/badge/SpaceMCP_Metric_Scene_Graph-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/University_of_Oxford-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 SpaceMCP：用 Depth Anything 3 实时重建度量点云、SAM 3 做开放词表分割构建场景图，再以 MCP 式结构化函数调用让 VLM 查询距离、物体位置与相机属性。完全无训练下在 VSI-Bench、MMSI-Bench、VSTI-Bench 上把基座 VLM 各提升 15–22 分。**</p>

+ **Keep Images in Sight: Visual Position Re-Anchoring for Long-Context MLLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15100)
![architecture](https://img.shields.io/badge/VPR_Visual_Position_Reanchoring-red)
![task](https://img.shields.io/badge/Visual_Grounding-magenta)
![organization](https://img.shields.io/badge/Tsinghua_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 VPR：训练-free 地把缓存中视觉 key 的 rotary 相位向短上下文参考位置平移，解决长上下文里图像在但细节取不到的位置性失访。10 个 checkpoint、10 个基准共 100 组分数中改善 97 组，答案证据区域注意力份额平均提升 0.70–2.57 个百分点。**</p>

+ **MAST: Medoid-Anchored Subspace Steering for Visual Grounding in Multimodal LLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15168)
![architecture](https://img.shields.io/badge/MAST_Medoid_Subspace_Steering-red)
![task](https://img.shields.io/badge/Visual_Grounding-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 MAST 免训练、输入自适应的激活引导框架：按任务做多中心聚类并为每簇选 medoid 代表，查询路由到多个代表后抽取局部低秩方向再聚合。在 LLaVA-v1.5-7B 上把 CV-Bench 的空间关系、计数、距离、深度分别提升 19.42、6.35、16.25、26.25 分。**</p>

+ **Unbundling Multimodal Vision Encoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17334)
![architecture](https://img.shields.io/badge/Unbundled_Vision_Encoding_Study-red)
![task](https://img.shields.io/badge/VLM_Architecture-magenta)
![organization](https://img.shields.io/badge/Meta_FAIR-green)
[![project](https://img.shields.io/badge/project-blue)](https://unbundling.github.io)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在同数据、同算力下逐一拆解视觉编码器的三个设计选择：视觉先验并非必需、关键在于专用视觉容量、且容量可放在骨干内部而非前置。在 1.7B 骨干上把视觉分支放进前 8 层即拿到平均 VQA 45.0，与前置编码器 46.5 相当而无编码器方案仅 39.0。**</p>

<!-- direction: llm_vlm_rl -->

+ **The Illusion of Diversity: Aligning LLM Exploration via Effective Entropy**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15493)
![architecture](https://img.shields.io/badge/VEPO_Effective_Entropy_Policy_Optimization-red)
![task](https://img.shields.io/badge/Exploration-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出标准熵把幻觉误当成探索，提出只在奖励定义的有效子空间内度量多样性的 effective entropy 并实例化为 VEPO，在匹配正确数的 441 道 MATH500-7B 题上把每题策略簇数从 2.31 提到 2.68。**</p>

+ **Safety as a Budget: Calibrating the Control Channel of Constrained GRPO for Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16628)
![architecture](https://img.shields.io/badge/Two_Channel_Constrained_GRPO-red)
![task](https://img.shields.io/badge/Multimodal_GRPO-magenta)
![organization](https://img.shields.io/badge/Lanzhou_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 VLM 安全重写为有害帮助率与过度拒答率两个预算，指出直接套约束 GRPO 会因评分器均值偏差和组内标准化两次失效，用双通道加保序校准映射把 1,037 条对抗提示的有害率从 8.9% 压到 4.8%。**</p>

+ **Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16816)
![architecture](https://img.shields.io/badge/Outcome_Mass_Alignment-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/University_of_Chinese_Academy_of_Sciences-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出多轮 agent RL 的逐行物化会重复计入同一条轨迹的结局、token 归约又造成目标质量失衡，提出按唯一源轨迹统计结局的 OMA 框架，在 ALFWorld 上把 1.5B 成功率从 0.734 提到 0.828。**</p>

+ **Bait: Mitigating Harmful Agentic Reinforcement Learning via Probing Reward Function**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16369)
![architecture](https://img.shields.io/badge/Bait_Probing_Reward_Defense-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/git-disl/Bait)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**披露约 20 美元成本的 agentic RL 服务攻击可彻底推翻模型安全对齐，提出通过主动探针奖励函数来识别有毒奖励的 Bait 防御，在三个种子上把平均有害分从 20.4 压到 6.8 且不损 agent 准确率。**</p>

+ **Negative-Only Policy Optimization for One-Sided Verifiable Rewards**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17287)
![architecture](https://img.shields.io/badge/Negative_Only_Policy_Optimization-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把只有廉价证伪手段的现实场景形式化为单边可验证性，指出高假阳性率会诱导模型走捷径，提出只抑制可靠负样本的 NOPO，在 Qwen3-4B 上把五个基准的平均 pass@16 从 48.93 提到 52.86。**</p>

