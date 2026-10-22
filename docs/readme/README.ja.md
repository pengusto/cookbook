# Cookbook by Pengusto

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/brand/cookbook-horizontal-dark-1200.png">
  <img src="../../assets/brand/cookbook-horizontal-light-1200.png" width="600" alt="Cookbook by Pengusto">
</picture>

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

**コーディングの会話で、次の一歩に合うレシピを。**

Cookbook は Codex や Claude Code を使う開発者向けに、13 のワークフローを提供します。プロジェクトの計画、進捗確認、休止後の状況把握、共有前のレビュー、引き継ぎの整理に使えます。必要なときにレシピを選び、ホストとモデルが作業を行います。

**わかりやすい質問**か**料理の名前**を選んでください。両方とも同じ管理された指示から生成されます。ホストごとに一方の命名スタイルをインストールします。

**実験的な公開ベータ · 0.5.1.** [レシピを見る](https://pengusto.github.io/cookbook/cookbook.html) · [Plain](https://pengusto.github.io/cookbook/cookbook-plain.html)

## クイックスタート：命名スタイルを選ぶ

先に Codex や Claude Code をインストールしてログインしてください。例では Kitchen を使います。Codex で Plain を使う場合は `--ref plain` を指定します。両方とも同じプラグイン識別子を使うため、一度に一方だけをインストールします。パッケージのビルドはホストのインストールを変更しません。

Codex — ローカルビルドは不要：

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

インストール後、新しい Codex セッションで試してください：

```text
$show-me-the-kitchen Cookbook を説明し、長い休止の後でプロジェクトに戻るためのワークフローを勧めてください。
```

ガイドは説明と推薦を行い、推薦したワークフローを実行しません。Plain ではインストール時に `--ref plain`、会話では `$explain-the-cookbook` を使います。

Claude Code — 先に下記のビルドと検証コマンドを実行してください：

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

## ビルドと検証

Git と Python 3.10+ が必要です。追加の Python パッケージは不要です。Codex または Claude Code は別途インストールしてログインしてください。コマンドはリポジトリのルートで実行します。

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## レシピメニュー

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

パッケージ、ハッシュ、リンク、可搬ビルドの検証は自動化されています。メンテナーは 0.4.0 の十二のスキルの Desktop 選択画面と終了ガイドを確認しました。0.5.0 の新しい導入ガイドは、新規のネイティブ Codex 呼び出しで別途テストされています。これは各バージョンの記録であり、0.5.1 全体の視覚的受け入れ確認やストア承認ではありません。視覚的な Cookbook は 12 の UI 言語とシステム／ライト／ダークテーマに対応します。UI 言語はワークフローの指示を翻訳しません。任意のローカル MCP サイドバーは別パッケージです。

セキュリティや法務のレシピは検証を案内しますが、保証はしません。リポジトリとウェブサイトの公開はストア申請とは別です。インポートした Git 履歴と帰属情報は、承認された過去の連絡先ページも含めて保存されています。置き換えられた四つの GitHub リポジトリはメンテナーの承認で削除されました。 [0.5.0 acceptance](../../docs/acceptance-0.5.0.md) · [Release review](../../docs/public-release-review.md).

## 貢献とライセンス

issue や範囲を絞った pull request を歓迎します。共通のスキルソースのみを編集し、8言語の README を同期してください。独自コードとスキルは MIT、第三者アイコンは MIT/ISC の表記を保持します。イラストは AI 生成です。

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).

既存の Cookbook ロゴを使用：Cormorant Garamond の字形輪郭は SIL OFL に従います。レシピのイラストは AI 生成であり、スクリーンショットやホストでの受け入れ確認を示すものではありません。[素材の出所とライセンス](../../THIRD_PARTY_NOTICES.md) · [ロゴガイド](../../assets/brand/GUIDE.md)。
