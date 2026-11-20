<!-- direction: llm_core -->

+ **Chorus: Shared N-gram Embeddings with Layer-wise Adaptation**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23386)
![architecture](https://img.shields.io/badge/Chorus_Shared_NGram_Embedding-red)
![task](https://img.shields.io/badge/LLM_Architecture-magenta)
![organization](https://img.shields.io/badge/DualverseAI-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/dualverse-ai/chorus)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Chorus 提出单一共享 n-gram 嵌入表加逐层投影的读表方式，表规模比逐层独立表小 87%，1.2B 表参数即可超过 Engram 与 FactorEngram 的 9.6B 配置，并兼容省显存的 Ember 优化器。**</p>

+ **Beyond Replacement: Levenshtein Editing for Diffusion Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23750)
![architecture](https://img.shields.io/badge/LED_Levenshtein_Editing-red)
![task](https://img.shields.io/badge/LLM_Architecture-magenta)
![organization](https://img.shields.io/badge/Southern_University_of_Science_and_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**LED 用最长公共子序列对齐在微调时自动构造插入与删除监督，把扩散语言模型的替换式编辑扩成 Levenshtein 式序列修订，在 16B 模型上把无置信度解码均分从 27.52 提到 47.19。**</p>

+ **Semantic Context Handoff with On-Demand Evidence for Long-Horizon Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24357)
![architecture](https://img.shields.io/badge/Semantic_Context_Handoff-red)
![task](https://img.shields.io/badge/Agent_Memory-magenta)
![organization](https://img.shields.io/badge/Minjiang_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://anonymous.4open.science/r/sch-F88C/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SCH 把长程 Agent 的上下文拆成语义状态与可寻址证据两部分，证据可在后续步骤重新进入上下文，在 150 任务 SWE-bench 上把 Pass@1 从 80.0% 提升到 86.9%，且比最强基线少用 43% token。**</p>

+ **Late Entry in Looped Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24576)
![architecture](https://img.shields.io/badge/Late_Entry_Looped_LM-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/Nanyang_Technological_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://xalp.net/late-entry)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**论文提出循环语言模型的晚入场解码：新 token 跳过前序 pass 直接接入末段 K 层并复用深上下文缓存，Wake 验证在 Ouro-2.6B 上取得 5.2 倍贪心精确加速，在 Huginn-3.5B 上可达 8.4 倍。**</p>

+ **Clover-35B-A3B-Preview Technical Report**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24636)
![architecture](https://img.shields.io/badge/Clover_BD_GDN_MoE-red)
![task](https://img.shields.io/badge/MoE-magenta)
![organization](https://img.shields.io/badge/DiffuSpace_Technical_Team-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/DiffuSpace/Clover-35B-A3B-Preview)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Clover 是 35B 总参 3B 激活的混合专家扩散语言模型，用 BD-GDN 在块内做双向注意力、在七项 Agent 指标上领先，SWE-bench Verified 达 73.6，单卡 GB300 上生成速度 680 tokens/s。**</p>

+ **On-Policy Morphing into Hybrid Attention Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24809)
![architecture](https://img.shields.io/badge/FlashMorph2_OnPolicy_Layer_Selection-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/Fudan_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FlashMorph2 指出 FlashMorph 层选择存在连续插值与冻结权重两处策略外错配，改为用采样出的离散混合结构端到端评估并联合优化选择分数与权重，RULER 上比前者平均高 2.42 分。**</p>

+ **Atomic MathReasoner: Instance-Level Composition of Atomic Reasoning Skills for Mathematical LLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.24-blue)](https://arxiv.org/abs/2611.24846)
![architecture](https://img.shields.io/badge/Atomic_MathReasoner-red)
![task](https://img.shields.io/badge/Math_Reasoning-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**AMR 把数学推理拆成原子技能并训练 LoRA 专家库，用无梯度优化搜出组合原型再蒸馏为轻量路由，在 Qwen2.5-Math-Instruct-7B 上把逻辑推理均分从 39.4% 提升到 46.8%。**</p>

+ **RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25433)
![architecture](https://img.shields.io/badge/RoCoKV_Uncertainty_Redundancy-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/Georgia_Institute_of_Technology_USA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RoCoKV 为大型推理模型设计 KV 缓存压缩：按置信度自适应调整剪枝强度并惩罚与近期推理高度重复的 token，以三阶段融合 CUDA 解码核做成 vLLM 插件，AIME25 上加速 1.27 倍。**</p>

+ **VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25717)
![architecture](https://img.shields.io/badge/VR_SparseQuant_2of4_FP4-red)
![task](https://img.shields.io/badge/Quantization-magenta)
![organization](https://img.shields.io/badge/Nebius_Applied_AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VR-SparseQuant 利用 Vera Rubin 的逐元素 2:4 稀疏把激活表示为两路不同 scale 的稀疏 FP4 流，在 Nemotron-3-Nano-30B-A3B 上把困惑度从 6.85 降到 5.57，内核相对 BF16 加速 3.1 倍。**</p>

+ **Efficient and Robust Drafting with Multi-Token Prediction**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25813)
![architecture](https://img.shields.io/badge/G_MTP_Drafting_Head-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/Google-green)
[![project](https://img.shields.io/badge/project-blue)](https://ai.google.dev/gemma/docs/mtp/mtp)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**G-MTP 在 Gemma 4 上把多 token 预测起草头做成单个共享 4 层 Transformer，配合目标激活注入、零拷贝 KV 交叉注意力与聚类词表投影，服务器端加速最高 3.1 倍、手机 GPU 达 2.2 倍。**</p>

+ **DTS: Delta-Based Tile Scoring for Efficient Long-Context Sparse Attention**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25938)
![architecture](https://img.shields.io/badge/DTS_Delta_Tile_Scoring-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/Leiden_Institute_of_Advanced_Computer_Science_LIACS_Leiden_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**DTS 提出无需训练的 delta 式 tile 打分，按 query 与 key 的局部向量变化挑选锚点并并行打包扫描，在 512K 长度下于 4 张 H100 取得相对 FlashAttention-2 的 3.3 倍 prefill 加速。**</p>

+ **FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26020)
![architecture](https://img.shields.io/badge/FrontierReplay_Prefix_Caching-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/School_of_Computer_Science_Beijing_Institute_of_Technology-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**FrontierReplay 面向混合语言模型，在多轮对话与 Agent 循环等可预判的结构边界上免切 prefill 地物化精确前缀检查点，用跨层只重放状态的内核把 TTFT 中位数降低 16% 到 89%。**</p>

<!-- direction: vlm_core -->

+ **Bits, Not Boxes: Label-Free Layer Selection for Visual Localization in VLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23432)
![architecture](https://img.shields.io/badge/WhereBits_Layer_Prior-red)
![task](https://img.shields.io/badge/Visual_Grounding-magenta)
![organization](https://img.shields.io/badge/University_of_British_Columbia-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/fengyurenpingsheng/BitsNotBoxes)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WhereBits 提出无标注的视觉定位选层方法：把注意力落点信息折算成比特量作为层先验并与逐头对比分数结合，在 COCO 上把指向准确率做到 0.72，远高于均值注意力的 0.22。**</p>

+ **MobileWeave: Program-First Synthesis of Dependency-Linked Tasks for Training Mobile GUI Agents**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23860)
![architecture](https://img.shields.io/badge/MobileWeave_Program_Synthesis-red)
![task](https://img.shields.io/badge/GUI_Agent-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://maxxnotmarx.github.io/MobileWeave/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MobileWeave 改为程序优先的移动 GUI 任务合成：从应用实现抽出带类型的能力图，用显式值与对象依赖组合出跨应用程序并以原生执行验证，8B 模型在 MobileGym 上提升 26.7 分。**</p>

+ **Recurrent Vision Language Models Solve the Shell Game**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25210)
![architecture](https://img.shields.io/badge/RecurrentVLM_Recurrent_Attention-red)
![task](https://img.shields.io/badge/Video_Understanding-magenta)
![organization](https://img.shields.io/badge/Johns_Hopkins_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**RecurrentVLM 把预训练视觉语言模型的每个注意力层改造成随时间循环，用该层自身输出生成已结束帧组的键值，在 VET-Bench 与 MET-Bench 上分别达到 100% 与 99.6% 的准确率。**</p>

+ **WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26409)
![architecture](https://img.shields.io/badge/WeMM_Video_Omni_Model-red)
![task](https://img.shields.io/badge/Omni_Model-magenta)
![organization](https://img.shields.io/badge/WeChat_Vision_Tencent_Inc.-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Tencent/WeMM-Video)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WeMM-Video 发布 2B、4B、9B 与 35B-A3B 四档中英双语全模态视频模型，以约 1.2 万亿 token 渐进预训练并配合多教师 OPD 与抗重复 MrDPO，35B-A3B 在 17 个音视频基准中的 16 个领先闭源模型。**</p>

<!-- direction: llm_vlm_rl -->

+ **ReSynth: Constructing Synthetic Supervision for Multi-Image Understanding**
[![paper](https://img.shields.io/badge/Arxiv_2611.23-blue)](https://arxiv.org/abs/2611.23996)
![architecture](https://img.shields.io/badge/ReSynth_Relation_Synthesis-red)
![task](https://img.shields.io/badge/Multimodal_GRPO-magenta)
![organization](https://img.shields.io/badge/ZJU-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**ReSynth 用单图感知加可控生成造出跨图关系监督，以约 44 万条纯合成多图题做 GRPO，让 Qwen2.5-VL-7B 在 BLINK/MUIRBench/VLM2-Bench 上平均涨 17.73 分。**</p>

+ **EgoWitness: Benchmarking Instance-Level Spatial Memory and Reasoning in Egocentric Video Streams**
[![paper](https://img.shields.io/badge/Arxiv_2611.25-blue)](https://arxiv.org/abs/2611.25849)
![architecture](https://img.shields.io/badge/EgoClue_Spatial_Memory_Agent-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://egowitness.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EgoWitness 以 8453 个人工核验问题量化第一视角视频的实例级空间记忆，其 EgoClue 智能体经 SFT+GRPO 训练后在 1320 道留出题上从 23.64% 提升到 72.65%。**</p>

