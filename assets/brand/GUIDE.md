# Cookbook by Pengusto — Logo-Kit

Gewählte Richtung A: ein gebundenes Rezeptbuch mit einer reduzierten Pfanne im Deckel. Dieselbe Marke gilt für Plain und Kitchen. Logo-Kit für digitale Nutzung, Stand 2026-10-22.

## Dateien und Anwendung

- `cookbook-horizontal-*`: primärer Schriftzug mit Symbol, Cookbook und by Pengusto.
- `cookbook-stacked-*`: gestapelter Aufbau für quadratische Präsentationen.
- `cookbook-wordmark-*`: Schriftzug ohne Symbol.
- `cookbook-symbol-*`: Symbol für 32 px und größer.
- `cookbook-small-*`: separat vereinfachte 20er-Geometrie für 16–24 px.
- `cookbook-app-*`: bewusst unterlegte Kachel, etwa für Web-App und Touch-Icon.
- `*-light`: Weinrot für helle Hintergründe. `*-dark`: Creme für dunkle Hintergründe. Die transparenten Dateien enthalten keinen Hintergrund.
- PNG-Exporte haben die Größe im Dateinamen. SVG-Master enthalten echte Schriftkonturen, keine Live-Schrift oder eingebettete Rasterbilder.

## Farben

| Farbe | HEX | RGB | Einsatz |
|---|---|---|---|
| Weinrot | #682C27 | 104, 44, 39 | Primärmarke auf Creme oder Weiß |
| Papiercreme | #F6F0E4 | 246, 240, 228 | Negativmarke auf Weinrot oder Dunkel |
| Kohle | #25231E | 37, 35, 30 | Dunkler Hintergrund |
| Salbei | #52623E | 82, 98, 62 | Begleitfarbe, kein zweiter Logoton |
| Kupfer | #B6633D | 182, 99, 61 | Kleine Akzente, keine Pflicht im Logo |

Die Master sind einfarbig; Schwarz/Weiß bleiben für einfarbige Medien verfügbar. CMYK/Pantone sind nicht produktionstechnisch abgestimmt und werden nicht als Druckfreigabe behauptet. Für Print einen farbverbindlichen Proof und passende Separation erstellen.

## Typografie und Schutzraum

Schriftkonturen: Cormorant Garamond, Gewicht 600, SIL Open Font License; Lizenz liegt bei. Die Wortmarke wurde aus der vorhandenen Schrift aufgebaut, nicht als exklusive eigene Schrift entworfen. Keine zusätzliche Fontinstallation ist zum Anzeigen der SVGs nötig.

Schutzraum außen mindestens eine Rahmenstärke des Buchsymbols: 24 Einheiten auf dem 256er-Canvas (rund 9,4 % der Symbolhöhe). Freiraum in Lockups beibehalten. Symbol mindestens 32 px; darunter die small-Datei verwenden. Horizontal mindestens 220 px breit; gestapelt mindestens 160 px. Bei engeren Plätzen nur das Symbol verwenden; den Absender nicht unlesbar verkleinern.

Logo nicht verzerren, drehen, mit Schatten versehen oder auf unruhige Illustrationen legen. Hell/Dunkel-Variante nach tatsächlicher Fläche wählen, bei automatischer Darstellung Systempräferenz als Vorgabe nutzen. Die Form wird zwischen Themes nicht animiert oder gespiegelt.

## Codex

Die Paketquellen `assets/icon.png` und `assets/icon-dark.png` sind transparente 512×512 PNGs der gewählten Marke. Die vorhandenen Manifestfelder `logo`, `logoDark`, `composerIcon`, `composerIconDark` verweisen darauf. `assets/sidebar-icon.svg` verwendet ausschließlich currentColor und die vereinfachte kleine Geometrie; Codex bestimmt die tatsächliche Symbolfarbe. Die Buchseitenansicht verwendet das neue Symbol am Einband, ihre Rezept-Piktogramme bleiben erhalten.

Webmanifest und favicon sind vorbereitete Webassets, kein Nachweis einer PWA-Installation. Kein Plugin neu installiert, kein Store-Upload, keine Veröffentlichung. Native Codex-Darstellung muss am exakten Installationspaket zusätzlich visuell abgenommen werden.

## Rights / English usage summary

Cormorant Garamond outlines are covered by the included SIL OFL. Use light artwork on light surfaces, cream artwork on dark surfaces; preserve aspect ratio and clear space. Use the small drawing below 32 px. This digital delivery does not claim trademark clearance, exclusive ownership of general book/pan motifs, or print colour certification. The original product artwork is preserved in the local pre-kit backup.

## Prüfung und Aufbewahrung

Symbol und kleine Zeichnung bestehen den SVG-Strukturcheck ohne Warnung. Schriftkonturen enthalten erwartbar viele Anker und feine Serifen; diese Warnungen sind keine Empfehlung, den Schriftzug bei Icongröße zu verwenden. Die Konturen wurden auf Überlauf geprüft und die Zeichenflächen an ihre tatsächliche Breite angepasst. Sichtprüfung der kombinierten Übersicht und der gestapelten Wortmarke abgeschlossen. Die Paketprüfung umfasst Build, Hashes, 29 Tests und einen identischen portablen Neuaufbau.

Vorherige Produkticons bleiben unter `.scratch/logo-before-kit/` bis zur nativen Codex-Abnahme erhalten. Die Unterlagen in `design/logo-2026-10-22/` bewahren die beiden Konzeptstände. Die kleine Zeichnung ist ein eigener Master und wird nicht aus dem Schriftzug verkleinert.
