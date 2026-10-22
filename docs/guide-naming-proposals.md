# Neuer Cookbook-Guide: Namenspaare

Gewählt vom Maintainer: **Explain the Cookbook / Show Me the Kitchen**. Gemeinsame Quelle: `skills/explain-the-cookbook/`. Seit 0.5.0 als dreizehntes Rezept in Katalog, beiden Paketen und der Übersicht enthalten. Die folgenden Alternativen dokumentieren die Namensentscheidung.

Aufgabe: Cookbook erklären, vorhandene Rezepte einordnen, passend zur Nutzerfrage einen Skill empfehlen und einen konkreten Aufruf zeigen. Nicht jeden Workflow selbst ersetzen, nicht automatisch starten und nicht Pengusto als reale Person verkörpern.

## 20 bewertete Paare

Alle IDs sind Vorschläge. Gegen beide Familien des aktuellen lokalen Katalogs auf identische Titel und IDs geprüft; externe Verfügbarkeit nicht geprüft. Rang 1 ist meine Empfehlung.

| Rang | Klartext | Plain-ID | Kitchen | Kitchen-ID | Begründung / Grenze |
|---|---|---|---|---|---|
| 1 | Explain the Cookbook | `explain-the-cookbook` | Show Me the Kitchen | `show-me-the-kitchen` | Klarster Gesamtguide; zeigt Sammlung, Bedienung und Auswahl. |
| 2 | Walk Me Through It | `walk-me-through-it` | Give Me the Kitchen Tour | `give-me-the-kitchen-tour` | Persönlich und einladend; Kontext muss Cookbook benennen. |
| 3 | What Can I Do Here? | `what-can-i-do-here` | What Can We Cook Here? | `what-can-we-cook-here` | Starker Einstieg über Möglichkeiten; keine Ausführung versprechen. |
| 4 | Help Me Get Started | `help-me-get-started` | Show Me Around the Kitchen | `show-me-around-the-kitchen` | Zugänglich für neue Nutzer; vom eigentlichen Projektstart abgrenzen. |
| 5 | How Does This Work? | `how-does-this-work` | How Does This Kitchen Work? | `how-does-this-kitchen-work` | Betont Erklärung und Bedienung; verständlich, aber länger. |
| 6 | Show Me My Options | `show-me-my-options` | Show Me the Recipes | `show-me-the-recipes` | Übersicht aller Rezepte; Auswahl etwas stärker als Einführung. |
| 7 | Which Skill Should I Use? | `which-skill-should-i-use` | What Should I Cook? | `what-should-i-cook` | Sehr gute Skill-Beratung; enger als ein umfassender Gesamtguide. |
| 8 | Guide Me Through the Skills | `guide-me-through-the-skills` | Walk Me Through the Menu | `walk-me-through-the-menu` | Fokus auf Unterschiede und Einsatzmomente der Sammlung. |
| 9 | Teach Me the Basics | `teach-me-the-basics` | Teach Me the Kitchen Basics | `teach-me-the-kitchen-basics` | Einsteigerfreundlich; bei Experten nicht zu schulisch erklären. |
| 10 | Give Me the Overview | `give-me-the-overview` | Open the Cookbook | `open-the-cookbook` | Kompakt und redaktionell; Open darf kein automatisches UI-Öffnen versprechen. |
| 11 | Show Me What This Does | `show-me-what-this-does` | What’s in This Cookbook? | `whats-in-this-cookbook` | Erklärt Leistungsumfang ohne Alleskönner-Versprechen. |
| 12 | Help Me Choose a Skill | `help-me-choose-a-skill` | Help Me Choose a Recipe | `help-me-choose-a-recipe` | Klare Hilfe bei Auswahl; als Gesamtguide etwas eng. |
| 13 | Find My Workflow | `find-my-workflow` | Find My Recipe | `find-my-recipe` | Kurz und merkbar; klingt eher nach Finder als Einführung. |
| 14 | Explain My Options | `explain-my-options` | Explain the Menu | `explain-the-menu` | Ruhige Orientierung; gut für Vergleiche ähnlicher Skills. |
| 15 | Take Me Through Cookbook | `take-me-through-cookbook` | Take Me Through the Kitchen | `take-me-through-the-kitchen` | Ausdrückliche Führung, aber etwas länger. |
| 16 | Help Me Use This | `help-me-use-this` | Help Me Use the Cookbook | `help-me-use-the-cookbook` | Betont konkrete Bedienung statt nur Aufzählung. |
| 17 | Tell Me Where to Start | `tell-me-where-to-start` | Where Do I Start Cooking? | `where-do-i-start-cooking` | Natürliche Frage, aber nahe am bestehenden Projektstart. |
| 18 | Meet Your Workflows | `meet-your-workflows` | Meet Your Recipes | `meet-your-recipes` | Freundliche Sammlungseinführung; weniger präzise bei Bedienfragen. |
| 19 | Make This Make Sense | `make-this-make-sense` | Make Sense of the Menu | `make-sense-of-the-menu` | Lockerer Ton, passend zu Verwirrung; weniger sachlicher Store-Name. |
| 20 | Pengusto’s Guide | `pengustos-guide` | Pengusto’s Kitchen Guide | `pengustos-kitchen-guide` | Dein Markenwunsch als Alternative; eher Handbuchtitel, keine echte Person oder Live-Beratung. |

## Empfehlung

**Explain the Cookbook / Show Me the Kitchen** trifft den Gesamtumfang am klarsten. Der Kitchen-Aufruf wäre `$show-me-the-kitchen`. „Pengusto’s Guide / Pengusto’s Kitchen Guide“ ist die bewusst markenbezogene Alternative. Gewählt wurde Rang 1.

Die Paketaufnahme umfasst Katalog, Paketmetadaten, Übersichten und alle zwölf UI-Sprachen. Ein Entwurf oder gewählter Name allein ist noch kein funktionierender Skill-Aufruf.
