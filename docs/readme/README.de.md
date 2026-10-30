# Cookbook by Pengusto

Projekt: **Cookbook by Pengusto** · GitHub-Repository: [`pengusto/cookbook`](https://github.com/pengusto/cookbook).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme/cookbook-banner-storybook-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="../../assets/readme/cookbook-banner-storybook-v3.png">
  <img alt="KI-Illustration: Der Cookbook-Pinguin kocht in einer Küche in Creme und Weinrot, die aus einem offenen Kochbuch wächst, neben Workflow-Rezeptkarten." src="../../assets/readme/cookbook-banner-storybook-v3.png">
</picture>

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

**Ein Rezept für den nächsten Schritt im Coding-Chat.**

Cookbook bietet Entwicklerinnen und Entwicklern mit Codex oder Claude Code 19 gezielte Workflows: Projekte planen, Fortschritt prüfen, nach einer Pause wieder einsteigen, vor dem Teilen prüfen und mit einer brauchbaren Übergabe abschließen. Wähle bei Bedarf ein Rezept; Host und Modell führen die Arbeit aus.

Wähle **einfache Fragen** oder **Koch-Namen**. Beide entstehen aus denselben gepflegten Anleitungen; installiere pro Host eine Namenswelt.

**Experimentelle öffentliche Beta · 0.7.2.** [Rezepte ansehen](https://pengusto.github.io/cookbook/cookbook.html) · [Plain](https://pengusto.github.io/cookbook/cookbook-plain.html)

## Schnellstart: eine Namenswelt wählen

Codex und/oder Claude Code zuerst installieren und anmelden. Die Beispiele installieren Kitchen; für Plain in Codex `--ref plain` verwenden. Beide Namenswelten teilen eine Plugin-Identität, deshalb nur eine gleichzeitig installieren. Der Paketbau verändert keine Host-Installation.

Codex — ohne lokalen Build:

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Nach der Installation eine neue Codex-Sitzung starten und ausprobieren:

```text
$show-me-the-kitchen Erkläre Cookbook und empfehle einen Workflow für den Wiedereinstieg nach einer langen Projektpause.
```

Der Guide erklärt und empfiehlt; er führt den empfohlenen Workflow nicht aus. Für Plain bei der Installation `--ref plain` und im Chat `$explain-the-cookbook` verwenden.

Claude Code — zuerst die untenstehenden Build- und Prüfbefehle ausführen:

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

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 38 individual ZIPs + `SHA256SUMS`.

## Bauen und prüfen

Zum Bauen brauchst du Git und Python 3.10+, keine zusätzlichen Python-Pakete. Codex und/oder Claude Code separat installieren und anmelden. Befehle im Stammordner ausführen.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## Die Rezeptkarte

| Plain | Kitchen |
|---|---|
| Explain the Cookbook | Show Me the Kitchen |
| Find Our Work | Find the Recipe |
| Where Does This Chat Belong? | Find the Kitchen |
| Catch Me Up | Back to the Kitchen |
| Where Were We? | What Was I Cooking? |
| How Do I Start? | Prep the Kitchen |
| Finish My Prompt | Finish My Order |
| Which Name Wins? | Name That Dish |
| You Got This | You’re the Chef |
| Am I Making Progress? | Are We Cooking? |
| Why Is It Broken? | Find the Bad Ingredient |
| Can We Simplify? | Trim the Recipe |
| Review My Changes | Taste Before Serving |
| Did I Leak? | Keep the Recipe Secret |
| Will They Sue Me? | Can I Serve This? |
| Am I Ready to Share? | Ready to Serve |
| What Did We Change? | What’s New on the Menu? |
| Can We Finish? | Close the Kitchen |
| Here We Go Again | Why Did It Burn? |

Weitere Modi: `$prep-the-kitchen explain <Ablauf>` erklärt vorhandenen Code; `$prep-the-kitchen choose <Entscheidung>` vergleicht passende Optionen; `$ready-to-serve verify-live <Ziel>` prüft die tatsächliche Auslieferung; `$close-the-kitchen handoff <Ziel>` bereitet eine gezielte Übergabe vor. Plain nutzt `$how-do-i-start`, `$am-i-ready-to-share` und `$can-we-finish` mit denselben Argumenten. Erklärung, Vergleich und Prüfung allein erlauben keine Änderungen; eine vorbereitete Übergabe ist kein vollzogener Transfer.

Nach Situation wählen: [Auswahlhilfe](../choosing-workflow.md). Für einen aktuellen Fehler nutze `$find-the-bad-ingredient` (Kitchen) oder `$why-is-it-broken` (Plain). Einen echten Nutzerablauf prüfst du mit `$youre-the-chef usertest <Ablauf>` oder `$you-got-this usertest <Ablauf>`; der Modus meldet Befunde ohne automatische Reparaturen und ist keine Studie mit Menschen.

Mit `$youre-the-chef <Ziel>` (Kitchen) oder `$you-got-this <Ziel>` (Plain) übernimmt der Agent die Umsetzung bis zum geprüften Ergebnis. `gauntlet` ergänzt eine endliche Kritikschleife; `audit` liefert Befunde ohne breite Umsetzung. Die Prompt-Vervollständigung erstellt dagegen nur einen Entwurf.

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

Paket-, Hash-, Linkprüfungen und portabler Neubau sind automatisiert. Der Maintainer bestätigte den Desktop-Picker mit zwölf Skills und den Abschlussguide für 0.4.0; für 0.5.0 wurde die neue Einführung separat in einem frischen nativen Codex-Aufruf getestet. Das sind datierte Prüfstände, keine vollständige visuelle Abnahme von 0.6.0 oder Store-Freigabe. Das visuelle Cookbook bietet 12 UI-Sprachen und System-/Hell-/Dunkel-Themes; die UI-Sprache übersetzt keine Workflow-Anleitungen. Die optionale lokale MCP-Seitenleiste ist ein separates Paket.

Sicherheits- und Rechtsprüfrezepte leiten Prüfungen an, bieten aber keine Garantien. Repository- und Website-Veröffentlichung sind von der Store-Einreichung getrennt. Importierte Git-Historien und Herkunft bleiben erhalten, einschließlich freigegebener früherer Kontaktseiten; die vier abgelösten GitHub-Repositories wurden mit Zustimmung des Maintainers entfernt. [0.5.0 acceptance](../../docs/acceptance-0.5.0.md) · [Release review](../../docs/public-release-review.md).

## Mitwirken und Lizenzen

Issues und gezielte Pull Requests sind willkommen. Nur die gemeinsame Skill-Quelle bearbeiten und alle acht READMEs gemeinsam pflegen. Eigener Code und Skills: MIT; Drittanbieter-Icons behalten MIT/ISC-Hinweise. Illustrationen sind KI-generiert.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).

Vorhandenes Cookbook-Logo: Cormorant-Garamond-Schriftkonturen unter SIL OFL. Rezeptillustrationen sind KI-generiert; sie belegen weder Screenshots noch Host-Abnahmen. [Asset-Herkunft und Lizenzen](../../THIRD_PARTY_NOTICES.md) · [Logo-Anleitung](../../assets/brand/GUIDE.md).

## Entwicklung unterstützen

Wenn dir Cookbook hilft, kannst du [meine Open-Source-Arbeit unterstützen](https://github.com/sponsors/pengusto).
