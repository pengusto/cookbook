> **Current portal status 0.7.0 (2026-10-27):** draft upload confirmed by the maintainer's portal capture. Not published; review needs attention. Blocking findings: terms URL not yet published (bilingual pages and manifest URL are prepared locally) and “We are not accepting more skills-only submissions at this time.” The 18 skill checks were still pending. Local validation passes, but does not establish Store eligibility. See the [current release checklist](../docs/release-checklist.md). Earlier results below are historical.

> **Abnahme 0.4.0 abgeschlossen (2026-10-22):** zwölf Skills nativ synthetisch geprüft; Nutzer bestätigt alle zwölf im Desktop-Picker und funktionierenden Abschluss-Guide. Exaktes Upload-ZIP erneut gescannt. Store-Zugang scheitert aktuell an der Identitätsprüfung; veröffentlichte vollständige Datenschutzerklärung fehlt. [Finaler Bericht](../docs/final-acceptance-0.4.0.md). Nichts hochgeladen oder veröffentlicht.

# Store preparation / Store-Vorbereitung

Reviewed 2026-10-22 for the OpenAI/Codex Plugins Directory. Local preparation only: this review does not establish portal access, identity verification, upload, submission, approval or publication. Claude directory submission is a separate process.

## Upload package

Run `python3 scripts/launch_check.py` from the repository root. It builds and checks both naming variants and compares a portable rebuild, including the upload ZIPs:

- `dist/store/kitchen/cookbook-by-pengusto.zip`
- `dist/store/plain/cookbook-by-pengusto.zip`

The maintainer selected **Kitchen** for the store identity on 2026-10-22; `bundle.json` records `store_variant: kitchen`. Plain remains a local alternative and a reproducibility test output. Each ZIP contains `.codex-plugin/plugin.json`, `skills/`, icons, English/German usage instructions, licenses and source provenance directly at its root. It contains no marketplace wrapper, sidebar, MCP configuration, hooks or private evidence. The existing `site/downloads/` ZIPs remain self-contained local marketplaces; use the dedicated store ZIP for the portal. SHA-256 values are recorded in `dist/launch-report.json`.

The package retains `requires_local_executor: true`: repository checks call local tools. Do not remove this declaration just to pass portal validation. The optional sidebar is a separate local MCP product; it is not part of this submission.

## Remaining acceptance

| Item | Evidence needed before release |
|---|---|
| Naming style | **Decided: Kitchen**, approved by the maintainer on 2026-10-22. |
| Desktop acceptance | Historical 0.3.1: native reinstall matched 42 files, eight bounded scenarios passed, and the maintainer confirmed the eight visible skills. Current 0.4.0 adds four workflows; see the [local installation evidence](../docs/skill-installation-0.4.0.md). A native visual review of the exact new package remains open. See [current acceptance](../docs/store-acceptance-2026-10-22.md) for scope and limits. |
| Privacy | A published plugin privacy policy is required by the general guidelines, even though skills-only metadata validation does not require all four MCP URLs. Finalize the [local draft](privacy-policy.draft.md), confirm publisher/contact and hosting details, then publish only with authorization. |
| Publisher | Confirm organization/project submission access, verified individual or business identity, displayed publisher and category in the actual portal. A local `Pengusto` field does not verify identity. |
| Public contents | Review the exact upload ZIP and any new source changes for unintended public content. Optional extra scanner coverage is not a blanket prerequisite; unresolved sensitive findings still prevent release. |
| Portal checks | Upload only after authorization, resolve metadata/skill findings, complete the applicable review and inspect the approved version before publishing. |

For skills-only submissions, the current OpenAI metadata rules do not require all four MCP listing URLs, MCP review test cases or a demo recording. Do not invent support, privacy or terms destinations. The verified developer identity determines the directory publisher name. For a skills-only package requiring local execution, follow the standard flow; if the portal rejects the local-executor field, resolve submission access with OpenAI. The approved-partner allowlisting requirement for local MCP servers applies to the separate sidebar scope.

