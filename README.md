# Start It Right

Ein Codex-Skill, der aus einer freien Produktidee einen passenden, direkt
arbeitsfähigen Projektstart macht.

## Produktversprechen

> Idee beschreiben, sinnvolle Bausteine auswählen, arbeitsbereites Projekt
> erhalten.

Der Nutzer erklärt seine Idee in Alltagssprache. Der Skill erkennt Projekttyp,
Reifegrad, Risiken und offene Entscheidungen. Er schlägt passende Module
vorausgewählt vor. Nach der Bestätigung legt Codex nur die benötigten
Projektartefakte an und markiert genau den nächsten ausführbaren Schritt.

## Geplanter Ablauf

1. Idee und vorhandenes Repository verstehen.
2. Produktart, Reifegrad und Vertrauensgrenzen erkennen.
3. Passende Module mit kurzen Begründungen vorschlagen.
4. Reversible, eindeutige Entscheidungen selbst treffen.
5. Materielle Entscheidungen bei Bedarf mit Let Him Grill klären.
6. Nach Bestätigung die ausgewählten Artefakte und Werkzeuge vorbereiten.
7. Mit einem offenen, nicht blockierten Frontier-Ticket enden.

Der Skill soll zuerst brainstormen und Vorschläge zeigen. Der Nutzer muss den
Projektstart nicht jedes Mal neu erklären.

## Flow-Regel

Jede Runde endet mit Empfehlungen. Der Skill nennt mindestens den nächsten
sinnvollen Schritt, passende Module oder Skills und offene Human-Gates. Er
zeigt diese Empfehlungen vorausgewählt als kurze Checkbox-Auswahl. Der Nutzer
kann sie abwählen, muss den Ablauf aber nicht selbst neu planen.

Wenn keine wichtige Entscheidung offen ist, arbeitet der Skill mit dem
kleinsten sicheren Vorschlag weiter. Wenn der Nutzer ein Modul ablehnt, bleibt
der restliche Ablauf erhalten und der Skill empfiehlt den nächsten passenden
Schritt. Bei einem bestehenden Projekt beginnt jede Fortsetzung mit dem ersten
offenen, nicht blockierten Ticket.

## Modul-Katalog

Der Katalog bleibt optional. Die KI wählt aus Signalen der Idee und erklärt die
Empfehlung in einem Satz.

### Produkt und Validierung

- Produktbrief, Zielgruppe, Problem und Produktversprechen
- kleinster nutzbarer Ablauf, Erfolgssignal und Abbruchkriterium
- Wettbewerbs- und Alternativencheck
- Nutzerinterviews oder manueller Validierungstest
- Pricing, Geschäftsmodell und Kostenannahmen
- KPI- oder Messplan, wenn eine Entscheidung Daten braucht

### Planung und Entscheidungen

- MVP-Spec und Out-of-Scope
- versionierte Tickets mit Abhängigkeiten und Akzeptanzkriterien
- private Scratch-Artefakte für vorläufige Recherche
- Let Him Grill für materielle Architektur-, Workflow-, Kosten- oder
  Datenbesitzentscheidungen
- ADR oder kurze Entscheidungsnotiz, wenn eine Entscheidung dauerhaft gilt

### UI, UX und Inhalte

- UX-Flow und sichtbare Zustände
- UI-Vorschläge als Ticket mit Desktop-/Mobile-Screenshots
- Design-Tokens oder `DESIGN.md` nur bei echtem Bedarf
- Accessibility, Tastatur, Fokus, Kontrast und reduzierte Bewegung
- responsive Verhalten, Lade-, Leer-, Fehler- und Erfolgszustände
- i18n als Option: Sprachen, Locale, Datums-/Zahlen-/Währungsformate,
  Textlängen, Pluralformen, Fallbacks und bei Bedarf RTL
- realistische Dummy-Daten für visuelle und redaktionelle Abnahme
- Stop Slop für sichtbare menschliche Texte; Deslopify als tieferer Pass

### Daten, Plattform und Integrationen

- Datenmodell und Source of Truth
- API oder Backend-Vertrag
- Datenbank, Migrationen, Persistenz und Backup
- Authentifizierung, Rollen und Berechtigungen
- externe APIs, Webhooks, Jobs und Benachrichtigungen
- Suche, Filter, Pagination, Uploads und Medienrechte
- Cache oder Offline-Verhalten nur bei nachgewiesenem Bedarf

### Vertrauen, Recht und Sicherheit

