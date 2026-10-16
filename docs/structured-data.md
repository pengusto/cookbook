> **Historischer Prüfstand 0.1.x.** Die aktuelle Architektur, Namenswelten und Installationswege stehen in [consolidation.md](consolidation.md) und der [README](../README.md). Frühere Testergebnisse werden nicht als neue 0.2.0-Abnahme behauptet.

# Strukturierte Daten: lokal eingebunden

Stand 2026-10-15: Die Cookbook-Startseite enthält jetzt einen JSON-LD-Block im HTML-Head. Der installierte Skill `schema` wurde angewendet; er wird nicht Teil des Cookbook-Bündels. Die Website wurde nicht veröffentlicht. Der eingebundene JSON-LD-Block wurde auf ausdrücklichen Nutzerwunsch per Code-Eingabe an Schema.org und Google zur Prüfung gesendet.

`scripts/cookbook.py` erzeugt das Markup bei jedem Build direkt aus denselben Katalogzeilen wie die sichtbaren Karten. `templates/index.html` bindet es über `{{STRUCTURED_DATA}}` ein. `site/index.html` und `dist/website.zip` enthalten den finalen lokalen Stand. Es gibt keine zusätzliche manuell zu pflegende Produktionskopie.

## Zweck und Auswahl

Schema.org beschreibt die Bedeutung von Website-Inhalten. JSON-LD ist dafür ein maschinenlesbares Format. Das ist unabhängig von JSON Schema zur Datenvalidierung und von Plugin-Manifesten zur Installation.

- Die eingebundene Startseite: CollectionPage mit einer ItemList der sechs sichtbaren Katalogeinträge. Jeder Eintrag ist ein CreativeWork. Der Katalogeintrag Are We Cooking? behauptet damit keine Paketverfügbarkeit.
- Die sechs Dateien unter `structured-data/` bleiben frühere Dokumentationsbeispiele, keine Build-Eingabe. Die fünf Skill-spezifischen Beispiele: WebPage mit SoftwareSourceCode als Hauptinhalt für die fünf vorhandenen Skill-Snapshots. Das beschreibt die verteilten Quelldateien einschließlich ihrer Anleitungen; es behauptet keine eigenständig ausführbare Anwendung. Vor Einbau muss die jeweilige Website tatsächlich diesen Inhalt vorstellen.
- Titel und Beschreibungen stammen aus `catalog.json`. Es gibt keine erfundenen Bewertungen, Preise, Downloads, Autoren oder öffentlichen URLs. Die Dokumentationsbeispiele sind manuelle Momentaufnahmen; bei Katalogänderungen vor Verwendung erneut abgleichen. Das eingebundene Cookbook-Markup bleibt automatisch synchron.

Trotz des Namens Cookbook verwenden wir kein Recipe-Markup: Es handelt sich um eine Skill-Sammlung. SoftwareApplication, Product und FAQPage werden ohne passenden sichtbaren Inhalt und konkrete Suchmaschinen-Unterstützung ebenfalls nicht ergänzt.

Der Nutzen ist eine eindeutige Beschreibung der Seiten. Eine besondere Google-Darstellung oder bessere Platzierung folgt daraus nicht automatisch. Vor einer späteren Freigabe müssen reale Seiten-URLs, eindeutige IDs und gegebenenfalls belegte öffentliche Repository-/Lizenzlinks ergänzt werden. Private Repository-Adressen und lokale Pfade gehören nicht hinein. Der lokale Einbau benötigt diese öffentlichen Angaben nicht: `url`, `@id`, Canonical, Repository- und Download-URLs bleiben im JSON-LD vollständig weg. Der einzige URL-Wert ist der feste Vokabular-Kontext `https://schema.org`. Keine Bewertungen, Preise, Veröffentlichungstermine, Verfügbarkeits- oder Rich-Result-Versprechen. Die Freigabe für die beiden Code-Tests wurde anschließend ausdrücklich erteilt; Ergebnisse siehe unten.

## Warum der Schema-Skill erwähnt wird

Der lokal installierte Skill `schema` behandelt Schema.org und strukturierte Website-Daten. Der ebenfalls installierte Skill `ai-seo` verweist mehrfach darauf. Im Cookbook-Bündel sowie in den untersuchten Cookbook-Texten und Vorlagen ist er nicht enthalten. Die Ursache wiederholter Vorschläge in der App-Preview ist damit nicht belegt; eine Empfehlung durch den SEO-Kontext bleibt eine Vermutung. Die Beispiele ändern keine App-Empfehlungen.

## Store-Einreichung ist ein eigener Schritt

Schema.org-Markup ist keine Voraussetzung für die beschriebenen Plugin-Einreichungswege. Unsere lokalen ZIPs sind Review-Pakete, keine bestätigten Store-Pakete.

Die zunächst fehlenden Interface-Angaben und Icons (`logo`, `composerIcon`) sind inzwischen lokal ergänzt; siehe store/README.md und host-tests.md. Konto-/Publisher-Voraussetzungen, Upload, automatische Prüfungen und Review bleiben separate Schritte. Bei Skills-only verlangt OpenAI nicht dieselben MCP-Testfälle und Demo-Videos wie bei einem Plugin mit MCP-Verbindung. Die Eignung für Desktop-Ausführung muss wegen lokaler Werkzeuge separat geprüft werden.

