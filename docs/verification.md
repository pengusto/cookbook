# Verifikation

Aktueller Launch-Prüfstand 2026-10-15: [launch-readiness.md](launch-readiness.md) ersetzt ältere Statusaussagen unten. Historische Ergebnisse bleiben zur Nachvollziehbarkeit erhalten.

Aktueller Nachtrag 2026-10-15: [Host-Tests](host-tests.md) dokumentieren Codex-CLI-Installation und gezielte Szenarien aller fünf Skills sowie Claude-Code-Validierung und ZIP-Discovery. Claude-Modellaufrufe bleiben wegen fehlender Anmeldung blockiert. Review 0.1.1 enthält Store-Metadaten und Icons; acht Paketvertragstests bestehen. Die folgenden früheren Prüfstände sind historische Einträge.

Ausgeführt am 2026-10-12 mit Python 3.14.7. Dokumentierte Mindestversion 3.10 wurde nicht separat getestet.

| Prüfung | Ergebnis und Grenze |
|---|---|
| Build und Check | 6 Rezepte, 5 ZIPs; Metadaten, Dateihashes, ZIP-Inhalt/Prüfsummen und relative Links bestanden |
| Paketvertragstests | 4 Tests bestanden: deterministische vollständige Archive, bestehende Installation/Symlink erhalten, Kandidat abgelehnt, manipulierte Hashes/Pfade abgelehnt |
| Portable Kopie | Ohne .git, site, sources.local.json, .scratch und lokale Originale gebaut und geprüft; kein Clean-Clone-Test, weil noch kein Commit |
| Isolierte Installation | Alle 5 Pakete in temporären leeren Skill-Ordner installiert; zwei Builds mit identischen ZIP-Hashes |
| Quellen | Ausgewählte Originalprojekt-Dateien und Git-Status unverändert; Driftprüfung bestanden |
| Private Pfade | Keine maschinenspezifischen Benutzerpfade in den vorgesehenen Repository-Dateien. Did I Leak enthält absichtlich ein generisches /Users/-Erkennungsmuster; unverändert erhalten. |
| Gitleaks 8.30.1 | Redigierter Verzeichnisscan ohne Findings; kein erreichbarer Git-History-Scan, da noch keine Commits; kein TruffleHog-Lauf |
| Browser Desktop | 1200 Pixel; 6 Karten/5 Downloads, visuell geprüft, kein horizontaler Überlauf |
| Browser schmal | Emulierter 390-Pixel-Viewport; eine Spalte, kein horizontaler Überlauf; kein physisches Gerätetest |
| Interaktion | Erste Rezeptkarte per Klick geöffnet, Rezeptinhalt sichtbar; per Enter wieder geschlossen |
| Navigation/Downloads | Alle 14 internen Linkziele per Browser-fetch mit HTTP 200; Reload bestanden; keine fehlenden erforderlichen Ressourcen |
| Konsole | Nach Favicon-Korrektur und finalem Reload keine Fehler/Warnungen; absichtlicher Zugriff auf private Quellenregistrierung mit 403 abgelehnt |
| Privater Zustand | Quellenregistrierung und Punktordner nicht über Preview zugänglich; Server nur 127.0.0.1 |
| Agent/Host | Unabhängige Verhaltenstests und tatsächliche Host-Discovery nicht ausgeführt |

Die Vorschau lief auf 8767, weil 8766 belegt war. Externe Quellprojektlinks und Rechtsquellen wurden nicht pauschal auf Erreichbarkeit oder Aktualität geprüft; keine neuen rechtlichen Produkturteile erstellt. Screenshots konnten wegen der abweichenden Tool-Dateigrenzen nicht gespeichert werden; die Desktopansicht wurde direkt als Toolbild betrachtet.

Keine Veröffentlichung, Releases, Außenkommunikation, Pushes, Sichtbarkeitswechsel, Umbenennung oder Verschiebung bestehender Originalprojekte. Die neuen Cookbook-Dateien bleiben uncommitted für den privaten Review. Temporäre portable Kopie und Installationstestordner automatisch entfernt; .scratch enthält ausschließlich lokale Evidenz, keine Ersatzoriginale.

## Plugin-Ergänzung vom 2026-10-15

- Build/Check: sechs Rezepte, fünf Einzel-ZIPs und zwei Plugin-ZIPs; Manifeste, Marketplace-Pfade, Skill-Hashes, ZIP-Inhalte und vollständige SHA256SUMS geprüft.
- Sieben Tests bestanden, darunter bytegleiche Skills beider Hosts, deterministische Plugin-Archive samt versteckten Manifesten und Ablehnung unlizenzierter/fehlender/doppelter Bündeleinträge.
- Portable Kopie ohne dist, site, Git, lokale Quellenregistrierung und private Evidenz: Build, Check und Tests bestanden; alle sieben ZIP-Prüfsummen nach zweitem Build identisch. Temporäre Kopie automatisch entfernt.
- check-sources bestanden: ausgewählte Snapshots stimmen weiterhin mit lokalen Originaldateien überein. Keine Aktualisierung oder Migration der Originale vorgenommen.
- Codex CLI 0.160.0 und dessen Plugin-Hilfe gelesen. Keine Host-Installation/Registrierung. Claude Code nicht installiert; nativer Validator und tatsächliche Skill-Aufrufe offen.
- Aktuelle Browser-Navigation zur Loopback-Vorschau mit Verbindungsfehler gescheitert; neue Links nicht als browser-geprüft ausweisen. Keine Sicherheits-/Netzwerkeinstellungen verändert.
