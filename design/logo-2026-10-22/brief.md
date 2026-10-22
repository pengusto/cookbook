# Cookbook by Pengusto — Logo-Konzepte

Ziel: warmes, handwerkliches und souveränes Zeichen für eine kuratierte Skill-Sammlung. Hauptname Cookbook, Absender by Pengusto. Beide Namensvarianten teilen dieselbe Marke. Einsatz: Codex-Plugin 16–32 px, Kochbuchseite, README und spätere Landingpage. Bestehende Buch/Pfanne-Marke bleibt bis zur Wahl erhalten.

Die Marke soll die Kochbuchwelt aufnehmen, aber keine Illustration mit Zutaten werden. Keine generischen Code-Klammern, KI-Sterne, Kochmützen oder zusätzlichen Besteck-Piktogramme. Kleine Details und Farbe dürfen die Erkennung nicht tragen.

## Longlist und Vorauswahl

Bewertung je Idee: Klarheit / Eigenständigkeit / Einfachheit / Passung / kleine Größe (je 1–5).

| Idee | Typ | Punkte | Entscheidung |
|---|---|---|---|
| Gebundenes Rezeptbuch mit einer reduzierten Pfanne im Deckel | Bildmarke | 5/3/4/5/4 | A: bestehende Markenidee präzisieren |
| Ein kräftiges C wird zum Pfannenkörper mit kurzem Griff | Buchstabenmarke | 4/4/5/5/5 | B: stärkstes kleines Zeichen |
| Zwei offene Seiten bilden über einer geschwungenen Basis einen servierten Teller | Abstrakte Bildmarke | 4/4/5/5/4 | C: ruhigste Buchmarke |
| Acht Rezeptregister bilden ein C | Abstrakt | 3/3/2/4/2 | Zu viele kleine Lücken |
| Ein Kochlöffel als Lesezeichen | Bildmarke | 4/2/4/4/3 | Zu nah an gewöhnlichen Küchenpiktogrammen |
| Kochmütze aus Buchseiten | Kombination | 4/2/3/4/3 | Klischee |
| CB als verschlungene Kücheninitialen | Monogramm | 2/3/3/3/2 | Kleine Lesbarkeit zu schwach |
| Eigene Serifenschrift mit Pfanne im zweiten o | Wortmarke | 3/3/2/4/1 | Symbol für 16 px fehlt |
| Rezeptkarte mit einem einzelnen Einschnitt | Abstrakt | 3/3/5/3/5 | Zu wenig Bezug zur Buchmarke |

Konstruktion: alle Symbole auf 256er-Canvas, kräftige gefüllte Flächen; keine Rasterbilder, Filter oder Live-Schrift. A nutzt 24 Einheiten Rahmen und einen ausgesparten Pfannenring. B nutzt einen 90er Außenradius und einen 56er Innenradius. C nutzt zwei getrennte Seiten mit 24 Einheiten Mittelraum. Buchstaben in Präsentationsbeschriftungen sind keine finalen Wortmarken.

Bibliotheksvergleich: Storybook nur als Beispiel für kleine Buchsilhouetten; weitere Exemplare für Negativraum und gefüllte Geometrie. Keine Dateien oder Konturen übernommen. Die lokale Referenzbibliothek ist keine Markenfreigabe.

## Abnahme der Konzepte

Zwei Geometrie-Runden gerendert und visuell geprüft. A bleibt Empfehlung, weil es vorhandene Markenidee und Kochbuch zusammenführt. B ist kompakter, aber ohne Wortmarke nicht eindeutig ein Kochbuch. C ist ruhig und gut zum Buchstil passend, aber ähnelt eher einer allgemeinen Verlagsmarke. SVG-Audit in audit-v2.txt; Größenleiter 64/32/16 auf concepts.png. Kein finales Logo-Kit, keine Produktassets ersetzt.

Der Chrome-Renderer des Skills lieferte in diesem Lauf kein Bild; der Aufruf wurde beendet. Die SVG-Übersicht wurde mit dem bereits installierten Sharp/librsvg gerendert und angesehen. Rendering-Fallback ist kein Beleg für Browserdarstellung oder Markenfreigabe.

Skill vor Beginn auf offizielle Version 1.4.5, Commit 734090317a2155c5bf1ae8bd4cc85c6848a0128f, aktualisiert. Vollständiger Dateivergleich gegen Quelle bestanden; zwei Upstream-Tests bestanden. Vorherige Skillinstallation (~13 MiB) bleibt in ignorierter .scratch/logo-design-before-1.4.5 bis zur bestätigten Nutzung der aktualisierten Exporte erhalten. Quellcheckout bleibt als Update-Nachweis unter .scratch/logo-design-upstream.
