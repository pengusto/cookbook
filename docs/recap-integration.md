# Conversation recap integration · 0.3.0

The eighth shared source is `what-was-i-cooking`, an existing private skill written by Pengusto and included under MIT with maintainer approval. Its workflow text is retained; the heading and interface metadata use the same naming templates as the other sources. The original private source is untouched. Original file hashes are recorded in `source-history.json`; no Git history is invented for this previously unversioned source.

| Variant | Visible title | Install ID / Codex invocation |
| --- | --- | --- |
| Plain | Where Were We? | `$where-were-we` |
| Kitchen | What Was I Cooking? | `$what-was-i-cooking` |

It reconstructs the original goal, later decisions, current work and remaining tasks from available chat evidence. It reports gaps and side quests without changing files or automatically continuing unfinished work. This differs from the progress diagnostic and release-notes skills.

Integration covers both host bundles, individual downloads, optional sidebar, four DE/EN website views and their matching structured data, store metadata and all eight README languages. Install one naming variant, not both.

## Local verification

- `python3 scripts/launch_check.py`: 23 tests pass locally and in a portable rebuild; artifact hashes match. Source hashes, licenses, links and package contents pass.
- A packaging regression contract ensures every reviewed source is selected in both hosts and both naming variants, with provenance and per-skill licenses.
- Local Kitchen website: eighth card expands and exposes the correct invocation, source link and individual download.
- The standalone skill-creator validator could not run because PyYAML is unavailable. No dependency was installed globally.
- Native Codex/Claude loading and behavioral acceptance of this new skill remain open. Previous host-test records do not prove acceptance of version 0.3.0.

The maintainer authorized publishing this source update to GitHub. No active host installation was replaced. Website deployment and store submission are outside this update.
