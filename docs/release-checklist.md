# Release 0.6.0 / Veröffentlichung

14 Workflows, beide Namensvarianten und Host-Pakete; You Got This / You’re the Chef mit übernommener MIT-Lizenz. Der lokale Stand besteht 44 Tests, Quellen- und Paketprüfungen sowie den bytegleichen portablen Neubau. Die gerenderte Browserprüfung ist in [landing-page.md](landing-page.md) belegt.

Der Nutzer hat Commit, Push, Website-Deploy und das Update des installierten Kitchen-Plugins ausdrücklich beauftragt. Erfolgsnachweise sind der aktuelle Publish-/Check-Workflow zum konkreten Commit, die aktuelle Live-Seite und der bytegleiche installierte 0.6.0-Cache. Ein Build, ein Push oder eine alte Host-Abnahme ersetzt keinen dieser Nachweise. Der vorherige Plugin-Cache wird bis zur erfolgreichen Prüfung als lokale Rückfallkopie erhalten. Kein Tag, GitHub-Release oder Store-Upload beauftragt.

---

## Historischer Prüfstand 0.5.1

# Release 0.5.1 vorbereiten / Prepare release 0.5.1

## Inhalt / Contents

13 Workflows aus derselben Quelle in Plain und Kitchen. 13 eigene, geometrisch gezeichnete Küchenmotive, gebunden an stabile Quell-IDs statt Listenpositionen. Einheitliche Icons in Index, Rezeptkopf und Landingpage. Dunkel/Hell/System und reduzierte Bewegung bleiben erhalten. Favicon und Markenlogos bleiben gegenüber 0.5.0 bytegleich.

Die Zuordnung steht in `ui/recipe-icons.json`: Schneidebrett (Start), Kochtopf (Fortschritt), Rezeptkarte (Kontext), Vorratsglas (Sensible Inhalte), Sieb (Prüfung), Servierglocke (Freigabe), Menütafel (Änderungen), Schürze (Abschluss), angebrannte Pfanne (Retrospektive), Teekessel (Wiedereinstieg), Spritzbeutel (Prompt), Beschriftungsschild (Namen), offenes Kochbuch (Guide). Handgezeichnete Vektorgeometrie, keine zusätzliche Bibliothek oder Netzwerkanfrage.

## Technischer Release / Technical release

1. `python3 scripts/launch_check.py`: Pakete, Hashes, Quellen, Tests und bytegleicher portabler Neubau. Python 3.10/3.13 CI muss für den konkreten Commit grün sein.
2. `dist/launch-report.json` enthält die SHA-256-Werte der exakten Archive; `site/downloads/SHA256SUMS` die öffentlich angebotenen Installationsarchive. Nicht aus älteren Abnahmeberichten übernehmen.
3. Für einen GitHub-Release den geprüften Commit als `v0.5.1` markieren. Als Assets `site/downloads/cookbook-by-pengusto-kitchen-codex.zip`, `site/downloads/cookbook-by-pengusto-kitchen-claude.zip`, `dist/website.zip` und passende Prüfsummen verwenden. Native Marketplace-Installation braucht diesen GitHub-Release nicht; sie nutzt den generierten Branch `kitchen` bzw. `plain`.
4. Live-Seite, Datenschutz, Impressum und Downloads gegen denselben Build prüfen. Erst erfolgreicher Workflow und tatsächliche Live-Antwort belegen das Deployment.

Ein GitHub-Release/Tag wird nicht automatisch durch den Build erstellt. Die öffentliche Beta ist eine getrennte Veröffentlichung von einer Store-Einreichung.

## Store-Einreichung / Store submission

- **Upload-Datei:** `dist/store/kitchen/cookbook-by-pengusto.zip`. Enthält Skills direkt am Root; kein Marketplace-Wrapper, keine optionale MCP-Sidebar.
- Exakten ZIP-Inhalt und Hash prüfen. Einen Scan ohne Funde nur als begrenzten Nachweis, nie als Sicherheitsgarantie behandeln.
- Frische lokale Desktop-Sitzung: alle 13 Kitchen-Skills sichtbar; `$show-me-the-kitchen` empfiehlt korrekt einen Skill und bleibt bei der Erklärung; `$close-the-kitchen` mit reiner Guide-Anfrage löst keine externe Aktion aus. Die vom Nutzer bestätigte 12-Skill-Abnahme 0.4.0 ersetzt diese versionsbezogene Prüfung nicht.
- Tatsächlichen Publisher und Identitätsprüfung im Portal abschließen. Die zuvor beobachtete Verifizierung war offen; keine Identitätsnachweise in dieses Repository aufnehmen.
- Öffentliche Metadaten sind vorbereitet: Produktseite, GitHub-Issues als Support, DE/EN-Datenschutzerklärung. Danach Portal-Scans, Review und Freigabe für den konkreten Upload.
- **Keine Store-Einreichung durch CI.** Der Maintainer startet und bestätigt den konkreten Store-Release separat. Für die optionale lokale MCP-Sidebar gilt eine eigene Zulassung.

## Regression / Maintenance

Icons werden aus einer validierten gemeinsamen Quelle gerendert. Tests prüfen eindeutige Motive, beide Namensvarianten, identische Verwendung auf Landingpage und im Buch sowie das Zurückweisen aktiver SVG-Inhalte. Neue Rezepte ohne Icon lassen den Build fehlschlagen. Damit können zusätzliche Skills die Zuordnung nicht mehr durch verschobene Array-Indizes verfälschen.

English: The technical beta and exact archives are ready for a concrete release once their CI and live checks pass. Store release still needs current Desktop acceptance, verified publisher access, portal scans and review. Build and CI do not submit to the Store or create a release tag.

## Geprüfter lokaler Stand / Verified local build

2026-10-22: Build, Quellen- und Hashprüfung, 34 Unit-Tests und portabler Neubau bestanden. Kitchen-Store-ZIP: 13 Skills, 57 Dateien. SHA-256: `6a7f898d906c17096c049d4c31f267461682887d59afe3a8e0203e67c67bbcb6`. Gitleaks-Scan dieses exakten entpackten ZIPs mit redigierter Ausgabe: keine Funde. Entpackte Scan-Kopie nach Prüfung entfernt; Quellarchiv und Nachweis bleiben lokal erhalten. Browser-Sichtprobe bestätigt Schneidebrett und Pfannenmotiv, Namenswechsel und Kontrast in Hell/Dunkel. Die separate native Desktop- und Portal-Abnahme bleibt wie oben beschrieben offen.
