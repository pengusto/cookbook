> Historical preparation record. For current Beta status, installation and limitations, use the [README](../README.md) and [public release review](public-release-review.md).

# Privater Review und Übergabe

Aktueller Launch-Prüfstand 2026-10-15: [launch-readiness.md](launch-readiness.md) ersetzt ältere Statusaussagen unten. Historische Ergebnisse bleiben zur Nachvollziehbarkeit erhalten.

Stand: 2026-10-15. **Bereit für privaten Review mit benannten Grenzen.**

Aktualisierung nach angeforderten Host-Tests: [host-tests.md](host-tests.md) ist der aktuelle Prüfstand. Codex hat alle fünf Skills erkannt und gezielte Szenarien ausgeführt; externe Scannerabdeckung bleibt eingeschränkt. Claude Code 2.1.295 besteht strikte Plugin-/Marketplace-Validierung und lädt das finale ZIP mit allen fünf Skills; Modellaufrufe benötigen eine Anmeldung. Die temporäre Codex-Testinstallation wurde entfernt. Review 0.1.1 enthält Listing-Texte und Icons, weiterhin ohne Veröffentlichung. Frühere Aussagen unten zu fehlender Host-Prüfung sind durch diesen Nachtrag ersetzt.

## Ergebnis

Sechs kuratierte Rezepte; fünf installierbare, deterministische MIT-Snapshots. Are We Cooking? bleibt ein redaktioneller Kandidat ohne kopierten Skill. Inventar: 22 eigene Skills unter Own plus Will They Sue Me. Cookbook-Texte und Werkzeuge unter ausdrücklich gewählter MIT-Lizenz; Original-Lizenzen unverändert.

Lokales Repository ohne Remote. Originale, vorhandene Installationen, Quellhistorien und Änderungen wurden nicht bearbeitet. Die neue Git-Historie enthält keine fremden Repository-Historien. Installiert wurde ausschließlich in temporären Prüfverzeichnissen; diese werden automatisch entfernt.

## Zustände und Nachweise

| Stufe | Cookbook-Stand |
|---|---|
| Lokal | Katalog, Dokumentation, Snapshots, Installer, ZIPs und Vorschau erstellt |
| Geprüft | Hashes, Metadaten, relative Links, Paketinhalt, Prüfsummen und isolierte Installation; vier Paketvertragstests |
| Committed | Noch kein Commit; Dateien liegen reviewbar im lokalen Repository |
| Pushed | Nein; kein Remote |
| Deployed | Nein |
| Browser | Lokale Vorschau; finale Abnahme-Ergebnisse in verification.md |
| Agent-Verhalten | Nicht unabhängig getestet; Szenarien in behavior-review.md |

Aktuelle lesende GitHub-Prüfung des separaten Will-They-Sue-Me-Projekts: visibility=private, main=9c2fac2ba85f3624322ce48b7d18560ddd155222, has_pages=false; Pages-Endpunkt liefert 404. Das bestätigt kein aktiv eingerichtetes Pages-Projekt. Keine neue CI-Prüfung vorgenommen. Can I Serve This? bleibt eine Namensalternative, kein Rename.

## Review starten

`site/index.html` direkt öffnen oder im Repository `python3 scripts/cookbook.py serve --port 8767` ausführen und http://127.0.0.1:8767/site/ öffnen. Der Standardport 8766 war während der Prüfung bereits belegt; deshalb wurde 8767 verwendet. Die Vorschau bindet nur Loopback. Markdown-Links zeigen Rohdokumente; die Rezeptkarten sind die lesbare Browseroberfläche.

## Nächste Entscheidungen

1. Die sechs Rezepte und ihre Einsatzmomente redaktionell bestätigen oder ersetzen.
2. Lizenz für den originalen Are-We-Cooking-Skill separat entscheiden. Die Cookbook-MIT-Wahl wird nicht auf unlizensierte Originale übertragen.
3. Unabhängige Agent-Szenarien durchführen und Host-Erkennung testen, bevor Verhaltensqualität behauptet wird.
4. Falls ein privater GitHub-Review gewünscht ist: Ziel pengusto/vibe-coding-cookbook, visibility private, main, ausschließlich die Git-Dateien dieses lokalen Repositorys. Nach Review ausdrücklich Repository-Erstellung und Push freigeben; keine Pages-Aktivierung. Vor dem Senden Quellen, Rechte, private Daten und erreichbare History erneut am konkreten Commit prüfen.

Ein Remote ist für diesen lokalen Review nicht erforderlich. Public Release, Sichtbarkeitswechsel, Außenkommunikation und Deployment bleiben separate direkte Freigaben.

Vorgeschlagene Commit-Nachricht: `feat: prepare curated private cookbook review`

## Ergänzung: lokale Plugin-Bündel (2026-10-15)

Zwei Plugin-Pakete für Codex und Claude Code sind vorbereitet; fünf Einzel-ZIPs bleiben erhalten. Gemeinsame Auswahl und Review-Version in bundle.json; bytegleiche Skill-Dateien in allen Ausgaben. Lokale Marketplace-Dateien unter dist/codex und dist/claude, keine globale Registrierung oder Aktivierung. EN/DE-Anleitungen und Quellenmanifest liegen jedem Plugin bei. Siehe [Einrichtung und Website-Anbindung](plugins.md).

Sieben Paketvertragstests sowie portabler Build ohne lokale Quellregistrierung bestanden; sieben ZIP-Prüfsummen bei zwei Builds identisch. Keine native Host-Ladeprüfung: Claude Code ist nicht installiert; Codex wurde nicht registriert/aktiviert. Die neue Browserprüfung erreichte den lokalen Server nicht; die ältere Browserabnahme vom 12.10. gilt nicht als Nachweis für die neuen Download-Links. Lokale Dateilinks und Paketdateien wurden geprüft.

Einzelne Skill-Websites und Originalrepos bleiben unverändert. Ihr späterer Anschluss an die gemeinsamen Downloads ist dokumentiert, nicht veröffentlicht. Commit-Vorschlag für diese Ergänzung: `feat: package cookbook skills for Codex and Claude`.