A full marketing website, its additional hosting-specific legal pages, removing preview `noindex`, an additional scanner installation and sidebar partner approval are separate work. The published plugin privacy policy remains a submission prerequisite. None alone establishes that this skill package cannot be submitted. Passing local checks is not portal approval.

## Listing and assets

`listing.json` supplies English Codex presentation fields; `listing.de.json` supplies the German subtitle and description. The builder preserves the useful subtitle for both variants and generates host-specific invocation tables from the catalog. Claude receives shared package description, author, keywords, display name and primary icon through its native manifest. English/German long listing text describes the same eight workflows and limitations. OpenAI currently retains imported translations without displaying them in directory/API listing responses.

The cookbook/pan/egg mark has light/dark SVG originals and 512 × 512 PNGs under `assets/`, covered by the root MIT license. All four are bundled. No third-party marks, fonts, links or scripts are embedded in these icons. Third-party website artwork and icons retain their separate [notices](../THIRD_PARTY_NOTICES.md). Website assets are not bundled into the skill upload.

Local verification on 2026-10-22: build, check, check-sources and all 27 unit tests pass; the portable rebuild also passes all 27 tests and produces identical artifact hashes, including both store ZIPs. Archive checks compare every upload file with the generated plugin, preserve hidden manifests, exclude marketplace/MCP content and verify host-specific invocation tables. That polish pass did not include native or portal acceptance. The subsequent [Kitchen acceptance record](../docs/store-acceptance-2026-10-22.md) records the clean native reinstall, exact-byte verification, bounded behavior checks, upload-content scan and portal identity blocker; the maintainer subsequently confirmed all eight visible Kitchen skills and a working closing guide.

## Deutsch

Der Build erzeugt unter `dist/store/{kitchen,plain}/cookbook-by-pengusto.zip` je ein eigenes Upload-Paket mit Plugin-Manifest und Skills direkt im ZIP-Stamm. Die Download-ZIPs der Website bleiben lokale Marketplaces. Für den Store ist Kitchen seit dem Nutzerentscheid vom 2026-10-22 festgelegt; `bundle.json` hält die Auswahl fest. Plain bleibt als lokale Alternative erhalten. Die Sidebar mit lokalem MCP-Server bleibt separat.

Native Installation und begrenzte Nutzerabnahme sind bestätigt. Offen sind insbesondere die im Portal geforderte Publisher-Verifizierung, eine veröffentlichte Plugin-Datenschutzerklärung und die späteren Metadaten-, Skill- und Review-Ergebnisse. Frühere CLI-Tests belegen keine sichtbare Abnahme dieser Revision. Lokale erfolgreiche Prüfungen sind keine Store-Freigabe. Es wurde nichts hochgeladen, eingereicht oder veröffentlicht.

Für das reine Skill-Paket sind die vier MCP-Pflicht-URLs, MCP-Testfälle und ein MCP-Demovideo laut aktueller Dokumentation nicht erforderlich. Keine Zieladressen erfinden. `requires_local_executor: true` bleibt wegen lokaler Werkzeuge erhalten. Eine Partnerfreigabe für lokale MCP-Einreichungen betrifft die separate Sidebar; bei einer Portal-Ablehnung des Local-Executor-Felds muss der Einreichungszugang mit OpenAI geklärt werden. Eine vollständige Marketing-Website, zusätzliche Hosting-Rechtsseiten, `noindex` und optionale Zusatzscanner sind getrennte Aufgaben; die allgemeine Pflicht zu einer veröffentlichten Plugin-Datenschutzerklärung bleibt bestehen.

The general [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines) also require a meaningful purpose, reliable complete workflows and a published privacy policy. Trial/demo products are not accepted; skills-only listing eligibility is a review decision, not established by local tests.

References checked 2026-10-22: [Package layout](https://developers.openai.com/plugins/build/plugins), [submission and metadata](https://developers.openai.com/plugins/deploy/submission), [desktop-only plugins](https://developers.openai.com/plugins/deploy/desktop-only). Requirements may change; confirm portal findings against current documentation before submission.
