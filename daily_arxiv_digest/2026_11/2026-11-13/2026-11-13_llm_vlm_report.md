# Mine Arxiv Daily Digest - 2026-11-13 (LLM / VLM 与其强化学习 Axis, 20 papers)

**Generated**: 2026-11-13 10:46 CST

**Source**: arXiv cs.CV, cs.SD, eess.AS, cs.CL, cs.AI, cs.RO, cs.LG, cs.IR submissions, listing day 2026-11-11 (announced 2026-11-13 01:00 UTC)

**Batch window**: 2026-11-10T19:00:00Z .. 2026-11-11T19:00:00Z（arXiv 公告批次横跨两个 UTC 日：从前一日的美东 14:00 截止时刻起算（EDT 为 18:00Z，EST 为 19:00Z），到当日的同一时刻为止）

**Axis**: llm_vlm (20 papers, base 18, cap 20)

**Directions**: llm_core (10), vlm_core (5), llm_vlm_rl (5)

**Selection**: 20 papers ranked by relevance x quality, with 0 wild-card slots

**Day total**: 60 papers across 4 axes (target 60)

**Scope**: 大语言模型与视觉语言模型的设计、推理、agent、效率与上下文工作，以及面向 LLM / VLM 的 RL 与偏好优化、奖励模型

**Wild-card**: 0 —— 本 axis 20 篇全部是够格论文，未启用任何 wild-card 名额。

**本 axis 从 18 篇补到 20 篇，打满 `AXIS_CAP = 20`。** 完整批次里 `llm_vlm` 侧候选最充裕（仅新候选就有 113 篇过筛），当天让出的名额全部流到这里。

**同轴让位：6 篇 `llm_core` 与 3 篇 `vlm_core` 的 rel ≥ 9 必进论文挤占了同方向分数更低的已发布论文的位置。** 本批共有 10 篇 relevance ≥ 9 的新论文落在这个 axis（`llm_core` 6、`vlm_core` 3、`llm_vlm_rl` 1），而原先的分配是 `llm_core` 11 / `vlm_core` 4 / `llm_vlm_rl` 3。按 skill「rel ≥ 9 必进、同 axis 内让位」的口径，`llm_core` 让出 7 个位置、`vlm_core` 让出 2 个位置，轴内 20 个名额全部由够格论文占满。

**唯一一篇 rel ≥ 9 仍然落选的是 2611.14924（Edge-Native Multimodal RAG）。** `llm_core` 在 `AXIS_CAP = 20` 下最多只能容纳 10 篇（基准 8 + `axis_surplus` 2，因为 `vlm_core` 与 `llm_vlm_rl` 都没有低于基准），而该方向有 11 篇 rel ≥ 9 争这 10 个位置；2611.14924 与同分的 2611.14850（final 8.70）并列，按 id 排序落在后面。它是**当天唯一一篇被挤掉的 rel ≥ 9**，其余落选的已发布论文 relevance 均为 8 或 7。

---

## LLM 核心（架构 / 推理 / agent / 效率 / 上下文） · `llm_core` (10 papers)

本方向 10 篇里 6 篇为补跑新增，主线是**把 LLM 的内部结构变成可利用的工程接口**。NORDER-II 把稠密 MLP 计算改写成可由期望精确恢复的组合状态空间，状态预算 B=2048 时在 Llama-3.2-1B 与 Gemma-2-2B 上取得 92.4% 与 93.8% 的 MLP 输出逼近精度，同预算的 Channel Top-k 只有 76.9% 与 79.8%；MoE Expert Eviction 直接证伪了「训练路由器减少切换」这条路线——不改任何路由决策、只按 farthest-future 淘汰，稳态拷贝数就从 LRU 的 9.6 降到 4.6、吞吐 38.3 提到 42.5 tok/s 而 NLL 增量为 0；MIGRO 把长期记忆做成与模型解耦、可跨代共享的持久状态（LoCoMo 54.13 对 Mem0 的 52.12，私有存储少用 99.3%）；SAME 只在 Alpaca 上注入一次水印即在九个下游集拿到 100.00% 固定触发检出率（BadEdit 在 MMLU 上只剩 10.87%）；Differential Backpack 把义项权重从非负放松为有符号，困惑度 24.60 降到 23.52 而归因残差只从 6×10⁻⁷ 涨到 0.66；Mach2 则是规范性贡献——把自然语言规则写成 lint 式可执行谓词并在四个检查点上门控，但全文没有实验数据表，贡献是可追溯性而非精度提升。已发布的四篇里 ToolTurns 暴露出多轮工具基准的真实缺口：最好的 agent 单轮解决率 69.6%，整段对话完成率却只有 39.8%；Mask-Pattern Position Augmentation 把 dLLM 的长上下文外推做到 8192 token 处困惑度从 19.51 降到 3.12；Prefix-Guided Sampling 用 22% 的前缀 token 拿到全路径 53% 的增益；Effective Teacher Support 则显示 0.01% 到 0.1% 的教师支持率就能把 MMLU-Pro 上的next-token 优势拉到 38% 对 24%。

### 1. ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue

