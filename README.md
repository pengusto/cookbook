# Vibe Coding Cookbook

[English](README.md) · [Deutsch](docs/readme/README.de.md)

**Private review edition · Python 3.10+ · MIT (Cookbook)**

A curated collection of Pengusto's own agent skills. Choose by the moment you need help, read the recipe and its limits, then install only the relevant skill. Seven recipes, seven reviewed installable snapshots. The playful names stay; the instructions stay practical.

## Local review

From this repository directory:

```sh
python3 scripts/cookbook.py build
python3 scripts/cookbook.py check
python3 -m unittest discover -s tests
python3 scripts/cookbook.py serve
```

Open [the loopback preview](http://127.0.0.1:8766/site/) while the server runs. You can also open `site/index.html` directly after building. There is no application framework, package installation, account, or deployment requirement.

## Choose a recipe

| Name | Cooking title | ID |
|---|---|---|
| Start It Right | Prep the Kitchen | `start-it-right` |
| Check Progress | Are We Cooking? | `are-we-cooking` |
| Did I Leak? | Keep the Recipe Secret | `did-i-leak` |
| Will They Sue Me? | Can I Serve This? | `will-they-sue-me` |
| Let Them See It | Ready to Serve | `let-them-see-it` |
| What Did We Change | What’s New on the Menu? | `what-did-we-change` |
| Finish This Chat | Close the Kitchen | `kill-the-todos` |

The [inventory and journey](docs/inventory.md) explain the selection and exclusions. Each recipe covers when to use it, ingredients, preparation, verification, serving and limits. Recipe prose is German in this edition; original skill instructions are English. Both README versions cover the same installation and maintenance flow.

## Install one snapshot

First test in an empty disposable destination:

```sh
python3 scripts/cookbook.py install let-them-see-it --dest .scratch/review-skills
```

For a deliberate Codex installation, use `--dest ~/.codex/skills`. This is a proposed user action, not an installation performed during preparation. Existing directories and symlinks are refused; provider-managed installations are preserved. Restart/reload your host if needed and verify that it recognizes the skill. Targeted host tests and their limits are recorded in docs/host-tests.md.

Alternatively extract the selected `site/downloads/<id>.zip` into an empty skill destination. Each ZIP contains one top-level skill folder with `SKILL.md`, its LICENSE, and the explicitly selected runtime files. Compare its SHA-256 with `site/downloads/SHA256SUMS`. Never install the repository root as one skill. Packaging is deterministic and requires no network; Did I Leak uses Git/Python and reports optional scanner availability during use.

## Install the bundle locally

The same build creates Codex and Claude Code plugin ZIPs in `site/downloads/`, plus local review layouts and marketplaces in `dist/codex/` and `dist/claude/`. `bundle.json` explicitly selects the seven reviewed skills; individual downloads remain available. The two plugin packages preserve the same skill bytes and original license notices and include `SOURCES.json` for provenance.

See [local plugin setup and website integration](docs/plugins.md). Review 0.1.4 contains all seven skills, listing metadata and icons. Both hosts have native installation and seven-skill loading checks; packaging tests and a portable rebuild are checked locally. The Codex manifest declares its local execution requirement. Visible desktop acceptance remains separate. The closing skill has targeted Codex and Claude behavior coverage, including both visible names in Claude. See [host-tests.md](docs/host-tests.md) for actual coverage, prior tests of the other skills and remaining scanner limits. Nothing was published.

Individual skill websites may later link to their own recipe, single download, and the shared bundles. Those websites and existing repositories have not been modified.

## Sources and updates

Original projects remain the only maintained skill sources. `catalog.json` records the curated recipe, source revision where available, and SHA-256 for every copied file. `skills/` contains read-only-intended review snapshots. ZIPs and the site are generated, ignored output. No source scripts execute during build.

The existing skill-library remains the broad local catalog; this repository adds a reviewed distribution selection rather than another global registry. Ignored `sources.local.json` maps selection IDs to local originals. It is optional for portable builds and required only for `python3 scripts/cookbook.py check-sources`.

Follow [the update process](docs/maintenance.md): review changes at the original, inspect the exact runtime allowlist, copy approved files, update hashes/revision and rebuild. There is no automatic upstream sync or silent installation replacement. A Git revision is context; file hashes establish exact snapshot bytes, including an uncommitted source or a source without Git.

## Rights and readiness

[MIT](LICENSE) covers new Cookbook text and tooling, as selected by the owner. Each packaged skill retains its own original MIT notice. Are We Cooking? has no source LICENSE and is not copied or packaged. Personal integrations, addresses, account settings, landing-page assets and unrelated source history are excluded.

**Ready for private review with stated limitations.** Local checks do not establish legal clearance, complete security, cross-host compatibility or tested agent behavior. See [handoff](docs/handoff.md), [evaluation](docs/evaluation.md) and [behavior scenarios](docs/behavior-review.md). No Cookbook remote, push, release, deployment or public visibility change is part of this preparation.

## Final local launch audit

Run `python3 scripts/launch_check.py` for packaging tests, source checks where available, and a portable rebuild. `dist/website.zip` is a self-contained static website; `dist/launch-report.json` records artifact hashes and outstanding gates. See [launch readiness](docs/launch-readiness.md). Nothing is uploaded by the audit.

All seven Cookbook entries have two visible names and their own local source repositories; IDs remain stable. See [names and source repositories](docs/skill-naming.md). The closing skill is included individually and in both bundles as `$kill-the-todos`.
