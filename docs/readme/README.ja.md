# Cookbook by Pengusto

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

13のエージェント用ワークフローを共通のソースで管理します。**わかりやすい質問**または**料理の名前**を選び、ホストごとに一方だけインストールしてください。

**実験的な公開 Beta.** [pengusto/cookbook](https://github.com/pengusto/cookbook)

| Plain | Kitchen |
|---|---|
| How Do I Start? | Prep the Kitchen |
| Am I Making Progress? | Are We Cooking? |
| Where Were We? | What Was I Cooking? |
| Did I Leak? | Keep the Recipe Secret |
| Will They Sue Me? | Can I Serve This? |
| Am I Ready to Share? | Ready to Serve |
| What Did We Change? | What’s New on the Menu? |
| Can We Finish? | Close the Kitchen |
| Here We Go Again | Why Did It Burn? |
| Catch Me Up | Back to the Kitchen |
| Finish My Prompt | Finish My Order |
| Which Name Wins? | Name That Dish |
| Explain the Cookbook | Show Me the Kitchen |

> **0.5.0 · 13 workflows.** Start with `$show-me-the-kitchen` (Kitchen) or `$explain-the-cookbook` (Plain). The visual Cookbook supports 12 languages and system/light/dark themes. Use `--ref plain` for Plain installation. The GitHub release is separate from the Store review. [Publication and installation](../../docs/publication.md).



## ビルドと検証

Git と Python 3.10+ が必要です。追加の Python パッケージは不要です。Codex または Claude Code は別途インストールしてログインしてください。コマンドはリポジトリのルートで実行します。

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## 命名スタイルを1つインストール

plain または kitchen を選びます。両方とも同じプラグイン識別子を使用します。例は Kitchen のインストールです。その後、新しいセッションを開始してください。ビルドは既存のインストールを変更しません。

Codex:

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Claude Code:

```sh
claude plugin marketplace add ./dist/kitchen/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

切り替える前にインストール済みパッケージをバックアップし、ホストの標準操作で Cookbook プラグインだけをアンインストールし、その marketplace 登録を削除してから別のスタイルを登録します。単独のコピーや旧版 vibe-coding-cookbook を併用しないでください。

スキルの個別インストールも可能です。保存先に同じワークフローが存在してはいけません。例では close-the-kitchen、plain では can-we-finish が作成されます。

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 26 individual ZIPs + `SHA256SUMS`.

## 更新

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

更新前に変更をコミットするか別途バックアップしてください。再ビルドはローカルパッケージを更新しますが、インストール済みキャッシュは更新しません。バックアップ後、標準のアンインストールと再インストールで更新します。Mac ガイドも参照してください。 [Mac setup](../../docs/mac-setup.md).

## ウェブサイト

独語・英語のページはシステムのライト／ダーク設定に従います。言語と命名スタイルは独立して切り替えられますが、スキルの説明は翻訳されません。ローカルプレビューを開始し、表示された URL を開いてください。公開 Beta サイトは GitHub Pages で提供されます。ストア審査は別です。

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## 制限と状態

パッケージ、ハッシュ、リンク、ポータブル再ビルドを自動検証します。スキルの読み込みはローカルで確認済みですが、完全なデスクトップ目視受け入れ確認とストア審査は未完了です。安全性・法務の確認用スキルは保証を提供しません。履歴には管理者が公開を承認した過去の連絡先ページが含まれます。元のGit履歴はCookbookに保持しています。以前の4つのGitHubリポジトリは承認を得て削除しました。 [Release review](../../docs/public-release-review.md).

## 貢献とライセンス

issue や範囲を絞った pull request を歓迎します。共通のスキルソースのみを編集し、8言語の README を同期してください。独自コードとスキルは MIT、第三者アイコンは MIT/ISC の表記を保持します。イラストは AI 生成です。

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).
