# Vibe Coding Cookbook

[English](../../README.md) · [Deutsch](README.de.md)

**Private Review-Edition · Python 3.10+ · MIT (Cookbook)**

Kuratierte eigene Agent-Skills von Pengusto. Wähle nach Einsatzmoment, lies Rezept und Grenzen und installiere nur den passenden Skill. Sieben Rezepte, sieben geprüfte installierbare Snapshots. Gute Namen bleiben; die Anleitungen bleiben praktisch.

## Lokal ansehen

Im Repository-Ordner ausführen:

```sh
python3 scripts/cookbook.py build
python3 scripts/cookbook.py check
python3 -m unittest discover -s tests
python3 scripts/cookbook.py serve
```

Bei laufendem Server [die lokale Vorschau](http://127.0.0.1:8766/site/) öffnen. Nach dem Build lässt sich auch `site/index.html` direkt öffnen. Kein App-Framework, Paketinstallation, Konto oder Deployment nötig.

## Ein Rezept auswählen

| Name | Koch-Titel | ID |
|---|---|---|
| Start It Right | Prep the Kitchen | `start-it-right` |
| Check Progress | Are We Cooking? | `are-we-cooking` |
| Did I Leak? | Keep the Recipe Secret | `did-i-leak` |
| Will They Sue Me? | Can I Serve This? | `will-they-sue-me` |
| Let Them See It | Ready to Serve | `let-them-see-it` |
| What Did We Change | What’s New on the Menu? | `what-did-we-change` |
| Finish This Chat | Close the Kitchen | `kill-the-todos` |

[Inventar und Nutzerreise](../inventory.md) begründen Auswahl und Ausschlüsse. Jedes Rezept beschreibt Einsatzmoment, Zutaten, Zubereitung, Verifikation, Ergebnis und Grenzen. Die Rezepttexte sind in dieser Edition deutsch, die originalen Skill-Anleitungen englisch. Beide README-Versionen decken denselben Installations- und Wartungsablauf ab.

## Einen Snapshot installieren

Zunächst in einem leeren, isolierten Ziel testen:

```sh
python3 scripts/cookbook.py install let-them-see-it --dest .scratch/review-skills
```

Für eine bewusst gewählte Codex-Installation `--dest ~/.codex/skills` verwenden. Das ist ein vorgeschlagener Nutzerschritt, keine während der Vorbereitung ausgeführte Installation. Vorhandene Ordner und Symlinks werden abgelehnt; verwaltete Installationen bleiben erhalten. Den Host bei Bedarf neu laden und prüfen, ob er den Skill erkennt. Gezielte Host-Tests und ihre Grenzen sind in docs/host-tests.md dokumentiert.

Alternativ das gewählte `site/downloads/<id>.zip` in ein leeres Skill-Ziel entpacken. Jedes ZIP enthält genau einen Skill-Ordner mit `SKILL.md`, Original-LICENSE und ausdrücklich ausgewählten Laufzeitdateien. SHA-256 mit `site/downloads/SHA256SUMS` vergleichen. Nicht das Repository als einen Skill installieren. Der Build ist deterministisch und braucht kein Netzwerk; Did I Leak verwendet Git/Python und meldet bei Nutzung die verfügbaren optionalen Scanner.

## Das Bündel lokal installieren

Derselbe Build erzeugt Codex- und Claude-Code-Plugin-ZIPs unter `site/downloads/` sowie lokale Review-Strukturen und Marketplaces unter `dist/codex/` und `dist/claude/`. `bundle.json` wählt die sieben geprüften Skills ausdrücklich aus; Einzel-Downloads bleiben verfügbar. Beide Plugin-Pakete erhalten identische Skill-Bytes und Original-Lizenzvermerke; `SOURCES.json` dokumentiert die Herkunft.

Siehe [lokale Plugin-Einrichtung und Website-Anbindung](../plugins.md). Review 0.1.4 enthält alle sieben Skills, Listing-Metadaten und Icons. Native Installation und Laden aller sieben Skills in beiden Hosts, Pakettests und portabler Neubau werden lokal geprüft. Das Codex-Manifest kennzeichnet die lokale Ausführung. Die sichtbare Desktop-Abnahme bleibt getrennt. Der Abschluss-Skill hat gezielte Codex- und Claude-Verhaltenstests, einschließlich beider sichtbarer Namen in Claude. [host-tests.md](../host-tests.md) dokumentiert tatsächliche Abdeckung, frühere Tests der anderen Skills und verbleibende Scannergrenzen. Nichts wurde veröffentlicht.

Einzelne Skill-Websites können später auf ihr Rezept, den Einzel-Download und die gemeinsamen Bündel verweisen. Diese Websites und bestehenden Repositories wurden nicht geändert.

## Quellen und Aktualisierung

Originalprojekte bleiben die einzigen gepflegten Skill-Quellen. `catalog.json` dokumentiert Rezept, Quellrevision soweit vorhanden und SHA-256 jeder kopierten Datei. `skills/` enthält ausschließlich Review-Snapshots. ZIPs und Vorschau sind generierte, ignorierte Ausgabe. Beim Build werden keine Quellskripte ausgeführt.

Die vorhandene skill-library bleibt der breite lokale Katalog. Dieses Repository ergänzt eine geprüfte Distributionsauswahl statt einer weiteren globalen Registrierung. Die ignorierte `sources.local.json` ordnet IDs lokalen Originalen zu. Portable Builds brauchen sie nicht; nur `python3 scripts/cookbook.py check-sources` benötigt sie.

[Aktualisierungsablauf](../maintenance.md): Änderungen im Original reviewen, Laufzeit-Auswahl prüfen, freigegebene Dateien kopieren, Hashes/Revision aktualisieren und neu bauen. Kein automatisches Sync und kein stiller Installationsaustausch. Eine Git-Revision liefert Kontext; Dateihashes belegen exakte Snapshot-Bytes auch bei uncommitteten oder nicht versionierten Quellen.

## Rechte und Prüfstand

[MIT](../../LICENSE) gilt auf ausdrückliche Entscheidung für neue Cookbook-Texte und Werkzeuge. Jeder ausgelieferte Skill behält seinen eigenen originalen MIT-Vermerk. Are We Cooking? hat keine Quell-LICENSE und wird weder kopiert noch paketiert. Persönliche Integrationen, Adressen, Account-Einstellungen, Landingpage-Assets und fremde Quellhistorie sind ausgeschlossen.

**Für privaten Review bereit, mit benannten Grenzen.** Lokale Checks beweisen weder rechtliche Freigabe, umfassende Sicherheit, Host-Kompatibilität noch Agent-Verhalten. Siehe [Übergabe](../handoff.md), [Evaluation](../evaluation.md) und [Verhaltensszenarien](../behavior-review.md). Kein Cookbook-Remote, Push, Release, Deployment oder Sichtbarkeitswechsel gehört zu dieser Vorbereitung.

## Finaler lokaler Launch-Check

`python3 scripts/launch_check.py` prüft Pakete, verfügbare Originalquellen und einen portablen Neubau. `dist/website.zip` enthält die eigenständige statische Website; `dist/launch-report.json` dokumentiert Artefakthashes und offene Schritte. Siehe [Launch-Prüfstand](../launch-readiness.md). Der Check lädt nichts hoch.

Alle sieben Cookbook-Einträge haben zwei sichtbare Namen und eigene lokale Quell-Repos; IDs bleiben stabil. [Namen und Quell-Repositories](../skill-naming.md). Der Abschluss-Skill ist als `$kill-the-todos` einzeln und in beiden Bündeln enthalten.
