# ArXiv Daily Digest - 2026-11-05 (LLM 后训练 RL, 10 papers)

**Generated**: 2026-11-05 17:30 CST

**Source**: arXiv cs.CV, cs.SD, eess.AS, cs.CL, cs.AI, cs.RO, cs.LG submissions, listing day 2026-11-04 (announced 2026-11-05 00:00 UTC)

**Batch window**: 2026-11-03T18:00:00Z .. 2026-11-04T18:00:00Z（arXiv 公告批次横跨两个 UTC 日：前一日 18:00 UTC 起算，当日 17:59:59 UTC 截止）

**Track**: rl_llm (top 10 of 518 papers scanned, 70 full reads)

**Scope**: LLM 后训练的 RL：RLHF / DPO / GRPO / RLAIF / RLVR / on-policy 蒸馏与 RLVR 调度

---

## Top 10 - LLM 后训练 RL

### 1. C-GRPO: Conformal Group Relative Policy Optimization

**arXiv**: [2611.05591](https://arxiv.org/abs/2611.05591) | **Score**: 9.7 (relevance 10 x 0.7 + quality 9 x 0.3) | **Tags**: rl-llm, grpo, conformal-prediction, adaptive-rollout-budget, reasoning-training, compute-efficiency, University of Southern California | **Categories**: cs.LG | **Pages**: 24

**Authors**: Arya Fayyazi; Seyedarmin Azizi; Mehdi Kamal; Massoud Pedram

**Affiliation**: University of Southern California

**Abstract**

> Reasoning-oriented language model training increasingly relies on multiple on-policy rollouts, but standard Group Relative Policy Optimization (GRPO) uses a fixed group size, wasting compute on easy prompts and under-exploring hard ones. Existing adaptive-budget methods alleviate this inefficiency, yet their stopping rules are heuristic and do not provide a finite-sample calibration guarantee. We propose CGRPO, which replaces the fixed rollout budget of standard GPRO with calibrated conformal thresholds over task-specific nonconformity scores, combining Adaptive Prediction Set (APS)-style calibration for closed-form reasoning, a first-success score for execution-based code, automatic miscoverage selection, and periodic re-calibration. We prove finite-sample coverage for the resulting stopping rule and show that, under monotone policy improvement, recalibration induces a non-increasing expected training budget. Across six benchmarks spanning mathematics, graduate-level science, and code generation, CGRPO reduces mean training rollouts by 49-70% relative to fixed-budget GRPO while retaining strong fixed-budget accuracy, achieves the strongest pass@1 among evaluated static and dynamic baselines on different datasets, and transfers across model families with up to 82% rollout savings.

**Key findings**

- **Finding**: C-GRPO 用 APS 式共形校准（闭式推理）与 first-success 分数（执行式代码）替换固定 rollout 预算，6 个基准上平均训练 rollout 减少 49–70%，在 GSM8K 上对 Llama-3.1-8B 不重新调参还能再省 82%。
- **Inference**: 说明 rollout 预算可以是按难度自适应分配的量，而不是所有 prompt 一刀切的常数。
- **Recommendation**: 想压 GRPO 训练开销可直接替换停止规则；论文额外给出覆盖保证、假停控制与自退火保证，并做周期重校准（Δcal=50）。

**Key figures**

*Framework - Overview of C-GRPO workflow.*

![C-GRPO: Conformal Group Relative Policy Optimization - framework](res/2611.05591_framework.png)

*Result - Training dynamics (GSM8K, Qwen2.5-7B). C-GRPO sus- tains the highest reward and lowest KL divergence throughout training. Periodic dips align with ∆cal=50 re-calibration events; the policy r*

![C-GRPO: Conformal Group Relative Policy Optimization - result](res/2611.05591_result.png)

**Why this ranks #1**: 本线第 1：把 GRPO 的固定 rollout 预算换成基于共形校准的停止阈值，对闭式推理用 APS 式分数、对执行式代码用 first-success 分数，并给出有限样本覆盖证明；在 6 个基准上平均训练 rollout 减少 49–70%，跨模型迁移时在 GSM8K 上对 Llama-3.1-8B 额外省下 82%。

---

### 2. Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment

**arXiv**: [2611.06543](https://arxiv.org/abs/2611.06543) | **Score**: 9.7 (relevance 10 x 0.7 + quality 9 x 0.3) | **Tags**: rl-llm, process-reward, rubric-verification, token-level-credit, grpo, agentic-rl, Computer Network Information Center | **Categories**: cs.AI | **Pages**: 18

**Authors**: Shumao Wu; Kongcheng Zhang; Jianqiang Huang; Baisheng Lai

**Affiliation**: Computer Network Information Center, University of Chinese Academy of Sciences; Zhejiang University

**Abstract**

> Agent trajectories often contain both successful decisions and failed attempts, yet optimization with sparse trajectory-level rewards struggles to identify which critical decisions should be reinforced or suppressed. We observe that meaningful distinctions among on-policy trajectories can be distilled into natural-language process rubrics and used as process supervision signals. Based on this insight, we propose Online Rubric Self-Distillation (ORSD), which leverages self-derived process rubrics for dense token-level supervision, thereby augmenting outcome-centric reinforcement learning. Specifically, the current policy independently generates multiple rubric bundles at each step according to the same group of trajectories, extracting candidate process rubrics from cross-trajectory behavioral differences. A frozen verifier then evaluates all rubric items against each trajectory in the group, and selects one candidate bundle based on bundle-level alignment between rubric satisfaction and task success. ORSD treats the selected rubric bundle as privileged information during training, then compares the log-likelihoods of the original tokens with and without the rubric. The resulting likelihood gap provides token-specific process credit, which is added to the original trajectory-level GRPO advantage through additive advantage shaping. ORSD thus bridges trajectory-level outcome supervision and fine-grained process supervision, enabling token-level credit assignment using process signals. Extensive experiments on ALFWorld and WebShop show that ORSD accelerates policy improvement and boosts final task performance for both Qwen3-1.7B and Qwen3-4B under the same environment-interaction budget. Our code is available at https://github.com/AnnaXChun/ORSD.

**Key findings**

- **Finding**: 论文默认生成 M=4 份候选 rubric bundle 并由冻结验证器打分选出最优一份（默认 α=0.01、εc=0.2、η=10⁻³）；在 ALFWorld 上 ORSD 比最强基线 GRPO 高 12.12（Qwen3-1.7B）与 3.36（Qwen3-4B）个百分点，在 WebShop 上分别高 2.80 与 10.90 个百分点。
- **Inference**: 说明「判定过程好坏」比「产生好结果」更容易，可以从 on-policy 轨迹里自举出过程监督信号。
- **Recommendation**: 稀疏轨迹奖励下要定位关键决策时可照此用似然差构造 token 级信用；WebShop 上 Qwen3-1.7B 成功率从 GRPO 基线 55.40% 提到 63.00%，α 取 0.001 与 0.1 时分别掉到 59.80% 与 59.85%。

**Key figures**

*Framework - The overview of ORSD. (a) For each task, the policy first samples a group of trajectories. It then takes the task description and these trajectories as inputs to generate multiple rubric bun*

![Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment - framework](res/2611.06543_framework.png)

*Result - Sensitivity to α on WebShop with Qwen3-1.7B. The default is α = 0.01. Each setting uses the same GRPO baseline (55.40% success).*

![Using Experience Twice: Dynamic Process Rubrics for Privileged Token-Level Credit Assignment - result](res/2611.06543_result.png)

**Why this ranks #2**: 本线第 2：用策略自己从同一组 on-policy 轨迹生成多份自然语言过程 rubric，再由冻结验证器逐条打分并选出一份作为特权信息，用「有 rubric / 无 rubric」的似然差给出 token 级过程信用并叠加到 GRPO 优势上；在 ALFWorld 上比最强基线 GRPO 高 12.12 与 3.36 个百分点，WebShop 上 Qwen3-1.7B 达 63.00%。

---

### 3. On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation

**arXiv**: [2611.05609](https://arxiv.org/abs/2611.05609) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Tags**: rl-llm, on-policy-distillation, ood-generalization, capability-consolidation, post-rl, negative-result, University of Chicago | **Categories**: cs.LG | **Pages**: 27

**Authors**: Yichen Wang; Yufa Zhou; Siqi Zhu; Haozheng Luo; Jingzhi Bao; Zhichao Liu; Zijun Wei

**Affiliation**: University of Chicago; Duke University; University of Illinois Urbana-Champaign; Northwestern University; ByteDance

**Abstract**

> Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) to consolidate capabilities from multiple teachers. Although prior work reports near-perfect in-distribution (IND) distillation performance, we find that this can mask incomplete capability consolidation beyond the supervised distribution. A preliminary study on synthetic reasoning shows that OPD does not fully transfer teachers' generalization capabilities. We then extend this investigation to real-world tasks, evaluating extrapolative and compositional generalization across mathematical reasoning, coding, agent, and long-context capabilities using Qwen3 models. Across extrapolative settings, OPD and MOPD reach 96.04-102.73% of their teachers' IND scores. Yet their out-of-distribution (OOD) scores remain 2.45-16.25% below the base model's. Across three compositional settings, MOPD improves IND performance over the base model, but its performance on composed tasks as OOD remains 18.19-24.34% below that of the best teachers. To understand these gaps, we examine teacher capability and data coverage as two potential bottlenecks. Jointly alleviating these bottlenecks eliminates OOD forgetting in our experiments and suggests the potential for generalization beyond the teacher. (M)OPD also reduces OOD forgetting on average relative to its reinforcement learning (RL) baselines. Analysis of the associated update geometry reveals smaller and more spectrally concentrated updates on average than those of the RL baselines, along with greater shared update structure under MOPD. Motivated by these findings, we propose geometry-based patching and base-preserving replay to improve OOD performance while largely preserving IND performance. Our findings identify a blind spot in capability consolidation via (M)OPD, highlighting the need for algorithms that explicitly support OOD retention and generalization.

**Key findings**

- **Finding**: 外推设定下 OPD 与 MOPD 达到教师 IND 分数的 96.04–102.73%，但 OOD 分数仍比基座模型低 2.45–16.25%；三个组合设定下 MOPD 的组合任务 OOD 比最强教师低 18.19–24.34%。
- **Inference**: 说明分布内指标几乎不携带分布外信息，用它评估「能力固化」会给出过于乐观的结论。
- **Recommendation**: 评估蒸馏后的后训练必须同时报告 IND 与 OOD；论文据此提出几何修补与保持基座的回放，可在保住 IND 的同时改善 OOD。

**Key figures**

*Framework - Near-perfect IND distillation leaves an OOD transfer gap. The distillation ratio is sstudent−sbase*

![On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation - framework](res/2611.05609_framework.png)

*Result - Near-perfect IND distillation does not ensure OOD retention. Within each panel, benchmarks are arranged from IND on the left to OOD on the right. On most OOD evaluations, OPD performance (pur*

![On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation - result](res/2611.05609_result.png)

**Why this ranks #3**: 本线第 3：指出 on-policy 蒸馏「分布内近乎完美」掩盖了分布外能力没有被真正固化——外推设定下 OPD/MOPD 能拿到教师 IND 分数的 96.04–102.73%，但 OOD 仍比基座低 2.45–16.25%，组合设定下比最强教师低 18.19–24.34%。

---

### 4. Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains

**arXiv**: [2611.06244](https://arxiv.org/abs/2611.06244) | **Score**: 9.0 (relevance 9 x 0.7 + quality 9 x 0.3) | **Tags**: rl-llm, rubric-reward, preference-learning, curriculum, non-verifiable-domain, reward-hacking, University of Oxford | **Categories**: cs.AI, cs.LG | **Pages**: 35

**Authors**: Sumeet Ramesh Motwani; Tejas Krishnan; Alistair Letcher; Charles London; Suhaas Bhat; Huitian Jiao; Philip Torr; Riashat Islam; Christopher Summerfield; Jakob Foerster; Christian Schroeder de Witt; Qilong Gu

**Affiliation**: University of Oxford; Microsoft Research

**Abstract**

> Reinforcement learning with verifiable rewards (RLVR) has led to significant gains in math and code generation. Extending these gains to open-ended domains remains challenging: ground-truth verification is unavailable, human annotation is expensive, and learned reward models are prone to reward hacking. The generation-verification gap, where judging good outputs is easier than producing them, offers a potential path to improvement. However, rubric-based judges are often imprecise and stationary, so policies can overfit or reward hack them. We introduce Rubric Curriculum RL (RcRL), which exploits this gap without new data, human annotations, or stronger teacher models. We combine pairwise preferences over rollouts with a curriculum over rubric criteria, yielding a more discriminative signal than absolute scoring and a non-stationary objective. Whereas baselines plateau within a few hundred steps, RcRL preserves output entropy and keeps improving past 1000 steps. On creative writing, RcRL achieves a 70.5% human win rate against the base model, with gains across benchmarks and judges. On HealthBench, RcRL improves over the base model by 14.6% (full set) and 25.4% (consensus subset), outperforming all training baselines, including instance-specific rubrics.

**Key findings**

- **Finding**: RcRL 用 rollout 间的成对偏好加 rubric 准则课程，基线在几百步内 plateau 而 RcRL 保住输出熵并在 1000 步后继续提升；创意写作上对基座模型取得 70.5% 人类胜率，HealthBench 上相对基座提升 14.6%（全集）与 25.4%（共识子集），超过含实例专属 rubric 在内的所有训练基线。
- **Inference**: 说明在不可验证领域，靠准则难度随训练推进制造非平稳目标，比追求更准的静态评分更能抵抗 reward hacking。
- **Recommendation**: 做开放式领域的自提升时可直接组合成对偏好与准则课程；RcRL 无需新数据、人工标注或更强教师模型即可落地。

**Key figures**

*Framework - RcRL vs. RaR on FictionBench. Win rates against the*

![Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains - framework](res/2611.06244_framework.png)

*Result - Overview of Rubric Curriculum RL (RcRL). (Left) The challenge: training with a static rubric leads to reward hacking, where*

![Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains - result](res/2611.06244_result.png)

**Why this ranks #4**: 本线第 4：针对「判定比生成容易」的生成-验证鸿沟，用 rollout 之间的成对偏好加上 rubric 准则的课程学习，把静态评分换成更难被 hack 的非平稳信号；基线在几百步内就 plateau，RcRL 保住输出熵并在 1000 步后仍在提升，创意写作上对基座模型取得 70.5% 人类胜率。

---

### 5. Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning

**arXiv**: [2611.05942](https://arxiv.org/abs/2611.05942) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Tags**: rl-llm, reward-budgeting, advantage-construction, premature-convergence, sharpness-factor, llm-reasoning, Qwen Business Unit | **Categories**: cs.LG | **Pages**: 23

**Authors**: Mengni Jia; Mengyu Zhou; Xiaoxi Jiang; Guanjun Jiang

**Affiliation**: Qwen Business Unit, Alibaba; University of Cambridge

**Abstract**

> RL for LLM reasoning often reaches an early performance plateau as the policy distribution becomes increasingly sharp. Recent work has studied policy entropy as both a diagnostic and a control signal for this behavior. In our experiments, however, increasing entropy alone does not reliably change the eventual plateau. We analyze RL through its implicit target policy and derive a sharpness factor $κ$, together with an effective counterpart $κ_{\mathrm{eff}}$, that describes how strongly reward or advantage gaps are translated into probability-ratio gaps. Motivated by this view, we introduce \emph{reward budgeting}, a plug-in advantage construction that assigns a fixed total reward budget to each prompt. For binary rewards and independent on-policy rollouts, its unclipped score-function estimator follows the gradient of an exact finite-$G$ concave objective with diminishing returns, while its advantage gap decreases as more rollouts become correct. For general rewards, a shifted log-mean interpretation holds asymptotically under the stated regularity conditions. These results motivate, rather than establish exact objective equivalence for, the clipped implementations. On Qwen3-8B and Llama3.2-3B-Instruct, reward budgeting consistently improves a range of RL baselines, with gains up to +12.50 on AMC23 and +10.00 on AIME24 and AIME25. Overall, our results support an update-dynamics view of premature convergence and show that strong gains can be obtained without explicitly preserving entropy.

**Key findings**

- **Finding**: 论文导出 sharpness 因子 κ 与有效对应 κ_eff 描述奖励差距到概率比差距的映射；二元奖励与独立 on-policy rollout 下，奖励预算的未裁剪得分函数估计量是有限 G 凹目标的精确梯度；Qwen3-8B 与 Llama3.2-3B-Instruct 上 AMC23 最多提升 +12.50，AIME24 与 AIME25 各 +10.00。
- **Inference**: 说明 LLM 推理 RL 的早期 plateau 是更新动力学问题，而不是单纯的熵塌缩问题。
- **Recommendation**: 遇到训练提前饱和不必先动熵正则；论文的熵干预实验显示单纯提高熵不能可靠改变最终 plateau（Llama3.2-3B-Instruct 上 12 次运行，先用各自设置跑 500 步再切回同一基线跑到 1000 步）。

**Key figures**

*Framework - Average training entropy and validation accuracy across 12 runs for Llama3.2-3B-Instruct.*

![Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning - framework](res/2611.05942_framework.png)

*Result - Entropy-intervention test: each method uses its own setting for the first 500 steps and then switches back to the same baseline for steps 500–1000.*

![Reward Budgeting Reduces Premature Convergence in Reinforcement Learning for LLM Reasoning - result](res/2611.05942_result.png)

**Why this ranks #5**: 本线第 5：从隐式目标策略的视角导出 sharpness 因子 κ 及其有效对应 κ_eff，把「奖励或优势差距被翻译成多大概率比差距」讲清楚，并据此提出每个 prompt 分配固定总奖励预算的即插即用优势构造；在 Qwen3-8B 与 Llama3.2-3B 上稳定提升多个 RL 基线，AMC23 最多 +12.50、AIME24 与 AIME25 各 +10.00。

---

### 6. The Alignment Tax Is Graded: Task-Selective Capability Loss Under Length-Normalized DPO with SFT Retention

**arXiv**: [2611.06476](https://arxiv.org/abs/2611.06476) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Tags**: rl-llm, alignment-tax, dpo, length-normalization, pre-registered-study, tost-equivalence, Independent Researcher | **Categories**: cs.LG | **Pages**: 25

**Authors**: Ye Yuan

**Affiliation**: Independent Researcher

**Abstract**

> Setting. This is an empirical characterization study; we propose no new method and run no comparisons against alternative objectives. We fine-tune Qwen3.5-4B with sparse LoRA and length-normalized DPO plus an SFT retention term (the RPO objective) on structured financial-filing tasks, and track downstream capability as the implicit reward margin grows to $\sim 7$ $β$-scaled units (nf4 training; $\sim 3$ under fp16 measurement on the unquantized base). Question. Does margin growth degrade capability uniformly across tasks, or selectively? Findings. In a pre-registered study (8 seeds, 6 unseen at freeze) with artifact-aware scoring and TOST equivalence testing, the alignment tax is graded and task-selective: extraction is preserved ($Δ= -0.55$ pts, equivalent at $\pm5$ pts), json loses little ($Δ= -3.52$ pts, equivalence fails on a clustered item-level interval), and router degrades severely ($Δ= -30$ pts). Router's loss concentrates in a margin 1-3 damage window containing a transient format-break spike. The margin is accounted for almost entirely ($\geq 96\%$) by suppression of rejected completions, with chosen reward approximately flat, consistent with the retention term anchoring it; we do not attribute the behavioral damage to any single gradient channel. Gold-logp deflation is task-selective (extraction $-0.15$, json $-1.04$, router $-1.47$ nats/token under fp16), with gold selectively protected relative to incorrect controls on extraction (8/8 seeds). QLoRA reward margins differ up to $3.4\times$ between nf4 training and unquantized fp16 measurement, with an axis-dependent gap. Scope. Length-normalized rewards with SFT retention, sparse LoRA on 8/32 layers, one 4B model, easily-separable synthetic preferences, three structured tasks. A no-retention control and a measured format-alignment metric are left to future work.

**Key findings**

- **Finding**: 预注册研究用 8 个种子（6 个在冻结时未见）跟踪隐式奖励 margin 增长到约 7 个 β 单位：抽取 Δ=−0.55 点且在 ±5 点内等效，json Δ=−3.52 点但等效检验失败，router Δ=−30 点；至少 96% 的 margin 被拒绝回复的抑制解释。
- **Inference**: 说明「对齐税」不是一个标量，用「未检出差异」代替等效检验会把「已保留」与「功效不足」混为一谈。
- **Recommendation**: 报告 DPO 造成的能力损失时应做 TOST 等效检验并分任务给 Δ；该研究只覆盖长度归一化奖励加 SFT 保留项、4B 模型的稀疏 LoRA 与三个结构化任务，未做无保留项对照。

**Why this ranks #6**: 本线第 6：用预注册研究（8 个种子、其中 6 个在冻结时未见）配 TOST 等效检验，测出对齐税是「分级的、任务选择性的」——抽取几乎无损（Δ=−0.55 点，在 ±5 点内等效），json 小幅下降（Δ=−3.52 点），而 router 直接崩塌（Δ=−30 点）。

---

### 7. Suppressing Misaligned Behaviors in Language Models, Durably

**arXiv**: [2611.05358](https://arxiv.org/abs/2611.05358) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Tags**: rl-llm, behavior-suppression, grpo, alignment-shallow, durability, model-organisms, Princeton University | **Categories**: cs.AI, cs.CL, cs.LG | **Pages**: 31

**Authors**: Luxi He; Pengcheng Jiang; Jifan Zhang; Jiawei Han; Danqi Chen

**Affiliation**: Princeton University; University of Illinois Urbana-Champaign; Thinking Machines Lab

**Abstract**

> Undesired model behaviors can emerge or re-emerge at any stage of training. Once observed, how effectively can we suppress them? To study this question, we first construct two model organisms--language models deliberately trained to exhibit a specific misalignment--that differ in what triggers the behavior. The narrow-trigger organism misbehaves only when the prompt contains a specific cue: it cheats on multiple-choice questions by following a planted hint that points to a wrong answer, and behaves normally otherwise. The broad-trigger organism has no such cue: after fine-tuning on insecure code, it gives harmful responses across a wide range of open-ended prompts. We then formalize post-hoc behavioral suppression and evaluate methods along three criteria: immediate suppression of the target behavior, durability under further training, and preservation of general capability. We compare standard methods--SFT, GRPO, and gradient-ascent unlearning--along these dimensions. Building on prior work on alignment shallowness, we hypothesize that more durable suppression requires the ability to recover from a wider range of misalignment states. We introduce Prefix-Expanded Adversarial Reinforcement Learning (PEARL), a GRPO variant that augments rollouts with continuations from intermediate states sampled along cached organism trajectories. Across both organism settings and two model families (Qwen3-4B, GPT-OSS-20B), PEARL achieves strong immediate suppression while preserving task accuracy, and remains durable under further fine-tuning on either the organism's data or unrelated data. It obtains the greatest benefit when the undesirable behavior is broad and cannot be addressed through targeted SFT. Together, our framework and method offer a step toward more durable post-hoc removal of undesired behaviors.

**Key findings**

- **Finding**: 表格 2（3 个种子）显示 GPT-OSS-20B 上 PEARL 干净准确率 58.7±1.6%、带线索准确率 55.4±1.9%、作弊率 2.0±0.7%；Qwen3-4B 上 PEARL 作弊率 1.6±0.6%，而无 warmup 的 GRPO 干净准确率崩到 25.1±7.4%、作弊率高达 74.8±9.5%。
- **Inference**: 说明窄触发行为可以靠针对性 SFT 压住，宽触发行为则必须靠能覆盖更广错位状态的 RL 才压得住。
- **Recommendation**: 需要持久抑制不良行为时优先用前缀扩充的 GRPO 变体；宽触发 organism 上 GRPO 在 N=18k 回升到 6.28%，而 PEARL 在全部重激活尺度下都保持在 2% 以内。

**Key figures**

*Framework - Overview of our behavioral suppression framework. We first construct model organisms with narrow-trigger or broad-trigger undesired behavior, then apply suppression methods, and finally eval*

![Suppressing Misaligned Behaviors in Language Models, Durably - framework](res/2611.05358_framework.png)

*Result - Overview of PEARL. Gray squares denote prompt tokens, coral squares denote tokens from cached organism trajectories (used only as forced prefixes, with no gradient), and blue squares denote*

![Suppressing Misaligned Behaviors in Language Models, Durably - result](res/2611.05358_result.png)

**Why this ranks #7**: 本线第 7：把「事后抑制不良行为」形式化为三准则（立即抑制、继续训练下的持久性、通用能力保持），并提出 PEARL——用缓存的 organism 轨迹中间状态做前缀扩充 rollout 的 GRPO 变体；在 GPT-OSS-20B 上把作弊率压到 2.0%，而无 warmup 的 GRPO 在 Qwen3-4B 上崩塌到 74.8%。

---

### 8. GIST: Gibbs-Targeted Hierarchical Data Selection for Offline RLVR

**arXiv**: [2611.06395](https://arxiv.org/abs/2611.06395) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Tags**: rl-llm, offline-rlvr, data-selection, gibbs-target-policy, bidirectional-kl, token-efficiency, Hong Kong University of Science and | **Categories**: cs.AI, cs.LG | **Pages**: 19

**Authors**: Xuliang Huang; Tianxiang Zhao; Chengwei Qin; Yao Shu

**Affiliation**: The Hong Kong University of Science and Technology (Guangzhou); The Hong Kong University of Science and Technology

**Abstract**

> Offline reinforcement learning with verifiable rewards (RLVR) trains on a fixed pool of sampled responses and typically supervises every token of every response, although responses and tokens are not equally informative. We study which ones to supervise through the Gibbs-optimal policy of KL-regularized RLVR, which offline training targets, and measure the mismatch between a policy and this target with a bidirectional KL divergence. At the reference policy, this mismatch factorizes exactly and separates the two outcomes: correct responses contribute mainly through the forward term, concentrated on their low-probability tokens, and incorrect responses through the reverse term, concentrated on the responses the policy generates often and on their high-probability tokens. Based on this analysis, we propose GIST (Gibbs-Targeted Hierarchical Data Selection), a two-level selection method that approximates these principles with signals available before training. GIST uses the sampling temperature to select correct responses on-policy and incorrect responses near the policy's mode, and it uses the initial policy's token probabilities to supervise only the tokens where the mismatch lies. Applied to two offline training objectives, GIST raises the average accuracy over GSM8K, MATH-500, and MBPP for all three models under both objectives. In a controlled comparison on Qwen3-0.6B/GSM8K, it outperforms seven selection baselines that choose from the same candidates while supervising 66.6% fewer tokens than training on all candidates of the same prompts.

**Key findings**

- **Finding**: Qwen3-0.6B/GSM8K 上 GIST 用 4.55M 监督 token 达 45.79% 严格准确率，Random 为 6.64M token / 43.14%，全量候选为 13.60M token / 43.82%；GIST 比同样从这批候选里挑的 7 个选择基线高 1.59–3.33 个点。
- **Inference**: 说明离线 RLVR 里并非所有回复与 token 都同样有信息量，用 Gibbs 目标分解就能挑出该被监督的部分。
- **Recommendation**: 做离线 RLVR 时可按此两级策略筛样本；GIST 监督 token 比全量少 66.6%、比 Random 少 31.5%，同时少走 49.9% 的优化步数。

**Key figures**

*Framework - Test Strict accuracy versus super- vised tokens on Qwen3-0.6B/GSM8K. All methods use BOLT on the same candidate pool. GIST reaches the highest accuracy while supervising 66.6% fewer tokens t*

![GIST: Gibbs-Targeted Hierarchical Data Selection for Offline RLVR - framework](res/2611.06395_framework.png)

*Result - Overview of GIST (schematic). (a) Rollouts on-policy (τh = 1) and near the mode (τl). (b) Correct responses are taken from τh and incorrect ones from τl. (c) The frozen initial policy scores*

![GIST: Gibbs-Targeted Hierarchical Data Selection for Offline RLVR - result](res/2611.06395_result.png)

**Why this ranks #8**: 本线第 8：从 KL 正则化 RLVR 的 Gibbs 最优策略出发，用双向 KL 分解出「正确回复靠前向项、错误回复靠反向项」的不同失效形态，据此做两级选择；在 Qwen3-0.6B/GSM8K 上以 4.55M 监督 token 拿到 45.79% 严格准确率，比全量候选的 13.60M token / 43.82% 少用 66.6% token。

---

### 9. What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?

**arXiv**: [2611.06483](https://arxiv.org/abs/2611.06483) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Tags**: rl-llm, multi-turn-rl, pass-at-k-t, error-recovery, budget-mix, agentic-rl, Institute of Automation | **Categories**: cs.CL, cs.LG | **Pages**: 26

**Authors**: Kejian Zhu; Zhuoran Jin; Shangqing Tu; Tianyi Men; Yupu Hao; Jiachun Li; Kang Liu; Jun Zhao

**Affiliation**: Institute of Automation, Chinese Academy of Sciences, Beijing, China; School of Artificial Intelligence, University of Chinese Academy of Sciences; Tsinghua University

**Abstract**

> While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth $K$ and interaction depth $T$ via $Pass@(K,T)$, we show that trajectory-level RL advantages depend on sufficient turn budgets, diminishing significantly when budgets tighten. Besides, agentic RL does not uniformly elevate single-step decision quality; rather, its strength concentrates in error recovery and long-horizon resilience. To mitigate the deployment risks caused by this budget dependence, we provide a preliminary discussion on the benefits and limitations of process supervision signals and introduce BudgetMix RL as an alternative that varies interaction budgets during training. Experiments demonstrate that BudgetMix RL achieves robust performance across diverse execution settings. Project Page: https://rethinking-agentic-rl.github.io/

**Key findings**

- **Finding**: 在 FrozenLake 与 DeepCoder-MT 上，RL 模型选出的单步动作只在 46.8% 与 42.8% 的状态上优于基座（基座占优 52.5% 与 57.2%）；但从相同错误状态继续时，RL 终局成功率反超到 51.3% 对 38.6%、38.5% 对 22.9%。
- **Inference**: 说明多轮 agentic RL 提升的是错误恢复与长程韧性，而不是均匀地提升单步决策质量。
- **Recommendation**: 部署前应按交互预算评估而非只看平均回报；论文提出的 BudgetMix 在 25%、50%、75% 预算下相对全预算 RL 平均提升 7.5、5.3、4.0 个百分点，在 100% 预算下保持持平。

**Key figures**

*Framework - Overview of our findings. Left: Multi-turn agentic RL does not uniformly enhance per-step action quality; rather, it mainly enhances ability of error recovery and long-horizon resilience. Ri*

![What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents? - framework](res/2611.06483_framework.png)

*Result - Pass@K across sampling breadth. Sweeping the number of sampled trajectories K.*

![What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents? - result](res/2611.06483_result.png)

**Why this ranks #9**: 本线第 9：用二维指标 Pass@(K,T) 同时扫采样广度与交互深度，证明轨迹级 RL 的收益高度依赖交互预算——在 FrozenLake 与 DeepCoder-MT 上 RL 模型的单步动作质量只在 46.8% 与 42.8% 的状态上占优，但进入错误状态后反超到 65.7% 与 67.3%。

---

### 10. Turns Matter: Advancing Streaming Video RL via Turn-Level Credit

**arXiv**: [2611.06728](https://arxiv.org/abs/2611.06728) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Tags**: rl-llm, streaming-video, turn-level-credit, grpo, silence-prefix, streaming-decision, Fudan University | **Categories**: cs.CL, cs.CV, cs.LG | **Pages**: 16

**Authors**: Shuai Dong; Kanghui Tian; Linghan Chen; Wenqi Shao; Hongrui Wu; Haowen Hou; Yongfu Zhu; Xuehui Wang; Ziyue Wang; Wenpu Liu; Weichu Xie; Yuqi Xu

**Affiliation**: Fudan University; Shanghai Innovation Institute; JD.com; Stanford University

**Abstract**

> Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied to this setting, with existing approaches emphasizing reward design while retaining a single trajectory-level advantage across turns. Such shared credit can reinforce redundant replies after earlier successes and discourage useful follow-ups after earlier failures. We propose TurnWise, a turn-level GRPO framework that aligns learning with individual streaming decisions. TurnWise addresses the mismatch between trajectory-level feedback and turn-level interaction, promoting informative responses and reducing redundancy. Specifically, turn-level credit assignment uses silence-completed prefix scoring to construct group-relative advantages from each decision's remaining return, separating its learning signal from earlier rewards. Turn-mean policy optimization averages token losses within each turn and then across turns, giving response and waiting decisions equal weight regardless of output length. These complementary designs improve streaming policy learning without a learned critic or additional rollouts. Extensive experiments show our method outperforms prior RL approaches for streaming video understanding.

**Key findings**

- **Finding**: Qwen2.5-VL-3B 上 TurnWise 达 43.56 PAUC（ProactiveVQA）、21.59 平均 Timing F1（OVO-Timing）与 49.43 平均准确率（StreamingBench），分别超过最强非本方法结果 3.96、3.87、0.69 点；Qwen3-VL-4B 上为 42.44、11.15、58.96，增益 6.26、1.92、2.38 点。
- **Inference**: 说明流式场景的学习信号必须对齐「这一轮该不该回应」这个决策单元，共享优势会同时奖励冗余重复与惩罚有效追问。
- **Recommendation**: 做流式视频或流式交互 RL 时应按轮次分配信用；配合轮次内 token 损失平均后，重复率相对只做信用分配时从 15.53 降到 5.98，降幅 61.5%。

**Key figures**

*Framework - Shared advantages can reinforce redundant replies. GRPO assigns one trajectory-level advantage to all turns, so later repetitions may inherit positive credit from earlier successes. TurnWise su*

![Turns Matter: Advancing Streaming Video RL via Turn-Level Credit - framework](res/2611.06728_framework.png)

*Result - Overview of TurnWise. Given streaming video input x, user queries, dialogue history, and an observation plan, the policy samples a group of trajectories {τi}G*

![Turns Matter: Advancing Streaming Video RL via Turn-Level Credit - result](res/2611.06728_result.png)

**Why this ranks #10**: 本线第 10：指出流式视频 RL 里「一个轨迹级优势摊给所有轮次」会造成粒度错配——早轮成功会奖励后续重复、早轮失败会压制有用的追问；TurnWise 用静默完成前缀打分构造轮次级组内优势并做轮次内 token 损失平均，Qwen2.5-VL-3B 上 ProactiveVQA 达 43.56 PAUC，超过最强非本方法结果 3.96 点。

---