Claude beschreibt für Plugin-Bündel einen GitHub-basierten Einreichungsweg über sein Directory-Portal für bezahlte Pläne, inklusive automatischer Validierung, Sicherheitsprüfung und Review. Die vorhandene Claude-Code-Laufzeit besteht inzwischen native Validierung und lädt das Paket; Modell-Verhaltenstests scheitern an fehlender Anmeldung. Ein lokal ladbares Claude-Code-Plugin beweist noch keine Freigabe für andere Claude-Oberflächen.

Einschätzung: überschaubarer technischer Aufwand für ein Skills-Bündel; die verbleibende Arbeit liegt vor allem in nachvollziehbaren Host-Tests, vollständigen Metadaten und dem Review. Es gibt keine zugesagte Annahme oder Durchlaufzeit. Nächste sinnvolle Reihenfolge: Host-Tests, Distribution-Metadaten/Icons, private Review-Fassung; Website-Markup ist lokal eingebaut; öffentliche IDs und Zieladressen folgen erst, sobald die Zielseiten feststehen. Nichts wurde eingereicht.

## Quellen und Prüfgrenzen

- [Schema.org: CollectionPage](https://schema.org/CollectionPage), [ItemList](https://schema.org/ItemList), [SoftwareSourceCode](https://schema.org/SoftwareSourceCode).
- [Google: Structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies): sichtbaren Inhalt korrekt wiedergeben; Rich Results sind nicht garantiert.
- [OpenAI: Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission): Distribution-Metadaten, Icons und Einreichung.
- [OpenAI: Desktop-only plugins](https://developers.openai.com/plugins/deploy/desktop-only).
- [Anthropic: Plugin directory submission](https://claude.com/resources/articles/build-plugins-for-claude).

Quellen am 2026-10-15 gelesen. Lokal wurden JSON-Syntax, Katalogübereinstimmung und der Verzicht auf erfundene Angaben geprüft. Diese früheren lokalen Prüfungen sind von den nachfolgenden externen Validator-Ergebnissen und einer Store-Prüfung zu unterscheiden.


## Lokale Prüfung des Einbaus

Zwei Regressionstests prüfen den finalen HTML-Block gegen tatsächlich geparste sichtbare Kartentitel und Beschreibungen, Anzahl und Reihenfolge sowie das bewusst minimale Schema. Ein Sonderzeichentest prüft, dass neue Katalogwerte sofort übernommen werden und `</script>` in einem Titel den JSON-LD-Block nicht verlassen kann. `<`, `>` und `&` werden im JSON-Inhalt als Unicode-Escapes ausgegeben und beim JSON-Lesen verlustfrei wiederhergestellt.

Build, Check, Originalquellenabgleich und vierzehn Tests einschließlich portablem Neubau bestehen. Dies sind lokale Syntax-, Inhalts- und Einbettungsprüfungen; die anschließend autorisierten externen Ergebnisse stehen unten. `noindex,nofollow` bleibt erhalten. Hilfeseite und separate Skill-Websites erhalten im Rahmen dieser Änderung kein zusätzliches Markup.

English: The local Cookbook homepage now embeds one JSON-LD CollectionPage with an ItemList of its six visible catalog entries. Titles, summaries and ordering come from the same catalog data as the rendered cards. No public identifiers, download availability, prices or ratings are invented. HTML-safe serialization and rendered-content regression tests pass. Public URLs remain omitted, preview noindex remains enabled, and nothing was published. The embedded JSON-LD block was subsequently submitted to both official validators by code input with explicit user authorization.

Browser-Nachweis: Die lokale Startseite wurde neu geladen. Im DOM liegt genau ein JSON-LD-Block vom Typ CollectionPage mit sechs Einträgen; Namen und Beschreibungen stimmen mit allen sechs sichtbaren Karten überein. Der robots-Wert bleibt noindex,nofollow.

Commit-Vorschlag: `feat: generate content-matched cookbook JSON-LD`


## Externe Code-Validierung am 2026-10-15

Mit ausdrücklicher Nutzerfreigabe wurde derselbe unveränderte `<script type="application/ld+json">`-Block aus `site/index.html` in beide offiziellen Code-Eingaben eingefügt. Keine URL-Prüfung, keine erfundene Basis-URL, keine Veröffentlichung, keine Betätigung der Freigeben-Funktion. Der übrige HTML-Seiteninhalt und private Dateien wurden nicht übermittelt. Die erste Ankündigung sprach allgemein von HTML-Code; tatsächlich wurde ausschließlich der eingebettete Script-Block getestet.

| Prüfdienst | Beobachtetes Ergebnis | Bedeutung |
|---|---|---|
| [Schema.org Validator](https://validator.schema.org/) | CollectionPage erkannt, ItemList mit numberOfItems 6 und allen sechs CreativeWork-Einträgen; **0 Fehler, 0 Warnungen** | Das übermittelte Schema.org-Markup besteht die Validatorprüfung |
| [Google Rich Results Test](https://search.google.com/test/rich-results) | Code-Test abgeschlossen, **Keine Elemente erkannt**; keine Rich-Suchergebnisse erkannt | Für dieses CollectionPage/ItemList/CreativeWork-Markup wurde kein unterstütztes Rich-Result-Element erkannt. Kein Rich-Result-Erfolg und kein Schema.org-Syntaxfehler behauptet |

Keine Markup-Änderung nötig. Es werden keine sachfremden Recipe-, Product-, Rating- oder FAQ-Angaben ergänzt, um ein Google-Ergebnis zu erzwingen. Die Codeprüfung ist kein Crawl-/Indexierungsnachweis für die weiterhin lokale noindex-Website.

SHA-256 des geprüften Script-Blocks: `b54ab8ce18eb867cf86b93b0498507520c7dd8a98e58ffeb2ae93563caf3cdbf`.

Die Eingabekopie liegt lokal ignoriert unter `.scratch/launch/validator-input.html`. Beide Ergebnis-Tabs wurden zur Nachprüfung offengehalten; kein Share-Link wurde erzeugt. Google erstellt beim Code-Test technisch eine Ergebnis-ID. Diese ist keine veröffentlichte Cookbook-Seite und wurde nicht als Website-URL in Markup oder Manifeste übernommen.

English: Both official code-input tests were completed using the exact embedded JSON-LD script block. Schema.org reports zero errors and zero warnings. Google reports no detected rich-result items; this is not a general schema validation failure. No extra markup, public URLs, deployment or publication was introduced.

## Review 0.1.3

Der Katalog enthält jetzt sieben sichtbare Einträge. Die sichtbaren Koch-Titel werden als `alternateName` im aus dem Katalog erzeugten JSON-LD ausgegeben; Schema-Vertragstests vergleichen beide Namen und Beschreibung mit den tatsächlichen Karten. Es wurden keine öffentlichen URLs oder IDs ergänzt. Die obigen externen Testergebnisse gelten ausschließlich für den dort gehashten früheren Script-Block mit sechs Einträgen. Das neue Markup wurde anschließend erneut per Code-Eingabe in beiden Validatoren geprüft; Ergebnis und neuer Hash folgen unten.

## Erneute externe Code-Prüfung: sieben Skills und beide Namen

2026-10-15 · Review 0.1.3. Der Schema-Skill wurde erneut angewendet. Beide lokalen Schema-Vertragstests bestehen; Namen, Koch-Titel, Beschreibungen, Anzahl und Reihenfolge stimmen mit den sieben sichtbaren Karten überein. Der exakt eingebettete Script-Block wurde aus der lokalen Browser-Seite übernommen und bytegleich mit der lokalen Eingabekopie abgeglichen. Keine vollständige Website, privaten Quelldateien oder lokalen Pfade übermittelt.

| Code-Test | Beobachtetes Ergebnis | Einordnung |
|---|---|---|
| [Schema.org Validator](https://validator.schema.org/) | CollectionPage mit ItemList, numberOfItems 7 und sieben CreativeWork-Einträgen; **0 Fehler, 0 Warnungen**. Alle sieben `name`- und sieben `alternateName`-Werte sind im Ergebnis enthalten. | Das aktualisierte Markup besteht die Schema.org-Prüfung. |
| [Google Rich Results Test](https://search.google.com/test/rich-results) | Abgeschlossener Code-Test: **Keine Elemente erkannt**. Die Codeansicht zeigt den aktualisierten Block mit sieben Einträgen und alternateName. | Kein unterstütztes Rich-Result-Element erkannt; keine Rich-Result-Eignung oder Suchdarstellung behauptet. |

SHA-256 des exakt geprüften Script-Blocks: `a7a3f4f52f96ddd1208f2f954cb5a2cfcf74a44ea274f924c33172ddedb5272a`. Das Markup wurde nicht verändert. Keine URLs ergänzt, keine Recipe-/Product-/Rating-Angaben erfunden. `noindex,nofollow` bleibt erhalten. Die Website wurde nicht veröffentlicht, nichts eingereicht und die Freigeben-Funktion nicht benutzt. Google erzeugt technisch eine Ergebnis-ID; diese wird nicht zur Cookbook-URL und nicht ins Markup übernommen.

Eingabekopie, Bytegleichheitsnachweis, Ergebnisansichten und zwei Screenshots bleiben lokal ignoriert unter `.scratch/schema-review-013/` bis zur Review-Abnahme erhalten. Beide Ergebnis-Tabs bleiben zur Nachprüfung offen. Die früheren Sechs-Einträge-Ergebnisse oben sind historische Nachweise für ihren damaligen Hash.

English: The exact current embedded JSON-LD was submitted by code input to both official validators. Schema.org reports zero errors and zero warnings, recognizing all seven entries and both name fields per skill. Google completes the test with no supported rich-result items detected. No markup correction, invented URL or publication occurred.
