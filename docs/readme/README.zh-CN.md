# Cookbook by Pengusto

项目名称：**Cookbook by Pengusto** · GitHub 仓库：[`pengusto/cookbook`](https://github.com/pengusto/cookbook)。

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme/cookbook-banner-storybook-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="../../assets/readme/cookbook-banner-storybook-v3.png">
  <img alt="AI 生成插图：Cookbook 企鹅在一本打开的食谱中展开的奶油色与酒红色厨房里烹饪，旁边摆着工作流配方卡片。" src="../../assets/readme/cookbook-banner-storybook-v3.png">
</picture>

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

**为编程对话的下一步选一道配方。**

Cookbook 为使用 Codex 或 Claude Code 的开发者提供 20 个专注的工作流：规划项目、检查进展、在休息后找回上下文、分享前审查，以及整理有用的交接。按需选择配方，由宿主和模型执行工作。

选择**直白问题**或**厨房名称**。两种风格由同一份维护中的指令生成；每个宿主安装一种命名风格。

**实验性公开 Beta · 0.7.3.** [浏览配方](https://pengusto.github.io/cookbook/cookbook.html) · [Plain](https://pengusto.github.io/cookbook/cookbook-plain.html)

## 快速开始：选择一种命名风格

请先安装 Codex 和/或 Claude Code 并登录。示例安装 Kitchen；在 Codex 中使用 Plain 时指定 `--ref plain`。两种命名风格共用一个插件标识，因此一次只安装一种。构建软件包不会更改宿主安装。

Codex — 无需本地构建：

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

安装后，打开新的 Codex 会话并尝试：

```text
$show-me-the-kitchen 解释 Cookbook，并推荐一个适合在长时间暂停后重新进入项目的工作流。
```

指南只解释和推荐，不会执行推荐的工作流。使用 Plain 时，安装时指定 `--ref plain`，在对话中使用 `$explain-the-cookbook`。

Claude Code — 请先运行下方的构建和验证命令：

```sh
claude plugin marketplace add ./dist/kitchen/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

切换前备份已安装的软件包，用宿主原生命令仅卸载 Cookbook 插件并移除其 marketplace 注册，然后注册另一种风格。不要同时保留独立副本或旧版 vibe-coding-cookbook。

也可单独安装技能；目标位置不能已有此工作流。示例创建 close-the-kitchen；plain 创建 can-we-finish。

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 40 individual ZIPs + `SHA256SUMS`.

## 构建与验证

构建需要 Git 和 Python 3.10+，无需额外 Python 包。请分别安装并登录 Codex 或 Claude Code。在仓库根目录运行命令。

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## 配方菜单

| Plain | Kitchen |
|---|---|
| Explain the Cookbook | Show Me the Kitchen |
| Find Our Work | Find the Recipe |
| Where Does This Chat Belong? | Find the Kitchen |
| Sort and Triage | Sort the Ingredients |
| Catch Me Up | Back to the Kitchen |
| Where Were We? | What Was I Cooking? |
| How Do I Start? | Prep the Kitchen |
| Finish My Prompt | Finish My Order |
| Which Name Wins? | Name That Dish |
| You Got This | You’re the Chef |
| Am I Making Progress? | Are We Cooking? |
| Why Is It Broken? | Find the Bad Ingredient |
| Can We Simplify? | Trim the Recipe |
| Review My Changes | Taste Before Serving |
| Did I Leak? | Keep the Recipe Secret |
| Will They Sue Me? | Can I Serve This? |
| Am I Ready to Share? | Ready to Serve |
| What Did We Change? | What’s New on the Menu? |
| Can We Finish? | Close the Kitchen |
| Here We Go Again | Why Did It Burn? |

其他模式：`$prep-the-kitchen explain <flow>` 解释现有代码，`$prep-the-kitchen choose <decision>` 比较方案，`$ready-to-serve verify-live <target>` 验证实际交付，`$close-the-kitchen handoff <destination>` 准备交接。Plain 使用相同参数配合 `$how-do-i-start`、`$am-i-ready-to-share` 和 `$can-we-finish`。这些请求本身不授权修改；准备交接不代表已经完成转移。

按情况选择：[使用指南](../choosing-workflow.md)。当前故障使用 `$find-the-bad-ingredient`（Kitchen）或 `$why-is-it-broken`（Plain）。真实操作流程使用 `$youre-the-chef usertest <flow>` 或 `$you-got-this usertest <flow>`。该模式只报告发现，不自动修复，也不是由真人参与的用户研究。

## 更新

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

更新前提交或另行备份本地修改。重新构建只更新本地软件包，不更新已安装的插件缓存。请备份安装包后使用原生卸载和重装命令刷新。详见 Mac 指南。 [Mac setup](../../docs/mac-setup.md).

## 网站

德语和英语页面跟随系统明暗主题。页面语言与命名风格可独立切换；技能说明不会因此翻译。启动本地预览并打开输出的 URL。公开 Beta 网站托管在 GitHub Pages；商店审核单独进行。

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## 限制与状态

软件包、哈希、链接和可移植重建检查已自动化。维护者确认了 0.4.0 的十二个技能在 Desktop 选择器中的显示和结束指南；0.5.0 的新入门指南在新的原生 Codex 调用中单独测试。这些是特定版本的检查，不代表 0.6.0 的完整视觉验收或商店批准。可视化 Cookbook 提供 12 种界面语言及系统/浅色/深色主题；界面语言不会翻译工作流指令。可选的本地 MCP 侧栏是独立软件包。

安全和法律审查配方只提供检查指导，不提供保证。仓库和网站发布与商店提交相互独立。导入的 Git 历史和署名均予保留，包括维护者批准的历史联系页面；四个被替代的 GitHub 仓库已获维护者授权删除。 [0.5.0 acceptance](../../docs/acceptance-0.5.0.md) · [Release review](../../docs/public-release-review.md).

## 贡献与许可证

欢迎提交 issue 或有明确范围的 pull request。只编辑共享技能源，并同步维护八种 README。原创代码及技能采用 MIT；第三方图标保留 MIT/ISC 声明。插图由 AI 生成。

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).

使用现有 Cookbook 标志：Cormorant Garamond 字形轮廓，遵循 SIL OFL。配方插图由 AI 生成，不是截图，也不证明宿主验收。[素材来源与许可](../../THIRD_PARTY_NOTICES.md) · [标志指南](../../assets/brand/GUIDE.md)。

## 支持开发

如果 Cookbook 对你有帮助，欢迎[支持我的开源工作](https://github.com/sponsors/pengusto)。
