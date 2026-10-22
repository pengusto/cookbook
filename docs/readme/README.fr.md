# Cookbook by Pengusto

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

Treize processus pour agents issus d’une source maintenue. Choisissez les **questions simples** ou les **noms de cuisine** et installez un seul style par environnement.

**Bêta publique expérimentale.** [pengusto/cookbook](https://github.com/pengusto/cookbook)

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

> **0.5.1 · 13 workflows.** Start with `$show-me-the-kitchen` (Kitchen) or `$explain-the-cookbook` (Plain). The visual Cookbook supports 12 languages and system/light/dark themes. Use `--ref plain` for Plain installation. The GitHub release is separate from the Store review. [Publication and installation](../../docs/publication.md).



## Construire et vérifier

Git et Python 3.10+ sont nécessaires, sans paquet Python supplémentaire. Installez Codex ou Claude Code et connectez-vous séparément. Exécutez les commandes à la racine du dépôt.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## Installer un style de noms

Choisissez plain ou kitchen. Les deux utilisent la même identité de plugin. Les exemples installent Kitchen. Démarrez ensuite une nouvelle session. La construction ne modifie aucune installation existante.

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

Avant de changer de style, sauvegardez le paquet installé, désinstallez uniquement le plugin Cookbook avec l’outil natif et retirez son inscription au marketplace, puis inscrivez l’autre style. Évitez les copies individuelles ou l’ancien paquet vibe-coding-cookbook en parallèle.

L’installation individuelle reste possible ; ce processus ne doit pas déjà exister dans la destination. L’exemple crée close-the-kitchen ; plain crée can-we-finish.

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 26 individual ZIPs + `SHA256SUMS`.

## Mettre à jour

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

Commitez ou sauvegardez vos changements avant la mise à jour. Reconstruire actualise les paquets locaux, pas le cache installé. Sauvegardez le paquet puis utilisez la désinstallation/réinstallation native. Consultez le guide Mac. [Mac setup](../../docs/mac-setup.md).

## Site web

Les pages DE/EN suivent le thème clair ou sombre du système. La langue et les noms sont indépendants ; les instructions des skills ne sont pas traduites. Lancez l’aperçu et ouvrez l’URL affichée. Le site bêta public est hébergé sur GitHub Pages ; la validation en boutique reste distincte.

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## Limites et état

Les paquets, empreintes, liens et reconstruction portable sont vérifiés automatiquement. Le chargement des skills a été testé localement ; l’acceptation visuelle complète et les boutiques restent ouvertes. Les skills de sécurité et de droit ne fournissent aucune garantie. L’historique conserve des pages de contact anciennes autorisées par le responsable. Les historiques Git originaux restent dans Cookbook ; les quatre anciens dépôts GitHub ont été supprimés avec autorisation. [Release review](../../docs/public-release-review.md).

## Contribuer et licences

Ouvrez une issue ou une pull request ciblée. Modifiez uniquement la source commune des skills et synchronisez les huit README. Code et skills originaux : MIT ; icônes tierces : mentions MIT/ISC. Illustrations générées par IA.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).
