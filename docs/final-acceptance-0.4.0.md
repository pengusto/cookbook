# Finale lokale Abnahme · Cookbook Kitchen 0.4.0

Prüfdatum: 2026-10-22. **Lokale/native Abnahme und nutzerbestätigte Desktop-Kurzabnahme bestanden; noch nicht einreichbar wegen konkreter Publisher-/Datenschutzvoraussetzungen.** Nichts hochgeladen, eingereicht oder veröffentlicht.

## Exaktes Artefakt

- Upload: `dist/store/kitchen/cookbook-by-pengusto.zip`.
- SHA-256: `e8fbfa1749cc055e1be9c7259f09dd5ba5ee0ae1eb9f47f77f02b4d422fc7e60`.
- Installierte Cookbook-Version 0.4.0, aktiviert; alle 54 Dateien bytegleich mit diesem ZIP.
- Zwölf Kitchen-Skills; `requires_local_executor: true`, keine Hooks oder MCP-Konfiguration im Store-Paket.
- Separate Sidebar 0.4.1 bleibt installiert und auf Nutzervorgabe deaktiviert. Die Kochbuchansicht ist nicht Teil des Skills-only-Uploads.
- Persönliche Standalone-Skills bleiben wie zuletzt ausdrücklich gewünscht erhalten und aktualisiert.

## Desktop-Evidenz sauber abgegrenzt

Die Desktop-Steuerung verweigert den Zugriff auf Codex mit „Computer Use is not allowed … for safety reasons“. Diese Sperre wurde nicht umgangen. Alternative verfügbare Plugin-Connectoren bieten keine native Picker-Abnahme. Eine CLI-Erkennung wird nicht als visuelle Prüfung bezeichnet.

Der Nutzer prüfte auf ausdrückliche Rückfrage eine frische lokale Codex-Sitzung und bestätigte: **„Alle zwölf sichtbar; Abschluss-Guide funktioniert“**. Prüfauftrag war der Picker einschließlich der vier neuen Kitchen-Skills und `$close-the-kitchen` mit einem reinen Abschluss-Guide, ohne Änderungen, Archivierung oder Veröffentlichung. Damit ist die sichtbare Kurzabnahme nutzerbestätigt; es gibt keine neue agentenseitig erstellte Codex-Screenshot-Evidenz und keinen behaupteten visuellen Volltest jedes einzelnen Workflows.

## Native synthetische Hauptabläufe

Eine frische ephemere Codex-Sitzung hat alle zwölf Anleitungen aus dem installierten Cache gelesen. Nur lesende Fixture-Prüfung, MCP-Werkzeuge für diesen Lauf deaktiviert, keine Delegation, externe Scans oder Veröffentlichungen durch die Testsession. Exit 0; Fixture bytegleich. Alle Antworten wurden auf die folgenden erwarteten Grenzen geprüft. Das ist begrenzte Szenarioabdeckung, keine allgemeine Verhaltensgarantie.

| Workflow | Beobachtetes Ergebnis |
|---|---|
| Prep the Kitchen | Brainstorm bleibt klein; keine Umsetzung oder Ticketpflicht. |
| Are We Cooking? | Regressionsnachweis zählt als Fortschritt; nicht angenommener Dashboard-Vorschlag bleibt außerhalb. |
| What Was I Cooking? | Fehlende frühe Historie bleibt vorläufig; kein Analytics-Auftrag erfunden. |
| Keep the Recipe Secret | Unlesbare Datei verhindert uneingeschränktes GO; keine erfundene Datei aus Zähler abgeleitet. |
| Can I Serve This? | Gemeldeter Fokusfehler bleibt unreproduziert; keine Rechtsfreigabe. |
| Ready to Serve | Private Prüfung löst keine pauschale Dokumentations- oder Veröffentlichungspflicht aus. |
| What’s New on the Menu? | Mehrdeutige Release-Linie wird geklärt; Regression als Fix, nicht als neue Funktion. |
| Close the Kitchen | Guide-only Abschluss ohne neue Aufträge, Push oder erneutes Testen ohne Grund. |
| Why Did It Burn? | Wiederholte Prüflücke als eine Ursache; akzeptierte Empfehlung nicht mit belegter Umsetzung verwechselt. |
| Back to the Kitchen | Alten Stand und neu berichteten Dokumentationsstand getrennt; keine Implementierung. |
| Finish My Order | Kopierbarer Prompt; keine Ausführung des Entwurfs. |
| Name That Dish | Genau drei Namenspaare mit beiden IDs; keine Auswahl aus einer Frage abgeleitet. |

Die vier neuen `$`-Aufrufe wurden zusätzlich bereits einzeln in frischen Sitzungen geprüft; Nachweise stehen im [Installationsbericht](skill-installation-0.4.0.md). Der bestehende Paketprüfstand mit 30 Tests und identischem portablem Neuaufbau bleibt gültig: Kein Runtime- oder Paketinhalt wurde während dieser abschließenden Prüfungen verändert.

