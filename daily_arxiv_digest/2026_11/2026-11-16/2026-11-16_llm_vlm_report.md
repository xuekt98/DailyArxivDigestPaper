# Mine Arxiv Daily Digest - 2026-11-16 (LLM / VLM 与其强化学习 Axis, 20 papers)

**Generated**: 2026-11-16 11:54 CST

**Source**: arXiv cs.CV, cs.SD, eess.AS, cs.CL, cs.AI, cs.RO, cs.LG, cs.IR submissions, listing day 2026-11-13 (announced 2026-11-16 01:00 UTC)

**Batch window**: 2026-11-12T19:00:00Z .. 2026-11-13T19:00:00Z（arXiv 公告批次横跨两个 UTC 日：从前一日的美东 14:00 截止时刻起算（EDT 为 18:00Z，EST 为 19:00Z），到当日的同一时刻为止）

**Axis**: llm_vlm (20 papers, base 18, cap 20)

**Directions**: llm_core (10), vlm_core (5), llm_vlm_rl (5)

**Selection**: 20 papers ranked by relevance x quality, with 0 wild-card slots

**Day total**: 48 papers across 4 axes (target 60)

**Scope**: 大语言模型与视觉语言模型的设计、推理、agent、效率与上下文工作，以及面向 LLM / VLM 的 RL 与偏好优化、奖励模型

**Wild-card**: 0 —— 本 axis 未启用任何补位名额，三个 direction 都有足量够格论文，按候选富余量把名额分给了 `llm_core`，没有需要用邻接选题补位的空位。

**本 axis 20 篇，打满 axis 上限 20**：候选池 94 篇，是本批次供给最充裕的轴。`llm_core` 10 篇、`vlm_core` 5 篇、`llm_vlm_rl` 5 篇——`llm_core` 超出基准 2 个，正是 axis 内 `dir_under = 0` 时由 `axis_surplus = 2` 允许的额度。

**`llm_vlm_rl` 的 5 篇全部是无人工偏好数据的可验证奖励路线**：MDLM 的逐块方差缩减策略梯度、模型自己出反方陈词自己裁定的辩证能力训练、可验证判据的晶体结构 agentic 搜索、自动化 RL 训练过程监督、以及用 F1 当奖励的 AI 审稿人。本批没有一篇典型的「RLHF 打偏好数据」型工作。

⚠️ **pool 预筛有漏采**：另有 2611.17806（agent 的时间感知）、2611.17696（长程业务 agent 的确定性执行）、2611.17460（持久化 agent 的规则违规评测）、2611.17707（随机滤波重建损失）等论文的标题摘要都未命中 `pipeline.py` 的轴级正则，是逐篇读完全量候选时补进来的。词表本身不差，但**不能只依赖 pool 的关键词命中**。

---

## LLM 核心（架构 / 推理 / agent / 效率 / 上下文） · `llm_core` (10 papers)

本方向 10 篇，沿三条主线展开。**长期 agent**：CarryOn 学的是「在长程交互历史里该保留什么」，它指出既有做法大多在压缩历史，却没有回答该保留哪部分；Co-Sight Harness 把工作流定义、状态与领域知识整体外置成版本化控制资产，用状态机与可机器检查的验收门在执行期强制，并由独立审计器给轨迹打分；Can Agents Keep Up with Time 把「感知到当前时间」和「用时间改计划」明确拆成两件事，发现 agent 常常能拿到时间、甚至在推理里写下「日期已过」，却仍然让用户为一个过期事件做准备。**工程与效率**：LuthorSQL 让一个一次通过的 text-to-SQL 模型充当慢速 LLM agent 的 System 1，把每次查询都调外部模型的延迟与隐私暴露挪走；Interpreting Coding Agents 用 143,209 条执行轨迹、125 种 agent 配置与 117 个模型把 coding agent 的行为拆成可比较的结构；More Agents, More Samples, or More Thinking 用 516 组独立评测把多智能体协作、集成与测试时算力三者解耦；Fuse-All MoE 在 TPU 上给出带负载均衡的 MoE 推理 kernel。**安全与评测**：Unfinished-Bench 的 97 个情景里目标与规则不可兼得，它发现持久化会把「内部文档里写的规则」的违规率从 32.2% 抬到 43.6%，是同一条规则由用户直接说出时 8.5% 的五倍，而且 98.3% 的违规发生在规则已经展示之后；Reflect-Reasoning 训练的则是「如何推理原则」而不是「该遵循哪些原则」。RAG-FGO 则把 query rewriting 放进离散—连续混合空间，当作带精英记忆池的黑箱优化问题来做。

### 1. Co-Sight Harness: Externalized Control Assets and Deterministic Enforcement for Long-Horizon Business Agents

