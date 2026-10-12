# Will They Sue Me?

[![Status: experimentell](https://img.shields.io/badge/status-experimentell-f4ce54)](#status) [![Lizenz: MIT](https://img.shields.io/badge/Lizenz-MIT-46644c)](../../LICENSE) · [CI-Workflow](../../.github/workflows/check.yml)

**Ein Rezept vor dem Launch: Prüfe, ob Verhalten, Versprechen und Pflichten deiner App zusammenpassen.**

[English](../../README.md) · [Deutsch](README.de.md)

Ein Agent-Skill für Menschen, die Apps und Websites mit KI bauen. Er prüft relevante Abläufe zu Datenschutz, Verbraucherrechten, Barrierefreiheit und Asset-Lizenzen, findet belegte Lücken und bereitet gezielte Fixes vor. Der Name ist humorvoll. Die Prüfung ist kein Rechtszertifikat und sagt keine Klagen voraus.

## Verwenden

Installation in einen Agenten mit Skill-Unterstützung, etwa Codex. Voraussetzungen: Git, ein Agent, der `SKILL.md` liest, und Zugriff auf das zu prüfende Produkt. Aktuelle Rechtsrecherche braucht Browserzugriff; fehlende Belege werden markiert statt erraten.

```sh
git clone https://github.com/pengusto/will-they-sue-me.git
cd will-they-sue-me
python3 scripts/project.py build
mkdir -p ~/.codex/skills
cp -R dist/skill ~/.codex/skills/will-they-sue-me
```

Solange das Repository privat ist, brauchst du Zugriffsrechte. Der Build benötigt Python 3.11+. Existiert das Ziel bereits, prüfe es vor dem Kopieren. Alternativ nach Veröffentlichung das ZIP der Landingpage herunterladen und entpacken. Falls nötig die Skill-Erkennung des Agenten neu laden.

```text
Prüfe mit $will-they-sue-me diese App vor dem Launch.
Zielmarkt: Deutschland/EU. Sie verkauft Abos an Verbraucher.
Zeige anwendbare Checks, Belege, Lücken und konkrete Abnahmeprüfungen.
```

Fixes ausdrücklich beauftragen. Eine Prüfung erlaubt keine beliebigen Änderungen oder Produktionsaktionen. Andere kompatible Agenten können `SKILL.md` direkt laden; ihre Kompatibilität wurde nicht separat getestet.

## Das Rezept

1. **Zutaten:** Betreiber, Märkte, Geschäftsmodell, Zielgruppe, Code/Konfiguration und zugängliche Abläufe.
2. **Prüfen:** Tatsächliche Datenflüsse, Einwilligung, Checkout, Aussagen, Barrierefreiheit und Asset-Herkunft mit anwendbaren Pflichten vergleichen.
3. **Abschmecken:** Findings mit Belegen, aktuellen Primärquellen, Fixes und beobachtbaren Abnahmekriterien.
4. **Servieren:** Beauftragte Fixes verifizieren und verbleibende Unklarheiten nennen.

Die Ausgabe trennt bestätigte Findings, fehlende Belege, begründete Nicht-Anwendbarkeit und Checks mit benanntem Umfang. Die Prüfliste deckt zwanzig Bereiche ab, ohne zwanzig neue Funktionen zu verlangen. Banner, AGB, Einwilligungsboxen oder Altersabfragen werden nicht automatisch ergänzt.

## Beispiel-Finding

> **Launch-Blocker — Analytics vor Einwilligung:** Die App lädt ein nicht notwendiges Analytics-SDK vor der Auswahl. Belege: Initialisierung im Code und beobachteter Netzwerkverkehr. Fix: Initialisierung bei entsprechender Anwendbarkeit sperren; frische Sitzungen vor Auswahl, nach Ablehnung, Zustimmung und Widerruf prüfen. Rechtsgrundlage und Anwendbarkeit brauchen aktuelle Recherche zum Zielmarkt.

Das ist ein Beispielszenario, keine Aussage über dieses Repository oder deine App.

## Entwickeln und Vorschau

Python 3.11+; keine Laufzeitpakete, kein Frontend-Framework und kein JavaScript-Paketmanager nötig.

```sh
python3 scripts/project.py check
python3 scripts/project.py build
python3 -m http.server 4173 --directory dist/preview
```

`http://localhost:4173/will-they-sue-me/` öffnen. Die Vorschau prüft den echten Projekt-Unterpfad, Skill-Download und Dokumentationslinks. Das Paket enthält nur Skill-Anweisungen, Referenzen, UI-Metadaten und MIT-Lizenz. Quellen: `SKILL.md`, `agents/`, `references/`; Website: `site/`; generierte Ausgabe: ignoriertes `dist/`.

## Veröffentlichung

Das Repository soll während der Maintainer-Prüfung privat bleiben. GitHub Pages ist vorbereitet, aber weder aktiviert noch deployed. Der Pages-Workflow startet ausschließlich manuell mit ausdrücklicher Veröffentlichungsbestätigung. Ein Push veröffentlicht die Website nicht. Er baut selbst und deployt nur Website-Dateien. Vor dem Start Pages auf GitHub Actions konfigurieren und die Sichtbarkeit prüfen.

Ein privates Repository garantiert keine private Pages-Website; siehe [GitHubs Dokumentation](https://docs.github.com/en/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site). Nach freigegebenem Deployment ist die erwartete öffentliche URL `https://pengusto.github.io/will-they-sue-me/`; derzeit ist sie kein Live-Demo-Link.

## Status

Experimentelle erste Version. Struktur-/Paketchecks und dokumentierte Verhaltensszenarien sind von unabhängigen Agentenprüfungen und Live-Produktprüfungen zu unterscheiden. Siehe [Prüfszenarien](../behavior-checks.md) und [Maintainer-Übergabe](../review.md). Es wird keine vollständige Rechtskonformität oder Barrierefreiheit zugesichert.

Für Änderungen ein Issue mit reproduzierbarem Szenario und erwartetem Verhalten oder einen fokussierten Pull Request erstellen. Keine personenbezogenen Daten oder Zugangsdaten in Issues aufnehmen. Englisch und Deutsch werden gemeinsam gepflegt; die deutsche Fassung ist KI-unterstützt und wurde nicht unabhängig sprachlich geprüft.

## Lizenz

[MIT](../../LICENSE) für eigenen Code, Dokumentation und Skill-Anweisungen. Verlinkte Gesetze, externe Dokumentation und Drittprodukte behalten ihre eigenen Bedingungen. MIT gewährt keine Rechte an fremden Assets und keine rechtliche Freigabe für geprüfte Apps.
