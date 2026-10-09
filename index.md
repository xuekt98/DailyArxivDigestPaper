# ArXiv 论文日报索引

由 `mine-arxiv-daily-digest` skill 每日生成。每条记录包含当天各研究线的论文数，
以及当天最值得读的 3 篇。

**统计口径**：每次运行扫描 arXiv 的 7 个分类（cs.CV / cs.SD / eess.AS / cs.CL /
cs.AI / cs.RO / cs.LG），按 5 条研究线各出 10 篇排名报告。

## 目录

| 日期 | 扫描量 | AIGC 视觉 | AIGC 音频 | 语音 LM | 具身/世界模型 | 强化学习 | 当天最值得读 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [2026-10-09](daily_arxiv_digest/2026_10/2026-10-09/) | 643 | 10 | 10 | 10 | 10 | 10 | [聚合准确率掩盖成对漂移](https://arxiv.org/abs/2610.11196) · [因果视频扩散不需要双向教师](https://arxiv.org/abs/2610.11479) · [双工智能体的异步委派范式](https://arxiv.org/abs/2610.11299) |
| [2026-10-08](daily_arxiv_digest/2026_10/2026-10-08/) | 580 | 10 | 10 | 10 | 10 | 10 | [SGF+ 梯度负对齐（+ 实时音视频 26fps）](https://arxiv.org/abs/2610.10429) · [预测的未来不足以控制](https://arxiv.org/abs/2610.09309) · [BoT-GRPO 不要价值网络](https://arxiv.org/abs/2610.09804) |
| [2026-10-07](daily_arxiv_digest/2026_10/2026-10-07/) | 531 | 10 | 10 | 10 | 10 | 10 | [World Models' Last Exam 实测物理一致性](https://arxiv.org/abs/2610.08791) · [QF3 首个从零训练人形策略的离策略流 RL](https://arxiv.org/abs/2610.08789) · [PERSIST 记忆要区分「原本」与「现在」](https://arxiv.org/abs/2610.07725) |
| [2026-10-06](daily_arxiv_digest/2026_10/2026-10-06/) | 879 | 10 | 10 | 10 | 10 | 10 | [EvoMem-VLA 记忆存错了东西](https://arxiv.org/abs/2610.05418) · [H-JEPA 分层世界模型 18%→73%](https://arxiv.org/abs/2610.06805) · [S2PD 物理一致性来自串行深度](https://arxiv.org/abs/2610.06847) |
| [2026-10-05](daily_arxiv_digest/2026_10/2026-10-05/) | 648 | 10 | 10 | 10 | 10 | 10 | [ID-Forcing (长视频 KV-provenance)](https://arxiv.org/abs/2610.03120) · [JEPA 可规划性诊断](https://arxiv.org/abs/2610.03137) · [AURAL 隐式推理降延迟 11.8x](https://arxiv.org/abs/2610.01560) |

---

## 2026-10-09

- **arXiv 批次窗口**：2026-10-08 UTC（截至 2026-10-09 17:00 CST，当天批次尚未发布）
- **扫描**：643 篇去重论文（cs.LG 230 / cs.AI 237 / cs.CV 184 / cs.CL 119 / cs.RO 86 /
  cs.SD 18 / eess.AS 14，其余为跨分类重复）
- **全文精读**：50 篇，抽取作者机构与 92 张论文原图
- **Wild-card**：本批 6 篇（集中在 aigc_audio 与 rl），**audio_lm 零 wild-card**——三天来首次

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-09/2026-10-09_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[Selective Listening: Mechanism-Guided Control of Audio Influence in Large Audio-Language Models](https://arxiv.org/abs/2610.11196)**（audio_lm #2）
   — 本批方法论价值最高的一篇，也是本项目日报「指标系统性漏掉真实失效」这条线索的**第三例**
   （前两例：10-06 的 Mind the Execution Gap、10-07 的 World Models' Last Exam）。
   任务无关的音频在**不需要听的时候**仍会改变 LALM 的文本推理决策——模型在偷听。
   关键在于：**聚合准确率完全掩盖了这种成对漂移**，因为音频带来的修复与损害互相抵消，
   净值不变但逐样本行为已经改变。作者用成对漂移分析定位出架构特定、可干预的**晚期音频通路**。
   这比前两例更进一步：前两例是「指标测错了东西」，这一例是「指标测对了总量却漏掉了行为改变」。

2. **[Conditional Residual Prediction: Improving Autoregressive Video Diffusion without a Bidirectional Teacher](https://arxiv.org/abs/2610.11479)**（aigc_visual #1）
   — 质疑的是领域默认路径而非某个模型。因果视频扩散适合流式/交互/长视频，
   但标准训练下质量常低于**同规模**双向模型；既有做法多是初始化自或蒸馏一个预训练双向教师，
   这篇改为直接训练因果模型。「同规模因果不如双向」常被归因于因果结构的信息损失，
   若条件残差能在不引入教师的情况下补上差距，说明**差距来自训练信号而非架构上限**——
   这会改变大量视频生成工作的基线设定。

3. **[DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration](https://arxiv.org/abs/2610.11299)**（audio_lm #1）
   — **三天来第一篇真正的双工语音助手架构论文**（10-08 这条线是空窗的，用了 8 个 wild-card）。
   语音智能体正在收敛到一种协作范式：全双工模型作为实时对话入口常驻通道，
   检索/推理/编码通过**异步委派**处理。分工理由是能力边界——双工模型支持持续听说，
   但复杂推理与工具使用超出其能力。把「双工模型」定位为**接口层**而非全能体，是重要的架构转向：
   它正好回答了记忆问题（10-07 PERSIST / AgentMemGate）在系统层面归谁管。
   **今天双工方向是三部曲**，建议连读：[DiffuPlex](https://arxiv.org/abs/2610.12214)（滚动掩码扩散，
   在单次骨干唤醒中预测多个未来帧，把等待用户说话的空转变成有用计算）、
   [SteerablePlex](https://arxiv.org/abs/2610.12201)（双工模型随历史增长失控，
   用作用户模拟器会产生**不可靠的评测结果**）。

### 备注

- **⚡ 双工线全面回补**：10-08 那天 cs.SD/eess.AS 之外双工关键词全库零命中，今天三篇真双工同时出现，
  且恰好覆盖架构、效率、可控性三个正交问题。把 SteerablePlex 与 10-07 的
  [Coupled but Late](https://arxiv.org/abs/2610.08683)（模型间环路稳定到的时序未必是人类的）连起来读，
  结论是：**以全双工模型为主体的评测协议目前都不可靠**，不只是需要改进。
- **跨线信号：绝对代理指标不预测下游实际效应**（本批最强）。Beyond Speech Captions 实证
  「语音-文本对齐只能弱预测下游声学结果」；Residual Advantage 用**学生相对**教师的指导替代结果标签，
  解释 OPD 为何无效（教师信号只有相对学生状态才有意义）；Can Jev be Your Q or Policy 追问
  RL 需要的是生成能力还是校准的评估接口；MiDashengLM-Spatial 与多篇论文都指出
  「各自强但都不完整」的空缺。10-08 日报的「预测精度/动作相关性/目标达成度是三个不同的量」继续延伸。
- **灵巧操作的数据来源被拆成三个独立障碍**：[Generative Neural Retargeting](https://arxiv.org/abs/2610.12440)
  （IK 忽略动力学，而灵巧操作恰是动力学受限任务）、[Dex-One2Many](https://arxiv.org/abs/2610.12470)
  （严格模仿动作把单条演示当成唯一答案，而成功轨迹是一个集合）、
  [OmniDex](https://arxiv.org/abs/2610.11194)（杂乱场景数据随场景×物体组合爆炸）。
  三篇合起来说明：用人类数据做灵巧操作不是「找更好的重定向算法」的问题。
- **新任务设定两则**：[Acting from Belief, Looking When Needed](https://arxiv.org/abs/2610.11591)
  把**观测时机**当作决策变量（间歇感知下的导航），是本批唯一一篇如此处理世界模型的工作；
  [Path-Creative Navigation](https://arxiv.org/abs/2610.11072) 指出导航任务被定义得过窄——
  既有方法假设环境固定只做绕行，而路线可能被铰接结构或可移动物体阻断。

## 2026-10-08

- **arXiv 批次窗口**：2026-10-07 UTC（截至 2026-10-08 17:00 CST，当天批次尚未发布）
- **扫描**：580 篇去重论文（cs.LG 251 / cs.AI 178 / cs.CV 148 / cs.RO 92 / cs.CL 79 /
  cs.SD 18 / eess.AS 18，其余为跨分类重复）
- **全文精读**：50 篇，抽取作者机构与 80 张论文原图

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-08/2026-10-08_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](https://arxiv.org/abs/2610.10429)**
   （aigc_visual #1）— 本批最强的诊断。自回归视频生成要同时做两件事：对当前帧去噪、
   把当前帧的 KV 写成后续预测的上下文。这两个角色通常**共用参数**，而作者测到它们的梯度
   呈现不同模式并存在**系统性负对齐**，直接妨碍视觉质量与时序一致性的联合优化。
   这解释了为什么时序不一致很难靠更大模型解决——不是学不会长程依赖，
   而是去噪梯度在直接损害 KV 写入目标。
   **务必连读 [Real-Time Joint Audio-Video Generation](https://arxiv.org/abs/2610.10343)**：
   它在部署侧给出同一病因的同一解法——链式流水线靠顺序获得「块自回归」与「少步采样」，
   但每一步都在微调上一步的权重，所以**后一个目标可以撤销前一个能力**；
   改为并行获得后，两个适配器的更新方向近似正交（训练中未施加任何正交约束），
   推理时直接相加。实时性数字是本批唯一完整的：**480×832、未量化、约 26 fps、30 秒连续生成**。

2. **[Predicted Futures Are Not Enough: Learning Executable Goals for Robot Manipulation](https://arxiv.org/abs/2610.09309)**
   （embodied #3）— 具身线四篇高相关论文合起来是本项目日报迄今最完整的一条批判线，
   这篇是最锋利的一环：生成式世界模型能预测操作场景如何朝目标演化，
   但**这些未来并不直接暴露控制所需的紧凑任务变量**；当训练只监督未来预测时，
   终极目标精度就不是一个显式的学习目标——即便几何恢复的信息在中间层可得。
   [RoboJEPA](https://arxiv.org/abs/2610.10515) 补上原则层（我们缺少估计潜世界模型
   能力如何随规模/数据/算力变化的方法），[ΔWAM](https://arxiv.org/abs/2610.09734) 补上第三块
   （可预测的未来有很大一部分由外观与场景持续性主导，而非动作依赖的动力学）。
   结论：**预测精度、动作相关性、目标达成度是三个不同的量**，把前一个当作后两个的代理
   会系统性误导。这条线直接对接 10-07 日报「世界模型可预测但不可控」。

3. **[BoT-GRPO: Efficient Process-Reward RL for Reasoning via Bag-of-Token Aggregation](https://arxiv.org/abs/2610.09804)**
   （rl #1）— GRPO 中每次 rollout 的所有 token 共享同一优势值，因此过程监督无梯度分化。
   BoT-GRPO 用 bag-of-tokens 聚合让过程奖励生效，**且不引入价值网络**——这一点比机制本身
   更关键，因为价值网络的训练成本与不稳定性正是 GRPO 被大量采用的主因，绕开它意味着
   这套方法能直接套进现有 GRPO 流水线。
   配对读 [COPC](https://arxiv.org/abs/2610.09597)：异步 LLM RL 的主流做法只修正策略侧的
   token 级不匹配，COPC **证明这不充分**——优势估计同样继承了行为策略的不匹配
   （优势正是用陈旧策略的轨迹算出的）。两篇同属 LLM RL 训练机制，一篇改奖励分配、
   一篇改 off-policy 校正。

### 备注

- **⚠️ 音频 LM 线今天几乎空窗**：cs.SD / eess.AS 之外双工与语音 LM 关键词全库零命中，
  25 篇声音类论文里没有一篇是真正的双工或语音语言模型工作。该线用了 **8 个 wild-card**，
  由 ASR、评测与安全类论文补足，真实相关的只有前两篇。读这条线时必须打折。
  唯二值得看的：[Dialect-Robust Speech LM](https://arxiv.org/abs/2610.09321)
  （LLM 生成方言文本 → 标准语言 TTS 转伪方言语音，把数据依赖从稀缺的语音侧移到丰富的文本侧）；
  [Boundary-Free Contextual Biasing](https://arxiv.org/abs/2610.09467)
  （为冻结的公开 CTC 模型做免训练、无二次解码的偏置解码，字符级 Aho-Corasick 绕开中日文词边界缺失）。
- **跨线信号（本日最强）**：**共享权重/共享参数导致两个目标互相抵消**。
  SGF+（梯度负对齐）、实时音视频（后一目标撤销前一能力）、ORCA（组合失败是对齐错位而非信息缺失，
  据此判定「补更强文本编码器」这条主流解法无效）、Visual Jev Rewards（主体在场≠主体参与交互）、
  ΔWAM（可预测未来被外观主导）、Predicted Futures（预测不暴露控制变量）、
  Juno（JEPA 潜变量干扰动作学习）、COPC（只修策略侧不足）——八篇跨全部五条线指向同一病因。
- **触觉方向从方法期进入基准期**：本批至少 5 篇触觉工作同时出现（因子化表征、500 小时视触数据、
  时序触觉学习、磁纤毛传感器、统一仿真-真实基准）。信号是子方向在快速积累、
  但尚无统一基准使这些方法无法横向比较。
- **与 10-07 的连线**：RFPO（推理端 ODE 积分预算错配）与前一天的 QF3（训练端流策略 RL 过慢）
  正好构成一对流策略实用化的两端；TTS 激活引导已连续两天出现（情感控制、隐式性别偏差校准）。

## 2026-10-07

- **arXiv 批次窗口**：2026-10-06 UTC（截至 2026-10-07 17:00 CST，当天批次尚未发布，
  最新已公告批次为 10 月 6 日）
- **扫描**：531 篇去重论文（cs.AI 221 / cs.LG 204 / cs.CV 112 / cs.CL 98 / cs.RO 86 /
  cs.SD 15 / eess.AS 8，其余为跨分类重复）
- **全文精读**：50 篇，抽取作者机构与 90 张论文原图

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-07/2026-10-07_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[World Models' Last Exam in Physics](https://arxiv.org/abs/2610.08791)**（embodied #1）
   — 本批相关性最高的一篇，也是三天来"指标系统性漏掉真实失效"这条线索的收口。
   此前 S2PD（物理一致性不随数据规模化涌现）、H-JEPA（潜变量对动作不敏感导致规划失败）
   都是**诊断**，这篇换掉了**评判方式**：40 个受控任务、基于实测而非模型判断，
   直接测视频世界模型的物理一致性。作者指出既有评测两个缺口——依赖模型判断或参考视频的
   不可靠，而直接物理测试又只覆盖力学。配套读 [DepthWorld](https://arxiv.org/abs/2610.08780)
   （方法侧答案：视频世界模型只在 RGB 上训练，rollout 逐帧正确却组合不成一致三维世界），
   诊断—修复链条完整。

2. **[QF3: Fast Flow RL with Filtered Q-Gradients](https://arxiv.org/abs/2610.08789)**（rl #1）
   — 首个能**从零**训练人形运动策略并零样本迁移到真机的离策略流 RL 方法。两个关键点：
   梯度经由流输出的一步预测反传，使离策略 critic 在流策略上可用而不发散；"过滤"的
   具体做法是把 critic 梯度只施加在保持接近 replay 动作的维度上，即只在 critic 与该预测
   都可靠的区域更新。配套高吞吐训练配方，墙钟时间相对在策略流 RL 基线 FPO++ **提速 10 倍**
   ——这个量级差异才是真正的门槛，因为流策略 RL 此前慢到难以实用。
   实机侧是 Unitree G1 零样本跟踪约 3 分钟的舞蹈动作。

3. **[PERSIST: Who-What-When Memory Across Sessions for Full-Duplex Spoken Dialogue](https://arxiv.org/abs/2610.07725)**（audio_lm #1）
   — 清华 + 华为。要回答"我原本打算什么时候离开"这类问题，仅靠主题相似检索不够：
   必须识别当前说话人、恢复相关历史状态，并**把它与后来的修正区分开**。
   "与修正区分"是全部难点——多数记忆系统写入即覆盖，因此只能回答"现在"而非"原本"。
   配对读 [AgentMemGate](https://arxiv.org/abs/2610.07707)（Distyl AI）：同一问题从写入端解决，
   提出"推测污染"（可能搬去西雅图的用户被记成已搬）并给出写入时门控。一读读取端、一读写入端。

### 备注

- **音频生成线连续第三天偏薄**：cs.SD 15 篇、eess.AS 8 篇，aigc_audio 用 4 个 wild-card
  补足（morphing 评测度量、RAVE 解码器激活分析、匿名化攻击、音乐源恢复）。
  头两篇仍撑得住——WorldSonus 的单卡 H100 上 RTF = 0.41 是全篇最有门槛意义的数字，
  它让"给世界模型加声音"从事后离线生成变成可交互闭环组件。
- **本批是评测论断密集的一天**：audio_lm 的四篇高相关论文里有三篇在质疑现有评测协议——
  Two-Body Problem 指出全双工模型普遍对着不会反应的单边对手评测；Coupled but Late 把两个
  模型放上共享时钟，发现模型间环路稳定到的时序未必是人类的（这对自生成数据是质量风险）；
  加上 embodied 的物理实测基准，构成同一批判的三个方向。
- **音频 LM 的方法侧进展**：HiPLEX 的论点值得记住——时序奖励与语义奖励施加在同一条 token 流上
  必然互相拉扯，因此需要层次化策略分解，而非"再加一个时序损失"。

## 2026-10-06

- **arXiv 批次窗口**：2026-10-04/05 UTC（截至 2026-10-06 17:00 CST，最新已公告批次）
- **扫描**：879 篇去重论文（cs.LG 386 / cs.AI 352 / cs.CV 186 / cs.CL 164 / cs.RO 113 /
  cs.SD 22 / eess.AS 15，其余为跨分类重复）
- **全文精读**：87 篇，抽取作者机构与 144 张论文原图

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-06/2026-10-06_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[EvoMem-VLA: State-Evolution Memory for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2610.05418)**
   （embodied #1）— 全批最干净的一个"记忆"论证：现有 VLA 记忆存的是*看到了什么*，
   而长程控制需要记住的状态必须带*它怎么变的*。用 conditional delta tokenization 把
   有序的源帧-目标帧对压成一个方向性的、以源为条件的 token。消融是决定性的：去掉 delta
   token 成功率 80.7% → 52.3%；而最朴素的"目标帧减源帧"特征差分只有 47.1%，**比完全没有
   delta token 还低**——33.6 个点的差距说明关键在于*学会*这个变化，而不是把差异暴露出来。
   一个策略联合训练即达 RMBench 80.7%（EventVLA 67.8%）、RoboMME 82.0%（最强基线
   44.5%）、真机 83.8%。

2. **[H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning](https://arxiv.org/abs/2610.06805)**
   （embodied #2）— 直接接上昨天日报里那条线。昨天那篇发现能解 PushT 的 LeWM 在语言目标
   基准上成功率 <1%，因为它的 latent 几乎对动作不敏感；H-JEPA 是建设性的回应：3 层层次
   结构把 Visual AntMaze 的规划成功率从 **18% 提到 73%**，而且是在**更低的** planner
   计算量下取得的。配合同批的 [Mind the Execution Gap](https://arxiv.org/abs/2610.06582)
   （世界模型可以预测得准却仍然不可控）一起读，三篇构成一条完整的诊断—修复链条。

3. **[S2PD: Serial-to-Parallel Diffusion for Physically and Logically Consistent Video Generation](https://arxiv.org/abs/2610.06847)**
   （aigc_visual #1）— 一个反直觉的强负结果：双向视频扩散 transformer 即使在"无限"的
   程序化生成数据上训练，仍然违反物理规律和简单符号规则——所以**物理正确性不会从数据
   规模化中自动涌现**，瓶颈是串行深度。方法端只加一个连续旋钮 τ（从全并行跨到全串行），
   τ=0.6 时采样 6.8 s 对 13.6-13.8 s 的基线，同时在四个视频数据集上 CD-FVD 全面最优。
   配套建议读同批的 [How Does Geometry Enter Generated Motion?](https://arxiv.org/abs/2610.05135)
   ——9 个模型、5000+ 视频的诊断给出同样方向的结论：小球在 72 个视频里有 63 个升到释放
   高度之上，在 49 个物理上不可逾越的障碍里跨过了 43 个。

### 备注

- **音频两线连续偏薄**：eess.AS 在两天窗口内只有 15 篇，aigc_audio 用 5 个 wild-card、
  audio_lm 用 5 个补足。第一轮筛选时 audio_lm 曾误选 4 篇纯文本 cs.CL 论文（相关性
  0-1，零音频内容），已替换为真实的语音论文（语音基础模型鲁棒性、说话人嵌入、
  阿拉伯语青少年语音语料、音频时刻检索等）。
- **跨线信号**：本批有 5 篇论文（S2PD、几何诊断、H-JEPA、Mind the Execution Gap、
  概念擦除的 AVCE/Tracer）从不同角度指向同一结论——**现有指标与"攻击成功率"式证据
  系统性地漏掉真实失效**：世界模型可预测但不可控，概念擦除 ASR 归零但内部表示仍可恢复，
  视频模型合规但状态不对。


## 2026-10-05

- **arXiv 批次窗口**：2026-10-01/02 UTC（截至 2026-10-05 17:00 CST，arXiv 尚未发布
  当天批次，最新已公告批次为 10 月 1–2 日）
- **扫描**：648 篇去重论文（cs.CV 150 / cs.CL 150 / cs.AI 150 / cs.RO 150 /
  cs.LG 150 / cs.SD 29 / eess.AS 23，其余为跨分类重复）
- **全文精读**：50 篇，抽取作者机构与论文原图

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-05/2026-10-05_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[In-Distribution Forcing for Long Video Generation at Test Time](https://arxiv.org/abs/2610.03120)**
   （aigc_visual #3）— 指出并修复 AR 长视频的 **KV-provenance 问题**：现有 KV
   conditioning 假设缓存的 KV 始终在分布内，但 rollout 时没有任何机制约束其构造，
   缓存条目自身就会 OOD。self-caching 让每个 chunk 不关注历史 KV，滚动窗口始终保持
   分布内，训练-free 地把短视频模型推到分钟级。同一批里 MosaiChunk（KV 马赛克记忆）、
   TRAC（AR 轨迹级误差累积）、Weave Forcing（组合式记忆）都在打同一个长视频记忆难题，
   建议对照读。

2. **[Keeping JEPA World Models Plannable When Little of the Frame Moves](https://arxiv.org/abs/2610.03137)**
   （embodied #1）— 一篇诊断质量极高的论文：能解 PushT 的 LeWM 在语言目标基准 SLIM 上
   成功率 **<1%**。探针把故障定位到编码器——latent 几乎对动作不敏感，rollout 不比直接
   复制当前 latent 更好。一个 inverse-dynamics 辅助损失把成功率从 0.003 拉到 0.35。
   还给出一个无需环境访问的 action-sensitivity 探针作为"可规划"的必要条件。
   配对阅读同批的 [AVL-JEPA](https://arxiv.org/abs/2610.03587)，它治的是另一个
   互补的失效：JEPA 保留了高维视觉信息却丢掉了动作的物理后果。

3. **[AURAL: Adaptive Latent Reasoning with Joint Chunk for Speech Language Models](https://arxiv.org/abs/2610.01560)**
   （audio_lm #1）— 语音 LM 里 CoT 的延迟税被量化并解决：在隐空间建模多条合理推理
   续写的分布并联合预测未来状态块，配合 683K 条 CoT 语料（≈1000 小时）与 RL，
   在 Qwen2.5-Omni 上把首 token 延迟从 **1.22 s 降到 0.10 s（11.8x）**，质量与
   CoT-RL 相当。本批没有真正的全双工语音助手论文，但这是双工助手延迟问题最具体的
   一个答案。同批
   [Metadata-Supervised Pretraining for Encoder-Free Speech-LLMs](https://arxiv.org/abs/2610.01695)
   则在质疑预训练语音编码器是否必要，同样值得一读。

### 备注

- **音频两线偏薄**：本批 eess.AS 仅 23 篇、cs.SD 29 篇，AIGC 音频与语音 LM 两条线
  依靠 wild-card 补足（各 1 篇）。`aigc_audio` 的 wild-card 是一篇上下文长度审计，
  作者自查出自己早期稿件的 split leakage，作为方法论参考价值高。
- **跨线信号**：本批有 4 篇论文（TerraVis、PhysicsLENS、"Does Physics Live in the
  Activations?"、AVL-JEPA）从不同角度指向同一结论——现有生成/世界模型指标系统性地
  漏掉物理正确性问题。
