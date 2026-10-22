# Public beta 0.5.0 / Öffentliche Beta

This release contains thirteen shared workflows, including **Explain the Cookbook / Show Me the Kitchen**. Kitchen and Plain are two naming variants of the same source; installing a naming style does not install aliases from the other one.

## Install Codex without a build

Install and sign in to the Codex CLI first. For Kitchen:

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Start a fresh local Codex session and use `$show-me-the-kitchen`. For Plain replace `--ref kitchen` with `--ref plain` and use `$explain-the-cookbook`. Install one variant at a time. Existing installations are not silently replaced: preserve the installed package and use native plugin uninstall/reinstall when changing version or style. Existing standalone skills are retained unless their removal is explicitly requested.

The generated `kitchen` and `plain` branches contain native Codex marketplace roots and exact reviewed skill packages. They are generated from main by `scripts/publish_marketplaces.py --push`, with normal non-force pushes and parent history. The script's default is a read-only dry run. Each generated commit records its source SHA. Do not edit these branches manually.

Claude Code and individual skill ZIPs remain available from the website. Extract the Claude plugin ZIP and run its README commands from the extracted root. Building locally remains supported; see the main README.

## Website / Website

[Landing page](https://pengusto.github.io/cookbook/) · [Interactive Kitchen cookbook](https://pengusto.github.io/cookbook/cookbook.html) · [Plain cookbook](https://pengusto.github.io/cookbook/cookbook-plain.html).

The visual cookbook has thirteen individually illustrated recipes, twelve UI languages, a name comparison control and system/light/dark themes. Language changes translate the interface and recipe summaries, not the maintained workflow bodies. Fonts, motion runtime and artwork are embedded; reduced motion is respected. The DE/EN installation landing pages retain their previous layout; a full visual restyle remains deferred.

GitHub Actions verifies all packages and a clean portable rebuild before generating marketplace branches and deploying `site/` through GitHub Pages. A push alone is not evidence of a successful deployment; inspect the workflow and actual live pages. The workflow needs repository Contents write permissions and Pages configured with build type `workflow`.

## Privacy and attribution / Datenschutz und Herkunft

The maintained public text is in `templates/legal.json`, rendered into [Legal notice](https://pengusto.github.io/cookbook/legal-en.html) and [Privacy policy](https://pengusto.github.io/cookbook/privacy-en.html), with German versions. The public maintainer identity was reused from the maintainer's confirmed legal skill. GitHub Pages hosting, support contacts, local preferences, host/model processing and local scanner cache are described separately. No tracking or external font runtime was added.

Generated artwork provenance and third-party licenses remain in `assets/cookbook/SOURCES.json`, `assets/vendor/`, `assets/brand/` and `THIRD_PARTY_NOTICES.md`. Original imported histories and licenses remain preserved.

## Store boundary / Store-Grenze

Repository and website publication do not submit the plugin to the OpenAI Store. The twelve-skill Desktop result remains a user-confirmed 0.4.0 snapshot, not a thirteen-skill visual observation. The new guide is checked separately. The prior store upload ZIP and hash are historical, because 0.5.0 adds a workflow.

Still required before Store submission: verified publisher identity/access in the actual portal, review of the exact 0.5.0 Kitchen upload ZIP and metadata (including the live privacy URL), portal skill scans and Store review. The optional local MCP sidebar is outside the skills-only Store package. Nothing is submitted automatically by the publication workflow.

## Regression lessons / Erkenntnisse

Keep dates and release scopes on acceptance reports. Derive workflow counts from the catalog; never replace the English word “eight” indiscriminately in HTML, because that also corrupts `height`. Link validation covers the exported site, legal contact `mailto:` links and fragment targets. Packaging tests cover the native marketplace root and exact generated payload.
