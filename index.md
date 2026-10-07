# ArXiv 论文日报索引

由 `mine-arxiv-daily-digest` skill 每日生成。每条记录包含当天各研究线的论文数，
以及当天最值得读的 3 篇。

**统计口径**：每次运行扫描 arXiv 的 7 个分类（cs.CV / cs.SD / eess.AS / cs.CL /
cs.AI / cs.RO / cs.LG），按 5 条研究线各出 10 篇排名报告。

## 目录

| 日期 | 扫描量 | AIGC 视觉 | AIGC 音频 | 语音 LM | 具身/世界模型 | 强化学习 | 当天最值得读 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [2026-10-07](daily_arxiv_digest/2026_10/2026-10-07/) | 531 | 10 | 10 | 10 | 10 | 10 | [World Models' Last Exam 实测物理一致性](https://arxiv.org/abs/2610.08791) · [QF3 首个从零训练人形策略的离策略流 RL](https://arxiv.org/abs/2610.08789) · [PERSIST 记忆要区分「原本」与「现在」](https://arxiv.org/abs/2610.07725) |
| [2026-10-06](daily_arxiv_digest/2026_10/2026-10-06/) | 879 | 10 | 10 | 10 | 10 | 10 | [EvoMem-VLA 记忆存错了东西](https://arxiv.org/abs/2610.05418) · [H-JEPA 分层世界模型 18%→73%](https://arxiv.org/abs/2610.06805) · [S2PD 物理一致性来自串行深度](https://arxiv.org/abs/2610.06847) |
| [2026-10-05](daily_arxiv_digest/2026_10/2026-10-05/) | 648 | 10 | 10 | 10 | 10 | 10 | [ID-Forcing (长视频 KV-provenance)](https://arxiv.org/abs/2610.03120) · [JEPA 可规划性诊断](https://arxiv.org/abs/2610.03137) · [AURAL 隐式推理降延迟 11.8x](https://arxiv.org/abs/2610.01560) |

---

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
