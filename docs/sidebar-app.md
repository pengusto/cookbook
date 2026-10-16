# Cookbook in der globalen Codex-Leiste

Stand 2026-10-15: lokale Sidebar-App installiert und aktiviert. Kein Upload, keine Veröffentlichung. Die sichtbare Platzierung in der laufenden Desktop-Oberfläche ist noch nicht bestätigt; UI-Automation für Codex ist hier gesperrt. Kein App-Neustart ausgelöst.

Die offizielle Erweiterung dafür ist ein MCP-App-Tool mit `_meta["openai/ui"].entrypoints: [{"type":"global"}]`. Es öffnet die App aus der primären Navigation. Das Navigationssymbol kommt zuerst aus `tools/list` → `icons`, danach aus dem Server-Icon. Ein reines Skill-Bündel mit Listing-Icon erzeugt diesen Einstieg nicht.

## Lokale Umsetzung

`python3 scripts/cookbook.py build` erzeugt zusätzlich `dist/sidebar/` mit eigenem Marketplace, dem Plugin `cookbook-sidebar` und einem ZIP. Das bestehende Codex-/Claude-Skill-Bündel und die Einzelpakete bleiben unabhängig. Die Sidebar-App dupliziert keine installierten Skills.

- Einziger Tool-Einstieg: `open_cookbook`, Titel Cookbook, akzeptiert `{}`.
- Helle/dunkle Pfannen-/Ei-PNGs direkt als eingebettete Tool- und Server-Icons; unabhängig vom Listing-Icon, ohne externen Bildserver.
- Lesbare Rezeptkarten aus demselben `catalog.json`, aufklappbare Details und Beispielaufrufe. Keine Installations-, Schreib- oder Veröffentlichungsaktionen.
- Selbst enthaltene HTML-Ressource mit MCP-App-Initialisierung; keine Downloads, externen Ressourcen oder Netzverbindungen. Inhalte sind im Build enthalten, kein Loopback-Server nötig.
- Python 3.10+ und Standardbibliothek, keine neuen Pakete oder Hooks. Der MCP-Prozess läuft bei Bedarf über stdio. `cwd: ./` und relativer Skriptpfad werden vom Plugin-Root aufgelöst. Ein zunächst getesteter `${PLUGIN_ROOT}`-Argumentpfad scheiterte beim MCP-Start und wurde ersetzt.

## Nachweise

Zehn Tests bestehen: einschließlich tatsächlichem stdio-Handshake, tools/list, Aufruf mit `{}`, UI-Ressource, beiden Navigationsicons, Abweisung fremder Ressourcen/Argumente/Methoden und ZIP-Dateigleichheit. Build, Check und Quellenabgleich bestehen; Skill-Originale unverändert.

Native Installation: `codex plugin marketplace add ./dist/sidebar`, dann `codex plugin add cookbook-sidebar@cookbook-sidebar-local`. Codex CLI 0.160.0 listet die Installation als enabled. Die native app-server-Abfrage `mcpServerStatus/list` erkennt `open_cookbook` und `ui://cookbook/catalog-v1`, mit `toolsError: null`. Diese Prüfung verwendet keine Modellaufrufe. Private Roh-Evidenz liegt unter `.scratch/sidebar/`.

Der Eintrag bleibt auf Nutzerwunsch lokal installiert. Falls die laufende App ihn noch nicht zeigt, Codex neu laden und Cookbook in der globalen Navigation beziehungsweise deren Mehr-Menü prüfen. Genaues Pinning, Reihenfolge und gerendertes Icon sind noch keine sichtbare Abnahme. Ein CLI-Discovery-Nachweis ersetzt diese nicht.

Entfernung bei Bedarf: `codex plugin remove cookbook-sidebar@cookbook-sidebar-local`, anschließend `codex plugin marketplace remove cookbook-sidebar-local`. Keine anderen Plugins verändern.

## English

An optional, local-only MCP sidebar companion is installed and enabled. It exposes a global entrypoint with explicit frying-pan/egg tool icons and a read-only catalog generated from the existing source. Python standard library only; no duplicate skills, hooks, external assets or publishing. Native Codex discovery succeeds; visual placement and the rendered UI remain unverified. Reload the desktop host if the entry is not yet visible. The companion is independent of the original skill bundles.

## Primary references

- [OpenAI Plugin Extensions](https://developers.openai.com/plugins/build/extensions): global sidebar apps.
- [OpenAI MCP Extensions specification](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md): global entrypoints, icon priority and empty-object invocation.

Read 2026-10-15. The previous assumption that no supported sidebar route was established is superseded by this implementation and native discovery evidence.


## Icon-Überarbeitung 0.1.1

Nach sichtbarer Nutzerabnahme der Sidebar-App: mehr Flächennutzung, kräftigere Konturen und deutlich helleres Symbol im Dark Mode. Eine reduzierte Buchkontur rahmt die Pfanne mit Ei. Die lokale Sidebar-Version 0.1.1 ersetzt 0.1.0; Tool und Funktionen bleiben gleich. Vorschau in assets/sidebar-preview.png zeigt 24, 32 und 48 Pixel. Die neue Darstellung in der laufenden Codex-Leiste muss nach Neuladen visuell bestätigt werden.

## Monochromes Navigationssymbol 0.1.2

Die Nutzerbeobachtung: Farben erscheinen in der linken Leiste weiß und die Darstellung wirkt blass. Die OpenAI Icon Guidelines empfehlen für Entrypoint-Tools transparente, monochrome SVGs mit `currentColor`, 20×20 Viewport und 1,33 px Kontur. Die abgerufene GitHub-Seite enthielt diese Hinweise, während die gleichzeitig abgerufene Raw-Fassung noch die kürzere Icon-Prioritätsbeschreibung zeigte. Referenz: https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#icon-guidelines (2026-10-15).

Sidebar 0.1.2 liefert deshalb `assets/sidebar-icon.svg` direkt als Tool- und Server-Icon. Buch und Pfanne haben klare Konturen; das Ei eine volle Fläche und einen transparent ausgesparten Dotter. Damit bleibt die Zeichnung ohne Farbunterschiede verständlich. Keine eingebaute Transparenz oder grauen Abstufungen; die tatsächliche Navigationsfarbe bestimmt der Host. Farbige Listing-Icons bleiben eigenständige Assets. Die Vorschau simuliert helle und dunkle Hintergründe bei 20, 24, 32 und 40 Pixeln; sie ist kein Screenshot aus Codex.

Build, Check, Quellenabgleich und zehn Tests bestehen. Version 0.1.2 wurde lokal mit `codex plugin add cookbook-sidebar@cookbook-sidebar-local --json` installiert. Sichtbare Darstellung und eventuelle hostseitige Abschwächung im inaktiven Zustand müssen nach Neuladen weiterhin am Desktop geprüft werden. Nichts veröffentlicht.

English: Sidebar 0.1.2 uses a transparent monochrome SVG with `currentColor`, a 20×20 viewport and 1.33 px outlines. A transparent yolk cutout keeps the egg recognizable when tinted. Local installation and packaging checks pass; the actual rendered desktop appearance remains to be confirmed after reload.
