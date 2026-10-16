# Evaluation vor Änderungen

Historischer Auswahlbericht vom 2026-10-12. Aktuell sind sieben Skills MIT-lizenziert und integriert; Kill the TODOs wurde zum Abschluss-Skill weiterentwickelt. Aktueller Stand: [Namen und Quellen](skill-naming.md) und [Launch-Prüfstand](launch-readiness.md).

Stand 2026-10-12; Workflow: Let Them See It. Der Benutzer hat Inventar, kleine lokale Struktur, Katalog, installierbare Artefakte, Dokumentation und private Review-Vorbereitung konkret beauftragt. Keine erneute Scope-Freigabe nötig; MIT für neue Cookbook-Texte/Werkzeuge wurde separat ausdrücklich gewählt.

| Priorität | Evidenz | Änderung | Abnahme |
|---|---|---|---|
| Nötig | Leerer Workspace; skill-library besitzt manage.py, lokale Registrierung, Template und Export | Kleine kuratierte Auswahl nach demselben Quellenprinzip; bestehende Bibliothek unverändert | Originaldateien/Status bleiben gleich; unabhängiger Build ohne Quellenzugriff |
| Nötig | MIT bei fünf ausgewählten Skills; keine Lizenz bei Are We Cooking | Original-LICENSE je Snapshot; Kandidat ohne Download | Dateien und Hashes nachvollziehbar |
| Nötig | Quellen enthalten Sites, Assets und persönliche Integrationen | Explizite Runtime-Dateiliste statt Komplettkopie | ZIP-Mitglieder entsprechen exakt catalog.json |
| Empfohlen | Benennung allein erklärt Einsatzzweck nicht | Sechs Rezeptkarten mit fünf Schritten, Grenzen und Beispiel | Lokale Vorschau mit lesbarer Nutzerreise |
| Empfohlen | Kein neuer Laufzeitbedarf | Python-Standardbibliothek, HTML/CSS und native details | Kein Paketmanager oder JS-Framework |
| Empfohlen | Öffentliche Dokumentation später sinnvoll | README.md und docs/readme/README.de.md | Gegenseitige Links und gleiche Befehle/Inhalte |

## Bereits vorhanden und bewusst nicht dupliziert

skill-library ist ein lokaler breiter Katalog mit ignoriertem sources.local.json. Sein Export nimmt große Teile eines Quellordners auf und verwendet Dateizeitstempel. Für diese Auswahl wird deshalb nur das Muster übernommen; der Cookbook-Build nutzt geprüfte Dateilisten und feste ZIP-Metadaten. Die Bibliothek hat bestehende untracked Dateien und wird weder versioniert noch verändert.

## Präsentation und GitHub-Flächen

Statt externer Badge-Bilder steht eine überprüfbare Statuszeile unter beiden README-Titeln. Dynamische CI-, Release- oder Download-Badges wären ohne Cookbook-Remote irreführend. Repository-Beschreibung später: “Curated agent-skill recipes for starting, reviewing, and preparing projects.” Mögliche Topics später: agent-skills, developer-tools, cookbook. Beides ist nur Vorschlag.

Sponsors, Discussions, Releases, Social Preview, Traffic-Auswertung und CITATION.cff sind für den lokalen Review nicht nötig. Es gibt keine zugesagte Community- oder Security-Mailbox. CONTRIBUTING, Code of Conduct, Issue-Templates und Changelog werden erst ergänzt, wenn ein echter Kollaborations- oder Release-Prozess sie braucht. Keine CI ohne Remote; dieselben lokalen Checks können später in einer schmalen Workflow-Datei laufen. Keine Pages-Konfiguration oder öffentliche Legal-Seiten für die private Loopback-Vorschau.

## Veröffentlichungsgates

Skill-Verhalten unabhängig testen, Quellen erneut reviewen, Kandidatenrechte klären, vollständigen Inhalt und erreichbare Git-Historie am tatsächlichen Veröffentlichungscommit prüfen. Persönliche Quellenpfade bleiben ignoriert. Nie Scanner-Stille mit umfassender Sicherheit gleichsetzen. Diese Vorbereitung erlaubt weder Push noch Veröffentlichung.
