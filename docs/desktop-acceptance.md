> **0.5.0 publication:** thirteen workflows; current install, website and Store boundaries: [publication.md](publication.md). Earlier acceptance results below are version-specific historical evidence.

> **Abnahme 0.4.0 abgeschlossen (2026-10-22):** zwölf Skills nativ synthetisch geprüft; Nutzer bestätigt alle zwölf im Desktop-Picker und funktionierenden Abschluss-Guide. Exaktes Upload-ZIP erneut gescannt. Store-Zugang scheitert aktuell an der Identitätsprüfung; veröffentlichte vollständige Datenschutzerklärung fehlt. [Finaler Bericht](final-acceptance-0.4.0.md). Nichts hochgeladen oder veröffentlicht.

> **Aktueller lokaler Stand 0.4.0 (2026-10-22):** zwölf Kitchen-Skills installiert und in frischen Codex-Sitzungen erkannt; vier neue Aufrufe verhaltensgeprüft. Sidebar 0.4.1 aktualisiert, vorherigen deaktivierten Zustand erhalten. [Aktueller Installations- und Abnahmebericht](skill-installation-0.4.0.md). Frühere Nachweise unten bleiben historisch; keine Veröffentlichung.

# Aktuelle Kitchen-Abnahme · 2026-10-22

Die aktuelle lokale Installation von Cookbook Kitchen 0.3.1 stimmt nach nativer Neuinstallation in allen 42 Dateien mit dem vorbereiteten Store-ZIP überein. Eine neue native Codex-CLI-Sitzung erkennt und liest alle acht Skills; acht begrenzte synthetische Szenarien bestehen. Der Nutzer hat anschließend bestätigt: „Alle acht sichtbar; Abschluss-Guide funktioniert.“ Damit ist die sichtbare Kurzabnahme als Nutzerbeobachtung erfasst. Die Computersteuerung verweigert weiterhin den direkten Zugriff auf Codex; keine eigene visuelle Beobachtung oder umfassende UI-Abnahme behauptet.

Vollständiger Prüfstand, Paket-Hash, Grenzen und Einreichungsblocker: [Kitchen Store Acceptance](store-acceptance-2026-10-22.md).

In einer neuen lokalen Codex-Sitzung Cookbook auswählen. Erwartete Kitchen-IDs: `prep-the-kitchen`, `are-we-cooking`, `what-was-i-cooking`, `keep-the-recipe-secret`, `can-i-serve-this`, `ready-to-serve`, `whats-new-on-the-menu`, `close-the-kitchen`. Keine parallele Plain-Installation hinzufügen. Die Sidebar gehört nicht zur Store-Abnahme dieses Skill-Pakets.

Sichtbare Kurzprobe: `$close-the-kitchen` mit „Nur Abschluss-Guide: Zwei Links sind repariert, der relevante Test ist grün. Nichts ändern, archivieren oder veröffentlichen.“ Erwartet: begrenzter Abschluss auf Grundlage der mitgeteilten Beobachtungen, keine neuen Aufgaben oder externen Aktionen. Sichtbarkeit, Host-Version und Ergebnis festhalten; bei Fehlern die genaue Meldung ohne Zugangsdaten dokumentieren. Icons im tatsächlichen Picker auf Erkennbarkeit prüfen; ein CLI-Test belegt das nicht.

English: Kitchen is the selected store variant. All 42 installed files match the upload ZIP; a fresh native CLI session discovered/read all eight skills and passed bounded synthetic scenarios. The maintainer subsequently confirmed all eight visible skills and a working closing guide; this is user-reported short acceptance. Computer use still denies direct access to Codex. Check the eight Kitchen IDs and the guide-only closing scenario in a fresh local desktop session, and record actual UI results. Do not publish.

---

> **Historischer Prüfstand 0.1.x.** Die aktuelle Architektur, Namenswelten und Installationswege stehen in [consolidation.md](consolidation.md) und der [README](../README.md). Frühere Testergebnisse werden nicht als neue 0.2.0-Abnahme behauptet.

# Lokale Desktop-Abnahme / Local desktop acceptance

