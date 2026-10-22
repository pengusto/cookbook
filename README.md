# Cookbook by Pengusto

[![MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](README.md) · [Deutsch](docs/readme/README.de.md) · [简体中文](docs/readme/README.zh-CN.md) · [日本語](docs/readme/README.ja.md) · [Español](docs/readme/README.es.md) · [한국어](docs/readme/README.ko.md) · [Português (Brasil)](docs/readme/README.pt-BR.md) · [Français](docs/readme/README.fr.md)

Thirteen agent workflows from one maintained source. Choose **Plain questions** or **Kitchen names**; install one naming style per host.

**Experimental public Beta.** [Website](https://pengusto.github.io/cookbook/) · [Interactive Cookbook](https://pengusto.github.io/cookbook/cookbook.html). [pengusto/cookbook](https://github.com/pengusto/cookbook)

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

> **0.5.1 · 13 workflows.** Start with `$show-me-the-kitchen` (Kitchen) or `$explain-the-cookbook` (Plain). The visual Cookbook supports 12 languages and system/light/dark themes. Use `--ref plain` for Plain installation. The GitHub release is separate from the Store review. [Publication and installation](docs/publication.md).



## Build and verify

Python 3.10+ and Git are required to build; no Python packages are needed. Install and sign in to Codex and/or Claude Code separately. Run these commands from the repository root.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## Install one naming style

Choose plain or kitchen. Both use the same plugin identity. The examples install Kitchen. Start a new host session afterward. The build itself never changes host installations.

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

Before switching styles, back up the installed package, natively uninstall only the Cookbook plugin, remove only its marketplace registration, then register the other style. Avoid unintended duplicate installations. Existing standalone aliases are not automatically removed.

Individual installation is supported; the destination must be empty for this workflow. This creates close-the-kitchen; plain creates can-we-finish.

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 26 individual ZIPs + `SHA256SUMS`.

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

Package, hash, link and portable rebuild checks are automated. The maintainer confirmed all twelve 0.4.0 skills in the Desktop picker and the close guide. Version 0.5.0 adds the introduction; automated package and invocation checks do not replace Store review. Security and legal review skills guide checks; they are not guarantees. The imported histories contain maintainer-approved historical contact pages. The original Git histories are preserved in Cookbook; the four superseded GitHub repositories were removed with maintainer approval. [Release review](docs/public-release-review.md).

## Contributing and licenses

Report issues or send focused pull requests. Edit only the shared skills source and keep all eight READMEs aligned. Original code and skills are MIT; third-party icons retain MIT/ISC notices and artwork is AI-generated.

[Contributing](CONTRIBUTING.md) · [MIT](LICENSE) · [Third-party notices](THIRD_PARTY_NOTICES.md) · [Maintenance](docs/maintenance.md).
