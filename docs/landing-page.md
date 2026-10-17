# Landingpage: grün-weißer Entwurf

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
