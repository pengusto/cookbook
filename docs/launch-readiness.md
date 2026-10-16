> **Historischer Prüfstand 0.1.x.** Die aktuelle Architektur, Namenswelten und Installationswege stehen in [consolidation.md](consolidation.md) und der [README](../README.md). Frühere Testergebnisse werden nicht als neue 0.2.0-Abnahme behauptet.

# Launch readiness / Launch-Prüfstand

2026-10-15 · Review 0.1.4 · lokal vorbereitet, nichts veröffentlicht. Dieser Stand ersetzt frühere Launch-Zusammenfassungen; historische Host- und Validator-Ergebnisse bleiben mit ihrer jeweiligen Version in den Prüfberichten erhalten.

## Lokal vorbereitet

- Sieben eigene Skill-Quellprojekte, jeweils mit eigenem lokalem Git-Repository und zwei sichtbaren Namen. Bestehende IDs und Originalordner bleiben erhalten. What Did We Change wurde lokal mit Git initialisiert. Keine neuen Remotes, Commits, Pushes oder externen Repository-Änderungen.
- Alle sieben Skills sind MIT-lizenziert. Are We Cooking wurde nach ausdrücklicher Nutzerwahl aufgenommen. Der neu verfasste Abschluss-Skill Finish This Chat / Close the Kitchen entwickelt `kill-the-todos` weiter; kein konkurrierender zweiter Skill.
- Sieben Einzelpakete und identische Skill-Dateien in beiden Codex-/Claude-Bündeln. Icons und Listing-Metadaten sind enthalten. Die optionale Sidebar-Ausgabe zeigt denselben Katalog; bestehende globale Plugin-Installationen wurden nicht ersetzt.
- Website mit sieben Karten, beiden sichtbaren Namen, Originalanleitungen, Installation/Hilfe und neun Downloads. JSON-LD enthält ausschließlich passende sichtbare Inhalte, einschließlich `alternateName`; keine erfundenen URLs. Die aktualisierte Code-Prüfung für alle sieben Einträge und beide Namen meldet bei Schema.org 0 Fehler/0 Warnungen; Google erkennt keine Rich-Result-Elemente. Hash und Prüfgrenzen stehen in [structured-data.md](structured-data.md).

## Nachweise und Grenzen