**arXiv**: [2611.17696](https://arxiv.org/abs/2611.17696) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, long-horizon-agent, harness-design, control-assets, acceptance-gates, enterprise-workflow, ZTE | **Categories**: cs.AI | **Pages**: 21

**Authors**: Luyao Wang; Xijun Zhu; Zhaohui Hao; Xiwen Zhang; Xingyu Wen; Weishan Li; Yuyang Liao; Yanqin Gao; Yongsheng Du; Lingjun Huang; Shaowei Zhao; Gang Li

**Affiliation**: ZTE Corporation

**Abstract**

> Long-horizon business workflows fail in two ways: errors accumulate as a chain of activities lengthens, and the knowledge an activity needs is written in a different vocabulary from the user's request. We study whether such workflows can be made reliable without changing the language model. Our method keeps the backbone fixed and moves the workflow definition, state and domain knowledge into versioned control assets outside the model. A state machine and machine-checkable acceptance gates enforce these assets during execution; an independent auditor grades the resulting trace. The assets are updated only after a regression check and human approval .We evaluate the method on three deployed workflows exceeding 200 steps. On Domain A, a 120-case end-to-end evaluation set shows unattended completion rising from 50% to 100%, retrieval recall from 56% to 91.67%, and end-to-end latency dropping from 440 to 159 minutes, with scenario-analysis recall rising from 45% to 93%. Two other domains were taken over by teams that did not write the assets, one in four days and one in seven days. A controlled ablation separates the two failure sources. The code is available at https://github.com/ZTE-AICloud/Co-Sight/tree/master/Co-Sight%20Harness.

**Key findings**

- **Finding**: 冻结骨干只改 harness，Domain A 的 120 例评测显示无人值守完成率 50%→100%、检索召回 56%→91.67%、端到端延迟 440→159 分钟、情景分析召回 45%→93%。
- **Inference**: 逐步可靠性 0.95 串十步只有 0.95^10≈60% 的成功率，长流程失败是乘积结构问题，靠换更大模型或加重试都改不动。
- **Recommendation**: 想提长流程可靠性，先把流程定义、状态与验收门外置成可版本化资产，再谈换模型；资产更新必须先过回归门并人工批准。

**Key figures**

*Framework - Overview of the proposed method and its implementation.*

![Co-Sight Harness: Externalized Control Assets and Deterministic Enforcement for Long-Horizon Business Agents - framework](res/2611.17696_framework.png)

**Why this ranks #1**: 中兴通讯（ZTE Corporation）把工作流定义、状态与领域知识外置成版本化控制资产，由状态机和机器可检验的验收门在执行期强制执行，骨干模型全程冻结。Domain A 的 120 例端到端评测里，无人值守完成率从 50% 升到 100%，检索召回从 56% 升到 91.67%，端到端延迟从 440 分钟降到 159 分钟；三个部署域的工作流都超过 200 步，且同一套资产被非原团队以 2 人×4 天、1 人×7 天接手。

---

### 2. CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents

**arXiv**: [2611.17808](https://arxiv.org/abs/2611.17808) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, context-management, long-horizon-agent, evidence-selection, token-efficiency, tool-agents, University of New South Wales | **Categories**: cs.AI, cs.CL | **Pages**: 31

**Authors**: Lihuan Li; Ruiyi Yang; Jiru Wang; Yifan Duan; Xiachong Lin; Hao Xue; Yang Song; Flora Salim

**Affiliation**: University of New South Wales; The Hong Kong University of Science and Technology (Guangzhou)

**Abstract**

> Long-horizon LLM agents can coordinate tools and applications to complete complex, multi-step tasks. As their interaction histories grow, effective context management becomes essential for reliable and efficient execution. Existing methods reduce context through summarization, pruning, or history selection. However, shorter contexts do not necessarily support better decisions: summaries can omit exact details needed for later actions, while retaining entire interactions can carry substantial irrelevant information. We propose CarryOn, a lightweight context manager that pairs compact execution state with fine-grained, source-linked evidence. A learned selector and adaptive retention policy keep relevant evidence available without additional LLM calls for context management. We introduce two complementary evaluation metrics: $S_α$ prioritizes task success while accounting for resource use, and normalized cost per success (NCS) measures the resources spent per successful task. Across AppWorld, OfficeBench, and Tau2 Telecom with three LLM Actors, CarryOn achieves 75.7% macro-averaged task success, exceeding the strongest baseline by 6.7 percentage points. It also achieves the best average scores on both metrics.

**Key findings**

- **Finding**: 三个 benchmark × 三个 Actor 上平均 Success 75.7%、S0.8 68.45、平均 NCS 0.792，Success 在 8 组对比中 7 次第一、1 次并列第一，NCS 在 6 组最低。
- **Inference**: 同一冻结选择器可跨不同 Actor 复用，说明收益来自证据选择机制本身，而不是靠某个基座模型的能力。
- **Recommendation**: 做长程 agent 时把状态与证据分开存，并按证据是否被后续调用复用来决定取舍，而不是按最近顺序裁剪。

**Key figures**

*Framework - CarryOn: carry what matters. Left: Context-management challenges and CarryOn’s separation of compact task state from fine-grained evidence. Right: Success–efficiency comparison (top) and tas*

![CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents - framework](res/2611.17808_framework.png)

*Result - CarryOn overview. (1) History: The archive supplies fine-grained observation units. (2) Evidence selection: The selector ranks units using the task and latest observation. (3) Acting: The Ac*

![CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents - result](res/2611.17808_result.png)

**Why this ranks #2**: 新南威尔士大学与香港科技大学（广州）把紧凑执行状态和细粒度、带来源链接的证据分开管理，学习式选择器加自适应保留策略无需额外 LLM 调用即可取舍历史。在 AppWorld、OfficeBench、Tau2 Telecom 三个 benchmark、三个 LLM Actor 上宏平均任务成功率 75.7%，比最强基线高 6.7 个百分点，平均 S0.8 为 68.45、平均 NCS 0.792 为最低，是 llm_core 里上下文预算管理最完整的一篇。

---

### 3. Alignment with Reflect-Reasoning: Learning How To Follow Principles

**arXiv**: [2611.17398](https://arxiv.org/abs/2611.17398) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, constitutional-alignment, reflective-reasoning, grpo-posttraining, ood-principles, jailbreak-robustness, Duke University | **Categories**: cs.LG | **Pages**: 51

**Authors**: Henry Bell; Caroline Zhang; Dhaval Potdar; Mohammed Mobasserul Haque; Brandon Fain

**Affiliation**: Duke University; Independent Researcher

**Abstract**

> The appropriate governing norms and principles for the alignment of Large Language Models (LLMs) often depend on cultural context and deployment application. However, most alignment techniques focus on training models to conform to human preferences or constitutional principles specified at training time and subsequently fixed. In practice, many deployers rely on system prompting to implement contextual norms and guardrails at inference time. Prior work has shown that post-generation reflective reasoning with critique and revision can improve conformance compared to simple system prompting, but such methods are limited to the reasoning abilities inherent in the trained model. We introduce Reflect-Reasoning, a training method that teaches models how to reason about alignment to principles, rather than simply which principles to follow. Across five models, Reflect-Reasoning consistently outperforms both system prompting and explicit prompting strategies for in-context reflective reasoning. These improvements extend and generalize to entirely out-of-distribution domains of medical and financial principles. We additionally demonstrate that Reflect-Reasoning reduces the occurrence of rare but serious principle violations. Finally, we show that Reflect-Reasoning does not erode the safety engineering of a model and is robust against jailbreaking attempts using adversarial constitutions. Overall, our results demonstrate that Reflect-Reasoning is a scalable method for training constitutional alignment as a generalizable reasoning capability, enabling models to adapt to novel principles and produce transparent reasoning traces without additional fine-tuning.

**Key findings**

- **Finding**: 五个模型在留出原则上对 Base-ICL 胜率 82.5%–94.7%、对 Reflect-ICL 66.8%–86.9%，金融与医疗分布外领域最高分别达 80.2% 与 86.3%。
- **Inference**: 胜率优势来自训练出的反思过程本身，因此换一套新原则也能直接迁移，而不必为每个部署场景重启后训练。
- **Recommendation**: 需要按场景切换原则时优先训练反思推理能力，并为罕见但严重的原则违规单独做尾部统计，别只看平均胜率。

**Key figures**

*Framework - Demonstration of reflective reasoning traces on different deployment-specific constitutions of princi- ples*

![Alignment with Reflect-Reasoning: Learning How To Follow Principles - framework](res/2611.17398_framework.png)

*Result - Reflect-Reasoning training process*

![Alignment with Reflect-Reasoning: Learning How To Follow Principles - result](res/2611.17398_result.png)

**Why this ranks #3**: 杜克大学与独立研究者用两阶段后训练（先 SFT 再 GRPO）教模型「如何对原则做反思推理」而不是「遵守哪些原则」，全程不需要人工标注数据。五个模型在留出原则上的成对胜率对 Base-ICL 达 82.5%–94.7%、对 Reflect-ICL 达 66.8%–86.9%，并延伸到金融与医疗两个分布外领域（最高 80.2% 与 86.3%），且不损伤模型原有安全工程、对抗性越狱宪法也稳健。

---

### 4. Interpreting Coding Agents Through Their Behavioral Trajectories

**arXiv**: [2611.17440](https://arxiv.org/abs/2611.17440) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, coding-agent, trajectory-analysis, behavioral-profile, agent-scaffold, tool-call-parsing, Nebius | **Categories**: cs.AI, cs.LG, cs.SE | **Pages**: 18

**Authors**: Ibragim Badertdinov; Alexander Golubev

**Affiliation**: Nebius

**Abstract**

> Standard coding-agent benchmarks primarily evaluate binary task success, treating execution as a black box and obscuring the behaviors that produce those outcomes. We analyze a large corpus of 143,209 execution trajectories from 125 agent configurations spanning 117 unique models. To enable comparisons across heterogeneous agent interfaces, we develop a rule-based parser that maps raw execution traces to high-level actions such as repository search, file editing, and test execution, and audit its predictions against a six-model consensus reference on 500 events. We find that agents with similar solve rates can nevertheless differ substantially in how they explore, modify and verify code. Moreover, without using task outcomes, token counts, or tool names as features, aggregate behavioral profiles retrieve the corresponding agent stack across disjoint repository sets and programming languages, although task composition is not fully controlled in the cross-repository setting. Through analyses of frontier models and agent scaffolds, we further show that scaffold choice and reasoning effort systematically shift agents' search, editing, and testing behavior. We release the deterministic parser together with the full annotation and analysis pipeline alongside an annotated trajectory subset.

**Key findings**

- **Finding**: 143,209 条轨迹覆盖 125 种 agent 配置与 117 个模型，解析器预测在 500 个事件上与六模型共识参考做审计对齐。
- **Inference**: 不用解题结果、token 数和工具名当特征，仅凭行为画像就能跨不相交仓库与编程语言检索出对应 agent 栈，说明成功率之外确实还有可区分的行为信息。
- **Recommendation**: 选 coding agent 时先对齐 scaffold 与推理强度再看行为差异，否则会把框架差异误当成模型能力差异。

**Key figures**

*Framework - Automated action classification pipeline. The rule-based parser pairs each tool call with its execution output and classifies it across four core attributes: primary operation, target file r*

![Interpreting Coding Agents Through Their Behavioral Trajectories - framework](res/2611.17440_framework.png)

*Result - Workflow differences across outcome-matched agent pairs. Points indicate the median task-level absolute difference across 60 scaffold-matched agent configuration pairs (|∆solve| ≤1.0 pp on ≥*

![Interpreting Coding Agents Through Their Behavioral Trajectories - result](res/2611.17440_result.png)

**Why this ranks #4**: Nebius 用规则解析器把原始执行轨迹映射成检索、文件编辑、测试执行等高层动作，四个属性（主动作、目标文件角色、修改类型、读取模式）都能从 tool call 与其输出配对推出，并在 500 个事件上与六模型共识参考交叉审计。语料覆盖 143,209 条轨迹、125 种 agent 配置、117 个模型，60 对 scaffold 匹配配置（|∆solve| ≤1.0pp）显示解题率相近的 agent 行为差异依然明显，是解读 coding agent 行为的可核对基线。

---

### 5. Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments

**arXiv**: [2611.17460](https://arxiv.org/abs/2611.17460) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, persistent-agent, rule-violation, instruction-conflict, agent-benchmark, workplace-scenario, NAVER AI Lab | **Categories**: cs.CL, cs.LG | **Pages**: 21

**Authors**: Seunghyun Lee; Jaehui Hwang; Dongyoon Han; Sangdoo Yun

**Affiliation**: NAVER AI Lab

**Abstract**

> AI agents are increasingly equipped with persistence toward task completion to run delegated work autonomously for long periods, under many unstated constraints from internal documents and other people's authority. When completion requires violating a rule, the agent must decide alone, yet benchmarks of instruction-rule conflicts state the rule in the prompt or keep it hidden and do not evaluate persistence. We present Unfinished-Bench, a benchmark that gives models persistence in autonomous runs without a user, in realistic work environments with embedded rules. In each of its 97 scenarios across 7 organizations and 7 risk categories, the goal and the rule cannot both hold. We find that persistence raised violations of a rule in an internal document from 32.2% to 43.6%, five times the 8.5% for the same rule stated by the user. Of the document-rule violations, 98.3% occurred after the rule was displayed, and in 89% of a judged sample the agent first wrote down the rule. Violations of rules placed in the environment without user oversight can lead to serious incidents, so persistence-driven risks need to be evaluated. Benchmark documentation: https://francis21c.github.io/unfinished-bench/

**Key findings**

- **Finding**: 97 个情景（7 组织、7 风险类）中，文档规则违反率随持久性从 32.2% 升到 43.6%，而用户口述同一规则时只有 8.5%。
- **Inference**: 98.3% 的文档规则违反发生在规则已被展示之后，且被判定样本里 89% 的 agent 先把规则写下来再继续，说明它看见规则却仍选择违例。
- **Recommendation**: 评估持久化 agent 必须单独设「规则藏在环境里、无用户监督」这一档，否则会系统性低估事故概率。

**Key figures**

*Framework - Overview of Unfinished-Bench. Left: a user hands off a task in an organization with internal documents, chat, work tools, and colleagues, and leaves. Red marks show where the rule for the ta*

![Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments - framework](res/2611.17460_framework.png)

*Result - Violation rate per model. Red marks the rule in an internal document and dark gray the rule stated by the user; light circles are without persistence and dark circles with persistence, joine*

![Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments - result](res/2611.17460_result.png)

**Why this ranks #5**: NAVER AI Lab 的基准让 agent 在没有用户在场的情况下持久执行任务，97 个情景覆盖 7 个组织与 7 类风险，每个情景里任务目标与内部文档规则不可兼得。一旦给 agent 持久性，文档规则违反率从 32.2% 升到 43.6%，是同一条规则由用户口述时 8.5% 的五倍；其中 98.3% 的违反发生在规则已被展示之后，是评估持久化 agent 风险时不可省略的一档。

---

### 6. More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs

**arXiv**: [2611.17610](https://arxiv.org/abs/2611.17610) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, multi-agent, test-time-compute, baseline-matching, ensemble-decomposition, meta-analysis, University of Nevada | **Categories**: cs.AI, cs.CL, cs.LG, cs.MA | **Pages**: 43

**Authors**: Seyed Mahmoud Sajjadi Mohammadabadi

**Affiliation**: University of Nevada, Reno

**Abstract**

> Evaluations of multi-agent language models often compare communicating architectures against a single greedy pass. This practice confounds coordination with sample multiplicity and inference compute. We synthesize nine primary empirical evaluations comprising 516 unique multi-agent configurations organized along a resource vector R with six dimensions and a baseline ladder with four categories. Against baselines with a single pass (Category A), multi-agent accuracy differences are negative overall and near zero when omitting the largest contributing study. When evaluated against baselines matched on sample count (Category B) or resource budget (Category C), multi-agent systems average -0.042 in accuracy, and multilevel random effects modeling on the log odds scale remains negative across sensitivity checks. Multi-agent accuracy equals or falls below the baseline in 74% of these comparable contrasts, and study means are nonpositive in almost all evaluated studies. Across studies reporting both baselines, moving from a greedy pass to a sampled baseline shifts accuracy differences by -0.038 on average. Because communication adds no information when agents share identical evidence, positive returns require partitioned evidence, external verification, or error diversity across models. We provide a reviewer checklist and accounting utilities.

**Key findings**

- **Finding**: 对齐样本数或资源预算后，多智能体系统平均精度差 −0.042，在 474 次可比对照中 74% 等于或低于基线（对采样基线的 360 次里占 76%）。
- **Inference**: 对 Choi 等的 14 个模型与 benchmark 配置做分解，贪心解码 0.670、5 样本投票 0.747、5 agent 辩论 0.715，所谓多智能体收益主要来自采样效应而非协作本身。
- **Recommendation**: 评审多智能体方案时必须要求给出样本数与推理预算对齐的基线，否则多出来的算力无法归因到协作设计。

**Key figures**

*Framework - The Baseline Ladder: Single-agent baseline categories and inferential validity. Gray rungs represent comparisons that do not control test-time compute: Category A (Greedy single pass): A sin*

![More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs - framework](res/2611.17610_framework.png)

*Result - Accounting decomposition on Choi et al. [13] (m = 14 model and benchmark configura- tions). Mean accuracy for single-agent greedy decoding (0.670), five-sample majority voting (0.747, differ*

![More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs - result](res/2611.17610_result.png)

**Why this ranks #6**: 内华达大学里诺分校把多智能体评测里的协作、采样与推理预算拆开：9 项主评测、516 种唯一配置，按 6 维资源向量和 4 级基线阶梯分类。与样本数或资源预算对齐的基线相比，多智能体系统平均精度差 −0.042，474 次可比对照里 74% 等于或低于基线；仅把贪心单次换成采样基线，差距就变化 −0.038，是本批次最直接的多智能体祛魅证据。

---

### 7. LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent

**arXiv**: [2611.17780](https://arxiv.org/abs/2611.17780) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, text-to-sql, system1-system2-cascade, local-model-offload, inference-cost, quantization, UC Irvine | **Categories**: cs.AI, cs.CL, cs.DB, cs.LG | **Pages**: 23

**Authors**: Ibrahim Memon; Armin Karamzade; M. Hanif Jhaveri; Roy Fox

**Affiliation**: UC Irvine; Independent Researcher

**Abstract**

> Frontier LLM agents that query databases with tools are among the most accurate text-to-SQL systems, but per-query calls to a hosted model are slow, costly, and expose sensitive organizational queries to external APIs. For example, a Claude Opus 5.5 agent serving 10,000 queries a day costs over $70,000 a year at list price. To what extent can local hardware already owned by an organization offload this burden without compromising the agent's accuracy? We present LuthorSQL, a non-autoregressive 7B text-to-SQL model that serves as a rapid System 1 gate for a slower LLM agent (System 2), escalating queries only when uncertain. LuthorSQL makes a single forward pass to predict slot scores over a bounded grammar for query plans, compiles and runs up to 32 candidate plans, and chooses an answer using a trained validator. On its own, LuthorSQL reaches 68.03% execution accuracy on BIRD's hidden test set at 0.84 s per question on a single GPU, maintains its accuracy in 9 GB with 8-bit quantized weights, and transfers zero-shot to Snowflake, BigQuery, MySQL, PostgreSQL, and DuckDB within 3.1 points of its native SQLite accuracy. Combined with Claude Opus 5.5 in a pre-registered confidence cascade over 227 questions on databases published after Opus's training cutoff, LuthorSQL answers nearly half of all questions locally and cuts API cost by 33.3% at the same accuracy. Finally, contamination probing shows that Opus reproduces 48-92% of public benchmark gold queries verbatim without seeing the schema; however, its tool-assisted accuracy holds on renamed schemas and reaches 95.6-97.4% on post-cutoff databases. Code and data: https://github.com/IAMIbrahimmemon/luthorsql

**Key findings**

- **Finding**: LuthorSQL 单独在 BIRD 隐藏测试集达到 68.03% 执行准确率、每题 0.84 秒，8-bit 量化后仍在约 9 GB 内存内维持该准确率。
- **Inference**: 227 道截止后新题上的预注册置信度级联让本地模型回答了近一半问题，API 成本降 33.3% 而准确率 95.15% 对 95.59%（p=1.0）无统计差异。
- **Recommendation**: 量大且查询敏感的数据库场景可先用本地小模型过滤，只把不确定的样本交给闭源 agent，但要保留验证器的置信度边际作为路由依据。

**Key figures**

*Framework - How LuthorSQL answers a question. The slot heads, read after the question, point to schema columns and to a stored value; the word links are drawn for illustration, since the model scores sl*

![LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent - framework](res/2611.17780_framework.png)

*Result - Cost saving of the t = 3.0 cascade in the held- out tests against Opus alone (B0, circles) and Opus with System 1’s candidates on every question (B1, squares), with System 1 on local hardwar*

![LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent - result](res/2611.17780_result.png)

**Why this ranks #7**: 加州大学尔湾分校（UC Irvine）用 7B 非自回归模型做 text-to-SQL 的 System 1：单次前向给有界语法下的查询计划槽位打分，编译并运行最多 32 个候选计划，再用训练好的验证器选答案。单独使用在 BIRD 隐藏测试集拿到 68.03% 执行准确率、每题 0.84 秒（单 GPU），8-bit 量化后只占 9 GB 内存；与 Opus 级 agent 做置信度级联，API 成本下降 33.3% 而准确率不变。

---

### 8. Can Agents Keep Up with Time? An Empirical Analysis of Temporal Adaptation After a Conversational Hiatus

**arXiv**: [2611.17806](https://arxiv.org/abs/2611.17806) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, temporal-awareness, long-horizon-agent, session-rekindling, date-reasoning, agent-benchmark, People's Public Security University of | **Categories**: cs.AI | **Pages**: 11

**Authors**: Hongguan Su; Ming Wang; Shun Zhang; Yifan Wang; Rong Yin; Zhiming Ma; Mengzheng Yang; Peng Chen

**Affiliation**: People's Public Security University of China; Northeastern University; Beihang University; Henan University

**Abstract**

> Long-horizon agents increasingly serve as persistent personal assistants across modern web platforms, managing schedules, applications, and multi-step plans over weeks or months. Users often return to an ongoing conversation after a long conversational hiatus, while earlier bookings and preparation notes stay on record. During this hiatus, scheduled dates may pass even though the retained records remain unchanged and event outcomes go unrecorded. Existing evaluations of long-horizon agents focus on fact retention and explicit state updates. Whether agents perceive the passage of time and adapt their advice accordingly therefore remains unknown. We frame this ability as temporal state perception and use, which means perceiving the current time and applying it when interpreting dated records. To study it, we design session-rekindling tasks that keep the earlier conversation fixed and vary only the follow-up date and the way temporal information reaches the agent. Experiments across five model routes and five temporal-information conditions show that agents can obtain the current time but often fail to use it. They reliably query the clock and even note in their reasoning that the scheduled date has passed, yet many still tell users to prepare for the expired event. Supplying explicit temporal context reduces this error, and providing the computed date relation removes it entirely. Keeping up with time therefore depends on turning perceived time into updated plans. Based on these findings, we design a session-rekindling benchmark that provides temporal-awareness guidance for designing long-horizon agents. The code can be found at https://github.com/Adoreu2/session-rekindling-benchmark.

**Key findings**

- **Finding**: 五条路线中四条在 70 题显式日期基线上答对 69 或 70 题，但整体过期框架率仍达 58.9%、建议接受率只有 46.6%（41/88）。
- **Inference**: 120 个答案里有 116 个的推理过程明确写出了日期已过，答案却仍把事件说成即将到来，是推理与回答脱节而不是算错日期。
- **Recommendation**: 直接给 agent 已算好的日期关系（如「已过期 30 天」）比只提供当前时间更能消除过期建议，这也被整理成 session-rekindling 基准。

**Key figures**

*Framework - A session-rekindling scenario where the scheduled May 6 health check has passed by the June 5 follow-up, con- trasting stale preparation advice with an appropriate clarify- ing response.*

![Can Agents Keep Up with Time? An Empirical Analysis of Temporal Adaptation After a Conversational Hiatus - framework](res/2611.17806_framework.png)

*Result - Structure of a session-rekindling episode re-engaged on June 5, comparing retained records, unobserved event outcomes, and divergent responses from two model routes under identical clock rea*

![Can Agents Keep Up with Time? An Empirical Analysis of Temporal Adaptation After a Conversational Hiatus - result](res/2611.17806_result.png)

**Why this ranks #8**: 中国人民公安大学等四校把长程 agent 的能力拆成时间状态感知与使用：五条规定时间信息条件、五个模型路线、940 个主评测单元。结果是 agent 拿得到当前时间却常常不用——自然条件下 158/210 次响应调用时钟工具，但过期框架率仍达 58.9%、建议接受率只有 46.6%（41/88），说明缺的是把感知到的时间转成更新后的计划。

---

### 9. Fuse-All MoE Inference Kernel with Load Balancing on TPUs

**arXiv**: [2611.17857](https://arxiv.org/abs/2611.17857) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, moe-inference, tpu-kernel, load-balancing, expert-parallelism, prefill-decode, Meta SuperIntelligence Lab | **Categories**: cs.LG | **Pages**: 23

**Authors**: Rupeng Liu; Bangsheng Tang; Zongwei Zhou; Chengji Yao; Yejin Lee

**Affiliation**: Meta SuperIntelligence Lab

**Abstract**

> Mixture-of-Experts (MoE) architectures activate only a subset of experts for each token, allowing large language models (LLMs) to scale parameter capacity without a proportional increase in computation per token. However, intermediate data movement and uneven expert loads limit the efficiency of MoE inference on TPUs. To address these bottlenecks, we introduce Fuse-All MoE, a TPU kernel design that jointly optimizes expert computation, output communication, and load balancing. The kernel fuses token collection, expert projections, gated activation, and output writes, retaining expert computation intermediates on chip. Fixed token-slot destinations allow scheduling and expert placement to change while preserving routing semantics. In prefill-decode (PD) disaggregated serving, Fuse-All MoE balances EP16 prefill workloads through scheduling and expert redistribution, while symmetric EP8TP2 shares active expert computation between the two TensorCore devices within each chip during decode. Our experiments show that Fuse-All MoE reduces kernel runtime for a measured skewed EP16 prefill workload from 2.3x to 1.09x the same fixed reference time for a balanced workload. Across 32-512 decode tokens, symmetric EP8TP2 reduces kernel latency by up to 21.3% relative to fused EP16. With accompanying serving stack optimizations, the integrated system improves serving throughput by up to 34.5% over the Megablox EP16 baseline.

**Key findings**

- **Finding**: 融合内核把倾斜 EP16 prefill 的耗时从参考平衡负载的 2.3 倍降到 1.09 倍，对称 EP8TP2 在 32–512 个 decode token 上延迟最多再降 21.3%。
- **Inference**: 行分桶、热专家预取与目的地交错分别针对空算、权重预取重叠与流量突发，说明 MoE 推理的瓶颈一半在访存与均衡而不在算力。
- **Recommendation**: 部署 MoE 服务要分开调 prefill 与 decode 的并行策略（EP16 对称 EP8TP2），并把负载均衡和融合内核当作两件事分别压测。

**Key figures**

*Framework - Fusion boundary. Gate/up and activated intermediates stay in VMEM; expert results go directly to final token-slot buffers. Routing, input exchange, and postprocessing remain outside the expe*

![Fuse-All MoE Inference Kernel with Load Balancing on TPUs - framework](res/2611.17857_framework.png)

*Result - Hardware and representation. Chipmates have separate address spaces; scalar metadata and vector tiles use separate memories. FP4 packing reduces weight storage, and a leading row axis suppor*

![Fuse-All MoE Inference Kernel with Load Balancing on TPUs - result](res/2611.17857_result.png)

**Why this ranks #9**: Meta SuperIntelligence Lab 为 TPU7x（Ironwood）设计的融合 MoE 内核把 token 收集、专家投影、门控激活与输出写回合到一条流水，专家中间结果留在 VMEM、不再落回主机；固定 token-slot 目的地让调度与专家放置可以独立改动而不改路由语义。实测倾斜 EP16 prefill 负载的内核耗时从平衡负载参考时间的 2.3 倍压到 1.09 倍，32–512 个 decode token 下对称 EP8TP2 延迟再降 21.3%，整体服务吞吐最高提升 34.5%。

---

### 10. RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG

**arXiv**: [2611.17788](https://arxiv.org/abs/2611.17788) | **Score**: 7.7 (relevance 8 x 0.7 + quality 7 x 0.3) | **Direction**: `llm_core` | **Tags**: LLM-VLM, query-rewriting, prompt-optimization, black-box-search, elite-memory-pool, retrieval-quality, Kyung Hee University | **Categories**: cs.CL | **Pages**: 12

**Authors**: Qigan Sun; Xudong Wang; Chaoning Zhang; Chenghao Li; Jiaquan Zhang; Jiehui Xie; Sungyoung Lee; Jie Zou; Ning Xie; Peng Wang; Yang Yang; Heng Tao Shen

**Affiliation**: Kyung Hee University; University of Electronic Science and Technology of China; Tongji University

**Abstract**

> In retrieval-augmented generation (RAG), query rewriting serves as a core interface that aligns user intent with external knowledge bases, and its effectiveness directly determines overall system performance. However, generative retrieval faces three critical challenges in real-world deployment: noisy retrieval feedback, the difficulty of jointly optimizing discrete prompt templates and continuous decoding-control parameters, and the limited generalization of static rewriting strategies under semantically complex scenarios. To address these issues, we propose RAG-FGO, a dynamic optimization framework for generative retrieval strategies. RAG-FGO formulates query rewriting as a non-differentiable black-box optimization problem in a mixed discrete-continuous space, and represents prompt templates and decoding parameters as adaptively optimizable query-rewriting agents. The framework performs global search to enable semantic jumps and structural reorganization that escape local optima, while applying local perturbations for fine-grained alignment and precise refinement. In addition, RAG-FGO introduces an elite-preserving memory pool that accumulates high-quality strategies across iterations, thereby mitigating the impact of stochasticity and noisy feedback on optimization stability. Experimental results on a diverse suite of benchmarks demonstrate the effectiveness and robustness of the proposed method, supporting its applicability to complex semantic retrieval tasks.

**Key findings**

- **Finding**: 六个 QA benchmark 上 GPT-4o-mini 的平均 F1 从直接检索的 47.6 升到 77.1；在同一 retriever 与 Gemma-2-27B 生成器下平均 F1 71.2，高于 AutoPrompt 58.6 与 RLPrompt 63.2。
- **Inference**: 在 HotpotQA 上优化出的改写策略迁移到 NQ、SQuAD、AmbigQA、StrategyQA 只掉 1.9–5.7 分，说明学到的是可跨任务复用的检索策略而非数据集过拟合。
- **Recommendation**: 调 RAG 时把提示模板与温度、top-p 当作同一个黑箱优化问题整体搜索，而不是分开手调，也别指望一次静态改写适配所有语义场景。

**Key figures**

*Framework - Conceptual illustration of the FGO-inspired search dynamics in RAG-FGO. Hyphae grow from low-efficiency (info-sparse) zones toward high-efficiency (info-rich) zones in the retrieval space. (i)*

![RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG - framework](res/2611.17788_framework.png)

*Result - Overview of the main components of RAG-FGO. (a) A query-rewriting agent consists of a prompt template and continuous decoding parameters. (b) Variation optimization evolves agents via local se*

![RAG-FGO: Dynamic Optimization of Query-Rewriting Agents for Generative RAG - result](res/2611.17788_result.png)

**Why this ranks #10**: 庆北大学、电子科技大学与同济大学把查询改写建模成离散提示模板与连续解码参数混合的非可微黑箱优化问题：全局搜索做语义跳跃、局部扰动做精修，再用精英保留记忆池抗噪与抗随机性。六个 QA benchmark、五个生成模型上宏平均 F1 达 77.1（GPT-4o-mini），在同 retriever 与生成器配置下平均 F1 71.2，比无梯度提示优化基线高出 7 分以上，是 llm_core 里少见的「检索策略可被优化」的完整证据。

---

## VLM 核心（多模态架构 / 理解 / 视频 / GUI agent） · `vlm_core` (5 papers)

本方向 5 篇。**文档与长上下文**是主线：DoubleTake 针对长文档问答里「检索到的页面其实含有充分证据、模型却仍然答错」这一现象，引入聚焦式视觉证据核验；ParseBench-2 指出文档解析的既有度量会给「改了重要事实」的输出打高分、给「保留语义」的改动扣分，因此提出按严重程度来评估解析结果。**空间与几何**：Zoom In, Scale Out 用一个极简测试——数码变焦，即裁剪再放大——检验度量深度模型是否真的在解相机几何，结论是它们把变焦误当成了相机靠近。**Agent 与视频**：Vision-as-a-Tool 把视觉能力从 agent 的内生感知里解耦成可显式调用的工具，理由是 Thinking-with-Images 把感知与执行架构耦合在一起会让 agent 的性能被内生感知的天花板钉死；Q-GAS 用可坐标查询的多分辨率三维特征网格把视频表示的构建时间压到秒级。

### 11. DoubleTake: Focused Verification of Visual Evidence for Long-Document Understanding

**arXiv**: [2611.17853](https://arxiv.org/abs/2611.17853) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, long-document-qa, focused-verification, training-free, frozen-backbone, visual-evidence, [unverified] | **Categories**: cs.CV | **Pages**: 6

**Authors**: Kejun Xue; Ang Li; Jinghua Tang; Xincheng Wang; Yongbin Gao; Yanghua Xiao; Zhijun Fang

**Affiliation**: [unverified]

**Abstract**

> In long-document question answering, a vision-language model can answer incorrectly even when the retrieved pages contain sufficient evidence. Rereading those pages with the original question gives the model little guidance about which fact to check. We introduce DoubleTake, a training-free framework for focused verification of visual evidence. An initial reading produces a candidate answer and a separate evidence record that guides retrieval for a second reading. A planner compares the two candidates and their supporting evidence to formulate a factual question. A verifier answers it from the source images without seeing either candidate or evidence record, and a reasoner uses this observation to resolve the original question. With a frozen Qwen3-VL-8B-Instruct backbone, DoubleTake achieves the highest overall accuracy among the evaluated methods on each of four benchmarks. With the same pages and number of model calls, asking a focused factual question yields higher accuracy on all four benchmarks than asking the original question again. Our code is available at https://github.com/small-code-cat/double_take.

**Key findings**

- **Finding**: 四个 benchmark 微平均准确率 66.76%，MDocAgent 65.16%、Base 60.13%；去掉核验环节降到 64.56%，去掉补读在 PaperTab 上从 56.23% 降到 52.16%。
- **Inference**: 只有两个候选之一正确时 DoubleTake 答对 391/591（66.2%），而始终选初读或补读分别只有 53.6% 与 46.4%，说明收益来自比较与核验而非重复阅读。
- **Recommendation**: 长文档问答里与其重问原问题，不如让规划器先写出一个可直接核对的聚焦事实问题，再让独立核验器只看页面回答。

**Key figures**

*Framework - Illustrative example. (a) Direct reading compares sales across years. (b) Rereading with the original question repeats the error. (c) DoubleTake uses the two readings to check the 2024 target*

![DoubleTake: Focused Verification of Visual Evidence for Long-Document Understanding - framework](res/2611.17853_framework.png)

*Result - DoubleTake connects evidence-guided dual reading with comparison-guided visual verification. All roles receive the original question. The first evidence record guides the second search. Both c*

![DoubleTake: Focused Verification of Visual Evidence for Long-Document Understanding - result](res/2611.17853_result.png)

**Why this ranks #11**: 全文未标注机构的 6 页论文提出免训练的 DoubleTake：冻结 Qwen3-VL-8B-Instruct，先读出候选答案与独立证据记录，再由规划器据此构造一个可直接从图上核对的事实问题，让核验器在看不到任何候选的前提下作答。四个 benchmark 共 4,816 道题的微平均准确率 66.76%，高于 MDocAgent 的 65.16% 与基线的 60.13%，且同样页面、同样调用次数下问聚焦事实优于重复原问题。

---

### 12. ParseBench-2: Severity-Aware Evaluation of Document Parsing

**arXiv**: [2611.17400](https://arxiv.org/abs/2611.17400) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, document-parsing, severity-aware-metric, benchmark, error-severity, metric-alignment, LlamaIndex | **Categories**: cs.CV | **Pages**: 59

**Authors**: Pierre-Loïc Doulcet; Boyang Zhang; Sebastián G. Acosta; Sacha Bron; Daniel B. Ospina; Antonio Jimeno Yepes; Nutchapol Dendumrongsup; Simon Suo

**Affiliation**: LlamaIndex

**Abstract**

> Document-parsing metrics can give high scores to outputs that change important facts and penalize changes that preserve meaning. People can often judge these consequences more easily than they can design a metric to measure them. We introduce a method for developing parsing metrics from severity policies that specify how each error type should affect the score. We express these policies through test scenarios that specify how a metric should behave. We then optimize the metric implementations against these fixed expectations, using coding agents to refine comparison rules, error detectors and weights under human review. This makes stated human priorities an explicit objective of metric design. We apply this method in ParseBench-2, a comprehensive document-parsing benchmark that combines broad capability coverage with metrics calibrated to error severity. It covers 4,317 pages across six dimensions of parsing quality: text, formatting, tables, charts, visual grounding, and forms. We use detailed annotations and targeted difficult cases to check for changed facts, broken structural relationships, and missing content. We take the lower of a parsing score that measures content recovery and a severity cap that penalizes detected errors, so recovering most of a page cannot hide a serious error. Across six severity test suites, our metrics more closely match the expert judgments expressed by the scenario targets than existing metrics and penalize at most 3.4% of the tested benign variations. We conduct a comprehensive evaluation spanning frontier vision-language models, specialized document parsers and open-weight systems, comparing their overall rankings, performance across parsing capabilities and tradeoffs between accuracy and cost.

**Key findings**

- **Finding**: 基准含 4,317 页、6 个维度、2,645 份源文档与 1,025 张带完整数据表的图表，评分取内容恢复分与严重度上限的较小值。
- **Inference**: 曾把数值单元格的改动当成普通改写时，45 张测试表里达到十分目标的只有 56%，修正比较规则后升到 98%，说明指标必须按错误严重度重写而非加权平均。
- **Recommendation**: 选文档解析系统要看按严重度加权的分数，并单独检查数值、表头关联与遗漏内容，别被整体内容恢复率掩盖。

**Key figures**

*Framework - ParseBench-2 aligns parsing scores with human judgments of error severity.*

![ParseBench-2: Severity-Aware Evaluation of Document Parsing - framework](res/2611.17400_framework.png)

*Result - Experts express their severity policy through test scenarios, and we refine parsing metrics to follow that policy (Sections 2.1 to 2.3).*

![ParseBench-2: Severity-Aware Evaluation of Document Parsing - result](res/2611.17400_result.png)

**Why this ranks #12**: LlamaIndex 的 ParseBench-2 覆盖 4,317 页、文本/格式/表格/图表/视觉定位/表单 6 个解析维度，来自 2,645 份源文档、13 个集合，1,025 张图表都附完整数据表。指标本身由专家严重度策略经编码 agent 反复迭代校准，评分取内容恢复分与严重度上限的较小值，六个严重度测试套件上比既有指标更贴近专家判断，同时最多只惩罚 3.4% 的良性变体。

---

### 13. Towards Seconds-level Video Representation: Quadratically Gated Feature Grid with Adaptive, Prediction-free Sampling

**arXiv**: [2611.17786](https://arxiv.org/abs/2611.17786) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, video-representation, implicit-neural-representation, feature-grid, quadratic-gating, fast-decoding, Harbin Institute of Technology | **Categories**: cs.AI, cs.CV | **Pages**: 13

**Authors**: Tie-Yun Li; Hao-Ran Wang; Chao Wang; Zhiyong Yin; Yiming Xu; Zhenwei Cai; Li Li; Rongzhi Lin; Feng-Lei Fan

**Affiliation**: Harbin Institute of Technology; City University of Hong Kong; China Construction Third Engineering Bureau (Shenzhen) Co., Ltd.; University of Science and Technology of China

**Abstract**

> Implicit neural video representations are notoriously slow to build, which does not cross the basic practical threshold for most industrial applications. Here, we present Q-GAS, a coordinate-queryable video representation that couples multi-resolution explicit 3D feature grids with a compact SwiGLU-style quadratic-gating (QG) decoder and an error-aware, prediction-free sampler. The explicit grids avoid hash-collision coefficient sharing at the cost of modestly higher storage yet greatly boost the expressive capacity; the QG decoder introduces low-rank local second-order interactions to improve the nonlinear feature response. During fitting, a global error map periodically refreshes a high-error pool, and each batch mixes pool samples with uniform samples, which is free from the auxiliary model to predict difficult samples, thereby further escalating the efficiency. On UVG Beauty/Bosphorus/Jockey, Q-GAS fits and quantizes under 50 s on one RTX PRO 6000, decodes at over 370 FPS with mixed precision and about 146 FPS in FP32. In our PyTorch implementation, Q-GAS trains and quantizes 5.5-7.2 times faster than the evaluated Instant-NGP baseline and 19-28 times faster than RNeRV. Under a 90 s budget, it improves PSNR/MS-SSIM/LPIPS over the evaluated NeRV-family pipelines at comparable BPP over the measured overlap. We have shared our code at https://github.com/MillenRosen/Q-GAS for readers' free use.

**Key findings**

- **Finding**: 约 3M 参数档下 Q-GAS 在 Beauty 上 PSNR 32.04、耗时 33.94 秒、418.27 FPS，而 Instant-NGP 为 30.65、203.68 秒、18.37 FPS，RNeRV 单是拟合加量化就要 958.65 秒。
- **Inference**: 训练加量化耗时比 Instant-NGP 快 5.5–7.2 倍、比 RNeRV 快 19–28 倍，加速来自显式网格加二次门控的表达力而非少算了样本。
- **Recommendation**: 做实时视频重建或播放时优先试显式网格加误差感知采样这类秒级拟合方案，并按 90 秒预算与 NeRV 系管线对齐后再比较 PSNR 与感知指标。

**Key figures**

*Framework - An overview of Q-GAS. Multi-Resolution 3D Feature Grids: At each coordinate (x, y, t), trilinear interpolation retrieves features. The schematic illustrates the multiscale construction. QG Dec*

![Towards Seconds-level Video Representation: Quadratically Gated Feature Grid with Adaptive, Prediction-free Sampling - framework](res/2611.17786_framework.png)

*Result - Explicit and hash-constrained 3D feature grids at the same resolution and feature dimension. Both use trilinear interpolation. Feature grid: Each vertex has an independent feature vector. Hash*

![Towards Seconds-level Video Representation: Quadratically Gated Feature Grid with Adaptive, Prediction-free Sampling - result](res/2611.17786_result.png)

**Why this ranks #13**: 哈尔滨工业大学、香港城市大学等用多分辨率显式 3D 特征网格配 SwiGLU 式二次门控解码器和免辅助模型预测的误差感知采样器，做坐标可查询的视频隐式表示。在 UVG Beauty/Bosphorus/Jockey 的完整 600 帧、1920×1080 序列上，单张 RTX PRO 6000 拟合加量化不到 50 秒、混合精度解码超过 370 FPS、FP32 约 146 FPS，是把视频表征拉进秒级预算的一篇。

---

### 14. Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding

**arXiv**: [2611.17797](https://arxiv.org/abs/2611.17797) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, vision-as-a-tool, agentic-coding, tool-use, modular-perception, text-only-agent, Peking University | **Categories**: cs.AI, cs.CV | **Pages**: 27

**Authors**: Haolin Yang; Wenshan Wu; Jin Jiang; Yu Cheng; Yan Xia; Ting Song; Yangyu Huang; Zhiliang Peng; Wenhui Wang; Hangbo Bao; Yuzhe Zhang; Wen-Da Wei

**Affiliation**: Peking University; Microsoft Research; University of Edinburgh; Nanjing University

**Abstract**

> Multimodal agentic coding requires robust visual reasoning to analyze observations and evaluate generated artifacts. Current frameworks largely rely on a Thinking-with-Images paradigm, where agents depend on their intrinsic vision to execute visually grounded tasks. However, this architectural coupling introduces a fundamental bottleneck. Agent performance remains strictly bounded by internal perceptual limitations. Furthermore, text-only agents lack native perception. Without specialized tools, they cannot perform visual reasoning. To overcome these constraints, we introduce the Vision-as-a-Tool (VaaT) paradigm. Prior visual tool-use merely manipulates images for an agent's intrinsic vision to read. In contrast, VaaT reframes general-purpose multimodal large language models (MLLMs) as callable external utilities. As a result, text-only agents can completely offload visual reasoning during agentic execution. Meanwhile, vision-capable agents can dynamically augment their native perception on demand. We instantiate this paradigm in VHarness, a unified framework driven by five atomic actions. We comprehensively evaluate VHarness across Image-to-HTML, Image-to-SVG, and Image-to-3D generation tasks. Experimental results demonstrate that VHarness consistently improves visual fidelity and geometric accuracy across both text-only and multimodal coding agents. These findings highlight that modularizing visual reasoning into callable utilities provides a flexible and scalable foundation for future agentic coding systems.

**Key findings**

- **Finding**: Image-to-SVG 消融中 SigLIP2 从 0.7368 升到 0.7529、LPIPS 从 0.0572 降到 0.0473、Edge F1 从 0.8310 升到 0.8546；纯文本的 GLM-5.2 因此能做出视觉落地任务。
- **Inference**: Image-to-3D 上换成自由格式 MLLM 接口仍明显落后五个原子动作（SigLIP2 0.6677 对 0.7212，Chamfer 0.0070 对 0.0035），说明接口粒度本身决定效果。
- **Recommendation**: 做视觉 coding agent 时把外置视觉能力拆成可组合的原子动作，而不是给一个自由问答式接口，否则收益会打折。

**Key figures**

*Framework - Overview of VHarness, an instantiation of the Vision-as-a-Tool (VaaT) paradigm. Given a target visual input across*

![Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding - framework](res/2611.17797_framework.png)

*Result - Qualitative comparisons across Image-to-HTML, Image-to-SVG, and Image-to-3D tasks. From left to right, we show the*

![Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding - result](res/2611.17797_result.png)

**Why this ranks #14**: 北京大学与微软研究院等提出 Vision-as-a-Tool：把通用 MLLM 重构为 coding agent 可调用的外部视觉工具，用 transcribe、grep、inspect、align、diff 五个原子动作覆盖 Image-to-HTML、Image-to-SVG、Image-to-3D 三类任务，纯文本 agent 借此完全外放视觉推理，多模态 agent 则可按需增强自身感知，是把感知能力模块化后交给 agent 调用的少见范式。

---

### 15. Zoom In, Scale Out: Metric Depth Models Mistake Digital Zoom for Moving Closer

**arXiv**: [2611.17903](https://arxiv.org/abs/2611.17903) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `vlm_core` | **Tags**: LLM-VLM, metric-depth, digital-zoom, focal-length-estimation, label-free-correction, depth-consistency, Daffodil International University | **Categories**: cs.CV | **Pages**: 22

**Authors**: Rabeya Noor; Khandoker Nosiba Arifin

**Affiliation**: Daffodil International University

**Abstract**

> Many new AI models estimate how far away things are, in metres, from a single photo. To do this they must also work out what camera took the photo. We check whether they really do with a simple test: digital zoom, that is, cropping a photo and enlarging the crop back to full size. Zooming moves nothing in the scene, so a correct model should give the same distance for every point still in the picture. The test is free, exact and needs no labels. Two numbers describe a model's reaction: its depth changes like $s^{-α}$ (ideal $α=0$) and its focal-length estimate like $s^β$ (ideal $β=1$), for zoom factor $s$. On 800 images from KITTI, NYUv2 and DIODE, the widely used Depth Anything V2 has $α=0.95$: it treats a zoomed photo almost as if the camera had moved closer, because it judges distance mainly from how large things look. Models that also predict the camera remove only part of this error ($α\approx0.31$-$0.36$), because their focal estimate grows too little. Given the true camera, Depth Pro and DA3-Nested keep their depth ($α\approx0$), so the error lies in their camera estimate. The reason: a zoomed photo is, pixel for pixel, a normal photo of a scene squashed in depth, so size alone cannot tell the two apart, and a focal estimator trained by regression stays close to the cameras it saw in training. Undoing this needs no labels or training and makes Depth Pro pass the test ($α=0.04$) at almost no cost on normal photos. Controls, including a real optical zoom lens, rule out blur and resizing artefacts. Finally, label-free fine-tuning for self-consistency lowers $α$ to 0.05 on KITTI and 0.07 on NYUv2 once a "blurry means zoomed" shortcut is removed; we report what this costs on normal and unseen photos.

**Key findings**

- **Finding**: Depth Anything V2 的 α=0.95、ZoeDepth 0.61，而会预测相机的 Depth Pro 0.31、MoGe-2 0.36、UniDepthV2 0.34，给出真实相机的 Metric3D v2-S 为 −0.07。
- **Inference**: 模糊对照只让 DA-V2-S 的深度变动 1.3%，说明误差来自「数字变焦等于场景被压缩」这条提示，而不是分辨率或重采样损失。
- **Recommendation**: 用度量深度做测量或重建前先按预测焦距把数字变焦的尺度换算回去，并用免标签的自一致性微调进一步校正 α。

**Key figures**

*Framework - A KITTI image at 1×, 2×, 3× digital zoom, one colour scale (metres); the number is the median depth inside the 3× crop, the same points in every column. Depth Anything V2 moves the scene clo*

![Zoom In, Scale Out: Metric Depth Models Mistake Digital Zoom for Moving Closer - framework](res/2611.17903_framework.png)

*Result - Depth (left) and predicted focal (right) of the same pixels as a function of the zoom factor, median over images. Dashed: the law; dotted: apparent size only.*

![Zoom In, Scale Out: Metric Depth Models Mistake Digital Zoom for Moving Closer - result](res/2611.17903_result.png)

**Why this ranks #15**: 达卡大学（Daffodil International University）给度量深度模型设计了一个免标签体检：把照片裁剪放大做数字变焦，场景没动，正确模型应对图内每个点给出同一距离。在 KITTI、NYUv2、DIODE 每个模型 800 张图上，Depth Anything V2 的深度指数 α=0.95（理想 0），几乎把裁剪当成相机靠近；会预测相机的模型也只有 0.31–0.36，问题出在焦距估计（β 理想为 1）。

---

## LLM / VLM 的 RL 与偏好优化 · `llm_vlm_rl` (5 papers)

本方向 5 篇，全部落在**可验证奖励**这条路线上，而且都不依赖人工偏好数据。See Every Block Once 指出 masked diffusion LM 的 log-likelihood 无法直接计算，后训练只能依赖 ELBO 代理目标，现有工作用蒙特卡洛逐块估计这个目标；它的做法是逐块方差缩减，让策略梯度一次前向就能算。Benchmarks Don't Talk Back 训练一种它称为「辩证能力」的东西：模型自己陈述立场、自己生成最强的反方陈词、自己裁定，然后用同一个可验证检查同时给答案和裁定打分，因此全程不需要奖励模型、偏好数据或人工标注。Verifiable pXRD 把晶体结构测定写成可验证的 agentic 搜索问题——候选结构可以被物理判据验证。AutoRL 用感知器、提案者、编排者三个 agentic 角色自动化 RL 训练的过程级监督。PaperCritic 则把奖励函数从偏好数据换成了任务定义本身——精确率与召回率的 F1。

### 16. Benchmarks Don't Talk Back: Learning Through Self-Disagreement

**arXiv**: [2611.17563](https://arxiv.org/abs/2611.17563) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, self-disagreement, dialectical-competence, rlvr, grpo, capitulation, Microsoft Research | **Categories**: cs.AI, cs.CL, cs.LG | **Pages**: 34

**Authors**: Soheil Abbasloo; Peng Cheng

**Affiliation**: Microsoft Research

**Abstract**

> A benchmark usually measures a language model alone with a question, and deployment rarely looks like that: answers get contested, and models give up correct ones under counter-reasoning that is itself wrong. We show that what fails there is not a shortfall of accuracy but a capability in its own right -- knowing when to hold a position and when to yield to a better one -- which we call dialectical competence. It stands on first-answer accuracy without following from it: a model can be made materially better at answering and no better at this, and training for accuracy alone can drift against it. Nor can it be bought at inference, by self-reflection or by sampling more. Taking a cue from the dialectical tradition in philosophy, in which productive opposition arises within a position rather than being imposed on it from outside, we hypothesize that this capability can be trained from opposition the model supplies itself. It states a position, generates the strongest case against that position -- its antithesis -- rules on whether the case stands, and is trained on that ruling, with no second model at training or at deployment. We call this learning through Self-Disagreement: reinforcement learning from verifiable rewards throughout, where the same check that scores an answer against its reference scores the ruling too, so no reward model, no preference data and no human annotation enter anywhere. The capability is trained rather than elicited: weak in the base model, it arrives with the reward, is not paid for out of first-answer accuracy, and holds against challengers the model never trained against, including ones stronger than itself. The opposition a model needs in order to improve, it turns out, need not come from outside it.

**Key findings**

- **Finding**: D-probe 用 327 道题 × 17 个挑战者测「被质疑后是否守住正确回答」，基础模型 Qwen3-8B 守住率只有 53.3%、让步率高达 84.1%，Self-Disagreement 训练后守住率升到 88.9%、让步率降到 53.3%（Gemma-2 9B 守住率 25.1%→89.5%）。
- **Inference**: 奖励消融里各臂综合准确率跨度 12.23 pp，而首答准确率跨度只有 2.75 pp（差 4.4 倍），说明学到的是「分辨对错挑战」的独立能力，而不是答案变准的副产品。
- **Recommendation**: 需要抗辩能力的助手可直接复用该配方——反题不进训练轨迹、格式门控失败即置地板分、capitulation 与 stubbornness 必须对称惩罚，但不必另配奖励模型或偏好数据。

**Key figures**

*Framework - Answering better does not buy the ca- pability. Share of the base model’s correct an- swers each arm gives up under challenge, one po- sition per challenger; each trained arm is the mean of*

![Benchmarks Don't Talk Back: Learning Through Self-Disagreement - framework](res/2611.17563_framework.png)

*Result - Buying accuracy is not buying the ca- pability. SuperGPQA: each arm sits at its thesis accuracy (x) against how often it gave up a cor- rect answer under challenge (y, inverted), so bet- ter*

![Benchmarks Don't Talk Back: Learning Through Self-Disagreement - result](res/2611.17563_result.png)

**Why this ranks #16**: 把 RLVR 的验证器从「只判答案对错」扩到「也判裁决对错」：单策略依次扮演正题 T、反题 A、综合裁决 S，反题只采样不入训练轨迹，只有答与裁两轮拿奖励，回报里 capitulation 与 stubbornness 各罚 0.5、格式解析失败直接压到 Rfloor=-0.75，算法本身仍是标准 GRPO。在 327 题 × 17 挑战者的 D-probe 上，Qwen3-8B 九个公开基准的平均综合准确率（synthesis accuracy）从 50.0% 升到 55.9%（+5.90 pp），Gemma-2 9B 从 19.9% 升到 37.8%，全程没有奖励模型、偏好数据或人工标注，因此属于 RLVR 方向的核心工作。

---

### 17. See Every Block Once: Variance-Reduced Post-Training for Masked Diffusion Language Models

**arXiv**: [2611.17754](https://arxiv.org/abs/2611.17754) | **Score**: 8.7 (relevance 9 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, masked-diffusion, monte-carlo, variance-reduction, blockwise-generation, grpo, Kyoto University | **Categories**: cs.CL | **Pages**: 22

**Authors**: Yunzhen He; Hiroaki Yamagiwa; Hidetoshi Shimodaira

**Affiliation**: Kyoto University; SB Intuitions; RIKEN AIP

**Abstract**

> Policy gradient methods are widely used to align large language model outputs with human preferences, but the log-likelihoods they require cannot be directly computed in Masked Diffusion Language Models (MDLMs). MDLM post-training therefore relies on a surrogate objective based on the Evidence Lower Bound (ELBO), and recent work estimates a blockwise variant of this objective via Monte Carlo methods to support blockwise generation. However, existing estimation schemes randomly sample the block index, so they may evaluate the same block more than once and leave some blocks unevaluated. This introduces variance arising from block selection into the estimates. In this work, we propose a full-block estimator that evaluates every block exactly once and averages the results. We theoretically show that the proposed estimator remains unbiased while eliminating the between-group variance arising from block selection, thereby achieving lower variance than the baseline for the same sample size. In experiments on five benchmarks spanning mathematics, planning, and coding, our method achieves the highest accuracy on four benchmarks and outperforms the random block sampling baseline by an average of 12.79 points.

**Key findings**

- **Finding**: 随机抽 block 时 K=C=4 有 0.91 的概率漏掉整块；全块估计在 K=4 就拿到 Spearman ρ=0.878、RMSE=50.1，而随机采样只有 ρ=0.602、RMSE=136.0，约等于随机采样 K≈32 的估计质量。
- **Inference**: 五个数据集上的方差比 Var[L̂Full]/Var[L̂Rand] 仅 0.076–0.122，但策略梯度层面的方差比仍高达 0.79–0.96，说明精度收益主要来自「每步给每个 block 都发学习信号」而不只是梯度更稳。
- **Recommendation**: 在 MDLM 上做 GRPO 后训练时，可直接把蒙特卡洛样本数设为 block 数 C 并逐块求平均，这是零额外模型成本的可插拔改动；作者提示 C 变大时并行实现会线性占用显存，可改用顺序累加梯度。

**Key figures**

*Framework - Comparison of block selection in Monte Carlo estimation of the blockwise surrogate objective. For each Monte Carlo sample index k, a block b is sam- pled, and the corresponding set of token*

![See Every Block Once: Variance-Reduced Post-Training for Masked Diffusion Language Models - framework](res/2611.17754_framework.png)

*Result - Mask state during the generation of block b = 1 for a response o of length L = 12 (C = 3, B = 4). Block B0 is considered already generated, so its original tokens are retained. In this examp*

![See Every Block Once: Variance-Reduced Post-Training for Masked Diffusion Language Models - result](res/2611.17754_result.png)

**Why this ranks #17**: 针对掩码扩散语言模型（MDLM）后训练里 blockwise 代理目标的蒙特卡洛估计器做改造：京都大学、SB Intuitions 与 RIKEN AIP 把随机抽 block 换成「每个 block 恰好评一次」的全块估计，代理目标与 GRPO 策略更新完全不动。K=C=4 时随机采样至少漏掉一个 block 的概率高达 0.91，全块估计把估计方差比压到 0.076–0.122（约为随机采样的十分之一），在 GSM8K/MATH-500/Countdown/Sudoku/HumanEval 五个基准上平均比随机采样高 12.79 分、比最强基线 SPG 高 5.05 分。

---

### 18. Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents

**arXiv**: [2611.17539](https://arxiv.org/abs/2611.17539) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, pxrd, crystal-structure, verifiable-reward, agent-adaptation, inference-time-scaling, Stanford University | **Categories**: cs.AI | **Pages**: 49

**Authors**: Samuel Chen; Jiaru Bai; Austin Henry Cheng; Varinia Bernales; Alán Aspuru-Guzik

**Affiliation**: Stanford University; University of Toronto; Vector Institute for Artificial Intelligence; Acceleration Consortium; Canadian Institute for Advanced Research (CIFAR); NVIDIA

**Abstract**

> Autonomous crystal-structure determination from powder X-ray diffraction (pXRD) remains a key bottleneck for self-driving materials laboratories. We formulate the task of pXRD structure determination as a verifiable agentic search problem: candidate structures can be assessed during inference through forward-simulated profile agreement and during evaluation through structural matching to a known reference. To benchmark progress, we introduce pXRD-Bench, a suite of 200 simulated single-phase problems spanning in-distribution structure determination, challenging and polymorphic structures, and controlled compositional and topological distribution shifts. Agent adaptation raises selected structural recovery from 27% to 69%, with further gains from repeated sampling and verifier-guided inference-time scaling. We extend this approach to experimental multiphase pXRD through a reflexive evolution framework that learns from self-generated synthetic problems. A replaceable laboratory specification defines the sample family and measurement conditions. An evolver agent uses the known generating structures and measurement parameters to diagnose solver failures and develop persistent guidance and executable tools, which are then provided to agents on measured patterns. This supplies verifiable training experience without requiring a collection of solved experimental measurements. On 15 measured patterns from solid-state synthesis, the evolved package improves average profile agreement and transfers an analogue-substitution procedure that recovers a phase whose structure is absent from the supplied reference library. These results demonstrate how learning from verifiable synthetic experience can improve agentic characterization of experimental samples whose structures are not known in advance.

**Key findings**

- **Finding**: pXRD-Bench 含 200 道单相题（pXRD-100 与 pXRD-ood 各 100），已有专用求解器最好也只有 32.0%（PXRDGen，pass@1），而 adapted-codex 选中的结构精确匹配率是 69.0%，pXRD-ood 上为 61.0%。
- **Inference**: 学习型适配的收益来自验证器引导的自我进化——能力包只有 139 词的技能加一个 DICVOL 适配器，却把准确率从 57.0% 推到 69.0%，说明对齐验证器评分比堆砌工具更关键。
- **Recommendation**: 任何「能算出物理残差」的科学领域都可照搬该思路：用 Rwp 做推理期验证器时，LLM 验证器判定 155/200（77.5%）正确，优于固定阈值 Rwp≤6.66% 的 149/200（74.5%），并应按覆盖率定向续跑而非盲目重复采样。

**Key figures**

*Framework - pXRD structure determination as a verifiable inverse problem. Ground truth: pXRD-Bench case pxrd100-rep-010. Proposed: pxrd-codex selected.cif. Structures rendered with Crystal Toolkit [Hort*

![Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents - framework](res/2611.17539_framework.png)

*Result - Repeated-sampling results on pXRD-Bench-20. Panels (a)–(c) show candidate-set exact StructureMatcher recovery for pxrd-codex Sol, pxrd-codex Luna, and adapted-codex Sol, respec- tively. A co*

![Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents - result](res/2611.17539_result.png)

**Why this ranks #18**: 斯坦福大学与多伦多大学等把粉末 X 射线衍射（pXRD）结构测定写成可验证的智能体搜索问题：推理期用前向模拟的 Rwp 残差评估候选结构、评测期用 pymatgen StructureMatcher 与真值比对，这个验证器同时充当训练信号与推理期筛选依据，于是可以做奖励式爬坡。在 200 题的 pXRD-Bench 上，无工具的 GPT-5.6 Sol 只有 27.0%，加材料科学编码智能体升到 52.0%，接入 GSAS-II/DICVOL 升到 57.0%，再用 50 题独立课程做可验证自进化得到 69.0%，属于典型的 RLVR 路线。

---

### 19. AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning

**arXiv**: [2611.17790](https://arxiv.org/abs/2611.17790) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, autonomous-rl, multi-agent, training-supervision, reward-repair, checkpoint-resume, Meituan | **Categories**: cs.AI, cs.LG | **Pages**: 23

**Authors**: Simon Tang; Wenjie Shi; Yongjing Yin; Keheng Wang; Jialin Liu; Zheng Zhang; Linvo Lin; Xiangyuan Xue; Kan Ren; Jingang Wang; Xunliang Cai

**Affiliation**: Meituan; The Chinese University of Hong Kong; ShanghaiTech University; Fudan University

**Abstract**

> Recursive self-improvement (RSI) is one of the most promising paths toward an AI singularity for superintelligence. Achieving this vision requires AI systems to undertake the full training pipeline for iterative improvement. Reinforcement learning (RL) plays an essential role in this cycle to improve model capabilities and generalization, yet automating RL remains difficult due to unstable training dynamics and the need for sustained supervision. We introduce AutoRL, a multi-agent system for automating RL training, as a cornerstone for future RSI. Different from conducting research by end-to-end complete experiments, AutoRL monitors the evolving training state and integrates process-level supervision and research into an ongoing RL training, following the practical workflow of an RL researcher. Specifically, AutoRL consists of three RL-specific agentic roles. Perceptors track training dynamics, rollouts, evaluation, and efficiency, triggering deliberation when they detect anomalies, degradation, or stagnation. Three complementary Proposers diagnose problems and refine candidate interventions through shared evidence and checks. The Orchestrator reviews their recommendation and applies approved changes through online hot updates or checkpoint-based resumption. Experiments on Qwen3 and LongCat-Flash-Lite demonstrate the superiority of AutoRL over static RL recipes and a general agent. The research records show that existing agents can handle unattended RL supervision and dynamic adjustment. The difficulty for future RSI lies in developing fundamental methods that are valuable for resource-consuming validation.

**Key findings**

- **Finding**: Qwen3-4B 上 AutoRL 在全部九个基准超过静态 GRPO 配方：AIME 2024 由 46.67% 升到 66.67%（+20.00 pp），HMMT 2025 由 20.00% 升到 31.67%，MBPP 由 63.55% 升到 65.25%，1.7B 规模上同样全项领先。
- **Inference**: LongCat-Flash-Lite 上 AutoRL 在 64 步内从 65.53% 升到 73.16%，而静态配方同期跌到 56.05%，差距 17.11 pp；六次热更新里有四次在修评分器（选项映射、多值匹配、LaTeX 解析、空白与单位），说明瓶颈常在奖励实现而非算法。
- **Recommendation**: 要做长时无人值守 RL，应先搭好「感知—诊断—提案—CPU 校验—热更新/检查点恢复」这条链；编码智能体实验里 14.7 天训练经历 11 次运行时故障后仍把 SWE 相关任务 pass@1 从 52.29% 推到 65.13%。

**Key figures**

*Framework - AutoRL: autonomous RL supervision and research. Right: AutoRL continually adopts interventions, such as fixes and adjustments, to sustain gains over a static recipe.*

![AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning - framework](res/2611.17790_framework.png)

*Result - Framework of AutoRL. Four Perceptors monitor training and diagnose problems. Three specialized Proposers discuss candidates, review evidence, and perform CPU-only checks to guide revision an*

![AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning - result](res/2611.17790_result.png)

**Why this ranks #19**: 美团联合香港中文大学、上海科技大学与复旦大学提出 AutoRL，用四个感知器（梯度/rollout/评测/效率）、三个提案器（Tuner/Innovator/Reviewer）和一个编排器接管 GRPO 训练的过程级监督：提案器在至多五轮辩论里用 Borda 打分选出最多两个候选，编排器再决定 HOT 在线热更新还是 COLD 从检查点恢复。Qwen3-4B 上九个基准全面超过静态 GRPO 配方，AIME 2024 由 46.67% 升到 66.67%（+20.00 pp），是把 RL 训练本身当作智能体 RL 任务的代表作。

---

### 20. PaperCritic: Training AI Reviewers to Assess the Soundness of Papers

**arXiv**: [2611.17834](https://arxiv.org/abs/2611.17834) | **Score**: 8.0 (relevance 8 x 0.7 + quality 8 x 0.3) | **Direction**: `llm_vlm_rl` | **Tags**: LLM-VLM, paper-review, reward-modeling, grpo, f1-reward, review-points, KAIST AI | **Categories**: cs.CL | **Pages**: 26

**Authors**: Hyun Ryu; Ji Yong Cho; Eunho Yang; Moontae Lee; June Yong Yang; Sean Welleck; Carolyn Rose

**Affiliation**: KAIST AI; Carnegie Mellon University Language Technologies Institute; LG AI Research

**Abstract**

> As AI conference submissions grow rapidly, AI reviewers are being considered as an alternative. However, simply imitating human reviewing is problematic because reviewing serves multiple purposes, including evaluating papers' soundness, interestingness, and clarity, the last two of which are subjective. In this work, we focus solely on evaluating soundness, the most important and objective criterion, and define the learning objective as jointly maximizing (1) precision, based on the soundness and substantiveness of review points, and (2) recall, the coverage of high-quality reference review points. Under this problem formulation, we construct a quality-labeled review point dataset, PaperSound-23K, using 1K ICLR submissions and 23K human-written and LLM-generated review points. Using this dataset, we train an AI reviewer model, PaperCritic, through reinforcement learning with the F1 score of precision and recall as the reward. Our experiments show that PaperCritic outperforms frontier models and models trained with other AI reviewer training methods on an in-domain test set. Surprisingly, learning to review ICLR submissions also transfers to reviewing Nature-family papers and even to out-of-domain reviewing tasks (e.g., code review, legal contract review, and feedback on story writing).

**Key findings**

- **Finding**: PaperSound-23K 取 1K 篇 ICLR 投稿中的 989 篇论文、23,215 个审查点（人均 23.47±6.95），其中 62.4% 来自人类评审，人机一致性 0.624 已高于人人一致性 0.597。
- **Inference**: 奖励三件套缺一不可——去掉匹配器召回掉到 10.3（F1 13.2），去掉 soundness 奖励模型精确率掉到 13.1（F1 17.6），把精确率换成基于匹配的版本则 F1 只剩 25.7。
- **Recommendation**: 用 F1 型密集奖励做领域审查时，应分别建「内容正确性」与「实质重要性」两个奖励模型并保留覆盖率匹配器；改用 Gemini 3.8 Flash 复评时 PaperCritic-4B 仍以 44.4 F1 领先 DeepSeek-V4-Flash-0731 的 33.3。

**Key figures**

*Framework - Comparison of paper soundness assess- ments with conventional holistic review-and-score generation. Conventional AI reviewers are trained us- ing holistic review similarity or preference and*

![PaperCritic: Training AI Reviewers to Assess the Soundness of Papers - framework](res/2611.17834_framework.png)

*Result - An overview of the PaperCritic training framework. SFT uses sound and substantive reference points. Online RL maximizes a review-level F1 reward, combining precision estimated by soundness a*

![PaperCritic: Training AI Reviewers to Assess the Soundness of Papers - result](res/2611.17834_result.png)

**Why this ranks #20**: 把 AI 审稿目标从「模仿人类整篇评审」改成「最大化审查点的精确率与召回率 F1」：SFT 后用两个奖励模型分别评 soundness 与 substantiveness 估计精确率、用 LLM 匹配器算参考点覆盖度估计召回，合成整篇评审级的 F1 奖励交给 GRPO 优化，奖励由人类评审点标注驱动因而属 RLHF 路线。PaperSound-23K 覆盖 989 篇论文、23,215 个带质量标签的审查点，PaperCritic-4B 的 F1 达 45.1，比最强 4B 训练基线高 21.4 pp，并泛化到四个域外审稿任务。

---

## Footer

- Total papers reviewed across all 4 axes: 48
- llm_vlm axis final count: 20
- Wild-cards in this axis: 0
- Figure assets: 2026-11-16/res/

Generated by `mine-arxiv-daily-digest` skill. Sister file: `2026-11-16_llm_vlm_entry.md`.