## Erneuter Scan des exakten Uploads

Das geprüfte ZIP wurde in einen separaten privaten Prüfbereich entpackt. Gitleaks scannte den entpackten Inhalt redigiert: **Exit 0, keine Findings**, ungefähr 145 KB. Dieser Scan umfasst nur die eingereichten Dateien, nicht Git-Historie oder das gesamte Repository. Ein leerer Bericht beweist keine vollständige Sicherheit. Der SHA-256 oben bindet den Scan an das genaue Artefakt.

## Portal heute geprüft

Der In-App-Browser war nicht angemeldet; die vorhandene Chrome-Anmeldung bot einen autorisierten alternativen Zugang. In **Personal organization / Default project** wurde der Einstieg „Upload new or existing plugin“ nur bis zur Voraussetzung geöffnet. Ergebnis: **Complete identity verification** / „You need a verified developer identity before you can create or upload a plugin.“ Dialog abgebrochen; keine Identitätsdaten eingegeben, keine Datei ausgewählt, kein Draft angelegt. Andere Organisationen oder deren Berechtigungen wurden nicht geprüft.

## Was für den Store fehlt

| Priorität | Offener Punkt | Konkrete Abnahme |
|---|---|---|
| Erforderlich | Verifizierte Developer-/Business-Identität und Einreichungszugang | Portal lässt die passende bestätigte Publisher-Identität auswählen; heute im geprüften Kontext blockiert. |
| Erforderlich | Öffentliche vollständige Datenschutzerklärung | Den vorhandenen EN/DE-Entwurf mit Betreiber/Kontakt, Supportweg, Empfängern, Aufbewahrung, Hosting und Nutzerkontrollen vervollständigen und an bestätigter öffentlicher URL bereitstellen. Kein URL-Platzhalter und keine erfundene rechtliche Identität. |
| Vor erster Einreichung entscheiden | Skills-only oder einschließlich visueller lokaler Sidebar | Der aktuelle Store-Scope ist Skills-only. Wenn die Kochbuch-MCP-Oberfläche mitgeliefert werden soll, braucht sie einen eigenen geprüften Paket-/Zugangsweg; lokale MCP-Einreichungen sind partnerbeschränkt. Späteres Hinzufügen eines MCP-Servers zu einem bestehenden Skills-only-Plugin ist laut aktueller Submission-Dokumentation nicht unterstützt. |
| Nach gesondertem Auftrag | Exaktes ZIP hochladen und Portal-Findings beheben | Metadaten- und Skill-Scans tatsächlich durchlaufen, danach Review-Entscheidung abwarten. Keine automatisierte Store-Freigabe aus lokalen Tests ableiten. |
| Review-Kriterium | Vollständiges, stabiles Produkt mit erkennbarem Nutzen | Die Richtlinien akzeptieren keine Trial-/Demo-Plugins. Experimentelle Beta-Dokumentation und tatsächlichen Reifegrad ehrlich aufeinander abstimmen; kein bloßes Entfernen des Labels als Nachweis. |

Die Skills-only-Metadatenvalidierung fordert nicht pauschal alle vier MCP-Listing-URLs; MCP-Demoaufnahme und MCP-Testfälle sind für dieses Skills-only-Paket ebenfalls nicht nötig. Die allgemeine Pflicht zu einer veröffentlichten Datenschutzerklärung bleibt bestehen. Ein externer Produkt-/Supportkanal ist empfehlenswert und muss tatsächlich existieren, wenn er angegeben wird; eine vollständig neu gestaltete Landingpage ist keine pauschale Store-Pflicht.

## Aktuelle Primärquellen

Am 2026-10-22 erneut gelesen: [Submission und Metadaten](https://developers.openai.com/plugins/deploy/submission), [Plugin-Richtlinien](https://developers.openai.com/plugins/plugin-guidelines), [Desktop-only](https://developers.openai.com/plugins/deploy/desktop-only). Der Skills-only-Local-Executor-Flag bleibt korrekt gesetzt. Partner-Allowlisting nicht ungeprüft auf das reine Skills-Paket übertragen.

## Evidenz und Aufbewahrung

Private Belege unter `.scratch/final-acceptance-0.4.0/`: Paketinventar/Hash, installierte Plugin-Listings, native Toolereignisse/Antwort, Fixture, Gitleaks-Bericht und Portal-Screenshot. Der entpackte Prüfbereich wird bis zum Abschluss des exakten Release-Artefakts beibehalten; Originale und Rollback-Sicherungen bleiben erhalten. Keine privaten Protokolle oder Portal-Screenshots im Store-ZIP.

Lehre für die Abnahme: „sichtbar im Desktop“ ist von „nativ per CLI entdeckt“ und „synthetisches Verhalten geprüft“ getrennt. Diese Evidenzklassen stehen hier und im Installationsbericht ausdrücklich nebeneinander.

Commit-Vorschlag für diesen Dokumentationsstand: `docs: record twelve-skill desktop acceptance and remaining store gates`.