Build, Hashprüfung, Originalquellenabgleich, vierzehn Paket-/Website-/Schema-/MCP-Vertragstests und portabler Neubau ohne Quellenregistry prüfen die reproduzierbaren lokalen Artefakte. Seit Review 0.1.4 setzt der Generator im Codex-Kompatibilitätsmanifest `requires_local_executor: true` auf oberster Ebene, entsprechend der [OpenAI-Dokumentation](https://developers.openai.com/plugins/deploy/desktop-only). Claude erhält kein Codex-spezifisches Feld. Ein bestehender Paketvertrag prüft diese Host-Trennung. Skill-Inhalte und IDs sind unverändert. Exakte finale Hashes stehen in `dist/launch-report.json` und `site/downloads/SHA256SUMS`.

Der offizielle Skill-Validator prüft alle sieben Originalquellen. Beide finalen 0.1.4-ZIPs bestehen zusätzlich native Installation, Aktivierung, Discovery und Laden aller sieben Skills in neuen Codex-/Claude-Sitzungen. Alle 37 installierten Dateien je Host stimmen bytegenau mit dem jeweiligen ZIP überein; beide Namen sind zugeordnet und die Testfixtures unverändert. Die temporären Installationen wurden entfernt, die vorherige Codex-Konfiguration bytegleich wiederhergestellt und die bestehende Sidebar erhalten. Einzelheiten und genaue Grenzen stehen in [host-tests.md](host-tests.md). Eine sichtbare Desktop-Abnahme ist damit nicht bewiesen; die UI-Steuerung verweigert Zugriff auf Codex.

Der Abschluss-Skill wurde unter Claude mit Guide-only, Pause, autorisiertem lokalem Abschluss und beiden sichtbaren Namen geprüft; Codex erhielt einen isolierten Guide-/Pause-Test. Einzelheiten, Are-We-Cooking-Szenario und frühere Tests der übrigen fünf Skills stehen in [host-tests.md](host-tests.md). Das sind gezielte Szenarien, keine Garantie für jedes Modell oder jede Aufgabe. Der ergänzende kontrollierte Did-I-Leak-Test erkennt mit Gitleaks je einen künstlichen Wert im aktuellen Dateistand und in der gelöschten Git-Historie; Bericht und Ausgabe enthalten keinen Rohwert. TruffleHog ist weiterhin nicht verfügbar. Das ist keine Prüfung echter Credentials oder aller Detektoren.

In der lokalen Browser-Vorschau sind beide Namen und der Abschluss-Eintrag sichtbar. Keine vollständige WCAG-, Screenreader- oder physische Geräteabnahme behauptet. Die Sidebar bleibt ein separat zu prüfendes optionales lokales MCP-Paket.

## Vor öffentlichem Launch offen

1. Sichtbare Desktop-Installation und Hauptabläufe abnehmen: [lokale Abnahme-Anleitung](desktop-acceptance.md). Beide CLI-Installationen und alle sieben Lade-Tests bestehen. Die verfügbare UI-Steuerung darf Codex nicht bedienen; daher keine sichtbare Abnahme behauptet.
2. Zusätzliche TruffleHog-Abdeckung ergänzen. Der zuvor offene kontrollierte Erkennungsnachweis besteht jetzt für Gitleaks im aktuellen Dateistand und in der gelöschten Historie; dies ist eine begrenzte Qualitätsprüfung, keine pauschale Store-Pflicht.
3. Öffentliche Website-, Repository-, Support- und Hostingziele bestätigen; Anbieterkennzeichnung und passende Datenschutzerklärung ergänzen. Keine Platzhalter-URLs einsetzen. Erst für die ausdrücklich freigegebene Veröffentlichung echte öffentliche Metadaten und Indexierung setzen; `noindex,nofollow` bleibt vorerst erhalten.
4. Store-Zugänge und Einreichung vorbereiten: [OpenAI](https://developers.openai.com/plugins/deploy/submission) verlangt unter anderem verifizierten Publisher und erfolgreiche Skill-Scans; passende Organisationsrechte sind erforderlich. [Claude](https://claude.com/resources/articles/build-plugins-for-claude) beschreibt einen bezahlten Plan, ein auf GitHub gehostetes Plugin-Bündel sowie automatische Prüfung und menschliches Review. Kontoberechtigungen und Portalstatus wurden hier nicht geprüft. Die OpenAI-Partnerfreigabe für lokale MCP-Server betrifft die optionale Sidebar separat, nicht pauschal das Skills-only-Bündel.
5. Veröffentlichung, Upload, Store-Einreichung und Deployment erst nach direkter Freigabe. Keine Store-Annahme behauptet.

Private Vorher-Kopien der bearbeiteten Skill-Anleitungen, der konsolidierte frühere Entwurf und Host-Testevidenz bleiben ignoriert unter `.scratch/closing-update/` bis zur Review-Abnahme erhalten. Sie sind in keinem Paket enthalten. Temporäre Validator-Abhängigkeiten und agentenerzeugte Skill-Testkopien werden nach Prüfung entfernt; Originale und Prüfprotokolle bleiben erhalten.

English: All seven curated skills have their own local source Git repository, stable IDs, two visible names and MIT licenses. They are individually packaged and integrated into both Cookbook bundles and the local website. Targeted host scenarios and reproducible packaging checks are recorded separately; these are not a general security, legal or store approval. Public destinations, final desktop acceptance and explicit publication authorization remain open. Nothing was published.

Commit-Vorschlag: `fix: declare local Codex execution and verify plugin installs`
