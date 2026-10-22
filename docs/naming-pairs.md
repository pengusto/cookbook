# Skill-Namen: Klartext und Kitchen

Stand: 2026-10-22. **Bestätigt sind das Namenspaar des Namens-Skills und die drei empfohlenen Paare unten** (Nutzer: „namen sind ok“). Die weiteren Alternativen bleiben Vorschläge, keine Umbenennungen oder installierten Aliasse. Externe Verfügbarkeit wurde nicht geprüft.

## Bestätigt: Namens-Skill

| Klartext | Klartext-ID | Kitchen | Kitchen-ID | Status |
|---|---|---|---|---|
| Which Name Wins? | `which-name-wins` | Name That Dish | `name-that-dish` | Vom Nutzer gewählt; als portable Quelle in 0.4.0 aufgenommen; Kitchen-Aufruf `$name-that-dish`. |

Die kanonische Quelle und der Installationslink bleiben `which-name-wins`. Die portable Cookbook-Fassung wird für Kitchen als `name-that-dish` gerendert. Die persönliche Originalquelle bleibt separat erhalten; ihr privater Korpus wird nicht paketiert.

## Bestätigte Auswahl für die drei besprochenen Skills

| Funktion | Klartext | Kitchen |
|---|---|---|
| Retrospektive | **Here We Go Again** | **Why Did It Burn?** |
| Wiedereinstieg | **Catch Me Up** | **Back to the Kitchen** |
| Prompt-Vervollständigung | **Finish My Prompt** | **Finish My Order** |

Die folgenden Tabellen enthalten fünf gewertete Paare je Funktion. Rang 1 ist die Empfehlung. Hier We Go Again ist ein bestehender Name; die bisherige ausführliche Anzeige „(Ah Shit) Here We Go Again“ wird durch diese Übersicht nicht geändert.

## Retrospektive: aus vergangenen Versuchen lernen

Vorhandener Skill: `here-we-go-again`. Untersucht wiederkehrende Ursachen, verschwendeten Aufwand und Empfehlungen ohne belegte Umsetzung. Kein reiner Projektstatus und kein Wiedereinstieg.

| Rang | Klartext | Vorgeschlagener Aufruf | Kitchen | Vorgeschlagener Aufruf | Bewertung |
|---|---|---|---|---|---|
| 1 | Here We Go Again | `$here-we-go-again` | Why Did It Burn? | `$why-did-it-burn` | Behält die bekannte Klartext-Marke; Kitchen fragt nach der Ursache. |
| 2 | What Went Wrong? | `$what-went-wrong` | What Burned This Time? | `$what-burned-this-time` | Sehr verständlich, aber stärker auf Fehler als auf liegen gebliebene Ideen fokussiert. |
| 3 | Why Are We Stuck? | `$why-are-we-stuck` | Why Is Nothing Cooking? | `$why-is-nothing-cooking` | Passt zu blockierten Plänen; könnte mit dem aktuellen Fortschrittscheck verwechselt werden. |
| 4 | Learn From Our Attempts | `$learn-from-our-attempts` | Learn From the Last Batch | `$learn-from-the-last-batch` | Deckt Fehler und erfolgreiche Gegenmaßnahmen ab; weniger markant. |
| 5 | What Should We Do Differently? | `$what-should-we-do-differently` | How Can We Cook It Better? | `$how-can-we-cook-it-better` | Betont die Verbesserung; länger und ohne Untertitel weniger eindeutig rückblickend. |

## Wiedereinstieg: nach längerer Pause wieder abholen

Neuer gewünschter Skill. Stellt Projektzweck, letzte Entscheidungen, damaligen Stand und den gezielt frisch geprüften heutigen Stand gegenüber. Endet mit einem sinnvollen Einstiegspunkt, ohne automatisch weiterzuarbeiten.

