<!-- direction: llm_core -->

+ **Can KV Cache Be Reused Across Model Updates? A DeepSeek-V4-Flash Case Study**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14051)
![architecture](https://img.shields.io/badge/Cross_Version_KV_Reuse-red)
![task](https://img.shields.io/badge/KV_Cache-magenta)
![organization](https://img.shields.io/badge/Rank_Computing-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**实测四组模型更新间直接复用 KV 缓存：缓存能保留任务信息却未必复现新模型行为，GLM 复用把 32K 前缀 NIAH 准确率从 86.46% 推到 90.62%，Qwen 却从 55.21% 掉到 13.02%，已有源缓存时首 token 延迟中位数加速 2.10–5.08 倍。**</p>

+ **REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14399)
![architecture](https://img.shields.io/badge/Real_EAL_Training_Loss-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/The_University_of_Hong_Kong-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/King-ty/speculators/tree/real-loss)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**指出块级训练目标只是期望接受长度的代理、协方差差甚至会反转梯度方向，提出用路径权重做无偏估计并以 Rao-Blackwell 化降方差的 REAL 损失，在 Qwen3.6-35B-A3B 与 Domino drafter 上把概率式接受长度推到 4.792。**</p>

+ **Placing LLM Lookup Tables by Per-Layer Prefetch Deadlines**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13413)
![architecture](https://img.shields.io/badge/SlackTier-red)
![task](https://img.shields.io/badge/Inference_Efficiency-magenta)
![organization](https://img.shields.io/badge/Microsoft-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**以每层预取截止期为依据给 LLM 查表分层放置：DeepSeek-V4.1 两块共 203 GB 的 Engram 表从 host DRAM 下沉到 NVMe 或 RDMA，host 内存 212→34 GiB、每输出 token 时间最多涨 1.4%，释放出的内存做 KV cache 后吞吐再提升 36%。**</p>

+ **ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13442)
![architecture](https://img.shields.io/badge/ForeSpark_WCS_Scheduler-red)
![task](https://img.shields.io/badge/Speculative_Decoding-magenta)
![organization](https://img.shields.io/badge/Meta-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发现高负载下并行草稿最多吃掉 40% 步时间且大部分被丢弃，提出工作守恒的联合 draft/verify 预算调度 ForeSpark，在 vLLM 上吞吐较 DSpark 最高 1.77 倍、较自回归 2.49 倍，同时不改变输出分布并能承受 1.51 倍请求率。**</p>

+ **OpticalRAG: Pixel-Space Compression for Token-Efficient Retrieval-Augmented Generation**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13675)
![architecture](https://img.shields.io/badge/OpticalRAG_Encoder_Bridged_Pipeline-red)
![task](https://img.shields.io/badge/RAG-magenta)
![organization](https://img.shields.io/badge/Renmin_University_of_China-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/brighterr/OpticalRAG)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把 RAG 的压缩模态从一维文本换成页面像素：渲染文档经冻结视觉编码器压到约 100 个视觉 token，再蒸馏成 16 个注入 token，LongBench-v2、BAMBOO、LooGLE-v2 上压缩感知准确率最佳，LongBench-v2 比闭卷骨干高 5.17 分。**</p>

+ **SinkState: On-the-Fly SVD of Recurrent States for Efficient Hybrid LLM Serving**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14246)
![architecture](https://img.shields.io/badge/SinkState_Low_Rank_Recurrent_State-red)
![task](https://img.shields.io/badge/State_Space_Model-magenta)
![organization](https://img.shields.io/badge/Rutgers_University-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**发现线性注意力层的查询/键/值集中在稳定低维子空间，SinkState 以自适应低秩形式存储 recurrent state 并异步合并残余分量，在 4B–120B 四个混合模型上峰值内存最多降 2.6 倍、解码最多快 1.58 倍且精度保持不变。**</p>

+ **One-Sided Expert-Parallel All-to-All for Mixture-of-Experts Inference over NVLink**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13188)
![architecture](https://img.shields.io/badge/NVLinkOneSided_EP_All2All-red)
![task](https://img.shields.io/badge/MoE-magenta)
![organization](https://img.shields.io/badge/NVIDIA-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**针对 MoE 推理每层两次 all-to-all 的固定开销，提出单 NVLink 域内的单边专家并行实现 NVLinkOneSided：源端直写目标 rank-major 缓冲区、grouped GEMM 就地读取，在 Blackwell 上比 DeepEP 快 1.2–3.0 倍，MoE 层最多快 2.4 倍。**</p>

<!-- direction: vlm_core -->

+ **VIGOR: Benchmarking Visual Rationale Correctness in Multimodal Large Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13150)
![architecture](https://img.shields.io/badge/VIGOR_Grounded_Rationale_Benchmark-red)
![task](https://img.shields.io/badge/Visual_Grounding-magenta)
![organization](https://img.shields.io/badge/University_of_Virginia-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/deep-real/VIGOR)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**VIGOR 基准把多模态模型的视觉理由表示为概念加像素级落地，覆盖低层属性到高层运动关系四个抽象层级，含 1000 张图、3011 个概念、31433 个像素标注，最佳模型也只有 31.2% AP 与 38.7% Pointing Accuracy。**</p>

+ **Disentangling Multimodal Rotary Positional Embedding in Vision-Language Models**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13334)
![architecture](https://img.shields.io/badge/Attention_Specific_Coordinate_Assignment-red)
![task](https://img.shields.io/badge/VLM_Architecture-magenta)
![organization](https://img.shields.io/badge/University_of_Maryland_College_Park-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用注意力粒度的坐标分配把 MRoPE 的跨模态空间效应与模态内空间结构解耦，在 Qwen3-VL-2B/4B/8B 上发现：去掉模态内空间编码使 RefCOCO ACC@0.5 从 82.4% 崩到 18.5%，而只去掉跨模态效应反而提升空间理解与细粒度落地。**</p>

+ **EVAThink: Evidence Sufficiency-Guided Training for Adaptive Thinking in Video Understanding**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13907)
![architecture](https://img.shields.io/badge/EVAThink_Evidence_Guided_Adaptive_Thinking-red)
![task](https://img.shields.io/badge/Video_Understanding-magenta)
![organization](https://img.shields.io/badge/East_China_Normal_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/ChangtiWu/EVAThink)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**EVAThink 用证据充分性引导的训练让视频模型自适应决定是否显式推理：仅 6.7K 样本（VideoAuto-R1 用 83K），32 帧平均准确率 63.5%、64 帧 65.6%，比固定直接回答与只思考分别高 2.3 和 3.6 个点，输出长度还少 62%。**</p>

+ **Where Do Vision-Language Models Get Left and Right? Position-Code Counterfactuals in Qwen2.5-VL, Qwen3-VL and InternVL3**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14060)
![architecture](https://img.shields.io/badge/Position_Code_Counterfactual_Probe-red)
![task](https://img.shields.io/badge/Spatial_Reasoning-magenta)
![organization](https://img.shields.io/badge/Changzhou_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/chen4study-hub/where-vlms-get-left-right)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用只改位置码、不动像素的训练无关反事实探针定位 VLM 左右判断的来源：在 Qwen2.5-VL-7B、Qwen3-VL-4B、InternVL3-2B 上镜像 ViT 宽度位置码即可复现 84.3–93.2% 的 CV-Bench 左右翻转答案，LLM 侧镜像几乎无效。**</p>

+ **Sckwoky at SHROOM-Visions: Character-Level Hallucination-Span Detection in Image-Conditioned VLMs via Dual-Prompted LoRA Decoders**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14100)
![architecture](https://img.shields.io/badge/Dual_Prompted_LoRA_Span_Detector-red)
![task](https://img.shields.io/badge/Multimodal_Hallucination-magenta)
![organization](https://img.shields.io/badge/Novosibirsk_State_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/sckwokyboom/Vision-Hallucination-Detector)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**SHROOM-Visions 2026 共享任务的字符级幻觉跨度检测方案：冻结 Gemma-4-12B-it 加约 10.7M 参数 LoRA，靠把候选答案在提示里重复一次获得近似双向上下文，闭测集字符宏平均 IoU 0.4404，是官方基线 0.1854 的两倍多。**</p>

<!-- direction: llm_vlm_rl -->

+ **Wrong the Same Way: Cross-Prompt Sharing Both Suppresses and Amplifies Reward Hacking in RLVR**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13218)
![architecture](https://img.shields.io/badge/Cross_Prompt_Sharing_Drift_Model-red)
![task](https://img.shields.io/badge/Reward_Hacking-magenta)
![organization](https://img.shields.io/badge/Carnegie_Mellon_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/Rohan-Pandey1729/RLVR-Reward-Hacking)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**在 64 个 prompt 的可枚举环境里证明 RLVR 既可能继承也可能放大 reward hacking：跨 prompt 参数共享是关键通道，泄漏普适度决定漂移方向，修复应瞄准模型跨 prompt 重复犯的错误。**</p>

+ **Are Dense Rewards Worth Their Tokens in GRPO?**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13560)
![architecture](https://img.shields.io/badge/Matched_Compute_Validation_Protocol-red)
![task](https://img.shields.io/badge/GRPO-magenta)
![organization](https://img.shields.io/badge/Case_Western_Reserve_University-green)
[![project](https://img.shields.io/badge/project-blue)](https://github.com/vicky157/grpo-validation)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**提出按生成 token 与训练 GPU 小时双预算对齐的预注册评测协议，在 1,668 次运行中证明稠密过程奖励的排名会反转：蒙特卡洛奖励吃掉 91% 的 token，等算力下反比 GRPO 低 14.3 个点。**</p>

+ **Margin-Guided Token Credit for Reinforcement Learning with Verifiable Rewards**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14015)
![architecture](https://img.shields.io/badge/Margin_Credit_Policy_Optimization-red)
![task](https://img.shields.io/badge/RLVR-magenta)
![organization](https://img.shields.io/badge/PayPal.AI-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用 top-2 margin 取代 GRPO 的 token 均匀信用，把 reward 集中到决策分叉处：MiniCPM5-2B-Base 五个种子全部胜过基线，macro avg@32 平均 +6.55 点，且不需要额外前向传播。**</p>

+ **Personalized Memory Rubrics: Learning What to Remember per User via Rubric-Guided Credit Assignment**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14017)
![architecture](https://img.shields.io/badge/Rubric_Guided_Credit_Assignment-red)
![task](https://img.shields.io/badge/Agent_RL-magenta)
![organization](https://img.shields.io/badge/University_of_Science_and_Technology_of_China-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**用通用层加每用户残差层的个性化 rubric，把稀疏终端 QA 奖励转成 token 级信用：在 PersonaMem 32K 拿到 76.76 准确率、超最强基线 9.29 点，且推理阶段零额外开销。**</p>

+ **Metric-Aligned Group Relative Policy Optimization for Explainable Deepfake Detection**
[![paper](https://img.shields.io/badge/Arxiv_2611.14-blue)](https://arxiv.org/abs/2611.14436)
![architecture](https://img.shields.io/badge/Metric_Aligned_GRPO_Pipeline-red)
![task](https://img.shields.io/badge/Multimodal_GRPO-magenta)
![organization](https://img.shields.io/badge/University_of_Ljubljana-green)
[![project](https://img.shields.io/badge/project-blue)](https://explainable-deepfake-detection.github.io/)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把评测指标直接写成 GRPO 奖励来优化视觉语言解释器，把复杂解释 BERTScore-F1 从 0.686 提到 0.712、grounding 从 0.310 提到 0.341，复杂解释项在挑战赛上排名第一。**</p>

+ **Leveraging Psychophysical Attentional Distribution for Gaze-Augmented Reward Modeling**
[![paper](https://img.shields.io/badge/Arxiv_2611.13-blue)](https://arxiv.org/abs/2611.13477)
![architecture](https://img.shields.io/badge/Asymmetric_Gaussian_Gaze_Redistribution-red)
![task](https://img.shields.io/badge/Reward_Modeling-magenta)
![organization](https://img.shields.io/badge/KAIST-green)
[![note](https://img.shields.io/badge/note-mediumorchid)]() <p style="font-size: 14px;">**把眼动注视从离散 token 特征改成以注视为中心的可学习非对称高斯分布再注入奖励模型，OASST1 上 Llama-3-8B 的偏好预测准确率由 69.23 提到 74.81。**</p>

