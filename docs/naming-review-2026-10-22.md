# Namensreview und Skill-Grenzen · 2026-10-22

Status: Namens-Skill korrigiert; übrige Namenspaare bleiben Vorschläge. Keine Installation umbenannt und nichts veröffentlicht. Die drei Funktionen sind die bestehende Retrospektive `here-we-go-again` und die zwei gewünschten neuen Skills.

## Gefundene Zuständigkeiten

- `which-name-wins`: Namen finden und bewerten. Bestätigter Klartext-Name des privaten Namens-Skills; Kitchen heißt „Name That Dish“. Die aktualisierte Fassung schlägt Cookbook-Namen standardmäßig als zusammengehörige Plain/Kitchen-Paare vor.
- `whats-new-on-the-menu`: Kitchen-Aufruf für belegte Änderungsnotizen; kein Namensfinder.
- `here-we-go-again`: Ursachen wiederholter Fehler und liegen gebliebene Empfehlungen untersuchen. Der globale Skill bleibt unverändert.
- Bestehendes `what-was-i-cooking` / `where-were-we`: Ziel und Verlauf des aktuellen Chats rekonstruieren. Ein neuer Wiedereinstieg muss darüber hinaus den heutigen Stand gezielt gegen veraltete Angaben prüfen.

## Konventionsprüfung

`which-name-wins` wurde in seiner eigenen kanonischen Projektquelle aktualisiert: Plain/Kitchen-Paare stehen auf derselben Zeile, einschließlich beider vorgeschlagenen Invocation-IDs. Bestehende Nutzerzuordnungen haben Vorrang; Das bestätigte Paar lautet Klartext „Which Name Wins?“ / Kitchen „Name That Dish“. Der aktuelle Standalone-Aufruf bleibt `$which-name-wins`; die Kitchen-ID `name-that-dish` ist noch kein installierter Alias. Die starre 20er-Vorgabe gilt nur noch für eine breite freie Namenssuche; Pronomen sind eine Stilpräferenz. Namenwahl, stabile Quell-ID und tatsächlich installierter Aufruf bleiben getrennt. SKILL.md und UI-Beispielprompt wurden aktualisiert; keine Installation umbenannt und nichts veröffentlicht. Der skill-creator-Validator besteht.

`here-we-go-again` besitzt einen präzisen Trigger, klare Evidenzgrenzen und einen Bericht als Standard. Der Titel „(Ah Shit) Here We Go Again“ ist eine bewusste umgangssprachliche Ausnahme von der Zwei-bis-fünf-Wörter-Empfehlung; für die Store-Anzeige wäre „Here We Go Again“ ruhiger. In `agents/openai.yaml` fehlt gegenüber der gelesenen aktuellen skill-creator-Hilfe ein Beispielprompt mit `$here-we-go-again`; diese optionale Metadatenverbesserung ist vorgeschlagen, nicht global angewendet.

## Empfohlene Namenspaare

| Funktion | Klartext | Kitchen | Begründung |
|---|---|---|---|
| Retrospektive | Here We Go Again | Why Did It Burn? | Fragt nach der Ursache eines misslungenen Versuchs. |
| Wiedereinstieg | Catch Me Up | Back to the Kitchen | Signalisiert Rückkehr nach einer längeren Pause. |
| Prompt-Vervollständigung | Finish My Prompt | Finish My Order | Vervollständigt einen begonnenen Auftrag vor seiner Ausführung. |

„Finish My Order“ ist metaphorischer als die anderen Namen: Der Untertitel muss klar „Begonnenen Prompt vervollständigen“ sagen. Kein Name behauptet Zugriff auf die native Tab-Vervollständigung. Die Namen sind Vorschläge; externe Verfügbarkeit wurde nicht geprüft.

## Frühere einzelne Vorschläge (historisch)

Diese frühe Liste war noch nicht paarweise. Die vollständige korrigierte Gegenüberstellung steht in [Namenspaare](naming-pairs.md). Alle Slugs sind Vorschläge und keine Verfügbarkeitsprüfung. Bereits bestehende Namen werden oben als Bestand geführt, nicht als neue Erfindung.

