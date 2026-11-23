# Mine Arxiv Daily Digest - 2026-11-24 (LLM / VLM 与其强化学习 Axis, 20 papers)

**Generated**: 2026-11-24 01:23 CST

**Source**: arXiv cs.CV, cs.SD, eess.AS, cs.CL, cs.AI, cs.RO, cs.LG, cs.IR submissions, listing day 2026-11-19,2026-11-20 (announced 2026-11-20 01:00 UTC（listing 11-19）、2026-11-23 01:00 UTC（listing 11-20）)

**Batch window**: 2026-11-18T19:00:00Z .. 2026-11-20T19:00:00Z（arXiv 公告批次横跨两个 UTC 日：从前一日的美东 14:00 截止时刻起算（EDT 为 18:00Z，EST 为 19:00Z），到当日的同一时刻为止）

**Axis**: llm_vlm (20 papers, base 18, cap 20)

**Directions**: llm_core (8), vlm_core (5), llm_vlm_rl (7)

**Selection**: 20 papers ranked by relevance x quality, with 0 wild-card slots

**Day total**: 60 papers across 4 axes (target 60)

**Scope**: 大语言模型与视觉语言模型的设计、推理、agent、效率与上下文工作，以及面向 LLM / VLM 的 RL 与偏好优化、奖励模型

**Wild-card**: 0 篇 —— 三个方向候选都充裕(llm_core 303 / vlm_core 132 / llm_vlm_rl 22),让出的名额全部被同轴内更靠前的论文占满,不存在「比够格论文更该进」的邻接补位。

本轴 20 篇超出基准 18,代价是 llm_vlm_rl 被硬抬到 7 篇(超自身基准 2)—— 只有当 llm_core 与 vlm_core 双双站在自身基准(8 与 5)上时,`dir_over = 2 = axis_surplus` 才放行。结构上最刺眼的是效率论文扎堆:8 篇 llm_core 里有 4 篇在做记忆、量化或 KV 压缩;而 Agent 侧的三篇评测(CompAct-Bench、AutoRAGBench、未忠实工作报告)指向同一个判断 —— 上下文管理本身已是瓶颈,而不是模型能力不够。

---

## LLM 核心（架构 / 推理 / agent / 效率 / 上下文） · `llm_core` (8 papers)

8 篇里有 4 篇在做记忆、量化与缓存压缩,另 4 篇在评测「agent 到底能不能干对」。GrepMem 的做法最激进:一条只追加的纯文本日志加一个正则搜索工具,不要 embedding、不要索引、不要额外模型,在 ContextBench 上拿到 95–97% 准确率,而有损基线最多只有 21%,在 BCP-Multi 上比 SUPO 的摘要式记忆高 8.8 个百分点。NariQ 则指出了量化评测的错位:≤3 bit 的权重量化在 AIME 上能追平 BF16,到了长程 agent 基准 DeepSWE 上,现有方法最多只解出 BF16 一半的任务;而 NariQ 在 3.0 与 2.5 bit 上与 BF16 持平。评测侧同样扎手:435 份 coding agent 工作报告里 **37.24%** 至少含一条不忠实陈述,FaithDetector 拿到 93.06% macro-F1;Beam 技术报告则把规模摆上台面 —— 501.3B 总参数、23.4B 激活,10.5K 张 GB300 上跑了 4 周、超过 1 亿条 rollout。

### 1. Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents

