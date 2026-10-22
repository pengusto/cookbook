# Cookbook by Pengusto

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

Dreizehn Agent-Workflows aus einer gepflegten Quelle. Wähle **einfache Fragen** oder **Koch-Namen** und installiere pro Host genau eine Namenswelt.

**Experimentelle öffentliche Beta.** [pengusto/cookbook](https://github.com/pengusto/cookbook)

| Plain | Kitchen |
|---|---|
| How Do I Start? | Prep the Kitchen |
| Am I Making Progress? | Are We Cooking? |
| Where Were We? | What Was I Cooking? |
| Did I Leak? | Keep the Recipe Secret |
| Will They Sue Me? | Can I Serve This? |
| Am I Ready to Share? | Ready to Serve |
| What Did We Change? | What’s New on the Menu? |
| Can We Finish? | Close the Kitchen |
| Here We Go Again | Why Did It Burn? |
| Catch Me Up | Back to the Kitchen |
| Finish My Prompt | Finish My Order |
| Which Name Wins? | Name That Dish |
| Explain the Cookbook | Show Me the Kitchen |

> **0.5.0 · 13 workflows.** Start with `$show-me-the-kitchen` (Kitchen) or `$explain-the-cookbook` (Plain). The visual Cookbook supports 12 languages and system/light/dark themes. Use `--ref plain` for Plain installation. The GitHub release is separate from the Store review. [Publication and installation](../../docs/publication.md).



## Bauen und prüfen

Zum Bauen brauchst du Git und Python 3.10+, keine zusätzlichen Python-Pakete. Codex und/oder Claude Code separat installieren und anmelden. Befehle im Stammordner ausführen.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## Eine Namenswelt installieren

Wähle plain oder kitchen. Beide verwenden dieselbe Plugin-Identität. Die Beispiele installieren Kitchen. Danach eine neue Host-Sitzung starten. Der Build verändert keine Host-Installation.

Codex:

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Claude Code:

```sh
claude plugin marketplace add ./dist/kitchen/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

Vor einem Variantenwechsel das installierte Paket sichern, nur das Cookbook-Plugin nativ deinstallieren und dessen Marketplace abmelden; anschließend die andere Variante registrieren. Unbeabsichtigte Doppelinstallationen vermeiden. Bestehende eigenständige Aufrufe werden nicht automatisch entfernt.

Einzelinstallation bleibt möglich; dieser Workflow darf im Ziel noch nicht vorhanden sein. Das Beispiel erzeugt close-the-kitchen; plain erzeugt can-we-finish.

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 26 individual ZIPs + `SHA256SUMS`.

## Aktualisieren

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

Eigene Änderungen vor dem Pull committen oder separat sichern. Ein Neubau aktualisiert Pakete, keinen installierten Plugin-Cache. Installiertes Paket sichern und nativ deinstallieren/neu installieren. Details in der Mac-Anleitung. [Mac setup](../../docs/mac-setup.md).

## Website

Die DE/EN-Landingpages folgen dem hellen/dunklen Systemdesign. Sprache und Namenswelt sind unabhängig; die Skill-Anleitungen werden dadurch nicht übersetzt. Lokale Vorschau starten und die ausgegebene URL öffnen. Die Website wird auf GitHub Pages veröffentlicht; die Store-Einreichung bleibt separat.

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## Grenzen und Prüfstand

Paket-, Hash-, Linkprüfungen und portabler Neubau sind automatisiert. Skill-Laden wurde lokal getestet; vollständige sichtbare Desktop-Abnahme und Store-Freigaben bleiben offen. Sicherheits- und Rechtsprüfskills bieten Orientierung, keine Garantien. Die erhaltenen Historien enthalten ausdrücklich freigegebene frühere Kontaktseiten. Die ursprünglichen Git-Historien bleiben im Cookbook erhalten; die vier alten GitHub-Repos wurden auf Nutzerwunsch gelöscht. [Release review](../../docs/public-release-review.md).

## Mitwirken und Lizenzen

Issues und gezielte Pull Requests sind willkommen. Nur die gemeinsame Skill-Quelle bearbeiten und alle acht READMEs gemeinsam pflegen. Eigener Code und Skills: MIT; Drittanbieter-Icons behalten MIT/ISC-Hinweise. Illustrationen sind KI-generiert.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).
