# Cookbook by Pengusto

Project: **Cookbook by Pengusto** · GitHub repository: [`pengusto/cookbook`](https://github.com/pengusto/cookbook).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/readme/cookbook-banner-storybook-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/readme/cookbook-banner-storybook-v3.png">
  <img alt="AI illustration: the Cookbook penguin cooking in a cream-and-wine-red kitchen rising from an open cookbook, beside workflow recipe cards." src="assets/readme/cookbook-banner-storybook-v3.png">
</picture>

[![MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](README.md) · [Deutsch](docs/readme/README.de.md) · [简体中文](docs/readme/README.zh-CN.md) · [日本語](docs/readme/README.ja.md) · [Español](docs/readme/README.es.md) · [한국어](docs/readme/README.ko.md) · [Português (Brasil)](docs/readme/README.pt-BR.md) · [Français](docs/readme/README.fr.md)

**A recipe for the next step in your coding chat.**

Cookbook gives developers using Codex or Claude Code 14 focused workflows: plan a project, check progress, recover context after a break, review before sharing, and close with a useful handoff. Pick a recipe when you need it; your host and model carry out the work.

Choose **Plain questions** or **Kitchen names**. Both are built from the same maintained instructions; install one naming style per host.

**Experimental public beta · 0.6.0.** [Browse the recipes](https://pengusto.github.io/cookbook/cookbook.html) · [Plain](https://pengusto.github.io/cookbook/cookbook-plain.html)

## Quickstart: choose one naming style

Install and sign in to Codex and/or Claude Code first. The examples install Kitchen; use `--ref plain` for Plain in Codex. Both naming styles share one plugin identity, so install one at a time. Building packages does not change host installations.

Codex — no local build required:

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

After installation, start a fresh Codex session and try:

```text
$show-me-the-kitchen Explain Cookbook and recommend a workflow for returning to a project after a long break.
```

The guide explains and recommends; it does not execute the recommended workflow. For Plain, use `--ref plain` during installation and `$explain-the-cookbook` in the chat.

Claude Code — first run the build and verification commands below:

```sh
claude plugin marketplace add ./dist/kitchen/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

Before switching styles, back up the installed package, natively uninstall only the Cookbook plugin, remove only its marketplace registration, then register the other style. Avoid unintended duplicate installations. Existing standalone aliases are not automatically removed.

Individual installation is supported; the destination must be empty for this workflow. This creates close-the-kitchen; plain creates can-we-finish.

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 28 individual ZIPs + `SHA256SUMS`.

## Build and verify

Python 3.10+ and Git are required to build; no Python packages are needed. Install and sign in to Codex and/or Claude Code separately. Run these commands from the repository root.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## The recipe menu

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
| You Got This | You’re the Chef |

Use `$youre-the-chef <goal>` (Kitchen) or `$you-got-this <goal>` (Plain) to delegate implementation through a checked result. `gauntlet` adds a finite critique loop; `audit` reports findings without broad implementation. This differs from prompt completion, which only drafts the request.

## Update

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

Commit or separately back up your changes before pulling. A rebuild updates local packages, not an installed plugin cache. Back up the installed package and use native uninstall/reinstall to refresh it. See the detailed Mac setup guide. [Mac setup](docs/mac-setup.md).

## Website

DE/EN landing pages support the system light/dark preference. Website language and naming style switch independently; website translations do not translate skill instructions. Start the local preview and open the printed URL. The website is published on GitHub Pages; Store submission is separate.

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](docs/landing-page.md).

## Limits and status

Package, hash, link and portable rebuild checks are automated. The maintainer confirmed the twelve-skill 0.4.0 Desktop picker and closing guide; 0.5.0 separately tested the new introduction in a fresh native Codex invocation. These are dated checks, not full visual acceptance of 0.6.0 or Store approval. The visual Cookbook offers 12 UI languages and system/light/dark themes; UI language does not translate workflow instructions. The optional local MCP sidebar is a separate package.

Security and legal review recipes guide checks; they provide no guarantees. Repository and website publication are separate from Store submission. Imported Git histories and their attribution remain preserved, including maintainer-approved historical contact pages; the four superseded GitHub repositories were removed with maintainer approval. [0.5.0 acceptance](docs/acceptance-0.5.0.md) · [Release review](docs/public-release-review.md).

## Contributing and licenses

Report issues or send focused pull requests. Edit only the shared skills source and keep all eight READMEs aligned. Original code and skills are MIT; third-party icons retain MIT/ISC notices and artwork is AI-generated.

[Contributing](CONTRIBUTING.md) · [MIT](LICENSE) · [Third-party notices](THIRD_PARTY_NOTICES.md) · [Maintenance](docs/maintenance.md).

Existing Cookbook logo: Cormorant Garamond outlines under SIL OFL. Recipe illustrations are AI-generated; no screenshot or host acceptance is implied. [Asset provenance and licenses](THIRD_PARTY_NOTICES.md) · [Logo guide](assets/brand/GUIDE.md).
