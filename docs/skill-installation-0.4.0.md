> **Abnahme 0.4.0 abgeschlossen (2026-10-22):** zwölf Skills nativ synthetisch geprüft; Nutzer bestätigt alle zwölf im Desktop-Picker und funktionierenden Abschluss-Guide. Exaktes Upload-ZIP erneut gescannt. Store-Zugang scheitert aktuell an der Identitätsprüfung; veröffentlichte vollständige Datenschutzerklärung fehlt. [Finaler Bericht](final-acceptance-0.4.0.md). Nichts hochgeladen oder veröffentlicht.

# Lokale Erweiterung und Installation 0.4.0

Stand 2026-10-22. **Lokal erstellt, installiert und mit frischen Codex-Sitzungen geprüft.** Kein Commit, Push, Website-Deployment, Store-Upload oder Veröffentlichung durch diese Arbeit.

## Direkte Codex-Aufrufe

Neue Codex-Sitzung starten und `$` mit Bindestrichen verwenden. `/back to the kitchen` ist kein gültiger Skill-Aufruf. Bei mehrdeutiger Auswahl den passenden Eintrag unter dem Cookbook-Plugin wählen.

| Funktion | Kitchen-Aufruf | Plain-Alternative im alternativen Paket |
|---|---|---|
| Wiederkehrende Fehler und liegen gebliebene Empfehlungen belegt untersuchen. | `$why-did-it-burn` | `$here-we-go-again` |
| Nach einer Pause Ziel, Entscheidungen und heutigen Projektstand auffrischen. | `$back-to-the-kitchen` | `$catch-me-up` |
| Einen begonnenen Prompt aus sichtbarem Kontext sinnvoll vervollständigen. | `$finish-my-order` | `$finish-my-prompt` |
| Passende Namen finden und Klartext/Kitchen-Paare gemeinsam vergleichen. | `$name-that-dish` | `$which-name-wins` |

## Implementierte Quellen

Vier neue Quellen in `skills/`: Retrospektive, Wiedereinstieg, Prompt-Ergänzung und portable Namenswahl. `catalog.json` enthält geprüfte Runtime-Allowlisten und SHA-256-Hashes. Bundle 0.4.0 wählt alle zwölf Quellen; Plain und Kitchen entstehen weiterhin aus denselben Bodies.

Der Naming-Workflow wurde aus der bestätigten privaten Anleitung als portable Fassung ohne persönliche Pfade oder Namenssammlung erstellt. Die ursprünglichen privaten Projekte bleiben unangetastet. Retrospektive und Wiedereinstieg sind getrennt: Die erste lernt aus Versuchen, der zweite aktualisiert Orientierung nach einer Pause. Prompt-Ergänzung erzeugt einen Vorschlag, keine native Autocomplete-Integration.

## Installationsnachweise

| Paket | Version | Aktiv | Dateien | Nachweis |
|---|---|---|---|
| Cookbook Kitchen | 0.4.0 | Ja | 54 | Installierter Cache und gebautes Paket bytegleich |
| Optionale Sidebar | 0.4.1 | Nein, vorherigen Zustand erhalten | 14 | Installierter Cache und gebautes Paket bytegleich |

Der native Add-Befehl aktiviert auch bereits deaktivierte Plugins. Bei der Sidebar wurde ausschließlich der vorab gesicherte deaktivierte Zustand wiederhergestellt. Geparste Codex-Konfiguration nach Abschluss identisch zum Ausgangszustand; andere Plugins unverändert.

## Prüfungen

- Frische Codex-Sitzung listet alle zwölf Kitchen-Skills. Die vier einzelnen `$`-Aufrufe laden nachweislich ihre jeweilige SKILL.md aus dem installierten 0.4.0-Cache.
- Alle vier synthetischen Verhaltensfälle bestanden; Ergebnisdateien manuell inhaltlich bewertet. Testfixture nach allen Sitzungen bytegleich.
- Vier neue Skill-Quellen bestehen den skill-creator-Validator.
- Build, check, check-sources, 30 Unit-Tests und portabler Neuaufbau bestanden; Artefakthashes des Neuaufbaus identisch.
- Sidebar: zwölf Rezepte, passende Aufrufe, vier Schritte und geladene eigene Motive im Browser geprüft; kein horizontaler Überlauf. Klartext-Anzeige verändert die installierte Kitchen-Invocation nicht. Der scrollbare Desktop-Index hält das ausgewählte Rezept sichtbar, statt zwölf Einträge auf leere Buchseitenhöhe zu strecken.
- Alle zwölf UI-Sprachen am Wiedereinstieg geprüft, Arabisch mit RTL. Hell, Dunkel und System-Umschaltung geprüft. Browserfehlerliste leer. Übersetzungen wurden nicht unabhängig muttersprachlich abgenommen.
- Website wird mit zwölf Karten pro Namens-/Sprachvariante, Einzelpaketen, Anleitungen und aktualisierten Hilfeseiten gebaut; lokale Link- und Fragmentprüfung bestanden.
- Native Desktop-Picker-/MCP-Einbettungsabnahme bleibt getrennt von der erfolgreichen nativen CLI-Erkennung. Die Desktop-Steuerung ist für Codex auf diesem Host gesperrt.

