# Cookbook by Pengusto

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

Oito fluxos de trabalho para agentes em uma fonte mantida. Escolha **perguntas simples** ou **nomes de cozinha** e instale apenas um estilo por ambiente.

**Beta pública experimental.** [pengusto/cookbook](https://github.com/pengusto/cookbook)

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

> 0.3.0: Where Were We? / What Was I Cooking? is included in both naming variants under MIT. Package checks cover all eight skills; native host-loading and behavioral acceptance of the new skill remain open.

## Gerar e verificar

É necessário Git e Python 3.10+, sem pacotes Python adicionais. Instale e entre no Codex ou Claude Code separadamente. Execute os comandos na raiz do repositório.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## Instalar um estilo de nomes

Escolha plain ou kitchen. Ambos usam a mesma identidade de plugin. Os exemplos instalam Kitchen. Depois, inicie uma nova sessão. A geração não altera instalações existentes.

Codex:

```sh
codex plugin marketplace add ./dist/kitchen/codex
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Claude Code:

```sh
claude plugin marketplace add ./dist/kitchen/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

Antes de trocar o estilo, faça backup do pacote instalado, desinstale apenas o plugin Cookbook pela ferramenta nativa e remova seu registro de marketplace; depois registre o outro estilo. Evite cópias individuais ou o antigo pacote vibe-coding-cookbook em paralelo.

Também é possível instalar um skill individual; ele não deve existir no destino. O exemplo cria close-the-kitchen; plain cria can-we-finish.

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 16 individual ZIPs + `SHA256SUMS`.

## Atualizar

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

Faça commit ou backup das alterações antes de atualizar. Gerar novamente atualiza os pacotes locais, não o cache instalado. Faça backup e use a desinstalação/reinstalação nativa para renová-lo. Veja o guia do Mac. [Mac setup](../../docs/mac-setup.md).

## Site

As páginas DE/EN seguem o tema claro ou escuro do sistema. Idioma e nomes mudam de forma independente; as instruções dos skills não são traduzidas. Inicie a prévia e abra a URL indicada. Esta Beta não inclui site público publicado nem lojas.

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## Limitações e estado

Pacotes, hashes, links e geração portátil são verificados automaticamente. O carregamento dos skills foi testado localmente; a aceitação visual completa e as lojas continuam pendentes. Skills de segurança e revisão jurídica não oferecem garantias. O histórico contém páginas antigas de contato autorizadas pelo mantenedor. Os históricos Git originais continuam no Cookbook; os quatro repositórios antigos do GitHub foram removidos com autorização. [Release review](../../docs/public-release-review.md).

## Contribuições e licenças

Abra uma issue ou pull request focada. Edite apenas a fonte comum dos skills e mantenha os oito README alinhados. Código e skills originais: MIT; ícones de terceiros: avisos MIT/ISC. As ilustrações foram geradas por IA.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).
