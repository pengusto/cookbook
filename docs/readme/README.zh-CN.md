# Cookbook by Pengusto

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

七个智能体工作流，维护于同一份源代码。安装时选择**直白问题**或**厨房名称**，每个宿主只安装一种命名风格。

**实验性公开 Beta.** [pengusto/cookbook](https://github.com/pengusto/cookbook)

| Plain | Kitchen |
|---|---|
| How Do I Start? | Prep the Kitchen |
| Am I Making Progress? | Are We Cooking? |
| Did I Leak? | Keep the Recipe Secret |
| Will They Sue Me? | Can I Serve This? |
| Am I Ready to Share? | Ready to Serve |
| What Did We Change? | What’s New on the Menu? |
| Can We Finish? | Close the Kitchen |

## 构建与验证

构建需要 Git 和 Python 3.10+，无需额外 Python 包。请分别安装并登录 Codex 或 Claude Code。在仓库根目录运行命令。

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## 安装一种命名风格

选择 plain 或 kitchen。两者使用相同的插件标识。示例安装 Kitchen，随后请开始新的宿主会话。构建不会修改已有安装。

Codex:

```sh
codex plugin marketplace add ./dist/kitchen/codex
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Claude Code:

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

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 14 individual ZIPs + `SHA256SUMS`.

## 更新

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

更新前提交或另行备份本地修改。重新构建只更新本地软件包，不更新已安装的插件缓存。请备份安装包后使用原生卸载和重装命令刷新。详见 Mac 指南。 [Mac setup](../../docs/mac-setup.md).

## 网站

德语和英语页面跟随系统明暗主题。页面语言与命名风格可独立切换；技能说明不会因此翻译。启动本地预览并打开输出的 URL。本 Beta 不包含已部署的公开网站或商店上架。

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## 限制与状态

自动检查软件包、哈希、链接和可移植重建。技能加载已在本地测试；完整桌面可视验收及商店审核仍待完成。安全和法律审查技能提供指导，不作保证。保留的历史包含维护者明确允许公开的旧联系页面。原仓库作为存档保留。 [Release review](../../docs/public-release-review.md).

## 贡献与许可证

欢迎提交 issue 或有明确范围的 pull request。只编辑共享技能源，并同步维护八种 README。原创代码及技能采用 MIT；第三方图标保留 MIT/ISC 声明。插图由 AI 生成。

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).
