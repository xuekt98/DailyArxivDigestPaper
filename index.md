# ArXiv 论文日报索引

由 `mine-arxiv-daily-digest` skill 每日生成。每条记录包含当天各研究线的论文数，
以及当天最值得读的 3 篇。

**统计口径**：每次运行扫描 arXiv 的 7 个分类（cs.CV / cs.SD / eess.AS / cs.CL /
cs.AI / cs.RO / cs.LG），按 7 条研究线各出 10 篇排名报告（自 2026-10-21 起，
强化学习拆为 rl_core / rl_llm / rl_aigc 三条独立研究线）。

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
- **2026-10-24（周六）** — 探测 listing day 2026-10-23（窗口
  2026-10-22T18:00:00Z .. 2026-10-23T17:59:59Z）7 个分类**全部为 0 条**；
  无日期限制查询确认全库最新 v1 时间戳为 `2610.31671v1`（2026-10-22T17:59:53Z），
  恰为 listing day 2026-10-22 窗口的最后一刻——该批次已被
  [2026-10-23](daily_arxiv_digest/2026_10/2026-10-23/) 那份日报完整覆盖
  （705 条原始 / 535 篇去重），故不生成日报，以免与上一份重复。
  规律与 10-17 / 10-18 完全一致：**周五 14:00 ET 截止的批次要到下周一 00:00 UTC 才公告**
  （周末不公告），所以周六、周日两天必然为空窗。
  该批次预计在 **2026-10-26（周一）** 的运行中被取到 —— 周一运行的 listing day 会比
  常规的「运行当天减 1」再往前推一天（10-25 周日为空），届时应改用 `--auto` 探测。

## 目录

| 日期 | 扫描量 | AIGC 视觉 | AIGC 音频 | 语音 LM | 具身/世界模型 | 强化学习 | 当天最值得读 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [2026-10-23](daily_arxiv_digest/2026_10/2026-10-23/) | 535 | 10 | 10 | 10 | 10 | 10 / 10 / 10 | [奖励模型越准，下游反而越差](https://arxiv.org/abs/2610.30765) · [把运气从决策效应里拆开](https://arxiv.org/abs/2610.31544) · [纯文本 LLM 纠错会砸掉 13–32% 的正确转写](https://arxiv.org/abs/2610.30385) |
| [2026-10-22](daily_arxiv_digest/2026_10/2026-10-22/) | 568 | 10 | 10 | 10 | 10 | 10 / 10 / 10 | [偏好优化可以在崩塌中一路涨分](https://arxiv.org/abs/2610.29410) · [RL 微调的崩溃边界取决于 VAE 先验](https://arxiv.org/abs/2610.28849) · [世界模型该压缩到什么程度](https://arxiv.org/abs/2610.30129) |
| [2026-10-21](daily_arxiv_digest/2026_10/2026-10-21/) | 517 | 10 | 10 | 10 | 10 | 10 / 10 / 10 | [社区对 OPD 失效的主流解释是错的](https://arxiv.org/abs/2610.28586) · [偏好模型的分数里有多少不是「质量」](https://arxiv.org/abs/2610.28195) · [音频 LLM 到底有没有在听（机制层）](https://arxiv.org/abs/2610.28189) |
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

> **强化学习列的口径**：自 2026-10-21 起，`mine-arxiv-daily-digest` skill 升到 v0.3.0，
> 把强化学习拆成 **rl_core（算法/理论/MARL/sim-to-real）/ rl_llm（LLM 后训练与对齐）/
> rl_aigc（生成式内容模型的 RL）** 三条独立研究线，每条各 10 篇。
> 该日起的条目记作 `10 / 10 / 10`；**此前各日为一列合并计数**（合并线未按新口径重拆）。

> **批次窗口的口径（2026-10-22 起修正）**：arXiv 的投稿截止是美东 14:00（= UTC 18:00），
> 公告在次日 00:00 UTC 发出，所以 arXiv「new submissions for D」这一份公告里的论文，
> `published` 时间戳覆盖的是 **D-1 日 18:00:00Z 到 D 日 17:59:59Z**——**横跨两个 UTC 自然日**。
> 此前各日日报只取了 [D 00:00, D 17:59:59]，**漏掉了每份公告的前半段（D-1 傍晚 6 小时）**：
> 在 2026-10-21 公告上实测这占 7 个分类的 **21%**（789 篇中的 166 篇），且该段论文
> **不属于任何一天的窗口**，等于永久丢失。2026-10-22 起改用完整窗口
> （`scrape.py` 的 `window_bounds()`）；**此前各日的扫描量与论文数应视为下限**。

---

## 2026-10-23

- **arXiv 批次窗口**：**2026-10-22 listing day** = 2026-10-21 18:00:00Z – 2026-10-22 17:59:59Z
  （arXiv 00:00 UTC 公告的批次横跨两个 UTC 日：前一日 18:00 起算，当日 17:59:59 截止）
- **扫描**：705 条原始 / **535 篇去重**（cs.AI 206 / cs.LG 186 / cs.CV 113 / cs.CL 108 /
  cs.RO 67 / cs.SD 16 / eess.AS 9，其余为跨分类重复）
- **全文精读**：107 篇，抽取作者机构与 181 张论文原图（最终入库 **120** 张）
- **研究线**：**7 条**（skill v0.3.0 口径），每条各 10 篇，共 **70 篇**，全局无重复
- **Wild-card**：本批 **6 篇**（aigc_visual 0 / aigc_audio 3 / audio_lm 0 / embodied 0 /
  rl_core 0 / rl_llm 0 / rl_aigc 3）——比 10-22 的 7 篇再收敛 1 篇

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_embodied_entry.md) |
| 强化学习 · 核心算法 / 理论 / MARL / sim-to-real | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_rl_core_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_rl_core_entry.md) |
| 强化学习 · LLM 后训练与对齐 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_rl_llm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_rl_llm_entry.md) |
| 强化学习 · 生成式内容模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_rl_aigc_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-23/2026-10-23_rl_aigc_entry.md) |

