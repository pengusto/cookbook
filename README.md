# Will They Sue Me?

[![Status: experimental](https://img.shields.io/badge/status-experimental-f4ce54)](#status) [![License: MIT](https://img.shields.io/badge/license-MIT-46644c)](LICENSE) · [CI workflow](.github/workflows/check.yml)

**A pre-launch recipe for finding the gap between your app's behavior, its promises, and its obligations.**

[English](README.md) · [Deutsch](docs/readme/README.de.md)

An agent skill for people building apps and websites with AI. It checks relevant privacy, consumer-rights, accessibility and asset-licensing flows, finds evidence-backed gaps, and prepares scoped fixes. The name is a joke. The review is not a legal certificate or a prediction about lawsuits.

## Use it

Install into a skill-aware agent such as Codex. Prerequisites: Git, an agent that reads `SKILL.md`, and access to the product you want reviewed. Current legal research needs browsing; missing access is reported, not guessed.

```sh
git clone https://github.com/pengusto/will-they-sue-me.git
cd will-they-sue-me
python3 scripts/project.py build
mkdir -p ~/.codex/skills
cp -R dist/skill ~/.codex/skills/will-they-sue-me
```

The clone requires repository access while this project is private. Python 3.11+ is required for the build. If the destination already exists, inspect it first instead of overwriting it. Alternatively, download and unpack the built ZIP from the landing page after publication. Reload your agent's skill discovery if needed.

```text
Use $will-they-sue-me to review this app before launch.
Target market: Germany/EU. It sells subscriptions to consumers.
Show applicable checks, evidence, gaps, and proposed acceptance checks.
```

Ask for implementation explicitly when you want fixes. A review request does not authorize arbitrary changes or production actions. Another compatible agent can load `SKILL.md` directly; compatibility beyond Codex has not been separately tested.

## The recipe

1. **Ingredients:** operator and markets, business model, audience, code/configuration, and accessible product flows.
2. **Inspect:** compare actual data collection, consent, checkout, claims, accessibility and asset provenance with applicable obligations.
3. **Taste:** produce findings with evidence, current primary sources, fixes and observable acceptance checks.
4. **Serve:** verify authorized fixes and report remaining unknowns.

Output distinguishes confirmed findings, missing evidence, justified non-applicability, and checks with stated coverage. The review map covers twenty areas without demanding twenty new features. It does not automatically add banners, terms, consent checkboxes or age gates.

## Example finding

> **Launch blocker — analytics before consent:** the app loads a non-essential analytics SDK before the user makes a choice. Evidence: script initialization and observed pre-choice network traffic. Fix: gate initialization where applicable, then verify fresh sessions before choice, after rejection, after acceptance and after withdrawal. Legal basis and applicability require current jurisdiction-specific research.

This is an illustrative finding, not a claim about this repository or your app.

## Develop and preview

Python 3.11+; no runtime packages, frontend framework or JavaScript package manager required.

```sh
python3 scripts/project.py check
python3 scripts/project.py build
python3 -m http.server 4173 --directory dist/preview
```

Open `http://localhost:4173/will-they-sue-me/`. This previews the real project-site base path, generated skill download and documentation links. The package contains only skill instructions, references, UI metadata and MIT license. Source: root `SKILL.md`, `agents/`, `references/`; site: `site/`; generated output: ignored `dist/`.

## Publication

The repository is intended to stay private during maintainer review. GitHub Pages is prepared but not enabled or deployed. The Pages workflow runs only on manual dispatch with an explicit publication confirmation; pushing does not publish the site. It builds the static artifact itself and deploys only the site files. Configure Pages for GitHub Actions and confirm website visibility before dispatching it.

A private repository does not guarantee a private Pages website; see [GitHub's visibility documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site). The expected public project URL after an approved deployment is `https://pengusto.github.io/will-they-sue-me/`; it is not a live demo yet.

## Status

Experimental first version. Structural/package checks and documented behavioral scenarios are different from independent agent evaluations or reviews of a live product. See [the review scenarios](docs/behavior-checks.md) and [maintainer handoff](docs/review.md). No complete legal or accessibility compliance claim is made.

For changes, open an issue with a reproducible scenario and expected behavior, or a focused pull request. Do not put personal data or credentials in issues. English and German documentation are maintained together; the German text is AI-assisted and has not had an independent fluent review.

## License

[MIT](LICENSE) for this project's original code, documentation and skill instructions. Linked legislation, external documentation and third-party products retain their own terms. MIT does not grant rights to third-party assets or provide legal clearance for an audited app.
