# You Got This / You’re the Chef · 0.6.0

Stand: 2026-10-24, lokale Übernahme. Bestätigtes Namenspaar: **You Got This** (`you-got-this`, Plain) / **You’re the Chef** (`youre-the-chef`, Kitchen). Stabile Quell-ID: `you-got-this`.

## Herkunft und Pflege

Übernommen aus dem eigenen MIT-lizenzierten Repository [pengusto/you-got-this](https://github.com/pengusto/you-got-this), lokaler HEAD `d8ce9d530d74852ead13fac2f6994714808caff5`. Der gelesene installierte Skill-Text stimmt mit der lokalen Repository-Datei überein. Die ursprüngliche MIT-Datei mit Copyright Enis Uysal bleibt unverändert. Für künftige Änderungen ist `skills/you-got-this/` die gepflegte Cookbook-Quelle; das frühere Repo wird nicht zur Laufzeit oder beim Build geladen.

| Übernommene Datei | SHA-256 der gelesenen Originaldatei |
|---|---|
| `SKILL.md` | `acd9f67b01cd9099f0cb2c83de7b435e1b6dd0993b45a66c13d3128fe3667951` |
| `LICENSE` | `9131b11f9a1af740b404b4dfb8208db9ead2822aac31c8342081ce7246679da6` |
| `agents/openai.yaml` | `772440bb77de3e09c6f09371012b242d8fb44db22c128c6ac0c2866df658182b` |
| `examples.md` | `98efde28a1c4a7d7381308495eb5d9f3aa1c53801caf0317e00e475ccfdc59d5` |

Die Anleitung bleibt einschließlich Default-, Gauntlet- und Audit-Modus erhalten. Änderungen: Titel und Selbstaufrufe sind gemeinsame Platzhalter, Host-Metadaten folgen dem Cookbook-Muster, Beispiele verwenden die installierte Variante, und eine kurze Abgrenzung erläutert die Nachbar-Workflows. Das Cookbook enthält keine zweite Kopie der Standalone-Website oder ihrer Banner.

## Eigenständiger Einsatzmoment

- **You Got This / You’re the Chef:** führt ein autorisiertes Projektziel selbstständig aus, prüft das integrierte Ergebnis und verbessert wichtige Lücken.
- **How Do I Start? / Prep the Kitchen:** übersetzt eine Idee in den ersten prüfbaren Abschnitt.
- **Finish My Prompt / Finish My Order:** vervollständigt einen Prompt als Entwurf; führt ihn nicht aus.
- Fortschrittscheck, Produktreview und Release-Vorbereitung behalten ihre engeren Aufgaben. Der neue Skill bindet passende verfügbare Fachworkflows bei Bedarf ein; keine Pflichtkette und keine externen Skill-Abhängigkeiten.

Der neue Kitchen-Aufruf ist `$youre-the-chef`, Plain `$you-got-this`; Claude verwendet die dokumentierte namespaced Syntax. Ein Namensschalter im Buch installiert keinen Alias. Die beiden Host-Pakete werden aus derselben Quelle erzeugt; Version 0.6.0 benennt die lokale Erweiterung, keinen veröffentlichten Release.

## Originalrepo bleibt erhalten

Das ursprüngliche lokale Repository hat uncommittete Dokumentations-, Test- und Bildarbeiten. Es wurde weder gelöscht noch archiviert, seine Remote-Adresse wurde nicht verändert. Vor späterer Stilllegung diese Arbeit und die eigenständige Website gesondert prüfen und sichern. Aufnahme in Cookbook ist keine Autorisierung zur Löschung oder Archivierung des GitHub-Repositories und keine Änderung einer aktiven Host-Installation.

English: Cookbook now maintains the imported workflow from a single canonical source, preserving the original MIT license and source checksums. Both naming variants share its instructions and mode behavior. The standalone repository, its history and local uncommitted work remain intact; no archive, deletion, installation, push or publication occurred.
