# Cookbook by Pengusto

Sieben Workflows, eine gepflegte Quelle. Installiere **Plain** mit einfachen Fragen oder **Kitchen** mit Koch-Namen. Jede Installation zeigt genau eine Namenswelt. Die Namenstabelle und die gleichen Befehle stehen in der [englischen Haupt-README](../../README.md).

## Auf einem anderen Mac und später aktualisieren

Privates Repo: [pengusto/cookbook](https://github.com/pengusto/cookbook). Die [Mac-Anleitung](../mac-setup.md) beschreibt Klonen, Bauen, Variantenwahl und Cache-Aktualisierung. Zugangsdaten und persönliche Host-Einstellungen werden nicht mitkopiert.

## Lokal bauen und prüfen

```sh
python3 scripts/cookbook.py build
python3 scripts/cookbook.py check
python3 scripts/cookbook.py check-sources
python3 -m unittest discover -s tests
python3 scripts/launch_check.py
```

Python 3.10+, Standardbibliothek. Nur `skills/<stabile-id>/` bearbeiten; Namen und Aufruf-IDs kommen aus catalog.json. Die beiden Varianten werden generiert. Die Vorlagen nicht direkt in einen Host kopieren. Externe Originalrepos und sources.local.json werden nicht mehr für den Build verwendet.

## Eine Variante installieren

Codex, beispielsweise Plain:

```sh
codex plugin marketplace add ./dist/plain/codex
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Claude Code mit der vorhandenen Laufzeit:

```sh
claude plugin marketplace add ./dist/plain/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

Für Koch-Namen `plain` im Pfad durch `kitchen` ersetzen. Beide haben dieselbe Plugin-Identität. Für einen Wechsel das vorhandene Paket sichern, das Plugin nativ deinstallieren, nur dessen Marketplace abmelden und die andere Variante anmelden/installieren. Nicht zusätzlich zum alten vibe-coding-cookbook oder Einzelkopien installieren. Der Build verändert keine Host-Installation.

Einzelinstallation: `python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /leeres/lokales/ziel` erzeugt close-the-kitchen, Plain dagegen can-we-finish. Vorhandene Varianten desselben Workflows werden nicht überschrieben. site/downloads enthält vier Plugin-ZIPs mit vollständigem lokalem Marketplace und vierzehn Einzel-ZIPs. Optionale Sidebar-Pakete unter dist/plain/sidebar und dist/kitchen/sidebar enthalten keine Skills.

## Vorschau, Historie und Grenzen

`python3 scripts/cookbook.py serve --port 8767`: gedruckte lokale URL öffnen. index.html zeigt Plain, kitchen.html Kitchen. Die englischen Seiten heißen index-en.html und kitchen-en.html. Sprachwechsel erhalten die Namenswelt und umgekehrt. Jeweils nur passende Namen, Downloads und strukturierte Daten. Die Website-Sprache übersetzt nicht automatisch Skill-Anleitungen. Die neue weiße/grüne Landingpage lädt Styles und KI-generiertes Kochbuchmotiv lokal. Kein öffentliches Ziel erfunden; noindex bleibt.

Alle sieben bisherigen Git-Historien sind über history/* und als Vorfahren von main vollständig erhalten. Alte Originalrepos und frühere generierte Ausgaben bleiben bestehen, sind aber keine weiter gepflegten Quellen. [Zusammenführung und Nachweise](../consolidation.md), [Pflege](../maintenance.md).

Review 0.2.0 wird lokal geprüft und auf ausdrücklichen Wunsch privat auf GitHub zwischen eigenen Macs verfügbar gemacht. Pakettests sind keine umfassenden Host-, Sicherheits- oder Rechtsprüfungen. Frühere 0.1.x-Berichte sind historisch. Sichtbare Desktop-Abnahme, öffentliche Ziele, Rechtsseiten, zusätzliche Scannerabdeckung und Store-Voraussetzungen bleiben offen. Keine Originale gelöscht, keine öffentliche Veröffentlichung und keine Deployments. Der private GitHub-Abgleich ist separat autorisiert. MIT und vorhandene Skill-Lizenzen bleiben erhalten; private Historie ist nicht automatisch zur Veröffentlichung freigegeben.
