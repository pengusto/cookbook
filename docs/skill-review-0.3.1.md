# Local skill review · 0.3.1

2026-10-19. All eight shared workflows revised and locally verified. The maintainer subsequently authorized committing and pushing this source update to GitHub. Website deployment and store submission remain outside the approved scope.

| Workflow | Change and behavioral scenario |
| --- | --- |
| Prep the Kitchen | No mandatory ticket/module tree or permanent next-action loop. A small three-link local brainstorm does not require a hosting decision. |
| Are We Cooking? | Diagnose the current approach without reconstructing every turn or automatically demanding a full suite. CSV repair evidence stays separate from an unrequested dashboard redesign. |
| What Was I Cooking? | Short recap by default. Missing early history stays provisional; an unaccepted analytics suggestion is not open work. |
| Keep the Recipe Secret | Unreadable files count as incomplete heuristic coverage and prevent an unqualified GO. A count is not a path inventory; no safety guarantee or publication permission is inferred. |
| Can I Serve This? | Targeted versus launch scope. A reported Tab skip needs reproduction and does not by itself prove that submission is impossible or establish legal applicability. |
| Ready to Serve | Audience-driven documentation rather than mandatory eight-language or badge proposals; Pages details load only when needed. Unknown files are not confirmed missing artifacts. |
| What’s New on the Menu? | Ambiguous release lines require clarification, uncommitted work is distinct, and restored behavior is a fix. |
| Close the Kitchen | Reuse applicable observed checks, avoid new tasks for a completed slice, and leave a short evidence-based closure. |

## Verification

- `python3 scripts/launch_check.py`: 25 tests pass locally and in the portable rebuild; artifact hashes match. Coverage includes source hashes, exact package contents, two naming variants, website links, and JSON-LD matching the eight visible cards in each of four DE/EN views.
- New scanner tests exercise unreadable input with mocked completed external scanners: clean GO becomes GO WITH REVIEW, then recovers after readability returns. Capped text and binary input remain distinct. This is not a fresh real-repository secret audit.
- The official skill-creator validator accepts all 16 rendered skills. PyYAML was installed only in an ignored temporary directory for validation and then removed; no global dependency was added.
- Claude's native manifest validator passes. Its advisory suggests a newer one-step installation style; the existing local-marketplace installation succeeded and was retained.
- Eight synthetic, tool-disabled Claude scenarios were run and responses reviewed. Five were repeated after targeted corrections. The initial bare-mode attempt could not load authentication; the authenticated attempts completed. These are bounded behavior checks, not guarantees across models. Some responses are still more verbose than ideal.
- Native fresh Codex and Claude sessions discover all eight Kitchen IDs and load Close the Kitchen. Codex's event record confirms the installed skill file was read successfully. An initial Codex attempt with isolated command-line configuration failed; the repeat using the actual installed configuration passed. Native execution of each of the other seven skills was not separately repeated in both hosts.
- Browser checks cover the revised German Kitchen cards, expanded Close the Kitchen invocation/download, and English Plain view. JSON-LD contains the same visible names/descriptions; no invented URLs were added. External Schema.org/Google validator submissions were not repeated in this round.

## Local host state

Both hosts have `cookbook-by-pengusto@cookbook-by-pengusto-local` version 0.3.1, Kitchen only. Both installed skill trees match their built package files byte for byte. The previous `vibe-coding-cookbook@cookbook-local` registrations and marketplace entries were removed. Cookbook standalone aliases were checked in the global Codex/Agents/Claude and repository skill roots: none remain active.

The duplicate private `what-was-i-cooking` discovery symlink was moved outside discovery; its original source target is untouched. The optional Codex reading sidebar was refreshed to the same Kitchen catalog. Other plugins were preserved.

Restart Codex/Claude or open a fresh session to refresh desktop discovery. This existing chat can retain the old skill list until reloaded. Visible desktop picker acceptance remains a human check; CLI loading is verified.

Private rollback material is retained under `.scratch/kitchen-migration-0.3.1/` (approximately 696 KiB): prior host configuration, previous plugin copies, and the disabled standalone symlink. It remains ignored and outside skill discovery until visible desktop acceptance and a cleanup decision. Model outputs and native-load evidence remain under `.scratch/skill-review/`; neither directory is packaged or published.
