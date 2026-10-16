# Zwei alternative lokale Installationen

Aktueller Stand: [README](../README.md) und [Zusammenführung](consolidation.md). Review 0.2.0 heißt Cookbook by Pengusto. Ein gemeinsames Repo und sieben gemeinsame Quellen erzeugen Plain mit einfachen Fragen oder Kitchen mit Koch-Namen.

| Ausgabe | Plain | Kitchen |
|---|---|---|
| Codex | dist/plain/codex | dist/kitchen/codex |
| Claude Code | dist/plain/claude | dist/kitchen/claude |
| Optionale Sidebar | dist/plain/sidebar | dist/kitchen/sidebar |

Je Host werden gleiche Plugin- und Marketplace-Identitäten verwendet, daher jeweils eine Alternative installieren. Paketnamen enthalten zur Unterscheidung die Variante; installierte Skill-Verzeichnisse und Aufrufe tragen nur die gewählte Namenswelt. Einzel-ZIPs bleiben möglich. Gleiche Skill-Bodies, Skripte, Referenzen und Lizenzen kommen aus derselben gemeinsamen Quelle.

Zum Wechsel vorherige Pakete sichern, das bestehende Plugin nativ deinstallieren, nur seinen Marketplace abmelden und den neuen Pfad registrieren/installieren. Das alte vibe-coding-cookbook ist eine andere Identität und muss vor dauerhaftem Betrieb bewusst deaktiviert oder gesichert abgelöst werden; der Build wechselt bestehende Nutzerinstallationen nicht automatisch. Frühere 0.1.x-Installationsnachweise in host-tests.md bleiben historische Nachweise.

Native Manifest- und Ladeprüfungen des neuen Standes werden in consolidation.md getrennt von Pakettests erfasst. Nichts veröffentlicht.
