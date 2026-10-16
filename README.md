# Finish This Chat · Close the Kitchen

A closing workflow for Codex and Claude Code. It replaces the previous Kill the TODOs workflow while preserving the `kill-the-todos` ID.

Start with a short closing guide. Finish already authorized work, or leave a truthful handoff when pausing. Guide-only requests change nothing; deferred work stays open. Publication, deletion and archiving require their own authorization.

## Use either visible name

Ask “Finish This Chat” or “Close the Kitchen”. The exact skill ID stays `$kill-the-todos` in Codex. In the Cookbook Claude plugin, use `/vibe-coding-cookbook:kill-the-todos`. The visible names are discovery aliases, not additional slash commands.

## Local installation

Copy this complete directory into an empty `kill-the-todos` directory under your host’s skills directory (Codex: `~/.agents/skills/`; Claude Code: `~/.claude/skills/`). Preserve `SKILL.md`, `agents/` and `LICENSE`; never overwrite an existing installation blindly. The Cookbook also packages this source as an individual ZIP and in its Codex and Claude bundles.

## Validation

See `TESTING.md` for behavioral cases. This repository contains instructions, no hooks, service or runtime dependency. MIT covers this newly authored revision; see `LICENSE`. No release has been published by this preparation.
