# ArXiv 论文日报索引

由 `mine-arxiv-daily-digest` skill 每日生成。每条记录包含当天各研究线的论文数，
以及当天最值得读的 3 篇。

**统计口径**：每次运行扫描 arXiv 的 7 个分类（cs.CV / cs.SD / eess.AS / cs.CL /
cs.AI / cs.RO / cs.LG），按 5 条研究线各出 10 篇排名报告。

**跳过记录**：当 arXiv 尚未公告新批次时（周末、节假日、或公告尚未发布），
当日不生成日报，也不新增目录行，以免与上一份报告重复。已跳过或合并的日期：

- **2026-10-13** — 探测 10-10 / 10-11 / 10-12 / 10-13 四个 UTC 日均返回 0 条；
  无日期限制查询确认全库最新提交仍为 `2610.13947v1`（2026-10-09T17:59:41Z），
  与 10-12 那份日报所覆盖的批次相同，故跳过。
- **2026-10-14（累计补齐）** — 10-13 之后 arXiv 补发了 4 个批次（10-10 至 10-13 UTC），
  为避免漏读，本份日报采用**累计窗口**一次性覆盖 1935 篇，而非只取最新批次。
- **2026-10-17 与 2026-10-18（周六、周日）** — 连续两天探测 10-16 / 10-17 / 10-18 均为 0 条；
  无日期限制查询确认全库最新提交两次均为 `2610.22372v1`（2026-10-15T17:59:59Z），
  与 10-16 那份日报所覆盖的批次完全相同（574 篇 / 逐日原始 805 条），故两天均跳过。
  与 arXiv 的投稿周期一致：周五 14:00 ET 截止后至周日 14:00 ET 恢复，期间不受理新投稿。
  最新报告仍为 [2026-10-16](daily_arxiv_digest/2026_10/2026-10-16/)。

## 目录

