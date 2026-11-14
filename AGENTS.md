# daily-arxiv-paper

Daily arXiv paper collection, filtering, summarization, and reading notes.

> Initialized by the `mine-init-codex-project` skill on 2026-10-05.
> Edit this file to describe your project's structure, conventions, and any
> durable team agreements Codex should follow when working in this repo.

## Project Handbook

项目根目录下的 `project_handbook/` 是 Codex 在每个新会话开始时默认读取的项目手册。**Codex 在开始任何工作前，都应自动加载以下文件：**

- `project_handbook/project_architecture/ARCHITECTURE.md` — 项目的组织架构、目录划分、模块边界与依赖关系。
- `project_handbook/project_rules/RULES.md` — 项目级操作规则，包含 Windows / PowerShell 路径安全禁令。
- `project_handbook/project_skills/` — 项目本地 skills 的存放目录；按需读取其中的 skill 文件。
- `project_handbook/project_tools/` — 仅在根据本项目需要定制的 tools 存放目录；按需读取使用。

**危险命令**：Windows / PowerShell 环境下不要用 `cmd /c` 做路径操作，要用 PowerShell 原生命令 + `-LiteralPath` + 单引号包裹路径，详见 `project_handbook/project_rules/RULES.md` “危险命令禁令” 一节。

临时文件统一放在仓库根目录下的 `codex_temp/`（已在 `.gitignore` 中忽略其内容）。

## Remote Mirror (optional)

<!-- 如果项目启用了远程 GPU 镜像（运行 init_project.py 时使用了 --remote-path），下面会被替换为真实路径。 -->
<!-- 默认占位文本：项目尚未配置远程镜像。如需启用，请运行： -->
<!-- python scripts/init_project.py . --remote-path /share/home/xuekt/projects/<your-project>/ -->

> 项目当前**未配置远程 GPU 镜像**。如需在远程 SLURM 集群上跑训练/测试，运行：
>
> ```bash
> python scripts/init_project.py . --remote-path /share/home/xuekt/projects/<your-project>/
> ```
>
> 这会 SSH 到 `10.21.20.154` 并创建远程 `<remote-path>/codex_temp/`。
> 远程项目根目录需要你提前建好。

## 项目结构

本项目收纳**每日 arXiv 论文日报**：抓取 8 个分类（cs.CV / cs.SD / eess.AS / cs.CL /
cs.AI / cs.RO / cs.LG / cs.IR）的最新公告批次，按 **4 个 axis × 10 个 direction**
各出排名报告与条目目录，当天目标 **60 篇**。

现行口径（`mine-arxiv-daily-digest` skill **v0.8.0**，自 2026-11-09 起）：

| axis | direction | 覆盖范围 |
| --- | --- | --- |
| `aigc_visual` | `aigc_generation` / `aigc_editing` / `aigc_rl` | AIGC 图像 / 视频 / 3D / 4D 生成与编辑，含面向视觉生成的 RL、偏好优化与奖励模型 |
| `llm_vlm` | `llm_core` / `vlm_core` / `llm_vlm_rl` | LLM 本体（架构 / 训练 / 推理效率 / 长上下文 / 评测）、VLM 本体（多模态理解 / GUI / 文档）、以及两者的 RL 与偏好优化 |
| `duplex_speech` | `duplex_speech_core` / `speech_rl` | 全双工 / 实时 / 流式语音 LM、speech-to-speech、语音助手、TTS / 克隆 / 转换；语音与音频 LM 的 RL（GRPO / DPO / 语音奖励模型） |
| `world_embodied` | `world_model` / `embodied_ai` | 世界模型（JEPA / 潜动力学 / 模型式 RL）+ 具身 AI / VLA / 机器人学习，含面向具身任务的 RL |

**口径变更**：

- **2026-11-09 起（v0.8.0）**：7 条 track（v0.3.0）/ 4 条 track（v0.4.0）合并为
  **4 个 axis × 10 个 direction**；**新增 `llm_vlm` 轴**（LLM / VLM 及其 RL），
  原 `speech_rl` 降为 `duplex_speech` 轴内的一个 direction；分类从 7 个增至 8 个
  （加入 `cs.IR`）。2026-11-06 及更早的日报仍按旧口径，未改写。
- **2026-11-06 起（v0.4.0）**：7 条线合并为 4 条线——原 `rl_aigc` 并入 `aigc_visual`、
  原 `rl_core` 并入 `world_embodied`、`rl_llm` 与纯文本 LLM 的 RL 退出跟踪范围，
  语音合成并入 `duplex_speech`，纯音乐生成降级为 wild-card。

**方法学优先**：视觉生成侧的 RL 归 `aigc_visual` 轴，具身任务的 RL 归 `world_embodied` 轴，
语音 / 音频 LM 的 RL 归 `duplex_speech` 轴的 `speech_rl` direction；
**纯文本 LLM 的 RL 不再是独立跟踪线**，但当它服务于 VLM 或作为
`llm_vlm_rl` direction（多模态 RLHF / DPO / GRPO、奖励模型、reward hacking）时仍会入选。

**两级弹性配额**：

- **axis 级**：`AXIS_BASE = {aigc_visual:15, llm_vlm:18, duplex_speech:12, world_embodied:15}`
  （合 60），单个 axis 上限 `AXIS_CAP = 20`；富余名额按富余量依次重分配到候选最充裕的 axis。
