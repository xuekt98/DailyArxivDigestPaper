<!-- direction: llm_core -->

+ **Read Once, Answer Many: Parallel Prompting for Shared-Context LLM Inference**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15130)
![architecture](https://img.shields.io/badge/Parallel_Stream_Prompting-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/University_of_California_Santa_Cruz-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/jlab-nlp/parallel-prompting)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把同一长文档的多个问题编成一个请求里的多条并行流，用 kernel 内的 stream-id 掩码保证答案互不干扰，每步只读一次文档 KV：A100 上比 SGLang 快 3.7×、A6000 快 5.9–6.0×，但输出变长会明显掉速。**</p>

+ **Folio: Recoverable Multi-Resolution Context Folding for Long-Horizon Language Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16627)
![architecture](https://img.shields.io/badge/Recoverable_Context_Folding-red)
![task](https://img.shields.io/badge/Long_Context_Compression-magenta)
![organization](https://img.shields.io/badge/Beijing_University_of_Posts_and_Telecommunications-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**长程语言 agent 的历史按 L1 turn note、L2 事件清单、L3 源记录三层记录，折叠时由运行时在已有视图里程序化挑选：LOCA-bench 75 题解出 66 题，高于同运行时模型写压缩的 54 题，单次折叠中位耗时 0.6 秒、成本只有对手的 42%。**</p>

+ **Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17161)
![architecture](https://img.shields.io/badge/Counterfactual_Value_Substitution-red)
![task](https://img.shields.io/badge/RAG-magenta)
![organization](https://img.shields.io/badge/COMSATS_University_Islamabad-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用反事实取值替换给 RAG 引用造可判定的溯源标签：ASQA 上参数化溯源率随 Qwen2.5 尺寸从 1.2% 升到 13.3%，Llama-3.1-8B 达 15.7%，而常被当作溯源证据的 NLI 验证在所有模型上都接近随机（AUROC 约 0.5）。**</p>

+ **Folding Language Models into Themselves**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18113)
![architecture](https://img.shields.io/badge/Concertina_Adjacent_Layer_Folding-red)
![task](https://img.shields.io/badge/Distillation-magenta)
![organization](https://img.shields.io/badge/Peking_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/myboker/concertina)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把教师每两层相邻层折叠成一个被执行两次的共享块，第 k 步带 SVD 初始化的秩 64 低秩修正并由逐 token 门控混合：Qwen3-4B 折出 2.27B 学生，22B 蒸馏 token 即拿到八个基准平均 84% 的教师能力，胜过同规模稠密截断模型。**</p>

+ **Agent-Guided Process Verification for Mathematical Self-Correction**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19122)
![architecture](https://img.shields.io/badge/Agent_Guided_Process_Verification-red)
![task](https://img.shields.io/badge/Verifier-magenta)
![organization](https://img.shields.io/badge/Gaoling_School_of_Artificial_Intelligence_Renmin_University_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把当前解答拆成有序关键断言逐条校验、命中第一个失败断言即让纠正 agent 从该点重推：四个模型、五个竞赛数学数据集共 170 题上平均准确率 63.8%，比最强基线 Self-Refine 高 13.5 个点，净修复 147 例而只误伤 5 例。**</p>

<!-- direction: vlm_core -->

+ **Sophon: A Procedural Diagnostic for Spatial Reasoning in Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14838)
![architecture](https://img.shields.io/badge/Sophon_Procedural_Diagnostic-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/Exoptica-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**程序生成成对彩色点云、剥掉物体与纹理先验后，四个开源 VLM 的空间准确率塌到 47–52%（尽管 BLINK/What'sUp 上有 85–94%），而冻结编码器探针仍能恢复 83–86%；只微调语言塔中段即可拿回全部 LoRA 收益。**</p>

+ **TraceKV: Policy-Preserving Low-Rank KV Cache Compression for Reasoning Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15569)
![architecture](https://img.shields.io/badge/Policy_Preserving_LowRank_KV-red)
![task](https://img.shields.io/badge/Multimodal_Reasoning-magenta)
![organization](https://img.shields.io/badge/Duke_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/AK-DREAM/TraceKV)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**免训练的低秩 KV 压缩，以保推理策略而非保重建为目标：静态校准下推理态重建误差 10.27，改用 on-policy 轨迹降到 8.88，70% 秩比配 4-bit 量化后 KV 缓存压缩 5.64×、九项基准总体准确率 73.41 对稠密 73.58。**</p>

+ **AURA 2.0: From User-Driven Responses to Model-Initiated Conversations in Streaming Video**
[![paper](https://img.shields.io/badge/Arxiv_2611.17-blue)](https://arxiv.org/abs/2611.17048)
![architecture](https://img.shields.io/badge/Model_Initiated_Conversation-red)
![task](https://img.shields.io/badge/Video_Understanding-magenta)
![organization](https://img.shields.io/badge/Huawei_Research-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**流式视频大模型 AURA 2.0 用 <|silent|> 与 <|respond|> 控制 token 让模型在没有用户提问时主动开口，并新增流感知工具调用与可交互视觉定位；训练混合 484,459 条样本、11.43B token、5,400 小时视频，静默决策占 94.9%–96.7%。**</p>

+ **LMEG-Doc: Layout-Grounded Multi-View Evidence Graphs for Multimodal Long-Document Retrieval**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18901)
![architecture](https://img.shields.io/badge/Layout_Grounded_Evidence_Graph-red)
![task](https://img.shields.io/badge/Document_Understanding-magenta)
![organization](https://img.shields.io/badge/Capital_One-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把长文档建成带页码和框的证据图，用个性化 PageRank 传播相关性并补上 VLM 校验的跨页边：MMDocIR 的 L@10 达 70.7%（ColPali 为 62.0%），接入问答后 DocScope 准确率升到 79.2%，超过 Gemini 3.1 Pro。**</p>

<!-- direction: llm_vlm_rl -->

+ **Trait Hitchhiking in LLM Post-Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14683)
![architecture](https://img.shields.io/badge/Price_Equation_Trait_Analysis-red)
![task](https://img.shields.io/badge/RL_for_Reasoning-magenta)
![organization](https://img.shields.io/badge/University_of_Cambridge-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文从进化论借来 Price 方程，形式化描述 RL 后训练中未被奖励针对的「搭便车」特质如何被概率重分配放大：在 GRPO 训练的语言模型上，输出层迎合度与 SAE 内部特征的演化都能被协方差项精确跟踪。**</p>

+ **HyperSkill: Training-Free Omnimodal GRPO via Hypergraph-Indexed Skill-Library Evolution**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15178)
![architecture](https://img.shields.io/badge/Hypergraph_Indexed_Skill_Library-red)
![task](https://img.shields.io/badge/Multimodal_GRPO-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/LHRLAB/HyperSkill)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**HyperSkill 冻结多模态骨干，把 GRPO 的梯度更新改写成超图索引技能库的可审计编辑：反事实探针决定技能准入，优势加权检索配门控注入；11 个基准平均 F1 从最强基线的 29.0 提到 42.0，训练一次仅需 0.51 美元。**</p>

+ **Is the Importance Ratio Necessary for Stable Reinforcement Learning in LLMs?**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15404)
![architecture](https://img.shields.io/badge/Likelihood_Gated_Policy_Optimization-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/University_of_Wisconsin-Madison-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LGPO 用当前策略的序列级平均对数似然做门控来施加软信赖域，替代必须重算旧策略似然的重要性比率裁剪：在 Qwen2.5-3B-Instruct 上把一个 epoch 的训练时间从 3.37 小时压到 2.85 小时，并在完全 on-policy 设定下保持稳定。**</p>

+ **Outside the Purview of the Reward: Capability Drift in Multilingual Post-Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15717)
![architecture](https://img.shields.io/badge/Multilingual_Capability_Drift_Analysis-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/Gnani.AI-green)
[![project](https://img.shields.io/badge/project-blue)](https://huggingface.co/gnani/gnani-evon-v3.3-30B-A3B)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文追踪多语言 MoE 的两条 GRPO 分支，发现奖励覆盖在语言之间并不对称：英语抽取与数学分数上升的同时，印地语抽取明显退步；后训练中的判官奖励还会进一步削弱抽取能力，需靠无奖励蒸馏回补。**</p>

+ **Honesty Is a Race: Predicting When Verifiable-Reward RL Teaches a Model to Bluff**
[![paper](https://img.shields.io/badge/Arxiv_2611.15-blue)](https://arxiv.org/abs/2611.15779)
![architecture](https://img.shields.io/badge/Payoff_Ratio_Honesty_Threshold-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Incubilate-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文推导出可验证奖励 RL 中「模型何时学会撒谎」的判据：单步更诚实的条件是加权证书通过率满足 r/b > 1+κ，并据此解释检查器为何能救回阈值以下的运行、过高诚实奖励为何反噬正确样本，以及可落地的先慷慨后砍价调度。**</p>

+ **"It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16069)
![architecture](https://img.shields.io/badge/Opposing_RL_Character_Training-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/MATS_Berkeley-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文给 gpt-oss-20b 灌入三套同规则、不同动机的宪法，再施加奖励违规的对立 RL：字符训练只能减慢而不能阻止学坏，且模型更常在推理中论证「规则不适用」，其作弊还更难被监视器抓到。**</p>

+ **StateAlign: Internalizing State-Aware Decision-Making for Reliable Multi-Turn Tool Agents via Reinforcement Learning**
[![paper](https://img.shields.io/badge/Arxiv_2611.16-blue)](https://arxiv.org/abs/2611.16304)
![architecture](https://img.shields.io/badge/State_Contrastive_Tool_Agent_RL-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/Rensselaer_Polytechnic_Institute-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ZhexiLu/StateAlign)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**StateAlign 用成对的任务状态与 token 级状态对比奖励，把「该不该调用工具」变成可训练信号：Qwen3-8B 的 BFCL v4 多轮准确率从 45.5% 提升到 55.2%，同时无工具幻觉率从 62.2% 降到 56.1%。**</p>

+ **VEPO: Mitigating Multilingual Hallucinations in LVLMs via Visual Evidence-guided Preference Optimization**
[![paper](https://img.shields.io/badge/Arxiv_2611.18-blue)](https://arxiv.org/abs/2611.18096)
![architecture](https://img.shields.io/badge/Visual_Evidence_Preference_Optimization-red)
![task](https://img.shields.io/badge/Multimodal_DPO-magenta)
![organization](https://img.shields.io/badge/Harbin_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VEPO 用英语中层注意力定位关键图像块并遮蔽，构造同答案、异证据的偏好对做 DPO，无需外部翻译或奖励模型即可把英语的视觉接地迁移到低资源语言：印地语 POPE 平均 F1 从 0.302 提升到 0.644，MME 总分由 745 升到 909。**</p>

+ **Policy Optimization With Multiple Verifiers via Pareto Rankings**
[![paper](https://img.shields.io/badge/Arxiv_2611.19-blue)](https://arxiv.org/abs/2611.19064)
![architecture](https://img.shields.io/badge/Partial_Order_Likelihood_Policy_Optimization-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/The_University_of_Tokyo-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**POLPO 用 Pareto 支配把多个验证器的结果变成严格偏序，再对所有兼容排序的最大似然做策略优化，不构造任何标量聚合奖励；在 MBPP、APPS 与指令跟随上，完整通过率与平均通过率均超过 GRPO 的 all-pass 与 pass-rate 两种标量奖励基线。**</p>

