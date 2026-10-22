# Kitchen store acceptance · 2026-10-22

Status: **native CLI acceptance and user-reported desktop short acceptance passed; submission still requires verified developer identity and a published privacy policy**. No ZIP upload, submission, publication, identity verification or external repository change was performed.

The maintainer selected Kitchen for the OpenAI/Codex store identity. `bundle.json` records this decision; Plain remains a supported local alternative. Both variants retain the same plugin identity. This is local acceptance of the prepared 0.3.1 package, not a new published release.

## Exact package and installation

- Upload: `dist/store/kitchen/cookbook-by-pengusto.zip`.
- SHA-256: `f78435a92a9d4c4ada0a01314d623316ad66485b656973ba5bbfe82f76d2eefe`.
- Codex CLI: `0.160.0`.
- All 42 native marketplace source files match the upload ZIP before installation.
- The pre-existing Kitchen cache differed only in its manifest and two READMEs. It was backed up with the user configuration, then this Cookbook plugin alone was natively removed and reinstalled from the already registered Kitchen marketplace.
- All 42 installed files then matched the upload ZIP exactly. Native listing reports version 0.3.1, installed and enabled. No marketplace or other plugin was removed.
- Native installation reformatted the user configuration: byte comparison differs, but parsed TOML before and after is identical. Original bytes remain in the private backup. No configuration was manually rewritten.

## Native discovery and bounded behavior

A fresh ephemeral Codex session ran with read-only execution in an isolated synthetic fixture. Configured MCP servers were disabled for that invocation only. The existing model configuration and authentication were used; no new model choice, login or global configuration was introduced.

An initial invocation failed before any model execution because quoted names in command-line MCP overrides produced an invalid transport configuration. Correcting the temporary override syntax resolved it; no user configuration edit was needed. The successful session exited 0, read all eight installed SKILL.md files and relevant references, and reported all eight native Kitchen IDs. Its tool events show only file reads. The fixture remained unchanged and was removed after verification.

| Workflow | Observed synthetic response |
|---|---|
| Prep the Kitchen | Small three-link portfolio brainstorm; no implementation or mandatory ticket system. |
| Are We Cooking | Uses the supplied CSV regression evidence; excludes the unaccepted dashboard redesign. |
| What Was I Cooking | Keeps missing early history provisional; does not treat unaccepted analytics as work. |
| Keep the Recipe Secret | GO WITH REVIEW for one unreadable file despite completed external scanners; no unconditional safety claim. |
| Can I Serve This | Treats a reported Tab skip as a reproduction lead, not proof of impossibility or legal clearance. |
| Ready to Serve | Does not invent missing preparation for a private review or require unnecessary translations/scanners. |
| What's New on the Menu | Requests the release line; classifies restored export as a fix and excludes uncommitted dashboard work. |
| Close the Kitchen | Closes the bounded supplied-evidence task without new work, push or archiving. |

These are eight scenarios in one bounded native smoke session. They verify discovery, reads and selected instruction-following behavior. They are not eight independent end-to-end product workflows, full real-repository scanner runs or visible desktop picker tests.

## Upload content review

The exact ZIP contains only the plugin payload, source provenance and licenses, usage documents, four icon assets and the eight reviewed skill trees. There is no marketplace wrapper, sidebar MCP server, private evidence, .git directory or website payload.

Gitleaks scanned an extraction of the exact ZIP with redaction and returned exit 0 with zero findings. The temporary extraction was removed automatically. A bounded text inventory covered all 40 UTF-8 files: its only local-path-shaped match was the scanner's generic `/Users/` detection regex, not a machine-specific user path. This scan covers the upload contents, not Git history, and is not a guarantee of absence of sensitive data.

## Visible desktop acceptance

The computer-use inventory identifies Codex, but selecting its bundle ID returns: `Computer Use is not allowed to use the app 'com.openai.codex' for safety reasons.` The available plugin connector tools expose search, dependencies and permissions, not the native picker or local workflow UI. Native CLI tests provide independent evidence; they do not bypass or replace the denied visual test. No desktop screenshot, icon/theme acceptance or visible workflow success is claimed.

