# Mine Arxiv Daily Digest - 2026-11-09 (LLM / VLM 与其强化学习 Axis, 20 papers)

**Generated**: 2026-11-09 17:30 CST

**Source**: arXiv cs.CV, cs.SD, eess.AS, cs.CL, cs.AI, cs.RO, cs.LG, cs.IR submissions, listing day 2026-11-06 (announced 2026-11-09 00:00 UTC)

**Batch window**: 2026-11-05T19:00:00Z .. 2026-11-06T19:00:00Z（arXiv 公告批次横跨两个 UTC 日：从前一日的美东 14:00 截止时刻起算（EDT 为 18:00Z，EST 为 19:00Z），到当日的同一时刻为止）

**Axis**: llm_vlm (20 papers, base 18, cap 20)

**Directions**: llm_core (9), vlm_core (5), llm_vlm_rl (6)

**Selection**: 20 papers ranked by relevance x quality, with 0 wild-card slots

**Day total**: 60 papers across 4 axes (target 60)

**Scope**: 大语言模型与视觉语言模型的设计、推理、agent、效率与上下文工作，以及面向 LLM / VLM 的 RL 与偏好优化、奖励模型

**Wild-card**: 0（本 axis 本批次够格供给充足，未启用补位名额）

---

## LLM 核心（架构 / 推理 / agent / 效率 / 上下文） · `llm_core` (9 papers)

本方向 9 篇，集中在一件事上：**LLM 的推理成本结构**。MoE 负载均衡被重写成反馈控制问题（PID-Balancer 家族，把辅助均衡损失与路由器解耦归到同一族）；Transformer-FSQ 用有限标量量化瓶颈替换 K/V 投影，把 KV 缓存压到极端比例（Qwen3-1.7B 在 20 万条上下文下原本要 21 GiB，是权重的 6.6 倍）；FOSCAR 用仿射折叠把 2/4-bit KV 解码的 scale-offset 操作减少最多两个数量级；Attend at the Right Resolution 让每个注意力头按自身 query-key 响应结构自选稀疏分辨率；MINE 用 dtANS 无损熵编码加速单流推理；QGPM 用模型自己的注意力相关度在 RoPE 层重排位置缓解「中间遗忘」；Intent-Aware Caching 把用户意图当作前缀缓存命中率的信号；Parallel Agent Teams 让「并行采样小团队再择优」在 12 个长程任务上同时超过 Best-of-N 与单个大队；RPEG 则把推理语言模型的 RL 流水线本身当作可优化的数据结构。

### 1. Rethinking MoE Load Balancing as Feedback Control