- **direction 级**：`DIR_BASE = {aigc_generation:8, aigc_editing:4, aigc_rl:3, llm_core:8,
  vlm_core:5, llm_vlm_rl:5, duplex_speech_core:8, speech_rl:4, world_model:7, embodied_ai:8}`；
  薄 direction **让出名额而不是被填充**（`speech_rl` 发不满是正常结果，不得凑数）。
- **wild-card**：每 direction 1–2 条，须在报告开头声明数量与原因，
  并逐条标注 `[wild-card=yes]`。
- 评分 `final = 0.7 × relevance + 0.3 × quality`；`relevance >= 9` 必进。

```
daily_arxiv_digest/<YYYY_MM>/<YYYY-MM-DD>/
├── <date>_<axis>_report.md   # 每 axis 一份，含摘要、作者机构、关键图表，direction 为子节
├── <date>_<axis>_entry.md    # shields.io 条目目录（mine-create-paper-entry 格式）
└── res/                       # 论文原图，命名 <arxiv_id>_{framework,result}.png
index.md                       # 累计索引：每日一行摘要 + 各日详情章节
codex_temp/<date>/             # 每次运行的临时目录，报告写完后整体清理
```

**管线脚本**已固化在 `project_handbook/project_tools/digest/`：

- `scrape.py` — 探测最新公告批次（可回溯数日，处理周末/节假日空档）、
  逐（分类 × 日）抓取以避免 `max_results` 截断、按 axis 做关键词预筛。
  用法：`python scrape.py --out codex_temp/<date> --auto 6`（或 `--days 20261015,20261016`）
- `read.py` — 3 秒限速下载 PDF，抽取作者机构、贡献句与关键图（图注区域裁剪），
  产出 `phase2_cards/<id>.json`。用法：`python read.py --out codex_temp/<date>`
  （shortlist 由当次运行写入 `codex_temp/<date>/shortlist.json`）
- `pipeline.py` — axis/direction 维度的选稿与渲染器。子命令依次为
  `pool`（建候选池与 task 词表）→ `vocab` → `select`（两级配额校验）→
  `spec`（生成 `meta_spec.md` 与分工文件）→ `checkmeta` → `render` → `verify`。

每次运行的**相关性打分、排名与报告分析**是人工撰写的：选稿输入在
`codex_temp/<date>/selection_input.json`，分析元数据由 5 个 `meta_*.py` 模块产出，
机构核对结果写在 `codex_temp/<date>/orgs.json`（临时目录清理时一并删除，不入库）。

⚠️ arXiv 的公告存在**时区滞后与周末空档**：中文标准时间下午运行时，
最新可用批次通常是前一天的 UTC 日。若探测发现当日及近几日均为空，
**不生成日报**（避免与上一份重复），仅在 `index.md` 的「跳过记录」中登记原因。

⚠️ **批次窗口横跨两个 UTC 日，且截止时刻随美东夏令时变化**：arXiv 的投稿截止是
美东 14:00，公告在美东 20:00 发出。**美东 14:00 只在夏令时（EDT, UTC-4）等于
UTC 18:00；美东自 2026-11-01 起进入冬令时（EST, UTC-5），同一时刻变成 UTC 19:00。**
所以 arXiv「new submissions for D」这一份公告里，`published` 时间戳覆盖的是
**D-1 日的美东 14:00 起到 D 日的美东 14:00 止**——它横跨两个 UTC 自然日，
且不是一个固定的 UTC 瞬间。

- 窗口口径：**EDT 期 `[D-1 18:00Z, D 18:00Z)`，EST 期 `[D-1 19:00Z, D 19:00Z)`**。
  必须显式套用 `scrape.py` 的 `window_bounds(listing_day)`（内部按日期解析美东偏移，
  见 `deadline_utc()`），**不要硬编码 18:00**——2026-11-01 之前硬编码是对的，
  之后会每批漏掉最后一小时、并重复前一小时（该缺陷造成 2026-11-03 ~ 11-06
  四份日报共漏掉 129 篇，详见 `index.md` 跳过记录中的修正说明）。
- 只按 `published` 的自然日过滤，会漏掉每份公告的前半段（D-1 傍晚 6 小时）。
  在 2026-10-21 公告上实测这占 7 个分类的 **21%**（789 篇里的 166 篇），
  且该段论文不属于任何一天的窗口，等于永久丢失。
- ⚠️ **公告可见 ≠ API 索引已回填**：合并批次 / 大批次公告后，arXiv API 的
  `submittedDate` 检索索引可能要用**将近一天**才补齐。2026-11-13 10:00 CST 查
  listing day 2026-11-11 只得到 77 篇，24 小时后同一个窗口变成 393 篇，
  listing day 2026-11-12 从 0 篇变成 421 篇（合计 814 篇才是完整批次）。
  **因此每轮除 `--auto 6` 外，还要显式回探前一个 listing 日窗口**，
  确认规模是否还在增长；已发过的论文要从后续批次里排除，避免重复。
  跨窗口合并批次用 `--days <较早那天>,<较晚那天>` 一次抓全。

命名口径：

- **日报目录名 = 运行当天**（= 公告日 = listing 日 + 1）
- **报告内标注的 listing 日** = arXiv「new submissions for D」的 D
- 2026-10-22 起启用该口径；此前各日日报只覆盖了 [D 00:00, D 17:59:59]，
  属欠覆盖，详见 `index.md` 的「批次窗口口径」说明块。

## 使用约定

<!-- TODO: 列几条本项目特有的约定，例如：构建命令、测试入口、提交前自检、依赖管理等。操作约束与危险命令禁令请写到 `project_handbook/project_rules/RULES.md`。 -->