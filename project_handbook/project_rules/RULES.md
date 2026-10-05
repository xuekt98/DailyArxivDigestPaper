# 项目规则 (daily-arxiv-paper)

> 由 `mine-init-codex-project` skill 生成于 2026-10-05。
> 整体性的项目说明见仓库根目录的 `AGENTS.md`；本文件聚焦“操作约束”。

---

## 临时文件

Codex 在阅读 PDF、写代码、跑实验等过程中产生的所有中间产物，统一存放在仓库根目录下的 ```codex_temp/``` 文件夹内。

- 不在子项目目录里散落 `.log`、缓存、截图、转换后的图片等临时产物。
- 不在仓库根目录直接创建临时文件。
- 临时文件不进 git：`codex_temp/` 的内容已在 `.gitignore` 中忽略（仅保留 `.gitkeep` 让目录结构可见）。

**适用范围**：仅约束“Codex 操作产生的临时产物”。用户主动提交到仓库的结果文件（如 `results/`、`images/` 等）不受此规则限制。

**示例**（应放进 `codex_temp/`）：
- 阅读 PDF 时生成的中间图片 / 文本切片
- 跑实验时输出的 `.log`、调试图、临时 checkpoint
- 写代码时的草稿脚本、一次性的数据预处理脚本
- 其它任何“用完即可丢弃”的中间产物

---

## 危险命令禁令

> Codex 在 Windows / PowerShell 环境下做路径操作时，必须遵守以下 8 条硬规则。
> 背景：2026-08-13/14 的 `cmd /c "rmdir /S /Q \"<path>\""` 级联删盘事故——同样形态的坏命令（含空格路径 + `cmd /c` + 转义尾引号）三连发，删掉了 `X:\` 上多个目录。这套规则就是那次事故后沾淀的防御层。

### 8 条硬规则（无例外）

1. **永不使用 `cmd /c` 做路径操作**——`cmd /c` 路径解析规则与 PowerShell 的 `"` 转义互不兼容，会级联删盘。用 PowerShell 原生命令。
2. **永远用 `-LiteralPath`**——避免 `[` / `*` / `?` 被当成通配符。
3. **永远单引号包裹路径**——防止 `$variable` 展开和反引号转义歧义。
4. **永远不要 `cd X:\` 之后再做破坏性命令**——cwd 是爆破半径。
5. **沙盒优先**——任何新的破坏性命令先在 `X:\__test__\` 试，**目标外**放 marker 文件；marker 存活就说明没级联。
6. **先计数再删除**——`Get-ChildItem -LiteralPath <path> -Recurse | Measure-Object` 必须等于目标真实文件数，才能 `-Recurse -Force`。
7. **陌生破坏性命令前先备份**——`Copy-Item -LiteralPath <src> -Destination <backup> -Recurse`。
8. **不要把多个路径同时传给 `cmd /c`**——即便加了引号。

### Drop-in 替换模板

```powershell
# DELETE a tree (recursive, force, no prompts)
Remove-Item -LiteralPath 'X:\path with spaces\中文\sub' -Recurse -Force

# DRY-RUN first (count items that would be touched)
Get-ChildItem -LiteralPath 'X:\path with spaces' -Recurse -Force |
    Measure-Object | Select-Object Count

# MOVE
Move-Item -LiteralPath 'X:\src' -Destination 'X:\dst'

# COPY
Copy-Item -LiteralPath 'X:\src' -Destination 'X:\__backup__\src-<timestamp>' -Recurse

# DELETE with safety wrapper (see below)
Remove-PathSafely -Path 'X:\path with spaces'
```

### `Remove-PathSafely` 包装函数

加到 `$PROFILE`（或粘贴到当前 session）：

```powershell
function Remove-PathSafely {
    [CmdletBinding(SupportsShouldProcess, ConfirmImpact='High')]
    param([Parameter(Mandatory)][string]$Path, [switch]$Force)
    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Warning "Path does not exist: $Path"
        return
    }
    $n = (Get-ChildItem -LiteralPath $Path -Recurse -Force |
           Measure-Object).Count
    if ($PSCmdlet.ShouldProcess("$Path (-Recurse, $n items)", 'Remove-Item')) {
        Remove-Item -LiteralPath $Path -Recurse -Force:$Force
    }
}
```

`-Confirm` 首次使用时会提示；`-WhatIf` 走 dry-run。

### `cmd /c` 不可避免时的回退

用 **call operator**（`&`）+ 数组参数，每个元素都是独立的 `argv` 项，不再走 shell 风格的引号解析：

```powershell
& cmd.exe /c rmdir /S /Q 'X:\path with spaces' 'X:\another'
```

**绝不**把带引号路径的命令塞进 PowerShell 双引号字符串。

### 背景：`cmd /c` 为什么不安全

`cmd /c` 处理 `"` 时有两条互相竞争的规则：

| 规则 | 触发条件 | cmd 的行为 |
|---|---|---|
| Rule 1 | 恰好 2 个 `"`、无 `&<>()@^\\|`、看起来像可执行路径 | 保留引号原样 |
| Rule 2 | 其他 | 去掉首尾两个 `"`，重新解析剩余 |

PowerShell 的 `\"` 对 PowerShell 来说**不是**转义序列——它是字符串值里的字面两个字符 `\` + `"`。当这个字符串被传给 `cmd /c`，cmd 看到超过 2 个 `"`，Rule 1 不触发，Rule 2 触发，cmd 剥掉外层一对引号后重新解析。重新解析出来的字符串往往不是预期。如果解析出来的路径是空或 glob，`rmdir /S /Q` 就会沿着 `cwd`（经常是 `X:\`）递归——这就是级联。

---

<!--
TODO: 在下面继续追加本项目特有的规则，例如：
  - 构建 / 测试 / Lint 命令
  - 提交信息格式
  - 目录布局约定
  - 第三方依赖 / 虚拟环境管理
-->
