# Offenes Kochbuch als öffentliche Startseite

Stand 2026-10-23, lokal umgesetzt. Die gewünschte Landingpage ist die offene Kochbuchansicht aus `ui/book.html`, nicht das README-Banner und nicht die bisherige separate Marketingseite. Die README-Illustrationen bleiben dort. Diese Zielunterscheidung verhindert, dass eine Änderung am falschen Einstieg umgesetzt wird.

## Seiten im Buch

Mit **Zutaten** waren in der Gestaltung Lebensmittel-Bilder gemeint, keine neu erfundenen Textlisten und keine Navigationsicons. Jede der 17 Buchseiten hat deshalb einen eigenen gemalten Gericht-und-Zutaten-Bildsatz: 14 Workflows plus Willkommen, Installation und Über Cookbook. Die zusätzlichen Text-Zutatenlisten auf den drei Informationsseiten sind durch vier passende Zutatenbilder ersetzt; die tatsächlichen Installationsvoraussetzungen bleiben ausdrücklich lesbar. Die funktionalen vier Zutaten pro Workflow aus `ui/locales.json` bleiben erhalten und werden durch die jeweils passenden Lebensmittelbilder begleitet. Die Zubereitungsschritte verwenden ebenfalls den eigenen Bildsatz statt des gemeinsamen Knoblauch/Kräuter/Löffel-Bogens. Diese Bedeutungsunterscheidung vor weiteren Änderungen beibehalten.

- **Willkommen** ist der Einstieg ohne Rezept-Fragment: Nutzen, Zielgruppe, drei Einsatzmomente, Anzahl der Workflows, Hosts, Version, Beta und Lizenz.
- **Installation** ist eine eigene Doppelseite. Host-Schalter zeigt Codex oder Claude Code, Namensschalter wählt hier auch das tatsächliche Paket und die passenden Aufrufe. Befehle und erster Aufruf lassen sich kopieren; bei fehlender Clipboard-Berechtigung werden sie zur manuellen Kopie markiert. Updates, Variantenwechsel, Voraussetzungen und Prüfsummen bleiben erreichbar.
- **Über Cookbook** enthält Projekt/Feedback, MIT, Beta-Grenzen, Datenschutz und Verweise auf die öffentlichen Rechtstexte.
- Die **14 Rezeptseiten** behalten Illustrationen, Aufrufe, Zubereitung, Grenzen, Sprach-/Theme-Schalter und Seitenwechsel. Direkte Fragmente öffnen ihr Rezept; Plain-Fragmente wählen auch Plain als Namenswelt.
- Der Installieren-Link bleibt auf Desktop im festen Inhaltsverzeichnis, auf kleinen Bildschirmen als fester Button am unteren Rand erreichbar.

Papiercreme, Weinrot, Serifenschrift und Buchfalz bleiben erhalten; Texturen und Navigation sind auf der öffentlichen Ansicht ruhiger. Die neue Rahmenstruktur wird nur in den Website-Export eingesetzt. Die offline verfügbare MCP-Ansicht behält ihren direkten Rezepteinstieg und ihre installierte Aufruf-ID. Lenis ist als versionierte lokale Bibliothek eingebunden; keine aktive Codex-Installation wurde ersetzt.

## Routen und Sprachen

`index.html` (DE) und `index-en.html` (EN) öffnen das Kochbuch. `kitchen.html`, `kitchen-en.html` und `cookbook.html` bleiben Buch-Einstiege mit Canonical auf die passende neue Startseite. `cookbook-plain.html` bietet die Plain-Variante. Ausführliche bisherige Installationsübersichten werden als `install.html`, `install-en.html`, `install-plain.html`, `install-plain-en.html` generiert. Die ursprünglichen Quelltemplates bleiben dafür gepflegt; URLs in den Übersichten werden vom Builder erzeugt.

