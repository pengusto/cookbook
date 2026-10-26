# Cookbook by Pengusto

Projet : **Cookbook by Pengusto** · Dépôt GitHub : [`pengusto/cookbook`](https://github.com/pengusto/cookbook).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme/cookbook-banner-storybook-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="../../assets/readme/cookbook-banner-storybook-v3.png">
  <img alt="Illustration générée par IA : le pingouin de Cookbook cuisine à côté de cartes de processus dans une cuisine crème et rouge bordeaux qui émerge d’un livre de recettes ouvert." src="../../assets/readme/cookbook-banner-storybook-v3.png">
</picture>

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

**Une recette pour la prochaine étape de votre conversation de code.**

Cookbook propose aux développeurs utilisant Codex ou Claude Code 18 processus ciblés : planifier un projet, vérifier les progrès, reprendre après une pause, vérifier avant de partager et préparer une transmission utile. Choisissez une recette au besoin ; votre environnement et votre modèle effectuent le travail.

Choisissez les **questions simples** ou les **noms de cuisine**. Les deux styles proviennent des mêmes instructions maintenues ; installez un seul style par environnement.

**Bêta publique expérimentale · 0.7.0.** [Parcourir les recettes](https://pengusto.github.io/cookbook/cookbook.html) · [Plain](https://pengusto.github.io/cookbook/cookbook-plain.html)

## Démarrage rapide : choisir un style

Installez Codex et/ou Claude Code et connectez-vous d’abord. Les exemples installent Kitchen ; pour Plain dans Codex, utilisez `--ref plain`. Les deux styles partagent une identité de plugin : installez-en un seul à la fois. La construction ne modifie aucune installation existante.

Codex — sans construction locale :

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Après installation, ouvrez une nouvelle session Codex et essayez :

```text
$show-me-the-kitchen Explique Cookbook et recommande un processus pour reprendre un projet après une longue pause.
```

Le guide explique et recommande ; il ne lance pas le processus recommandé. Pour Plain, utilisez `--ref plain` à l’installation et `$explain-the-cookbook` dans la conversation.

Claude Code — exécutez d’abord les commandes de construction et de vérification ci-dessous :

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

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 28 individual ZIPs + `SHA256SUMS`.

## Construire et vérifier

Git et Python 3.10+ sont nécessaires, sans paquet Python supplémentaire. Installez Codex ou Claude Code et connectez-vous séparément. Exécutez les commandes à la racine du dépôt.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## La carte des recettes

| Plain | Kitchen |
|---|---|
| Explain the Cookbook | Show Me the Kitchen |
| Find Our Work | Find the Recipe |
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

Autres modes : `$prep-the-kitchen explain <parcours>` explique le code ; `$prep-the-kitchen choose <décision>` compare les options ; `$ready-to-serve verify-live <cible>` vérifie la livraison ; `$close-the-kitchen handoff <destination>` prépare la transmission. Plain utilise `$how-do-i-start`, `$am-i-ready-to-share` et `$can-we-finish` avec les mêmes arguments. Ces demandes seules ne permettent pas de modifier ; une transmission préparée n’est pas un transfert effectué.

Choisir selon la situation : [guide](../choosing-workflow.md). Pour une panne actuelle : `$find-the-bad-ingredient` (Kitchen) ou `$why-is-it-broken` (Plain). Pour tester un parcours réel : `$youre-the-chef usertest <parcours>` ou `$you-got-this usertest <parcours>`. Le mode rapporte les résultats sans réparation automatique ; ce n’est pas une étude avec des participants humains.

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

Les paquets, empreintes, liens et reconstructions portables sont vérifiés automatiquement. Le responsable a confirmé le sélecteur Desktop à douze skills et le guide de clôture en 0.4.0 ; la nouvelle introduction a été testée séparément en 0.5.0 dans une nouvelle invocation native Codex. Ces vérifications datées ne prouvent ni l’acceptation visuelle complète de 0.6.0 ni l’approbation en boutique. Le Cookbook visuel propose 12 langues d’interface et des thèmes système/clair/sombre ; cela ne traduit pas les instructions des processus. La barre latérale MCP locale facultative est un paquet séparé.

Les recettes de sécurité et de droit guident les vérifications sans garantie. La publication du dépôt et du site est distincte de la soumission en boutique. Les historiques Git importés et leur attribution sont conservés, y compris les anciennes pages de contact approuvées ; les quatre dépôts GitHub remplacés ont été supprimés avec l’accord du responsable. [0.5.0 acceptance](../../docs/acceptance-0.5.0.md) · [Release review](../../docs/public-release-review.md).

## Contribuer et licences

Ouvrez une issue ou une pull request ciblée. Modifiez uniquement la source commune des skills et synchronisez les huit README. Code et skills originaux : MIT ; icônes tierces : mentions MIT/ISC. Illustrations générées par IA.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).

Logo Cookbook existant : contours Cormorant Garamond sous SIL OFL. Les illustrations des recettes sont générées par IA ; elles ne constituent ni captures d’écran ni validation dans un environnement. [Origine et licences des ressources](../../THIRD_PARTY_NOTICES.md) · [Guide du logo](../../assets/brand/GUIDE.md).