- Lizenzwahl passend zu Code, Dokumentation und Medien
- Datenschutz, Impressum, Nutzungsbedingungen und Datenlöschung
- Secret- und Dependency-Prüfung
- Threat Model und Berechtigungsminimierung
- Audit-Log, Aufbewahrung und Export, wenn Nutzer- oder Betriebsdaten entstehen
- Moderation, Missbrauchsschutz und Meldeweg bei öffentlichen Inhalten

Die Lizenz ist eine Entscheidung, keine automatische Voreinstellung. Der Skill
fragt nach Öffentlichkeit, erlaubter Weiterverwendung, Copyleft-Bedarf,
kommerzieller Nutzung und getrennten Assets. Mögliche Kandidaten sind
proprietär, MIT, Apache-2.0, GPL-3.0, AGPL-3.0 oder eine getrennte Lizenz für
Dokumentation und Medien.

### Qualität, Release und Betrieb

- passender Test- und Smoke-Check
- Browser-, Geräte- oder Runtime-Abnahme
- CI und reproduzierbares Packaging
- `CHANGELOG.md`, Versionierung und Tags
- Release Notes aus dem kuratierten Changelog
- Deployment, Health/Readiness, Monitoring, Backup und Rollback
- Support-, Installations- und Diagnoseanleitung

### Distribution und Lernen

- README, Demo, Screenshots und Installationsweg
- GitHub-Projektpflege: Beschreibung, Topics, Lizenz, Support und Release
- Store- oder Marketplace-Material für Extensions und Apps
- SEO und strukturierte Metadaten für öffentliche Websites
- Analytics oder Telemetrie nur mit konkretem Erkenntnisziel und Datenschutz-
  Entscheidung
- Onboarding und Feedbacklog
- begrenzte Launch- und Community-Arbeit nach echtem Nutzungsbeleg

## Produkt-Typ-Module

- **Web-App:** Browser-QA, Accessibility, SEO, Auth, Datenschutz und Deployment.
- **Service:** API-Vertrag, Health, Readiness, Logs, Backup, Restore und Rollback.
- **Browser-Extension:** Manifest, Berechtigungen, Browser-Smoke, Packaging,
  Privacy- und Store-Texte.
- **Agent-Skill:** `SKILL.md`, Installationscheck, Beispiel, Invocation-Smoke,
  portable Artefakte und gegebenenfalls Benchmark.
- **News-/Content-Produkt:** Quellen, Faktenprüfung, Rechte, KI-Kennzeichnung,
  realistische Seed-Texte und Human-Gate vor Veröffentlichung.
- **CLI oder Library:** Installationsweg, API-Vertrag, Kompatibilität und
  reproduzierbare Paketprüfung.
- **Game oder kreative App:** Eingabe-/Spielablauf, Assets, Performance und
  echte Laufzeitabnahme.

## Ticket-Routing

- `.scratch/` enthält private, vorläufige oder wegwerfbare Recherche, rohe
  Belege, verworfene UI-Varianten und lokale Arbeitsartefakte. Der Ordner wird
  nicht versioniert.
- `docs/tickets/` enthält bestätigte, dauerhafte und teilbare Produktarbeit.
- GitHub Issues oder externe Tracker werden nur gewählt, wenn öffentliche oder
  teamübergreifende Zusammenarbeit sie rechtfertigt.
- Ein bestätigter UI-Vorschlag liegt als eigenes Verzeichnis unter
  `docs/tickets/<ticket>/` mit `ticket.md` und relevanten Screenshots unter
  `assets/`.

## Skill-Auswahl

Ein geradliniger kleiner Auftrag braucht keinen Entscheidungsworkshop. Komplexe
Produkt-, Architektur-, Kosten- oder Datenentscheidungen können Let Him Grill
nutzen. Research, Product Design, Browser-QA, Changelog, Secret-Scan und
GitHub-Module werden nur vorbereitet, wenn der Projekttyp sie rechtfertigt.

Diese Auswahl bleibt trotzdem aktiv: Auch wenn ein Modul nicht nötig ist, nennt
der Skill kurz, warum er es überspringt, und empfiehlt den kleinsten sinnvollen
Alternativschritt. Ein „kein Grill nötig“ endet zum Beispiel mit dem nächsten
konkreten MVP-Ticket oder einem kleinen Check.

Der Starter installiert keine Plugins und veröffentlicht nichts ohne
ausgewählte Erlaubnis.

## Projektstand

Das Produktkonzept und der Modul-Katalog sind bestätigt. Der Skill selbst ist
noch nicht spezifiziert oder implementiert.

## Nächster Schritt

Den Ein-/Ausgabevertrag des Skills an drei Fällen entwerfen: einfache Website,
News-/Content-Produkt und Browser-Extension oder Agent-Skill.
