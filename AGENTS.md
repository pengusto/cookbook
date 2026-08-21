# Project instructions

`README.md` ist die Quelle für Produktversprechen, Ablauf, Modul-Katalog und
Ticket-Routing.

- Baue den kleinsten vollständigen Starter-Workflow. Kein eigenes
  Projektmanagement-System, keine Datenbank und kein dauerhafter Agentenrunner.
- Prüfe zuerst Projekttyp, Reifegrad, vorhandene Repository-Konventionen und
  den aktuellen Git-Status.
- Empfehle Module anhand konkreter Signale. Führe keine vollständige
  Standard-Checkliste für jedes Projekt aus.
- Mache in jeder Runde einen kurzen Empfehlungspass. Zeige den nächsten
  ausführbaren Schritt, passende Skills oder Module und offene Human-Gates
  vorausgewählt. Der Nutzer kann Empfehlungen abwählen, soll den Ablauf aber
  nicht selbst neu planen müssen.
- Wenn kein Spezialmodul nötig ist, empfehle stattdessen den kleinsten
  sinnvollen Check oder das nächste offene, nicht blockierte Ticket und nenne den Grund für das
  Überspringen.
- Eindeutige, reversible Entscheidungen darf Codex selbst treffen.
- Lizenz, Öffentlichkeit, externe Kosten, Datenschutz, Berechtigungen und
  Veröffentlichung brauchen eine menschliche Bestätigung.
- Nutze `.scratch/` nur für private, vorläufige und lokale Artefakte. Der Ordner
  bleibt ignoriert. Secrets gehören auch dort nicht hinein.
- Lege bestätigte dauerhafte Tickets unter `docs/tickets/` ab. UI-Tickets
  speichern ausgewählte Referenz-Screenshots im jeweiligen `assets/`-Ordner.
- Halte dauerhafte Projektregeln kurz in der nächsten passenden Dokumentation.
  Blähe `AGENTS.md` nicht mit Projektstatus oder Ticketdetails auf.
- Nutze Stop Slop beim Schreiben oder wesentlichen Bearbeiten menschlich
  sichtbarer Prosa. Nutze es nicht für Code, Konfiguration, Logs oder
  strukturierte Daten.
- Pflege `CHANGELOG.md` für nutzerrelevante Änderungen im selben Change unter
  `Unreleased`. Vor Releases mit `$changelog-generator` gegen Commits seit dem
  letzten Tag abgleichen, ohne kuratierte Einträge blind zu ersetzen.
- Das Projekt ist vor dem ersten Release. Ersetze überholte Ansätze, statt
  parallele Legacy-Kompatibilität einzubauen.
- Externe Veröffentlichung, Plugin-Installation, bezahlte Dienste, Deployments
  und Nachrichten bleiben Human-Gates.