**arXiv**: [2611.25123](https://arxiv.org/abs/2611.25123) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, agent-memory, long-context, grep-retrieval, reinforcement-learning, context-management, University of Southern California | **Categories**: cs.AI, cs.CL | **Pages**: 17

**Authors**: Ziyan Yang; Taiwei Shi; Jieyu Zhao

**Affiliation**: University of Southern California

**Abstract**

> Long-horizon LLM agents often exceed their context windows, forcing them to discard information that may be needed later. Existing context management strategies rely on summarization, masking, or structured memory, requiring decisions about what to preserve or how to retrieve it before future needs are known. However, these methods can introduce lossy compression, potentially discarding details needed for future tasks. To address this limitation, we introduce GrepMem, a simple, lossless, and index-free memory mechanism built on two components: an append-only plain-text log of the agent's complete history and a regular-expression search tool for on-demand recall. Unlike structured memory systems, GrepMem requires no embeddings, retrieval index, memory extraction, or additional models. We train Qwen3.5-9B with reinforcement learning under five context management strategies and evaluate on multi-question research sessions, long-stream recall, and agent-trajectory question answering. GrepMem achieves 95-97% accuracy on ContextBench, versus at most 21% for lossy baselines, and outperforms SUPO's summarization by 8.8 percentage points on BCP-Multi. GrepMem scales effectively to increasingly long input streams while remaining on the accuracy-token-cost Pareto frontier across all five evaluation tasks. Our results show that a plain-text log and grep provide a simple but competitive approach to long-horizon agent memory, without requiring complex structured memory infrastructure.

**Key findings**

- **Finding**: 在 ContextBench 长流召回上，GrepMem 达到 95-97% 准确率，而 SUPO 摘要与观测掩码等有损基线最多只有 21%，且在 BCP-Multi 上比 SUPO 高 8.8 个百分点、比 MemGPT 高 7.0 个百分点。
- **Inference**: 既然完整保留原文再按需 grep 就能拿到 95% 以上召回，说明长程 Agent 的记忆瓶颈不在压缩能力，而在「事先不知道未来需要什么」这个丢弃决策本身。
- **Recommendation**: 做长程 Agent 记忆时先实现 append-only 日志加正则检索这一无损基线，再与摘要类方案在同 token 预算下对比精度与成本。

**Key figures**

*Framework - Mean Accuracy vs. Token Cost After RL. We compare four context management strategies by their mean accuracy and token usage across five evaluation tasks. SUPO compresses context through summ*

![Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents - framework](res/2611.25123_framework.png)

*Result - GREPMEM Overview. (a) The basic agent loop generates responses and tool calls from its active context, while GREPMEM additionally appends these interactions and tool results to a persistent*

![Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents - result](res/2611.25123_result.png)

**Why this ranks #1**: GrepMem 用只追加的纯文本日志加正则 grep 检索替代嵌入式结构记忆，无需嵌入、检索索引或额外模型；Qwen3.5-9B 在 ContextBench 上被训到 95-97% 准确率，而有损基线最多只有 21%，在 BCP-Multi 上还比 SUPO 的摘要高 8.8 个百分点，因此排进 llm_core 的 agent memory 首位。

---

### 2. Beam Model Technical Report

**arXiv**: [2611.26358](https://arxiv.org/abs/2611.26358) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, mixture-of-experts, model-report, reinforcement-learning, long-context, speculative-decoding, [unverified] | **Categories**: cs.AI, cs.CL | **Pages**: 156

**Authors**: Reflection Team; Adam Abdulhamid; Osama Abuelsorour; Yasmin Alameddine; Carlo Alfano; Duarte Alves; Brandon Amos; Selvaraj Anandaraj; Arseni Anisimovich; George Antoniadis; Ioannis Antonoglou; Sheila Babayan

**Affiliation**: [unverified]

**Abstract**

> Beam is a sparse Mixture-of-Experts (MoE) model with 501.3B total parameters and 23.4B active parameters, specifically built and optimized for coding, reasoning, and agentic workloads. Beam delivers frontier level reasoning, while requiring 3-4x less inference compute than many models of its class. Pretrained on 23.8T diverse, curated, high-quality tokens, Beam features a 1M-token context window achieved through a novel two-stage midtraining phase, built on verifiable, correctness-anchored data. Post-training leveraged a large-scale, fully asynchronous reinforcement learning (RL) campaign across 10.5K GB300 GPUs, generating over 100M rollouts over 4 weeks of training. We believe this is one of the largest scale RL runs conducted by any open lab to date. Across our evaluation suite, capabilities continued to improve as we increased RL compute, with no sign of a plateau. Supported by deep hardware-model co-design, FP8/NVFP4 quantization, and a 1.93B-parameter speculative decoding drafter (DFlash 2), Beam maximizes serving throughput with efficient, flexible deployment. Averaged across conversation turns and harm categories, Beam refuses or pivots on 88.9% of harmful requests while complying with 81.5% of harmless requests, achieving the highest refusal/pivot rate on harmful requests among open-weight models on the Pareto frontier.

**Key findings**

- **Finding**: Beam 全模型 52 层、每层 256 个专家、每 token 激活 8 个，总参数 501.3B 而激活参数仅 23.4B；23.8T token 预训练后在 10.5K 张 GB300 上训练 4 周，产生超过 1 亿条 rollout。
- **Inference**: 每 token 激活比例极低说明它的单步推理算力主要由 23.4B 激活参数决定，这也是它宣称比同级模型省 3-4 倍推理算力的根源，而不是来自更小的总参数。
- **Recommendation**: 自建开源 MoE 基线时可直接复用其「52 层、49 个 MoE 层、3 个 dense 层、局部与全局注意力 5:1」的配置与无辅助损失负载均衡思路。

**Key figures**

*Framework - Beam’s expert utilization over pretraining. The curve shows the busiest expert’s load divided by the uniform-routing load, averaged across MoE layers; the dashed line marks perfect balance.*

![Beam Model Technical Report - framework](res/2611.26358_framework.png)

*Result - Beam training loss in bits per byte (logarithmic scale) over the course of its pretraining run.*

![Beam Model Technical Report - result](res/2611.26358_result.png)

**Why this ranks #2**: Beam 是 501.3B 总参数、23.4B 激活参数的稀疏 MoE：52 层中每层 256 个专家、每 token 只激活 8 个，23.8T token 预训练后又用 10.5K 张 GB300 跑 4 周产生超过 1 亿条 rollout，是本轮开源 MoE 里规模与 RL 投入都最大的一篇，故进 llm_core 第一梯队。

---

### 3. Search From the Start: Search-Native Pretraining for Language Models

**arXiv**: [2611.26809](https://arxiv.org/abs/2611.26809) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, search-native-pretraining, retrieval-augmented, tool-use, knowledge-intensive, open-weights, EPFL | **Categories**: cs.AI, cs.CL, cs.LG | **Pages**: 26

**Authors**: Kaustubh Ponkshe; Gyung Hyun Je; Stefan Taga; Colin Raffel; Martin Jaggi

**Affiliation**: EPFL; University of Toronto

**Abstract**

> Modern language models (LMs) are increasingly deployed with access to search tools at inference. Yet pretraining remains predominantly focused on predicting static text, with search capabilities typically introduced during post-training. We propose Search-Native Pretraining as a practical route to teach search capability during pretraining from ordinary text corpora. Specifically, we augment pretraining corpus at scale with web-search queries and retrieve web response using a local index. Training on this augmented corpus teaches models to generate search calls and incorporate retrieved evidence during language modeling. Across Wikipedia and DCLM-Edu corpora and 360M to 3.3B parameter scales, search-pretrained models ("QueryLM") show improved performance on knowledge-intensive tasks and higher steerability toward the retrieved evidence. Crucially, their advantage persists after supervised fine-tuning of both search-pretrained and conventionally pretrained models, indicating that the tested post-training procedures do not fully recover the capabilities developed during pretraining. Throughout our experiments, we find that a 1.4B QueryLM consistently beats or matches the performance of a FLOP-matched 3.3B baseline model across all knowledge intensive tasks. These results establish search-pretraining as a practical way to develop foundational search capabilities during pretraining. We release the training artifacts, including model checkpoints and data.

**Key findings**

- **Finding**: 在 Wikipedia 与 DCLM-Edu 两个语料、360M 到 3.3B 参数规模上，搜索预训练得到的 QueryLM 在知识密集任务上普遍优于同算力的常规预训练模型，其中 1.4B QueryLM 稳定追平或超过 FLOP 对齐的 3.3B 基线。
- **Inference**: 1.4B 顶住 3.3B 说明检索证据带来的信息增益高于参数量带来的算力增益；且该优势在 SFT 之后仍然存在，说明现有后训练流程补不回预训练期形成的搜索能力。
- **Recommendation**: 复现时用本地索引为语料批量配查询与响应，先在 1.4B 规模验证「小模型加搜索」是否抵得过更大的 FLOP 对齐基线，再决定是否放大。

**Key figures**

*Framework - QueryLM is better at searching for and using evidence. (a) After Search-Native Pretrain- ing, QueryLM with search outperforms the compute-matched baseline and the largest open-weight base mo*

![Search From the Start: Search-Native Pretraining for Language Models - framework](res/2611.26809_framework.png)

*Result - Search-Native Pretraining pipeline overview. (1) We augment training documents with inline search queries and corresponding search results, intended to contain useful knowledge for predictin*

![Search From the Start: Search-Native Pretraining for Language Models - result](res/2611.26809_result.png)

**Why this ranks #3**: Search-Native Pretraining 直接在预训练语料中注入网页搜索查询并用本地索引取回响应，训出的 1.4B QueryLM 在全部知识密集任务上稳定追平或超过 FLOP 对齐的 3.3B 基线，说明搜索能力可以被前置到预训练阶段，因此归入 Pretraining 而非后训练话题。

---

### 4. NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks

**arXiv**: [2611.26157](https://arxiv.org/abs/2611.26157) | **Score**: 8.4 (relevance 9 x 0.7 + quality 7 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, quantization, agentic-tasks, trellis-coding, post-training, long-horizon, Nari Labs | **Categories**: cs.LG | **Pages**: 7

**Authors**: Doyeob Kim

**Affiliation**: Nari Labs

**Abstract**

> Long-horizon agentic tasks require a model to call tools over many steps at contexts of 100K tokens or more, yet many low-bit quantization methods are calibrated on short web text and judged on perplexity. This mismatch is costly: existing quantizations of Qwen3.8-27B at or below 3 bits per weight match BF16 on shorter tasks like AIME, yet in published results solve at most 72% as many tasks as BF16 on DeepSWE, a long-horizon agentic benchmark. We propose NariQ, a trellis-coded post-training quantization method that calibrates on tokens generated by the BF16 model in agent sessions. On Qwen3.8-27B, NariQ at 3.0 and 2.5 bits per weight stays level with BF16 on two long-horizon agentic benchmarks, DeepSWE and Terminal Bench, as well as on AIME and RealWorldQA. Our checkpoint at 2.0 bits per weight trails this performance. To our knowledge, these are the first quantizations at or below 3 bits per weight shown to match their full-precision version on long-horizon agentic tasks. We release the files as Qwen3.8-27B-NariQ-GGUF (https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF), with inference available through our llama.cpp fork at https://github.com/nari-labs/nari-llama.cpp.

**Key findings**

- **Finding**: NariQ 在 3.0 与 2.5 bit 权重下 DeepSWE 得分分别为 84.9% 与 84.5%，按任务配对高于 BF16 的 83.0%（+1.9 与 +1.5 分），而此前 3 bit 以下文件最多只解出 BF16 的 72% 任务。
- **Inference**: 差距根源是校准分布不匹配——在网页短文本上校准、在困惑度上评测，反映不了 Agent 会话里真正需要算对的那批 token；trellis 编码的 agent KL 比 GPTQ+GSQ 低 3.2 倍。
- **Recommendation**: 评估低比特模型必须上 DeepSWE、Terminal Bench 这类长程 Agent 基准，只看 AIME 与困惑度会严重高估 3 bit 以下量化的真实可用性。

**Key figures**

*Framework - Development sequence at 3.0 bpw, ending at an earlier checkpoint. Trellis coding has 3.2× lower agent KL than GPTQ+GSQ, with the scalar search’s probabilities re-rounded under trellis costs.*

![NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks - framework](res/2611.26157_framework.png)

**Why this ranks #4**: NariQ 用 trellis 编码做后训练量化，把校准数据换成 BF16 模型在 Agent 会话中实际生成的 token，使 Qwen3.8-27B 在 3.0 与 2.5 bit 权重下 DeepSWE 得分 84.9% 与 84.5%、反超 BF16 的 83.0%，而此前 3 bit 以下方案最多只解出 BF16 的 72% 任务。

---

### 5. QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers

**arXiv**: [2611.27901](https://arxiv.org/abs/2611.27901) | **Score**: 8.3 (relevance 8 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, kv-cache, quantization, visual-geometry, streaming, inference-efficiency, University of Hong Kong | **Categories**: cs.CV | **Pages**: 19

**Authors**: Zunhai Su; Keyu Fan; Ruishan Guo; Zhongzhu Zhou; Jingzehua Xu; Bohan Sun; Hansen Feng; Ruihan Hu; Yik-Chung Wu; Ngai Wong

**Affiliation**: The University of Hong Kong; Tsinghua University; The University of Sydney; University of Chinese Academy of Sciences; Harbin Institute of Technology

**Abstract**

> Streaming visual geometry transformers retain historical key-value (KV) states as cross-view geometric memory, but growing caches constrain long-sequence inference. We systematically characterize KV quantization in streaming geometry and uncover two linked challenges: Nonuniform Geometric Sensitivity and Cache-Geometry Mismatch. Quantization sensitivity varies across precision choices and cache locations, while perturbed retrieval changes geometry-head inputs and propagates through subsequent predictions and KV writes. Guided by these findings, we propose QuantStream3D, to our knowledge the first dedicated KV quantization framework for streaming visual geometry transformers. Geometry-Guided Mixed-Precision KV Quantization protects sensitive cross-view evidence, while Geometry-Aligned Quantization-Aware Distillation jointly adapts transformer blocks and geometry heads on student-generated quantized history. Across five benchmarks and two backbones, QuantStream3D achieves near-lossless geometric accuracy in most settings with predominantly 2-bit KV caches, and many configurations surpass unquantized inference. Compared with LLM-oriented KV quantizers, it reduces TUM absolute trajectory error and NeuralRGBD completeness error by up to 57.4% and 69.7%, respectively. Integration with existing native cache-pruning methods further pushes compression while improving reconstruction quality on NeuralRGBD. Our optimized StreamVGGT backend achieves $5.05\times$ physical KV compression and 23.1% lower latency at batch size one. Under a fixed memory budget on the same GPU, it supports $5.4\times$ the maximum batch size and up to $1.67\times$ the peak throughput of unquantized inference. Code and pretrained checkpoints will be made publicly available.

**Key findings**

- **Finding**: 相对面向 LLM 的 KV 量化器，QuantStream3D 把 TUM 绝对轨迹误差降低最多 57.4%、NeuralRGBD 重建完整度误差降低 69.7%；优化后的 StreamVGGT 后端在 batch size 1 下有 5.05 倍物理 KV 压缩与 23.1% 更低延迟。
- **Inference**: 流式几何任务的 KV 缓存承载跨视角证据，量化误差会改写几何头的输入并沿后续预测与 KV 写入传播，因此必须按几何敏感度混合分配精度而不能全局统一位宽。
- **Recommendation**: 做流式 3D 推理时按「敏感跨视图证据保 4 bit、其余降到 2 bit」分层量化，并以轨迹误差而非仅重建指标验收效果。

**Key figures**

*Framework - Overview of QuantStream3D. (1) Geometry-Guided Mixed-Precision KV Quantization combines paired Q/K rotation and per-channel K/V quantization. All first-frame writes and all writes at global-*

![QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers - framework](res/2611.27901_framework.png)

*Result - Layer sensitivity across tasks. Joint K/V precision drops from 4 to 2 bits at one global-attention layer; all others remain at 4 bits. Relative degradation is measured from each backbone’s a*

![QuantStream3D: Geometry-Aligned Low-Bit KV Cache Quantization for Streaming Visual Geometry Transformers - result](res/2611.27901_result.png)

**Why this ranks #5**: QuantStream3D 是首个面向流式视觉几何 Transformer 的专用 KV 量化框架，在 5 个基准、2 个骨干上以主流量 2-bit KV 缓存逼近无损，相对 LLM 量化器把 TUM 绝对轨迹误差降低最多 57.4%、NeuralRGBD 完整度误差降低 69.7%，并实现 5.05 倍物理压缩。

---

### 6. AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development

**arXiv**: [2611.25582](https://arxiv.org/abs/2611.25582) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, rag, llm-agent, benchmark, retrieval, agentic-workflow, Tsinghua University | **Categories**: cs.AI, cs.CL, cs.IR | **Pages**: 15

**Authors**: Hang Zhang; Yuzhi Pan; Ziyao Zhong; Chaokun Wang; Shuo Cao; Zeyu Huang; Yue Xue; Fang Niu; Bofan Xie; Guanchen Ge; Zecheng Li; Leqi Zheng

**Affiliation**: Tsinghua University, Beijing, China; Sina Weibo Corp, Beijing, China

**Abstract**

> Retrieval-augmented generation (RAG) is a well-established paradigm for augmenting large language models (LLMs) with information retrieved from external corpora. However, developing effective RAG systems requires substantial engineering effort and iterative experimentation, as effective design choices vary across tasks and domains. With rapid advances in LLM agent capabilities, we ask how well these agents can autonomously build RAG systems and how effectively they can improve them through iteration. In this paper, we propose AutoRAGBench, the first benchmark to evaluate how well LLM agents develop RAG systems from scratch in an open code space. It comprises nine RAG system development tasks. For each task, agents build RAG systems from scratch without starter code or prescribed strategies, under a six-hour budget on a single H800 GPU. They analyze task data, implement RAG pipelines, and iteratively refine their designs based on experimental feedback. We evaluate nine agent configurations and analyze both the effectiveness of the resulting RAG systems and their development trajectories. GPT-6.1 Sol with Codex CLI achieves the highest average score of 56.1. The composite Human-SOTA baseline averages 44.4. These results show that LLM agents can automate effective RAG system development. When starting from a human-designed system on each of seven tasks, GPT-6.1 Sol with Codex CLI improves the score by 16.6 points on average.

**Key findings**

- **Finding**: 在 9 个 RAG 开发任务、单张 H800、每个 6 小时预算下，GPT-6.1 Sol 搭配 Codex CLI 取得最高平均分 56.1，比人类 SOTA 组合基线 44.4 高 11.7 分，比参考 RAG 系统高 9.7 分，并在 7 个任务上单项最优。
- **Inference**: 同一个人工设计系统被 Agent 接手后还能平均再涨 16.6 分，说明 Agent 的价值主要在于按实验反馈迭代调参，而不是从零发明新的检索结构。
- **Recommendation**: 评估「Agent 能否自动做 RAG 工程」时，应像该基准一样给定单卡 6 小时预算，按任务平均分而非单任务最优来比较。

**Key figures**

*Framework - Building a RAG assistant for internal documents. Developers spend considerable time and effort implementing, testing, and refining RAG methods, whereas an LLM agent can efficiently refine the*

![AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development - framework](res/2611.25582_framework.png)

*Result - AutoRAGBench pipeline.*

![AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development - result](res/2611.25582_result.png)

**Why this ranks #6**: AutoRAGBench 让 LLM Agent 在开放代码空间从零搭 RAG：9 个开发任务、单张 H800、每个 6 小时预算，GPT-6.1 Sol 配 Codex CLI 拿到平均 56.1 分，比人写的组合基线 44.4 高 11.7 分，接手人工系统后还能再提 16.6 分，是 RAG 工程自动化最直接的证据。

---

### 7. CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks

**arXiv**: [2611.25673](https://arxiv.org/abs/2611.25673) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, context-compaction, long-context, benchmark, agent-memory, context-management, Fudan University | **Categories**: cs.AI | **Pages**: 61

**Authors**: Jiayi Chen; Lizhe Chen; Yujia Chen; Shihan Dou; Ming Zhang; Chendi Ge; Shiguang Ni; Tao Gui; Qi Zhang; Xuanjing Huang; Maxm Pan

**Affiliation**: Fudan University; Hunyuan Team, Tencent; SIGS, Tsinghua University

**Abstract**

> As language-model agents are applied to increasingly extended tasks, their working context continuously accumulates interaction history, tool observations, intermediate decisions, and task progress. Context compaction offers a practical way to reduce this growing history while allowing execution to continue, yet the compaction ability of modern LLMs remains insufficiently understood. We introduce CompAct-Bench, a benchmark for evaluating working-context compaction through its downstream effect on agent task completion. Starting from successful agent trajectories, we insert compaction boundaries at different stages of execution, compress the preceding working context with the model under evaluation, and let the same executor continue the original task. To enable fair comparison across compactors, we evaluate them under controlled retention ratios using a lightweight iterative ratio-adjustment procedure. CompAct-Bench covers information-seeking, software-engineering, and workspace-oriented tasks through BrowseComp, SWE-bench, and an internal CompanyBench evaluation. Our experiments show that working-context compaction remains highly lossy even for frontier models: Claude- and GPT-family models perform strongest overall, yet substantial degradation in downstream task accuracy persists under aggressive compaction. Further analysis reveals that failures are often caused not only by omitted information, but also by distorted task state, such as turning unresolved issues into apparent conclusions or forgetting previously established results, which can lead to incorrect decisions or redundant execution. These findings highlight working-context compaction as a distinct and still challenging ability for LLMs operating in extended agent tasks.

**Key findings**

- **Finding**: CompAct-Bench 用 200 个成功轨迹（79 个 BrowseComp、96 个 SWE-bench、25 个 CompanyBench）在执行中途插入压缩边界，再由同一执行器续跑，用最终任务完成度直接衡量压缩效果。
- **Inference**: 失败不仅来自信息缺失，还来自任务状态被扭曲——未解决的问题被压缩成已有结论、此前已建立的结果被遗忘，从而导致错误决策与重复执行。
- **Recommendation**: 设计长程 Agent 的上下文压缩时，优先保住「未决事项」与「已验证结论」两类状态，而不是单纯追求压缩比。

**Key figures**

*Framework - Overview of CompAct-Bench. We collect successful long-horizon trajectories, compact their working context at intermediate execution boundaries, and evaluate whether the agent can complete t*

![CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks - framework](res/2611.25673_framework.png)

*Result - Post-compaction accuracy across compaction boundaries for Search, Coding, and Workspace. Model reasoning settings follow Table 2.*

![CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks - result](res/2611.25673_result.png)

**Why this ranks #7**: CompAct-Bench 在成功轨迹中途插入压缩边界来评测工作上下文压缩，覆盖 79 个 BrowseComp、96 个 SWE-bench 与 25 个 CompanyBench 任务共 200 项；结果显示 Claude 与 GPT 系列在激进压缩下仍明显掉点，说明压缩本身是尚未解决的独立能力。

---

### 8. Characterizing and Detecting Unfaithful Work Reports by Coding Agents

**arXiv**: [2611.25760](https://arxiv.org/abs/2611.25760) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, coding-agent, hallucination, faithfulness, detector, empirical-study, Peking University | **Categories**: cs.AI, cs.SE | **Pages**: 21

**Authors**: Wenhao Yang; Runzhi He; Minghui Zhou; Pengfei Gao; Dayi Lin; Qingwei Lin; Dongmei Zhang

**Affiliation**: Peking University, China; Microsoft

**Abstract**

> Coding agents increasingly carry out long-horizon development tasks, autonomously planning and executing multi-step actions that span files, tools, and sessions. Because developers rarely follow each action, and agents resuming the work depend on records of what was done, the agent's work report often becomes the primary account of what was changed and established. When the report contains false or unsupported claims, it gives recipients false assurance: incomplete work may be accepted without verification, incorrect assumptions about the current state can propagate to later steps and agents, and evaluators that credit stated success may reward the report rather than the work. Yet little is known about what unfaithful reporting looks like in real development work, or how developers and agents handle it once it surfaces. Starting from real developer-agent conversations in SWE-chat, we conduct a systematic mixed-methods analysis of self-admitted unfaithful reports. We identify eleven subtypes in four categories: misreported observations, misattributed evidence, overstated task success, and faulty technical explanations, with overstated task success the most common. Handling these problems involves on average 4.3 further user turns and 12.71 minutes of recorded response and execution time, and users express dissatisfaction more often. Among 435 work reports that we separately sample and annotate, 37.24% contain at least one unfaithful claim. We also develop FaithDetector, a detector for unfaithful reporting informed by the observed patterns. On naturally sampled reports, FaithDetector attains 93.06% macro-F1, about 13 percentage points above the baseline. Together, our findings and FaithDetector provide empirical evidence and an automated method for checking reporting faithfulness, informing agent evaluation and training feedback.

**Key findings**

- **Finding**: 在 339 条失实声明上归纳出 4 类 11 种模式，其中夸大任务成功占 69.3%；另抽样标注 435 份工作报告，有 162 份（37.24%）至少含一条不实陈述。
- **Inference**: 用户平均要再花 4.3 轮对话和 12.71 分钟才能纠正这些问题，说明失实报告的代价主要落在人工复核环节，而不是模型内部可以自动消化的。
- **Recommendation**: 把 Coding Agent 的工作报告接入 FaithDetector 这类后置检测作为验收闸门，尤其对「已完成、已修复」这类高风险声明单独抽查。

**Key figures**

*Framework - Motivating example from SWE-chat. The agent reports a database-initialization fix, but its schema routine discards all SQL statements.*

![Characterizing and Detecting Unfaithful Work Reports by Coding Agents - framework](res/2611.25760_framework.png)

*Result - Overview of the study methodology.*

![Characterizing and Detecting Unfaithful Work Reports by Coding Agents - result](res/2611.25760_result.png)

**Why this ranks #8**: 该文从 SWE-chat 真实开发对话归纳出 4 类 11 种失实报告模式（夸大任务成功占 69.3%），在 435 份抽样工作报告里发现 37.24% 含至少一条不实陈述，其提出的 FaithDetector 以 93.06% macro-F1 检测、比基线高约 13 个百分点，是 Coding Agent 可信度评估的第一手实证。

---

## VLM 核心（多模态架构 / 理解 / 视频 / GUI agent） · `vlm_core` (5 papers)

5 篇的共同问题只有一个:**几何是从像素读出来的,还是语义先验猜出来的**。StereoVLM 用标定双目消除多视图几何歧义,8B 模型在 Stereo3D-Bench 上做到 95.17% 的 δ1 深度精度、66.98 的物体级平均分,层级化几何监督在五个空间基准上平均 +3.54 分;干预实验直接证明收益来自有效的跨视图几何,而不是「多塞了几个视觉 token」。TuringSpace 用 125 个交互式 CAPTCHA 反问同一件事:人类解对 94.1%,GPT-6 Astra 仍失败 25.9%,失败多源于「读错截图后,推理反而为错误信念编造证据」。反幻觉训练也被拆账:一个只训练 11 个特征、500 张标注的后置探针,在 8 种方法里有 7 种能复现「超出少说话」部分的三分之二收益。SKILL.PNG 则把 skill 搬进像素空间,推理只占 64–256 个图像 token,文本 skill 要 900–2000 个。

### 9. StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning

**arXiv**: [2611.27915](https://arxiv.org/abs/2611.27915) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, stereo-vision, spatial-reasoning, metric-depth, disparity, benchmark, Hong Kong University of Science and | **Categories**: cs.AI, cs.CV, cs.RO | **Pages**: 29

**Authors**: Chi Yan; Guoyang Zhao; Wentao Yuan; Yixiao Ge; Yanning Zhou; Dan Xu

**Affiliation**: The Hong Kong University of Science and Technology (HKUST); XPENG Robotics

**Abstract**

> Vision-language models (VLMs) exhibit strong semantic understanding but remain limited in their ability to reason about metric 3D space in the physical world. Existing VLMs typically infer 3D scene structure from one or more images without known camera calibration or cross-view geometric constraints. This makes metric 3D inference inherently ambiguous and leaves it unclear whether their spatial predictions are grounded in visual evidence or driven primarily by semantic priors. In contrast, calibrated stereo provides explicit cross-view geometry that resolves this ambiguity and offers a more reliable foundation for metric 3D perception and geometric generalization. We investigate how VLMs can learn transferable 3D representations directly from calibrated binocular observations. To this end, we introduce StereoVLM, the first geometry-aware binocular VLM for metric 3D spatial reasoning. StereoVLM follows a hierarchical learning paradigm spanning from cross-view correspondence and disparity estimation to calibration-conditioned metric depth perception and semantic spatial reasoning. We further find that disparity supervision generalizes substantially better than direct binocular depth supervision on unseen environments. To evaluate these capabilities, we introduce Stereo3D-Bench, a comprehensive benchmark across three levels, from point-level geometry to object-level spatial reasoning. StereoVLM-8B achieves 95.17% depth accuracy ($δ_1$) and a 66.98 average object-level score on Stereo3D-Bench. Intervention results further indicate that the model's performance on Stereo3D-Bench benefits from valid cross-view geometry and cannot be explained solely by additional visual tokens or semantic priors. Hierarchical geometric supervision also yields average gains of 3.54 points across five spatial benchmarks and 4.3 percentage points in RoboCasa manipulation success.

**Key findings**

- **Finding**: StereoVLM-8B 在 Stereo3D-Bench 上深度 δ1 达 95.17%、物体级均分 66.98，同双目输入协议下把对应 MAE 从 GPT-6 Astra 的 9.27 像素降到 3.80 像素、视差 MAE 从 7.55 降到 3.76。
- **Inference**: 同一协议下换成强通用模型差距这么大，说明度量化 3D 推理的收益来自显式的跨视角几何约束，而不是更多的视觉 token 或语义先验。
- **Recommendation**: 训练带尺度的 3D 感知模型时应先学视差再学深度，因为论文发现视差监督在未见环境上的泛化明显优于直接的双目深度监督。

**Key figures**

*Framework - StereoVLM: from binocular geometry to spatial understanding and action. (a) Monocular observations leave metric scale ambiguous. (b) An illustrative example of language-grounded metric reaso*

![StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning - framework](res/2611.27915_framework.png)

*Result - Construction and task hierarchy of Stereo3D-Bench. (a) The main split is constructed from four stereo data sources. Independently selected point- and object-level subsets contain 2,017 and 1*

![StereoVLM: Binocular Vision-Language Models for Metric 3D Spatial Reasoning - result](res/2611.27915_result.png)

**Why this ranks #9**: StereoVLM 用标定双目观测训练首个几何感知双目 VLM，配 2,017 对点级、1,556 对物体级立体数据共 94,546 条问答的 Stereo3D-Bench；8B 模型深度 δ1 达 95.17%、物体级均分 66.98，把对应 MAE 从 9.27 降到 3.80 像素。

---

### 10. SKILL.PNG: Learning Agent Skills in Pixel Space

**arXiv**: [2611.26296](https://arxiv.org/abs/2611.26296) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, visual-prompt, agent-skill, gradient-optimization, vlm, prompt-efficiency, Hasso Plattner Institute | **Categories**: cs.CV, cs.LG | **Pages**: 13

**Authors**: Maximilian Seeth; Chengzhi Martin Hu; Marie Kempkes; Paul Röttger; Leo Schwinn

**Affiliation**: Hasso Plattner Institute; Technical University of Munich; Helmholtz AI; Volkswagen Group Innovation

**Abstract**

> AI agents are commonly specialized for new tasks and domains using skills, i.e. natural language instructions placed in their context. However, the discrete nature of textual skills prevents continuous optimization. Gradient-based approaches such as finetuning, on the other hand, are typically model-specific, preventing skill transfer across different agents. Since many agents today are built on vision-language models (VLMs), we can address these limitations by introducing Skill$.$png: a method for obtaining skill-like image inputs whose pixels are optimized with gradient descent through the vision encoder of a frozen VLM. Image skills are compatible with any VLM, and a single image can be optimized jointly for an ensemble of models. We show that Skill$.$png significantly outperforms state-of-the-art textual skills optimized using frontier LLMs in 9 of 16 settings (across 4 VLMs and 4 benchmarks) while requiring only 64 to 256 image tokens instead of roughly 900 to 2000 text tokens at inference time. Hybrid skills, i.e. text and image skills jointly optimized, further improve agent performance. Moreover, an image optimized with an ensemble of VLMs can successfully transfer across the models in the ensemble. Skill$.$png thus presents the first agent skill that can be optimized with gradient descent while retaining transfer benefits of text skills. Our code is available at: https://github.com/omseeth/skill.png

**Key findings**

- **Finding**: SKILL.PNG 在 4 个 VLM、4 个基准共 16 组设定中有 9 组显著优于 SkillOpt 的文本技能，相对无技能基线最高提升 37.8 分，而推理只需 64-256 个图像 token，对应文本技能约需 900-2000 个 token。
- **Inference**: 文本技能的离散性既挡死了梯度优化也抬高了 token 成本，把技能编码成可微图像等于同时拿回可优化性与推理效率这两件事。
- **Recommendation**: 为 VLM Agent 设计技能时先试一张可优化的「技能图」，与文本技能在同 token 预算下比得分，而不是只比最终准确率。

**Key figures**

*Framework - Three ways to improve agents. Text skills work with any model but cannot be optimized with gradients. LoRA is trained with gradients, but is model-specific. SKILL.PNG (ours) encodes the skil*

![SKILL.PNG: Learning Agent Skills in Pixel Space - framework](res/2611.26296_framework.png)

*Result - Length of text and image skills. Tokens per skill and model, averaged over the four benchmarks, with error bars showing one standard deviation across them. For SKILL.PNG, these are image tok*

![SKILL.PNG: Learning Agent Skills in Pixel Space - result](res/2611.26296_result.png)

**Why this ranks #10**: SKILL.PNG 把 Agent 技能从离散文本搬到像素空间，用梯度下降穿过冻结 VLM 的视觉编码器直接优化图像技能，在 4 个 VLM 乘 4 个基准的 16 组设定中 9 组显著超过 LLM 优化的文本技能，且推理只占 64-256 个图像 token。

---

### 11. TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs

**arXiv**: [2611.25387](https://arxiv.org/abs/2611.25387) | **Score**: 8.3 (relevance 8 x 0.7 + quality 9 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, gui-agent, spatial-reasoning, benchmark, synthetic-environment, interactive-task, University of Pennsylvania | **Categories**: cs.LG | **Pages**: 45

**Authors**: Xuwei Ding; Skylar Zhai; Linxin Song; Jiarui Feng; Dongqi Fu; Huajun Xi; Junnan Li; Jingcheng Liang; Jieyu Zhao; Yinglong Xia; Hong Li; Jian Kang

**Affiliation**: University of Pennsylvania; University of Minnesota; University of Southern California; Meta; MBZUAI

**Abstract**

> Humans act in the visual world by inferring the 3D layout behind a 2D view, predicting how an action changes it, and correcting themselves after seeing the result. Can multimodal large language models (MLLMs) do the same? CAPTCHAs offer a natural test, since humans solve them through this very loop, clicking and dragging on the screen and adjusting after each result. Yet existing CAPTCHA benchmarks are largely solved and rarely spatial, while spatial benchmarks rarely require action. We therefore present TuringSpace, a synthetic web environment of 125 interactive CAPTCHAs that span five spatial abilities and must be solved through clicks and drags on the screen. Every task is a program that generates new instances with a checker and an oracle, so the tasks also form a scalable training gym. Humans solve 94.1% of the tasks, whereas the best model, GPT-6 Astra, still fails 25.9% of them, and the best open-weight model, Kimi K3, fails 68.0%. Our further analysis shows that most failures come from misreading the screenshot, and that model reasoning rarely corrects a wrong belief but hallucinates evidence to defend it. To test whether such spatial abilities can be learned, we fine-tune Qwen3.5-9B on this gym. Its success rate rises from 1.6% to 33.1%, above Kimi K3, and it improves on all seven out-of-distribution benchmarks, including a 9.9-point gain on the real-world indoor videos of VSI-Bench. These results show that grounding spatial intelligence in screen actions exposes what MLLMs lack and offers a scalable way to teach it, with gains that transfer to real-world scenes. We will release TuringSpace to support further study.

**Key findings**

- **Finding**: 在 125 个必须靠点击与拖拽才能完成的交互式 CAPTCHA 上，人类通过率 94.1%（平均 33.1 秒），GPT-6 Astra 仍有 25.9% 失败，最佳开源模型 Kimi K3 失败 68.0%，而微调后的 TuringSpace-9B 把成功率从 1.6% 提到 33.1%。
- **Inference**: 失败主要来自读错截图，且模型极少纠正自己的错误认知，反而会编造证据为错误辩护，说明瓶颈在感知而不是推理链长度。
- **Recommendation**: 用这类交互式 CAPTCHA 训练 GUI Agent 时，应把「观察—动作—反馈」闭环当作训练信号，并在 7 个分布外基准上验证迁移效果。

**Key figures**

*Framework - (a) Failure rate (%) of nine MLLMs on TuringSpace-Bench and two CAPTCHA bench- marks; every model fails more often on TuringSpace- Bench than on both. (b) Success rate (%) of Qwen3.5- 9B, Qwen3.5-27B, and TuringSpace-9B on seven out-of-dist*

![TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs - framework](res/2611.25387_framework.png)

*Result - Overview of TuringSpace. Top: two of the 25 tasks in each of the five categories, with the instruction, start state, solved state, and a tag for how the player acts (tap, drag, or step); spat*

![TuringSpace: Grounding Spatial Intelligence in Action with Interactive CAPTCHAs - result](res/2611.25387_result.png)

**Why this ranks #11**: TuringSpace 用 125 个可交互 CAPTCHA 组成五类空间任务、每类 25 个，必须在屏幕上点击与拖拽完成；人类通过率 94.1%，最强的 GPT-6 Astra 仍失败 25.9%、最佳开源 Kimi K3 失败 68.0%，微调 Qwen3.5-9B 后成功率从 1.6% 升到 33.1%。

---

### 12. What Does Anti-Hallucination Training Buy? Saying Less, Cheap Pruning, and the Rest

**arXiv**: [2611.25814](https://arxiv.org/abs/2611.25814) | **Score**: 8.3 (relevance 8 x 0.7 + quality 9 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, hallucination, evaluation-methodology, probe, dpo, object-hallucination, Key Laboratory of Computing Power Network | **Categories**: cs.CL, cs.CV | **Pages**: 17

**Authors**: Lingkai Bu; Qian Gao

**Affiliation**: Key Laboratory of Computing Power Network and Information Security, Ministry of Education; Shandong Computer Science Center (National Supercomputer Center in Jinan); Qilu University of Technology (Shandong Academy of Sciences), Jinan, China

**Abstract**

> Preference training is the standard recipe for reducing object hallucination in vision-language models, and each new method reports a lower CHAIR score. We ask what that reduction consists of. Every trained system is compared with its base model's caption truncated to the same object recall, which removes the part of the gain that comes from saying less; the remainder is compared with what a deliberately weak, frozen, eleven-feature post-hoc probe fitted on 500 annotated images can reproduce. All criteria were specified in the analysis code and frozen before the outputs they judge existed. For eight public methods on LLaVA-1.5-7B, the probe reproduces at least two thirds of what training removes beyond saying less for 7 of 8 methods on COCO, 8 of 8 on AMBER and 6 of 8 on Object HalBench, with RLAIF-V the consistent exception; a later public method released for both LLaVA-1.5 and Qwen2.5-VL (SENTINEL) meets the same bar on both. On our own DPO checkpoints the accounting holds on Qwen2.5-VL but fails on InternVL2.5 on COCO (2 of 4 training designs). At matched recall, the base model plus the probe beats truncation for 8 of 9 LLaVA-1.5 systems on COCO and 9 of 9 on AMBER, on the two newer backbones, and when realized as actual sentence deletion. The same measure prices training signals: DPO on the model's own samples labelled by the probe or by an object-level CLIP score recovers 0.70 and 0.87 of the beyond-brevity gain of ground-truth-labelled DPO on Qwen2.5-VL (the probe 0.73 on InternVL2.5), both beat length-matched random labels, and CLIP labels buy more than probe labels on COCO. Human judgements show that the sentences the probe deletes are wrong more often than those truncation would delete; a human check of the CHAIR evaluator's precision falls below our pre-set bar, which we report as a limitation.

**Key findings**

- **Finding**: 对 LLaVA-1.5-7B 上 8 个公开方法，这个在 500 张标注图上拟合的 11 特征冻结探针在 COCO 上复现了 7 个方法超出部分的三分之二以上，在 AMBER 上是 8 个全中、Object HalBench 上 6 个，RLAIF-V 是唯一例外。
- **Inference**: 若大部分「训练带来的提升」都能被一个故意做弱的冻结后处理探针复现，那么很多抗幻觉方法的净贡献其实只是更保守地少说，而不是更强的语言能力。
- **Recommendation**: 评测新的抗幻觉训练时必须加上「同召回率下截断基模型描述」与「基模型加冻结探针」两条对照，否则 CHAIR 下降会被误读成能力提升。

**Key figures**

*Framework - What training removes, decomposed. Unit: hallucinated objects of the base model’s captions that a trained system no longer mentions on held-out images (= 100%). Light blue: removed by positi*

![What Does Anti-Hallucination Training Buy? Saying Less, Cheap Pruning, and the Rest - framework](res/2611.25814_framework.png)

**Why this ranks #12**: 该文把抗幻觉训练的收益拆成少说、廉价剪枝与剩余三块，用一个在 500 张标注图上拟合的 11 特征冻结探针做对照：在 LLaVA-1.5-7B 的 8 个公开方法里，有 7 个（COCO）、8 个（AMBER）、6 个（Object HalBench）的超额提升能被探针复现。

---

### 13. VisAlloc: Allocating Visual Supervision for On-Policy Self-Distillation

**arXiv**: [2611.25069](https://arxiv.org/abs/2611.25069) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, self-distillation, on-policy, visual-supervision, token-reweighting, multimodal-reasoning, Zhejiang University | **Categories**: cs.AI, cs.CV | **Pages**: 12

**Authors**: Haoran Xu; Tian Chen; Yuhe Wu; Yanbo Zhao; Junchi Liao; Hongyu Wang; Jiaze Li; Wentao Wang; Yanfeng Li; Rui Qian

**Affiliation**: Zhejiang University; Fudan University; The Hong Kong University of Science and Technology (Guangzhou); The Chinese University of Hong Kong; University of Electronic Science and Technology of China

**Abstract**

> On-policy self-distillation (OPSD) offers a promising approach to improving visual reasoning in multimodal large language models (MLLMs). However, not all samples benefit equally from privileged visual guidance, and uniform token supervision can dilute visually grounded signals. We propose VisAlloc, a dual-level framework combining sample-level visual filtering with token-level counterfactual reweighting. A fixed paired-teacher filter retains samples answered correctly from an evidence-centered positive crop but incorrectly from a spatially displaced negative crop. At the token level, both EMA teachers score the same student-generated response, and their absolute log-probability differences measure view sensitivity. Additional supervision targets tokens admitted by sensitivity or teacher-distribution disagreement, with shared frozen-prior, template-bigram, and student--teacher divergence gates. Inverse-frequency redistribution preserves the total additional weight within each micro-batch, while the positive teacher remains the sole distillation target. Inference requires only the full-image student. Across eight benchmarks, our 4B and 9B models achieve macro-averages of 81.44 and 84.92, outperforming Vision-OPD reproductions by 0.97 and 0.52 points, respectively. Code on GitHub: https://github.com/Kaelyn01/VisAlloc

**Key findings**

- **Finding**: VisAlloc 在 8 个基准上的宏平均为 4B 模型 81.44、9B 模型 84.92，分别比 Vision-OPD 复现高 0.97 与 0.52 分，且推理阶段只需完整图像的学生模型。
- **Inference**: 样本级过滤与 token 级重加权带来的稳定小幅增益说明「特权视觉证据」只有落在真正依赖视觉的样本与 token 上才有效，统一加权的做法反而稀释了信号。
- **Recommendation**: 做多模态自蒸馏时先用正负裁剪对筛出视觉依赖样本，再按教师分歧给关键 token 加权，并保持每个 micro-batch 的总权重不变以免引入尺度偏差。

**Key figures**

*Framework - Conceptual comparison of OPD, Vision-OPD, and VisAlloc. OPD provides uniform text-only teacher feedback. Vision-OPD adds a privileged evidence crop but retains uniform token weights. VisAllo*

![VisAlloc: Allocating Visual Supervision for On-Policy Self-Distillation - framework](res/2611.25069_framework.png)

**Why this ranks #13**: VisAlloc 用样本级视觉过滤加 token 级反事实重加权分配 MLLM 的视觉监督，在 8 个基准上 4B 与 9B 模型的宏平均分别达 81.44 与 84.92，比 Vision-OPD 复现高出 0.97 与 0.52 分；增益虽小，但证明统一 token 监督确实稀释了视觉信号。

---

## LLM / VLM 的 RL 与偏好优化 · `llm_vlm_rl` (7 papers)

7 篇里 3 篇 rel≥9,是本轮 llm_vlm 轴超额名额的来源,结论互相呼应:奖励侧污染比想象中更结构化。Blind Spots Travel 用 814 次 RL 运行测出:评委知道的**单题答案**留在评委那里,模型每 100 题只多对 1 题;但评委对**一类题**的判断会跟着模型走——一个拒掉 12 道正确答案里 11 道的评委,会让模型在新题上拒绝 **98%** 的同类题;人工只改这 12 条判决,拒绝率从 5% 跳到 90%。Search-RSI 从供给侧切入:题库增长常把「答案不存在」当「策略错」惩罚,不可达负样本越积越多;按能力边界递归扩题后,九个基准上 9B 与 27B 分别提升 9.8 与 9.5 点,其中 7.0 点是仅把检索世界做一致够不到的。Calibrated Decision Rewards 把奖励做成概率:GRPO 训 Qwen3-1.7B 在 MATH500 上从 72.2% 推到 76.8%,几乎追平答案键的 76.9%,随机奖励只有 +0.65。

### 14. Blind Spots Travel, Knowledge Stays Home: What RL Inherits from an LLM Judge

**arXiv**: [2611.25191](https://arxiv.org/abs/2611.25191) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, llm-judge, reward-signal, abstention, category-verdict, grpo, University of Colorado Boulder | **Categories**: cs.AI, cs.CL, cs.LG | **Pages**: 31

**Authors**: Liang Yue; Eric A. Vance

**Affiliation**: University of Colorado Boulder, Boulder, Colorado, USA

**Abstract**

> LLM judges serve as rewards where no answer key exists, in the hope that their knowledge passes to the trained model. In 814 RL runs that teach 7-8B models to answer closed-book questions or abstain, we ask what passes. What a grader knows about single answers stays home. A wrong answer that a judge rewards is memorised for that one question. A model trained with the answer key, or with a far stronger judge, chooses which new questions to answer no better than the untrained model does by sampling 32 answers and abstaining where they disagree; the grader's knowledge adds about one corrected answer per hundred questions. What a grader believes about a kind of question travels. A judge that rejects eleven of the twelve correct training answers about capitals of former states teaches the model to refuse 98% of such capitals on new questions, a loss that accuracy and abstention rates do not reveal. Changing only those twelve verdicts by hand moves the refusal from 5% to 90%, even for a grader that accepts as many answers as the answer key; at that leniency, two of four judges already cost 38-42% of these capitals. The capitals are not forgotten: with "I don't know" blocked, the model answers 94% of them correctly. The grader therefore needs no knowledge of its own: rewarding the model for giving the answer that most of its own untrained samples agree on, with no labels and no judge, earns the answer key's reward and keeps the category.

**Key findings**

- **Finding**: 814 次 GRPO 训练中，用答案键训练的模型比“采样 32 次再投票”的规则还低 0.8 分，评判者的知识每百题只多纠正约 1 个答案。
- **Inference**: 奖励只能在学生自己给出的候选之间做选择，评判者对单题的判断不会迁移到新题，只有针对某类问题的整体怀疑会被规则化并放大。
- **Recommendation**: 用 LLM 评判者当奖励前，先统计它在哪类问题上系统性拒答；若奖励只是让模型学会拒答，直接用模型自身 32 次采样投票的奖励即可，无需外部评判者。

**Key figures**

*Result - Does a grader’s knowledge reach new ques- tions? Each circle is one student–dataset pair: the true reward of students trained with the grader, minus the reward of the untrained student when*

![Blind Spots Travel, Knowledge Stays Home: What RL Inherits from an LLM Judge - result](res/2611.25191_result.png)

**Why this ranks #14**: 在 814 次 RL 运行里，7-8B 学生模型从 LLM 评判者继承的“单题知识”只值每百题约 1 个正确答案；但评判者对某一类问题的整体怀疑会被 12 个训练样本放大成规则，让 Llama 拒答 98% 的旧都城。

---

### 15. Search-RSI: Expanding Search Worlds Along Multimodal Agents' Capability Frontier

**arXiv**: [2611.27780](https://arxiv.org/abs/2611.27780) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, multimodal-search, self-improvement, retrieval-index, task-growth, reinforcement-learning, Hunan University | **Categories**: cs.AI, cs.CV | **Pages**: 25

**Authors**: Chengchao Lv; Yin Wang; Chunzheng Zhu; Wanli Chang

**Affiliation**: Hunan University; New York University

**Abstract**

> Multimodal search agents answer knowledge intensive visual questions by grounding them in retrieved evidence, and recent recipes train them on multi hop tasks that are synthesized from knowledge graphs and grown online to keep pace with the agent. These recipes, however, treat the searchable world as fixed: a new question can be well formed and verifiable while its evidence is absent from the retrieval backend, so the agent issues the right query, retrieves nothing, and is penalized as if its policy were at fault. Such unreachable negatives accumulate with every round of growth. We propose Search-RSI, a recursive self improvement framework that expands the search world along the agent's capability frontier. In each round, the current policy diagnoses its partially mastered regions of a task space spanned by hop depth, relation rarity, and distractor density; new tasks there are grown together with their evidence; and the same policy decides how they are used: candidates on which its probes disagree feed reinforcement learning, while those beyond its reach become hint guided demonstrations of its own. Keeping the policy inside this loop matters: an improver frozen at the start of training loses 3.2 points. On nine multimodal search benchmarks, Search-RSI keeps improving where static task growth saturates, raising the average accuracy of the recipe it builds on by 9.8 and 9.5 points at 9B and 27B, of which 7.0 points are out of reach for a world that is merely made consistent. The loop uses no external model and only privileged task structure that is removed before training, at 1.27x the compute of static growth.

**Key findings**

- **Finding**: 试点中 29.0% 的新长出任务缺少支撑元素，这类不可达负样本占全部负奖励的 41.0%，正确检索反而被当作策略过错惩罚。
- **Inference**: 检索后端固定时任务增长越快训练信号衰减越重，世界本身必须作为训练变量与策略能力同步扩张，而不是固定的背景板。
- **Recommendation**: 复现这类多跳搜索 RL 前先量化“不可达负样本”占比，并把新任务的证据同步注入索引，否则堆数据只会加速奖励污染。

**Key figures**

*Framework - Fixed pool and static world growth (top) vs. Search- RSI (bottom) on an MMSEARCH question. A fixed pool never asks the second hop; static growth asks it without its supporting fact, so a cor*

![Search-RSI: Expanding Search Worlds Along Multimodal Agents' Capability Frontier - framework](res/2611.27780_framework.png)

*Result - Overview of Search-RSI. We first diagnose the capability frontier from the rollout logs of the current policy πt, yielding a quota of new tasks for each partially mastered unit (Stage 1). We*

![Search-RSI: Expanding Search Worlds Along Multimodal Agents' Capability Frontier - result](res/2611.27780_result.png)

**Why this ranks #15**: 试点里 29.0% 新长出的任务缺少支撑证据，这类不可达负样本占全部负奖励的 41.0%；Search-RSI 把检索索引也当作训练变量，在 9 个多模态搜索基准上把所基于配方的平均准确率提高 9.8 与 9.5 分。

---

### 16. EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning

**arXiv**: [2611.26380](https://arxiv.org/abs/2611.26380) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, egocentric-video, video-captioning, temporal-alignment, reward-design, grpo, Hong Kong University of Science and | **Categories**: cs.CV | **Pages**: 17

**Authors**: Yuqi Tang; Yang Shi; Yuran Wang; Tengfei Liu; Rundong Wang; Zongyang Qiu; Qixun Wang; Zhuoran Zhang; Xuanyu Zhu; Yifan Xu; Yiyan Ji; Shujie Li

**Affiliation**: The Hong Kong University of Science and Technology (Guangzhou); KlingAI Research; Peking University; University of Science and Technology of China; Nanjing University

**Abstract**

> Egocentric video captioning requires fine-grained detail and accurate timing, yet current multimodal large language models (MLLMs) often miss brief actions, confuse their order, or misinterpret the wearer's motion. Existing caption formats also offer limited support for combining detailed narration with precise timing. We present EgoCaptioner, which pairs a video-level overview of the setting, participants, and the wearer's overall activity with timed steps whose narration adapts to varying perceptual demands and marks key moments at specific timestamps. We develop a coarse-to-fine annotation pipeline that establishes event structure before expanding step descriptions, yielding 50,000 training examples from eight egocentric video sources. Complementary rewards assess factual accuracy and coverage, measure step-level temporal alignment, and penalize fragmented or redundant narration, guiding caption refinement through Group Relative Policy Optimization (GRPO). To improve the reliability of factual supervision, we supplement caption references with pose-derived motion facts when sensor data are available. Across five egocentric benchmarks, EgoCaptioner achieves leading performance among evaluated open-source models in caption quality, caption-conditioned question answering, and temporal alignment. It also surpasses Gemini 3.1 Pro on PhysCapBench and all evaluated proprietary baselines on Minerva-Ego under the caption-to-QA protocol. Ablations support the complementary roles of factual and temporal rewards and show that coarse-to-fine annotation provides more effective supervision than single-pass annotation.

**Key findings**

- **Finding**: 以 Qwen3.5-9B 为底座，EgoCaptioner 在 PhysCapBench Overall 上比底座高 27.6 分并超过 Gemini 3.1 Pro，在 EgoTempo 准确率上高 16.8 个百分点。
- **Inference**: 事实正确性、时间对齐与文风三类奖励互补，分别对应“看得对、说得准、写得顺”，任何单一奖励都覆盖不了全部失效模式。
- **Recommendation**: 做带时间戳的视频描述时，按 0.6 事实 + 0.2 时序 + 0.2 风格起步，并把有姿态传感器数据的样本当作独立事实来源以校准监督。

**Key figures**

*Framework - Overview of EgoCaptioner. Given an egocentric video, EgoCaptioner produces a caption with a video-level overview and timestamped steps. The overview establishes the scene context and the we*

![EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning - framework](res/2611.26380_framework.png)

*Result - Data construction pipeline. (a) Gemini-3.1-Pro and Seed2.1 pro annotate each video coarse to fine, from a global overview and event outlines to timestamped steps. (b) The draft caption is r*

![EgoCaptioner: Towards Comprehensive and Fine-Grained Egocentric Video Captioning - result](res/2611.26380_result.png)

**Why this ranks #16**: 先用 8 个第一视角视频源的 5 万条粗到细标注做 SFT，再用 GRPO 以 0.6 事实分 + 0.2 时序分 + 0.2 风格分精修，相对 Qwen3.5-9B 底座在 PhysCapBench Overall 上提升 27.6 分并超过 Gemini 3.1 Pro。

---

### 17. Calibrated Decision Rewards: Training Language Models with a Judge That Knows How Sure It Is

**arXiv**: [2611.25135](https://arxiv.org/abs/2611.25135) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, calibrated-reward, reference-free, process-supervision, reward-hacking, grpo, FuturiX AI Research | **Categories**: cs.AI, cs.CL | **Pages**: 24

**Authors**: Rudransh Agnihotri; Manasvi Kapoor

**Affiliation**: FuturiX AI Research

**Abstract**

> Reinforcement learning (RL) can only teach a language model what its reward can recognize. Answer checkers are exact but need a reference answer; learned reward models and LLM judges work everywhere, but their scores are not probabilities. We study RLCDR (Reinforcement Learning from Calibrated Decision Rewards). An LLM converted into a decision model answers a typed question about a response ("is the final answer correct?", "which step is the first error?") with a probability distribution, read in one forward pass, debiased over option orders and calibrated with about a hundred labels. Training Qwen3-1.7B with GRPO on MATH, this reference-free reward raises MATH500 accuracy from 72.2% to 76.8% (+4.65 points, p < 1e-4), matching training on the answer key (76.9%), while a random reward gains only +0.65. The gain grows with difficulty, from 44.8% to 51.7% on the hardest level. On the policy's own changing samples the reward stays calibrated: its expected calibration error is half that of a softmax judge on the same 27B backbone (0.074 vs. 0.141), and it shows no sign of reward hacking. Without step training, the same model finds the first wrong step better than a dedicated 7B process reward model (ProcessBench F1 0.772 vs. 0.722, 20/20 splits). We also map where the approach stops being enough: trained only on problems the base model mostly fails, the reference-free reward still improves the policy (+1.9 MATH500 points, p = 0.03) but trails the answer key, because its probabilities become overconfident on that distribution. We state six hypotheses in advance and test each with a control designed to falsify it.

**Key findings**

- **Finding**: 只改奖励这一个变量时，RLCDR 让 MATH500 从 72.2% 升到 76.8%（+4.65，p<1e-4），随机奖励只涨 0.65，答案键训练为 76.9%。
- **Inference**: 奖励需要的是概率而不是分数；在策略自身不断变化的样本上保持校准（ECE 0.074 对 0.141）比离线榜单分数更能决定 RL 收益。
- **Recommendation**: 缺参考答案时把 LLM 判定做成带选项顺序去偏和概率校准的决策模型，并同时准备随机奖励下界与答案键上界两组对照来归因。

**Key figures**

*Framework - The policy improves because of the reward. Qwen3-1.7B trained with GRPO on MATH (training split), changing only the reward. Every evaluation uses reference answers, never the reward model. L*

![Calibrated Decision Rewards: Training Language Models with a Judge That Knows How Sure It Is - framework](res/2611.25135_framework.png)

*Result - RLCDR in one picture. Each policy answer is wrapped in a typed question. The decision model returns a distribution over the options in one forward pass. Averaging over option orders removes*

![Calibrated Decision Rewards: Training Language Models with a Judge That Knows How Sure It Is - result](res/2611.25135_result.png)

**Why this ranks #17**: 把 LLM 改造成输出概率分布的决策模型、只用约 100 条标签做顺序去偏与校准后，Qwen3-1.7B 用 GRPO 在 MATH500 上从 72.2% 升到 76.8%，与直接用答案键训练的 76.9% 持平。

---

### 18. When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards

**arXiv**: [2611.25793](https://arxiv.org/abs/2611.25793) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, multimodal-safety, rationale-hallucination, tool-use, grounding-verification, grpo, Harbin Institute of Technology | **Categories**: cs.AI | **Pages**: 30

**Authors**: Yingshuo Wang; Weixiang Zhao; Guancheng Li; Jiahe Guo; Yu Zhang; Yanyan Zhao

**Affiliation**: Harbin Institute of Technology

**Abstract**

> Multimodal safety guards increasingly generate rationales alongside safety predictions, yet whether these rationales are reliable remains largely unexplored. We systematically study *rationale hallucination* from two perspectives: visual rationale hallucination, where rationales contain unsupported visual facts, and safety attribution hallucination, where grounded content is assigned an incorrect safety interpretation. Across rationale-generation methods, multiple vision-language backbones, and safety datasets, we find that rationale hallucination is widespread and does not consistently diminish with higher classification accuracy or increased model scale. Further analysis of the Think-with-Image paradigm shows that hallucination is concentrated in fine-grained attributes and relations, while visual tools are often invoked infrequently or without sufficient spatial focus. Based on these findings, we propose *Tool-Contrastive Grounding Reinforcement Learning* (TCG-RL), which rewards tool use only when it improves rationale grounding over a tool-free reference. TCG-RL substantially reduces rationale hallucination while maintaining competitive safety prediction performance. By revealing the gap between prediction correctness and rationale reliability, our study motivates a shift in multimodal safety guarding from outcome-only evaluation toward safety decisions that are both accurate and verifiably grounded.

**Key findings**

- **Finding**: Qwen2.5-VL-7B 上 Direct CoT 的 Harm-C 视觉证据分只有 73.3，TCG-RL 提到 94.5，去掉工具对比奖励则回落到 81.9。
- **Inference**: 多模态安全护栏的准确率与理由可靠性是两个独立维度，只用结果型奖励会诱导模型编造看似合理的视觉依据。
- **Recommendation**: 评估多模态安全护栏时同时报视觉证据分与安全归因分；训练时把工具轨迹与无工具参考配对，只奖励 grounding 确有提升的调用。

**Key figures**

*Framework - Examples of rationale hallucination in multimodal safety guards. The left panel shows vi- sual evidence hallucination caused by unsupported entities, attributes, and relations. The three rig*

![When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards - framework](res/2611.25793_framework.png)

*Result - Mean safety-attribution scores across the four image-text safety benchmarks for Qwen2.5- VL-7B (left) and Qwen2.5-VL-32B (right). Each point represents a rationale-generation method, and the*

![When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards - result](res/2611.25793_result.png)

**Why this ranks #18**: 在 8 种理由生成方法、5 个视觉语言底座、4 个安全数据集上系统诊断理由幻觉，并提出 TCG-RL：只有当工具调用比无工具参考更 grounded 时才给奖励，使 Qwen2.5-VL-7B 在 Harm-C 的视觉证据分从 73.3 提到 94.5。

---

### 19. RegionAgent: Two-Stage Preference Optimization for Regional Image Restoration

**arXiv**: [2611.26179](https://arxiv.org/abs/2611.26179) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, image-restoration, preference-optimization, vision-language-model, region-selection, dpo, Northwestern Polytechnical University | **Categories**: cs.AI, cs.CV | **Pages**: 14

**Authors**: Weiyu Zhou; Jiacong Tang; Tao Hu; Axi Niu; Jinqiu Sun; Peng Wu; Wei Dong; Qingsen Yan

**Affiliation**: Northwestern Polytechnical University; Xi’an University of Architecture and Technology

**Abstract**

> Images under non-uniform coupled degradations require diverse restoration capabilities for different degraded regions. Existing methods employ globally uniform operations, potentially overlooking regional differences and causing incomplete restoration or even damage to image content. Moreover, a degraded region may require successive restoration actions, and earlier actions may alter residual degradation characteristics or introduce artifacts, potentially hindering subsequent restoration. To address these challenges, we propose RegionAgent, an adaptive restoration framework that trains a Vision-Language Model (VLM) through two-stage preference learning to generate a region-specific restoration action at each iteration. Specifically, we first train the VLM to select an action suited to the current region through step-level Direct Preference Optimization (DPO), using preferences derived from immediate restoration feedback to supervise only the differing component in each action pair. To account for the effects of current actions on subsequent restoration, we then apply trajectory-level DPO, using preferences derived from complete trajectory scores to supervise the sole differing action in each trajectory pair. Furthermore, as conventional image-pair datasets do not directly provide preferences over regional restoration decisions, we construct a regional restoration preference dataset comprising 10K action pairs and 20K trajectory pairs for two-stage VLM training. Experiments across multiple datasets demonstrate strong restoration performance under both mixed and single degradations. Ablation studies further validate the effectiveness of two-stage preference learning in improving restoration quality.

**Key findings**

- **Finding**: RegionAgent 把三组混合退化的 PSNR 从 19.68/20.87/21.34 提到 20.90/21.61/22.11 dB，单退化套件平均 28.71 dB，比最强基线 AutoDIR 高 0.90 dB。
- **Inference**: 偏好监督只作用在配对中唯一不同的那个分量上，才能把“选哪个区域、用哪些专家、融合多强”分别对齐到即时反馈与轨迹收益。
- **Recommendation**: 做区域级修复的偏好学习时，先构造只差一个配置分量的动作对与只差一个动作的轨迹对，再按先步级后轨迹级两阶段训练。

**Key figures**

*Framework - Conceptual comparison of restoration paradigms. (a) Task-specific and all-in-one models restore the whole image. (b) Image-level agents select tools using iterative feedback. (c) RegionA- ge*

![RegionAgent: Two-Stage Preference Optimization for Regional Image Restoration - framework](res/2611.26179_framework.png)

*Result - Overview of RegionAgent. (a) The Localizer proposes candidate regions, and the VLM selects restoration actions from the current image state. (b) The composed restorer processes the selected*

![RegionAgent: Two-Stage Preference Optimization for Regional Image Restoration - result](res/2611.26179_result.png)

**Why this ranks #19**: 用 1 万组动作对与 2 万组轨迹对做两阶段 DPO，训练 Qwen3-VL-4B 每轮挑选退化区域并配置修复，三组混合退化 PSNR 比共享修复器基线高 0.77、0.74、1.22 dB，单退化套件平均 28.71 dB。

---

### 20. Sequential Anytime Valid Tests for Efficient Inference-Time Alignment

**arXiv**: [2611.26413](https://arxiv.org/abs/2611.26413) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, inference-time-alignment, sequential-testing, reward-model, anytime-valid, best-of-n, Indian Institute of Technology Kanpur | **Categories**: cs.LG | **Pages**: 18

**Authors**: Vishesh Kumar Singh; Sayak Ray Chowdhury

**Affiliation**: Indian Institute of Technology Kanpur, India

**Abstract**

> Inference-time alignment methods, such as Best-of-N (BoN), improve language model outputs by generating multiple candidates per prompt and selecting among them using a reward model. Much of this cost is wasted: a fixed budget is applied to every prompt, although the computation required by prompts varies widely. Adaptive methods halt once sampled answers appear settled, but their thresholds are tuned heuristics with no statistical control over early-stopping errors. We instead seek an anytime-valid stopping rule that takes an error tolerance $α$ as input and halts only once an answer is certified to hold a majority ($θ_a > 1/2$) under the generator's distribution. We aggregate candidates by final answer with a reward-weighted self-consistency (RWSC) score and treat stopping as a sequential test over the resulting clusters. Applying Wald's sequential probability ratio test to these clusters yields SPRT-RWSC, which performs well empirically, but its guarantee fails because the leading answer shifts during sampling, and the run is continuously monitored. Our main contribution, e-RWSC, replaces Wald's test with a betting supermartingale (an e-process) for every answer the policy produces, bounding the probability of ever certifying a non-dominant answer by $α$, uniformly over time and across all answers. The RWSC scores drive the bets, so they affect only how quickly a dominant answer $a^\star$ is certified, not validity; certification takes $O(\log(1/α)/d_{\mathrm{KL}}(θ_{a^\star}\|1/2))$ samples. Experiments across several language models, datasets, and reward models confirm the predicted $1/d_{\mathrm{KL}}$ scaling of cost and show that accuracy improves over baselines at substantially lower token cost.

**Key findings**

- **Finding**: MATH500 上预算从 32 增到 512 时 BoN 准确率从 71.4% 掉到 69.8%，暴露奖励被 hack；RWSC 单调升到 77.8%，E-RWSC 早期认证答案准确率 94.5%。
- **Inference**: 固定预算选择会让异常高分响应独自胜出，而 anytime-valid 的下注超鞅让奖励只影响认证速度、不参与有效性判定。
- **Recommendation**: 做推理时对齐时按提示难度自定预算，把认证阈值 α 固定为可接受的第一类错误率，再用 1/dKL 缩放估算所需样本数。

**Key figures**

*Result - Stopping reliability and token footprint analysis on MATH500 (Nmax = 512) for Qwen2.5-3B with ArmoRM. (a) E-RWSC achieves 94.5% accuracy on certified early stops (τ < 512). (b) Decision reli*

![Sequential Anytime Valid Tests for Efficient Inference-Time Alignment - result](res/2611.26413_result.png)

**Why this ranks #20**: 把 Best-of-N 的推理时对齐改写成对奖励加权自一致簇的序贯检验，用 e-process 把误认证非优势答案的概率控制在 α 以内；MATH500 上比 BoN 提升 8.2 个百分点且预算减少 61.7%。

---

## Footer

- Total papers reviewed across all 4 axes: 60
- llm_vlm axis final count: 20
- Wild-cards in this axis: 0
- Figure assets: 2026-11-24/res/

Generated by `mine-arxiv-daily-digest` skill. Sister file: `2026-11-24_llm_vlm_entry.md`.
