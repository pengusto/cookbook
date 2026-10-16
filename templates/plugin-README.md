# Vibe Coding Cookbook — local plugin review

[English](README.md) · [Deutsch](README.de.md)

This skills-only review bundle contains Start It Right, Check Progress (Are We Cooking?), Did I Leak?, Will They Sue Me?, Let Them See It, What Did We Change, and Finish This Chat (Close the Kitchen). It adds no hooks, MCP servers, accounts, or background services. Python/Git and optional scanners are needed when running Did I Leak; current primary sources are needed for legal conclusions in product reviews.

The hidden manifest directory identifies the target: `.codex-plugin` for Codex, `.claude-plugin` for Claude Code. This archive contains one plugin folder, not a marketplace or an individual skill. Preserve hidden files when extracting. Version 0.1.4 identifies the private review build, not a published release.

## Local use

Claude Code: from the extracted Claude plugin folder, run `claude plugin validate .`, then start an isolated review session with `claude --plugin-dir .`. Invoke `/vibe-coding-cookbook:let-them-see-it` with your task. Do not enable the bundle in the same session as separate copies of these skills when comparing behavior.

Codex: place the extracted Codex folder at `plugins/vibe-coding-cookbook` in a chosen review project. Add `.agents/plugins/marketplace.json` at that project's root:

```json
{
  "name": "cookbook-local",
  "plugins": [{
    "name": "vibe-coding-cookbook",
    "source": {"source": "local", "path": "./plugins/vibe-coding-cookbook"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
    "category": "Developer Tools"
  }]
}
```

Reload the local desktop host and inspect/install the available plugin through its plugin interface. Merely extracting the ZIP does not install it. Discovery and skill invocation need verification in your host; local test registration is temporary and removed after verification. The Cookbook source build also generates this complete review-project layout under `dist/codex/`.

## Contents and limits

`SOURCES.json` records the bundled source revisions and exact per-file SHA-256 hashes. Each `skills/<id>/LICENSE` preserves its original notice; the root MIT license covers the Cookbook packaging and text. Are We Cooking? is included under MIT with the user’s explicit license selection.

Individual skills remain separately installable through the Cookbook's individual ZIPs. To use only one skill from this archive, copy its complete `skills/<id>` directory into an empty skill destination appropriate for your host, preserving its references, scripts and license. Never replace an existing skill or install this plugin root as one skill.

Skill files are reviewed source snapshots. Five existing skills have prior authenticated Claude behavior coverage; the closing workflow has separate Codex and Claude behavior coverage. Package equality does not prove identical host behavior. See the Cookbook host-test report for current coverage and limits. Nothing is published.

Format references: [Codex plugins](https://developers.openai.com/plugins/build/plugins), [Claude Code plugins](https://code.claude.com/docs/en/plugins/create). Package formats checked on 2026-10-15.
