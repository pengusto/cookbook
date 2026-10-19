# Skill-Namen und gemeinsame Quelle

Stand 2026-10-19 · Fassung 0.3.0. Acht MIT-lizenzierte Skills aus einer gepflegten Quelle; keine separaten Skill-Repos erforderlich.

| Stabile Quell-ID | Plain | Kitchen |
|---|---|---|
| `start-it-right` | How Do I Start? (`how-do-i-start`) | Prep the Kitchen (`prep-the-kitchen`) |
| `are-we-cooking` | Am I Making Progress? (`am-i-making-progress`) | Are We Cooking? (`are-we-cooking`) |
| `what-was-i-cooking` | Where Were We? (`where-were-we`) | What Was I Cooking? (`what-was-i-cooking`) |
| `did-i-leak` | Did I Leak? (`did-i-leak`) | Keep the Recipe Secret (`keep-the-recipe-secret`) |
| `will-they-sue-me` | Will They Sue Me? (`will-they-sue-me`) | Can I Serve This? (`can-i-serve-this`) |
| `let-them-see-it` | Am I Ready to Share? (`am-i-ready-to-share`) | Ready to Serve (`ready-to-serve`) |
| `what-did-we-change` | What Did We Change? (`what-did-we-change`) | What’s New on the Menu? (`whats-new-on-the-menu`) |
| `kill-the-todos` | Can We Finish? (`can-we-finish`) | Close the Kitchen (`close-the-kitchen`) |

Die stabile Quell-ID bleibt im Katalog und im Quell-Frontmatter erhalten. Beim Build werden nur Überschrift, Anzeigename und Aufruf-ID der gewählten Namenswelt eingesetzt. Ablauf und Lizenz sind in beiden Varianten gleich. Einzeldownloads und beide Host-Plugins enthalten dieselben ausgewählten Quelldateien. Keine zusätzlichen Alias-Skills; jeweils eine Variante installieren. Codex: `$<install-id>`, Claude: `/cookbook-by-pengusto:<install-id>`.

## What Was I Cooking? wieder aufgenommen

Die vom Nutzer selbst verfasste und privat genutzte Anleitung wurde am 2026-10-19 aus seiner vorhandenen Quelle übernommen. Sie war dort nicht in Git versioniert und hatte keine Lizenzdatei. Der Nutzer hat die Aufnahme nach dem gleichen MIT-Konzept bestätigt. Originaldateien bleiben unverändert; der Workflow-Text ist unverändert bis auf den Titelplatzhalter. Die ursprünglichen UI-Metadaten erhalten nur die gemeinsamen Titel-/ID-Platzhalter. MIT-Lizenz: Copyright 2026 Pengusto, wie bei den anderen eigenen Quellen. Verbindliche Runtime-Hashes stehen in catalog.json.

**Where Were We? / What Was I Cooking?** rekonstruiert Ziel, Zieländerungen, erledigte und offene Arbeit sowie Nebenwege. Es ist ein Rückblick ohne automatische Änderungen. **Am I Making Progress? / Are We Cooking?** bewertet den Fortschritt; **What Did We Change? / What’s New on the Menu?** erstellt Release-Notizen. Der Abschluss-Skill **Can We Finish? / Close the Kitchen** bleibt separat.

Die sieben früher importierten Git-Historien bleiben erhalten. Die vier ehemaligen GitHub-Einzelrepos wurden am 2026-10-18 auf Nutzerwunsch gelöscht. Die Erweiterung der Source-Beta auf 0.3.0 ist zur Veröffentlichung auf GitHub freigegeben. Keine Website deployt, keine Stores eingereicht, aktive Host-Installationen nicht verändert.
