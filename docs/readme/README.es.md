# Cookbook by Pengusto

Proyecto: **Cookbook by Pengusto** · Repositorio de GitHub: [`pengusto/cookbook`](https://github.com/pengusto/cookbook).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/readme/cookbook-banner-storybook-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="../../assets/readme/cookbook-banner-storybook-v3.png">
  <img alt="Ilustración generada por IA: el pingüino de Cookbook cocina junto a tarjetas de flujo de trabajo en una cocina de color crema y rojo vino que surge de un recetario abierto." src="../../assets/readme/cookbook-banner-storybook-v3.png">
</picture>

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

**Una receta para el siguiente paso de tu conversación de código.**

Cookbook ofrece a quienes desarrollan con Codex o Claude Code 19 flujos concretos: planificar un proyecto, comprobar el progreso, retomar el contexto tras una pausa, revisar antes de compartir y cerrar con un traspaso útil. Elige una receta cuando la necesites; tu entorno y modelo realizan el trabajo.

Elige **preguntas sencillas** o **nombres de cocina**. Ambos estilos se generan desde las mismas instrucciones mantenidas; instala un estilo por entorno.

**Beta pública experimental · 0.7.2.** [Explorar las recetas](https://pengusto.github.io/cookbook/cookbook.html) · [Plain](https://pengusto.github.io/cookbook/cookbook-plain.html)

## Inicio rápido: elige un estilo

Primero instala Codex y/o Claude Code e inicia sesión. Los ejemplos instalan Kitchen; para Plain en Codex usa `--ref plain`. Ambos estilos comparten una identidad de plugin: instala uno a la vez. Compilar paquetes no cambia las instalaciones existentes.

Codex — sin compilación local:

```sh
codex plugin marketplace add pengusto/cookbook --ref kitchen
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Tras instalar, abre una sesión nueva de Codex y prueba:

```text
$show-me-the-kitchen Explica Cookbook y recomienda un flujo para retomar un proyecto tras una pausa larga.
```

La guía explica y recomienda; no ejecuta el flujo recomendado. Para Plain, usa `--ref plain` al instalar y `$explain-the-cookbook` en la conversación.

Claude Code — ejecuta primero los comandos de compilación y verificación que aparecen abajo:

```sh
claude plugin marketplace add ./dist/kitchen/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

Antes de cambiar de estilo, guarda una copia del paquete instalado, desinstala únicamente el plugin Cookbook con la herramienta nativa y elimina su registro de marketplace; registra el otro estilo. Evita copias individuales o el antiguo paquete vibe-coding-cookbook en paralelo.

También hay instalación individual; el flujo no debe existir en el destino. El ejemplo crea close-the-kitchen; plain crea can-we-finish.

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 38 individual ZIPs + `SHA256SUMS`.

## Compilar y verificar

Se requieren Git y Python 3.10+; no hacen falta paquetes Python. Instala Codex o Claude Code e inicia sesión por separado. Ejecuta los comandos desde la raíz del repositorio.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## La carta de recetas

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

Otros modos: `$prep-the-kitchen explain <flujo>` explica el código; `$prep-the-kitchen choose <decisión>` compara opciones; `$ready-to-serve verify-live <destino>` verifica la entrega; `$close-the-kitchen handoff <destino>` prepara el relevo. Plain usa `$how-do-i-start`, `$am-i-ready-to-share` y `$can-we-finish` con los mismos argumentos. Estas solicitudes solas no autorizan cambios; preparar un relevo no completa una transferencia.

Elige según la situación: [guía](../choosing-workflow.md). Para un fallo actual: `$find-the-bad-ingredient` (Kitchen) o `$why-is-it-broken` (Plain). Para probar un recorrido real: `$youre-the-chef usertest <recorrido>` o `$you-got-this usertest <recorrido>`. Informa de hallazgos sin reparaciones automáticas; no es un estudio con participantes humanos.

## Actualizar

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

Confirma o guarda tus cambios antes de actualizar. Compilar actualiza los paquetes locales, no la caché instalada. Guarda el paquete y utiliza la desinstalación/reinstalación nativa para renovarlo. Consulta la guía de Mac. [Mac setup](../../docs/mac-setup.md).

## Sitio web

Las páginas DE/EN siguen el tema claro u oscuro del sistema. Idioma y nombres se cambian por separado; las instrucciones de los skills no se traducen. Inicia la vista previa y abre la URL indicada. El sitio Beta público se aloja en GitHub Pages; la revisión de tiendas es independiente.

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## Límites y estado

Las comprobaciones de paquetes, hashes, enlaces y compilación portátil están automatizadas. El responsable confirmó el selector Desktop con doce skills y la guía de cierre en 0.4.0; la nueva introducción se probó por separado en 0.5.0 con una invocación nativa nueva de Codex. Son pruebas fechadas, no una aceptación visual completa de 0.6.0 ni aprobación en tienda. El Cookbook visual ofrece 12 idiomas de interfaz y temas del sistema/claro/oscuro; no traduce las instrucciones de los flujos. La barra lateral MCP local opcional es un paquete separado.

Las recetas de seguridad y revisión legal orientan las comprobaciones sin garantías. Publicar el repositorio y la web es distinto de enviarlo a la tienda. Se conservan los historiales Git importados y su atribución, incluidas las páginas de contacto históricas aprobadas; los cuatro repositorios GitHub sustituidos se eliminaron con autorización del responsable. [0.5.0 acceptance](../../docs/acceptance-0.5.0.md) · [Release review](../../docs/public-release-review.md).

## Contribuir y licencias

Envía incidencias o pull requests concretos. Edita solo la fuente común de skills y mantén alineados los ocho README. Código y skills originales: MIT; iconos de terceros: avisos MIT/ISC. Las ilustraciones se generaron con IA.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).

Logo Cookbook existente: contornos Cormorant Garamond bajo SIL OFL. Las ilustraciones de recetas son generadas por IA; no son capturas ni acreditan aceptación en un entorno. [Origen y licencias de recursos](../../THIRD_PARTY_NOTICES.md) · [Guía del logo](../../assets/brand/GUIDE.md).

## Apoya el desarrollo

Si Cookbook te resulta útil, puedes [apoyar mi trabajo de código abierto](https://github.com/sponsors/pengusto).
