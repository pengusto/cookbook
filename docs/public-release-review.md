> **0.5.0 publication:** thirteen workflows; current install, website and Store boundaries: [publication.md](publication.md). Earlier acceptance results below are version-specific historical evidence.

> **Aktueller lokaler Stand 0.4.0 (2026-10-22):** zwölf Kitchen-Skills installiert und in frischen Codex-Sitzungen erkannt; vier neue Aufrufe verhaltensgeprüft. Sidebar 0.4.1 aktualisiert, vorherigen deaktivierten Zustand erhalten. [Aktueller Installations- und Abnahmebericht](skill-installation-0.4.0.md). Frühere Nachweise unten bleiben historisch; keine Veröffentlichung.

# Public Beta release review

Historical source-Beta review. For the current eight-workflow package and OpenAI store preparation, see [0.3.1 verification](skill-review-0.3.1.md) and [Store preparation](../store/README.md). The seven-workflow counts below describe the reviewed 2026-10-17 scope.

Reviewed 2026-10-17 with Let Them See It / Ready to Serve. Audience: Codex and Claude Code users who want seven focused workflows from one shared source and one naming style per host. Status: experimental Beta, not a store-approved product.

## Scope and decisions

The maintainer explicitly approved a public `pengusto/cookbook` Beta, all eight README languages, preservation of historical contact-page data, and archiving the old four GitHub skill repositories. No repository deletion, Git history rewrite, website deployment or store submission is included.

## Evaluation

| Priority | Evidence | Change / acceptance |
|---|---|---|
| Necessary | README, docs/mac-setup.md previously described a private checkout | Public clone/build instructions, honest Beta limits, fresh-clone launch check |
| Necessary | Imported history includes old legal/contact pages | Inspect all reachable blobs and retain maintainer-approved contact information; no unresolved credential finding |
| Necessary | assets/site.css and website templates were light-only | System dark scheme, light logo, dark hero, contrast and responsive browser checks |
| Recommended | No current root CI workflow or topics | Existing launch check in GitHub Actions, truthful static CI/license/runtime/Beta badge links, relevant topics |
| Recommended | Website icons have separate licenses | THIRD_PARTY_NOTICES.md and bundled MIT/ISC attribution |
| Optional, approved | README localization | EN at root; DE, zh-CN, ja, es, ko, pt-BR, fr under docs/readme; reciprocal links and identical commands; machine translation disclosed |

Already working: seven canonical MIT skill sources, two generated naming styles, four complete marketplace ZIPs, fourteen individual ZIPs, deterministic builds, source hashes and retained seven histories. No new runtime framework or package manager is necessary.

## Historical and content inspection

Gitleaks scanned 39 reachable commits (~748 KB) with `--all --redact` and reported no leaks before these changes. An additional inventory read 81 tracked text files and 287 UTF-8 historical blobs across 475 reachable objects, including deleted files and all imported refs. Candidate checks covered user paths, email addresses, local/private-network URLs and private/security-note language. Personal contact details in historical did-i-leak and let-them-see-it legal pages were found and explicitly approved for public retention. Scanner regex patterns, synthetic test addresses, localhost preview links and historical review notes are expected content. No private raw session transcripts or credentials are included in the intended export.

Automated scanners and this review are not proof that all sensitive data or legal issues have been found. Original license files and attribution remain. Historical contact approval is not a claim that old legal notices apply to a future hosted Cookbook website.

## GitHub surfaces

- Description/topics: useful for discovery; point to the real repository only.
- README badges: MIT, Python 3.10+, experimental Beta and a static CI link. A CI link is not a claim that its current run passed.
- CONTRIBUTING.md: useful, focused on one source and synchronized translations; no response-time promise or invented security mailbox.
- Sponsors/funding: unnecessary without an approved funding destination.
- Discussions: unnecessary until there is demand and moderation capacity.
- CITATION.cff: unnecessary for this workflow collection.
- Tagged Releases / binary attachments: deferred; public source Beta and local reproducible packages suffice for this scope.
- Social preview: potentially useful later; no separate upload in this scope.
- Insights traffic: useful to inspect after launch; no traffic/star promises.

## Verification boundaries

The local launch check verifies packages, source allowlists/hashes, links, tests and a portable rebuild. A fresh clone is checked before public visibility. This is distinct from a complete agent behavior or visible desktop workflow test. Historical native load tests remain historical. DE/EN website content and seven unchanged skill IDs remain the runtime source of truth; translated READMEs do not translate the skills themselves.

Store approvals, complete desktop acceptance and production website/legal/hosting checks remain open. A separate discovery/launch review may compare relevant skill collections and suggest a few channels; it is not part of this release and no external posts are authorized.

Assessment: **ready with stated limitations** for public-source Beta after the recorded checks pass. Publication, pushed SHA, CI and archived-state evidence must be verified from GitHub separately; this document alone does not assert their completion.