| Richtung | Rang | Name / Slug | Funktion und Grund |
|---|---|---|---|
| Locker | 1 | Why Did We Burn It? / `why-did-we-burn-it` | Retrospektive: kleine Dramatik mit klarer Ursache. |
| Locker | 2 | Get Me Cooking Again / `get-me-cooking-again` | Wiedereinstieg: zurück in die Arbeit finden. |
| Locker | 3 | Finish My Order / `finish-my-order` | Prompt: begonnenen Auftrag ergänzen. |
| Locker | 4 | What Did We Overcook? / `what-did-we-overcook` | Retrospektive: unnötige Schleifen erkennen. |
| Locker | 5 | You Know My Order / `you-know-my-order` | Prompt: vorhandenen Kontext aufgreifen, ohne Gedankenlesen zu behaupten. |
| Fragen | 1 | Why Did It Burn? / `why-did-it-burn` | Retrospektive: stärkster Kitchen-Favorit. |
| Fragen | 2 | Where Did We Leave Off? / `where-did-we-leave-off` | Wiedereinstieg: verständlich, aber nahe am bestehenden Recap. |
| Fragen | 3 | What Was My Next Step? / `what-was-my-next-step` | Wiedereinstieg: konkrete nächste Arbeit. |
| Fragen | 4 | What Did I Miss? / `what-did-i-miss` | Wiedereinstieg: Änderungen seit der Pause. |
| Fragen | 5 | Can You Finish My Thought? / `can-you-finish-my-thought` | Prompt: natürliche Bitte um Vervollständigung. |
| Direkte Bitten | 1 | Catch Me Up / `catch-me-up` | Wiedereinstieg: kurz und klar. |
| Direkte Bitten | 2 | Finish My Prompt / `finish-my-prompt` | Prompt: Funktion sofort erkennbar. |
| Direkte Bitten | 3 | Check Our Last Attempt / `check-our-last-attempt` | Retrospektive: letzter Versuch als Evidenz. |
| Direkte Bitten | 4 | Remind Me Where We Stopped / `remind-me-where-we-stopped` | Wiedereinstieg: gemeinsamer Ausgangspunkt. |
| Direkte Bitten | 5 | Complete My Request / `complete-my-request` | Prompt: klare Vervollständigung eines Auftrags. |
| Ermutigung | 1 | We Can Try Again / `we-can-try-again` | Retrospektive: zweiter Versuch nach Ursachenprüfung. |
| Ermutigung | 2 | We Can Pick Up Here / `we-can-pick-up-here` | Wiedereinstieg: ruhige Fortsetzung. |
| Ermutigung | 3 | You Can Start Here / `you-can-start-here` | Wiedereinstieg: Einstiegspunkt sichtbar machen. |
| Ermutigung | 4 | Let Me Finish That / `let-me-finish-that` | Prompt: begleitet einen begonnenen Gedanken. |
| Ermutigung | 5 | Let Us Fix the Recipe / `let-us-fix-the-recipe` | Retrospektive: aus belegten Ursachen verbessern. |

## Anzeigenamen und Aufrufe

Die Sidebar bietet Kitchen/Klartext als gespeicherte Anzeigenpräferenz. Der jeweils andere Anzeigename steht unter dem Titel. Die kopierbare Invocation und der URL-Anker bleiben beim tatsächlich gebauten Paket; ein Anzeigenwechsel installiert oder benennt keinen Skill um. Diese Trennung ist als Paketvertrag in `tests/test_sidebar.py` geprüft.

| Kitchen | Klartext |
|---|---|
| Prep the Kitchen | How Do I Start? |
| Are We Cooking? | Am I Making Progress? |
| What Was I Cooking? | Where Were We? |
| Keep the Recipe Secret | Did I Leak? |
| Can I Serve This? | Will They Sue Me? |
| Ready to Serve | Am I Ready to Share? |
| What’s New on the Menu? | What Did We Change? |
| Close the Kitchen | Can We Finish? |

## Aktueller Stand nach lokaler Erweiterung

Die vier bestätigten Quellen sind in 0.4.0 aufgenommen. Installation, neue Aufrufe und Verhaltensprüfungen werden in [skill-installation-0.4.0.md](skill-installation-0.4.0.md) dokumentiert. Die Landingpage erhält den Kochbuchstil weiterhin später; ihre aktuellen Inhalte, Skillkarten und Verknüpfungen werden mitgebaut. Keine Veröffentlichung.