The maintainer subsequently confirmed in this chat: **“Alle acht sichtbar; Abschluss-Guide funktioniert.”** This closes the requested visible picker/guide short acceptance as user-reported evidence. The agent did not observe the desktop directly. Host desktop version, theme/icon rendering and end-to-end real-project workflows were not separately reported.

## Portal findings and remaining work

The authenticated OpenAI Plugins page was inspected in the current Personal organization and Default project. Opening the upload entry displayed **Complete identity verification** and: “You need a verified developer identity before you can create or upload a plugin.” The dialog was cancelled; no file was selected and no draft was created. This is evidence for the inspected organization only, not a claim about other organizations.

1. Targeted desktop acceptance is complete: native reinstall/loading plus user-confirmed eight visible Kitchen skills and working closing guide. Retain the stated limits.
2. Confirm the intended owning organization/project. Complete its individual or business identity verification personally, then check the resulting directory publisher name against the listing. `Pengusto` in a JSON file does not verify the publisher or prove that it will be the directory name.
3. Finalize and publish a truthful privacy policy for this plugin, then use its real public URL. The metadata-import exemption for four MCP URLs does not waive the general plugin privacy-policy requirement; see [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines). A local [privacy draft](../store/privacy-policy.draft.md) records implementation facts and unresolved publisher/hosting details.
4. Confirm submission permission and the actual Developer Tools category after the identity gate is resolved. Merely seeing an upload button does not prove all permissions.
5. After explicit upload authorization, upload the exact Kitchen ZIP, resolve the portal's metadata and skill scan findings, then prepare submission for review. No automated portal result can be claimed before upload.
6. Complete applicable policy attestations and review separately; publish only after approval and direct authorization.

For the current skills-only package, the four MCP listing URLs, MCP demo recording and MCP review cases are not required by the cited metadata rules. Local MCP partner allowlisting concerns the separate sidebar. The local-executor flag stays true; if rejected by the portal, resolve submission access with OpenAI rather than hiding the requirement.

Review consideration: the general guidelines require a meaningful purpose beyond built-in capabilities and reject trial/demo products. This collection supplies evidence-oriented workflows and local scanning safeguards, but eligibility and product quality remain review decisions. The experimental source-Beta label is not evidence of a specific rejection; do not remove limitations just to imply maturity.

Primary references checked 2026-10-22: [OpenAI submission](https://developers.openai.com/plugins/deploy/submission) , [desktop-only plugins](https://developers.openai.com/plugins/deploy/desktop-only) and [general plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines). Portal findings take precedence over assumptions about access.

## Retention and Deutsch

Private pre-install rollback material and native-test evidence remain ignored under `.scratch/store-acceptance-2026-10-22/`. The backup is about 225 KiB; logs, synthetic responses and verification records are about 73 KiB. Visible short acceptance is confirmed; retain the original backup until a cleanup decision. The synthetic fixture and scanner extraction were removed after verification; no real project data was used in the synthetic fixture. This private evidence is not packaged.

Kitchen ist für den Store festgelegt. Die native Neuinstallation stimmt in allen 42 Dateien mit dem Upload-ZIP überein; Discovery und acht begrenzte synthetische Szenarien bestehen. Gitleaks meldet im genauen ZIP-Inhalt keine Funde. Der Nutzer hat alle acht sichtbaren Skills und den funktionierenden Abschluss-Guide bestätigt; das ist eine begrenzte Nutzerabnahme, keine vom Agenten beobachtete Oberfläche. Im geprüften Portal blockiert die noch fehlende Developer-Identitätsverifizierung bereits das Anlegen oder Hochladen eines Plugins. Zusätzlich fehlt eine veröffentlichte Datenschutzerklärung nach den allgemeinen Plugin-Richtlinien. Eigentümer-Organisation, Publisher-Anzeige, Einreichungsrechte und Portalprüfungen müssen danach bestätigt werden. Nichts wurde hochgeladen, eingereicht oder veröffentlicht.
