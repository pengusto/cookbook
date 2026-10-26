# Choose by the question / Nach der Frage wählen

Choose the situation first, then use the installed naming variant. The guide
recommends one workflow; it does not execute the recommendation. Kitchen and
Plain have the same behavior. These examples use Codex syntax. In Claude Code,
use `/cookbook-by-pengusto:<installed-id>` followed by the same arguments.

Wähle zuerst die Situation, dann die installierte Namensvariante. Die Auswahlhilfe
empfiehlt einen Ablauf, führt ihn aber nicht automatisch aus. Die Beispiele
verwenden Codex-Syntax; für Claude Code gilt die Syntax im Absatz oben.

| Your question / Deine Frage | Plain | Kitchen | Result / Ergebnis |
|---|---|---|---|
| Which workflow fits? / Welcher Ablauf passt? | Explain the Cookbook | Show Me the Kitchen | One recommendation / Eine Empfehlung |
| Where did we start? / Wo hatten wir angefangen? | Find Our Work | Find the Recipe | Verified source match / Bestätigte Originalquelle |
| I have been away. / Ich war länger weg. | Catch Me Up | Back to the Kitchen | Project reentry checked against today / Wiedereinstieg mit aktuellem Abgleich |
| What did I originally ask? / Was wollte ich ursprünglich? | Where Were We? | What Was I Cooking? | This chat’s goal and decisions / Ziel und Entscheidungen dieses Chats |
| Where do I start? / Wie fange ich an? | How Do I Start? | Prep the Kitchen | Small next step / Kleiner nächster Schritt |
| Finish my request. / Formuliere meinen Auftrag fertig. | Finish My Prompt | Finish My Order | Draft only / Nur Prompt-Entwurf |
| What should I call it? / Wie soll es heißen? | Which Name Wins? | Name That Dish | Ranked name options / Namensvorschläge |
| Does this journey work? / Funktioniert dieser Nutzerablauf? | You Got This `usertest` | You’re the Chef `usertest` | Observed journey findings / Befunde aus tatsächlichen Aktionen |
| Build this for me. / Setze das um. | You Got This | You’re the Chef | Verified implementation / Geprüfte Umsetzung |
| Are we getting anywhere? / Kommen wir voran? | Am I Making Progress? | Are We Cooking? | Course check / Kursprüfung |
| This fails now. / Das schlägt gerade fehl. | Why Is It Broken? | Find the Bad Ingredient | Reproduction, cause, requested fix / Reproduktion, Ursache, beauftragter Fix |
| Can it be simpler? / Geht das einfacher? | Can We Simplify? | Trim the Recipe | Behavior-preserving reduction / Vereinfachung mit gleichem Verhalten |
| Review this change. / Prüfe diese Änderung. | Review My Changes | Taste Before Serving | Concrete diff findings / Konkrete Diff-Befunde |
| Could I leak something? / Könnte ich etwas offenlegen? | Did I Leak? | Keep the Recipe Secret | Sensitive-content review / Prüfung sensibler Inhalte |
| What product/legal risks apply? / Welche Produkt- und Rechtsfragen gelten? | Will They Sue Me? | Can I Serve This? | Scoped review with evidence / Eingrenzung mit Belegen |
| Can others use this repo? / Können andere das Repo nutzen? | Am I Ready to Share? | Ready to Serve | Sharing preparation / Vorbereitung zum Teilen |
| What changed? / Was hat sich geändert? | What Did We Change? | What’s New on the Menu? | Release notes / Änderungsnotizen |
| Can we stop here? / Können wir aufhören? | Can We Finish? | Close the Kitchen | Completion, cleanup review, handoff / Abschluss, Aufräumprüfung, Übergabe |
| How does it work? / Wie funktioniert das? | How Do I Start? `explain` | Prep the Kitchen `explain` | Code-path explanation / Erklärung des Codepfads |
| Which option fits? / Welche Option passt? | How Do I Start? `choose` | Prep the Kitchen `choose` | Grounded recommendation / Begründete Empfehlung |
| Is it really delivered? / Ist es wirklich ausgeliefert? | Am I Ready to Share? `verify-live` | Ready to Serve `verify-live` | Delivery evidence and gaps / Auslieferungsnachweise und Lücken |
| Continue on another machine. / Auf anderem Rechner fortsetzen. | Can We Finish? `handoff` | Close the Kitchen `handoff` | Destination-specific preparation / Zielbezogene Vorbereitung |
| Why does this keep happening? / Warum passiert das immer wieder? | Here We Go Again | Why Did It Burn? | Patterns and preventive lessons / Muster und Vorbeugung |

## Examples / Beispiele

```text
$find-the-bad-ingredient Saving reports success, but changes disappear after reload. Find and fix the cause.
$why-is-it-broken Investigate the failing build; do not edit files.
$youre-the-chef usertest Create, save, reload and reopen a draft in the local test environment. Report findings without fixes.
$you-got-this usertest Prüfe das Formular mit Tastatur und schmalem Bildschirm. Nur Befunde, keine Änderungen.
```

`usertest` is an agent-run journey check, not a study with human participants.
It adds no separate skill. Missing interaction tools remain a coverage gap.
Real payments, external messages and production mutations require specific
authorization. Requested fixes are retested against the original journey.

`usertest` prüft einen echten Bedienablauf durch den Agenten; es ist keine
Studie mit Menschen und kein zusätzlicher Skill. Fehlende Interaktionswerkzeuge
bleiben eine Prüflücke. Reale Zahlungen, Nachrichten und produktive Änderungen
brauchen einen konkreten Auftrag. Beauftragte Fixes werden am ursprünglichen
Ablauf nachgeprüft.

## More focused examples / Weitere gezielte Beispiele

```text
$taste-before-serving Review the selected settings diff for regressions; report findings without edits.
$trim-the-recipe Simplify this export path while preserving its public format and errors.
$find-the-recipe Find the earlier scanner-comparison chat or handoff; do not move anything.
$prep-the-kitchen explain how a saved draft reaches the database
$prep-the-kitchen choose whether this project needs another state library
$ready-to-serve verify-live Compare the intended release with the package users actually receive.
$close-the-kitchen handoff Prepare the next work block for the other machine, including its first verification step.
```

Code review inspects a bounded change; usertest exercises a real user journey.
Simplification preserves contracts; debugging corrects a current defect. Finding
work locates its source before a recap or reentry. An explanation, comparison,
review or lookup alone does not authorize edits. `verify-live` observes delivery;
it does not publish. `handoff` prepares context; actual sending or host transfer
requires the user's corresponding instruction.

Code-Review untersucht die Änderung; usertest durchläuft den Bedienablauf.
Vereinfachung erhält Verträge; Debugging behebt einen aktuellen Fehler. Die Suche
findet die Quelle vor Rückblick oder Wiedereinstieg. Erklär-, Vergleichs-, Review-
und Suchaufträge allein erlauben keine Änderungen. `verify-live` prüft und
veröffentlicht nicht. `handoff` bereitet Kontext vor; Versand oder Hostwechsel
brauchen den entsprechenden Auftrag.
