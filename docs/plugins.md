> **0.5.0 publication:** thirteen workflows; current install, website and Store boundaries: [publication.md](publication.md). Earlier acceptance results below are version-specific historical evidence.

# Zwei alternative lokale Installationen

Aktueller Stand: [README](../README.md) und [Zusammenführung](consolidation.md). Die lokale Fassung 0.4.0 heißt Cookbook by Pengusto. Ein gemeinsames Repo und zwölf gemeinsame Quellen erzeugen Plain mit einfachen Fragen oder Kitchen mit Koch-Namen.

| Ausgabe | Plain | Kitchen |
|---|---|---|
| Codex | dist/plain/codex | dist/kitchen/codex |
| Claude Code | dist/plain/claude | dist/kitchen/claude |
| Optionale Sidebar | dist/plain/sidebar | dist/kitchen/sidebar |

Je Host werden gleiche Plugin- und Marketplace-Identitäten verwendet, daher jeweils eine Alternative installieren. Paketnamen enthalten zur Unterscheidung die Variante; installierte Skill-Verzeichnisse und Aufrufe tragen nur die gewählte Namenswelt. Einzel-ZIPs bleiben möglich. Gleiche Skill-Bodies, Skripte, Referenzen und Lizenzen kommen aus derselben gemeinsamen Quelle.

Zum Wechsel vorherige Pakete sichern, das bestehende Plugin nativ deinstallieren, nur seinen Marketplace abmelden und den neuen Pfad registrieren/installieren. Das alte vibe-coding-cookbook ist eine andere Identität und muss vor dauerhaftem Betrieb bewusst deaktiviert oder gesichert abgelöst werden; der Build wechselt bestehende Nutzerinstallationen nicht automatisch. Frühere 0.1.x-Installationsnachweise in host-tests.md bleiben historische Nachweise.

Native Manifest- und Ladeprüfungen stehen in [skill-review-0.3.1.md](skill-review-0.3.1.md), getrennt von Pakettests und sichtbarer Desktop-Abnahme. Eigene Store-Upload-ZIPs unter `dist/store/{plain,kitchen}/` enthalten das Plugin ohne Marketplace-Hülle; siehe [Store-Vorbereitung](../store/README.md). Diese Vorbereitung lädt nichts hoch und reicht nichts ein.

Die optionale Kochbuch-Sidebar kann beide Anzeigenamenswelten zeigen: Kitchen/Klartext umschalten, den anderen Namen direkt unter dem Titel lesen. Kopieren verwendet immer den Aufruf des tatsächlich gebauten Pakets. Die Auswahl verändert keine Installation und erzeugt keine Skill-Duplikate. Siehe [Namensreview und Vorschläge](naming-review-2026-10-22.md).

Aktuelle lokale Erweiterung: zwölf Workflows in 0.4.0, Sidebar 0.4.1. Historische Abnahmen oben bleiben zeitgebunden. [Installations- und Aufrufnachweis](skill-installation-0.4.0.md).
