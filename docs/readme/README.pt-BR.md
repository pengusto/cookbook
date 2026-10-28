# Cookbook by Pengusto

Projeto: **Cookbook by Pengusto** · Repositório no GitHub: [`pengusto/cookbook`](https://github.com/pengusto/cookbook).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme/cookbook-banner-storybook-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="../../assets/readme/cookbook-banner-storybook-v3.png">
  <img alt="Ilustração gerada por IA: o pinguim de Cookbook cozinha ao lado de cartões de fluxo de trabalho em uma cozinha creme e vinho que surge de um livro de receitas aberto." src="../../assets/readme/cookbook-banner-storybook-v3.png">
</picture>

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

**Uma receita para o próximo passo na sua conversa de código.**

Cookbook oferece a quem desenvolve com Codex ou Claude Code 18 fluxos focados: planejar um projeto, verificar o progresso, retomar o contexto após uma pausa, revisar antes de compartilhar e encerrar com uma passagem de trabalho útil. Escolha uma receita quando precisar; seu ambiente e modelo executam o trabalho.

Escolha **perguntas simples** ou **nomes de cozinha**. Ambos vêm das mesmas instruções mantidas; instale um estilo por ambiente.

**Beta pública experimental · 0.7.0.** [Explorar as receitas](https://pengusto.github.io/cookbook/cookbook.html) · [Plain](https://pengusto.github.io/cookbook/cookbook-plain.html)

## Início rápido: escolha um estilo

Primeiro instale Codex e/ou Claude Code e entre na sua conta. Os exemplos instalam Kitchen; para Plain no Codex, use `--ref plain`. Ambos compartilham uma identidade de plugin: instale um de cada vez. Compilar pacotes não altera instalações existentes.

Codex — sem compilação local:

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Após instalar, abra uma nova sessão do Codex e experimente:

```text
$show-me-the-kitchen Explique Cookbook e recomende um fluxo para retomar um projeto após uma longa pausa.
```

O guia explica e recomenda; não executa o fluxo recomendado. Para Plain, use `--ref plain` na instalação e `$explain-the-cookbook` na conversa.

Claude Code — execute primeiro os comandos de compilação e verificação abaixo:

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

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 28 individual ZIPs + `SHA256SUMS`.

## Gerar e verificar

É necessário Git e Python 3.10+, sem pacotes Python adicionais. Instale e entre no Codex ou Claude Code separadamente. Execute os comandos na raiz do repositório.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## O menu de receitas

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

Outros modos: `$prep-the-kitchen explain <fluxo>` explica o código; `$prep-the-kitchen choose <decisão>` compara opções; `$ready-to-serve verify-live <alvo>` verifica a entrega; `$close-the-kitchen handoff <destino>` prepara a passagem. Plain usa `$how-do-i-start`, `$am-i-ready-to-share` e `$can-we-finish` com os mesmos argumentos. Esses pedidos sozinhos não autorizam alterações; preparar uma passagem não conclui a transferência.

Escolha pela situação: [guia](../choosing-workflow.md). Para uma falha atual: `$find-the-bad-ingredient` (Kitchen) ou `$why-is-it-broken` (Plain). Para testar um fluxo real: `$youre-the-chef usertest <fluxo>` ou `$you-got-this usertest <fluxo>`. O modo relata resultados sem reparos automáticos; não é uma pesquisa com participantes humanos.

## Atualizar

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

Faça commit ou backup das alterações antes de atualizar. Gerar novamente atualiza os pacotes locais, não o cache instalado. Faça backup e use a desinstalação/reinstalação nativa para renová-lo. Veja o guia do Mac. [Mac setup](../../docs/mac-setup.md).

## Site

As páginas DE/EN seguem o tema claro ou escuro do sistema. Idioma e nomes mudam de forma independente; as instruções dos skills não são traduzidas. Inicie a prévia e abra a URL indicada. O site Beta público é hospedado no GitHub Pages; a revisão nas lojas é separada.

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## Limitações e estado

As verificações de pacotes, hashes, links e reconstrução portátil são automatizadas. O mantenedor confirmou o seletor Desktop com doze skills e o guia de encerramento em 0.4.0; a nova introdução foi testada separadamente em 0.5.0 numa nova invocação nativa do Codex. São verificações datadas, não aceitação visual completa da 0.6.0 nem aprovação na loja. O Cookbook visual oferece 12 idiomas de interface e temas do sistema/claro/escuro; isso não traduz as instruções dos fluxos. A barra lateral MCP local opcional é um pacote separado.

As receitas de segurança e revisão jurídica orientam verificações sem garantias. Publicar o repositório e o site é separado de enviar à loja. Os históricos Git importados e sua atribuição são preservados, incluindo páginas de contato históricas aprovadas; os quatro repositórios GitHub substituídos foram removidos com autorização do mantenedor. [0.5.0 acceptance](../../docs/acceptance-0.5.0.md) · [Release review](../../docs/public-release-review.md).

## Contribuições e licenças

Abra uma issue ou pull request focada. Edite apenas a fonte comum dos skills e mantenha os oito README alinhados. Código e skills originais: MIT; ícones de terceiros: avisos MIT/ISC. As ilustrações foram geradas por IA.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).

Logo Cookbook existente: contornos Cormorant Garamond sob SIL OFL. Ilustrações das receitas são geradas por IA; não são capturas nem comprovam aceitação no ambiente. [Origem e licenças dos recursos](../../THIRD_PARTY_NOTICES.md) · [Guia do logo](../../assets/brand/GUIDE.md).

## Apoie o desenvolvimento

Se o Cookbook é útil para você, pode [apoiar meu trabalho de código aberto](https://github.com/sponsors/pengusto).