### 当天最值得读的 3 篇

1. **[Scaling Laws for Generative Reward Models](https://arxiv.org/abs/2610.30765)**（rl_aigc #1）
   — **奖励模型越准，下游反而可能越差：静态判断准确率不决定在线优化质量。**
   这篇是本批最反直觉的一篇。在 Qwen3 奖励模型 0.6B–14B 的规模上，
   用 **GRPO** 训练的 **Thinking 裁判**静态 Gold 标签准确率**高于**用 SFT 训练的
   Answer-Only 裁判；但换成在线 DPO 去训策略，这个排序**在 8 组匹配设定中的 7 组里反转**——
   Answer-Only 奖励器给出更高的峰值与前五平均策略 Elo。更扎人的是，**中间的 Thinking 裁判
   checkpoint 作为奖励器时也能胜过更晚、静态准确率更高的 checkpoint**。
   作者把这命名为**评测者-奖励者鸿沟**：固定分布上的判断准确率并不决定下游优化质量。
   另一条工程结论同样重要：奖励模型容量有显著收益，**包括裁判比策略更大**的情形——
   这把奖励模型从「辅助模块」抬成了需要独立扩展的核心资产。
   作者自己列了三条限定（模型族、评测器、评审一致性），这种自我约束反而让结论更可信。
   **做奖励模型、GRPO / DPO 训练或评测器设计的人，这篇应该先读。**
2. **[Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.31544)**（rl_core #1）
   — **把「运气」从「决策效应」里拆开，rollout 需求从 Θ(Δ⁻²) 降到 Θ(Δ⁻¹)。**
   反事实分支通过重跑 episode 估计每个决策的信用，但分支**独立抽采样噪声**，
   于是结果差异混进了「决策的效果」和「后续的运气」。作者的观察很干净：在智能体搜索里
   检索器、语料、评分器都是确定性的，于是 episode 是决策与采样噪声的**确定性函数**——
   「孪生世界」（同样的噪声、不同的决策）是可实现的。TWICE 按 turn 与 line 键控 Gumbel 噪声，
   让反事实孪生体继承事实 episode 的下游噪声，把成对结果差异转成 turn 级优势。
   理论上孪生信用对任意耦合质量无偏，方差是独立反事实按 1-ρ 缩放；
   实践中解析一个大小为 Δ 的优势所需 rollout 数**从 Θ(Δ⁻²) 降到 Θ(Δ⁻¹)**。
   七个问答基准上，GRPO 的平均精确匹配在 Qwen2.5-3B / 7B 上分别提升 **5.3 / 4.5 点**，
   比 VinePPO 少用 **68%** 辅助 token。
   **做 agentic RL、信用分配或 GRPO 改进的人，这篇应该先读。**
3. **[Text-Only LLM Correctors Break Correct Transcripts](https://arxiv.org/abs/2610.30385)**（audio_lm #4）
   — **纯文本 LLM 纠错 ASR 输出，会砸掉 13–32% 本来就正确的转写。**
   用聚合 WER 评判纠错器，会把「修了什么」和「弄坏了什么」混在一起。这篇把每一次 WER 变化
   **精确分解**为 repaired tokens、damaged tokens 与 insertions，再据此追问源音频到底带来了什么。
   结论很硬：Gemini 2.5 Flash **纯文本**纠正自己的 draft 时破坏 **13–32%** 已正确的转写，
   **带上音频时只有 1–3%**。两种设定下都有 damage；repair 在「自己的 draft」上下降、
   在「独立识别器输出」上上升；在医疗口述上，保留下来的 insertions 会**抵消**净 WER 的收益。
   很少做编辑的开源 Voxtral 不呈现这个模式。作者也坦承两个分支 prompt 不同，
   所以这只是**界定音频影响的上下界**而非隔离它。
   **任何用「LLM 修 ASR 输出」这条 pipeline、或用 WER 下结论的人，都应该先读这篇。**

### 其他值得记的点

- **世界模型该为谁而训**（rl_core #7）：
  [DRILL](https://arxiv.org/abs/2610.30814) 指出世界模型被训练成预测下一帧像素，
  但它在 VLA 后训练里的角色是**产生能改进策略的学习信号**——两者错配且代价严重：
  **更低的像素 MSE 可能产生更差的策略梯度**，为策略效用训练的世界模型即使下一帧 MSE 高 **17%**
  也能给出更好的下游策略。DRILL 用双层框架（外层最大化内层 GRPO 更新后的策略回报）解决，
  闭式代理 DRILL-VWI 还能恢复元梯度 DRILL-IMG 的局部单步分量。五个操作仿真器上成功率相对 WMPO 提升 **13.1 点**。
- **「先记后做」把人形机器人从 29% 拉到 73%**（embodied #4）：
  [WholeBodyMem](https://arxiv.org/abs/2610.31166) 指出动态场景中的人形 loco-manipulation 是
  **非马尔可夫**的——线索会随物体变化或遮挡消失，也会因机器人转身而离开视野。
  它用 SAM3 跟踪任务物体、由物体事件**因果性地**挑关键帧（自适应预算），再由动作专家交叉注意力读取。
  仿真成功率 **29.1% → 72.6%**，Unitree G1 真机 **36.7% → 88.3%**。
  关键不是「记更多帧」而是「**保留对的帧**」。
- **显式 3D 优先的世界模型，57 倍加速**（embodied #1）：
  [DeXplicit](https://arxiv.org/abs/2610.30781) 先在度量 3D 中显式预测物体运动与形变，
  再把这些预测当作脚手架驱动视频渲染——渲染器只需补全新暴露的内容，不必再隐式学习世界动力学。
  移动点误差相对 PointWorld 降 **27–40%**，HOT3D 物体保真 IoU+ 提升 **47%**，
  两步因果生成相对 14B 双向配置 **57× 加速**。
- **监督也可以变便宜**（embodied #9）：
  [FastHarness](https://arxiv.org/abs/2610.31427) 用经验驱动的调度降低对 π0.5 策略的大模型审查频率
  （快路径随经验积累降频，恢复路径集中纠错），**策略保持冻结**。
  审查 token 平均降 **57.2%**，episode 时长从 **85.5 分钟降到 52.0 分钟**，
  而成功率从 **80% 升到 97.19%**——「既省又涨」的原因是审查频率自适应。
- **「少步即无损」这句话只在 FID / CLIP 下成立**（rl_aigc #8，wild-card）：
  [ParaLin++](https://arxiv.org/abs/2610.30704) 先审计了训练无关减步的质量指标：
  这些方法在 FID / CLIP 类指标下近乎无损，却在 **GenEval、DPG-Bench、LongTextBench**
  这类语义组合 / 密集指令 / 长文本渲染基准上**实质退化**。据此提出的步数奇偶并行采样器
  保留完整步数离散化、只解耦求解器的时间依赖，加速 **2.6×–4.8×**。
  **所有报告过加速倍数与 FID 的论文，都该补一遍这类语义基准。**
- **「等一下」不是 RL 教出来的**（rl_llm #5）：
  [Inherited, Not Invented](https://arxiv.org/abs/2610.30882) 追踪推理模型里 {wait} 标记的来源：
  **零 RL 几乎从不铸造它**，它随训练数据到来（OLMo-3 的中期训练、在推理轨迹上微调）。
  两个已发布的 RL-Zero 配方会**放大**它，同基座的**无 KL 的 GRPO 不会**；
  SFT 之后的 RL 几乎不改它，作者的 GRPO 反而**抹掉**由微调植入的标记。
  结论：标记频率本身不足以表明 RL 诱发的推理——顺手还提醒了 LLM-as-a-judge 在修订类指标上不可靠。
- **成对奖励评测有一半是盲的**（rl_llm #10）：
  [What Pairwise Evaluation Misses](https://arxiv.org/abs/2610.31090) 指出成对评测只比较同一 prompt 的
  两个响应，于是该 prompt 共享的分数分量**被抵消、从未被检验**。对 18 个已发布评分器的审计显示
  **分数按 prompt 聚集的程度远高于人类评分**（HelpSteer2 上 prompt 间占比 0.34–0.64，人类近零），
  且「聚集」本身并不表明与人类一致。作者建议分别检查 prompt 间变化、对错误 prompt 的敏感性与选择有用性。
- **两个方法学硬结论**（rl_llm #3 / rl_core #6）：
  [RWPO](https://arxiv.org/abs/2610.31239) 指出标准偏好优化把比较压成二元排序、**丢弃了「好多少」**，
  而在有连续奖励的组合优化里这个信息量最大；按奖励差加权后，OP 上 100–2000 节点规模超过 Compass 元启发式。
  [Converse Optimality Benchmarking](https://arxiv.org/abs/2610.30954) 则给 RL 评测补上了
  **认证过的最优值函数与最优策略**（只对学习者隐藏），让「到最优性的距离」第一次可观测。
- **视频编辑的奖励后训练**（rl_aigc #2）：
  [UniVOE](https://arxiv.org/abs/2610.31641) 用「移除驱动」同时训练物体移除与注入——
  训练好的移除器把真实有物体视频转成无物体配对，**为注入造出大规模监督**；
  再用专有奖励模型做后训练对齐人类偏好，因为像素级重建不足以刻画感知真实感。
- **路由 vs 适配**（rl_aigc #6）：
  [Route or Adapt](https://arxiv.org/abs/2610.31095) 在三个留出地图上比较测试时路由与奖励微调：
  **八种路由方案无一优于静态默认**，逐场景挑最优专家的 oracle 也只减少 **0.9 m** 偏移；
  而 20 个目标区域场景的奖励微调把车队平均偏移从 **12.4 m 降到 6.9 m**。
  附带一个值得警惕的诊断：有两个测试时自适应基线之所以偏移低，是因为产生了**退化轨迹**。
- **音频侧的两个硬数字**（audio_lm #4 / aigc_audio #7）：
  [Measuring the Verifier's Floor](https://arxiv.org/abs/2610.31470) 量化了 TTS 评测的地板误差：
  评测识别器**在人类录音上**仍漏掉 **33–67%** 的极罕见词，直接掩蔽这些词是有偏的
  （其他识别器在其上的 TTS 错误率高达 4–6%），且剩余错误可能一半是拼写变体，**仍需听辨测试**。
  [SyRA-CS](https://arxiv.org/abs/2610.31415) 则给出正面结论：合成代码切换语音的正确用法是
  **「学一个适配友好的初始化」**而非普通监督，用 Reptile 元学习 + 1 小时真实标注，
  16 个模型-语言对的 WER 全部优于持续微调，XLS-R 宏平均相对降低 **17.7%**。
- **产品级的语音克隆与基座模型**（aigc_audio #1 / audio_lm #1）：
  [HeyGen Voice](https://arxiv.org/abs/2610.30470) 把「谁在说」与「在哪儿说」分开
  （图像决定表达方式与声学环境、录音决定音色），在 Artificial Analysis 受控音色 TTS 榜以 **Elo 1201** 居首，
  盲测中用户克隆自己的声音时 **62% / 54%** 的投票选择它而非 ElevenLabs v4 与 Cartesia Sonic 3.6。
  [Spark-Audio 1.0](https://arxiv.org/abs/2610.31292) 用 0.65B 稠密音频编码器 + 30B-A3B MoE、
  1300 万小时音频数据，在国产算力上训练，支持 **99 种语言 / 202 种方言**，
  多语种识别与口语对话超过 Qwen3.5-Omni-Flash。
- **音频两条线是本批最薄的**（aigc_audio 3 个 wild-card、rl_aigc 3 个 wild-card）：
  本批 cs.SD 仅 **16** 篇、eess.AS 仅 **9** 篇，生成侧真实命中的音频工作只有 7 篇，
  rl_aigc 也只有 6 篇真实命中。两个 wild-card 数量都**超出 skill 规定的 1–2 名额**，
  已在报告开头与每条 wild-card 条目上逐条标注理由：
  aigc_audio 的 3 个是「音乐生成对齐评测 / 人声混音评判器 / 语音内容操纵取证」，
  rl_aigc 的 3 个是「扩散采样加速 / Elo 锦标赛给生成候选打分 / 扩散 LM 并行承诺选择」，
  均为同一生成模型方法族内与 RL / 奖励 / 选择机制最接近的邻居。
- **一条机构未标注的**（embodied #5）：
  [DiffDreamer](https://arxiv.org/abs/2610.31617) 的 PDF 文本层内**没有任何机构行**，
  因此机构标为 `[unverified]`，未做任何推测填充。


## 2026-10-22

- **arXiv 批次窗口**：**2026-10-21 listing day** = 2026-10-20 18:00:00Z – 2026-10-21 17:59:59Z
  （arXiv 00:00 UTC 公告的批次横跨两个 UTC 日：前一日 18:00 起算，当日 17:59:59 截止）
- **扫描**：789 条原始 / **568 篇去重**（cs.LG 224 / cs.AI 193 / cs.CV 137 / cs.CL 130 /
  cs.RO 74 / cs.SD 19 / eess.AS 12，其余为跨分类重复）
- **全文精读**：105 篇，抽取作者机构与 184 张论文原图（最终入库 **121** 张）
- **研究线**：**7 条**（skill v0.3.0 口径），每条各 10 篇，共 **70 篇**，全局无重复
- **Wild-card**：本批 **7 篇**（aigc_visual 1 / aigc_audio 2 / audio_lm 1 / embodied 0 /
  rl_core 0 / rl_llm 0 / rl_aigc 3）——比 10-21 的 19 篇大幅收敛

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_embodied_entry.md) |
| 强化学习 · 核心算法 / 理论 / MARL / sim-to-real | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_rl_core_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_rl_core_entry.md) |
| 强化学习 · LLM 后训练与对齐 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_rl_llm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_rl_llm_entry.md) |
| 强化学习 · 生成式内容模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_rl_aigc_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-22/2026-10-22_rl_aigc_entry.md) |

### 当天最值得读的 3 篇

1. **[ECHO: Emergent Common-Mode Hidden Offsets Drive Vocabulary Collapse in Preference Optimization](https://arxiv.org/abs/2610.29410)**（rl_llm #4）
   — **偏好优化可以一路涨分，同时正在走向生成坍缩。**
   这篇是本批最尖锐的一篇。作者把「排序指标在涨、生成却在坏掉」这个矛盾，
   追溯到**共模偏移**：隐状态里一个跨 token 位置、跨 prompt、同时移动 chosen 与 rejected
   表征的共享方向性位移。因为它把两个表征**一起**移动，相对排序损失对它的累积几乎不反应；
   等它增长到投影到输出层形成**词表井**，就会抬升单个 token 的概率直到主导解码。
   证据链很硬：孤立偏移本身就能重建词表井；把学到的偏移注入基座模型能复现坍缩，
   而**范数匹配的随机方向不能**；在损失里屏蔽共模成分即可阻止井形成。
   同一坍缩出现在 **17 个基座模型谱系中的 14 个**，且偏移在**教科书级 DPO 与 SimPO**（不成井）
   里就已存在——所以它不是坍缩的副产品，而是目标函数的结构性盲区。
   最后一击：在 17 次 UltraFeedback 运行中，**排名越好的运行，越少被公开奖励模型偏好于基座模型**。
   **任何用排序指标判断训练健康度的人，都应该先读这篇。**
2. **[When Do Gaussian Priors Fail? A Latent Geometry Investigation of RL Fine-Tuning](https://arxiv.org/abs/2610.28849)**（rl_aigc #5）
   — **RL 微调的崩溃边界，可能不是 RL 的问题，而是你的 VAE 先验在收租。**
   潜扩散模型几乎普遍用高斯先验。作者指出标准 VAE 的 KL 项**不只是忽略模式结构，
   而是主动对分离度与紧致度征税**；数据多模态时 ELBO 最优解把不同模式压进重叠潜空间，
   而 RL 微调会**放大**这种重叠（鞍区欠分辨、dynamic-to-variational 放大急升）。
   在真实的 alanine-dipeptide Boltzmann 分布上，高斯先验 VAE 在 beta_c = 0.224 崩溃，
   **模式跟踪的高斯混合先验在 0.00316 崩溃——同一流水线下 71 倍的差距**。
   作者用完全中介的因果识别（先验标签系数 0.995x，95% CI [0.79, 1.25]）把差距归到
   单一几何中介量 d_min/(2 sigma_0)，并做三源分解把放大定位到**学到的策略**
   （ODE 求解器零贡献）。结论是条件性的：**只有当潜几何会落入重叠且任务对覆盖敏感时，
   非高斯先验才是必需的**；而**覆盖率的平台期是模式分离先验的无条件收益，再多 RL 容量也换不回来**。
   **做潜扩散 RL 微调、VAE 先验设计或覆盖率评测的人，这篇应该先读。**
3. **[Rethinking Video Autoencoders for Interactive World Models](https://arxiv.org/abs/2610.30129)**（embodied #3）
   — **「世界模型该压缩到什么程度」第一次被当成一个设计问题来回答。**
   作者指出世界模型普遍直接复用文生视频生成器的自编码器——那些是为**离线生成**设计的
   （没有智能体在等），且在缺少训练数据与代码时无法换压缩率重训。
   他们构建 CADRE（因果扩散表征自编码器家族），在操作与导航两个领域各两个环境上
   用**同一个世界模型**训练每个自编码器，得到四条结论：强压缩下扩散解码器比感知回归更锐利；
   操作任务中**时间压缩放在自编码器里比放在世界模型里更有效**；
   **操作与导航需要相反的压缩**（相机静止时时间压缩代价很小，相机运动时则需要空间压缩）；
   以及最反直觉的一条——**相机静止时更粗的空间 token 对运动的伤害远大于对图像质量的伤害**。
   最后一条意味着**视觉质量指标会系统性掩盖运动退化**。
   代码、模型与在线 demo 均已公开。

### 其他值得记的点

- **一条最锋利的机制发现**（aigc_audio #1）：
  [Decodability Is Not Controllability](https://arxiv.org/abs/2610.29345) 在 VoxCPM2 上
  用位置匹配探针 + 等范数干预（30 说话人 / 60 组有向二元组）证明
  **高线性可解码性并不蕴含因果可控性**：参考音频状态在最终 RALM L7 层保留
  **0.970 探针准确率**，但对齐编辑产生 **0/60** 目标主导二元组；L0 处则达到 **60/60**。
  换言之，**说话人控制的位置是位置依赖的**——浅层可因果操纵，深层只能被动读取。
  凡是拿线性探针当因果证据的地方，这个反例都该摆上桌。
- **「让模型听着改会改坏」**（rl_aigc #6）：
  [Agentic Music Post-Production](https://arxiv.org/abs/2610.29093) 发现让近期多模态模型
  听并修改混音通常会**让混音变差**，所以真正的难点是可靠修正；他们的做法是把评判与参数建议分开，
  用 45,657 条从专业混音拟合出的修复批评做偏好优化，在 MedleyDB 上把误差降低 19%
  （其中偏好优化比纯监督训练再降 8.4%），人工听测质量高于 Qwen3-Omni / Gemini 3.8 Flash / GPT-4o-audio。
- **工具把答案写出来，模型就不推理了**（audio_lm #4）：
  [Derivation Depth Exposes Reasoning Failures in Tool-Augmented Music Analysis](https://arxiv.org/abs/2610.29060)
  固定音乐信息、只变推导深度：工具直接给结论时五个模型接近 100% 且**照答错答案**；
  隔一步时开源模型掉到 57–81%（而单独问那一步它们答得对），更深时 0%；**加上音频并不能恢复损失**。
- **触觉线连续第四批升温**（embodied #9）：
  [T-WLA](https://arxiv.org/abs/2610.28814) 指出接触条件**在视觉策略更新动作之前就已改变**，
  于是用共享视觉记忆 + 轻量触觉编辑器，在不重跑视觉分支的前提下修正未执行动作，
  手指关节 MPJPE 相对最强基线降 30%，真实灵巧操作平均成功率约 50%。
  配合 [CW-WAM](https://arxiv.org/abs/2610.30117)（把**接触力**作为世界动作模型的一等输出，
  1 mm 间隙方销插入成功率 25%→70%、电源适配器 40%→95%），
  「视觉慢、触觉快」这条线正在从传感器问题变成架构问题。
- **世界模型摊销的第三条支线**（embodied #3）：除 SuperMimic（跨动作）与 Ropedia（跨本体）之外，
  本批的 CADRE 把摊销问题推到了**自编码器压缩率**这一层——沿同一脉络，
  [AtomicRL](https://arxiv.org/abs/2610.30097)（rl_core #1）用「原子子任务 + 语义门控」
  抑制失败子任务的 TD 残差跨边界传播（信用污染），配合 Real2Sim2Real 让真实任务性能平均再提 21.3%。
- **RL 侧的三个反直觉结论**：
  [ReAPO](https://arxiv.org/abs/2610.28770) 指出独立随机 rollout 会**反复采样相似失败策略**，
  改用随机最短路视角给重试分配信用，在 Qwen3-0.6B 上以**少 39% 的生成 token** 达到 GRPO 两倍组大小的峰值准确率；
  [PhiBE-PI](https://arxiv.org/abs/2610.28915) 证明**更细的时间离散化不必然带来更好的策略**
  （逼近误差下降但统计误差上升）；
  [DoobPO](https://arxiv.org/abs/2610.28990) 用 Doob h-变换解决扩散/流策略**似然不可解**下
  PPO/GRPO 用不上的硬约束。
- **音频两条线依旧最薄**（aigc_audio 2 个 wild-card、audio_lm 1 个）：
  本批 cs.SD 仅 19 篇、eess.AS 仅 12 篇，真实命中的生成侧音频工作只有 8 篇、
  理解侧 9 篇。rl_aigc 同样紧张（7 篇真实命中 + 3 个 wild-card，超出 skill 规定的 1–2 名额 1 个），
  已在报告开头与条目中逐条标注理由。


## 2026-10-21

- **arXiv 批次窗口**：2026-10-20 UTC 00:00–17:59:59（arXiv 00:00 UTC 公告的批次 = 前一天截稿前的提交）
- **扫描**：517 篇去重论文（逐日原始 796 条：cs.AI 265 / cs.LG 178 / cs.CV 148 / cs.CL 96 /
  cs.RO 71 / eess.AS 10 / cs.SD 9，其余为跨分类重复）
- **全文精读**：93 篇，抽取作者机构与 162 张论文原图（最终入库 128 张）
- **研究线**：**7 条**（skill v0.3.0 起 RL 拆为三线），每条各 10 篇，共 **70 篇**
- **Wild-card**：本批 19 篇（aigc_visual 0 / aigc_audio 7 / audio_lm 2 / embodied 0 /
  rl_core 3 / rl_llm 0 / rl_aigc 7）

### 各研究线

| 研究线 | 篇数 | 报告 |
| --- | --- | --- |
| AIGC 图像/视频/3D 生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_aigc_visual_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_aigc_visual_entry.md) |
| AIGC 音频生成与编辑 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_aigc_audio_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_aigc_audio_entry.md) |
| 音频与语音语言模型 / 双工语音助手 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_audio_lm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_audio_lm_entry.md) |
| 具身智能与世界模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_embodied_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_embodied_entry.md) |
| 强化学习 · 核心算法 / 理论 / MARL / sim-to-real | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_rl_core_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_rl_core_entry.md) |
| 强化学习 · LLM 后训练与对齐 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_rl_llm_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_rl_llm_entry.md) |
| 强化学习 · 生成式内容模型 | 10 | [报告](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_rl_aigc_report.md) · [条目](daily_arxiv_digest/2026_10/2026-10-21/2026-10-21_rl_aigc_entry.md) |

### 当天最值得读的 3 篇

1. **[Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation](https://arxiv.org/abs/2610.28586)**（rl_llm #1）
   — **把社区对 OPD 失效的主流解释直接推翻了。**
   智能体 on-policy 蒸馏（OPD）在学生自己的轨迹上训练、由教师给每个 token 打分。
   社区的通行解释是**复合误差**：学生的错误把轨迹带出教师可靠的区域，
   于是近期方法用 episode-length 课程、教师引导回合、前缀重放、教师介入等手段把训练限制在该区域内。
   作者证明**这个解释不完整**：从学生偏离教师最多的那些状态出发，
   教师自己的接管仍然能完成任务，但按 token 打分训练的学生仍会耗尽回合。
   真因是 **next-token 打分的短视**——教师给每个 token 评分时看不到 episode 的结局，
   于是它的分数放行了「安全的、拖延的」动作，而结果导向的 RL 会用零奖励惩罚它们。
   R2S 因此把修复点从**训练数据**移到了**打分器**：先从未训练学生的高分歧状态跑教师接管，
   用接管结果反过来微调教师，再做普通 OPD。
   **任何在 OPD 上做局部改进的工作都应先确认自己修的是不是同一个病。**

2. **[Attractive Faces Skew Text-to-Image Reward Models and Leaderboards](https://arxiv.org/abs/2610.28195)**（rl_aigc #1）
   — **偏好模型的分数里，有相当一部分根本不是「质量」。**
   对人脸，**感知吸引力压过图像质量**：在受控用户研究中，标注者把更漂亮的脸评为更高质量，
   **哪怕拿来对比的是同保真度的真实照片**。隔离编辑 40 个人脸属性后，
   吸引力是 PickScore / MPS / HPSv2.1 / HPSv3 四个主流偏好模型的最强相关项，也是回归分析中的最强预测因子。
   换言之，当前 T2I 奖励模型与榜单在很大程度上奖励的是「生成更好看的人脸」，
   而这与「更符合提示词」没有必然关系——与本项目自 10-16 起追踪的「审计/评测工具有问题」线索直接接续。

3. **[Uncovering Audio-Text Alignment in Large Audio-Language Models through Cross-Modal Concept Neurons](https://arxiv.org/abs/2610.28189)**（audio_lm #1）
   — **「音频 LLM 到底有没有在听」这条三日线索在机制层收口。**
   10-19 的 VocalGrad 说声学信息在语言共现时用不上，10-20 的 Text Dominance 说转写可用时模型忽略副语言线索；
   本篇进一步问**机制**：是否存在一个音频与文本表示**对齐的共享子空间**？
   作者识别跨模态神经元并对其做因果测试（steering）。
   若共享子空间存在，那么「有转写就忽略声音」就不是全有全无的现象，
   而是**可定位、可干预**的局部行为——这比行为层的观察更进一步。

### 备注

- **⚠️ skill 升级到 v0.3.0：5 条研究线 → 7 条，50 篇 → 70 篇，10 个文件 → 14 个文件。**
  强化学习被拆成三条独立线，因为 RL 文献里其实有三个不同的社群——
  不同的基准（AlpacaEval vs GenEval）、不同的核心方法（PPO-clip vs 分类器引导）、不同的会场（NeurIPS/ACL vs CVPR/SIGGRAPH）；
  混在一条报告里只会得到「5 篇 LLM 对齐 + 5 篇扩散微调」，不如拆开。
  新增**方法学优先**原则：RL 论文归方法学线，不归领域线——
  音频 LM 上的 GRPO 归 `rl_llm`，视频扩散上的 RL 归 `rl_aigc`，机器人操作的 sim-to-real RL 归 `rl_core`。
  本批最典型的两例：LoCA（TTS 上的 RL）从音频线移入 `rl_aigc`；
  Attractive Faces（T2I 奖励模型）从视觉线移入 `rl_aigc`。
  **此前各日未按新口径重拆**，历史条目仍为合并计数。
- **⚠️ 批次窗口口径此前一直是错的，本次修正。**
  arXiv 的投稿截止是美东 14:00（= **UTC 18:00**），因此 00:00 UTC 公告的那一批覆盖的是
  **前一天 00:00–17:59:59 UTC** 的提交。此前按「自然日」过滤 `published`，
  会把**两个不同公告批次**拼进同一窗口；本批修正后为 517 篇（原报 501）。
  同时修掉了分页截断：单个分类在批次内超过 300 篇时（本次 cs.AI 有 265 篇唯一论文、
  逐分类原始 284 条）旧脚本只取首页，**此前各份日报的扫描量都因此偏少**。
  `scrape.py` 现在按分类翻页 + 显式套用 18:00 UTC 截止线。
  **历史条目的扫描量应视为下界。**
- **arXiv API 对 `submittedDate` 区间查询限流**：本轮排查中，
  `submittedDate:[... TO ...]` 形式的区间查询持续返回 **HTTP 429 / 503**，
  而普通 `cat:<分类>` 查询正常。管线已改为**按分类倒序拉取 + 本地按 v1 `published` 过滤**，
  并加入 429/503 退避重试与页面缓存；整批 9 次请求完成，速率限制仍为 3 秒以上。
  **今后抓取再次大面积失败，先检查是否又是区间查询。**
- **on-policy 蒸馏（OPD）在本批独占 rl_llm 的一半席位**，且从三个不同角度改进同一件事：
  [R2S](https://arxiv.org/abs/2610.28586) 修**打分器**（社区主流解释被推翻）；
  [Adaptive Pullback](https://arxiv.org/abs/2610.28194) 指出师生对数比惩罚的
  **当前取值不区分「持续的高惩罚」与「突然上升」**，并发现惩罚跳变处同时出现**教师置信度下降**；
  [OPTD](https://arxiv.org/abs/2610.28048) 发现**中间层的师生转移一致性可直接预测答案正确率**，
  据此加了一项几乎零成本的层间监督。
  另有 [Ask to Distill](https://arxiv.org/abs/2610.27450) 把「好问题」重新定义为
  「能在学生轨迹上逼出多少教师监督」，并证明这可在**全程不需要答案**的前提下学出来。
  **OPD 正在成为 LLM 后训练的新主线，值得单独追踪。**
- **一条隐形的偏好污染通道**：
  [Near-Duplicate Image Selection Transfers Preferences](https://arxiv.org/abs/2610.27943) 证明，
  仅仅**在近重复图像中做选择**（源照片与人工字幕固定、不使用任何目标特定提示），
  就能让偏好从策展者传给下游学生，在 LLaVA-1.5 / Qwen2.5-VL / Qwen3-VL / Gemma 4 上均出现方向性偏移。
  换言之，**任何做数据筛选的流程（包括 RLHF 里的偏好数据构造）都可能无意识写入策展者的偏好**——
  这是一条不依赖任何显式偏好标注的污染通道。
- **触觉子方向连续第三批升温**：本批同时出现三篇——
  [Tactile-ETA](https://arxiv.org/abs/2610.27613)（用上下文注入把触觉经验给进智能体，**不做任务特定训练**）、
  [HuTact](https://arxiv.org/abs/2610.27995)（**改用人类手-物交互数据**预训练触觉手部表示，绕开机器人触觉数据瓶颈）、
  [Physical Canvas](https://arxiv.org/abs/2610.28613)（把触觉放进**世界模型**并要求状态一致性）。
  三篇分别落在「数据从哪来」「表示怎么学」「模拟器怎么用」，构成了一个完整链条。
- **世界模型的两条摊销路线同时出现**：
  [SuperMimic](https://arxiv.org/abs/2610.28480)（CoRL 2026 Oral）用**一个可微世界模型**替换
  「一堆逐动作专家 + 有损蒸馏」，GPU 小时数下降**一个数量级以上**；
  10-20 日报的 [Ropedia](https://arxiv.org/abs/2610.26855) 则是**跨本体**摊销。
  两者回答的是同一个问题：如何把一次性的大规模训练变成一次性的可微模型复用。
- **AR 视频缓存线索接续**：[CALM](https://arxiv.org/abs/2610.28192) 指出各注意力层/头对 token merging
  的敏感度**不同但相关且跨提示稳定**，于是可用**离线校准**决定各层各头的合并比例，
  并证明注意力输出误差可作轻量代理——这是把「拍脑袋定统一比例」换成可测分配问题的做法。
  配套 [MoDDiT](https://arxiv.org/abs/2610.28086) 把「图像是稀疏的」这一被 DiT 丢掉的先验
  落成了可学习的 token 路由。
- **⚠️ rl_aigc 是本项目日报至今最薄的一次**：517 篇里真正做「RL / 偏好优化用于生成式内容模型」的
  只有 3 篇（Attractive Faces、LoCA、DeCert），该线用了 **7 个 wild-card**，
  超出 skill 规定的 1–2 个名额——已逐条标注理由。
  仍值得看 [DeCert](https://arxiv.org/abs/2610.27528)：它在**没有参考答案**的情况下构造偏好监督，
  办法是利用**同一批正确判定之间「理由质量」的差异**——
  这对文生图这类「本就没有唯一答案」的生成任务尤其有价值。
- **aigc_audio 连续第二次极薄**（cs.SD 仅 9 篇、eess.AS 仅 10 篇），该线用了 7 个 wild-card。
  仍值得看 [LoCA](https://arxiv.org/abs/2610.28035)：它指出 TTS 用 RL 的真正痛点是
  **句子级奖励定位不了局部错误**，解法是用 ASR 对齐把内容错误定位到声学帧上再重分配优势，
  在 VoxCPM2 上把样本加权内容误差相对预训练骨干降 **20.5%**。
- **一个被量化的物理建模陷阱**：
  [Differentiable Karplus-Strong](https://arxiv.org/abs/2610.28043) 通过梯度分析发现
  **标准频谱损失对起音时间不提供有意义的方向性梯度**——
  这直接解释了为什么物理建模合成里的参数长期不可辨识（是系统性的，不是调参问题）。
- **一个「零代价增益」的范例**：
  [Slots Are Not Speakers](https://arxiv.org/abs/2610.28053) 指出流式 diarizer 的 N 个槽位限制的是
  「能同时表达几个人」而非「会遇到几个人」，用**只重标注**的因果 linker
  （不引入任何额外漏检）把 4 槽主干在超限部分的 DER 从 **36.8%** 降到 **22.6%**，
  在 23 人庭审场景把 cpWER 从 **82.7%** 降到 **24.4%**。

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
