# 项目架构 (daily-arxiv-paper)

> 由 `mine-init-codex-project` skill 生成于 2026-10-05。
> 本文件说明项目的组织架构：目录划分、模块职责、依赖关系与数据流向。

## 目录划分

```
daily-arxiv-paper/
├── index.md                       # 累计索引：每天追加一行摘要 + 目录链接
├── daily_arxiv_digest/            # 所有日报的存放根目录
│   └── <YYYY_MM>/                 # 按月份分组，如 2026_10
│       └── <YYYY-MM-DD>/          # 当天报告目录（已存在则不覆盖）
│           ├── <date>_<track>_report.md   # 5 份排名报告
│           ├── <date>_<track>_entry.md    # 5 份条目目录（shields.io 徽章）
│           └── res/                       # 当天图片资源（各 track 共享）
├── codex_temp/                    # 中间产物：PDF、脚本草稿、phase1/3/4 审计留痕
└── project_handbook/              # 本手册
```

**5 条研究线**（`track` 标识）：`aigc_visual`、`aigc_audio`、`audio_lm`、
`embodied`、`rl`，每条线每天各出 10 篇。

## 数据流向

```
arXiv API (7 分类, 3 秒限速)
  → codex_temp/phase1_listing.md + phase1_papers.json   # 抓取
  → codex_temp/downloads/*.pdf                          # 精读候选（用后即删）
  → codex_temp/figures/<id>/*.png                       # 抽机构 + 抽图
  → codex_temp/phase3_relevance.md                      # 相关性打分
  → codex_temp/phase4_ranking.md                        # 5 线各 top-10
  → daily_arxiv_digest/<YYYY_MM>/<YYYY-MM-DD>/*.md      # 报告 + 条目
  → index.md                                            # 追加当天摘要
```

报告内图片一律用**相对路径** `res/<id>_<name>.png` 引用，因此整块目录可自由移动，
图片引用不会失效。

## 运行方式

由 `mine-arxiv-daily-digest` skill 驱动（6 个 phase：scraper → reader → filter →
ranker → reporter → cleanup）。可复用脚本保留在 `codex_temp/`：`fetch_all.py`、
`triage.py`、`extract_figs4/5*.py`、`merge_figs.py`、`add_captions2.py`、
`build_reports.py`、`paperdata.py`。

**注意**：arXiv 周末不公告。若运行当天批次尚未发布，按 skill 的失败恢复规则把窗口
放宽到最近一个已公告批次，并在报告头部标注实际批次窗口。
