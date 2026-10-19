# Cookbook by Pengusto

[![MIT](https://img.shields.io/badge/license-MIT-blue)](../../LICENSE) [![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](../../README.md#build-and-verify) [![Beta](https://img.shields.io/badge/status-experimental_Beta-orange)](../../docs/public-release-review.md) [![CI](https://img.shields.io/badge/CI-launch_checks-grey)](https://github.com/pengusto/cookbook/actions/workflows/check.yml)

[English](../../README.md) · [Deutsch](README.de.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [Español](README.es.md) · [한국어](README.ko.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md)

> Machine-translated documentation; no independent fluent-speaker review. Commands, identifiers and paths match the English source.

Ocho flujos de trabajo para agentes desde una fuente mantenida. Elige **preguntas sencillas** o **nombres de cocina** e instala un solo estilo por entorno.

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

## Compilar y verificar

Se requieren Git y Python 3.10+; no hacen falta paquetes Python. Instala Codex o Claude Code e inicia sesión por separado. Ejecuta los comandos desde la raíz del repositorio.

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

## Instalar un estilo de nombres

Elige plain o kitchen. Ambos usan la misma identidad de plugin. Los ejemplos instalan Kitchen. Después inicia una sesión nueva. La compilación no cambia las instalaciones existentes.

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

Antes de cambiar de estilo, guarda una copia del paquete instalado, desinstala únicamente el plugin Cookbook con la herramienta nativa y elimina su registro de marketplace; registra el otro estilo. Evita copias individuales o el antiguo paquete vibe-coding-cookbook en paralelo.

También hay instalación individual; el flujo no debe existir en el destino. El ejemplo crea close-the-kitchen; plain crea can-we-finish.

```sh
python3 scripts/cookbook.py install kill-the-todos --variant kitchen --dest /empty/local/skills
```

Codex: `$close-the-kitchen` · Claude Code: `/cookbook-by-pengusto:close-the-kitchen`

`skills/<stable-id>/` → `catalog.json` → `dist/{plain,kitchen}/{codex,claude}` · `site/downloads/`: 4 plugin ZIPs + 16 individual ZIPs + `SHA256SUMS`.

## Actualizar

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

Confirma o guarda tus cambios antes de actualizar. Compilar actualiza los paquetes locales, no la caché instalada. Guarda el paquete y utiliza la desinstalación/reinstalación nativa para renovarlo. Consulta la guía de Mac. [Mac setup](../../docs/mac-setup.md).

## Sitio web

Las páginas DE/EN siguen el tema claro u oscuro del sistema. Idioma y nombres se cambian por separado; las instrucciones de los skills no se traducen. Inicia la vista previa y abre la URL indicada. Esta Beta no incluye un sitio público desplegado ni publicación en tiendas.

```sh
python3 scripts/cookbook.py serve --port 8767
```

`index.html` / `kitchen.html` (DE), `index-en.html` / `kitchen-en.html` (EN). [Website details](../../docs/landing-page.md).

## Límites y estado

Se automatizan las comprobaciones de paquetes, hashes, enlaces y compilación portable. La carga de skills se probó localmente; quedan pendientes la aceptación visual completa en escritorio y las tiendas. Los skills de seguridad y revisión legal no dan garantías. El historial conserva páginas de contacto antiguas autorizadas por el mantenedor. Los historiales Git originales se conservan en Cookbook; los cuatro repositorios anteriores de GitHub se eliminaron con autorización. [Release review](../../docs/public-release-review.md).

## Contribuir y licencias

Envía incidencias o pull requests concretos. Edita solo la fuente común de skills y mantén alineados los ocho README. Código y skills originales: MIT; iconos de terceros: avisos MIT/ISC. Las ilustraciones se generaron con IA.

[Contributing](../../CONTRIBUTING.md) · [MIT](../../LICENSE) · [Third-party notices](../../THIRD_PARTY_NOTICES.md) · [Maintenance](../../docs/maintenance.md).
