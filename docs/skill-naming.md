# Skill-Namen und Quell-Repositories / Names and source repositories

Stand: 2026-10-15, lokale Review-Fassung 0.1.3. Die sieben kuratierten Cookbook-Skills haben jeweils ein eigenes lokales Git-Quellprojekt. Keine Originalordner verschoben, keine neuen Remotes angelegt und nichts veröffentlicht.

| Verständlicher Name | Koch-Titel | Unveränderte ID | Paket |
|---|---|---|---|
| Start It Right | Prep the Kitchen | `start-it-right` | Einzeln + Codex/Claude |
| Check Progress | Are We Cooking? | `are-we-cooking` | Einzeln + Codex/Claude |
| Did I Leak? | Keep the Recipe Secret | `did-i-leak` | Einzeln + Codex/Claude |
| Will They Sue Me? | Can I Serve This? | `will-they-sue-me` | Einzeln + Codex/Claude |
| Let Them See It | Ready to Serve | `let-them-see-it` | Einzeln + Codex/Claude |
| What Did We Change | What’s New on the Menu? | `what-did-we-change` | Einzeln + Codex/Claude |
| Finish This Chat | Close the Kitchen | `kill-the-todos` | Einzeln + Codex/Claude |

Beide sichtbaren Namen stehen in den Codex-UI-Metadaten; Koch-Namen sind auch in den Skill-Beschreibungen auffindbar. Du kannst im normalen Chat beide Namen nennen. Das erzeugt keine zusätzlichen Slash-Commands: der exakte Codex-Aufruf bleibt `$<id>`, im Claude-Bündel `/vibe-coding-cookbook:<id>`. Keine duplizierten Alias-Skills.

## Ein Quellprojekt, mehrere Ausgaben

Originalprojekt → bewusst ausgewählte, gehashte Dateien in `skills/<id>/` → identische Einzelpakete und beide Plugin-Bündel → Cookbook-Karte mit beiden Namen. Lokale Quellpfade stehen ausschließlich in der ignorierten `sources.local.json`. Bestehende Repository-URLs bleiben erhalten; für neue lokale Repos wird keine öffentliche URL erfunden. Änderungen dieser Runde sind uncommitted, daher identifizieren Dateihashes die Snapshots statt einer vermeintlich passenden Commit-Revision.

`what-did-we-change` hat jetzt ein eigenes lokales Git-Repository. Die vorhandenen sechs anderen Repositories bleiben bestehen. `are-we-cooking` ist nach ausdrücklicher Nutzerwahl ebenfalls MIT-lizenziert und vollständig aufgenommen. Die bereits gewählte MIT-Lizenz gilt für den neu verfassten Abschluss-Skill; andere Quell-Lizenzen wurden nicht ersetzt.

## Ein Abschluss-Skill

`kill-the-todos` wurde zu **Finish This Chat · Close the Kitchen** weiterentwickelt. Er rekonstruiert den vereinbarten Umfang, empfiehlt zuerst einen kleinen Abschluss-Guide und erledigt dann nur die autorisierte Arbeit. Ein Guide-only-Auftrag oder eine bewusste Pause verändert weder Dateien noch Aufgabenstatus. Vertagte Arbeit ist offen, fehlgeschlagene Checks bleiben sichtbar. Keine automatischen Archivierungs-, Publikations- oder Löschaktionen. Der frühere zusätzliche Entwurf `close-the-kitchen` wurde darin konsolidiert.

Die tatsächlichen lokalen Verhaltenstests und Grenzen stehen in [host-tests.md](host-tests.md). Es wurden keine separaten Skill-Websites migriert oder bestehenden globalen Plugin-Installationen ersetzt.

English: Each of the seven curated entries has its own local source Git repository and two visible names, with stable IDs. All seven licensed snapshots are individually installable and bundled identically for Codex and Claude. The closing workflow replaces the former Kill the TODOs behavior rather than adding an overlapping skill. Natural-language display aliases do not create additional slash commands. Nothing was published.