| Rang | Klartext | Vorgeschlagener Aufruf | Kitchen | Vorgeschlagener Aufruf | Bewertung |
|---|---|---|---|---|---|
| 1 | Catch Me Up | `$catch-me-up` | Back to the Kitchen | `$back-to-the-kitchen` | Kurze Rückkehr nach der Pause; beide Namen lassen Platz für Kontext und Aktualisierung. |
| 2 | Bring Me Up to Speed | `$bring-me-up-to-speed` | Bring Me Back to the Kitchen | `$bring-me-back-to-the-kitchen` | Die Auffrischung ist im Klartext besonders deutlich; Kitchen ist länger. |
| 3 | Refresh My Context | `$refresh-my-context` | Dust Off the Recipe | `$dust-off-the-recipe` | Betont veralteten Kontext und das erneute Sichten; Kitchen braucht den passenden Untertitel. |
| 4 | What Changed Since Last Time? | `$what-changed-since-last-time` | What Changed While I Was Out? | `$what-changed-while-i-was-out` | Geeignet, wenn Veränderungen seit der Pause im Vordergrund stehen; zweite Hälfte weniger kulinarisch. |
| 5 | Help Me Pick This Up Again | `$help-me-pick-this-up-again` | Get Me Cooking Again | `$get-me-cooking-again` | Menschlicher Ton; kann ohne Untertitel bereits Ausführung statt Orientierung erwarten lassen. |

## Prompt-Vervollständigung: einen begonnenen Auftrag ergänzen

Neuer gewünschter Skill. Nutzt den sichtbaren Kontext für einen bearbeitbaren Prompt-Vorschlag in der Sprache des Nutzers. Führt den vorgeschlagenen Auftrag nicht aus, erfindet keine Absicht und verspricht keine native Tab-Integration.

| Rang | Klartext | Vorgeschlagener Aufruf | Kitchen | Vorgeschlagener Aufruf | Bewertung |
|---|---|---|---|---|---|
| 1 | Finish My Prompt | `$finish-my-prompt` | Finish My Order | `$finish-my-order` | Klarste Funktion auf der Plain-Seite; Kitchen passt zum begonnenen Auftrag. Untertitel: Begonnenen Prompt vervollständigen. |
| 2 | Finish My Thought | `$finish-my-thought` | Finish the Recipe | `$finish-the-recipe` | Natürlicher und persönlicher; Kitchen könnte einen vollständig ausgearbeiteten Plan versprechen. |
| 3 | Complete My Request | `$complete-my-request` | Complete the Order | `$complete-the-order` | Sachlich und verständlich; Untertitel muss vom Ausführen einer Bestellung abgrenzen. |
| 4 | Help Me Say It | `$help-me-say-it` | Help Me Write the Order | `$help-me-write-the-order` | Gute Wahl für gemeinsames Formulieren, klingt weniger nach automatischer Ergänzung. |
| 5 | What Was I About to Ask? | `$what-was-i-about-to-ask` | What Was I About to Order? | `$what-was-i-about-to-order` | Spielerisch und nah am abgebrochenen Gedanken; Kontextgrenzen müssen sichtbar bleiben. |

## Prüfung der zwölf integrierten Skills

Die acht bisherigen Katalogeinträge besitzen bereits zwei unterschiedliche Anzeigenamen und zwei gültige, innerhalb der jeweiligen Variante eindeutige Invocation-IDs. Für diese Liste ist keine Umbenennung nötig. Stabile Quell-IDs bleiben unverändert.