Die CLI meldete außerdem vorhandene Host-Warnungen zu ignoriertem `features.rmcp_client`, nicht auflösbaren Icons anderer Skill-Pakete und einem abgelehnten Remote-Katalog-Token. Diese wurden nicht als Cookbook-Fehler umgedeutet und keine fremden Einstellungen geändert. Die lokalen Aufrufe liefen trotz dieser Warnungen mit Exit 0.

## Seiten und visuelle Einordnung

Die zwölfsprachige Sidebar zeigt die bestätigten neuen Rezepte mit eigener Illustration und Akzentfarbe sowie dem gewählten Logo A. Die statische EN/DE-Website hat aktuelle Inhalte und funktionierende Downloads; ihre vollständige Umgestaltung im Kochbuchstil bleibt das zuvor vertagte Landingpage-TODO. Die optionale Sidebar wurde nicht gegen die vorherige Nutzereinstellung aktiviert.

## Aktualisierte Standalone-Aufrufe und Sicherung

Die bisherigen privaten Standalone-Verknüpfungen `which-name-wins` und `here-we-go-again` bleiben auf ausdrücklichen Nutzerwunsch aktiv. Nach der Klarstellung „will aktualisiert haben“ wurden beide Originalquellen aktualisiert: bestätigte Plain/Kitchen-Zuordnungen, aktuelle Unterscheidung zwischen Standalone-Aufruf und Cookbook-Variante sowie passende UI-Metadaten. Die persönlichen Namensregeln bleiben erhalten. Beide aktualisierten Originale bestehen den skill-creator-Validator; die bestehenden Symlinks zeigen nachweislich auf die aktualisierten Dateien. Keine offene Freigabe zur Entfernung mehr: Die alten Aufrufe werden behalten. Die früher abgelehnte Entfernung wurde nicht ausgeführt.

Vor der Installation wurden Konfiguration und vorherige Paket-Caches (~1,9 MiB) unter der ignorierten `.scratch/skills-0.4.0/before-install/` gesichert. Aufrufprotokolle, Antworten, Prüfberichte und Browser-Screenshot liegen im selben privaten Evidenzordner. Behalten bis die neuen Aufrufe in einer sichtbaren Desktop-Sitzung bestätigt sind und die optionale Altaufruf-Migration entschieden ist. Keine Geheimnisse oder personenbezogenen Testfälle wurden absichtlich als Fixture verwendet.

## Store-Grenzen

Das neue Kitchen-Upload-ZIP ist lokal vorbereitet, SHA-256 `e8fbfa1749cc055e1be9c7259f09dd5ba5ee0ae1eb9f47f77f02b4d422fc7e60`. Frühere 0.3.1-Secret-Scan- und Desktop-Nachweise gelten nicht automatisch für dieses Paket. Vor Einreichung: erneute Prüfung des exakten ZIPs, native Desktop-Abnahme, Publisher-Identitätsprüfung, veröffentlichte passende Datenschutzerklärung und ausdrücklicher Uploadauftrag. Nichts davon wird durch einen lokalen Build als erledigt behauptet.

## Festgehaltene Lehre

Ein bestätigter Name ist noch kein installierter Aufruf. Der neue Paketvertrag in `tests/test_cookbook.py` prüft deshalb, dass alle vier bestätigten Workflows tatsächlich ausgewählt, in beiden Varianten gerendert und mit passenden UI-Beispielaufrufen paketiert sind. UI- und Website-Prüfungen verwenden die Kataloglänge statt der früher hart codierten acht Rezepte.

Commit-Vorschlag: `feat: add four Kitchen workflows and update the twelve-recipe catalog`

Korrektur aus der Nutzerklärung: „alte Aufrufe behalten“ bedeutet hier vorhandene IDs und Links erhalten **und Inhalte aktualisieren**, nicht alte Inhalte einfrieren. Originalstände sind zusätzlich unter `.scratch/standalone-refresh-2026-10-22/before/` gesichert.
