![You Got This: a penguin assembles a desk lamp on an island workbench, from loose parts through assembly to a working lamp with a check card.](output/portfolio-handoff/banner-purple-v1.png)

# You Got This

**Give your agent a goal. Get back a change it can explain and verify.**

You Got This is a project-execution skill for Codex: a set of instructions that helps an agent turn intent into a small, complete, checked result. Use it when you know what should improve but want the agent to investigate the repository and handle the implementation details.

[Explore the website](https://pengusto.github.io/you-got-this/) · [Artwork and prompts](output/portfolio-handoff/)

*AI-generated banner illustration. [Prompt and provenance](output/portfolio-handoff/) · [Original process illustration](docs/assets/you-got-this-preview.webp).*

## From “make it better” to something inspectable

```text
$you-got-this Finish the onboarding flow for public demo use. Keep the current visual direction.
```

The skill directs the agent to read the project's instructions, trace the real flow, choose observable checks, implement the highest-value improvements, and hand back what changed, what passed, and what remains unverified. It is for developers and maintainers working in an existing project, from a focused bug fix to a demo polish pass.

**Goal → context → build → verify → handoff.** When scope, privacy, destructive actions or cost require a real decision, the instructions call for human input. The quality loop is finite.

## Install

### Codex

Prerequisites: Git and Codex with local skill support. No package manager, API key or build step is required for this skill. The project you work on still needs its own tools and dependencies.

Clone into an unused destination directory:

```sh
mkdir -p ~/.codex/skills
git clone https://github.com/pengusto/you-got-this.git ~/.codex/skills/you-got-this
```

Open a Codex session in the project you want to improve. Start a new session if the skill is not yet listed, then invoke it with:

```text
$you-got-this <goal>
```

The canonical instructions are in [SKILL.md](SKILL.md); [agents/openai.yaml](agents/openai.yaml) supplies Codex display metadata. Other harnesses need their own way to load those instructions; the installation above is for Codex.

### Update

```sh
git -C ~/.codex/skills/you-got-this pull --ff-only
```

## Modes

| Invocation | Use it for |
| --- | --- |
| `$you-got-this <goal>` | Normal autonomous execution, verification, and handoff |
| `$you-got-this gauntlet <goal>` | A finite build → critique → fix → re-check loop |
| `$you-got-this audit [area]` | Evidence-backed findings without a major implementation |

The mode word only applies when it is the first argument. A goal containing “audit” or “gauntlet” is still treated as a normal goal unless it starts with that mode.

See [examples.md](examples.md) for prompts and expected mode selection.

## What it does

- finds the actual repository and reads its governing instructions;
- traces the affected user-visible or operational flow;
- infers safe details instead of blocking on low-value questions;
- sets a concrete quality bar for the domain;
- implements the smallest complete change using existing patterns;
- runs relevant checks and distinguishes local evidence from unverified runtime or deployment gates;
- preserves product intent and surfaces decisions that genuinely need the user.

It does not create a framework, scoreboard, state machine, or process layer around the work. The repository and its existing tools remain the source of truth.

## Status and boundaries

This repository ships a Markdown skill, prompt examples, Codex metadata and a static website. Its automated checks validate package structure and site integrity; they do not prove that an agent will complete every goal successfully.

Execution depends on the model, harness, tools, permissions and project context. These instructions do not grant additional access or enforce a sandbox. Checks that cannot run, external integrations and deployment acceptance must remain explicit in the handoff. Gauntlet mode calls for a fresh critic when the host supports one; it does not install an agent orchestrator.

## Repository layout

```text
.
├── SKILL.md                 # Canonical skill instructions
├── agents/openai.yaml       # Codex display metadata
├── examples.md              # Prompt examples and expected mode selection
├── docs/                   # Static GitHub Pages website
├── output/portfolio-handoff/ # Public image, original and generation prompt
├── tests/test_skill.py      # Dependency-free structural validation
├── tests/test_site.py       # Site links, images and copy-target checks
├── .github/workflows/       # Validation on every push and pull request
├── CHANGELOG.md
└── LICENSE
```

## Validate locally

```sh
python3 tests/test_skill.py
python3 tests/test_site.py
```

No package installation is required. The static website uses local assets and no framework, analytics, external fonts or browser storage. Pages deploys `docs/` after validation on pushes to `main`. The public handoff assets are intentionally tracked; local `.scratch/` work is ignored.

## Contributing

Keep changes focused on better decisions, safer execution, clearer evidence, and less unnecessary ceremony. If a rule cannot be checked or does not improve outcomes, it probably does not belong in the skill.

Run both validation commands above before opening a pull request and include the behavior or failure mode the change improves. Keep the project banner as the first content in the README, before the heading.

## License

MIT. See [LICENSE](LICENSE).