| Klartext | Aufruf | Kitchen | Aufruf | Bewertung |
|---|---|---|---|---|
| How Do I Start? | `$how-do-i-start` | Prep the Kitchen | `$prep-the-kitchen` | Paar passend für Projektstart und ersten kleinen Schritt. |
| Am I Making Progress? | `$am-i-making-progress` | Are We Cooking? | `$are-we-cooking` | Passender Fortschrittscheck; von Retrospektive und Pause trennen. |
| Where Were We? | `$where-were-we` | What Was I Cooking? | `$what-was-i-cooking` | Passender Chat-Recap. Neuer Wiedereinstieg braucht zusätzlich heutige Zustandsprüfung. |
| Did I Leak? | `$did-i-leak` | Keep the Recipe Secret | `$keep-the-recipe-secret` | Secret-Prüfung erkennbar; keine Sicherheitsgarantie aus dem Namen ableiten. |
| Will They Sue Me? | `$will-they-sue-me` | Can I Serve This? | `$can-i-serve-this` | Kitchen klingt nach Freigabe; Untertitel muss technisches Produktreview und Grenzen erklären. |
| Am I Ready to Share? | `$am-i-ready-to-share` | Ready to Serve | `$ready-to-serve` | Passend für Repository- und Release-Vorbereitung; keine Veröffentlichung durch den Namen. |
| What Did We Change? | `$what-did-we-change` | What’s New on the Menu? | `$whats-new-on-the-menu` | Passendes Paar für Änderungsnotizen; kein Namensfinder. |
| Can We Finish? | `$can-we-finish` | Close the Kitchen | `$close-the-kitchen` | Passend für Abschluss oder bewusste Übergabe. |

## Weitere zurückgestellte Skills ohne bestätigtes Namenspaar

Diese vier allgemeinen Workflows stehen im historischen Projektinventar. Ihre aktuellen SKILL.md-Beschreibungen wurden für die Namenspassung gelesen. Die folgenden Paare sind zusätzliche Vorschläge; keine neue Zusage zur Paketaufnahme, Lizenz oder Portabilität. Persönliche Betriebs- und Kontoskills sind bewusst außerhalb dieser Namensrunde.

| Bestehender Skill | Klartext-Vorschlag | Plain-ID | Kitchen-Vorschlag | Kitchen-ID | Warum |
|---|---|---|---|---|---|
| Let Him Grill | Let Me Decide | `let-me-decide` | Let Him Grill | `let-him-grill` | Begrenzte Planungsentscheidungen eigenständig klären; vorhandenen kulinarischen Namen behalten. |
| Yap to Spec | Turn This Into Tasks | `turn-this-into-tasks` | Write the Recipe | `write-the-recipe` | Lose Chat-Ideen in ausgewählte Aufgaben oder kurze Spezifikationen überführen. |
| You Got This | You Got This | `you-got-this` | Take Over the Kitchen | `take-over-the-kitchen` | Breiten Ausführungsworkflow mit passender Küchenmetapher verbinden. |
| Remix My UI | Remix My UI | `remix-my-ui` | Try Another Plating | `try-another-plating` | Mehrere visuelle Richtungen vergleichen; keine Änderung des Produktzwecks versprechen. |

## Alle Vorschläge sehen

Diese Datei zeigt beide Namenswelten und sämtliche Alternativen direkt nebeneinander. Die Kochbuch-Sidebar hat für die zwölf integrierten Skills zusätzlich eine Kitchen/Klartext-Umschaltung und zeigt den anderen Namen unter dem Titel. Die drei Erweiterungen und die portable Namensfassung sind Teil von 0.4.0 und des Sidebar-Katalogs. Die vier weiteren zurückgestellten Workflows bleiben Vorschläge.

## Festgehaltene Korrektur und Prüfung

Eine Frage nach dem Kitchen-Namen ist keine Festlegung. Bestätigte Namen werden aus ausdrücklichen Entscheidungen übernommen. Im Namens-Skill steht nun explizit: Plain „Which Name Wins?“ / Kitchen „Name That Dish“. Die bisherige falsche Zuordnung wurde ersetzt. Die 15 Hauptvorschläge wurden gegen beide Namens- und ID-Familien des aktuellen Katalogs auf identische Namen und Aufruf-IDs geprüft. Ähnliche Einsatzmomente sind in den Bewertungen genannt. Der Skill-Validator prüft die Struktur; er beweist keine unverwechselbare Namenswirkung.

## Aufrufen in Codex

Namen als Skill über `$` mit Bindestrichen aufrufen, nicht als Slash-Befehl mit Leerzeichen. Nach Installation eine neue Codex-Sitzung öffnen. Die wählbaren Anzeigenamen auf der Seite installieren keine zweite Variante. [Installations- und Verhaltensnachweise](skill-installation-0.4.0.md).
