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
cs.AI / cs.RO / cs.LG）的最新公告批次，按 5 条研究线（AIGC 视觉 / AIGC 音频 /
音频与语音 LM / 具身与世界模型 / 强化学习）各出 top-10 排名报告与条目目录。

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

## 使用约定

<!-- TODO: 列几条本项目特有的约定，例如：构建命令、测试入口、提交前自检、依赖管理等。操作约束与危险命令禁令请写到 `project_handbook/project_rules/RULES.md`。 -->