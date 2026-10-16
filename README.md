# What Did We Change · What’s New on the Menu?

`what-did-we-change` turns real Git changes into clean release notes. Both visible names refer to this one skill; the technical ID stays unchanged. The Cookbook distributes a reviewed snapshot individually and in its Codex/Claude bundles. There is no separately maintained implementation in the Cookbook.

It asks Codex or another compatible AI agent to inspect repository history, changed files, and relevant diffs instead of paraphrasing commit messages.

## Example

```text
Use $what-did-we-change to generate release notes from v1.3.0 to HEAD.
```

```markdown
# v1.4.0

## New

- Added support for renaming downloaded images from the context menu.

## Fixed

- Removed temporary query parameters from generated download names.
```

## Installation

From its parent directory, copy the complete local skill directory into an empty Codex skill destination. First check that the destination does not already exist:

```bash
mkdir -p ~/.agents/skills
test ! -e ~/.agents/skills/what-did-we-change && test ! -L ~/.agents/skills/what-did-we-change && cp -R ./what-did-we-change ~/.agents/skills/what-did-we-change
```

Restart Codex if it is already running. Other agents that support `SKILL.md` can load the repository from their own skills directory.

## Usage

Run Codex from the repository you want to inspect, then ask:

```text
Create release notes.
```

You can also name the range or target version:

```text
Use $what-did-we-change to prepare release notes for v2.0.0 from v1.8.0 to HEAD.
```

## Existing and initial releases

For an existing project, the skill selects a relevant reachable release tag, reviews the range to the target, and groups verified behavior changes.

For a repository without releases or tags, it reads the current code and documentation and describes the first public release. It may flag a few direct release blockers, but it does not create a version, tag, or release.

## Limits

- Local Git is sufficient; GitHub metadata is optional.
- The skill creates notes, not builds, packages, tags, or releases.
- It omits claims that the repository cannot support with evidence.

## License

MIT
