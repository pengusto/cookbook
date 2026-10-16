# Repository preparation / Repository-Vorbereitung

Stand: 2026-10-16. GitHub-Metadaten authentifiziert gelesen und die vier vorhandenen origin/main-Branches frisch gefetcht. Kein Push, keine Remote-Erstellung, kein Release oder Deployment.

## Bestehende GitHub-Repositories

| Repository | Sichtbarkeit | Lokaler HEAD / origin/main | Lokale Änderungen |
|---|---|---|---|
| [start-it-right](https://github.com/pengusto/start-it-right) | public | `cb7d6153e5` · 0 voraus / 0 zurück | Skill-Beschreibung und/oder agents-Metadaten uncommittet |
| [did-i-leak](https://github.com/pengusto/did-i-leak) | public | `f3bd587b35` · 0 voraus / 0 zurück | Skill-Beschreibung und/oder agents-Metadaten uncommittet |
| [will-they-sue-me](https://github.com/pengusto/will-they-sue-me) | private | `9c2fac2ba8` · 0 voraus / 0 zurück | Skill-Beschreibung und/oder agents-Metadaten uncommittet |
| [let-them-see-it](https://github.com/pengusto/let-them-see-it) | public | `908abc50d4` · 0 voraus / 0 zurück | Skill-Beschreibung und/oder agents-Metadaten uncommittet |

GitHub enthält bei allen vier bereits SKILL.md, README und LICENSE. Start It Right enthält Referenzen; Did I Leak zusätzlich Scanner, Tests und Website-Dateien; Will They Sue Me Referenzen, lokale Prüfscripts und Website-Dateien; Let Them See It Website, Dokumentprüfungen und Übersetzungen. Did I Leak und Let Them See It melden aktivierte GitHub Pages; deren Erreichbarkeit und aktueller Deployment-Stand wurden hier nicht geprüft. Bei keinem der vier wurden GitHub-Releases zurückgegeben.

## Nur lokal vorbereitete Repositories

- `vibe-coding-cookbook`: Sammlung, Website-Quellen, Paketgenerator, beide Host-Manifeste, optionale Sidebar und Tests.
- `are-we-cooking`: Check Progress / Are We Cooking?
- `what-did-we-change`: What Did We Change / What’s New on the Menu?
- `kill-the-todos`: Finish This Chat / Close the Kitchen; bestehende lokale Historie bleibt erhalten.

GitHub-Abfragen dieser vier Namen unter pengusto ergaben 404: nicht vorhanden oder für das aktuelle Konto nicht zugänglich. Keine Remote-Adresse erfunden oder eingetragen. Lokale Vorbereitung umfasst README, MIT-Lizenz, Host-Metadaten, passende Ignore-Regeln und lokale Git-Commits. Bestehende vier GitHub-Repos werden durch diese Vorbereitung weder committet noch gepusht. Die drei Skill-Quellen sind lokal sauber committet: Are We Cooking `f32f94c0c5`, What Did We Change `1432a33116`, Close the Kitchen `c309e60b17`. Cookbook erhält einen lokalen Initial-Commit; kein Remote wird hinzugefügt.

## Warum Skill-Dateien im Cookbook liegen

Ein Originalrepo pro Skill ist die einzige editierbare Quelle. `skills/<id>/` im Cookbook ist ein bewusst versionierter, durch catalog.json gehashter Review-Snapshot. Der Paketgenerator erzeugt daraus Einzel-ZIPs und bytegleiche Skill-Inhalte in beiden Plugin-Bündeln. Das ist eine Distributionskopie, keine zweite aktive Installation und kein zweites gepflegtes Original.

Codex lädt nach der lokalen Bereinigung jede der sieben IDs einmal aus dem Cookbook-Plugin. Claude hat ebenfalls jeden namespaced Aufruf einmal. Wer ein Bündel installiert, sollte dieselben Skills nicht zusätzlich einzeln installieren. Einzelinstallation bleibt für Nutzer ohne Bündel möglich.

Generierte Website, ZIPs, dist-Ausgabe, private Quellpfade und Testevidenz bleiben ignoriert. Lokale Commits veröffentlichen nichts. Vor späterer Veröffentlichung sind weiterhin sichtbare Host-Abnahme, öffentliche Ziele, Rechtsseiten und Store-Voraussetzungen zu klären.

English: Four existing GitHub repositories were read and fetched; local HEAD equals origin/main, while newer skill naming metadata remains uncommitted. Three repositories are public and Will They Sue Me is private. Four other repository names returned 404. Their local sources are prepared without creating a remote or pushing. Cookbook skill snapshots are intentional distribution copies of the original sources; they are not duplicate active installations.
