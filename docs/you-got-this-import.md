# You Got This / You’re the Chef · 0.6.0

Erstübernahme: 2026-10-24; Stilllegungsabgleich: 2026-10-31. Bestätigtes Namenspaar: **You Got This** (`you-got-this`, Plain) / **You’re the Chef** (`youre-the-chef`, Kitchen). Stabile Quell-ID: `you-got-this`.

## Herkunft und Pflege

Übernommen aus dem eigenen MIT-lizenzierten Repository `pengusto/you-got-this` (Originalverlauf: `history/you-got-this`), lokaler HEAD `d8ce9d530d74852ead13fac2f6994714808caff5`. Der gelesene installierte Skill-Text stimmt mit der lokalen Repository-Datei überein. Die ursprüngliche MIT-Datei mit Copyright Enis Uysal bleibt unverändert. Für künftige Änderungen ist `skills/you-got-this/` die gepflegte Cookbook-Quelle; das frühere Repo wird nicht zur Laufzeit oder beim Build geladen.

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

## Stilllegungsabgleich · 2026-10-31

Cookbook ist die einzige gepflegte Quelle: [Workflow](../skills/you-got-this/SKILL.md), [Installation](https://github.com/pengusto/cookbook#quickstart-choose-one-naming-style), [Website](https://pengusto.github.io/cookbook/). Der Katalog verweist nun auf Cookbook. Die historische Quellrevision oben bleibt als Herkunftsnachweis erhalten, nicht als Cookbook-Revision.

### Bestand und Übernahme

- Original-Remote: `main` bei `a97e1a19b9c5800c1e37575b2ebaa684c9e6456b`, zusätzlicher Branch `improve-project-discovery` bei `cbd03627e38f80bd939bbb4f1bac523a6af7f001`; keine Tags oder Releases/Assets. `history/you-got-this` und `history/you-got-this-discovery` erhalten beide Verläufe einschließlich Merge-Ancestry. Der Discovery-Branch entspricht im Inhalt dem bereits gemergten Stand.
- Der lokale Stand bei `d8ce9d5` enthält Änderungen an README, Bildprovenienz und Website-Test sowie unversionierte Banner, Prompts und Vorschauen. Der ausführbare Skill, MIT-Lizenz, Host-Metadaten und Beispiele enthalten keine noch fehlenden Änderungen. Cookbook hat darüber hinaus bereits den Modus `usertest`; dieser bleibt erhalten.
- Die ausgewählten Licht-/Dunkelbanner und exakten Prompts sind unter [design/you-got-this-retirement](../design/you-got-this-retirement/README.md) mit Hashes und Rechtevorbehalten erhalten. Die vollständigen Vorschauen und Originale bleiben gesichert; alte Website und Test-Skripte werden nicht als zweite Pflegequelle kopiert.
- Der lokale Test für HTML-Bilder und `srcset` ergänzt nun die vorhandene Cookbook-README-Linkprüfung. Die beiden Themenpfade und Alternativtexte werden damit geprüft. Die bestehenden Cookbook-Banner und das Buchdesign bleiben bestehen.
- GitHub: ein gemergter PR (#1, Discovery/Autorenlinks), ein offenes Issue (#2, JSON-LD auf der alten Landingpage), keine Kommentare dazu und keine Releases. Vollständige Daten sind im unabhängigen Backup erhalten. Cookbook besitzt bereits JSON-LD und Schema-Vertragstests für seine Buchseiten; der Vorschlag für die aufgegebene Standalone-Seite wird deshalb nicht dupliziert. Externe Validator-/Indexierungszusagen werden nicht übernommen.
- Keine belegten Software-Ergebnisse aus der alten Bannerillustration: sie zeigt einen Prozess, keine tatsächliche Produktprüfung. Es werden keine Erfolgszahlen oder Akzeptanzbelege daraus abgeleitet.

### Sicherung und Aufbewahrung

Vor Änderungen entstand außerhalb beider Repositories ein unabhängiger Sicherungsordner `you-got-this-2026-10-31` unter dem persönlichen Codex-Backupverzeichnis. Der lokale Übergabebericht enthält den absoluten Pfad; private Maschinenpfade gehören nicht in dieses öffentliche Repository.

Enthalten sind Remote-Mirror, Bundle aller lokalen Refs, vollständiges lokales Archiv einschließlich `.git`, uncommitteter/unversionierter/ignorierter Dateien sowie paginierte GitHub-Daten zu Konfiguration, Pages, Issues/Timelines, PRs/Reviews/Dateien/Commits, Deployments und Actions. Es gab keine Release-Assets oder Actions-Artefakte. Ein aktiviertes Wiki lieferte kein erreichbares Repository. Geheimwerte, ablaufende Logs/Caches und Benachrichtigungszustände sind keine wiederherstellbaren Quellbestände.

Prüfung: `git fsck --full` für den unabhängigen Remote-Mirror; lokales Bundle separat geklont und mit `fsck` geprüft; alle regulären Dateien im lokalen Archiv bytegenau gegen das Original verglichen; SHA-256-Manifest erstellt. Der temporäre Restore-Klon wurde danach entfernt. Aufbewahrung unbefristet bis zur ausdrücklichen Freigabe zur Entfernung. Lokale Originaldateien bleiben erhalten.

### Alte Website und Löschgrenze

Die alte Adresse `https://pengusto.github.io/you-got-this/` ist GitHub Pages direkt aus dem alten Repository (`build_type: workflow`, ohne eigene Domain). Eine dort veröffentlichte Weiterleitung lebt nur, solange dieses Repository besteht. Nach seiner Löschung ist die alte URL kein dauerhafter Einstieg. Der neue Einstieg ist [Cookbook](https://pengusto.github.io/cookbook/).

Die Migration bereitet einen sichtbaren Cookbook-Verweis im alten Repository und auf dessen Website vor. Das allein belegt keine abgeschlossene Löschung. Die Remote-Löschung erfolgt erst nach veröffentlichter und geprüfter Übernahme sowie ausdrücklicher Entscheidung zum Wegfall der alten URL; ihr tatsächlicher Status wird im lokalen Übergabebericht dokumentiert.

English: Cookbook is the sole maintained source. Both original remote histories and MIT attribution are preserved. Selected uncommitted artwork and its provenance are retained as design history; full local originals and GitHub metadata have an independent verified backup. The old Pages URL depends on the retiring repository and cannot retain a redirect after deletion. No host installation changes are part of this migration.
