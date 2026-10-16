# Cookbook by Pengusto

Seven workflows. One maintained source. Choose **Plain questions** or **Kitchen names** when installing; each installation shows one name per workflow.

| Plain | Kitchen |
|---|---|
| How Do I Start? | Prep the Kitchen |
| Am I Making Progress? | Are We Cooking? |
| Did I Leak? | Keep the Recipe Secret |
| Will They Sue Me? | Can I Serve This? |
| Am I Ready to Share? | Ready to Serve |
| What Did We Change? | What’s New on the Menu? |
| Can We Finish? | Close the Kitchen |

## Use on another Mac and update

The private repository is [pengusto/cookbook](https://github.com/pengusto/cookbook). See [Mac setup and updates](docs/mac-setup.md) for clone, build, variant selection and cache refresh. GitHub access and plugin login are separate; no credentials or personal host settings are stored here.

## Local build

Python 3.10+ and standard library only:

```sh
python3 scripts/cookbook.py build
python3 scripts/cookbook.py check
python3 scripts/cookbook.py check-sources
python3 -m unittest discover -s tests
python3 scripts/launch_check.py
```

`skills/<stable-id>/` is now the only editable workflow source. Names and invocation IDs come from `catalog.json`; generated packages substitute only names and invocations. Do not directly install the source templates. There is no external source registry dependency, separate copy per naming variant, submodule or synchronization step.

## Install one variant

Choose `plain` or `kitchen`. For example, Plain in Codex:

```sh
codex plugin marketplace add ./dist/plain/codex
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Claude Code, using the existing local binary:

```sh
claude plugin marketplace add ./dist/plain/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

For Kitchen, replace `plain` with `kitchen` in the marketplace path. Both variants deliberately use the same marketplace and plugin identity. To switch, preserve the current package, uninstall that plugin natively, remove only its marketplace registration, then register/install the other variant. Do not install alongside the old `vibe-coding-cookbook` bundle or standalone copies of the same workflows. Review any existing installation before changing it; the build never installs or switches anything automatically.

Individual installation remains available:

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

This creates `close-the-kitchen/`; Plain creates `can-we-finish/`. The installer refuses either variant if that workflow already exists in the destination. Four plugin ZIPs (each including its complete local marketplace) and fourteen individual ZIPs are generated in `site/downloads/` with SHA256SUMS. Optional read-only sidebar companions are under `dist/plain/sidebar/` and `dist/kitchen/sidebar/`; neither includes skill copies.

## Website and history

Preview: `python3 scripts/cookbook.py serve --port 8767`, then open the printed local URL. `index.html` shows Plain; `kitchen.html` shows Kitchen. English alternatives are `index-en.html` and `kitchen-en.html`. Language switches preserve naming style; naming switches preserve language. Each page has matching downloads and structured data. Website language does not translate skill instructions. The white/green landing page uses local styles and an AI-generated cookbook illustration. No public URL is assumed; private-preview noindex remains.

All seven previous Git histories are preserved as `history/<stable-id>` branches and as ancestors of main, without squashing or rewriting. The previous source repositories and old generated outputs are retained. They are archives, not maintained inputs. See [consolidation and evidence](docs/consolidation.md), [maintenance](docs/maintenance.md) and [Deutsch](docs/readme/README.de.md).

Review 0.2.0 is prepared locally and synced to a private GitHub repository for use on your own Macs. Packaging tests do not prove full host behavior, security or legal compliance. Historical 0.1.x host and external-validator reports remain historical. Visible desktop acceptance, public destinations, legal pages, scanner coverage and store prerequisites remain open. No public publication, deletion of originals or deployment. Private GitHub sync was explicitly authorized.

MIT; each source retains its LICENSE and provenance. Some preserved historical repositories are private; history preservation is not permission to publish their past contents.
