# README presentation

Use this guide only when the repository review identifies a concrete presentation gap. First state the reader’s question, then propose the smallest useful change in the evaluation table. Preserve the existing quickstart and good writing. Apply the agreed scope; do not install tools or publish assets merely because they appear here.

## Choose by project and reader need

| Project / question | Preferred evidence | When to skip |
| --- | --- | --- |
| A short public code example needs visual emphasis | Optional Carbon image alongside the same copyable code | A normal fenced code block is already clear |
| Small library: how do I use it? | Short, copyable API example and expected result | A screenshot or animation adds no information |
| CLI: what happens when I run it? | Brief real terminal demo; VHS when reproducibility helps | A command and its text output already explain it |
| Website or game: what does it look like? | Current screenshot or short clip of the real product | Existing media already answers the question |
| Multi-component service or MCP: how does data move? | One small Mermaid flow or sequence diagram based on inspected code | A sentence explains the entire flow |
| Skill: how do I invoke it and what does it do? | Invocation, realistic input and reviewed outcome; distinguish actual agent behavior from package checks | A decorative terminal recording would only simulate behavior |
| Tiny repository: what is missing? | Nothing extra when purpose and quickstart suffice | Do not invent a presentation requirement |

## Structure reference

[Best-README-Template](https://github.com/othneildrew/Best-README-Template) (Unlicense) is an optional reference for missing sections, not a file to impose on every project. Select relevant material from its blank template; remove placeholders, irrelevant sections and decorative badges. Derive installation, configuration and examples from the target repository. Do not copy example commands or change the project's license to match the template. Keep secrets out of source-code configuration examples.

Acceptance: purpose is clear, a newcomer can follow the verified quickstart, links resolve, and claims match supported behavior. No runtime, account or installation is needed to consult the reference.

## Reproducible CLI demo

[VHS](https://github.com/charmbracelet/vhs) (MIT) turns a versioned `.tape` into a terminal recording. Consider it selectively when a real CLI interaction benefits from a demo. Reuse installed tools and the project's existing asset conventions first. Local VHS requires `ttyd` and `ffmpeg`; check prerequisites and available versions before proposing installation. This guide does not authorize package installation or a new CI dependency.

Tape commands execute real programs. Use disposable data and bounded actions; never operate on production merely to record a demo. Inspect every frame for credentials, personal data and private paths. Store a short recording and, when useful, its source tape in the project's existing documentation assets location. Do not invoke VHS hosting/publish or server features for this workflow.

Acceptance: reproduce the recording from its source when feasible, inspect the complete output, check legibility and file size, and retain copyable commands plus a useful text description. Report unavailable tooling or untested playback rather than claiming completion. A successful recording is not an agent behavior test.

## Optional code image

[Carbon](https://github.com/carbon-app/carbon) (MIT) styles a short code snippet and exports PNG or SVG. Consider it for a useful visual highlight, such as a compact API example, only when the image adds clarity. Keep the same code in a copyable fenced block or linked source file; an image must never be the only installation command or usage example. Do not replace real product screenshots or terminal output with a styled snippet.

Prefer the browser editor for an occasional public snippet; no plugin, CLI, PWA installation or account is required for the proposed basic workflow. Check the current editor and export availability before promising a format. Do not install Carbon or add a rendering dependency to the repository automatically. The hosted service is an external destination: use only public or explicitly approved, sanitized code. Do not put secrets or private source into the editor, a Gist, a share link or a saved snippet. A local setup is a separate project decision, not proof that every feature runs without external services.

Store an exported image in the existing documentation assets location and reference that local file, rather than depending on a live embed or publishing a saved snippet. Provide meaningful alt text, readable contrast and font size, a suitable file size and checked font/asset rights. Keep the visual and copyable version synchronized.

Acceptance: compare the export against the canonical example, verify that the copied text works when feasible, and inspect the image at the README's intended size in light and dark contexts. Record actual export/render checks and anything untested. No account connection, snippet publication or external upload beyond the approved public input is implied.

## Explanation diagram

[Mermaid](https://github.com/mermaid-js/mermaid) (MIT) can be used directly in a fenced `mermaid` block on GitHub; ordinary README use needs no package or MCP installation. See [GitHub diagram documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).

Keep one diagram small and tie every component and edge to the inspected implementation. Exclude private endpoints and credentials. Prefer native GitHub syntax over adding a renderer; consider a project-local renderer only for an actual export requirement. GitHub and local renderer versions can differ.

Acceptance: verify labels and flow against code, inspect legibility in light and dark themes, and check the actual GitHub preview when available. Local syntax/render success does not prove GitHub rendering. If preview is unavailable, explicitly record that remaining gate. Include a short textual explanation of the flow.

## Boundaries

No mandatory generator, template, badges, subscription or external hosting. Check rights to screenshots, fonts, logos and recorded data separately from each tool's software license. Keep selected translations consistent. Report what was generated, rendered, actually exercised and left unverified; do not imply release or CI success from visual polish.