| 日期 | 扫描量 | AIGC 视觉 | AIGC 音频 | 语音 LM | 具身/世界模型 | 强化学习 | 当天最值得读 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [2026-10-20](daily_arxiv_digest/2026_10/2026-10-20/) | 525 | 10 | 10 | 10 | 10 | 10 | [是 RL 的功劳还是数据的功劳](https://arxiv.org/abs/2610.25812) · [音频 LLM 到底有没有在听](https://arxiv.org/abs/2610.25599) · [首个跨本体 loco-操作世界基础模型](https://arxiv.org/abs/2610.26855) |
| [2026-10-19](daily_arxiv_digest/2026_10/2026-10-19/) | 429 | 10 | 10 | 10 | 10 | 10 | [准确率可以在不 grounding 的情况下提升](https://arxiv.org/abs/2610.23148) · [Qwen3-TTS 的条件化与失效模式](https://arxiv.org/abs/2610.23678) · [无视觉纯触觉操控](https://arxiv.org/abs/2610.23438) |
| [2026-10-16](daily_arxiv_digest/2026_10/2026-10-16/) | 574 | 10 | 10 | 10 | 10 | 10 | [一次通过回答多个话轮问题](https://arxiv.org/abs/2610.21150) · [167 万条 RLVR 语料的去污染审计](https://arxiv.org/abs/2610.21229) · [机器人策略该预测什么](https://arxiv.org/abs/2610.21915) |
| [2026-10-15](daily_arxiv_digest/2026_10/2026-10-15/) | 570 | 10 | 10 | 10 | 10 | 10 | [单次 rollout 的 token 信用分配](https://arxiv.org/abs/2610.20497) · [LALM 后训练学到的是格式适应](https://arxiv.org/abs/2610.19476) · [触觉从传感器变为表示学习来源](https://arxiv.org/abs/2610.20134) |
| [2026-10-14](daily_arxiv_digest/2026_10/2026-10-14/) | 1935 | 10 | 10 | 10 | 10 | 10 | [Diffuplex：全双工 1872 token/s](https://arxiv.org/abs/2610.17780) · [Demiurge：跨轨迹一致的 4D 世界](https://arxiv.org/abs/2610.14685) · [LLM 价值函数做信用分配](https://arxiv.org/abs/2610.15840) |
| [2026-10-12](daily_arxiv_digest/2026_10/2026-10-12/) | 488 | 10 | 10 | 10 | 10 | 10 | [审计 AAD：主流缓解手段的参照物是 OOD](https://arxiv.org/abs/2610.13112) · [动作不描述它将达成什么](https://arxiv.org/abs/2610.13212) · [PPO 的裁剪代理是几何退化的](https://arxiv.org/abs/2610.13015) |
| [2026-10-09](daily_arxiv_digest/2026_10/2026-10-09/) | 643 | 10 | 10 | 10 | 10 | 10 | [聚合准确率掩盖成对漂移](https://arxiv.org/abs/2610.11196) · [因果视频扩散不需要双向教师](https://arxiv.org/abs/2610.11479) · [双工智能体的异步委派范式](https://arxiv.org/abs/2610.11299) |
| [2026-10-08](daily_arxiv_digest/2026_10/2026-10-08/) | 580 | 10 | 10 | 10 | 10 | 10 | [SGF+ 梯度负对齐（+ 实时音视频 26fps）](https://arxiv.org/abs/2610.10429) · [预测的未来不足以控制](https://arxiv.org/abs/2610.09309) · [BoT-GRPO 不要价值网络](https://arxiv.org/abs/2610.09804) |
| [2026-10-07](daily_arxiv_digest/2026_10/2026-10-07/) | 531 | 10 | 10 | 10 | 10 | 10 | [World Models' Last Exam 实测物理一致性](https://arxiv.org/abs/2610.08791) · [QF3 首个从零训练人形策略的离策略流 RL](https://arxiv.org/abs/2610.08789) · [PERSIST 记忆要区分「原本」与「现在」](https://arxiv.org/abs/2610.07725) |
| [2026-10-06](daily_arxiv_digest/2026_10/2026-10-06/) | 879 | 10 | 10 | 10 | 10 | 10 | [EvoMem-VLA 记忆存错了东西](https://arxiv.org/abs/2610.05418) · [H-JEPA 分层世界模型 18%→73%](https://arxiv.org/abs/2610.06805) · [S2PD 物理一致性来自串行深度](https://arxiv.org/abs/2610.06847) |
| [2026-10-05](daily_arxiv_digest/2026_10/2026-10-05/) | 648 | 10 | 10 | 10 | 10 | 10 | [ID-Forcing (长视频 KV-provenance)](https://arxiv.org/abs/2610.03120) · [JEPA 可规划性诊断](https://arxiv.org/abs/2610.03137) · [AURAL 隐式推理降延迟 11.8x](https://arxiv.org/abs/2610.01560) |

---

## 2026-10-20

- **arXiv 批次窗口**：2026-10-19 UTC（截至 2026-10-20 17:00 CST，当天批次尚未发布）
- **扫描**：525 篇去重论文（cs.AI 198 / cs.LG 183 / cs.CV 129 / cs.CL 113 / cs.RO 68 /
  cs.SD 9 / eess.AS 10，其余为跨分类重复）
- **全文精读**：50 篇，抽取作者机构与 86 张论文原图
- **Wild-card**：本批 14 篇（aigc_visual 1 / aigc_audio 8 / audio_lm 5 / embodied 1 / rl 0）

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-20/2026-10-20_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[Is it RL or Data? A Controlled Comparison of GRPO and Rejection-Sampling Fine-Tuning](https://arxiv.org/abs/2610.25812)**（rl #1）
   — **本批最重要的一篇：把 GRPO 本身放上了实验台。**
   Bauer 等（2026）报告低数据 RLVR 中，混合难度提示训练 GRPO 相比只用易提示可获最高 **5 倍**样本效率，
   但**没有检验**这一收益是否 GRPO 特有——换一种用同样数据的后训练方法是否也能得到？
   作者在完全相同的提示与数据下做 GRPO 与拒绝采样微调的受控对比。
   **这是整个 RLVR 叙事的地基检验**：若收益主要来自「混合难度的数据」而非算法本身，
   那么大量围绕 GRPO 变体的工作其实在优化一个**数据效应**——而数据效应通常更便宜、更容易推广。

2. **[Text Dominance in Paralinguistic Conflict: Tracing Suppression Through Audio LLM Circuits](https://arxiv.org/abs/2610.25599)**（audio_lm #1）
   — 回答了一个基础问题：**音频 LLM 到底有没有在听声音**。
   在 LISTEN 风格条件下测试**六个**音频 LLM，检验它们是优先考虑转写内容还是副语言线索
   （情绪、说话人身份、讽刺），并在出现文本优势时**追踪到电路层面**。
   若模型在有转写可用时基本忽略音频，那么部署在危机热线、客服这类
   「转写错误代价高、声学信息关键」的场景就存疑。
   与 10-19 日报 VocalGrad（声学信息与语言共现时无法利用）互为宏观与微观版本。

3. **[Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855)**（embodied #1）
   — 据称是**首个跨本体的第一人称 loco-操作世界基础模型**。
   它把「移动+操作」明确为独立问题而非两个任务的叠加——
   移动与操作在物理上耦合（操作改变重心从而改变移动），分开建模必然丢掉这一耦合项。

### 备注

- **⚡ 越狱 ASR 的评测程序决定结论**：同一批攻击，面向低资源语言的攻击在关键词匹配下平均 ASR 达 **96.0%**，
  在另一种判定程序下仅 **2.7%**——**35 倍**的落差说明「提到敏感内容」与「被真正劫持」被混为一谈，
  这与 10-19 日报「被忽略而非被拒绝」是同一类误判。
  配套 [Beyond Attack Success Rate](https://arxiv.org/abs/2610.26589) 指出 ASR 完全未考虑
  **对受害模型的重复调用**——而每次额外调用都给了部署系统一次检测与干预的机会。
  **任何引用越狱 ASR 数字的工作都应先检查其判定程序**，否则跨论文比较毫无意义。
- **本批最值得做复现的一篇**：[Halcyon](https://arxiv.org/abs/2610.26863)
  （Text-to-Image Generative Modeling Without Language Pretraining）质疑整个领域最昂贵的前置投入——
  语言预训练对强 T2I 是否必要。它检验的是**领域默认**而非某个新组件。
- **自回归视频算力账一次性来了四篇**：
  [Dynamics-Aware Sparse Attention](https://arxiv.org/abs/2610.26262)（低效源于稠密计算**均匀分配**资源）、
  [TriTD](https://arxiv.org/abs/2610.26165)（把瓶颈分解为三个误差来源）、
  [Clean Forcing](https://arxiv.org/abs/2610.25634)（**冻结基座**换稳定性）、
  [RECAP](https://arxiv.org/abs/2610.26244)（稀疏注意力与时间缓存组合时**耦合误差**——
  两个各自安全的加速手段叠加后互相污染，这一教训在 10-17 的多奖励归一化、10-18 的主副轴耦合中同样出现）。
- **「测量优于判断」正在成为共识**：[PVBench](https://arxiv.org/abs/2610.26711) 用**物体级物理测量**
  替代粗糙的 VLM 判断，与 10-07 日报 World Models' Last Exam（40 个受控任务实测）主张相同，
  两篇独立工作同时出现。
- **⚠️ aigc_audio 是本项目日报至今第二薄的一次**：cs.SD 仅 9 篇，全库 525 篇中**只有三篇**真实音频生成论文
  （SEAM、MuLaCover、音乐结构分析），该线用了 **8 个 wild-card**。
  仍值得看 [SEAM](https://arxiv.org/abs/2610.26252)：**零音频**初始化扩展 TTS 词表，
  把词表扩展从「需要目标语言的真实录音」降为「只需目标语言的文本与谱结构」。
- **一个标注概念问题**：[Label Authority in SER](https://arxiv.org/abs/2610.26446) 指出
  情感识别的真值常被当作**单一分类事实**，但「被表演的情绪」与「听到的情绪」是同一录音的**不同方面**——
  若标注的是意图而模型学的是感知，标注一致性再高也无意义。

## 2026-10-19

- **arXiv 批次窗口**：2026-10-16 UTC（截至 2026-10-19 17:00 CST；周末无公告，故窗口较前次回溯 3 天）
- **扫描**：429 篇去重论文（cs.LG 156 / cs.AI 119 / cs.CL 96 / cs.CV 90 / cs.RO 54 /
  cs.SD 18，其余为跨分类重复）
- **全文精读**：50 篇，抽取作者机构与 90 张论文原图
- **Wild-card**：本批 10 篇（aigc_visual 1 / aigc_audio 3 / audio_lm 5 / embodied 1 / rl 1）；
  **aigc_audio 的 wild-card 从昨天的 9 降到 3**，音频生成线明显回暖

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-19/2026-10-19_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[Grounded Credit Assignment in Reinforcement Learning for Multi-Turn Search Agents](https://arxiv.org/abs/2610.23148)**（rl #1）
   — **本项目日报审计线索中最锋利的一次**：结果奖励 RL（GRPO）给搜索智能体每个 token 相同优势，
   而 rollout 实际同时练习「找到证据」与「使用证据」。作者表明
   **准确率可以在没有 grounding 的情况下提升**——Search-R1 在全部七个 QA 基准上提升准确率，
   但在 Bamboogle 上有证据支持的正确回答占比并未同步改善。
   换言之，一个旗舰 RL 方法可以在**不使用检索到的证据**的前提下刷高分数。
   配套必读 [Batched Contextual RL II](https://arxiv.org/abs/2610.22887)：长 rollout 窗口使 RLVR 昂贵，
   但单纯缩短会在**每条 rollout 都截断于答案之前**时消除组相对优势（组内同质则优势恒为零）。
   两篇合起来定义了 RLVR 的真实张力。

2. **[Beyond the Benchmark: Conditioning, Domains and Failure Modes of Qwen3-TTS](https://arxiv.org/abs/2610.23678)**（aigc_audio #1）
   — Qwen3-TTS 报告了 SOTA 零样本克隆，但技术报告留下三个未答问题：**模型应如何被条件化**、
   **在朗读语音之外表现如何**、**如何失败**。作者刻画其两种克隆接口（ICL 与 X-Vector），
   并与 Chatterbox、XTTS-v2、F5-TTS 对比。
   「朗读之外」是最少被测的条件——基准几乎都用朗读语料，而真实使用场景多为自然口语。
   **选型前用它作为替代评测，比直接采信技术报告的 SOTA 数字更可靠。**

3. **[No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?](https://arxiv.org/abs/2610.23438)**（embodied #2）
   — **触觉连续第五天出现在本日报**，而今天这篇把它推到极端：人类能仅凭手内触觉操控物体，
   机器人**在完全无视觉**下实现持续真实操作仍是开放挑战。
   这是一个干净的消融设定——它把触觉从「视觉的补充」提升为**独立的操作信息来源**，
   因此能真正回答触觉的边际价值，而非其在有视觉系统中的增量。

### 备注

- **⚡ 审计线索的第三种类型**：前几类是「指标测错了东西」（UMMOS 口音偏见）与
  「评测工具本身有问题」（Selective Listening、AAD 审计）；今天多了一类
  **「指标对但行为不是那样」**——Search-R1 在七个基准上涨分，却没用证据。
  同一批还有两个实例：[Ignored, Not Refused](https://arxiv.org/abs/2610.23254)
  审计**十一个开放权重模型的 33,000 条轨迹**，发现低提示注入成功率隐藏的是
  「**被忽略**」而非「被拒绝」；[MUB](https://arxiv.org/abs/2610.22989) 用**身份遮蔽**录音
  切断「搜歌名再答题」这条捷径；[Leakage-Audited Arousal](https://arxiv.org/abs/2610.23063)
  按**完整歌曲**留出，防止模型靠记忆片段而非预测趋势得分。
- **RL 信用分配的一个免费信号被找到**：MGE-PO 用 **rollout 生成熵**——
  GRPO 给同等奖励的响应相同优势，但它们之间的熵差异被浪费了；
  正确性决定修正的符号、熵决定幅度，且不需要额外的奖励模型。
- **一个值得做实验验证的论断**：[Learning to Correct Geometry in Generated Videos](https://arxiv.org/abs/2610.23856)
  论证生成视频的几何不一致**在很大程度上是数据问题**——网络规模视频语料中大部分运动来自手持拍摄，
  缺少精确相机轨迹。若成立，增加训练规模不会解决它。
- **数据侧的一个隐蔽陷阱**：[ASR-Style Transcript Normalization](https://arxiv.org/abs/2610.22934)
  指出 ASR 归一化会移除填充停顿、标点并展开口语形式——而这些恰恰是对话行为分类所依赖的线索。
  下游任务若直接用标准 ASR 输出，会在训练阶段就失去这些信息。成本极低而影响面很大。
- **⚠️ 双工语音方向仍然稀缺**：本批 cs.SD 与 eess.AS 之外双工关键词全库零命中，audio_lm 用了 5 个 wild-card。
  本线唯一可归入该议题的是 [Jarvis](https://arxiv.org/abs/2610.23804) 及其「慢脑-前端」分工——
  它把「双工」从轮次级并发推进到**任务级**并发：用户可在任务运行中改写需求，
  因此协调层必须是一等组件而非消息传递。

## 2026-10-16

- **arXiv 批次窗口**：2026-10-15 UTC（截至 2026-10-16 17:00 CST，当天批次尚未发布）
- **扫描**：574 篇去重论文（cs.AI 226 / cs.LG 211 / cs.CV 135 / cs.CL 135 / cs.RO 78 /
  cs.SD 13 / eess.AS 极少量，其余为跨分类重复）
- **全文精读**：50 篇，抽取作者机构与 89 张论文原图
- **Wild-card**：本批 10 篇，其中 **aigc_audio 占 9**（见下方警告）

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-16/2026-10-16_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[VoxTurn: Answering Several Turn-Taking Questions in One Pass with One Model](https://arxiv.org/abs/2610.21150)**（audio_lm #1）
   — 级联语音智能体必须在用户的**每次静默中**判断用户是否说完（太早→打断，太晚→变慢），
   而且往往还需要几个相关但不同的判断：用户是否会继续说、自己说话期间的声音是
   **打断还是附和**、那声音到底是不是语音。VoxTurn 用**一个模型一次通过**回答这几个问题。
   关键在于：把多个检测器合并为一次前向不只是省算力，而是让这些判断**共享表示**——
   而「打断 vs 附和」的区分恰恰需要同时看到语音与自身说话状态，分离的检测器在结构上无法做到。
   它直接回应了昨天 MultiPartyTurnBench 提出的「易混淆非事件」难题。

2. **[What Should We Remove? Evaluating the Reliability and Costs of RLVR Data Decontamination](https://arxiv.org/abs/2610.21229)**（rl #2）
   — **本项目日报审计线索中规模最大的一例**：审计 **16 个开放 RLVR 数学语料、1,673,514 条训练项**，
   对照 **6 个基准、1,949 道题**，评估去污染清理策略的可靠性与**数据损失代价**。
   去污染的隐含代价常被忽略：清理越激进训练数据损失越大，而训练语料规模与效果的关系在 RLVR 上
   尚未被系统刻画——因此「宁可多删」的直觉可能并不成立。任何用公开 RLVR 语料做后训练的团队都应先看这份数字。

3. **[What Should Robot Policies Learn to Predict?](https://arxiv.org/abs/2610.21915)**（embodied #2）
   — VLA 通常以动作预测为主要监督，而 latent-action（LA）与未来视觉（FV）预测等辅助目标
   常被加入以改进策略学习，然而作者指出它们会与动作预测**竞争表示容量**。
   「辅助目标越多越好」是本方向的普遍默认，本文把它变成一个可测的取舍——
   接上 10-12 Beyond Actions（预测目标换成效果）与 10-14 WAVE-0/ΔWAM，是这条线的又一环。

### 备注

- **⚠️ aigc_audio 是本项目日报至今最薄的一次**：cs.SD 仅 13 篇，
  全库 574 篇中**没有一篇** TTS、音乐生成或语音转换论文（10-14、10-15 这两天分别有 10、8 篇真实生成/编辑工作）。
  该线用了 **9 个 wild-card**，由转录、压缩、水印、语音增强、多语评测等**非生成**工作补足，
  读这部分时请大幅打折。
- **⚡ 本批是记忆方向的最大一次聚集**（跨四条线共八篇）：
  [Hy-Memory](https://arxiv.org/abs/2610.22196)（把**写入路径**识别为需专门优化的关键环节）、
  [MemComposer](https://arxiv.org/abs/2610.21091)（**语义相似本身不保证记忆有用**，有用性由呈现方式决定）、
  [All-in-One Memory](https://arxiv.org/abs/2610.21147)（搜索/写入/停止缺少**共享奖励空间**）、
  [MemCut](https://arxiv.org/abs/2610.21405)（记忆基准长期只测「找得回不准」，
  因此一个每次检索完美但拒绝删除的系统会得满分）、
  [从长上下文到选择性记忆](https://arxiv.org/abs/2610.21165)（「持续扩展上下文窗口并不消除推理期压力」）、
  以及嵌入/具身/RL 线的若干变体。这条线本项目已连续追踪五天（10-07 PERSIST → 10-09 Gated Memory → …）。
- **触觉连续第四天出现在本日报**：10-08 五篇、10-14 五篇力/接触、10-15 一篇综述、
  今天 [Spark-0](https://arxiv.org/abs/2610.22342)。关键设计是**空间对齐**：
  触觉的高维信号若不与视觉空间对齐，就只能提供「有接触发生」这类全局信息、无法定位接触位置，
  这正是触觉此前难以进入预训练的根本原因。
- **两个被质疑的标准组件**：[Speculative Forcing](https://arxiv.org/abs/2610.22347) 指出少步 AR 视频生成器
  **让每个 token 都走最终去噪步**而不论需要多少精修；[Rethinking CFG](https://arxiv.org/abs/2610.21550)
  论证 CFG 在文图到图建模中的角色被理解不足（输入已高度约束分布时 CFG 可能在放大输入偏差而非提升质量）。
  两篇都接上本日报审计线索。
- **管线脚本已固化**：抓取与 PDF 提取的机械部分已迁移到
  [`project_handbook/project_tools/digest/`](https://github.com/xuekt98/DailyArxivDigestPaper/tree/main/project_handbook/project_tools/digest)
  （`scrape.py` / `read.py`），不再每次随临时目录重写。

## 2026-10-15

- **arXiv 批次窗口**：2026-10-14 UTC（截至 2026-10-15 17:00 CST，当天批次尚未发布）
- **扫描**：570 篇去重论文（cs.LG 221 / cs.AI 211 / cs.CL 139 / cs.CV 120 / cs.RO 79 /
  cs.SD 19 / eess.AS 11，其余为跨分类重复）
- **全文精读**：50 篇，抽取作者机构与 93 张论文原图
- **Wild-card**：本批 10 篇（aigc_visual 2 / aigc_audio 3 / audio_lm 5 / embodied 1 / rl 1）

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-15/2026-10-15_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[Hindsight-Privileged RLVR: Single-Rollout Token Credit Without Group Sampling](https://arxiv.org/abs/2610.20497)**（rl #1）
   — **攻击的是 GRPO 必须多次采样这个结构性成本，而不是它的信用分配粒度。**
   组采样的代价不只是算力：它是熵退化与组内无变化的根源，因为组必须来自同一策略的窄分布；
   用事后（hindsight）信息替代同策略采样，等于绕开了这个循环依赖。
   配套读 [Where to Start, How to Move](https://arxiv.org/abs/2610.19349)，
   它给出同一问题的另一半：**训练早期全失败组很常见**，而长时程任务只在成功时给奖，
   因此全失败组**阻止了后续步骤被练习**——因为到达后续步骤本身就要求先成功。
   两篇合起来是一个自锁：不会到达，就不会被练到。

2. **[What Does LALM Post-training Learn?](https://arxiv.org/abs/2610.19476)**（audio_lm #2）
   — **本项目日报审计线索的第五次出现**，且对象是更根本的问题：
   后训练带来的基准提升**可能反映的是对特定问题格式（如选择题）的适应**，
   而非音频理解与推理能力的真正进步。
   选择题的后训练收益可以来自「学会排除干扰选项」这一格式技巧，这在开放式生成中完全无用——
   若评测只用选择题，该能力的价值被系统性高估。用 LALM 基准分数做选型前建议先看这篇。

3. **[Tactile-Guided Robot Learning: From Representation Learning to Foundation Models](https://arxiv.org/abs/2610.20134)**（embodied #1）
   — **把本项目日报已追踪三天的触觉趋势收束成一篇综述**（10-08 五篇触觉、10-14 五篇力/接触、今天三篇）。
   关键论断：触觉的角色已从接触检测与反应式控制，扩展到**学习可迁移表示**、条件化策略与支撑具身物理推理——
   它提供的是视觉无法获得的**物理接触信息**，而非更精细的接触信号。
   配套 [TacClaw-Infinity](https://arxiv.org/abs/2610.20320) 点出数据瓶颈的真实位置：
   触觉数据的难点不是采集量而是**标注结构**（视觉可自动弱标注，触觉需要与接触事件对齐的时序标签）。

### 备注

- **⚡ 一条可直接用于工程决策的反直觉观察**：
  [Speculative Sampling in Interactive Video Generation](https://arxiv.org/abs/2610.20556)
  实验显示交互式视频生成中**更大的块提升视频质量**且更好利用 GPU 并行，
  采样时间仅小幅增加——这直接推翻了「块越小越好」这一部署默认（小块的低质量可能来自其自身表达限制
  而非速度代价）。配合 [Are We Overthinking One-Step Generation?](https://arxiv.org/abs/2610.20331)
  （质疑一步生成研究的复杂度投入），两篇共同指向：过去几年在「更少步数」上的努力，
  可能不如「接受稍多步数换质量」划算。
- **自回归化的成本是本批 AIGC 视觉主线**，接上 10-09（Conditional Residual Prediction）
  → 10-12（Unified Generative Video Compression）→ 10-14（七篇 AR 缓存方案）→ 今天补上**转换本身**：
  [Glance Forcing](https://arxiv.org/abs/2610.20220) 指出主流做法需要**离线 PF-ODE 轨迹**，
  每次转换都要跑一遍完整求解器而蒸馏本身已需大量采样，**成本是叠加的**；
  [RepForcing](https://arxiv.org/abs/2610.20111) 则把初始化与蒸馏分开——
  中间 AR 教师能提供因果兼容的 ODE 目标，但**因果兼容本身并不保证高质量生成**。
- **⚠️ 双工语音方向再次稀缺**：本批 cs.SD 19 + eess.AS 11 篇中仅一篇真双工，
  且属通信域的带内全双工自干扰消除（非语音域）。audio_lm 用了 5 个 wild-card。
  仍值得看的 [MultiPartyTurnBench](https://arxiv.org/abs/2610.20172) 把话语权时机推进到多方场景，
  并明确提出**易混淆的非事件**这一关键设计——附和（backchannel）在声学上与真正的话轮转换几乎不可分，
  因此只测正例的基准会奖励「对任何声音都让出话语权」的策略。
  它接上 10-07 Coupled but Late → 10-09 DuplexAct → 10-14 Diffuplex/D2 这条追踪线。
- **RL 评测的第三个审计实例**：[More Methods, Better Agents?](https://arxiv.org/abs/2610.19789)
  指出既有评测常在不同实验条件下**复用已发表的基线分数**，意味着比较的不是方法而是**评测设置**。
- **RL 信号正确性三篇**：C3 指出纯结果 RL 会产生**误导性强化**（成功轨迹上不良的局部行为
  也可能拿到**正的** token 级优势）；When Pairwise Preferences Cycle 指出成对偏好可能成环
  （A>B、B>C 不蕴含 A>C）；When Does Momentum Help in RLVR? 用 bandit 形式化质疑一阶动量
  （动量有效的前提是梯度近似同向，而 RLVR 梯度方差极大）。

## 2026-10-14

- **arXiv 批次窗口**：**累计窗口 2026-10-10 至 2026-10-13 UTC**（10-13 之后 arXiv 补发 4 个批次；
  10-13 那次运行因当时尚未公告而跳过，这四次一并补齐，避免漏读）
- **扫描**：**1935 篇**去重论文（cs.AI 769 / cs.LG 759 / cs.CV 431 / cs.CL 355 / cs.RO 266 /
  cs.SD 60 / eess.AS 若干，其余为跨分类重复）；逐日原始量 10-10:481 / 10-11:427 / 10-12:851 / 10-13:912
- **全文精读**：50 篇，抽取作者机构与 89 张论文原图
- **Wild-card**：本批 5 篇；**audio_lm 零 wild-card**——双工方向自 10-08 以来首次满配

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-14/2026-10-14_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[Diffuplex: Full-duplex Spoken Language Modeling with Discrete Diffusion](https://arxiv.org/abs/2610.17780)**（audio_lm #1）
   — **双工方向自 10-08 记录以来首次满配**（10-08 空窗、10-09 三篇、10-12 空窗），今天一次性出现四篇真双工工作。
   Diffuplex 基于离散扩散，**开启思考模式时每次前向 13.0 个 token、平均 1872 token/秒**，
   解码速度显著超过前沿自回归模型。在全双工场景下「每次前向多 token」不是优化而是**必要**：
   轮次决策必须亚秒完成，否则等待用户说话的延迟会直接破坏交互体验。
   配套读 [D2](https://arxiv.org/abs/2610.17124)（MIT CSAIL + MIT-IBM Watson AI Lab）：
   全双工模型在通用能力上长期**落后于半双工**，D2 在细时间粒度上把预训练半双工转换为高能力全双工，
   这条路比「从零训练全双工」成本低一个量级。

2. **[Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering](https://arxiv.org/abs/2610.14685)**（aigc_visual #1）
   — 直接连接 AIGC 视频与世界模型两个核心兴趣。既有 novel-view 视频方法**独立处理每条相机轨迹**，
   缺乏形成连贯可导航 4D 世界所需的跨轨迹一致性。关键区分在于：单条轨迹的 NVS 只需轨迹内一致，
   而可导航世界要求跨轨迹的同一性——这是强得多的约束，也是世界模型真正需要的性质。

3. **[LLM Value Functions for Credit Assignment in Agentic RL](https://arxiv.org/abs/2610.15840)**（rl #1）
   — 本批 RL 十篇全部在处理 GRPO 家族的信用分配与信号质量。核心矛盾被反复陈述：
   GRPO 把相同的轨迹级优势**同等广播给所有动作**，而评论家方法需额外学一个价值函数。
   ProAS 把这称为「统一信用分配困境」并指出均匀性会**持续强化多数模式**——
   未尝试的动作因此无法获得优势。LLM Value Functions 试图绕开这个二选一：不训额外评论家，
   而是用 LLM 本身充当价值函数，代价是信用分配的正确性被绑定到 LLM 的判断质量上。

### 备注

- **⚡ 双工线全面回补且首次零 wild-card**。更值得注意的是 [DuplexAct](https://arxiv.org/abs/2610.17738)
  ——它是本项目日报在 10-09 提出的问题的**直接回应**。当时判断「以全双工模型为主体的评测协议都不可靠」，
  并列出三条具体缺陷（缺少动作级形式化、只评估动作是否发生而非成功、真实对话覆盖有限），
  DuplexAct 逐条处理。把 DuplexAct 与 10-07 的
  [Coupled but Late](https://arxiv.org/abs/2610.08683)（模型间环路时序未必是人类的）、
  10-09 的 SteerablePlex（失控导致评测不可靠）连读，三天下来这条线的问题陈述已相当完整。
- **AR 长视频生成成为本批最大的聚集**：AIGC 视觉线 10 篇中有 7 篇在处理自回归视频的**历史与缓存**，
  沿三个维度展开——缓存决策（Frequency-Step Cache 把耦合的「同步/修复」两决策**分离**；
  FrameFold 从「按历史长度保留」转向**响应引导**整合）、缓存压缩（TempoKV 指出既有 KV 量化方法
  **专为 LLM 设计、迁移到视频效果差**）、预测时程（Prospective Forcing 指出自回归视频生成器
  **通常只被训练预测紧邻的未来**）。这条线本项目已连续追踪五天（10-05 ID-Forcing → 10-08 Memory Forcing → 今天）。
- **RL 十篇全在处理信号质量**，三类问题各自清晰：
  核心矛盾（统一广播 vs 额外评论家）；信号被压缩或失真（Many Right Answers 指出单参考设计
  把偏置写进奖励、RELAY 指出 rubric 塌缩成单一奖励且并列时**零梯度**、Double-Rollout 指出
  **正确答案可能并不由推理轨迹支撑**）；探索预算该投在哪
  （Variance-Optimal State Resampling 给出**闭式 Neyman 型解**，把预算分配从调参变成可计算问题）。
- **流匹配正在系统性入侵判别式任务**：本批 FLOMSS（源分离）、Prime-EVC（情感语音转换）、
  MSVAE（连续潜空间音乐语义）三篇分属不同子任务却同一范式。
- **具身线的力/接触成为独立主线**，五篇从数据（ForceWAM 解耦「未来」与「响应」学习）、
  表征（DEFT-VLA 指出定位阶段力信息无用甚至干扰、接触后才关键）、
  架构（Vision-Predictor-Action 用轻量 JEPA 预测器替换自回归解码器以提高**闭环控制频率**）三侧切入。
  效率侧的选择与 audio_lm 线 Diffuplex 的「多 token 前向」完全同构。
- **审计主题继续**：[WoVR+](https://arxiv.org/abs/2610.17922) 指出世界模型用于 RL 时
  **幻觉会误导策略优化**——预测误差会被策略当作真实后果来利用，因此 RL 会主动放大世界模型的分歧区域；
  [What Do Deepfake Audio Detectors Hear?](https://arxiv.org/abs/2610.17617) 追问检测器在语音与
  背景混合上究竟关注哪个（若在听背景，则针对语音的对抗攻击恰好打在盲区）；
  [Collapse, Repair, and Drift](https://arxiv.org/abs/2610.18192) 指出 CER 揭示了损失曲线看不到的
  **暂态崩塌与恢复**，意味着训练中途存在比起点终点都差的检查点。

## 2026-10-12

- **arXiv 批次窗口**：2026-10-09 UTC（截至 2026-10-12 17:00 CST，当天批次尚未发布；
  10-10/10-11 为周末无公告，故窗口较前次回溯 3 天）
- **扫描**：488 篇去重论文（cs.LG 193 / cs.CV 132 / cs.AI 128 / cs.CL 90 / cs.RO 61 /
  cs.SD 22 / eess.AS 22，其余为跨分类重复）
- **全文精读**：50 篇，抽取作者机构与 92 张论文原图
- **Wild-card**：本批 11 篇；**双工方向再次空窗**（10-08 无、10-09 三篇、10-12 无），audio_lm 用 6 个

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_embodied_entry.md) |
| 强化学习 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_rl_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-12/2026-10-12_rl_entry.md) |

### 当天最值得读的 3 篇

1. **[Does Location Matter? A Black-Box Causal Audit Reveals Model-Dependent Audio Grounding in LALM Hallucination](https://arxiv.org/abs/2610.13112)**（audio_lm #1）
   — **本项目日报审计线索的第四例，且审计对象升级为「领域标准做法本身」**。
   LALM 幻觉的主流缓解手段 Audio-Aware Decoding（AAD）通过对比真实音频 logits 与全零「空白」波形
   logits 运作——而**此前评审已把该空白波形标记为分布外（OOD）**。
   若参照物本身 OOD，抑制幻觉的机制就建立在一个无效前提上；作者用黑盒因果测试隔离幻觉来源，
   并揭示音频 grounding 是**模型相关**的。用 LALM 的团队应先做这个审计再继续用 AAD。
   前例：10-06 Mind the Execution Gap、10-07 World Models' Last Exam、10-09 Selective Listening。

2. **[Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models](https://arxiv.org/abs/2610.13212)**（embodied #1）
   — 出发点是一个观察：**动作说明机器人执行什么，但不描述这些命令将达成什么**——
   而 VLA 却主要通过预测动作块来学习。AFCE 让一个以未来为基准的物理**效果**成为主要预测目标。
   把预测目标从「命令」换成「结果」，是因为命令在多解任务上不唯一：同一目标可由多组动作达成，
   而其中只有一部分在当前状态下可执行。这是 10-08 日报
   「预测精度/动作相关性/目标达成度是三个不同的量」那条批判线的**第五次延续**。
   同线的 Grounded-Dreamer（世界模型合成数据 + 物理 grounding）与
   Dream to Remember（世界模型承担记忆角色、避免顺序任务下的遗忘）构成今日具身三强。

3. **[Generalized Proximal Policy Optimization: Unifying LLM RL Algorithms from the Perspective of Divergence](https://arxiv.org/abs/2610.13015)**（rl #1）
   — 对本项目日报追踪的 GRPO 生态做了根源性判断：主流 PPO 依赖一个**几何退化的裁剪代理**，
   它无法自适应对策略偏移的抵抗力，导致过早裁剪与探索退化；后续所有 GRPO 变体都在打补丁而非修根本。
   作者从**散度**视角统一 LLM RL 算法。
   同批 [Trajectory-Aware Policy Optimization](https://arxiv.org/abs/2610.13020) 给出同源的第二个诊断：
   既有方法在 token 或序列层面控制策略不匹配，但**局部不匹配会沿轨迹累积成严重的状态分布偏移**
   ——控制粒度不足是根本原因。两篇建议连读。

### 备注

- **⚡ 审计线索今天扩展到四条线、五篇论文**（本项目日报迄今最集中）：
  审计 AAD 这个标准缓解手段（2610.13112）；审计生成音乐裁判——
  其有效性只通过「与专家评分的相关性」验证，而这没说明裁判在响应音乐、文本提示还是提问方式
  （2610.13247，四个带对照的探针）；审计 UTMOS——发现它**倾向给口音更重的合成语音打更低分**，
  而用 UTMOS 筛选合成数据会在数据里进一步强化口音偏见形成闭环（2610.13175）；
  审计 ASR 数据增强——收益几乎总以聚合错误率报告，无法解释「为什么以及何时有帮助」
  （2610.13807，4 语言 × 5 数据规模 × 2 增强）；审计 MMDiT 的 image-to-text 反馈——
  它**保留**而非纠正已出现的对象与属性（2610.13941）。
  共同结论：这些被广泛使用的组件，其有效性前提从未被验证。
- **信用分配的细化是本批 RL 第二主题**，三篇同源：TreeHCA 指出事后信用分配的估计**依赖于轨迹中存在
  信息性替代方案**（这个前提正是它引入树式扩展的原因）；Beyond Temporal Proximity 指出标准 RL 按
  **时间邻近性**而非显式相关性传播奖励，在长延迟回报场景（推荐、机器人长程）必然出错；
  EmoGavel 补上「只监督最终偏好决策、不定位错误内容」的缺陷。
- **本周最连贯的一组对**：Unified Generative Video Compression（2610.13023，把双向与自回归变成同一框架下的参数）
  与 10-09 日报的 Conditional Residual Prediction（质疑「必须有双向教师」）——
  两者合起来指向**因果性与双向性不是二选一**。
- **⚠️ 双工方向本周第三次空窗**：10-08 无、10-09 三篇、10-12 无。这条线（用户的首要兴趣）
  在 arXiv 上确实是低频出现，无法靠抓取窗口调整解决。

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