Willkommen, Installation und Projektinformationen sind DE/EN; die Rezeptoberfläche behält ihre zwölf Sprachen. Die jeweilige Sprache der Projektseiten ist explizit angegeben. Ohne JavaScript sind die Informationsseiten und eine vollständige Rezeptliste mit Zusammenfassungen und Installationslink lesbar. Keine externen Laufzeitanfragen, Cookies oder Tracking.

## Strukturierte Daten

Jeder öffentliche Bucheinstieg erhält JSON-LD als `CollectionPage` mit `ItemList` und 14 `CreativeWork`-Einträgen aus demselben Katalog wie die sichtbaren Rezepte. Namen und Zusammenfassungen werden bei einem Wechsel der Rezept-Sprache oder Namenswelt mitgeführt. Der statische Inhalt enthält passende Rezeptlinks und einen lesbaren No-JavaScript-Katalog. Installations- und Projektseiten zählen nicht als zusätzliche Skills. Canonical und DE/EN-Alternativen zeigen auf die neuen Bucheinstiege; die Sitemap enthält diese und die Installationsübersichten.

Kein `Recipe`, kein erfundenes Produktangebot, keine Bewertungen und kein Rich-Result-Versprechen. Typen und Inhaltsregeln anhand von [Schema.org CollectionPage](https://schema.org/CollectionPage), [ItemList](https://schema.org/ItemList) und [Google-Richtlinien](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) abgeglichen. Lokale Vertragsprüfungen ersetzen keine externe Validator- oder Search-Console-Abnahme.

## Lokale Verifikation

Build, Check, check-sources, 37 Unit-Tests und portabler Neubau mit identischen Artefakt-Hashes bestanden. Browser: Willkommen/Installation/Über, Codex-/Claude-Wechsel, Plain-Paket und erster Aufruf, Clipboard-Erfolgsmeldung, direkte Plain-Rezeptlinks einschließlich Neuladen, synchronisierte JSON-LD-Namen und englischer Einstieg geprüft. Helle und dunkle Doppelseiten visuell geprüft; bei 320 CSS-Pixeln kein horizontaler Überlauf und fester Installieren-Button im Viewport. Keine Browser-Konsolenfehler beim geprüften englischen Einstieg. Sichtnachweise liegen lokal unter `.scratch/open-book-home-review/`. Kein Push, Deployment, Store-Upload oder Austausch einer aktiven Host-Installation. Keine erneute externe Validator-Einreichung.

## Scrollen und Blättern · 2026-10-24

Auf Desktop oberhalb 850 CSS-Pixeln blättert ein bewusstes vertikales Scrollen über dem Papier am Dokumentende weiter, am Anfang zurück. Lange Seiten werden zuerst innerhalb ihrer Papierseite gelesen; der Desktop-Buchrahmen bleibt fest auf Fensterhöhe. Reihenfolge: Willkommen, Installation, 14 Rezepte, Über Cookbook; die lokale MCP-Ansicht blättert nur durch ihre Rezepte. Seitenauswahl und Tastaturbedienung bleiben zusätzlich verfügbar. Auf kleinen Bildschirmen bleibt natives Scrollen erhalten.

Durchgehendes Scrollen kann weitere Seiten drehen: mindestens 650 ms Abstand und erneut ausreichend Bewegung nach dem Wechsel. Während der Animation oder Wartezeit wird keine Bewegung für einen späteren Wechsel gesammelt. Schwacher Trackpad-Nachlauf unter 12 Pixeln pro Ereignis wird nach einem Wechsel ignoriert. Nach 220 ms ohne Ereignis beginnt eine neue Geste. Kleine Bewegungen unter dem akkumulierten Schwellwert lösen keinen Wechsel aus. Horizontale Gesten, Scrollbereiche, Eingaben und Zoom-Modifikatoren werden respektiert. Am ersten/letzten Buchblatt gibt es keinen Umlauf.

Lenis 1.3.27 glättet das Scrollen auf Desktop lokal, ohne CDN. Die dokumentierten Optionen `autoRaf`, `syncTouch: false`, `respectReducedMotion` und ein Filter für Cover/Dialoge/Eingaben erhalten native Touch- und Kontrollbedienung. Unter 851 Pixeln oder mit reduzierter Bewegung wird die Lenis-Instanz entfernt. Quelle und Lizenz unter `assets/vendor/lenis/`. Primärdokumentation: [Lenis v1.3.27](https://github.com/darkroomengineering/lenis/tree/v1.3.27).

Der Blättereffekt wurde vereinfacht: Die echten Papierhälften werden in zwei kurzen Phasen (je 140 ms) bewegt. Keine geklonten DOM-Seiten, keine kopierten berechneten Styles und keine zusätzliche Overlay-Ebene. Anime.js übernimmt die Papierbewegung, Lenis die Scrollposition; reduzierte Bewegung und direkte Navigation können den Wechsel abbrechen.

44 Tests einschließlich Verhaltenstests der Gestenerkennung und portabler Neubau bestanden. Die JS-Gestentests nutzen optional ein bereits installiertes Node.js, sonst werden sie als ausgelassen ausgewiesen; Build und Laufzeit benötigen kein zusätzliches Paket. Die anfängliche Browser-Ursprungssperre wurde nach ausdrücklicher erneuter Freigabe durch den Nutzer überwunden; aktuelle Sichtnachweise stehen unten. Keine Aussage über visuelle Abnahme oder eine geänderte aktive Codex-Installation.

## Gerichte und Zutatenbilder · 2026-10-24

`assets/cookbook/food/` enthält 17 individuelle transparente WebP-Bildbögen, zusammen rund 1,3 MB. Jeder Bogen enthält ein Gericht und vier dazu passende Lebensmittel. Unter `cutouts/` liegen zusätzlich 85 eigenständige quadratische WebP-Dateien: je ein vollständiges Gericht und vier einzelne Zutaten. Die gemalten Formen wurden anhand der Alpha-Silhouetten getrennt, samt halbtransparenten Rändern und losen Krümeln, anschließend mit transparentem Sicherheitsrand zentriert. CSS zeigt jedes Quadrat mit `background-size: contain`; unterschiedliche Bildproportionen werden nicht mehr durch verzerrte Sprite-Boxen abgeschnitten. Die ursprünglichen Bildbögen bleiben erhalten. Die Bildflächen haben pro Seite eigene CSS-Variablen, auch die kleinen Bilder neben den Zubereitungsschritten. Motive: Shakshuka, Risotto, Minestrone, Lachs im Pergament, Wellington, Zitronentarte, Poke Bowl, Lasagne, Zwiebelsuppe, Linseneintopf, Gnocchi, Bruschetta, Ramen, Mezze, Ravioli und Gemüsetarte.

Erzeugt mit dem eingebauten `image_gen`; Original-PNGs bleiben im ursprünglichen Generierungsverzeichnis erhalten. Die Sammelbögen wurden mit vorhandenem `cwebp` kodiert, die isolierten Quadrate einmalig mit Pillow aus dem vorhandenen Workspace-Runtime erstellt. Build und portable Distribution benötigen weiterhin nur die Python-Standardbibliothek. Quellen, Motiv-/Promptangaben, SHA-256 der Originale und Runtime-Dateien sowie historische Ausschnitt-Rechtecke, neue Freistellmethode, quadratische Maße und Prüfsummen aller Einzelbilder sind in `assets/cookbook/food/SOURCES.json` festgehalten. Die vorhandenen älteren Motive bleiben erhalten. Die Bilder sind Kochbuch-Metaphern zu Coding-Workflows, keine echten Kochanleitungen; JSON-LD bleibt deshalb eine Workflow-Sammlung. Alle 17 Bildbögen wurden visuell geprüft. Die aktuelle Browserabnahme für Desktop und Handy steht unten. 44 Tests und portabler Neubau bestehen.

## Kompakte Seiten und Bildplatzierung · 2026-10-24

Gericht und Beschriftung stehen gemeinsam im normalen Seitenfluss; der Name ist unter dem Bild zentriert. Die Navigation hat gleich große Pfeilspalten und eine mittige, tabellarische Seitenzahl; der gesamte Blätterbereich sitzt mittig unter der rechten Seite. Unter 851 Pixeln wird das Gericht direkt unter den Titel und den Alternativnamen auf die erste Seite versetzt. Zutaten stehen in zwei Spalten, auf kleinen Bildschirmen mit größeren Bildern über dem Text. Die Informationsseiten verwenden mobil ebenfalls zwei Zutaten pro Reihe.

Bis 900 Pixel Fensterhöhe werden Desktop-Abstände, Überschriften und Bildhöhen kompakter. Auf Desktop ab 851 Pixel Breite hat der Buchrahmen eine feste Höhe von `100dvh`; das Dokument selbst scrollt nicht. Die beiden Papierseiten sind auf die verfügbare Höhe begrenzt und scrollen nur bei echtem Inhaltsüberlauf intern. Lange Übersetzungen, aufgeklappte Grenzen und sehr niedrige Fenster bleiben dadurch erreichbar. Am Inhaltsrand blättert die Scrollgeste weiter. Lenis greift nicht in die nativen Scrollbereiche der Papierseiten ein. Vorwärts startet die neue Seite oben, rückwärts an ihrem Ende; direkte Auswahl startet oben. Mobil und ohne JavaScript bleibt der normale Dokumentfluss erhalten. Lehre aus dem vertikalen Springen: Eine Mindesthöhe allein begrenzt weder lange Inhalte noch den Dokument-Scrollbereich. Layoutregression vermeiden: keine neuen rechteckigen CSS-Sprite-Ausschnitte; Einzelbilder quadratisch und mit Rand liefern. Die 44 Tests prüfen unter anderem Bildmaße/Hashes, fortgesetztes Blättern, Nachlauf, Animation, lange Seiten und die internen Lesepositionen beim Richtungswechsel. Aktuelle visuelle Stichproben und Grenzen stehen unten.

## Gesamtfeinschliff · lokale 0.6.0

Ziel: Das offene Kochbuch bleibt der öffentliche Einstieg; Papier, Weinrot, Serifenschriften, Falz und individuelle Gerichtbilder bleiben erhalten. Qualitätsmaßstab: vollständige Inhalte und echte Installation, klarer Skill-Zweck, passende DE/EN-Daten, kein abgeschnittenes Bild, festes Desktop-Buch mit zugänglichem Überlauf, native mobile Bedienung, offline eigenständige Pakete und ehrliche Prüfgates. Gerenderte Browserabnahme nach erneuter Nutzerfreigabe durchgeführt; zusätzliche Geräte, Browser und alle zwölf Übersetzungen sind dadurch nicht vollständig visuell abgenommen. Code- und Paketprüfung allein ersetzt die Browserabnahme nicht.

0.6.0 ergänzt You Got This / You’re the Chef als vierzehnten Workflow mit Paella und vier eigenständigen Zutatenbildern, allen zwölf UI-Sprachen und beiden Host-/Namensvarianten. Originalskill und Lizenzherkunft bleiben nachvollziehbar; alte Repo-/Host-Installationen werden nicht verändert. Schema.org beschreibt die vierzehn Coding-Workflows als CollectionPage/ItemList/CreativeWork, siehe [aktueller Schema-Prüfstand](structured-data.md).

Unabhängige Codekritik fand und korrigierte drei Integrationsfehler: Die kopierten Skill-Aufrufe folgen jetzt dem gewählten Host; statische Infoseiten behalten ihre DE/EN-Sprache und LTR-Richtung trotz anderer Rezeptsprachen; Hilfeseiten übernehmen Version und Anzahl aus dem Build und führen Plain zur richtigen Installation. Regressionstests halten diese Grenzen fest. Die anfängliche Browser-Zugriffssperre wurde respektiert; der erneute Zugriff erfolgte erst nach ausdrücklicher Nutzerfreigabe.

## Gerenderte Browserabnahme · 2026-10-24

Nach ausdrücklicher Nutzerfreigabe wurde die laufende Vorschau auf Port 8768 im In-App-Browser neu geladen. Sie zeigt 14 Workflows und Beta 0.6.0. Die vorherige Zugriffssperre ist für diese freigegebene Prüfung überwunden. Temporäre Viewport-Overrides wurden anschließend zurückgesetzt; Deutsch, Klartext und die Willkommen-Seite wurden wiederhergestellt.

| Geprüfte Ansicht / Ablauf | Beobachtetes Ergebnis |
|---|---|
| 1280 × 720 CSS-Pixel, alle 14 Kitchen-Rezepte auf Deutsch | Dokumenthöhe 720, beide Papierseiten ohne Überlauf; keine vertikale Bewegung des Rahmens |
| 1440 × 900 CSS-Pixel, You’re the Chef | Dokumenthöhe 900, kein Überlauf auf beiden Seiten |
| 390 × 844 CSS-Pixel | Kein horizontaler Überlauf; Zutaten zweispaltig; Gericht direkt unter Titel; natives Dokument-Scrollen |
| Willkommen bei 1280 × 720 | Beide Papierseiten passen ohne Überlauf; Zutaten vollständig sichtbar |
| Fortgesetzte echte Scrollimpulse | Mehrfaches Weiterblättern, unter anderem 01 → 02 → 03 → 04; Dokument-Scrollposition blieb 0 |
| Aufgeklappte Grenzen | Rechte Papierseite scrollt intern; Dokumenthöhe und Rahmen bleiben unverändert |
| Claude Code → Rezept | Erstaufruf und Rezept verwenden `/cookbook-by-pengusto:`; Auswahl ändert keine Installation |
| Arabisch auf deutscher Infoseite | Dokument bleibt `lang=de`, `dir=ltr`, JSON-LD `inLanguage=de`; danach Deutsch wiederhergestellt |

Dabei wurden echte Layoutfehler korrigiert: ältere `.public-book .hero-illustration`-Regeln überstimmten die neueren allgemeinen Höhenregeln; der Rezeptindex hatte eine Mindesthöhe, die Projektlinks unter den festen Rahmen drückte. Die adaptiven Regeln berücksichtigen jetzt die öffentliche Ansicht ausdrücklich, der Index darf kleiner werden. Aufrufkarten haben kurze Überschriften und kompakte Abstände. Nach dem Wechsel von Handy zu Desktop bleibt das ausgewählte Rezept im Inhaltsverzeichnis sichtbar.

Lehre: Bei visuellen Größenkorrekturen die tatsächlich berechnete Höhe im öffentlichen Layout prüfen, einschließlich Selektorspezifität und Mindesthöhen der Geschwister. Quellenprüfung allein belegte diese Fälle nicht. PNG-Sichtnachweise bleiben lokal ignoriert unter `.scratch/browser-review-0.6.0/` erhalten. Dies ist eine lokale Browserprüfung, kein Deployment-, Store- oder vollständiger Geräte-/Übersetzungsnachweis.

## Pflege

Gemeinsame Quellen: `ui/book.html`, `ui/book.js`, `assets/sidebar.css`; öffentliche Zusatzseiten: `ui/public-pages.html` und `ui/public-locales.json`. `scripts/cookbook.py` setzt den Export zusammen. Generierte Dateien nie von Hand pflegen. Die folgenden Abschnitte sind historische Entwurfs- und Prüfstände.

---

## Historischer grün-weißer Entwurf

Stand 2026-10-16, lokal vorbereitet. Grundlage ist der vom Nutzer ausgewählte Chef’s-Table-Entwurf, nicht die vorherige Sanji-Variante.

## Inhalt und Bedienung

- Weiß, Waldgrün (#112e23), kontrastreiches Orange (#bd470a), Systemschriften, eigenständiges Kochbuchmotiv mit Pfanne und Ei.
- Vier statische Ansichten: index.html und kitchen.html auf Deutsch; index-en.html und kitchen-en.html auf Englisch. Hilfe ebenfalls DE/EN.
- Sprache und Namenswelt sind unabhängig. Beide Wechsel erhalten die jeweils andere Auswahl. Kein JavaScript, Cookie oder externer Übersetzungsdienst nötig.
- Pro Seite sieben sichtbare Titel und Zusammenfassungen, native aufklappbare Details mit Grenzen, stabilem Aufruf und Einzel-Download.
- Host-Downloads, tatsächliche CLI-Befehle, Variantenwechsel, Updates, Lizenz und lokale Datenschutz-/Release-Hinweise enthalten.
- Skill-Anleitungen und Laufzeitquellen bleiben unverändert; nur die Website ist übersetzt. Englische Erläuterungen unter templates/locales.json, deutsche Skill-Felder weiterhin aus catalog.json.

## Downloadkorrektur

Bisher enthielten Host-ZIPs nur den Plugin-Ordner. Für die auf der Landingpage gezeigte lokale Marketplace-Installation enthalten sie jetzt cookbook-by-pengusto/<Marketplace-Manifest> und cookbook-by-pengusto/plugins/cookbook-by-pengusto/<Plugin-Dateien>. Nach dem Entpacken im äußeren Ordner registrieren. Keine Änderung der Plugin-ID, Skill-IDs oder Workflow-Logik. Einzel-ZIPs unverändert.

## Umsetzung und Nachweise

Gemeinsames HTML-Template, templates/locales.json und assets/site.css. Sidebar-Styles liegen separat in assets/sidebar.css, damit die Website-Umgestaltung die eingebettete Ansicht nicht verändert.

19 Tests, Paket-/Quell-/Linkprüfungen und portabler Neubau mit identischen Hashes bestanden. Der neue ZIP-Test entpackt alle vier Host-Varianten, löst den Marketplace-Pfad auf und vergleicht die Plugin-Dateien bytegenau mit der gemeinsamen Quelle. Entpackte Claude-Pakete bestehen die native Manifestvalidierung. Vorhandene aktive Installationen wurden nicht geändert.

Browser: Desktop und schmale mobile Ansicht geprüft, Sprachwechsel und Namenswechsel erhalten die jeweilige Auswahl, Details zeigen die richtigen Aufrufe und Downloadnamen. JSON-LD beschreibt pro Seite genau die sieben sichtbaren Titel und Beschreibungen, inLanguage entspricht der Website. Keine öffentlichen Ziele erfunden. Die früheren offiziellen Validator-Nachweise gelten für ihre dokumentierten Payloads; der neue englische Block wurde bisher lokal geprüft.

Bild: assets/cookbook-hero.jpg, mit eingebautem Imagegen erzeugt, als JPEG für die Website exportiert. Kein Screenshot als Website, sondern HTML/CSS und separates Motiv. Das Kochbuch ist Illustration, kein physisches Verkaufsprodukt. PNG-Original und Prompt/Nachweise lokal unter .scratch/landing-review erhalten; zusätzlich bleibt das erzeugte Original im Imagegen-Verzeichnis erhalten. Aufbewahren bis zur Design-Abnahme. Temporäre ZIP-Testentpackungen wurden nach Prüfung entfernt.

Keine öffentliche Veröffentlichung, kein Deployment, keine Store-Einreichung. noindex,nofollow bleibt aktiv. Vollständige Desktop-Workflow-Abnahme, öffentliche Ziele, Hosting-/Rechtsseiten und Stores bleiben Release-Gates.

## Referenzkorrektur 2026-10-17

Größeres Portraitmotiv anhand des ausgewählten Originalentwurfs, kräftigere CTA-Flächen, Download-/Buch-Buttons, Kochmütze/Sprechblase und nummerierte Skill-Zeilen. Lokal eingebundene Tabler-Outline-Icons mit MIT-Lizenz unter assets/icons; keine externen Laufzeitanfragen. Browser-Cache-Version für CSS und Hero, lokale Linkprüfung berücksichtigt Query-Parameter. Beide Sprachen und Namenswelten verwenden dieselben Komponenten. Produktbeschreibungen bleiben belegbar aus dem Katalog statt weitergehender Aussagen des Bildentwurfs. Das bisherige Hero bleibt lokal unter .scratch/landing-review/cookbook-hero-before-reference-alignment.jpg bis zur Design-Abnahme erhalten.

GitHub: vorheriger vollständiger Stand 8ff03a4 privat gepusht. Diese nachfolgende Designkorrektur bleibt lokal zur Abnahme.

### Skill-Symbole verfeinert

Die sieben Listenmotive verwenden jetzt filigrane Lucide-Outlines mit 1,5 statt 2 Strichstärke: Klemmbrett, Kochtopf, Schloss, Lupe, Servierglocke, Notizliste, offene Tür. Zuordnung der Motive und unveränderte Original-Lizenzen unter assets/icons/README.md und LUCIDE-LICENSE. Bisherige Symbole lokal unter .scratch/landing-review/icons-before-refinement bis zur Abnahme behalten. Buttons und restliche Gestaltung unverändert.

## Dark Mode und öffentliche Source-Beta

Systemeinstellung über prefers-color-scheme; helle Logos und separates dunkles Hero-Bild. Keine Cookies, externen Dienste oder Theme-Skripte. Landingpages und Hilfe in DE/EN unterstützen beide Farbschemata. Browserprüfung verwendet isolierte, ignorierte Testkopien mit erzwungenem Medienzweig, weil die verfügbare Browser-API keine Farbschema-Emulation anbietet; die Produktionsdateien behalten den echten System-Media-Query. Beide Hintergründe, Bilderauswahl, aufklappbare Details, fehlende Bilder und horizontale Überläufe wurden geprüft, einschließlich 320 CSS Pixel.

Die frühere Aussage „keine Veröffentlichung“ bezieht sich auf den damaligen Stand. Öffentlich freigegeben ist jetzt die GitHub-Source-Beta, keine Website oder Store-Einreichung.

## Transparenter Hero · 2026-10-17

Das freigestellte Motiv assets/cookbook-hero-transparent.png ersetzt die beiden JPEGs im Website-Export. Echtes Alpha statt eingebautem weißem oder dunklem Hintergrund; alle vier Landingpages verwenden dieselbe Grafik. Die Original-JPEGs bleiben als Quellen erhalten. Cache-Version berücksichtigt die transparente Grafik. Erstellt per eingebautem Imagegen, Bearbeitungsauftrag: Hintergrund und Boden entfernen; Buch, Schrift, Register, Pfannen, Eier, Petersilie und Tuch unverändert erhalten; saubere Kanten ohne weißen Saum.

### Markup-Nachprüfung vor dem GitHub-Push

2026-10-17: Plain und Kitchen jeweils auf DE/EN lokal erneut geprüft. CollectionPage → ItemList → sieben ListItem/CreativeWork: Namen, Beschreibungen, Reihenfolge und Sprache entsprechen dem gerenderten Inhalt. Keine unsichtbaren alternativen Namen, erfundenen URLs, Bewertungen, Angebote oder Produktbehauptungen. Das transparente Markenmotiv wird nicht als physisches Produkt ausgezeichnet. JSON-LD bleibt unverändert. Aktuelle Schema.org-Typdefinitionen und Google-Richtlinien abgeglichen; keine erneute Code-Eingabe in externe Validatoren in diesem Durchlauf. Kein Rich-Result-Versprechen. Vollständiger lokaler Launch-Check mit 22 Tests und portablem Neubau bestanden. Der Builder entfernt nur veraltete generierte JPEG-Kopien, die Originale unter assets bleiben erhalten. GitHub-Push freigegeben; Website-Deployment weiterhin nicht freigegeben.

Referenzen: https://schema.org/CollectionPage · https://schema.org/ItemList · https://developers.google.com/search/docs/appearance/structured-data/sd-policies
