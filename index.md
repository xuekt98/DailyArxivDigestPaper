# ArXiv 论文日报索引

由 `mine-arxiv-daily-digest` skill 每日生成。每条记录包含当天各研究线的论文数，
以及当天最值得读的 3 篇。

**统计口径**：每次运行扫描 arXiv 的 7 个分类（cs.CV / cs.SD / eess.AS / cs.CL /
cs.AI / cs.RO / cs.LG），按 5 条研究线各出 10 篇排名报告。

## 目录

| 日期 | 扫描量 | AIGC 视觉 | AIGC 音频 | 语音 LM | 具身/世界模型 | 强化学习 | 当天最值得读 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [2026-10-05](daily_arxiv_digest/2026_10/2026-10-05/) | 648 | 10 | 10 | 10 | 10 | 10 | [ID-Forcing (长视频 KV-provenance)](https://arxiv.org/abs/2610.03120) · [JEPA 可规划性诊断](https://arxiv.org/abs/2610.03137) · [AURAL 隐式推理降延迟 11.8x](https://arxiv.org/abs/2610.01560) |

---

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