Review 0.1.4. Beide nativen CLI-Installationen und 7/7 Lade-Tests bestehen. Für die angeforderte sichtbare Abnahme sind jetzt beide Plugins aus den stabilen lokalen dist-Ausgaben installiert und aktiviert: Codex im lokalen Host, Claude Code im Benutzerprofil. Beide Installationscaches stimmen vollständig mit den geprüften finalen ZIPs überein. Diese Registrierungen bleiben für die Nutzerprüfung erhalten. Nichts veröffentlicht. Diese Anleitung ist für die noch offene sichtbare Nutzerabnahme. Sie behauptet keine geprüften Menübezeichnungen oder Desktop-Ergebnisse.

## Codex

Bereits ausgeführt. Bei einer späteren Neueinrichtung vom Cookbook-Projektordner aus:

```sh
codex plugin marketplace add ./dist/codex
codex plugin add vibe-coding-cookbook@cookbook-local
```

Codex neu laden und einen neuen lokalen Chat in einem leeren Testordner öffnen. In der Plugin-Verwaltung prüfen, dass Vibe Coding Cookbook 0.1.4 aktiviert ist. Die sichtbare Auswahlliste muss die sieben IDs aus `bundle.json` anbieten; eventuell schon vorhandene Einzelinstallationen dabei nicht mit dem Bündel verwechseln.

Die separate Cookbook-Sidebar ist bereits installiert geblieben. Ganz links beziehungsweise im Mehr-Menü ihr Buch-/Pfannen-/Ei-Symbol prüfen: erkennbar im hellen und dunklen Modus, anklickbar, Katalog mit sieben Skills und beiden Namen sichtbar. Das Bündel-Icon und das Sidebar-Icon sind getrennte Flächen.

## Claude Code

Bereits im Benutzerprofil installiert; für die jetzige Prüfung keine weiteren Installationsbefehle ausführen. Ein synthetischer Testordner und ein lokaler Starthelfer liegen ignoriert unter `.scratch/desktop-acceptance/`. Der Starthelfer öffnet nur die bestehende Claude-Code-Laufzeit im Testordner; er übermittelt keinen Prompt.

Den bereits vorhandenen angemeldeten Claude-Code-Binary verwenden; falls `claude` nicht im PATH liegt, dessen vorhandenen lokalen Pfad verwenden. Keine neue Anmeldung oder Installation erforderlich. Vom gewünschten lokalen Testprojekt aus die folgenden Befehle ausführen und die Pfade zur Cookbook-Build-Ausgabe auflösen:

```sh
claude plugin marketplace add /absoluter/lokaler/pfad/zum/cookbook/dist/claude --scope local
claude plugin install vibe-coding-cookbook@cookbook-local --scope local
```

Der absolute Pfad ist ausdrücklich ein zu ersetzender lokaler Dateipfad, keine URL. Eine neue Claude-Code-Sitzung im selben Testprojekt starten. Sie muss Version 0.1.4 und alle sieben namespaced Skills bereitstellen, beispielsweise `/vibe-coding-cookbook:kill-the-todos`.

## Gemeinsame kurze Probe

In einem leeren Testprojekt ausdrücklich nur einen Guide anfordern: „Finish This Chat / Close the Kitchen: Das Ziel bleibt offen. Bereite nur eine Übergabe und den nächsten Wiedereinstieg vor. Nichts ändern, archivieren oder veröffentlichen.“ Skill-Zuordnung, offene Punkte und fehlende Dateiänderungen prüfen. Danach die Hauptabläufe mit geeigneten synthetischen Aufgaben gezielt prüfen; dieser einzelne Guide ist kein Volltest aller sieben Skills.

Bei einem Fehler Host-Version, Plugin-Version, betroffene ID und genaue Meldung festhalten, ohne Zugangsdaten. Die bisherigen automatisierten Nachweise und Grenzen stehen in [host-tests.md](host-tests.md).

English: Native CLI installation and all seven loading checks pass. Both exact 0.1.4 packages are now installed and enabled from stable local build outputs for the requested visual review; Claude uses user scope. These registrations remain installed pending user review. Register the stable local build only for the intended review, restart in a fresh local session, inspect the actual plugin list and separate sidebar icon, and run a guide-only synthetic closing probe. Visual acceptance and main-workflow review are still pending. Do not publish.
