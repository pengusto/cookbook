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