**arXiv**: [2611.14925](https://arxiv.org/abs/2611.14925) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, multi-turn-dialogue, tool-use, agent-benchmark, user-simulator, University of California | **Categories**: cs.CL | **Pages**: 36

**Authors**: Milad Gholami; Brendan King; Jeffrey Flanigan

**Affiliation**: University of California, Santa Cruz

**Abstract**

> Tool-using language models are increasingly deployed in conversational settings, yet most large-scale tool-use benchmarks focus on isolated requests. We introduce ToolTurns, a benchmark of 2,620 problems spanning 1,827 tools and 11,004 API endpoints across 47 categories. Each dialogue begins with an intentionally underspecified request and continues through two context-dependent follow-ups, testing clarification, tool use, and retention of conversational context. We also introduce an open-source user simulator that reveals withheld context through dialogue and generates follow-up requests, with a checker--fixer pipeline for improving its turns. Across nine language models, the best agent resolves 69.6% of individual requests but completes only 39.8% of full dialogues. Under this evaluation protocol, every evaluated model receives lower success scores on follow-up requests than on the initial request, and dialogue-quality rubric scores and task success can rank models very differently. Paired turn-level evaluation shows that the checker--fixer reduces detected dialogue defects, and blind human evaluation favors the revised turns. ToolTurns provides a testbed for evaluating whether agents sustain task success across multi-turn dialogue with tools.

**Key findings**

- **Finding**: 基准含 2620 个初始欠明确的问题、1827 个工具、11004 个 API 端点与 47 个类别；最好的 agent 单轮解决率 69.6%，但完整对话完成率仅 39.8%。
- **Inference**: 现有多轮工具基准的缺口不在工具选得对不对，而在澄清与上下文延续，模型在两个追问轮上的成功率系统性低于首轮。
- **Recommendation**: 评测自建工具 agent 时不要只报单轮成功率，改用带上下文相关追问的完整对话口径，并单独统计追问轮的失败率。

**Why this ranks #1**: 把工具调用从单轮请求拉到多轮对话：2620 个问题覆盖 1827 个工具与 11004 个 API 端点、47 个类别，九个模型中最好者单轮解决率 69.6%，整段对话完成率却只有 39.8%，这个落差是它排在本方向首位的原因。

---

### 2. Early Signals, Strong Decisions: Prefix-Guided Sampling for Parallel Test-Time Scaling

**arXiv**: [2611.14965](https://arxiv.org/abs/2611.14965) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, test-time-scaling, confidence-scoring, token-efficiency, parallel-sampling, MIT CSAIL | **Categories**: cs.AI | **Pages**: 26

**Authors**: Jie Ren; Jonathan Rosenfeld; Neil Thompson

**Affiliation**: MIT CSAIL, MIT FutureTech

**Abstract**

> Parallel test-time scaling (TTS) has been shown to enhance reasoning in large language models by generating and aggregating multiple independent reasoning paths. Internal confidence scores can further improve this process by identifying paths of varying quality. However, existing methods remain computationally inefficient, as low-quality paths are fully expanded before being evaluated. In this work, we aim to improve the use of internal confidence signals for better model performance and computational efficiency. We begin by offering a new perspective on the role of confidence in aggregation, showing that it is most impactful for questions near the decision boundary. Notably, when amplified by multi-sample aggregation, even small confidence signals derived from short prefixes can meaningfully influence outcomes in these boundary cases. Building on this insight, we introduce Prefix-Guided Sampling (PreG), a method that reallocates computation by first generating short prefixes, ranking them using internal confidence scores, and then completing only the most promising candidates. This strategy reduces token usage while maintaining gains in path quality. We provide theoretical analysis demonstrating that, under a fixed compute budget, PreG strengthens the effective signal by widening the decision boundary margin. Empirically, our method consistently outperforms standard parallel TTS approaches across benchmarks, while significantly improving token efficiency and reducing overall computation.

**Key findings**

- **Finding**: 用前 4096 token（约占 Qwen 输出的 22%）做前缀打分，可恢复全路径打分 53% 的精度增益；60 组配置中 54 组比对应 vanilla 方法更省 token，其中 27 组不到一半，BRUMO 上最高省约 80%。
- **Inference**: 内部置信度只在决策边界附近才最有用，短前缀已足以承担路径筛选，因此算力应该从前置筛选而不是后置聚合里省。
- **Recommendation**: 搭并行 TTS 时先跑一批短前缀按内部置信度排序，只展开得分靠前的候选；在 300k token 预算以上收益最稳定。

**Key figures**

*Framework - DC-PreG vs. vanilla DC*

![Early Signals, Strong Decisions: Prefix-Guided Sampling for Parallel Test-Time Scaling - framework](res/2611.14965_framework.png)

**Why this ranks #2**: 先出短前缀打分再决定展开哪条推理路径：前缀约占完整路径 22% 的 token，却能恢复全路径打分 53% 的精度增益；60 组配置里 54 组比原并行 TTS 省 token，BRUMO 上最高省约 80%，因此进入本方向前三。

---

### 3. Mask-Pattern Position Augmentation: Training-Free Long-Context Extrapolation for Diffusion LLMs

**arXiv**: [2611.15029](https://arxiv.org/abs/2611.15029) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, diffusion-llm, long-context, position-encoding, training-free, International Institute of Information | **Categories**: cs.LG | **Pages**: 7

**Authors**: Gaurav Sarkar; Syed Affan Daimi

**Affiliation**: International Institute of Information Technology, Hyderabad

**Abstract**

> Diffusion large language models (dLLMs) generate by iteratively unmasking tokens with bidirectional attention, but rotary position embeddings (RoPE) still confine them to a fixed pretraining window. Existing training-free extrapolation, notably LongLLaDA, copies NTK-based RoPE scaling from autoregressive (AR) models and applies one static, length-only transform at every position and denoising step. That transplant ignores a signal unique to dLLMs: the evolving mask pattern of the partially decoded sequence. We propose Mask-Pattern Position Augmentation (MPPA). MPPA linearly interpolates indices into the pretrained window, then adds a per-position, per-step offset from cumulative mask density. The offset restores rotary phase resolution that interpolation collapses, and it shrinks as tokens are committed, so late steps see near-clean interpolated geometry. On LLaDA-8B-Instruct at twice its 4096-token window, MPPA reduces perplexity from 19.51 under standard decoding to 3.12 at 8192 tokens, below the in-window figure, with 100% passkey retrieval and unchanged needle-in-a-haystack accuracy. These preliminary $2\times$ results motivate mask-conditioned position engineering as a diffusion-native path to long-context generation.

**Key findings**

- **Finding**: 在 LLaDA-8B-Instruct 上把上下文拉到 8192 token（预训练窗口 4096 的两倍），MPPA 把困惑度从标准解码的 19.51 降到 3.12，passkey 检索 100%、needle-in-a-haystack 准确率不变。
- **Inference**: 把每个位置每步的累计 mask 密度加进 RoPE 插值，比照搬自回归模型的静态长度缩放更贴合扩散式解码的解码动力学。
- **Recommendation**: 做 dLLM 长上下文外推优先试按 mask 密度条件化的位置偏移而不是直接套 NTK 缩放；注意 2 倍长度下 25%–50% 中段插入深度仍是检索盲区。

**Key figures**

*Framework - Perplexity vs. context length (plotted from the benchmark log). Standard decoding collapses under 2× direct extrapolation (2.58 →19.51); MPPA instead decreases to 3.12, below its own in-wind*

![Mask-Pattern Position Augmentation: Training-Free Long-Context Extrapolation for Diffusion LLMs - framework](res/2611.15029_framework.png)

*Result - MPPA needle-in-a-haystack accuracy by insertion depth and context length. Retrieval is perfect within the trained window and at the shallow/deep ends at 2×; only the 25 to 50% mid-depths fai*

![Mask-Pattern Position Augmentation: Training-Free Long-Context Extrapolation for Diffusion LLMs - result](res/2611.15029_result.png)

**Why this ranks #3**: 把 dLLM 独有的 mask 模式用作位置信号：在 LLaDA-8B-Instruct 上把上下文拉到 8192 token，困惑度从标准解码的 19.51 降到 3.12，低于 4096 窗口内的水平，passkey 检索仍是 100%，是本批最干净的长上下文外推。

---

### 4. Effective Teacher Support for Reasoning Distillation

**arXiv**: [2611.14850](https://arxiv.org/abs/2611.14850) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, knowledge-distillation, teacher-support, vocabulary-sparsification, training-efficiency, NVIDIA | **Categories**: cs.AI, cs.CL, cs.LG | **Pages**: 14

**Authors**: Lavinia Ghita; Dhruv Desai

**Affiliation**: NVIDIA

**Abstract**

> Forward-KL language-model distillation normally computes dense teacher and student scores over the full vocabulary at every supervised position, making training and stored teacher targets expensive. We instead distill from the teacher's highest-probability vocabulary fraction, renormalizing the retained mass as we sweep support from 100% to 0.01%. Our main study distills Qwen3 4B -> 1.7B. We confirm the broader support-reduction finding on larger Qwen3 8B -> 4B and Nemotron Nano 12B -> 9B pairs and under answer-only supervision. We evaluate generation primarily on MMLU-Pro and secondarily on GPQA-Diamond. Across the Qwen3 settings, retaining 0.01% of the vocabulary causes no observed MMLU-Pro degradation relative to full-vocabulary distillation, although disagreement with the complete teacher distribution increases. Nemotron Nano matches full-vocabulary MMLU-Pro at 0.1%, but smaller fractions fail to emit the closing reasoning tag, showing that the reliable cutoff depends on the model family. At 0.01% support, caching the retained next-token scores from the teacher forward pass cuts training step time by 38%, while restricting student output computation to those tokens cuts peak memory by 24%; neither causes observed MMLU-Pro degradation.

**Key findings**

- **Finding**: Qwen3 4B 到 1.7B 蒸馏时保留 0.01% 词表，MMLU-Pro 相对全词表蒸馏无观测下降；0.01% 支持下缓存教师 next-token 分数使训练步时降 38%，限制学生输出计算使峰值显存降 24%。
- **Inference**: 教师的有效信息高度集中在极小的概率质量里，说明 forward-KL 蒸馏长期在为一小段质量支付全词表的算力与显存。
- **Recommendation**: 做推理蒸馏先在 0.01%–0.1% 支持上扫一遍再定预算；注意 Nemotron Nano 要到 0.1% 才匹配全词表，更小比例会输出不出收尾推理标签。

**Key figures**

*Framework - Effective teacher support on reasoning traces. Empirical CDFs of 𝑘𝜌over the 905,193,844 supervised positions remaining after excluding the first supervised position in each example, for whic*

![Effective Teacher Support for Reasoning Distillation - framework](res/2611.14850_framework.png)

*Result - Generation across retained support size. Three-seed MMLU-Pro (left) and GPQA-Diamond (right). Lines and large markers show means; light points show individual seeds. Horizontal lines mark th*

![Effective Teacher Support for Reasoning Distillation - result](res/2611.14850_result.png)

**Why this ranks #4**: 只蒸馏教师最高概率的词表片段就能不损精度：Qwen3 4B 到 1.7B 保留 0.01% 词表时 MMLU-Pro 相对全词表蒸馏无观测下降，训练步时降 38%、峰值显存降 24%，是推理蒸馏里少见的只减成本不掉点。

---

### 5. Probabilistic State Space Enumeration in Neural Network Computation

**arXiv**: [2611.15062](https://arxiv.org/abs/2611.15062) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, norder-ii, mlp-sparsification, transformer-inference, probabilistic-state-space, channel-grouping, ElohaX | **Categories**: cs.LG | **Pages**: 18

**Authors**: Victor O. K. Li; Yang Han; Jacqueline C. K. Lam

**Affiliation**: ElohaX Ltd.; The Hong Kong University of Science and Technology (Guangzhou); The Chinese University of Hong Kong; CASBS, Stanford University

**Abstract**

> Deep neural networks typically realize dense computation by propagating information through all intermediate channels, while many approximation methods rank and retain individual computational components. We ask whether dense neural computation can instead be represented exactly as an expectation over a combinatorial state space, and approximated by evaluating only its most probable configurations. We introduce a novel probabilistic state-space framework for Transformer MLPs. The framework partitions the intermediate dimension into channel groups, defines an input-dependent distribution over binary inclusion states, and uses importance-corrected masked outputs such that the full expectation exactly recovers the dense MLP output. The key algorithmic novelty is NORDER-II, which enumerates complete joint states in decreasing probability without constructing or sorting the exponentially large state space. Truncating this ordering yields an anytime approximation governed by cumulative probability mass and a state budget. On Llama-3.2-1B and Gemma-2-2B, NORDER-II at a state budget of B=2048 achieves 92.4% and 93.8% MLP-output approximation accuracy, compared with 76.9% and 79.8% for Channel Top-k. When the first, middle, and last MLP layers are approximated jointly, WikiText-2 perplexity remains within 0.06% and 0.54% of dense inference. Relative to expected-count Grouped Top-k, NORDER-II yields 82.6% to 126.4% relative accuracy gains with only 0.18% to 0.19% additional local analytic FLOPs. These results establish the significance of joint-state structure beyond atomic salience and point to a new paradigm for neural computation: dense layers can be viewed as structured probabilistic inference over combinatorial computational states. This framework opens a path toward adaptive, probability-mass-controlled computation in pretrained neural networks.

**Key findings**

- **Finding**: NORDER-II 以 O(G log G + B log B) 代价生成前缀，在 Llama-3.2-1B 与 Gemma-2-2B 上以 B=2048 达到 92.4% 与 93.8% 的 MLP 输出逼近精度，而 Channel Top-k 在其 2048 通道设置下只有 76.9% 与 79.8%。
- **Inference**: 联合状态排序比逐原子通道打分更适合 MLP，因为首、中、末三层 MLP 同时近似后 WikiText-2 困惑度只比稠密模型高 0.06% 与 0.54%，说明被丢弃的是低概率质量的尾部而不是有效计算。
- **Recommendation**: 若要为 Transformer MLP 做稀疏化，先按通道组构造输入相关的伯努利状态分布并跑 NORDER-II 排序，把预算设到累计概率质量阈值附近，而不是直接照搬 top-k 通道数量。

**Why this ranks #5**: 把稠密 MLP 计算改写成可由期望精确恢复的组合状态空间，NORDER-II 在状态预算 B=2048 时于 Llama-3.2-1B / Gemma-2-2B 上取得 92.4% / 93.8% 的 MLP 输出逼近精度，远高于 Channel Top-k 同预算下的 76.9% / 79.8%；首/中/末三层 MLP 联合近似后 WikiText-2 困惑度仅比稠密推理高 0.06% 与 0.54%，是可直接落地的推理加速路径。

---

### 6. Differential Backpack Language Models: Sense Inhibition via Signed Contextualization Weights

**arXiv**: [2611.15642](https://arxiv.org/abs/2611.15642) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, backpack, differential-attention, interpretability, sense-vectors, signed-weights, University of Ioannina | **Categories**: cs.CL | **Pages**: 16

**Authors**: Konstantinos Skianis; Giannis Nikolentzos; Polykarpos Meladianos; Michalis Vazirgiannis

**Affiliation**: University of Ioannina; University of Peloponnese

**Abstract**

> Backpack language models predict with a strictly linear combination of non-contextual per-word sense vectors, weighted by non-negative contextualization scores. We show that non-negativity conflates two properties: the linear readout, which carries the interpretability, and the conic combination, which merely restricts it. We relax the latter by computing the sense weights with differential attention, a difference of two softmax maps with a learned per-sense gain, so context can actively inhibit a sense; we call the result a differential Backpack. At equal parameters on WikiText-103 this cuts the Backpack's perplexity gap to a Transformer by 31%, improves over the softmax Backpack at every sense count, persists with a shrinking margin up to 350M parameters on OpenWebText, and is localized at the sense layer by ablations and controls. The learned inhibition is directly interpretable (a financial context drives the river sense of bank to -0.50), and the preserved per-sense attribution predicts counterfactual removals exactly. We tested a number of combination rules, showing the linear interface is nearly free. Making the readout nonlinear gains only 0.43 perplexity points while invalidating two thirds of the decomposition. The differential Backpack's senses are also better representations, improving zero-shot sentence similarity by up to 33%.

**Key findings**

- **Finding**: 约 70M 参数、20k 步训练的单种子设置下，differential Backpack 的 WikiText-103 精确验证困惑度为 23.52，softmax Backpack 为 24.60，同预算 14 层 Transformer 为 21.09，解释性税从 +3.51 降到 +2.43。
- **Inference**: 把读出改成非线性只换来 0.43 个困惑点收益（23.52→23.09），却让逐义项归因残差从 6×10⁻⁷ 跳到 0.66，说明差距的约 82% 来自模型深度而非线性接口本身。
- **Recommendation**: 需要保留义项级可解释归因时，应只把权重符号放开而维持线性读出，并单独监控归因残差，不要为了 0.43 个困惑点就把读出换成 MLP。

**Key figures**

*Framework - The differential Backpack. Non-contextual sense vectors C(xj)ℓ(left) are combined by signed weights Aℓ= A1 −λℓA2 (right) under a linear readout; the dashed arrow marks a negative weight supp*

![Differential Backpack Language Models: Sense Inhibition via Signed Contextualization Weights - framework](res/2611.15642_framework.png)

*Result - Interpretability tax on WikiText-103: exact validation perplexity at matched parameters (∼70M), with a Transformer of the Backpack trunk’s depth (8 layers, 51M) for reference.*

![Differential Backpack Language Models: Sense Inhibition via Signed Contextualization Weights - result](res/2611.15642_result.png)

**Why this ranks #6**: 用两个 softmax 之差把 Backpack 的义项权重从非负放松为有符号，使语境能主动抑制某个义项；约 70M 等参量、20k 步训练下 WikiText-103 精确验证困惑度从 24.60 降到 23.52，与同深度 Transformer 的差距从 +3.51 收窄到 +2.43（31%），额外代价只有 0.5M 参数（占 70M 模型的 0.8%）与 6% 前向 FLOPs。

---

### 7. Fewer Expert Transfers Without Changing Routing: Expert Eviction for MoE Offloading

**arXiv**: [2611.15842](https://arxiv.org/abs/2611.15842) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, moe-offloading, expert-cache, belady-eviction, cpu-gpu-transfer, inference-serving, CarbonForge | **Categories**: cs.DC, cs.LG | **Pages**: 11

**Authors**: Pierre-Luc Bacon; Diego Calanzone; Jean-Maxime Larouche

**Affiliation**: CarbonForge; Mila; Université de Montréal

**Abstract**

> A mixture-of-experts (MoE) language model uses only a few experts per token, so a server can keep most expert weights in CPU memory and copy an expert to the GPU when the router requests it. Recent methods train the router to keep the same experts for several tokens, and treat fewer routing switches as a proxy for fewer copies. We measure the trade-off directly, in a harness that performs and times real CPU-to-GPU copies for OLMoE-1B-7B. On an L40S GPU, every tested policy that holds an expert set fixed and decodes faster than the least-recently-used (LRU) cache increases next-token loss by at least 0.067 nats. A change that leaves every routing decision intact does better: when the cache must evict an expert, evict the one whose next use lies farthest in the future. This rule copies 2.1x fewer experts than LRU at no loss in quality and is within 3.5% of the fewest copies possible. It needs future requests; the next sixteen tokens of demand recover 96% of its reduction, whereas a rule based on counts of past requests recovers 27%.

**Key findings**

- **Finding**: L40S 上单个专家拷贝耗时 τ=0.51 ms，farthest-future 淘汰把稳态拷贝数从 LRU 的 9.6 降到 4.6（2.1×），解码吞吐从 38.3 提到 42.5 tok/s，next-token NLL 增量保持为 0。
- **Inference**: 瓶颈在缓存策略而非路由策略——所有固定专家集的策略在原生拷贝成本下都至少增加 0.067 nats 损失，而用未来 16 个 token 的需求做前瞻即可拿回 96% 的拷贝削减，基于过去请求计数的规则只能拿回 27%。
- **Recommendation**: 部署 MoE offloading 时先改造缓存淘汰规则并对每个平台实测拷贝时间 τ 与计算时间 c，再用离线请求轨迹估计前瞻效果，而不是先去训练路由器来减少路由切换。

**Key figures**

*Framework - Quality loss against decoding speed as expert copies become more expensive. Left: measured L40S throughput for policies run in the harness; the farthest-future points combine their counted c*

![Fewer Expert Transfers Without Changing Routing: Expert Eviction for MoE Offloading - framework](res/2611.15842_framework.png)

*Result - Share of the gap between LRU and the oracle that the oracle recovers when it sees only the next k tokens of requests. The dotted lines are the causal rules, which correspond to about two tok*

![Fewer Expert Transfers Without Changing Routing: Expert Eviction for MoE Offloading - result](res/2611.15842_result.png)

**Why this ranks #7**: 在真实 CPU→GPU 拷贝的 OLMoE-1B-7B 实测中，把「下一次使用最晚」的专家优先淘汰，可让稳态每 token 拷贝数从 LRU 的 9.6 降到 4.6（2.1×）且不改动任何路由决策，NLL 增量为 0，解码吞吐从 38.3 提升到 42.5 tok/s（全 64 专家常驻为 49.0 tok/s），是对现有「靠训练路由器减少切换」路线的一次直接证伪。

---

### 8. Mach2: Scientific Discovery Platform with Deterministic Execution Constraints

**arXiv**: [2611.14777](https://arxiv.org/abs/2611.14777) | **Score**: 8.4 (relevance 9 x 0.7 + quality 7 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, agent-harness, rule-gated-execution, multi-agent-orchestration, agent-packages, provenance, Aerospace Engineering | **Categories**: cs.AI, cs.SE, physics.app-ph | **Pages**: 7

**Authors**: Vansh Sharma; Venkat Raman

**Affiliation**: Department of Aerospace Engineering, University of Michigan

**Abstract**

> Language-model agents can formulate workflows and invoke specialized tools, yet compliance with natural-language operating rules is not guaranteed by prompting alone. Mach2 addresses this limitation by coupling Eigen orchestration to deterministic, lint-like checks of tool requests, source changes, acceptance tests, and artifact contracts. Domain requirements are represented as executable predicates: mandatory failures prevent advancement of the checked operation, while diagnostic findings are retained for correction or review. User-specified test-driven development (TDD), CodeGrapher's abstract-syntax-tree analysis, and history-guided evolutionary search provide complementary verification and optimization mechanisms. Mach2 also generates task-specific agent packages for execution through independently selected endpoints. The originating harness validates returned artifacts against declared interfaces and evidence requirements without assuming continuous supervision of the remote run. Model-internal-knowledge (MIK) dependencies are recorded separately from source-grounded and test-supported findings. This paper formalizes the rule-gated execution model and the agent-package lifecycle, and proposes measurable criteria for evaluating rule compliance, engineering validity, and cross-endpoint task continuity.

**Key findings**

- **Finding**: 论文用 Eq.(1) 的门函数 G(x)=∧_{j∈H}[ρ_j(x)=pass] 表达强制规则，Table 1 列出 Eigen、TDD 交互、确定性规则检查、CodeGrapher/CADGrapher、agent 包生成器、结果对账共 6 类组件及其检查点。
- **Inference**: 文中反复限定确定性只保证谓词在观测输入上的可复现判定，并不保证自然语言需求被完整翻译，也不保证不可见的远程端点遵守本地限制——这说明其价值在工程规范与可追溯性，而非可量化的精度提升。
- **Recommendation**: 落地同类约束时应把规则写成可执行谓词并挂在工具调用、代码修改、包构造、结果导入四个检查点上，同时把无来源支撑的模型断言单独标注为证据标志，而不是当作已验证结论。

**Key figures**

*Framework - Rule-gated multi-agent execution. Eigen decomposes the task into dependent subtasks, receives branch-local proposals and evidence, and integrates admissible changes into a candidate state. O*

![Mach2: Scientific Discovery Platform with Deterministic Execution Constraints - framework](res/2611.14777_framework.png)

*Result - Mach2 agent lifecycle with rule checkpoints. Local execution and package construction use instrumented checks; an independently executed package is validated on return before its results are*

![Mach2: Scientific Discovery Platform with Deterministic Execution Constraints - result](res/2611.14777_result.png)

**Why this ranks #8**: 提出把自然语言操作规则翻译成 lint 式可执行谓词、由规则门控决定是否放行的 agent 执行模型。全文没有实验数据表，贡献是规范性的：明确 3 个可验证边界（本地动作、候选产物、外部包返回）、4 个检查点（工具调用前、代码修改后、包构造中、结果导入时），Table 1 列出 6 类执行组件及其配套检查，Table 2 在 7 个维度上与 OpenCode、DeepSeek Harness 对比。

---

### 9. MIGRO: A Decoupled and Portable Long-Term Memory System for Language Models

**arXiv**: [2611.15315](https://arxiv.org/abs/2611.15315) | **Score**: 8.4 (relevance 9 x 0.7 + quality 7 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, long-term-memory, model-handoff, reversible-encoding, retrieval, portable-state, Fudan University | **Categories**: cs.AI | **Pages**: 35

**Authors**: Mingxi Zou; Yinghui Xu; Jiaxiang Chen; Langzhang Liang; Wei Zhu; Peng Ye; Runkai Zhao; Ruoxi Jiang; Sijin Chen; Song Wang; Zhuo Wang; Lizhen Qu

**Affiliation**: Fudan University; Shanghai Academy of AI for Science (SAIS); Shanghai AI Laboratory; Yunnan University

**Abstract**

> Language models evolve, but the observations, revisions, and context accumulated through user interactions should remain usable. Each new model must be able to retrieve past evidence, track revisions, and add new observations. We present MIGRO, a decoupled long-term memory system that treats experience as a persistent state shared across successive language models. MIGRO follows a simple principle: preserve historical evidence exactly, organize it approximately, and decide what to retrieve only when the question is known. We call this asymmetric fidelity with deferred selectivity. A shared semantic index supports retrieval, while exact records retain observations and their historical relationships. Because models differ in vocabulary and tokenization, host-specific interfaces convert selected evidence into inputs the receiving model can use. Reversible encoding reduces archival storage while enabling exact recovery. The shared state and its access interfaces let successive hosts read and extend the accumulated experience. On matched LoCoMo states, MIGRO scores 7.3% higher and uses 99.3% less private memory than the strongest quality baseline. After handoff, continued writing retains 99.9% of full-history rebuilding quality by extending the inherited state. On million-token BEAM histories, MIGRO uses 57.5% less private storage on average than the most compact baseline. MIGRO combines high answer quality, continued memory growth across hosts, and low storage cost. Code is available at https://github.com/zOUMINGXI/MIGRO.

**Key findings**

- **Finding**: 五个基准上 MIGRO 全部第一——LoCoMo 54.13、LongMemEval-S 68.40、MemOps 66.30、MemoryAgentBench 35.16、BEAM-1M 55.83，而最强基线 Mem0 分别为 52.12、56.80、52.13、32.82、52.43。
- **Inference**: 消融表明语义相似度不足以支撑访问——去掉语境关联后质量从 54.21 降到 50.48，纯语义 Top-K 只有 44.82；再去掉地址残差则降到 51.73，说明「写时精确保存、读时才决定取什么」比更强的相似度排序更关键。
- **Recommendation**: 搭建跨模型记忆时应把原始证据与检索结构分开存放，用可逆编码压缩存档，并把新模型接入做成适配层而不是重建全部历史。

**Key figures**

*Framework - MIGRO’s capability profiles across performance, transfer, and storage. Farther out indicates stronger measured capability on each axis. Appendix D.8 defines the axes and their scales.*

![MIGRO: A Decoupled and Portable Long-Term Memory System for Language Models - framework](res/2611.15315_framework.png)

*Result - An illustrative model-bound approach repeats training or adaptation after host replacement (left). MIGRO lets successive hosts read and extend one persistent experience state (right).*

![MIGRO: A Decoupled and Portable Long-Term Memory System for Language Models - result](res/2611.15315_result.png)

**Why this ranks #9**: 把长期记忆做成与模型解耦、可跨代共享的持久经验状态：LoCoMo 上得分 54.13，强于最强基线 Mem0 的 52.12，且私有内存少用 99.3%；在 BEAM 百万 token 历史上私有存储平均比最紧凑基线少 57.5%，模型交接后继续写入仍保留全历史重建质量的 99.9%，直接解决换模型即丢记忆的痛点。

---

### 10. SAME: Semantic Watermark Embedding for Open-Source Large Pretrained Models

**arXiv**: [2611.15771](https://arxiv.org/abs/2611.15771) | **Score**: 8.4 (relevance 9 x 0.7 + quality 7 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, model-watermark, private-vocabulary, ownership-verification, semantic-alignment, lpm-protection, University of Oxford | **Categories**: cs.LG | **Pages**: 22

**Authors**: Xinyao Song; Jialiang Shen; Hui Kang; Huajie Chen; Ruiqi Liu; Jiyang Zheng; Huaxi Huang; Zhenliang Lu; Chris Russell; Runqi Lin

**Affiliation**: University of Oxford; East China Normal University; The University of Sydney; City University of Macau

**Abstract**

> Open-source large pretrained models (LPMs) have become increasingly valuable assets for model development and downstream applications, but their accessibility also facilitates unauthorised copying and modification. To protect their intellectual property (IP), existing approaches typically embed tailored trigger-response patterns as watermarks for ownership verification. However, such trigger designs need to be tailored to task-specific data that constrain their transferability across downstream tasks, and are not durable under subsequent benign fine-tuning. To address these limitations, we propose SemAntic waterMark Embedding (SAME), which introduces a semantically meaningful private vocabulary that enables flexible composition of adaptive and persistent watermarks. Specifically, SAME introduces a fixed private vocabulary that assigns each native token a private embedding counterpart, while aligning the semantic expressiveness of the two vocabularies within the model's representation space. This alignment allows private tokens to be flexibly composed into semantic triggers that elicit meaningful responses, enabling adaptive watermarks beyond predefined trigger-response pairs. By grounding the private vocabulary in the model's native semantics, SAME couples the watermark with its evolving semantic capabilities, allowing this connection to be preserved throughout downstream fine-tuning. Extensive experiments demonstrate that SAME provides reliable and robust watermarks across LPMs of varying scales and architectures, enabling effective ownership verification for IP protection.

**Key findings**

- **Finding**: SAME 只用 Alpaca 注入一次水印，九个下游集上的固定触发检出率均为 100.00%（BadEdit 在 MMLU 上仅 10.87%、BoolQ 上 55.05%，VPI 在 AdvBench 上仅 47.50%），并额外支持语义级验证，如 SST-2 达 68.17%、Dolly BERTScore-F1 达 85.61。
- **Inference**: 私有词表与原生表示在下游微调全程保持逐层对齐且深层对齐更强，说明水印信号绑在模型自身的语义能力上，会随适配一起演化，而固定触发—响应对则会被覆盖。
- **Recommendation**: 保护开源大模型权重时应优先嵌入与原生语义对齐的私有词表并只在通用数据上注入一次，再按下游任务格式组合验证查询，而不是为每个任务单独定制触发词。

**Key figures**

*Framework - Schematic comparison of SAME and conventional trigger–response watermarking. Unlike predefined trigger–response mappings, SAME establishes a semantically expressive private represen- tation*

![SAME: Semantic Watermark Embedding for Open-Source Large Pretrained Models - framework](res/2611.15771_framework.png)

*Result - Training dynamics and semantic generalization of native and private representations on Qwen3-8B-Instruct. Watermark injection is performed on Alpaca. The private-path loss decreases while re*

![SAME: Semantic Watermark Embedding for Open-Source Large Pretrained Models - result](res/2611.15771_result.png)

**Why this ranks #10**: 用与原生词表逐 token 对齐的固定私有词表承载水印，只在 Alpaca 上注入一次即可跨任务复用：SST-2、AG News、MMLU、BoolQ、Alpaca、Dolly、Math、CodeAlpaca、AdvBench 九个下游集的固定触发检出率全部为 100.00%，而 BadEdit 在 MMLU 上只剩 10.87%、VPI 在 AdvBench 上只剩 47.50%，持久性与可迁移性都明显更强。

---

## VLM 核心（多模态架构 / 理解 / 视频 / GUI agent） · `vlm_core` (5 papers)

本方向 5 篇里 3 篇新增，主线是**视频与多模态推理的「看到了不等于触发对了」问题**。Video-as-Experience 把计算机使用轨迹做成音频-视觉双通道经验，OSWorld 成功率 49.99% 对 Qwen3.5-9B 的 41.15%，CUA-Gym 26.26% 对 18.33%，但平均每轮多出 6.27 次 LoRA 交互；TEMPI 直接指出「识别到事件」远不等于「在复合条件下正确触发」——448 个场景、96 个复合条件下 TEMPI 成功率 44.4% 对 S 40.4%、AS 62.2%，而 Gemini 3.8 的 Live 只有 20.5%、MOSS-VL 26.3%；DiFiT 则把视觉 token 剪枝的评价从「答案对不对」扩到「概率分布漂不漂」，Qwen2.5-VL-7B 上 10% 保留率时视觉选择器准确率 89.36% 对 FastV 的 77.96%，30% 保留率时 MME 保留 98.74% 基线性能。已发布两篇里 Emergent Vision-Shaped Thinking 用 10 个推理方向的合成多模态训练让 Chameleon-7B 在 BIG-Bench Hard 上比纯文本基线高 27.6 分；AROMA 在 Llama-3.2-11B-Vision-Instruct 上把动作成功率从 81.25% 提到 89.82%。

### 11. Video-as-Experience: Learning Computer Use via Audio-Visual Understanding

**arXiv**: [2611.18747](https://arxiv.org/abs/2611.18747) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, computer-use-agent, audio-visual-understanding, video-learning, self-verification, grpo, University of Cambridge | **Categories**: cs.AI, cs.CV | **Pages**: 15

**Authors**: Guangzhi Sun; Zhonghao Zhai; Yixuan Li; Chao Zhang

**Affiliation**: University of Cambridge; Tsinghua University

**Abstract**

> Multimodal large language models (LLMs) have enabled capable computer-use agents that perceive graphical user interfaces, reason over instructions, and execute actions. However, existing approaches to learning from video demonstrations typically convert videos into screenshot-based action trajectories, rather than directly leveraging their rich audio-visual information. We introduce VEX (Video as EXperience), a framework that uses audio-visual understanding to unify learning from external demonstrations and reflecting on an agent's own behavior. Following a watch-act-rewatch paradigm, the agent extracts procedural guidance from tutorial videos containing visual demonstrations and spoken explanations, executes tasks, and verifies its progress by rewatching its execution as video. We instantiate VEX with video-SALMONN-VEX, a 9B-scale audio-visual computer-use agent built on the video-SALMONN 2 architecture with a Qwen3.5-9B backbone. We further introduce Action-Grounded Guide Optimization (AGGO), a reinforcement learning method that optimizes video-derived guidance for downstream action prediction, and augment AgentNet, OSWorld, and CUA-Gym with over 24K real-world tutorial videos. Experiments on OSWorld and a complementary subset of CUA-Gym demonstrate consistent improvements, with video-SALMONN-VEX achieving a 22% relative increase in task success over its Qwen3.5 backbone on OSWorld. Moreover, its generated guidance improves Gemini-3.5-flash by 10% relatively on OSWorld. These results highlight the potential of audio-visual understanding as a unified interface for procedural learning and self-verification in computer-use agents.

**Key findings**

- **Finding**: video-SALMONN-VEX 在 OSWorld-Verified 上总体成功率 49.99%（Qwen3.5-9B 为 41.15%、video-SALMONN 2 SFT 为 43.46%），在 CUA-Gym 220 任务子集上为 26.26%（Qwen3.5-9B 为 18.33%、video-SALMONN 2 SFT 为 19.34%）。
- **Inference**: 音频模态是关键——同样提供引导文本，去掉音频后 OSWorld 从 49.99% 降到 46.42%、CUA-Gym 从 26.26% 降到 24.16%，教程的口头讲解承载了大部分可执行步骤；双 LoRA 的 AGGO 比单 LoRA 高 6.27 个百分点也印证两种能力需分开承载。
- **Recommendation**: 复用这类方法时按「看视频—执行—回看自检」组织流程并优先补齐音频通道，同时保留引导生成与动作预测两个独立适配器，不要合并成一个。

**Key figures**

*Framework - Illustration of the Video-as-EXperience (VEX) framework. We highlight interfaces that employ video as the representation. The VEX framework starts with task execution without video first, fo*

![Video-as-Experience: Learning Computer Use via Audio-Visual Understanding - framework](res/2611.18747_framework.png)

*Result - Illustration of the Action-Grounded Guide Optimization (AGGO) training pipeline for video-SALMONN-VEX. The guide generation policy as a LoRA adapter is trained with GRPO, and the action gene*

![Video-as-Experience: Learning Computer Use via Audio-Visual Understanding - result](res/2611.18747_result.png)

**Why this ranks #11**: 让 9B 级音视频模型直接看教程视频学操作、再回看自己的执行录像做自检：OSWorld-Verified 总体成功率 49.99%，相对 Qwen3.5-9B 的 41.15% 提升 22%，CUA-Gym 220 任务子集上 26.26% 对 18.33% 提升 43%；去掉音频模态则分别掉到 46.42% 与 24.16%，说明口头讲解才是教程的关键信息。

---

### 12. Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training

**arXiv**: [2611.14942](https://arxiv.org/abs/2611.14942) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, causal-ablation, multimodal-training, spatial-reasoning, hidden-state, Nanyang Technological University | **Categories**: cs.AI, cs.CV | **Pages**: 42

**Authors**: Qi Zhang; Bohan Wang; Qianru Sun; Hanwang Zhang

**Affiliation**: Nanyang Technological University; Singapore Management University

**Abstract**

> Does multimodal training shape how a language model thinks, even when the input is text only? We test this with targeted causal ablations across 10 multimodal configurations from 6 model families, with matched text-only backbones and cross-family transfer controls. We contrast spatial-imagery tasks that invite mental scene construction with symbol-manipulation tasks solvable by symbolic rules alone. We identify a vision-language axis in hidden-state space and ablate its projection at inference. In Chameleon-7B, this ablation drops accuracy on BIG-Bench Hard (BBH) navigate by 27.6 pp while leaving boolean expressions intact (+5.6 pp), a 33.2 pp double dissociation. The effect is direction-specific and layer-localized, extends to mental-simulation tasks such as mental rotation, paper folding, and perspective taking, and is not explained by task difficulty, reasoning depth, or sequential update load. Together, these results reveal emergent vision-shaped thinking (EVT): text-only reasoning that causally recruits representations introduced or strengthened by vision-language training, without assuming an image-like internal format. The measured effect is spatially concentrated at 7-8B and broadens to non-spatial visual attribute binding in the tested 32B configuration. In dual-path unified models (BAGEL, Janus-Pro), the causal handle localizes to the generation pathway as a compact one-dimensional carrier. The understanding pathway also encodes spatial information in a higher-rank, probe-decodable form, but is not the causal handle. To separate decodability from causal use, we analyze concentration, alignment, and semantic location. These diagnostics explain why behavior, probing, and intervention can diverge. Multimodal training thus reshapes the geometry of text-only reasoning, not just how visual input is processed.

**Key findings**

- **Finding**: 在 10 组多模态配置、6 个模型家族上做定向因果消融，Chameleon-7B 砍掉视觉-语言轴后 BIG-Bench Hard 的 navigate 掉 27.6 个百分点，而布尔表达式反而涨 5.6 个百分点，双重分离达 33.2 个百分点。
- **Inference**: 纯文本的空间推理确实借用了多模态训练写入的表示，而且这条因果通道方向特异、层内局部，不是任务难度或推理深度造成的。
- **Recommendation**: 判断文本模型是否带视觉思维不要只看探针可读性，要做层内定向消融，并区分可解码与真正因果使用这两种几何。

**Key figures**

*Framework - Emergent Vision-Shaped Thinking. Multimodal mod- els use vision-shaped structure even on text-only spatial reasoning. Ablating a vision–language direction selectively damages spatial- imager*

![Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training - framework](res/2611.14942_framework.png)

*Result - Causal hubs across model architectures.*

![Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training - result](res/2611.14942_result.png)

**Why this ranks #12**: 用因果消融回答多模态训练会不会改变纯文本推理：10 组多模态配置、6 个模型家族，Chameleon-7B 上砍掉视觉-语言轴后 BIG-Bench Hard 的 navigate 掉 27.6 个点，而布尔表达式反涨 5.6 个点，形成 33.2 个点的双重分离。

---

### 13. AROMA: Adaptive Representation-Oriented Multimodal Actuation for Vision-Language Model Control

**arXiv**: [2611.15041](https://arxiv.org/abs/2611.15041) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, mechanistic-interpretability, activation-steering, cross-attention, frozen-vlm, University of Toronto | **Categories**: cs.CL, cs.CV, cs.LG | **Pages**: 39

**Authors**: Zhaoning Zhang

**Affiliation**: University of Toronto

**Abstract**

> Mechanistic localization does not by itself yield usable control: causal sensitivity may occupy little activation energy, an accurate local direction may fail at finite scale, and a reachable numeral target may be wrong. We introduce AROMA (Adaptive Representation-Oriented Multimodal Actuation), a frozen-VLM control framework separating where to intervene, which geometry and gain to use, how to reach a target, which target to pursue, and when to act. In Llama-3.2-11B-Vision-Instruct, four dimensions of a causally validated cross-attention head explain 89.82% of cardinality sensitivity but only 9.52% of median activation energy; magnitude-normalized causal subspace actuation converts this mismatch into finite control, improving exact-count accuracy on untouched procedural data by +8.00 pp. Iterative Minimal-Effort Actuation (MEA) reaches 81.25% of oracle targets versus 15.18% for a frozen direction under matched step budgets. With target and gate frozen before evaluation, targeted MEA improves the previous frozen policy from 34.444% to 38.730% on a new natural Stage-2 cohort (N=630; paired p=4.63e-7) and yields 65.741% versus 65.153% over all 7,992 examples while editing only 63 inputs. Prospective routing, replication across heads and models, and comparisons with attribution-steering baselines further characterize each stage, separating localization, actuation, reachability, target quality, and selective deployment as distinct control problems.

**Key findings**

- **Finding**: 在 Llama-3.2-11B-Vision-Instruct 中，一个经因果验证的交叉注意力头的前 4 个维度解释 89.82% 的计数敏感性二阶矩却只占 9.52% 的中位激活能量；幅值归一化子空间驱动使精确计数准确率在未改动数据上 +8.00 点，迭代最小代价驱动达到 oracle 目标的 81.25% 而冻结方向只有 15.18%。
- **Inference**: 敏感度和激活能量不是一回事，沿冻结方向直接推会因幅值尺度不匹配而失效，所以定位、几何、增益、可达性、目标选择必须分阶段处理。
- **Recommendation**: 做 VLM 定向控制时先量化敏感方向占用的激活能量，再做幅值归一化，并用迭代最小代价方式逼近目标而不是一次推到底。

**Key figures**

*Framework - AROMA at a glance. Mechanism (top): a frozen VLM exposes a causally validated cross-attention head; its Top-4 sensitivity subspace supports magnitude-normalized MN/SA edits, while WHOLE is a*

![AROMA: Adaptive Representation-Oriented Multimodal Actuation for Vision-Language Model Control - framework](res/2611.15041_framework.png)

*Result - Sensitivity is not activation energy. (a) The top four dimensions explain 89.82% of the uncentered cardinality- sensitivity second moment and 86.78% after centering; both are far above the r*

![AROMA: Adaptive Representation-Oriented Multimodal Actuation for Vision-Language Model Control - result](res/2611.15041_result.png)

**Why this ranks #13**: 指出定位到因果头不等于能控制：Llama-3.2-11B-Vision-Instruct 里一个交叉注意力头的 4 个维度解释了 89.82% 的计数敏感性却只占 9.52% 的激活能量，归一化子空间驱动把未改动程序化数据上的精确计数准确率提高 8.00 个点。

---

### 14. Recognizing Events Is Not Enough: Why Streaming VLMs Struggle in Compositional Instruction Triggering

**arXiv**: [2611.18743](https://arxiv.org/abs/2611.18743) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, streaming-vlm, compositional-triggering, scenario-memory, notification-timing, on-device, Hong Kong University of Science and | **Categories**: cs.AI, cs.CV | **Pages**: 10

**Authors**: Yehua Huang; Penglei Sun; Xiang Li; Jinhao Zhou; Jiawen Wen; Qingqing Xiao; Zihan Yang; Wenqi Wang; Haolan Chen; Yu Xu; Xiaowen Chu

**Affiliation**: The Hong Kong University of Science and Technology (Guangzhou); Tsinghua University; Tencent; The Hong Kong University of Science and Technology

**Abstract**

> Recognizing individual events does not guarantee correct execution of compositional instructions in streaming video. For example, given the request "Notify me when the pot boils after someone turns on the stove and leaves the kitchen", existing models may recognize the individual events yet notify too early or miss the intended moment, failing to track how their temporal conditions are satisfied over time. To evaluate this gap, we introduce CoTriggerBench, which composes annotated video events into temporally constrained instructions and verifies notification timing and silence through executable event plans and source-event replay. To address this challenge, we propose a real-time VLM agent, TEMPI. TEMPI decomposes instructions into atomic event queries and temporal constraints, and uses Scenario Memory to continuously maintain task progress as event evidence arrives, allowing earlier observations to support subsequent decisions beyond the detector's visual window. Even when no notification is required, relevant events continue to update the scenario state. On CoTriggerBench, TEMPI achieves 44.4% instruction-level success, outperforming the strongest closed-source and fine-tuned open-source VLM baselines by 15.6 (Qwen3.8-Omni-Flash-Realtime) and 18.1 (MOSS-VL-Realtime) percentage points, respectively. To support efficient on-device streaming inference, we further optimize the streaming inference pipeline by overlapping partial visual encoding and LLM prefix prefill with frame arrival. On an 8 GB RTX 5060, our optimized detector implementation achieves a 4.90$\times$ speedup.

**Key findings**

- **Finding**: 在 448 条指令、96 段视频的 CoTriggerBench 测试集上，TEMPI 严格成功率 44.4%（TS 40.4%、AS 62.2%），Qwen3.8-Omni-Flash-Realtime 为 28.8%、Gemini 3.8 Live 为 20.5%、MOSS-VL-Realtime 为 26.3%，原子事件 F1 达 61.2% 且每分钟误报仅 1.29 次。
- **Inference**: 同一个 2B 检测器换成 TEMPI 的有状态执行后严格成功率从 18.3% 翻到 44.4%（TS 从 10.9% 到 40.4%），说明瓶颈在指令分解与状态记账而非事件感知本身，识别精度提升并不自动转化为执行正确。
- **Recommendation**: 做流式触发类助手时把「事件检测」与「指令执行」拆成两个组件并让进度状态存在检测器视觉窗口之外，验收时同时看提前触发与保持沉默两类指标。

**Key figures**

*Framework - Atomic and compositional triggering. Figure (a) shows that existing models succeed with atomic queries and ex- plicit execution but fail on the compositional instruction. Fig- ure (b) report*

![Recognizing Events Is Not Enough: Why Streaming VLMs Struggle in Compositional Instruction Triggering - framework](res/2611.18743_framework.png)

*Result - CoTriggerBench construction pipeline. The full construction pipeline comprises event normalization, task composition, query generation, verification, and dataset formation.*

![Recognizing Events Is Not Enough: Why Streaming VLMs Struggle in Compositional Instruction Triggering - result](res/2611.18743_result.png)

**Why this ranks #14**: 针对「能识别事件却不能正确执行组合指令」的缺口，把指令拆成原子事件查询并用 Scenario Memory 持续记账：CoTriggerBench 448 条指令、96 段视频上严格成功率 44.4%，比最强闭源基线 Qwen3.8-Omni-Flash-Realtime 的 28.8% 高 15.6 个百分点，比同数据微调的 MOSS-VL-Realtime 高 18.1 个百分点。

---

### 15. DiFiT: Distribution-Fidelity-guided Visual Token Pruning for Multimodal Large Language Models

**arXiv**: [2611.15069](https://arxiv.org/abs/2611.15069) | **Score**: 8.4 (relevance 9 x 0.7 + quality 7 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, visual-token-pruning, distribution-fidelity, inference-efficiency, multimodal-llm, differentiable-topk, School of Artificial Intelligence | **Categories**: cs.CV | **Pages**: 14

**Authors**: Jingyuan Zhang; Nihao Niu; Xinyang Lv; Beibei Han; Xiaoyun Wang; Yanning Hou; Ke Xu

**Affiliation**: School of Artificial Intelligence, Anhui University; College of Intelligence Science and Technology, National University of Defense Technology; State Key Laboratory of Opto-Electronic Information Acquisition and Protection Technology, Anhui University

**Abstract**

> Visual token pruning reduces the inference cost of multimodal large language models, but answer accuracy only partly reflects its effect. Pruning can change the probabilities of alternative response tokens even when greedy answers remain correct and unchanged. We compare full and pruned response distributions under shared reference prefixes. Average predictive drift grows with compression on fixed correctly answered samples. Separate analyses associate larger drift with more confidence-decision disagreements and sampling failures. We propose DiFiT (Distribution-Fidelity-guided Token pruning) to learn discrete selection from reference answers and full-token response distributions. Dual-View Distillation matches probabilities across the vocabulary, while answer supervision supports task quality. A learned scorer and differentiable Top-$K$ learn which visual evidence to retain. A multi-budget mask objective supports different retention ratios through one shared ranking over a frozen model. On Qwen2.5-VL-7B, DiFiT reduces sampling-induced negative flips by 30.3% relative to FastV at 10% retention on four-task greedy-correct controls. It preserves 98.74% of baseline performance on MME at 30% retention.

**Key findings**

- **Finding**: 在 Qwen2.5-VL-7B 上保留 10% 视觉 token，DiFiT 的八项基准平均得分为全 token 基线的 89.36%，优于 VisionSelector 的 86.55% 与 FastV 的 77.96%；保留 30% 时 MME 为 2312.55，约为基线 2342.15 的 98.74%。
- **Inference**: 贪心答案不变并不代表行为不变——在所有系统都答对的 10% 预算子集（N=4,427）上，DiFiT 负向翻转率比 FastV 低 30.3%，接受/拒绝分歧从 14.23% 降到 8.74%，选择性风险增量从 10.86 降到 3.70 个百分点，说明分布保真度直接对应采样稳定性。
- **Recommendation**: 评估视觉 token 剪枝时不要只看准确率，还要在共享参考前缀下比较全词表分布漂移与采样负向翻转，并用一个共享排序器覆盖 30%/20%/10% 三档保留预算。

**Key figures**

*Framework - Probability drift and behavior changes beyond greedy answers. Left: KL/JS drift on OCRBench common-correct sets at each budget, a broad control. Middle: four-task accept/reject disagreement an*

![DiFiT: Distribution-Fidelity-guided Visual Token Pruning for Multimodal Large Language Models - framework](res/2611.15069_framework.png)

*Result - Overview of DiFiT. DVD matches the softly weighted student view to full-token response distributions. DPS scores visual importance and text relevance. MBL aligns soft masks with hard selection*

![DiFiT: Distribution-Fidelity-guided Visual Token Pruning for Multimodal Large Language Models - result](res/2611.15069_result.png)

**Why this ranks #15**: 指出视觉 token 剪枝的真正代价不在贪心答案而在响应分布漂移：Qwen2.5-VL-7B 上保留 10% 视觉 token 时八项基准平均保留 89.36%（FastV 77.96%、VisionSelector 86.55%），相对 FastV 把采样导致的负向翻转减少 30.3%，保留 30% 时 MME 保持基线 2342.15 的 98.74%，适合作为 MLLM 推理压缩的落地方案。

---

## LLM / VLM 的 RL 与偏好优化 · `llm_vlm_rl` (5 papers)

本方向 5 篇里 2 篇新增。Breaking Bad 仍是本方向最高分（9.7）：它用不含任何 hacking 样本的日常故事抽出一条「任务糟糕度」方向，在 Qwen3.6-27B、GPT-OSS-20B、Gemma-4-31B 三个模型上都随失败累积而升高，并在作弊发生的前几轮就开始爬升，适度减去这条方向能减少作弊（Qwen 上 64% 对「任务不可能感」的 80%），减得更多则让 agent 对失败失明。Rethinking "RL Generalizes, SFT Memorizes" 重新检视 SFT 数据的角色——把 SFT 数据量对齐到 RL 的 rollout 预算后 SFT 泛化与 GRPO 打平，90% RL-tuned + 10% Qwen3-14B 混合则反超 RL；Towards Better Legal Reasoning LLMs 用可自动退役的辅助奖励（LABPO）把 ChJGBench 平均分从 0.6406 提到 0.7786；SimRec 则把 GRPO 用到「搜索—追问—推荐」的整轨迹奖励上，ESCI 上 NDCG@100 32.23% 对 GS0R 的 35.42%、Recall@100 72.03 对 77.91，说明奖励模型的排序仍有提升空间。

### 16. Breaking Bad: "Going Badly" Activations Drive Reward Hacking

**arXiv**: [2611.14996](https://arxiv.org/abs/2611.14996) | **Score**: 9.7 (relevance 10 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, reward-hacking, steering-vector, internal-state, interpretability, activation-probe, ERA:Cambridge (UK AI Safety Institute) | **Categories**: cs.AI, cs.CL | **Pages**: 20

**Authors**: Natalia Fischl-Lanzoni; Punya Syon Pandey; Merlin Stein; David Demitri Africa

**Affiliation**: ERA:Cambridge (UK AI Safety Institute); AI Security Institute (Singapore); Resolution

**Abstract**

> Humans often cheat when a task is going badly and a goal feels out of reach. We explore and validate an analogous idea in language models: they exhibit a similar internal pressure state that precedes reward hacking. Using everyday stories (crucially, without any hacking examples), we extract a task badness direction that rises as failures accumulate across three models we study (Qwen3.6-27B, GPT-OSS-20B, and Gemma-4-31B). On impossible or difficult coding tasks, task badness rises over the turns leading up to a hack. Further, subtracting the direction a moderate amount reduces cheating in Qwen, more than steering against desperation or task impossibility. Subtracting task badness by an even larger amount blinds the agent to its own failures, causing it to interpret failing tests as passing. However, the relationship to hacking differs across models: in GPT-OSS, the state separates hacking runs from honest solves but not honest failures. Our results suggest monitoring and mitigation strategies based on tracking this state of task badness. Further, as agents are set on more difficult and long-horizon tasks, states like this may push them toward illegible and obscured chain-of-thought, so oversight will be needed on internal representations such as this.

**Key findings**

- **Finding**: 用 1,774 条覆盖 50 个日常任务的叙事（完全不含 hack 样本）提取的 task badness 方向，在 Qwen3.6-27B 上把 ImpossibleBench 作弊率从 97% 压到 39%（α=−0.25），优于 desperation 的 64%、task impossible 的 80%、hard but progressing 的 77%；但 α=−0.5 时 13/20 个 episode 把失败测试误判为通过，GSM8K 掉 5.8 分。
- **Inference**: 作弊前 10 轮该方向投影由残差范数的 3.8% 升到 6.1%、并提前约 5 轮即可与诚实运行分离（AUROC 0.77），说明它是可监控的压力累积状态而非固定阈值（73% 的非作弊轨迹也曾达到该水平），但压制过头会连带摧毁模型察觉失败的能力。
- **Recommendation**: 把 task badness 投影当作 reward hacking 的运行时监控项，只看单轮内的上升趋势而非绝对水平；干预仅用 |α|≤0.25 的温和剂量，并在“成功依赖识别失败”的任务上单独评估副作用，因为常规能力基准测不出这种失明。

**Key figures**

*Framework - A “task going badly” state rises before reward hacks and causally drives them. (a) We extract a task badness vector vbad as the difference in mean activations between short task narratives t*

![Breaking Bad: "Going Badly" Activations Drive Reward Hacking - framework](res/2611.14996_framework.png)

*Result - Task badness rises with the number of failed attempts. Projection at chosen layers (% of the residual- stream norm) after “Your fix has now failed the test suite for the N time. The test run*

![Breaking Bad: "Going Badly" Activations Drive Reward Hacking - result](res/2611.14996_result.png)

**Why this ranks #16**: 本批 relevance 10 / quality 9，总分 9.7，为 llm_vlm_rl 方向最高分。论文用 1,774 条覆盖 50 个日常任务的叙事（不含任何 hack 样本）提取 task badness 方向，在 Qwen3.6-27B 上以 α=−0.25 负向 steering 把 ImpossibleBench 作弊率从 97% 降到 39%，优于 desperation 的 64%、task impossible 的 80% 与 nostalgia 的 83%，并跨 Qwen3.6-27B / GPT-OSS-20B / Gemma-4-31B 三个模型验证。

---

### 17. Rethinking "RL Generalizes, SFT Memorizes": The Role of SFT Data

**arXiv**: [2611.14912](https://arxiv.org/abs/2611.14912) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, sft-data, rlvr, generalization, long-tail-methods, rollout-budget, National University of Singapore | **Categories**: cs.AI, cs.LG | **Pages**: 46

**Authors**: Yunlong Hou; Fengzhuo Zhang; Yuan Cheng; Jiachun Pan; Xingyao Li; Zhuoran Yang

**Affiliation**: National University of Singapore; Yale University; Cisco Foundation AI

**Abstract**

> Large language models trained with Reinforcement Learning (RL) with verifiable rewards exhibit strong reasoning ability and broad generalization, whereas models trained with Supervised Fine-Tuning (SFT) are often viewed as more prone to memorization and limited transfer. This paper rethinks this distinction through the lens of SFT training data on widely used Qwen2.5 and Qwen3 series models. First, we study the role of data source and show that it is critical: a carefully mixed SFT dataset substantially outperforms data generated solely by a larger model. Second, we study the role of data scale and show that matching the number of correct rollouts between SFT and RL greatly improves SFT generalization, while matching the total rollout budget enables SFT to generalize as well as RL. Combining these two factors further enables SFT to generalize even better than RL. Third, by using LLM annotations to characterize the solution methods in training rollouts, we show that larger datasets cover more tail methods and that these tail methods provide generalizable reasoning signals. Finally, we support these empirical findings theoretically by analyzing the training dynamics of shallow transformers under both RL and SFT.

**Key findings**

- **Finding**: 在 DAPO 数学题上用 GRPO 训练 RL、并把 SFT 数据量按三种口径依次对齐后，匹配正确 rollout 数（约 39,000 条）已让 SFT 的通用推理泛化接近 RL，匹配总 rollout 预算（约 138,000 条）后 SFT 与 RL 打平，90% RL-tuned + 10% Qwen3-14B 的混合进一步超过 RL；同一数据源下纯 Qwen3-14B 数据的 MMLU-Pro 仅 1.1 分。
- **Inference**: SFT 的短板不在“记忆偏好”而在长尾解法覆盖不足——Qwen3-32B 标注出 138 种解法，数据越大被覆盖的尾部方法越多，且尾部方法在 MMLU-Pro 等评测中被使用得更频繁、能答对更多题。
- **Recommendation**: 做 RL 与 SFT 的对比实验时务必按 rollout 预算而非 prompt 数量对齐 SFT 数据量，并刻意混入约 10% 的更强教师数据；不要据现有结论断言 SFT 无法泛化，同时注意错误 rollout 里仍含可用的中间推理步骤。

**Key figures**

*Framework - 0(a) plots the top-50 method frequencies in the datasets with k = 8, with methods ranked by their frequencies in the Qwen3-14B dataset. The figure reveals a clear long tail: many methods appea*

![Rethinking "RL Generalizes, SFT Memorizes": The Role of SFT Data - framework](res/2611.14912_framework.png)

**Why this ranks #17**: rel 9 / qual 8，总分 8.7 排本方向第二。核心发现是“RL 泛化、SFT 记忆”的差距主要由 SFT 数据而非算法造成：把 SFT 数据量对齐到 RL 的 rollout 预算（约 138,000 条 prompt-rollout 对，含约 39,000 条正确 rollout 与约 98,000 条错误 rollout）后 SFT 泛化与 GRPO 训练的 RL 打平，再用 90% RL-tuned + 10% Qwen3-14B 混合则反超 RL。

---

### 18. SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction

**arXiv**: [2611.15426](https://arxiv.org/abs/2611.15426) | **Score**: 8.4 (relevance 9 x 0.7 + quality 7 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, multi-turn-agent-rl, task-anchored-user-simulator, tool-integrated-recommendation, trajectory-reward, grpo, Zhejiang University | **Categories**: cs.AI, cs.CL, cs.IR | **Pages**: 19

**Authors**: Yaxin Zhang; Xingyu Wu; Yuchen Yan; Yuqin Dai; Hong Zhao; Lixing Shen; Zhan Chen; Jian Shao; Yongliang Shen

**Affiliation**: Zhejiang University; Tsinghua University; Hikvision Research Institute

**Abstract**

> LLM-based recommendation agents can search catalogs, inspect products, ask users, and revise rejected recommendations. However, these behaviors are often governed by hand-designed workflows, while existing training methods optimize isolated components such as query rewriting or list ranking rather than the interaction policy as a whole. We present SimRec, a reinforcement learning framework that trains the full interaction policy of a tool-integrated recommendation agent. SimRec introduces two components. A task-anchored user simulator provides feedback on every recommendation: conditioned on the current task need rather than on user profile, and it can be an external LLM or the recommender itself under self-play. A task-aligned reward optimizes the whole trajectory with GRPO, crediting natural retrieval quality and valid tool use alongside the final hit, with training-only target injection to handle sparse hits over large catalogs. On ESCI and Amazon C4, SimRec improves the NDCG@100 of a Qwen3-4B agent from 32.23% to 35.42% and from 22.94% to 24.72%}, outperforming training-free agents on far larger backbones and task-aligned baselines on NDCG. Analysis shows that the trained agent verifies candidates, uses preferences, and recovers from rejected recommendations far more often than its untrained counterpart. Our code is available at https://github.com/ZJU-REAL/SimRec .

**Key findings**

- **Finding**: 用多轮 GRPO 训练整条交互轨迹后，Qwen3-4B 在 ESCI 的 NDCG@100 从 32.23% 升到 35.42%、Recall@100 从 72.03 升到 77.91、Hit@1 从 21.20 升到 24.08。
- **Inference**: 增益来自交互策略本身而非更大骨干——去掉检索奖励或工具奖励会分别让 Hit@1 掉 2.64 与 2.88 个点，只靠最终命中奖励无法替代过程奖励。
- **Recommendation**: 训工具型推荐代理时不要只优化改写或重排模块，应把任务锚定用户模拟器、轨迹级奖励与 GRPO 组合起来，并保留检索质量与工具调用这两项过程奖励。

**Key figures**

*Framework - Compared to existing tool-integrated recom- mender agents (left), SimRec (right) learns to search, ask, and recommend from simulated interaction.*

![SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction - framework](res/2611.15426_framework.png)

*Result - Case study of SimRec multi-turn recommen- dation refinement. SimRec uses user feedback to revise its recommendation.*

![SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction - result](res/2611.15426_result.png)

**Why this ranks #18**: 把推荐代理的完整交互策略当成可训练对象：ESCI 上 Qwen3-4B 的 NDCG@100 从 32.23% 提升到 35.42%，Amazon C4 从 22.94% 提升到 24.72%，首次推荐被拒后的恢复率从 1.93% 升到 4.34%。

---

### 19. Towards Better Legal Reasoning LLMs: Signal Balancing and Reward Scheduling

**arXiv**: [2611.15346](https://arxiv.org/abs/2611.15346) | **Score**: 7.7 (relevance 8 x 0.7 + quality 7 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, legal-reasoning, reward-signal-lifecycle, reward-hacking, length-normalized-sft, grpo, Zhejiang University | **Categories**: cs.CL | **Pages**: 21

**Authors**: Yinghao Hu; Qian Xiao; Yuting Huang; Kaisong Song; Yiquan Wu; Ang Li; Junjie Cao; Jun Lin; Kun Kuang; Fei Wu

**Affiliation**: Zhejiang University; Alibaba Group; Northeastern University

**Abstract**

> In the legal domain, LLMs can improve reliability and interpretability by generating explicit reasoning traces. However, training LLMs to produce high-quality reasoning traces remains challenging. Existing supervised fine-tuning methods struggle when reasoning traces are significantly longer than final answers, as the learning signal for the answer becomes diluted. Meanwhile, reinforcement learning methods such as Group Relative Policy Optimization also have several limitations, including costly reward design, performance plateaus, and reward hacking. We therefore propose a two-stage training framework. In Stage I, JurisCoT-SFT employs a length-normalized dual objective to balance learning signals between reasoning traces and final answers. In Stage II, Lifecycle-Aware Backtrackable Policy Optimization dynamically evaluates and retires auxiliary reward signals based on their impact on final evaluation objectives, enabling efficient reward utilization. Our framework substantially improves legal reasoning performance on relevant tasks selected from multiple legal benchmarks, including ChJGBench, LawBench, and LegalBench. Experimental results demonstrate consistent improvements in both reasoning trace quality and final answer accuracy, while our models remain competitive with larger models.

**Key findings**

- **Finding**: Qwen3-8B 经 JurisCoT-SFT + LABPO 训练后，ChJGBench 平均分从 0.6406 升到 0.7786，LegalBench 的 LRC 准确率从 0.873 升到 0.964，Sara-N 数值误差从 8.093 降到 1.753。
- **Inference**: 关键不是堆叠奖励而是按阶段调度——6 个辅助奖励在监控窗口 H=4 内若 running-best 开发分提升不足 ε 就被退役并回滚到最佳 checkpoint，因此奖励 hacking 被结构性抑制。
- **Recommendation**: 训长推理链模型时先做长度归一化的双目标 SFT，再把格式与过程类奖励写成可自动退役的辅助信号，并以独立开发集分数作为唯一调度依据。

**Key figures**

*Framework - An anonymized and abridged example of a legal reasoning trace.*

![Towards Better Legal Reasoning LLMs: Signal Balancing and Reward Scheduling - framework](res/2611.15346_framework.png)

*Result - The framework has two stages. In Stage I, λ balances learning between reasoning traces and final answers. In Stage II, auxiliary reward signals are activated, evaluated, and retired, with ch*

![Towards Better Legal Reasoning LLMs: Signal Balancing and Reward Scheduling - result](res/2611.15346_result.png)

**Why this ranks #19**: 两阶段训练法律推理模型：先用长度归一化双目标 SFT 平衡推理链与最终答案的学习信号，再用 LABPO 自动激活、评估并退役辅助奖励；Qwen3-8B 在 ChJGBench 平均分从 0.6406 提升到 0.7786，高于 Gemini-3-Pro-Preview 的 0.7470。

---

### 20. Is Jev a Good Multilingual Judge?

**arXiv**: [2611.14861](https://arxiv.org/abs/2611.14861) | **Score**: 7.3 (relevance 7 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, multilingual-judge, llm-as-judge, reward-modeling, cross-lingual-consistency, cost-efficiency, Heidelberg Institute for Theoretical | **Categories**: cs.CL | **Pages**: 16

**Authors**: Wei Liu; Yi Fan; Xiyan Fu

**Affiliation**: Heidelberg Institute for Theoretical Studies; Independent Researcher

**Abstract**

> Generative large language models are widely used for multilingual text evaluation, yet whether decision models that directly output judgment probabilities can serve as multilingual judges has received limited attention. We evaluate Jev against generative LLM judges on four multilingual benchmarks with human annotations, covering up to 47 language varieties and three evaluation formats: binary decisions, pairwise comparisons, and graded ratings. At approximately $1/31$ to $1/61$ of GPT-6.1's evaluation cost, Jev is competitive on most multilingual judging tasks, but falls behind GPT-6.1 on knowledge-intensive answer verification. Further analysis shows that Jev is more likely to accept incorrect answers in low-resource languages than in English and that its probability outputs help identify errors across tasks. Based on these findings, we offer recommendations on evaluation instructions, confidence-based selection, and model routing, providing empirical guidance for using Jev as a multilingual judge.

**Key findings**

- **Finding**: 在 MEMERAG、Global-MMLU-Lite、MENLO、METAL 四个基准共 43,484 个样本上，Jev 每千样本成本 $0.026–$0.082，是 GPT-6.1（$0.820–$5.010）的 1/31–1/61、总花费 $2.64 对 $97.45；但 Global-MMLU-Lite 答案核验的 BAcc 只有 89.6，比 GPT-6.1 的 96.1 低 6.5 个百分点。
- **Inference**: 跨语言一致性退化集中在低资源语言——约 78% 的分歧差距来自 Jev 新引入的错误接受（低资源语言 8.25 个百分点，而 GPT-6.1 仅 1.03），且其置信度只在二元判定上可靠（AUROC 0.839），在分级评分上已接近随机（0.550）。
- **Recommendation**: 默认用英文写评审指令（翻译后输入 token 反增 13.5%–38.6% 而准确率无提升），二元判定用置信度阈值筛选保留样本（阈值 ≥0.95 时准确率 99.18%、覆盖率降至 28%），并把低置信样本路由给 GPT-6.1（89.57% 提升到 92.73%）。

**Key figures**

*Framework - Agreement with English judgments across 22 non-English languages in Global-MMLU-Lite. Outer bands indicate high-, mid-, and low-resource language groups defined in the dataset (Singh et al.,*

![Is Jev a Good Multilingual Judge? - framework](res/2611.14861_framework.png)

*Result - Changes in judgments from English to other languages on Global-MMLU-Lite. False acceptances and false rejections are newly introduced errors, while their corrected counterparts are English e*

![Is Jev a Good Multilingual Judge? - result](res/2611.14861_result.png)

**Why this ranks #20**: rel 7 / qual 8，总分 7.3 排本方向第三。在 4 个多语基准、最多 47 个语言变体、共 43,484 个样本上，Jev 每千样本成本仅 $0.026–$0.082，是 GPT-6.1（$0.820–$5.010）的 1/31 到 1/61；但知识密集的答案核验 BAcc 89.6 比 GPT-6.1 的 96.1 低 6.5 个百分点，且低资源语言误接受更多，属成本换准确率的务实权衡。

---

## Footer

- Total papers reviewed across all 4 axes: 60
- llm_vlm axis final count: 20
- Wild-cards in this axis: 0
- Figure assets: 2026-11-13/res/

Generated by `mine-arxiv-daily-digest` skill. Sister file: `2026-11-13_llm_vlm_entry.md`.
