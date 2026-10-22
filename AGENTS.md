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

本项目收纳**每日 arXiv 论文日报**：抓取 7 个分类（cs.CV / cs.SD / eess.AS / cs.CL /
cs.AI / cs.RO / cs.LG）的最新公告批次，按 **7 条研究线**各出 top-10 排名报告与条目目录。

7 条研究线（`mine-arxiv-daily-digest` skill v0.3.0 起的划分）：

| track | 覆盖范围 |
| --- | --- |
| `aigc_visual` | AIGC 图像 / 视频 / 3D 生成与编辑 |
| `aigc_audio` | 音频生成、TTS、音乐（仅生成，不含语音理解/LM） |
| `audio_lm` | 音频与语音语言模型、双工语音助手 |
| `embodied` | 具身智能与世界模型 |
| `rl_core` | RL 算法与理论、多智能体 RL、sim-to-real |
| `rl_llm` | LLM 后训练的 RL：RLHF / DPO / GRPO / RLAIF / RLVR |
| `rl_aigc` | 生成式内容模型的 RL：扩散/流匹配 RL、生成式奖励模型 |

**方法学优先**：RL 论文归方法学线，不归领域线——音频 LM 上的 GRPO 归 `rl_llm`，
视频扩散上的 RL 归 `rl_aigc`，机器人操作的 sim-to-real RL 归 `rl_core`。

```
daily_arxiv_digest/<YYYY_MM>/<YYYY-MM-DD>/
├── <date>_<track>_report.md   # 10 篇/线，含摘要、作者机构、关键图表
├── <date>_<track>_entry.md    # shields.io 条目目录（mine-create-paper-entry 格式）
└── res/                       # 论文原图，命名 <arxiv_id>_{framework,result}.png
index.md                       # 累计索引：每日一行摘要 + 各日详情章节
codex_temp/<date>/             # 每次运行的临时目录，报告写完后整体清理
```

**管线脚本**已固化在 `project_handbook/project_tools/digest/`：

- `scrape.py` — 探测最新公告批次（可回溯数日，处理周末/节假日空档）、
  逐（分类 × 日）抓取以避免 `max_results` 截断、按研究线做关键词预筛。
  用法：`python scrape.py --out codex_temp/<date> --auto 6`（或 `--days 20261015,20261016`）
- `read.py` — 3 秒限速下载 PDF，抽取作者机构、贡献句与关键图（图注区域裁剪），
  产出 `phase2_cards/<id>.json`。用法：`python read.py --out codex_temp/<date>`
  （shortlist 由当次运行写入 `codex_temp/<date>/shortlist.json`）

每次运行的**相关性打分、排名与报告分析**是人工撰写的，存放在当次
`codex_temp/<date>/render.py`（随临时目录清理，不入库）。

⚠️ arXiv 的公告存在**时区滞后与周末空档**：中文标准时间下午运行时，
最新可用批次通常是前一天的 UTC 日。若探测发现当日及近几日均为空，
**不生成日报**（避免与上一份重复），仅在 `index.md` 的「跳过记录」中登记原因。

⚠️ **批次窗口横跨两个 UTC 日：[D-1 18:00:00, D 17:59:59] UTC**：arXiv 的投稿截止是
美东 14:00（= UTC 18:00），公告在美东 20:00（= 次日 00:00 UTC）发出。所以 arXiv
「new submissions for D」这一份公告里，`published` 时间戳覆盖的是
**D-1 日 18:00 起到 D 日 17:59:59 止**——它横跨两个 UTC 自然日。

- 只按 `published` 的自然日过滤，会漏掉每份公告的前半段（D-1 傍晚 6 小时）。
  在 2026-10-21 公告上实测这占 7 个分类的 **21%**（789 篇里的 166 篇），
  且该段论文不属于任何一天的窗口，等于永久丢失。
- 必须显式套用 `scrape.py` 的 `window_bounds(listing_day)`。

命名口径：

- **日报目录名 = 运行当天**（= 公告日 = listing 日 + 1）
- **报告内标注的 listing 日** = arXiv「new submissions for D」的 D
- 2026-10-22 起启用该口径；此前各日日报只覆盖了 [D 00:00, D 17:59:59]，
  属欠覆盖，详见 `index.md` 的「批次窗口口径」说明块。

## 使用约定

<!-- TODO: 列几条本项目特有的约定，例如：构建命令、测试入口、提交前自检、依赖管理等。操作约束与危险命令禁令请写到 `project_handbook/project_rules/RULES.md`。 -->