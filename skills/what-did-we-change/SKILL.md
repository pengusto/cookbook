---
name: what-did-we-change
description: Create concise, user-facing release notes from verified repository changes. Use when asked what changed since a release, to prepare release notes between Git refs or for a named version, or to describe an initial release in a repository with no prior release. Also known as What’s New on the Menu?.
---

# What Did We Change

Produce release notes from repository evidence. Treat commit messages, branch names, filenames, and TODOs as leads, not proof. Never change files, create tags, or publish releases unless the user separately asks.

## 1. Establish context

1. Find the Git root and read applicable `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `README.md`, `CHANGELOG.md`, release configuration, `.github/`, and relevant package metadata.
2. Follow the project's existing release-note categories, voice, audience, and version format when present.
3. Resolve the requested target, defaulting to `HEAD`, and verify that each supplied ref exists.

Finish with a known target, applicable project conventions, and any user-supplied base or version.

## 2. Select the comparison

Use an explicit base when supplied. Otherwise inspect releases and tags without assuming version sort alone identifies the right one:

```bash
git tag --merged <to> --sort=-version:refname
git describe --tags --abbrev=0 <to>
git log --decorate --oneline -n 30 <to>
```

Choose the latest release tag that belongs to the target's history and project release convention. If the target commit already has that tag, compare against the preceding relevant release tag. Use GitHub release or pull-request metadata only when `gh` exists and is authenticated; local Git must remain sufficient.

If no relevant release or tag exists, take the initial-release path. Do not reconstruct the repository's entire development history.

Finish with either a justified `<from>..<to>` range or a confirmed initial release.

## 3. Inspect evidence

For an existing release, start broad and narrow down:

```bash
git log <from>..<to> --oneline --decorate
git diff <from>..<to> --stat
git diff --name-status <from>..<to>
git diff <from>..<to> -- <relevant paths>
```

Inspect enough implementation, documentation, migrations, manifests, and tests to establish observable behavior. Group commits that implement one outcome. Separate unrelated outcomes even when one commit contains both.

For an initial release, inspect the repository tree, README, package metadata, entry points, public interfaces, and central implementation. Describe the installable or usable product. Leave repository housekeeping out of the notes unless it creates a release-readiness blocker.

Finish only when every included claim has code or documentation evidence and the important changed areas are accounted for.

## 4. Select release-worthy changes

Include behavior that users or developers can observe: new capabilities, meaningful improvements, fixes, breaking changes, security changes, compatibility changes, and material developer-workflow changes.

Omit formatting, cleanup, internal refactors with no visible effect, tests, routine CI work, lockfiles, trivial dependency bumps, comments, and type-only fixes. Include one only when evidence shows an effect on behavior, security, performance, compatibility, or developer workflow.

Resolve uncertainty by inspecting the relevant diff and callers. If evidence remains weak, use conservative wording or omit the claim. Never present intent as shipped behavior.

For an initial release, add a short `Release readiness` section only for obvious blockers such as a missing README, failing documented build, exposed secret, missing `.gitignore`, absent version, or undocumented core installation or usage. Report checks actually run and do not turn this into a general audit.

## 5. Write the notes

Use the requested version. Otherwise prefer the target tag or existing project version; for an unversioned initial release, label `v1.0.0` as a suggestion rather than changing the project.

Default to compact Markdown:

```markdown
# <version or release title>

## New

- <concrete user-facing outcome>

## Improved

- <concrete improvement>

## Fixed

- <fixed behavior>

## Breaking Changes

- <impact and required action>
```

Omit empty sections. For very small releases, use an ungrouped list. Write concise, factual bullet points in past tense for the repository's audience. Mention technical details only when they clarify impact. Distinguish verified facts from suggestions and unverified checks.

Return the notes in the response unless the user asks to write them to a file.
