<!-- direction: llm_core -->

+ **Tokenize Moments, Not Frames: Tokenizer-Aware Budget Allocation for Training-Free Video LLM Acceleration**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26933)
![architecture](https://img.shields.io/badge/ESSENCE_Moment_Tokenizer-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/Huazhong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/zhkandsrz/ESSENCE)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出训练无关的 ESSENCE：按帧相似度划分的 moment 而非逐帧编码视觉 token，配额分配同时考虑采样间隔与 tokenizer 类型，在三个骨干上 60 组同 TTFT 对比中 58 组更准，80% token 即可追平完整模型。**</p>

+ **LongCat Recall Sparse Attention: Co-Designing Key Organization and Retrieval for Long-Context Inference**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27233)
![architecture](https://img.shields.io/badge/LRSA_Paged_Retrieval_Attention-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/Meituan_LongCat_Team-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**长上下文推理中检索式稀疏注意力受制于选 key 时的全历史搜索。LRSA 用时间桶、容量均衡方向组与分页成员索引做两级粗到细检索，1024K 上下文下 key 选择比 DSA 快 4.70 倍，整体快全注意力 35.60 倍，并已接入 SGLang。**</p>

+ **Hy-MT3: More Accurate, Robust and Practical Multilingual Translation Models in the Wild**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27673)
![architecture](https://img.shields.io/badge/Hy_MT3_MoE_Translation-red)
![task](https://img.shields.io/badge/Pretraining-magenta)
![organization](https://img.shields.io/badge/Tencent_Hunyuan_Team-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Tencent-Hunyuan/Hy-MT3)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**腾讯混元第三代多语翻译模型 Hy-MT3，含 1.8B、7B 与 30B-A3B（MoE，仅 3B 激活）三个规格，语言覆盖从 38 种扩到 102 种，错译占比降 43%、漏译增译降 74%，并开源 TransRubric 自动评测套件。**</p>

+ **MemOnce: A Scalable Memory Architecture for Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27973)
![architecture](https://img.shields.io/badge/MemOnce_Memory_Sparse_Attention-red)
![task](https://img.shields.io/badge/LLM_Architecture-magenta)
![organization](https://img.shields.io/badge/Nanjing_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://clare-nie.github.io/MemOnce)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**MemOnce 把长程交互的记忆从逐 token 累积 KV cache 换成「末层隐状态稀疏缓存加动态解码回 KV 加跨层共享稀疏索引」，1M 上下文下显存降到 1/1313、prefill 快 6.9 倍，并在五个记忆基准上反超全上下文基线 5.77%。**</p>

+ **Language Model Harnesses can be Compositional Generalizers**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28298)
![architecture](https://img.shields.io/badge/RLM_Surrogate_Harness_Training-red)
![task](https://img.shields.io/badge/Agent-magenta)
![organization](https://img.shields.io/badge/MIT_CSAIL-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/alexzhang13/harness-cg)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把上下文管理外置到 harness 再训练：RLM 只用 32K–64K 短任务做 GRPO 就能泛化到长度放大 64 倍的评测集；再配合 surrogate harness training，RLM-27B 在八个长任务套件上平均提升 26.9%，推理 token 减半。**</p>

+ **NoHairCache: Calibrate-Once KV Cache Eviction with One Power-Law Exponent**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29006)
![architecture](https://img.shields.io/badge/NoHairCache_Power_Law_Eviction-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**NoHairCache 把 H2O 与 StreamingLLM 两种 KV cache 淘汰策略统一到同一幂律打分 s=A·(t-i)^-α 下，两者是 α=0 与 α→∞ 的端点。衰减指数是模型内在属性，一次校准即可跨三个语料复用，困惑度显著优于两者。**</p>

+ **Position-Skipped Distillation of Sparse-Attention Indexers: Train Short, Serve Long**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29664)
![architecture](https://img.shields.io/badge/Position_Skipped_Distillation-red)
![task](https://img.shields.io/badge/Sparse_Attention-magenta)
![organization](https://img.shields.io/badge/unverified-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**稀疏注意力的 indexer 通常要在满服务长度上蒸馏，训练成本极高。本文证明其长上下文失效主因是 RoPE，用 position-skipped distillation 在短序列的 position ID 插随机跳号，8K 训练即在 32K 内追平 32K 蒸馏，困惑度差约 0.5。**</p>

+ **The Temporal Residual: Fast and Effective Retrofitting of Latent Feedback into Pretrained Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29843)
![architecture](https://img.shields.io/badge/Temporal_Residual_Stream-red)
![task](https://img.shields.io/badge/LLM_Architecture-magenta)
![organization](https://img.shields.io/badge/Princeton_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**temporal residual 给预训练模型加一条跨 token 传递的第二残差流，让每个子层读写并在 token 间携带状态，只增 2,752 个参数；在 Qwen3.5-4B-Base 上后训练 5B token，AIME 2025 等竞赛数学题比同数据标准模型高 12.6 分。**</p>

+ **Fast 4-bit KV-Cache Decoding on Hopper GPUs: Why Existing Kernels Are Slow and How to Fix Them**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30027)
![architecture](https://img.shields.io/badge/Hopper_Native_4Bit_KV_Decode-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/Northeastern_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/thomaszhang2661/kv4-hopper)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Hopper 没有 FP4 硬件，4-bit KV 只能软件解码，导致 vLLM 现路径只用到 10–20% 带宽且慢于 FP8。本文用 TMA 生产 warp 与计算 warpgroup 重叠的自研 kernel 达到峰值带宽 67–75%，并在 vLLM 内把 Llama-3.1-8B 的解码提速 1.12–1.64 倍。**</p>

<!-- direction: vlm_core -->

+ **S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28649)
![architecture](https://img.shields.io/badge/S_Mind_Spatial_Tokens-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/The_Hong_Kong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://kanaboon1.github.io/S-Mind/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**S-Mind 用一组空间 token 在 MLLM 内部承载融合后的 3D 场景，并在推理切换视角时重新发射以重写场景。四个空间基准上最多提升 22.26 分，融合与变换探针准确率从 16.02% 与 37.28% 提到 65.11% 与 82.17%，推理比工具型 agent 快约 100 倍。**</p>

+ **What Does the Visual Encoder Buy? Visual Information Gain in Encoder-Free Multimodal Pretraining**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26917)
![architecture](https://img.shields.io/badge/Visual_Information_Gain-red)
![task](https://img.shields.io/badge/MLLM-magenta)
![organization](https://img.shields.io/badge/Rice_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/gezhixuan/visual-information-gain)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出 visual information gain 这一度量，把图文预训练中图像带来的 loss 下降拆成全局信息与布局信息两部分。实验显示 encoder-free decoder 的布局信息几乎不随模型规模增长，而冻结 SigLIP 2 的净优势几乎全部来自布局信息，即读懂图内文字与排版的能力。**</p>

+ **WePM: Hierarchical Conflict Reconciliation for Unified MLLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27365)
![architecture](https://img.shields.io/badge/WePM_Pocket_Unified_MLLM-red)
![task](https://img.shields.io/badge/MLLM-magenta)
![organization](https://img.shields.io/badge/WeChat_AI_Tencent-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Tencent/WePocketModel)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**WePM 把表征、生成与决策三类能力统一进一个 4B 端侧口袋模型，用多粒度视觉预算、统一 listwise 蒸馏与多任务优化解决视觉粒度冲突与数据冲突。Joint 分从 38.15 提到 52.74，驻留权重比多模型栈省 61.9%，能力密度高 2.64 倍。**</p>

+ **Seeing Right, Writing Wrong: Where Short Chain-of-Thought Breaks Spatial VQA**
[![paper](https://img.shields.io/badge/Arxiv_2611.28-blue)](https://arxiv.org/abs/2611.28665)
![architecture](https://img.shields.io/badge/CoT_Transcription_Failure_Analysis-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/Huazhong_University_of_Science_and_Technology-green)
[![project](https://img.shields.io/badge/project-blue)](https://ming-zch.github.io/seeing-right-writing-wrong)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**本文用可控实验拆解短 CoT 为何让 VLM 在空间问答上变差：写出关系会重加权视觉线索并让文本接管答案，结论句还可能反转真关系。15 个开源与 6 个闭源模型上，四分之五的 CoT 损失由假关系与结论误映射解释。**</p>

+ **Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26902)
![architecture](https://img.shields.io/badge/Baton_KV_Handoff_Map-red)
![task](https://img.shields.io/badge/Video_Understanding-magenta)
![organization](https://img.shields.io/badge/University_of_Pittsburgh-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**Baton 解决级联式 VLM 中大模型反复重编码历史的问题：小模型的视觉 KV 记忆经一个逐层线性映射交给大模型，映射只用大模型自身答案无标签蒸馏。32B 读端单次升级算力从 50.6 TFLOP 降到 19.0，精度仅差 0.7 分。**</p>

<!-- direction: llm_vlm_rl -->

+ **Which Loopholes Get Found? Predicting Reward Hacking of LLM Judges Before RL Training**
[![paper](https://img.shields.io/badge/Arxiv_2611.29-blue)](https://arxiv.org/abs/2611.29651)
![architecture](https://img.shields.io/badge/Judge_Exposure_Audit-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Columbia_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/justLxy/which-loopholes-get-found)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用「策略倾向性 × 评审器误判率」定义的暴露度，在训练前就能预测 GRPO 策略最先钻的评审器空子：36 次运行、7 个评审器中，12 次出现利用的运行全部由暴露度排第一，单看误判率只命中 6 次。**</p>

+ **Spatial Query Execution as Verifiable Rewards for Multi-step Spatial Reasoning**
[![paper](https://img.shields.io/badge/Arxiv_2611.26-blue)](https://arxiv.org/abs/2611.26787)
![architecture](https://img.shields.io/badge/FARON_Spatial_Query_Execution-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/University_of_Minnesota_-_Twin_Cities-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用可确定性执行的空间查询同时产出 SFT 的中间推理轨迹与 RLVR 的可验证奖励：轨迹式 SFT 在留出场景上把准确率从 59.94% 提到 67.53%，再叠加 GRPO 到 70.46%，5 步问题从 44.74% 提到 59.14%。**</p>

+ **Decision Models Are General-Purpose Process Reward Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27068)
![architecture](https://img.shields.io/badge/DM_PRM_Step_Credit-red)
![task](https://img.shields.io/badge/Process_Reward_Model-magenta)
![organization](https://img.shields.io/badge/UIUC-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把通用决策模型零样本当过程奖励模型，为每条 rollout 的每一步打上「是否推进任务」的概率并标准化后加进优势：ALFWorld 上把 GRPO 从 66.3% 抬到 90.0%，WebShop 上从 59.1% 抬到 72.2%。**</p>

+ **Visual-RFT++: Extending Visual Reinforcement Fine-Tuning to Multimodal Tool Use**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30193)
![architecture](https://img.shields.io/badge/Visual_RFT_Plus_Plus-red)
![task](https://img.shields.io/badge/Multimodal_GRPO-magenta)
![organization](https://img.shields.io/badge/Shanghai_Jiao_Tong_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Liuziyu77/Visual-RFT)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 GRPO 强化微调从数学与代码推广到视觉感知和多模态工具使用：1-shot 细粒度分类准确率比 SFT 高 24.3 个百分点，新提出的 MAT 基准上 MAT-Coding 提升 18.56 F1、MAT-Search 提升 10.28 F1。**</p>

+ **Typhoon OCR 2: From Thai Document Transcription to Multilingual, Multi-Task OCR**
[![paper](https://img.shields.io/badge/Arxiv_2611.27-blue)](https://arxiv.org/abs/2611.27494)
![architecture](https://img.shields.io/badge/Typhoon_OCR_2-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Typhoon_SCB_DataX-green)
[![project](https://img.shields.io/badge/project-blue)](https://opentyphoon.ai)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用一个模型同时做泰文文档的定向字段抽取与整页结构解析，并在 SFT 之后用带任务奖励和未完成惩罚的 GRPO 收尾：2B 模型泰文 MDPBench 从 68.9 提到 80.7，重复页比例从 SFT 后的 10.3 压回 2.3。**</p>

+ **Could This BE Any More Wrong? Teaching VLMs to Know What They Don't Know in Document Extraction**
[![paper](https://img.shields.io/badge/Arxiv_2611.30-blue)](https://arxiv.org/abs/2611.30119)
![architecture](https://img.shields.io/badge/Token_Logprob_Field_Confidence-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/AI_Lab_Barclays_Investment_Bank-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把模型自带的 token logprob 对齐到结构化 JSON 的每个字段，用字段内最小 token 概率判断该字段是否可能出错：CORD 上错误检测 AUROC 0.914 对口述置信度的 0.563，再用低置信字段当 GRPO 课程把准确率从 78.5% 提到 87.5%。**</p>