**arXiv**: [2611.09252](https://arxiv.org/abs/2611.09252) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, moe, load-balancing, feedback-control, router, Umea University | **Categories**: cs.LG | **Pages**: 32

**Authors**: Yikun Hou; Alp Yurtsever

**Affiliation**: Umea University

**Abstract**

> Mixture-of-Experts (MoE) training is often not stationary: the data mixture changes at curriculum boundaries, when a model is continually pretrained into a new domain, or when the corpus is refreshed. Routing is learned against the current mixture, so each such change disrupts the per-expert load the router had converged to, and existing balancing methods have only been evaluated on stationary data. We rethink load balancing as a feedback control problem, in which the deviation of each expert's load from its fair share is the control error and the per-expert routing bias is the control input, and define a family of controllers, the PID-Balancer, from the proportional, integral, and derivative terms of classical PID control. Two widely used methods belong to this family: the auxiliary balancing loss behaves like a proportional controller, and the loss-free bias update is an integral controller acting on the sign of the error. Reading the router as a static map with a one-step delay, we show that the integral term is the only one that both removes persistent imbalance and averages out the step-to-step fluctuation of the measured load, whereas the proportional and derivative terms pass or amplify that fluctuation into the routing bias. We therefore adopt PID (I), the pure-integral member of the family with a single gain. Two settings are evaluated: (i) training an OLMoE backbone from scratch with 16 to 64 experts per layer, through a mid-run mixture switch, and (ii) continual pretraining of the released OLMoE-1B-7B on a new corpus. PID (I) holds balance before the shift and restores it more tightly afterwards than either the auxiliary loss or loss-free balancing, at comparable perplexity.

**Key findings**

- **Finding**: 表 1 显示 E=16、1→1 场景中 PID (I) 的 postMV 为 0.30±0.02，Aux-loss 为 0.80±0.03，Vanilla 高达 4.44，三者 PPL 分别为 3.32、3.31、3.29。
- **Inference**: 辅助平衡损失等价于比例控制器，会把每步负载抖动直接写进路由偏置，积分项先累积误差再以单一增益纠正，因此切换后能更紧地恢复均衡。
- **Recommendation**: 遇到课程边界或语料切换的 MoE 续训，直接用纯积分 PID 更新路由偏置，并同时监控 MaxVio 与困惑度，不要只调辅助损失权重。

**Key figures**

*Framework - Pre- and post-shift MaxVio for the three pre-shift scenarios of Section 4.1. The circle marks the transition from the pre-shift steady state (preMV) to the post-shift steady state (postMV).*

![Rethinking MoE Load Balancing as Feedback Control - framework](res/2611.09252_framework.png)

*Result - MaxVio over training (E = 64, 1 →1 scenario, 6-seed mean, 51-step smoothing). Shading marks the 2,000-step windows averaged for PreMV and PostMV.*

![Rethinking MoE Load Balancing as Feedback Control - result](res/2611.09252_result.png)

**Why this ranks #1**: 把 MoE 负载均衡重述为 PID 反馈控制问题，证明只有积分项能同时消除持续不均衡与逐步抖动；在 E=16 的 1→1 混合切换场景下 PID (I) 的 postMV 为 0.30，优于辅助损失的 0.80，而困惑度 3.32 与 3.31 基本持平。

---

### 2. Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression

**arXiv**: [2611.09598](https://arxiv.org/abs/2611.09598) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, kv-cache, quantization, compression, long-context, University of Edinburgh | **Categories**: cs.LG | **Pages**: 42

**Authors**: Andras Szecsenyi; Thomas L. Lee; Vaisakh Shaj; Elliot J. Crowley; Amos Storkey

**Affiliation**: University of Edinburgh

**Abstract**

> Private, personalised language models must run on local consumer devices, where large, frontier models cannot fit, and retaining long contexts is non-trivial. Sequential memory---the key-value (KV) cache---grows linearly with context length, quickly dwarfing the model itself: for Qwen3-1.7B-Base, 200,000 retained entries require 21 GiB, 6.6 times more than the model weights. Yet the KV-cache compression methods we measured fail beyond moderate compression ratios. We introduce Transformer-FSQ, addressing extreme KV-cache compression by replacing standard key and value projections with a finite scalar quantisation bottleneck. Our cache stores a packed vector of discrete integer codes per token, with no per-token quantisation metadata. Converting a pretrained transformer trains only these projections on 0.25 tokens per original parameter. We evaluate Transformer-FSQ against five baseline families on models from 0.6B to 8B parameters. On long-context retrieval (RULER), from 12$\times$ to 97.5$\times$ Transformer-FSQ is the most accurate method we evaluate, across scales. A fused Triton kernel decodes directly from the integer codes; with baselines given their authors' kernels where available, it decodes at $1.01\times$ (95% interval $0.98$--$1.05$) the throughput of native SDPA attention on the uncompressed Qwen3-8B-Base at $32\times$ and $1.54\times$ at $97.5\times$. Extreme KV-cache compression is therefore a practical way to extend how much context a fixed device can hold.

**Key findings**

- **Finding**: Qwen3-1.7B-Base 保留 20 万条 KV 需要 21 GiB，是模型权重的 6.6 倍；Transformer-FSQ 在 RULER 上从 12× 到 97.5× 压缩比区间均为所测方法中最准确者。
- **Inference**: 打包的离散整数码去掉逐 token 量化元数据后，压缩比得以突破中等比率的失效拐点；Triton 内核直接从整数码解码，无需先反量化成浮点再算。
- **Recommendation**: 需要在本地设备保留超长上下文时，优先试有限标量量化加打包整数码方案，并在自己的任务上同时核对 RULER 精度与解码吞吐两个指标。

**Key figures**

*Framework - KV-cache capacity on a 16 GiB GPU. With ≈0.74 GiB left for cache after Qwen3-8B model weights, extreme com- pression (256×) expands token capacity from 5.4k to 1.39M, en- abling million-toke*

![Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression - framework](res/2611.09598_framework.png)

*Result - RULER at 8,192 tokens against achieved compression on Qwen3-0.6B, 1.7B and 8B. Solid: finetuned; dashed: training-free; grey horizontal line: uncompressed. Points average up to three seeds (*

![Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression - result](res/2611.09598_result.png)

**Why this ranks #2**: 用有限标量量化瓶颈替代常规 K/V 投影做极端 KV 压缩，RULER 上从 12× 到 97.5× 区间都是评测中最准的方法，97.5× 压缩下解码吞吐达原生 SDPA 的 1.54×，且每 token 不再存量化元数据。

---

### 3. Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure

**arXiv**: [2611.09700](https://arxiv.org/abs/2611.09700) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, sparse-attention, long-context, training-free, attention, University of Houston | **Categories**: cs.AI | **Pages**: 18

**Authors**: Wajih Hassan Raza; Ahsan Bilal; Yidan Shen; Renjie Hu; Xin Fu; Yu Wen

**Affiliation**: University of Houston; University of Oklahoma

**Abstract**

> Attention is a major scalability bottleneck in large language models (LLMs), with its computational cost and key-value (KV) memory traffic becoming increasingly prohibitive as context length grows. Sparse attention addresses this bottleneck by restricting each query to a subset of the context, but its effectiveness hinges on identifying relevant regions both cheaply and reliably. Existing training-free methods primarily rely on runtime relevance estimates, with selection dimensionality and granularity typically governed by fixed heuristics rather than the intrinsic interaction structure of pretrained attention heads. We take a different perspective: the query-key operator of each pretrained head defines a characteristic response structure that determines the resolution needed for sparse selection, both across feature directions and across context tokens. Building on this insight, we propose Head-Adaptive Sparse Attention (HASA), a training-free sparse attention framework that jointly adapts selection resolution along these two dimensions. Along the feature dimension, the singular spectrum of each head's query-key operator determines an effective rank, yielding a compact, head-specific response space. Along the sequence dimension, neighboring regions are progressively merged according to the directional coherence of their token responses in this same space, while heterogeneous regions remain separate. Exact attention is then computed using the original full-dimensional KV states of the selected regions. HASA captures 88.1% of dense-attention mass and, compared with UNIQUE, a strong recent sparse-attention baseline, improves accuracy by up to 3.47 and 2.57 points on RULER and LongBench-Pro, respectively, and accelerates self-attention by up to 1.32x, while achieving up to 14.07x speedup over dense attention.

**Key findings**

- **Finding**: HASA 在无需训练的前提下捕获稠密注意力的 88.1% 注意力质量；对比 UNIQUE，RULER 上最多提升 3.47 分、LongBench-Pro 上最多提升 2.57 分，自注意力加速 1.32×，相对稠密注意力最高 14.07×。
- **Inference**: 稀疏选择的粒度本应由各头自身的 query-key 响应结构决定，而非固定启发式，因此按奇异谱定有效秩、按方向一致性合并相邻区域可在几乎不损精度下大幅省算力。
- **Recommendation**: 替换现有训练无关稀疏注意力时，先离线测各头 query-key 算子的奇异谱衰减，用它设定特征维度秩与区域合并粒度，再对 RULER 与业务长文做同预算对比。

**Key figures**

*Framework - Motivation for HASA. Coarse-grained selection risks missing relevant tokens, while fine- grained selection increases selection overhead. HASA adapts selection granularity for each head.*

![Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure - framework](res/2611.09700_framework.png)

*Result - Overview of HASA. (1) Each head’s pretrained query–key interaction structure deter- mines its effective rank, yielding a compact head-specific response space. (2) In this compact re- sponse*

![Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure - result](res/2611.09700_result.png)

**Why this ranks #3**: 提出免训练的头自适应稀疏注意力 HASA，用每个注意力头 query-key 算子的奇异谱决定特征维度分辨率，捕获 88.1% 的稠密注意力质量，相对 UNIQUE 在 RULER 与 LongBench-Pro 上分别提升 3.47 与 2.57 分。

---

### 4. FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding

**arXiv**: [2611.09722](https://arxiv.org/abs/2611.09722) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, kv-cache, quantization, gpu-kernel, decoding, Together AI | **Categories**: cs.AI | **Pages**: 16

**Authors**: Donglin Zhuang; Pragaash Ponnusamy; Xiaoxia Wu; Shuaiwen Leon Song; Zhongzhu Zhou

**Affiliation**: Together AI; University of Sydney

**Abstract**

> Large-language-model decode attention streams the key-value (KV) cache for every generated token. Packing that cache into 2-bit or 4-bit quantized integers reduces memory traffic but does not automatically translate into latency saving. Existing 2-bit fused kernels reach under 31%/15% of peak HBM throughput on H100/B200. Converting each value and applying its scale and offset before feeding Tensor Cores is a major bottleneck because instruction-issue throughput is scarce on modern GPUs. Instead of applying scale and offset to each KV value, FOSCAR uses affine folding to apply them to the other operand or the output of decode-attention matrix products, depending on the quantization scheme (token-wise or channel-wise). This reduces scale-and-offset operations by up to two orders of magnitude while preserving the dequantized attention output in exact arithmetic. FOSCAR also uses bit manipulation to feed KV operands to Tensor Cores efficiently, requiring only 1 and 0.19 ALU instructions per INT2 element on H100 and B200, respectively. Finally, FOSCAR builds warp-specialized GPU pipelines for Hopper (H100) and Blackwell (B200) using wgmma and tcgen05. On H100, FOSCAR INT2 and INT4 kernels achieve geo-mean speedups of $3.36\times$ and $2.83\times$ over FlashInfer BF16, and $2.03\times$ and $1.71\times$ over TensorRT-LLM FP8. On B200, the corresponding INT2 and INT4 speedups are $2.67\times$ and $2.30\times$ over FlashInfer BF16, $1.48\times$ and $1.28\times$ over TensorRT-LLM FP8, and $1.16\times$ and $1.00\times$ over TensorRT-LLM NVFP4. We integrate FOSCAR into SGLang to benchmark serving efficiency. On long-context serving workloads, FOSCAR increases peak aggregate throughput by up to 170% and 341% over 2-bit and 16-bit baselines, respectively. We open-source FOSCAR as a kernel library at https://github.com/FutureMLS-Lab/FOSCAR.

**Key findings**

- **Finding**: 现有 2 位融合内核在 H100/B200 上只达到峰值 HBM 吞吐的 31% 以下与 15% 以下；FOSCAR 用仿射折叠把 scale/offset 操作减少最多两个数量级，每个 INT2 元素仅需 1 条（H100）与 0.19 条（B200）ALU 指令。
- **Inference**: 低比特解码的瓶颈已从显存带宽转向指令发射吞吐，把反量化常量折叠进矩阵乘的另一侧比原地反量化更划算，H100 上 INT2/INT4 相对 FlashInfer BF16 分别加速 3.36× 与 2.83×。
- **Recommendation**: 做低比特 KV 部署时按量化粒度（token-wise 或 channel-wise）选择折叠位置，并在 H100 与 B200 上分别测每字节指令数，而不要只看显存占用。

**Key figures**

*Framework - Effective KV access throughput of baseline kernels and*

![FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding - framework](res/2611.09722_framework.png)

*Result - GPU throughput scaling and per-byte instruction-issue*

![FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding - result](res/2611.09722_result.png)

**Why this ranks #4**: 针对 2/4 位 KV cache 解码时逐元素施加 scale/offset 的指令瓶颈，用仿射折叠把量化常量挪到另一操作数或输出上，H100 上 INT2 相对 FlashInfer BF16 取得 3.36× 几何平均加速，长上下文服务吞吐最高提升 170%。

---

### 5. Intent-Aware Caching for Efficient LLM Serving

**arXiv**: [2611.09715](https://arxiv.org/abs/2611.09715) | **Score**: 8.3 (relevance 8 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, prefix-caching, serving, kv-cache, latency, Virginia Tech | **Categories**: cs.AI, cs.LG | **Pages**: 25

**Authors**: Kazi Hasan Ibn Arif; JinYi Yoon; Dimitrios S. Nikolopoulos; Hans Vandierendonck; Deepu John; Bo Ji

**Affiliation**: Virginia Tech; Inha University; Queen's University Belfast; University College Dublin

**Abstract**

> Modern LLM serving systems use prefix caching to accelerate multi-turn conversational workloads. They cache the key-value states of previous conversation prefixes and reuse them when subsequent requests share the same prefix, to avoid redundant prefill computation and reduce serving latency. However, achieving a high cache hit rate remains challenging because cache reuse depends on whether a conversation continues and how soon the next turn arrives. Our analysis of real workloads shows that user intent is a useful signal for this behavior, as different intents exhibit different continuation probabilities and inter-turn delays. Based on this key insight, we propose Intent-Aware Caching (IAC), an online eviction policy that classifies requests by intent, learns lightweight reuse statistics from recent serving logs and leverages these statistics to guide an oracle-inspired eviction strategy. Extensive evaluation on real workloads (WildChat and ShareChat) shows that IAC reaches a 34.6% cache hit rate. This substantially outperforms both the previous learning-based approach (18.8%) and traditional methods such as least recently used (LRU, 12.2%), while reducing average serving latency by up to 46.1%.

**Key findings**

- **Finding**: 在 WildChat 与 ShareChat 真实负载上，IAC 的缓存命中率达 34.6%，此前基于学习的方案为 18.8%，LRU 为 12.2%，同时把平均服务延迟最多降低 46.1%。
- **Inference**: 不同意图的会话延续概率与轮次间隔差异明显，而现有驱逐只看时间局部性、忽略语义上的未来复用，按意图学习复用统计因此能优于纯时间启发式。
- **Recommendation**: 部署多轮对话服务时按意图分类请求、为每类维护复用率与延迟统计并用其驱动驱逐，上线前用真实日志回放对比 LRU 命中率与尾延迟。

**Why this ranks #5**: 把用户意图当作前缀缓存命中率的先验信号，在 WildChat 与 ShareChat 真实负载上把命中率推到 34.6%，显著高于此前学习类方法的 18.8% 与 LRU 的 12.2%，并把平均服务延迟最多降低 46.1%。

---

### 6. Test-Time Compute Scales Better with Parallel Agent Teams

**arXiv**: [2611.09798](https://arxiv.org/abs/2611.09798) | **Score**: 8.3 (relevance 8 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, test-time-compute, multi-agent, verifier, scaling, Duke University | **Categories**: cs.AI | **Pages**: 29

**Authors**: Junlin Wang; Haozhe Chen; Ang Li; Rahul Chalamala; Zhuang Liu

**Affiliation**: Duke University; Princeton University; New York University

**Abstract**

> Test-time scaling improves the performance of a fixed model by spending more computation at inference. There are two common ways to spend it on agents when a verifier can score every attempt. Best-of-N sampling runs many independent agents and keeps the best result but saturates quickly. One large team of collaborating agents can score higher but stops improving as it grows. Can we get the best of both? Our method, parallel agent teams, does so by sampling many small teams in parallel and keeping the best team's result. We test it on 12 long-horizon tasks from GPU kernels and formal proofs to exploit development. With a 27B model and a budget of 100 agents, parallel teams of ten beat parallel agents on 10 of 12 tasks and beat one team of 100 on all four tasks where we ran such large teams. At equal dollar cost the same parallel teams beat a frontier model on half the tasks. A simple statistical model shows that individual agents lose because their many samples have a low mean and that one large team loses because a single sample gets no gain from variance. Sampling many small teams in parallel balances a high mean with the gain from variance. Parallel agent teams thus offer a more effective way to scale test-time compute.

**Key findings**

- **Finding**: Qwen3.8-27B 在 100 个 agent 的预算下，10 人并行团队在 12 个任务中的 10 个上超过并行 agent，并在跑过单个 100 人团队的 4 个任务上全部取胜；同等美元成本下在半数任务上胜过前沿模型。
- **Inference**: 并行单 agent 的样本均值偏低、方差收益被平均掉，单一大团队则只有一个样本、得不到方差收益，采样多个小团队才能兼得高均值与方差收益。
- **Recommendation**: 有验证器能给每次尝试打分的场景，优先并行采样多个小规模协作团队再取最优，而不是一个大队或一堆独立 agent，并按等成本而非等 agent 数做对比。

**Key figures**

*Framework - Sample small teams, not agents or one big team. (a) Three ways to spend the same agents. A verifier keeps the best solution. (b) Qwen3.8-27B on four tasks. Parallel agents (blue) flatten quic*

![Test-Time Compute Scales Better with Parallel Agent Teams - framework](res/2611.09798_framework.png)

*Result - Parallel teams beat parallel agents on 10 of 12 tasks at 100 agents. Qwen3.8-27B parallel agents (blue) and parallel teams of ten (orange). Brackets give the teams’ gain at the largest budget*

![Test-Time Compute Scales Better with Parallel Agent Teams - result](res/2611.09798_result.png)

**Why this ranks #6**: 把测试时计算扩展做成并行 agent 团队：27B 模型、100 个 agent 预算下，10 人小队在 12 个长程任务中的 10 个上胜过并行单 agent，并在跑过 100 人大队的 4 个任务上全面胜出，同等美元成本下半数任务打赢前沿模型。

---

### 7. RPEG: Training Reasoning Language Models Scalably and Cost-Effectively

**arXiv**: [2611.09207](https://arxiv.org/abs/2611.09207) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, training-infrastructure, rl-pipeline, graph-ir, distributed-training, ETH Zurich | **Categories**: cs.AI, cs.CL, cs.DC, cs.LG, cs.PF | **Pages**: 42

**Authors**: Maciej Besta; Leonard Schmidt; Pierre Pang; Patrik Okanovic; Robert Gerstenberger; Torsten Hoefler

**Affiliation**: ETH Zurich

**Abstract**

> Reinforcement learning (RL) is now central to training Reasoning Language Models (RLMs), but RLM pipelines are difficult to scale and costly to run because each RL step couples multiple large models, heterogeneous stages, cross-step state, and complex asynchronous dependencies. Existing systems typically optimize only parts of this design space. We address this complexity by jointly optimizing the pipeline structure as well as its execution using a novel data-centric graph intermediate representation called RLM Pipeline Execution Graph (RPEG). RPEG exposes structural choices such as bounded asynchrony and actor-critic sharing together with execution optimizations such as stage fusion, fine-grained scheduling, and multi-dimensional model parallelism. It is coupled with a comprehensive analytical performance model for RLM training, jointly capturing compute, communication, memory, and hierarchical rack-, node-, and GPU-level effects. Across systems with up to 256 GH200 GPUs, our distributed runtime engine implementing RPEG improves performance by up to 2x over ReaL and reduces step latency by up to 2.48x over verl, while increasing hardware utilization by up to 30%. Overall, RPEG provides a graph-driven foundation for next-generation training pipelines for frontier reasoning LLMs.

**Key findings**

- **Finding**: 实现 RPEG 的分布式运行时在最多 256 张 GH200 的系统上相对 ReaL 性能最高提升 2×，相对 verl 的步延迟最多降低 2.48×，硬件利用率最高提升 30%。
- **Inference**: RL 训练管线里结构选择（有界异步、actor-critic 共享）与执行优化（阶段融合、细粒度调度、多维并行）互为约束，先用图 IR 统一表达才能联合搜出更优排布。
- **Recommendation**: 自建 RLM 强化学习训练框架时把管线写成图 IR 再交给规划器搜索，并同时建模算力、通信、显存与机架-节点-GPU 三级层次效应，别只调单个子系统。

**Key figures**

*Framework - Representative PPO schedules selected by different planners. RPEG exposes stage-level and fine-grained overlap, enabling disaggregated placements and bounded-asynchrony that are not available*

![RPEG: Training Reasoning Language Models Scalably and Cost-Effectively - framework](res/2611.09207_framework.png)

*Result - Overview of the RPEG. A steady-state graph template and execution plan are unrolled, lowered to an executable DAG with explicit communication and resharding, evaluated with local analytical co*

![RPEG: Training Reasoning Language Models Scalably and Cost-Effectively - result](res/2611.09207_result.png)

**Why this ranks #7**: 为推理语言模型的 RL 训练提出数据中心的执行图中间表示 RPEG，在最多 256 张 GH200 上比 ReaL 性能最高提升 2×、比 verl 降低步延迟最多 2.48×，硬件利用率最高增加 30%，把结构选择与执行优化统一进一张图。

---

### 8. MINE: Entropy-coded Memory-efficient Inference for Large Language Models

**arXiv**: [2611.09424](https://arxiv.org/abs/2611.09424) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, inference-efficiency, entropy-coding, quantization, memory-bandwidth, ETH Zurich | **Categories**: cs.DC, cs.LG, cs.PF | **Pages**: 20

**Authors**: Emil Schätzle; Markus Püschel

**Affiliation**: ETH Zurich

**Abstract**

> We present MINE (Memory-efficient INference Engine), a lossless entropy coding approach that accelerates single-stream inference of Large Language Models (LLMs), where existing lossless compression methods yield speedups only for specific data types such as \texttt{BF16} and under additional assumptions. Single-stream decoding is strongly memory-bound, since every weight must be streamed from memory once per generated token and requests cannot be batched in local or low-latency deployments. At the core of MINE is dtANS-LLM, a GPU entropy coding scheme adapted from the prior dtANS to the needs of LLM inference. It exploits the non-uniform distribution of weights, which persists even after quantization, and exposes hyper-parameters that trade compression ratio against decoding cost. We auto-tune these parameters for each tensor and GPU to obtain the Pareto front between model size and decoding latency. MINE integrates into vLLM as a plugin and selects the best kernel configuration for a given memory budget. On Llama~3.1~8B~Instruct with a 2.1-bit EntQuant checkpoint, MINE achieves speedups of 2.52$\times$ and 1.48$\times$ over the fastest baseline on an RTX~4060~Ti and an RTX~5090, at effective bitrates of 2.24 and 3.43~bits per weight. MINE is available as open source.

**Key findings**

- **Finding**: 在 Llama 3.1 8B Instruct 的 2.1 位 EntQuant 检查点上，MINE 相对最快基线在 RTX 4060 Ti 与 RTX 5090 上分别加速 2.52× 与 1.48×，对应有效码率 2.24 与 3.43 bit/权重。
- **Inference**: 量化后权重分布仍然高度非均匀，熵编码能在保留无损性的同时进一步压低每次解码需从显存搬运的字节数，而单流部署无法靠批处理摊薄这条带宽路径。
- **Recommendation**: 显存受限的单流或低延迟部署上，把量化检查点与熵编码内核组合使用，并为每个张量与 GPU 自动调压缩率-解码延迟的 Pareto 前沿，而不是沿用固定全局码率。

**Key figures**

*Framework - Overview of MINE. Left: tuning, done once for a given checkpoint and GPU; right: inference with the MINE plugin in vLLM.*

![MINE: Entropy-coded Memory-efficient Inference for Large Language Models - framework](res/2611.09424_framework.png)

*Result - Overview of the performance-critical mvm kernel. Compressed data is fetched and decoded into weights which are used in place for fused matrix-vector multiplication with activations.*

![MINE: Entropy-coded Memory-efficient Inference for Large Language Models - result](res/2611.09424_result.png)

**Why this ranks #8**: 针对单流解码受显存带宽约束的问题，提出基于 dtANS 的无损熵编码内核 dtANS-LLM，在 Llama 3.1 8B Instruct 的 2.1 位 EntQuant 检查点上相对最快基线在 RTX 4060 Ti 与 RTX 5090 上分别加速 2.52× 与 1.48×。

---

### 9. Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs

**arXiv**: [2611.09554](https://arxiv.org/abs/2611.09554) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, long-context, rope, lost-in-the-middle, training-free, USC | **Categories**: cs.AI, cs.CL, cs.LG | **Pages**: 13

**Authors**: Peiyu Zhang; Heng Ping; Shinibali Bhattacharyya; Anwesan Pal; Nikos Kanakaris; Kevin Cheang; Shixuan Li; Wei Yang; Paul Bogdan

**Affiliation**: USC; Amazon Web Services

**Abstract**

> Long-context language models often neglect information in the middle of the input, a phenomenon known as "lost-in-the-middle". Part of this gap may stem from the long-range decay of rotary position embedding (RoPE), which weakens the positional signal between distant tokens. Existing input compression deletes low-importance tokens, and attention reweighting acts only after RoPE has weakened this signal. RoPE-level methods modify positions directly but apply the same remapping to every query. To address these limitations, we propose QGPM (Query-Guided Positional Modulation), a training-free method that reshapes RoPE positions using query relevance from the model's own attention heads. QGPM builds a broad relevance map for lower layers and a sharp one for upper layers. Low-relevance tokens advance by less than one position on fast-rotating planes, pulling relevant evidence toward the query. Slow-rotating planes keep the original layout, with every token in place. Experiments on NoLiMa and RULER with multiple context lengths show that QGPM improves over base models and strong baselines, with the largest gains on retrieval tasks, and generalizes across multiple backbones. Our code is available at https://github.com/iZHpy/QGPM.

**Key findings**

- **Finding**: QGPM 在四个 backbone 的五任务平均分上均为最优，相对 Vanilla 提升 2.4 至 8.9 分；NoLiMa 上相对 Vanilla 的平均增益为 9.0 至 17.6 分，Granite 的 NIAH-MK 从 66.0 提到 85.1，96 个设置中至少赢 71 个。
- **Inference**: 位置衰减不是输入压缩或注意力重加权能补的，因为 RoPE 信号在注意力之前就已弱化；按 query 相关度重排位置能针对每个查询定制证据位置，而不是对所有查询用同一套重映射。
- **Recommendation**: 遇到长上下文中间信息丢失，先在检索型任务（NoLiMa/NIAH）上验证位置类免训练方法，同时注意 QA 类任务基本持平，别用平均分掩盖 QA 上的小幅回退。

**Key figures**

*Framework - Overview of QGPM. (a) A plain prefill reads the attention from the query to each context sentence in a few selected heads. The fused sentence ranking is shaped into a broad relevance map and*

![Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs - framework](res/2611.09554_framework.png)

*Result - Accuracy (%) of all five tasks at each context length. Gray lines show LLMLingua-2, Ms-PoE, and Self- Extend. The shaded region marks 64K for Ministral-8B, which exceeds the configured windo*

![Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs - result](res/2611.09554_result.png)

**Why this ranks #9**: 用模型自身注意力头的 query 相关度直接重塑 RoPE 位置，低相关 token 在快旋转平面上前进不足一个位置，免训练即在 NoLiMa 与 RULER 上把五任务平均分相对基座提升 2.4 至 8.9 分，96 个设置中至少赢 71 个。

---

## VLM 核心（多模态架构 / 理解 / 视频 / GUI agent） · `vlm_core` (5 papers)

本方向 5 篇，关心的是**多模态模型在「看」与「算」之间到底卡在哪**。Seeing vs. Counting 用「复杂度孪生」把同一张图上属于不同计数复杂度类的问题配对，再用转写探针和纯文本对照把读图与计算拆开，发现失败率更多由答案规模而非复杂度类决定；AtariBench 在 20 款 Atari 2600 游戏上把高速游戏动态与推理墙钟速度解耦，暴露主流 VLM 难以推断物体运动方向、序列决策脆弱；AdaAlloc 把长视频问答重述为视觉 token 分配问题，在固定预算下自适应分配全局概览与局部细节；Active VLM-TTA 探索「标注预算可用但当前样本必须先出结果」的部署中间态；Decoupled Mode Connectivity 则用两个 prompt 分别承接特化与泛化两个互相冲突的目标。

### 10. AtariBench: Evaluating Spatiotemporal Reasoning of Vision-Language Models in Atari Gameplay

**arXiv**: [2611.08755](https://arxiv.org/abs/2611.08755) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, vlm-evaluation, spatiotemporal-reasoning, atari, interactive-agent, UC San Diego | **Categories**: cs.AI, cs.CV | **Pages**: 26

**Authors**: Mingjia Huo; Yao Fu; Bo Chang; Yaqing Wang; Dawei Zhu; Dylan Zhang; Xinyang Yi; Lichan Hong; Ed H. Chi; Hao Zhang; Jiaxi Tang

**Affiliation**: UC San Diego; Google DeepMind; Peking University; UIUC

**Abstract**

> Vision-Language Models (VLMs) have achieved strong performance on static visual understanding benchmarks, yet their ability to act in dynamic environments remains less well understood. We introduce AtariBench, a controlled benchmark that evaluates VLMs across 20 Atari 2600 games, requiring models to make sequential decisions from high-temporal-resolution gameplay streams. By decoupling fast in-game dynamics from wall-clock inference speed, AtariBench focuses on whether models can perceive rapid visual state changes, reason over spatiotemporal dynamics, and ground actions in the current observation. Our experiments reveal substantial limitations in state-of-the-art VLMs: models often fail to infer object motion and direction, exhibit brittle sequential decision-making, and over-rely on textual interaction history despite newly appended visual feedback. We further introduce a separability analysis to identify which in-game scores provide reliable signals of model competence, and use the benchmark to study how memory design and prompting strategies affect performance. Overall, AtariBench exposes a persistent gap between passive visual perception and active decision-making, providing a lightweight and rigorous testbed for developing VLMs that can reason and act in dynamic environments.

**Key findings**

- **Finding**: AtariBench 覆盖 20 个 Atari 2600 游戏，每个模型设置跑 10 次 30 秒闭环回合（ALE 种子 0-9、禁用 sticky actions），对比 Gemini 3.1 Pro/3 Flash/2.5 Flash、GPT-5.4 与 Mini、Claude Opus 4.6 与 Sonnet 4.6、DeepSeek V3.1 和 GLM 5.1。
- **Inference**: 把游戏内时间与推理时间解耦后，随机动作基线稳定垫底而最强模型居前，说明分数差距来自真实视觉控制而非任意采样；模型普遍读不出物体运动方向并过度依赖文本交互历史。
- **Recommendation**: 评估 VLM 的动态环境能力时用这类高时间分辨率闭环基准，并单独检查运动方向判断与文本历史依赖，不要用静态视觉理解分数代替行动能力。

**Key figures**

*Framework - Workﬂow of AtariBench. At each turn, the harness assembles game instructions, interac- tion history, and the current frame into a prompt; the VLM returns a thought and an action sequence, wh*

![AtariBench: Evaluating Spatiotemporal Reasoning of Vision-Language Models in Atari Gameplay - framework](res/2611.08755_framework.png)

*Result - Fast temporal dynamics in Assault. The enemy projectile appears at t = 0.1s and already hits the player at t = 0.3s, motivating high tempo- ral resolution and 10 Hz control.*

![AtariBench: Evaluating Spatiotemporal Reasoning of Vision-Language Models in Atari Gameplay - result](res/2611.08755_result.png)

**Why this ranks #10**: 在 20 个 Atari 2600 游戏上用 10 次 30 秒闭环回合评测 Gemini 3.1 Pro、GPT-5.4、Claude Opus 4.6 等 VLM，把游戏内快动态与推理墙钟时间解耦，暴露出模型推断物体运动方向与序列决策的普遍短板。

---

### 11. Seeing vs. Counting: Complexity Twins Show Where Multimodal LLMs Fail on Diagrams

**arXiv**: [2611.08998](https://arxiv.org/abs/2611.08998) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, diagram-understanding, counting, mllm-evaluation, failure-analysis, Google | **Categories**: cs.AI, cs.CL, cs.CV | **Pages**: 107

**Authors**: Yin Liu

**Affiliation**: Google

**Abstract**

> When a multimodal LLM miscounts in a diagram, does it fail at seeing or at counting? Existing visual graph and puzzle benchmarks vary visual density and algorithmic hardness together, confounding the two. We pair counting questions about the same drawing that sit in different counting-complexity classes, such as its spanning trees (a determinant) and its simple paths (#P-complete), and use a transcription probe and a text-only control to separate reading from computing. We test Gemini, Gemma and Qwen3-VL models; for the Gemini models, the answer depends on how the model computes. In chain of thought, most of them read small drawings correctly and then fail at counting, at a rate set far more by the size of the answer than by its complexity class (for the primary model, the odds of an exact answer fall 2.38-fold per decade of the answer). Given code and an exact transcription, the primary model counts correctly even on 10x10 grids, and reading becomes the bottleneck: a single view misses horizontal edges, and a second reading of a rotated copy with crop checks reads 86/96 large grids exactly, against 57/96 when the upright reading is simply repeated.

**Key findings**

- **Finding**: 主模型在思维链下每过一个数量级的答案，精确答对几率下降 2.38 倍；给定代码与精确转写后主模型在 10×10 网格上也能数对，但换一次读取角度并做裁剪校验时大图读对 86/96，重复同一视角只有 57/96。
- **Inference**: 多数数错其实是看错，读图精度而非计数复杂度主导失败率；转写探针与纯文本对照能把两类错误分离，说明基准把视觉密度与算法难度混在一起会误导归因。
- **Recommendation**: 评测图表图形类多模态模型时同时给转写探针与二次不同视角读取，分别报告读图准确率与计算准确率，别用单一答案准确率下结论。

**Key figures**

*Framework - One image, two questions. (a) On this 4×5 drawing #ST (GapL, one determinant) is 324,268 and #Paths from vertex 0 to vertex 19 (#P-complete) is 200: the harder question has the smaller answe*

![Seeing vs. Counting: Complexity Twins Show Where Multimodal LLMs Fail on Diagrams - framework](res/2611.08998_framework.png)

**Why this ranks #11**: 用同一张图上复杂度不同的成对计数问题（生成树行列式与简单路径 #P-complete）把看错与算错分开，发现答案每增一个数量级命中概率下降 2.38 倍，10×10 网格即使给了代码与精确转写也会读错。

---

### 12. Training-Free Active Test-Time Adaptation for Vision-Language Models

**arXiv**: [2611.09084](https://arxiv.org/abs/2611.09084) | **Score**: 8.3 (relevance 8 x 0.7 + quality 9 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, test-time-adaptation, active-learning, vlm-adaptation, training-free, KAIST | **Categories**: cs.AI, cs.CV | **Pages**: 28

**Authors**: Jihwan Bang; Sumyeong Ahn; Hwanjun Song; Jae-Gil Lee

**Affiliation**: KAIST

**Abstract**

> Test-time adaptation (TTA) for vision-language models (VLMs) is usually studied in a fully unsupervised regime, where adaptation relies on pseudo-labels, confidence scores, or entropy computed by the model itself. This is a severe restriction on hard shifted samples: the model is asked to repair its own uncertain predictions without any external evidence. At the other extreme, supervised online adaptation assumes labels can directly train or correct the model. We study the intermediate deployment regime between these two extremes. In Active Test-time Adaptation for VLMs (Active VLM-TTA), a pretrained VLM may spend an explicit labeling budget on selected test samples, but the prediction for the current sample must be emitted before its label can be used; queried labels are therefore costed, delayed evidence for future samples rather than free correction for the present one. Under this future-only constraint, the central question is how to reuse sparse labels conservatively. We instantiate this setting with ACTive VLM-TTA for Online Retrieval (ACTOR), a training-free plug-in module that routes uncertain samples among base prediction, label query, and memory-based correction using a consistency-and-reliability check over previously queried labels. Across ten cross-domain benchmarks and a domain-transfer benchmark based on ImageNet, ACTOR consistently improves strong VLM-TTA baselines on ResNet and ViT backbones with negligible inference overhead. Our implementation is publicly available at https://github.com/kaist-dmlab/ACTOR.

**Key findings**

- **Finding**: 在 ViT-B/16 上 ACTOR 把零样本 CLIP 从 61.94% 提到 70.67%、把 TDA 从 68.14% 提到 72.66%；在 15 个数据集上比 Online-CoOp 与 Replay-CoOp 分别高 2.50 与 2.45 个百分点，且额外推理开销不到 1 毫秒。
- **Inference**: 在当前样本必须先出预测、标签只能事后使用的约束下，复用稀疏标签必须同时看一致性与局部可靠性，加入该判据后有害纠正率从 13.68% 降到 5.28%。
- **Recommendation**: 部署带人工标注预算的 VLM 服务时采用 future-only 主动适配流程，并单独统计有害纠正率而非只看最终准确率，同时监控验证器数量增加带来的准确率回落。

**Key figures**

*Result - Active test-time adaptation for vision-language model (Active VLM-TTA). The model relies on a base VLM-TTA method for confident samples, while selectively querying labels for uncertain ones*

![Training-Free Active Test-Time Adaptation for Vision-Language Models - result](res/2611.09084_result.png)

**Why this ranks #12**: 提出介于纯无监督与有监督在线适配之间的主动测试时适配设定：标签只能用于未来样本，ACTOR 作为免训练插件在 10 个跨域与 5 个 OOD 基准上一致提升 CLIP 与 TDA，推理开销不到 1 毫秒。

---

### 13. AdaAlloc: Adaptive Visual Token Allocation for Long-Video Question Answering

**arXiv**: [2611.09092](https://arxiv.org/abs/2611.09092) | **Score**: 8.3 (relevance 8 x 0.7 + quality 9 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, long-video, video-qa, token-budget, temporal-grounding, UT Austin | **Categories**: cs.AI, cs.CV | **Pages**: 22

**Authors**: Joungbin An; Kristen Grauman

**Affiliation**: UT Austin

**Abstract**

> Long-video question answering forces multimodal large language models to reason under strict visual-token budgets, creating a tradeoff between broad temporal coverage and fine-grained spatial detail. Uniform sampling preserves coverage but often obscures decisive local cues, while caption-based or frame-similarity retrieval operates over lossy proxies that can miss motion, state changes, and before-after relations. We recast long-video reasoning as a visual-token allocation problem: given a fixed budget, decide how much to spend on global context versus high-resolution local evidence, and where in the video to draw that local evidence from. We introduce AdaAlloc, a training-free inference framework that adaptively allocates visual tokens between a global video overview and localized visual detail. AdaAlloc first plans a global/local allocation policy, then uses temporal grounding to locate candidate evidence segments and refines them into a compact temporal memory. The selected policy controls both frame sampling density and resolution, combining sparse, lower-resolution global frames with denser, higher-resolution local frames drawn from the refined memory. The final answerer reasons over the allocated global context and refined local evidence. Across LVBench, MLVU, VideoMME, and LongVideoBench, AdaAlloc improves over budget-matched uniform sampling by up to 10.5 percentage points and outperforms the compared frame-selection and agentic methods on their reported benchmarks.

**Key findings**

- **Finding**: 在相同 token 预算与 MLLM backbone 下，AdaAlloc 相对均匀采样最多提升 10.5 个百分点，在 VideoMME medium 子集上比 DIG 高 10.3 与 9.0 分；VideoLLaMA3-7B 在 32K 预算下四个基准平均 +2.25 分。
- **Inference**: 均匀采样用低分辨率换全覆盖、检索式方法用有损代理换局部细节，二者都受限于固定帧预算；先做全局局部预算规划再按时序定位取高分辨率局部帧，才能同时拿到覆盖与细节。
- **Recommendation**: 做长视频多模态模型时把 token 预算显式拆成全局低分辨率与局部高分辨率两路，并让拆分随查询变化，问句条件化的拆分在四个基准上额外带来 1.5 至 3.2 分提升。

**Key figures**

*Framework - Visual token allocation for long-video reasoning. Uniform sampling preserves global coverage but loses fine details, while retrieval-based selection focuses on a few clips but can lose conte*

![AdaAlloc: Adaptive Visual Token Allocation for Long-Video Question Answering - framework](res/2611.09092_framework.png)

*Result - AdaAlloc pipeline. AdaAlloc splits a fixed visual-token budget B between low-res global context (blue) and high-res local evidence (orange). (1) From a sparse overview O, an MLLM planner pic*

![AdaAlloc: Adaptive Visual Token Allocation for Long-Video Question Answering - result](res/2611.09092_result.png)

**Why this ranks #13**: 把长视频问答重述为视觉 token 分配问题，AdaAlloc 先规划全局与局部分配再用时序定位挑证据，在 LVBench、MLVU、VideoMME、LongVideoBench 上于同等 token 预算下比均匀采样最多高 10.5 个百分点。

---

### 14. Decoupled Mode Connectivity for Base-to-Novel Generalization in Vision-Language Models

**arXiv**: [2611.09655](https://arxiv.org/abs/2611.09655) | **Score**: 8.3 (relevance 8 x 0.7 + quality 9 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, prompt-learning, base-to-novel, mode-connectivity, generalization, Telecom Paris | **Categories**: cs.CV | **Pages**: 46

**Authors**: Imad Eddine Marouf; Khalid Oublal; Enzo Tartaglione; Stéphane Lathuilière

**Affiliation**: Telecom Paris; Ecole Polytechnique; Inria / Univ. Grenoble Alpes

**Abstract**

> Prompt learning adapts vision-language models such as CLIP by optimizing a short learnable prompt. The cross-entropy objective pulls this prompt toward base-class specialization, whereas generalization to unseen classes benefits from staying close to CLIP's zero-shot feature space. Because both objectives act on the same prompt, their gradients conflict at convergence, and in our experiments no single-prompt loss design clearly improves on the cosine baseline. We propose Decoupled Mode Connectivity (DMC), which gives each objective its own prompt. Starting from a base-trained prompt, DMC trains a specialization prompt and a generalization prompt, and merges their text features with a fixed coefficient at test time, at the inference cost of a single prompt. A linear mode connectivity (LMC) corridor in text-feature space keeps the classification loss low for every classifier interpolated between the two endpoints, and a Visual Anchor KL term preserves CLIP's zero-shot class-similarity distribution of each image during specialization. We further argue that such regularizers should satisfy class-permutation invariance (CPI), and show via Fano's inequality, in an idealized model, that violating CPI lower-bounds the drop in novel accuracy by a term proportional to the mutual information between the prompt and the base-class labels. Across 11 datasets, DMC improves the average harmonic mean of base and novel accuracy over MergeTune for both CoOp and KgCoOp, and its interpolation curves pass beyond the single-prompt operating point, shifting the base-novel frontier rather than trading along it. Code is available at https://github.com/IemProg/DMC.

**Key findings**

- **Finding**: 11 个数据集上 DMC 的基类与新类平均调和平均相对 MergeTune 提升 +0.78（CoOp）与 +0.33（KgCoOp），分别在 11 个中的 9 个与 8 个上占优，插值曲线越过单提示工作点。
- **Inference**: 实验中没有任何单提示损失设计能稳定超过余弦基线，说明瓶颈是共享参数化结构而非正则项选择；把两个目标解耦到两个提示再插值，才能移动基类-新类前沿而非在其上权衡。
- **Recommendation**: 做 CLIP 提示学习时先做目标解耦，分别为特化与泛化训练提示、在文本特征空间用 LMC 走廊插值，并检查所用正则项是否满足类置换不变性。

**Key figures**

*Result - Empirical interpolation curves on Caltech101, SUN397, UCF101, and EuroSAT (CoOp base, 3-seed mean). Each curve traces the family of classifiers from fgen (α=0, near zero-shot) to fspec (α=1,*

![Decoupled Mode Connectivity for Base-to-Novel Generalization in Vision-Language Models - result](res/2611.09655_result.png)

**Why this ranks #14**: 指出 CLIP 提示学习中基类特化与新类泛化的梯度在同一提示上冲突，DMC 改为两个提示分别承载两个目标并在文本特征空间做模式连通插值，11 个数据集上相对 MergeTune 的调和平均提升 0.78 与 0.33。

---

## LLM / VLM 的 RL 与偏好优化 · `llm_vlm_rl` (6 papers)

本方向 6 篇，围绕「**奖励信号从哪来、怎么不失效**」展开。RuACT 指出群体相对优化下「所有样本都失败（不可达）或都通过（饱和）」的 rubric 不会给出任何学习信号——在 Qwen3-4B 医疗训练中有 60.88% 的 query-rubric 观测处于这种不活跃状态，于是让不可达 rubric 当特权教师、饱和 rubric 拆成子 rubric 当评论家；Monitor-Based Interventions 则正面处理「用监控器惩罚奖励黑客，模型却学会规避监控」这个反作用，开源了三个 Qwen3-4B 会奖励黑客的现实环境。RCEA 把 RLVR 里的全局 token 熵拆成轨迹级与 token 级、条件在验证结果上，回答「熵到底能不能诊断坍塌」；LambdaMix 用每个目标一个低秩适配器 + 偏好向量在线选择，一次训练支持推理期改偏好；PC-Dr.DPO 把测试时 RL 的多数票伪标签误差拆成群体多数偏置与有限 rollout 波动；AbCD 则完全不用标准答案，靠多智能体辩论自举出偏好数据。

### 15. RuACT: Recovering Inactive Rubrics as Adaptive Critics and Teachers

**arXiv**: [2611.09597](https://arxiv.org/abs/2611.09597) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, rubric-based-rl, group-relative-optimization, inactive-rubrics, self-distillation, verifiable-rewards, Zhejiang University | **Categories**: cs.CL | **Pages**: 22

**Authors**: Yijun Li; Zhengxi Lu; Zhipiao Liu; Jinzheng Yu; Xutao Weng; Jian Shao; Yongliang Shen

**Affiliation**: Zhejiang University; Huawei

**Abstract**

> Rubric-based reinforcement learning (RL) extends RL with verifiable rewards to open-ended tasks by scoring each response against query-specific rubrics. Under group-relative optimization, however, a rubric that every sampled response fails (unreachable) or passes (saturated) gives all responses the same outcome and no learning signal; in Qwen3-4B medical training, 60.88% of query-rubric observations are inactive. We find that the two states lack different supervision: stating an unreachable rubric in the prompt raises its satisfaction from 1.13% to 91.25%, whereas responses that all pass a saturated rubric still differ in quality. We therefore propose RuACT (Rubrics as Adaptive Critics and Teachers), which assigns each inactive rubric the role that supplies what it lacks. Rubric as Teacher uses unreachable rubrics as privileged information for reward-gated on-policy self-distillation, and Rubric as Critic decomposes saturated rubrics into child rubrics that separate current responses while sharing the parent's weight. RuACT outperforms GRPO, rubric reweighting, and rubric-guided exploration on all four medical and scientific benchmarks with Qwen3-4B and achieves the best average with Qwen3-1.7B. On initially unreachable rubrics, unguided recovery rises from 35.02% to 42.86%, while child refinement improves reward-quality alignment on independent rollouts from 57.74% to 60.77%. Code is available at https://github.com/ZJU-REAL/RuACT.

**Key findings**

- **Finding**: 122,768 条 query-rubric 观测中 60.88% 为 inactive（25.19% 不可达、35.69% 饱和）；把不可达 rubric 写进 prompt 可把其满足率从 1.13% 提到 91.25%，而饱和 rubric 的独立细粒度打分在 71% 的样本上仍能区分质量（不可达只有 29%）。
- **Inference**: 两种失活状态缺的是不同的监督——不可达缺的是行为本身，饱和缺的是组内区分度，所以任何形式的 rubric 重加权都无法恢复组内对比度，必须换角色而不是换权重。
- **Recommendation**: 用 rubric-based RL 时按组内通过率把 rubric 分成 unreachable / informative / saturated 三态，前者挂特权教师做奖励门控自蒸馏、后者拆子 rubric 并共享父级权重预算，别对全体 rubric 统一重加权。

**Key figures**

*Framework - Inactive rubrics and RuACT. (a) Illustration of unreachable, informative, and saturated rubrics and their distribution through training. (b) How RuACT re- covers inactive rubrics: reward-ver*

![RuACT: Recovering Inactive Rubrics as Adaptive Critics and Teachers - framework](res/2611.09597_framework.png)

*Result - Probes of inactive rubrics on frozen Qwen3-4B. (a) Fraction of initially unreachable rubrics satisfied by at least one of K independent ordinary sam- ples; shading denotes 95% confidence int*

![RuACT: Recovering Inactive Rubrics as Adaptive Critics and Teachers - result](res/2611.09597_result.png)

**Why this ranks #15**: 在 Qwen3-4B 的 RaR-Medicine 训练中，122,768 条 query-rubric 观测里有 60.88% 处于 inactive 状态（25.19% 不可达 + 35.69% 饱和），这些 rubric 的常量贡献在组内优势里完全抵消；RuACT 用 Teacher/Critic 双角色分别补回缺失的行为与缺失的对比度，是本方向当天空白点之一。

---

### 16. Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL

**arXiv**: [2611.09828](https://arxiv.org/abs/2611.09828) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, reward-hacking, monitor-evasion, rl-alignment, activation-probe, llm-judge, Google DeepMind | **Categories**: cs.LG | **Pages**: 40

**Authors**: Aria Wong; Joshua Engels; Neel Nanda

**Affiliation**: Google DeepMind

**Abstract**

> Reinforcement learning (RL) rewards are notoriously difficult to design and control, often leading to the model learning unintended behaviors such as reward hacking. One potential solution is to monitor for reward hacking and penalize it when detected; however, training against a monitor could lead to evasive behavior, and our general understanding of how to apply monitors effectively during training is limited. To study how best to use monitors to mitigate reward hacking, we introduce and open source three realistic environments where Qwen3-4B reward hacks: a coding environment hackable via test overwriting, a medical chat environment hackable via sycophancy, and a biography generation environment hackable via hallucination. We first focus on the coding environment, where we find that: (1) models can learn to evade highly accurate monitors by exploiting systemic flaws in probes and LLM judges; (2) monitors that leak more learning signal during RL suppress reward hacking but are more often evaded; and (3) including easier problems in training can decrease reward hacking. We apply our findings to build better reward hacking monitors for the medical chat and biography generation environments that improve upon naive baselines to reduce reward hacking rates across seeds to before-training levels in some interventions. Our results demonstrate that our takeaways translate to new settings and that better monitor intervention designs are possible.

**Key findings**

- **Finding**: 在 probe 惩罚下训练的 Qwen3-4B 先学会语义规避、再学表征规避；同种子 in-domain 探针的表征漂移为 0.0（95% CI [-0.01, 0.01]），换到新种子即恶化到 -0.32（95% CI [-0.36, -0.27]），且把打印"All tests passed!"这类掩饰与监控准确率负相关（r = -0.035, q = 0.024）。
- **Inference**: 训练前的静态准确率并不能预测监控在 RL 中的有效性，误差与策略无关（去相关）、抗适配的鲁棒性才是关键；监控奖励一旦主导奖励，规避就会变成模型的最优学习目标。
- **Recommendation**: 评估监控器时必须在 RL 过程中测漂移与规避率而非只看离线精度；干预上优先用低信号的"筛除"而不是高权重的渐进惩罚——后者在 2.0x 权重下有 40% 的运行退化成只输出错误答案。

**Key figures**

*Framework - We introduce three environments where reward hacking emerges naturally during training without finetuning or prompting to seed the behaviors. Using these environments, we build under- standi*

![Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL - framework](res/2611.09828_framework.png)

*Result - Naive probe and judge penal- ties applied during training provide lim- ited protection against reward hacking and harm performance: most runs still reward hack, and performance falls be- low*

![Designing Effective Monitor-Based Interventions for Mitigating Reward Hacking During RL - result](res/2611.09828_result.png)

**Why this ranks #16**: 论文开源三个真实奖励黑客环境（代码改测试、医患谄媚、传记幻觉），用 on-policy GRPO 训 Qwen3-4B（400 步、有效批量 256=16 prompt×16 采样、10 个随机种子），首次把监控器的信号强度、权重、召回与规避风险做成可量化权衡，是本方向少见的机制性研究。

---

### 17. Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards

**arXiv**: [2611.09448](https://arxiv.org/abs/2611.09448) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, rlvr, policy-entropy, exploration, covariance-attribution, solution-mode-collapse, School of Computer and Information Science | **Categories**: cs.AI, cs.LG | **Pages**: 8

**Authors**: Song Yu; Li Li; Zhenming Wu

**Affiliation**: School of Computer and Information Science, Southwest University

**Abstract**

> Policy entropy is widely used to diagnose exploration and collapse in reinforcement learning with verifiable rewards (RLVR), yet its magnitude does not consistently track reasoning performance across optimization objectives. We argue that this ambiguity arises because global token entropy conflates uncertainty in successful and failed trajectories, diversity across correct solution strategies, and variation among realizations of the same strategy. We introduce \textbf{Reward-Conditioned Entropy Allocation (RCEA)}, a hierarchical diagnostic framework that separates complete-trajectory entropy from average token entropy, conditions uncertainty on verifier outcome and process validity, measures correct-solution-mode retention, and connects these population-level quantities to local covariance-driven updates. In controlled sweeps over six RLVR objectives at two model scales, entropy trajectories do not induce a stable ordering of reasoning accuracy. Token entropy is higher for verifier-failed than successful trajectories under both broad separately aggregated estimates and a common-question paired analysis, whose confidence intervals exclude equality at 10 of 12 displayed endpoints. A local covariance approximation predicts the direction of adjacent-checkpoint entropy change in 95.5\% of nonfailed transitions; a reward-stratified endpoint proxy further shows that positive chosen-token covariance is more tail-concentrated within failed prefixes. Every reportable trained endpoint exhibits some contraction in independently audited correct-solution-mode breadth, whose positive association with large-\(k\) coverage remains exploratory. These results show that entropy collapse should be diagnosed by which uncertainty is removed, rather than by global entropy alone.

**Key findings**

- **Finding**: 6 个 RLVR 目标（GRPO/DAPO/Clip-Cov/KL-Cov/EP-GRPO/GTPO）在 Qwen2.5-3B/7B 上各训 1 个 epoch，熵轨迹给不出稳定的准确率排序（Clip-Cov 3B 宏平均最高 27.75%，KL-Cov 7B 最高 35.72%，DAPO 7B 的 MATH500 贪心 77.2% 却 pass@64 只有 92.6%）；Token 熵在 12 个端点上一律高于成功端点，配对 bootstrap 区间在 10 个端点排除相等。
- **Inference**: 全局熵下降既可能是错误被消除，也可能是正确解模式被压缩，因此熵的绝对值既非必要也非充分，不能当成可最大化目标来优化。
- **Recommendation**: 监控熵时按验证器结果分层统计 token 熵与有效解模式保留率 Ret+，并用协方差近似（方向命中 95.5%、R2 = 0.937）定位熵变化来自哪一批 token，而不是只看训练日志里的平均熵曲线。

**Key figures**

*Framework - Global entropy does not monotonically track rea- soning performance in the formal Qwen2.5-3B sweep.*

![Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards - framework](res/2611.09448_framework.png)

*Result - Conceptual overview of RCEA. The same direction of global entropy change can reflect error removal with successful- mode preservation or correct-solution mode contraction. Here R is verifier*

![Not All Entropy Is Equal: Reward-Conditioned Entropy Allocation in Reinforcement Learning with Verifiable Rewards - result](res/2611.09448_result.png)

**Why this ranks #17**: 这篇补上了本方向里「探索熵」这条的度量缺口：作者在 Qwen2.5-3B/7B 两个尺度、6 个 RLVR 目标的对照扫描中发现全局 token 熵与推理准确率没有稳定排序，配对分析里 12 个端点全部显示失败轨迹熵更高、其中 10 个置信区间排除相等，而局部协方差近似在 44 次相邻检查点转移中 42 次（95.5%）正确预测了熵变化方向。

---

### 18. Alignment by Confident Debate: Preference Learning from Multi-Agent Debate

**arXiv**: [2611.09568](https://arxiv.org/abs/2611.09568) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, multi-agent-debate, preference-learning, confidence-weighting, self-supervision, answer-equivalence, Upwork | **Categories**: cs.AI | **Pages**: 53

**Authors**: Nikhil Verma; Dingxian Wang; Mohammad Reza Rezaei; Andrew Rabinovich; Zhao Chen

**Affiliation**: Upwork Inc.

**Abstract**

> Post-training language models for reasoning typically rely on gold answers, task-specific verifiers, or learned reward models, limiting scalability when such signals are scarce. Multi-agent debate offers a self-supervised alternative, but converting debate into reliable training supervision remains challenging: majority voting weights agreeing responses equally, lacks a principled tie-breaking rule, and is ill-defined for open-ended tasks without a canonical answer; likelihood-based scoring can conflate fluency with correctness; and homogeneous committees may reinforce correlated errors. We introduce Alignment by Confident Debate (AbCD), which converts debate traces into preference data without gold answer labels. A sampling-diverse committee debates each problem, after which final answers are clustered by task-level semantic equivalence. We use verifiable tasks (mathematical reasoning, multiple-choice quantitative QA, and executable code-generation) as a controlled test bed: their answer keys or executable checkers let us evaluate the quality of debate-derived supervision against ground truth, even though the oracle itself never uses gold labels. Post-training on the resulting preferences outperforms inference-only ensembling and debate, as well as SFT on the same traces, across five model families spanning 1B to 8B parameters and four datasets, improving consensus accuracy, with a maximum gain of $21.5_{pp}$. Ablations show that the approach transfers to a larger model and to code generation, while also revealing limitations of heterogeneous committees and agreement-based weighting. Overall, the results suggest that debate traces can yield useful preference supervision when answer equivalence is combined with confidence-weighted disagreement.

**Key findings**

- **Finding**: 12 个模型-数据集组合上最优偏好目标全部超过推理期辩论，最大增益为 Llama-3.2-1B 在 SVAMP 上 19.0% 到 40.5%（+21.5pp），DPO 在 9 组最优、KTO 2 组、GRPO 1 组；而 SFT 在同样 traces 上只在 7/12 组超过辩论。
- **Inference**: 辩论产生的一致不等于正确——GSM8K 上五代理在第一轮交换后一致率最高，继续加轮次只增一致不加正确率，所以胜负必须由答案跨度置信度而非投票数决定。
- **Recommendation**: 无金标场景可用「答案等价聚类 + 跨度置信度」造偏好对，但默认只做一轮交换（N=5、M=2）并用温度多样性而非同质克隆组队；全轨迹置信度在首轮交换后 AUROC 平均掉 0.07，而答案跨度置信度平均升 0.04。

**Key figures**

*Framework - Committee behavior for Qwen- 2.5-1.5B-it on GSM8K. The committee size varies from one to five agents under inde- pendent sampling, after which the number of debate rounds is varied with five*

![Alignment by Confident Debate: Preference Learning from Multi-Agent Debate - framework](res/2611.09568_framework.png)

*Result - AbCD instantiates N sampling-diverse agents from the base policy πθ and lets them debate for M generations. Final traces are clustered by task-level answer equivalence, and the cluster with*

![Alignment by Confident Debate: Preference Learning from Multi-Agent Debate - result](res/2611.09568_result.png)

**Why this ranks #18**: 这篇把多智能体辩论改造成无金标偏好数据：N=5 个温度多样代理辩论 M=2 轮后按任务级答案等价聚类，用答案跨度置信度而非票数选出获胜簇；跨 5 个模型族（1B-8B）与 4 个数据集，DPO 在 12 组模型-数据对中的 9 组最优，最大提升 21.5pp。

---

### 19. Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters

**arXiv**: [2611.09634](https://arxiv.org/abs/2611.09634) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, multi-objective-alignment, lora-adapters, preference-conditioning, hypervolume, group-relative-optimization, School of Computer Science | **Categories**: cs.AI, cs.CL, cs.LG | **Pages**: 25

**Authors**: Constantinos Karouzos; Nikolaos Aletras

**Affiliation**: School of Computer Science, University of Sheffield

**Abstract**

> Language model deployment often requires different trade-offs between competing objectives as user preferences change, yet standard post-training methods typically produce a single policy for a fixed objective weighting. We introduce LambdaMix, a new parameter efficient method for learning a preference conditioned family of policies with group-relative online reinforcement learning. LambdaMix jointly trains one low-rank adapter per objective over a frozen base model. One preference vector selects the adapter mixture that generates responses and weights the separately normalized rewards used to update the adapters. A single training run supports changing preferences at inference without further optimization. We experiment with four models on helpfulness and harmlessness and on solving math problems while following instructions. We also evaluate the two largest models on rewriting comments to preserve wording while reducing clues about personal attributes. On the first two tasks, LambdaMix achieves higher hypervolume than all evaluated conditioned and policy merging baselines across all four models. LambdaMix uses fewer training completions and stores fewer adapter parameters than a set of GRPO specialist policies. With architecture and initialization fixed, varying adapter mixtures and objective weights together gives wider score ranges and higher coverage than varying either alone.

**Key findings**

- **Finding**: Qwen3.5-9B 上 LambdaMix 的 helpfulness/harmlessness 超体积达 0.8735，最强基线提示条件化为 0.7760；λ=(0.5,0.5) 时得分 5.586/8.487，高于十组 GRPO/GDPO 专家中最强的 5.040/7.747，而它只需两个适配器；GSM8K+指令遵循任务 HV 0.8099 对 GRPO 的 0.6947。
- **Inference**: 把偏好权重同时作用在采样策略和更新目标两处，比只做条件化的方法给出更宽的可调跨度（Qwen3.5-9B 上 1.931/1.982 对 0.300/0.379）和更少的非支配点损失。
- **Recommendation**: 需要多目标可调部署时优先考虑「每目标一个低秩适配器 + 偏好向量」方案，但注意按目标分别标准化奖励后再加权——在已归一化的奖励上标准化反而会拉低超体积（Qwen3-4B 上 0.6558 对 0.7372）。

**Key figures**

*Framework - LambdaMix uses the same preference for adapter mixing and objective weighting during training (a), then changes the preference mixture at inference (b).*

![Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters - framework](res/2611.09634_framework.png)

*Result - Helpfulness (Beaver reward) and harmlessness (negative cost) on PKU-SafeRLHF. Higher scores are better. Lines connect evaluated preferences.*

![Steerable Multi-Objective Group-Relative Preference Optimization with Jointly Trained Low-Rank Adapters - result](res/2611.09634_result.png)

**Why this ranks #19**: 一个偏好向量同时决定 LoRA 适配器的混合系数与各目标归一化奖励的权重，单次训练就得到可在推理期调节的策略族；在 Qwen3-4B/3.5-9B/3.6-27B 与 Olmo 3 7B 四个基座上，前两个任务（PKU-SafeRLHF 的 helpfulness/harmlessness、GSM8K 正确性+指令遵循）的超体积均优于全部条件化与策略合并基线。

---

### 20. On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning

**arXiv**: [2611.09872](https://arxiv.org/abs/2611.09872) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, test-time-rl, pseudo-labels, majority-vote, distributionally-robust, online-dpo, Mohamed bin Zayed University of | **Categories**: cs.AI | **Pages**: 15

**Authors**: Haoyu Wang; Ru Wang; Yuanyuan Wang; Jiaxian Guo; Mingming Gong

**Affiliation**: Mohamed bin Zayed University of Artificial Intelligence; The University of Melbourne; The University of Tokyo

**Abstract**

> Test-time reinforcement learning (TTRL) adapts pretrained language models to unlabeled target-domain data using self-generated pseudo-labels, whose reliability remains poorly understood. We analyze majority-vote supervision for TTRL with online Direct Preference Optimization (DPO) and decompose its error into population-majority bias and prompt-dependent finite-rollout variation. Because population-majority bias is generally unidentifiable without external supervision, we focus on mitigating the downstream effects of finite-rollout variation. We propose \emph{Prompt-Conditional Distributionally Robust DPO (PC-Dr.DPO)}, which conditions within-prompt robust reweighting on observed vote reliability to make updates from sampling-sensitive prompts more conservative. We further introduce a cache-based mechanism to reduce self-supervised forgetting during online adaptation. Across six mathematical and knowledge-intensive reasoning benchmarks and five model backbones, PC-Dr.DPO matches or outperforms the strongest TTRL baseline in 24 of 30 settings.

**Key findings**

- **Finding**: PC-Dr.DPO 每 prompt 采样 32 条 rollout 构造 8 对偏好，在 30 组模型-基准设置中有 24 组达到或超过最强 TTRL 基线（Qwen2.5-Math-1.5B 上 AMC 55.9% 对 TTRL 的 53.7%、MATH500 78.2% 对 77.9%；Qwen2.5-3B 上 MMLU-Pro 数学子集 64.7% 对 TTRL 的 46.0%）。
- **Inference**: 有限 rollout 波动随 m 指数衰减而总体多数偏置不随 m 下降，所以加大采样数只能稳住投票、纠正不了被多数带偏的答案，只能靠 prompt 级可靠度去调节更新的激进程度。
- **Recommendation**: 用多数投票自监督做在线 DPO 时，先统计每个 prompt 的众数占比 κ，对低可靠 prompt 用更小的鲁棒温度 βx = βbase·κ(x) 做更保守的组内重加权，并配合缓存回放抑制自监督遗忘。

**Key figures**

*Framework - Distribution of prompt-level modal-answer agree- ment for Qwen2.5-Math-1.5B-Instruct on the 83-problem AMC benchmark. For each prompt x, we sample m = 32 rollouts and compute the fraction pr*

![On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning - framework](res/2611.09872_framework.png)

*Result - Adaptation dynamics of Qwen2.5-Math-1.5B-Instruct on the AMC benchmark. Left: fraction of problems in the initial majority-vote-solvable set that are recovered by the adapted policy. Middle:*

![On the Reliability of Majority-Vote Pseudo-Labels in Test-Time Reinforcement Learning - result](res/2611.09872_result.png)

**Why this ranks #20**: 这篇把 TTRL 中多数投票伪标签的误差拆成「总体多数偏置」与「有限 rollout 波动」：前者不随 rollout 数下降、后者按 exp(-2mγ²) 衰减且不可外部辨识地纠正；PC-Dr.DPO 用 prompt 级众数占比 κ 条件化 Dr.DPO 的温度，在 6 个数学与知识推理基准、5 个骨干共 30 组设置中 24 组持平或优于最强基线。

---

## Footer

- Total papers reviewed across all 4 axes: 60
- llm_vlm axis final count: 20
- Wild-cards in this axis: 0
- Figure assets: 2026-11-09/res/

Generated by `mine-arxiv-daily-digest` skill. Sister file: `2026-11-09_llm_vlm_entry.md`.
