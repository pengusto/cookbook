> **Historischer Prüfstand 0.1.x.** Die aktuelle Architektur, Namenswelten und Installationswege stehen in [consolidation.md](consolidation.md) und der [README](../README.md). Frühere Testergebnisse werden nicht als neue 0.2.0-Abnahme behauptet.

# Inventar und Auswahl

Historischer Auswahlbericht vom 2026-10-12. Aktuell sind sieben Skills MIT-lizenziert und integriert; Kill the TODOs wurde zum Abschluss-Skill weiterentwickelt. Aktueller Stand: [Namen und Quellen](skill-naming.md) und [Launch-Prüfstand](launch-readiness.md).

Stand: 2026-10-12. Alle 22 eigenen SKILL.md unter Own wurden vollständig gelesen; zusätzlich Will They Sue Me. Keine ungeprüfte Gesamtkopie. Vorhandene skill-library-Registrierung wurde nur gelesen. Die Liste enthält Zusammenfassungen, keine privaten Konfigurationen.

| Skill | Auswahl | Begründung | Lizenzdatei |
|---|---|---|---|
| Let Him Grill | Zurückgestellt | Später: wertvoll für verzweigte Entscheidungen; Abhängigkeiten grilling/domain-modeling und lokale Änderungen benötigen separaten Review. | MIT |
| Add Enis Impressum | Ausgeschlossen | Zurückgestellt: persönliche/operative Integration, zusätzliche Zugriffe oder projektspezifische Annahmen; vor Aufnahme generalisieren und Rechte prüfen. | Fehlt |
| Bitbucket Cloud | Ausgeschlossen | Zurückgestellt: persönliche/operative Integration, zusätzliche Zugriffe oder projektspezifische Annahmen; vor Aufnahme generalisieren und Rechte prüfen. | Fehlt |
| Cloudflare Access Ops | Ausgeschlossen | Zurückgestellt: persönliche/operative Integration, zusätzliche Zugriffe oder projektspezifische Annahmen; vor Aufnahme generalisieren und Rechte prüfen. | Fehlt |
| Create Agent Portraits | Ausgeschlossen | Zurückgestellt: persönliche/operative Integration, zusätzliche Zugriffe oder projektspezifische Annahmen; vor Aufnahme generalisieren und Rechte prüfen. | Fehlt |
| GitHub Username Migration | Ausgeschlossen | Zurückgestellt: persönliche/operative Integration, zusätzliche Zugriffe oder projektspezifische Annahmen; vor Aufnahme generalisieren und Rechte prüfen. | Fehlt |
| Jira Cloud | Ausgeschlossen | Zurückgestellt: persönliche/operative Integration, zusätzliche Zugriffe oder projektspezifische Annahmen; vor Aufnahme generalisieren und Rechte prüfen. | Fehlt |
| Move Codex Thread to Project | Ausgeschlossen | Zurückgestellt: persönliche/operative Integration, zusätzliche Zugriffe oder projektspezifische Annahmen; vor Aufnahme generalisieren und Rechte prüfen. | Fehlt |
| Vikunja Ops | Ausgeschlossen | Zurückgestellt: persönliche/operative Integration, zusätzliche Zugriffe oder projektspezifische Annahmen; vor Aufnahme generalisieren und Rechte prüfen. | Fehlt |
| VPS image releases | Ausgeschlossen | Zurückgestellt: persönliche/operative Integration, zusätzliche Zugriffe oder projektspezifische Annahmen; vor Aufnahme generalisieren und Rechte prüfen. | Fehlt |
| Start It Right | Erstauswahl | Erste Strecke: Aus einer Idee wird ein kleiner, prüfbarer Projektstart. | MIT |
| Are We Cooking? | Erstauswahl | Erste Strecke: Prüfen, ob die aktuelle Arbeit dem vereinbarten Ziel dient. | Fehlt |
| Did I Leak? | Erstauswahl | Erste Strecke: Arbeitsbaum und Git-Geschichte auf sensible Inhalte prüfen. | MIT |
| (Ah Shit) Here We Go Again | Zurückgestellt | Später: historische Ursachenanalyse; braucht mehr Verlauf, Lizenz fehlt. | Fehlt |
| Kill the TODOs | Zurückgestellt | Später: autorisierte Restarbeit abschließen; Lizenz fehlt. | Fehlt |
| Let Them See It | Erstauswahl | Erste Strecke: Ein Repository verständlich und überprüfbar für Außenstehende vorbereiten. | MIT |
| Remix My UI | Zurückgestellt | Später: Variantenworkflow braucht Bildwerkzeuge und ausdrückliche Konzeptfreigabe; Lizenz fehlt. | Fehlt |
| What Did We Change | Erstauswahl | Erste Strecke: Release-Notizen aus belegten Änderungen statt Commit-Rhetorik schreiben. | MIT |
| What Was I Cooking? | Seit 0.3.0 aufgenommen | Ursprünglich zurückgestellt; auf Nutzerwunsch als Chat-Rückblick ergänzt. | MIT |
| Which Name Wins? | Zurückgestellt | Später: persönliche Namensmuster und lokale Änderungen; Portabilität und Lizenz offen. | Fehlt |
| Yap to Spec | Zurückgestellt | Später: offene Chat-Ideen in ausgewählte Aufgaben überführen; Lizenz fehlt. | Fehlt |
| You Got This | Zurückgestellt | Später: breiter Ausführungsworkflow; erste Edition fokussiert Diagnose und Release, statt mehrere Autonomie-Workflows zu bündeln. | MIT |
| Will They Sue Me? | Erstauswahl | Bedingtes Produktreview; ergänzend zu Secret- und Repository-Review. | MIT |

## Grenzen der Auswahl

Persönliche Impressumsdaten, Account-Konfigurationen und private Betriebszugriffe werden nicht übernommen. Bestehende Änderungen in Let Him Grill und Which Name Wins bleiben erhalten. Eine lokale Lizenzdatei ist die dokumentierte Rechtebasis, keine umfassende rechtliche Freigabe. Agent-Verhalten und externe Abhängigkeiten werden nicht durch Paketprüfung bewiesen.

## Nutzerreise

1. Einstieg über den Einsatzmoment, nicht über die Menge installierter Skills.
2. Rezept aufklappen: Kontext, Ablauf, Verifikation, Ergebnis und Grenzen lesen.
3. Nur den benötigten Skill herunterladen oder installieren; Quellenstand prüfen.
4. Beispiel im eigenen Projekt verwenden; fehlende Zugriffe und menschliche Gates respektieren.
5. Ergebnisse prüfen; vor öffentlichem Servieren Geheimnisse, Produktpflichten und Repository getrennt reviewen.

Are We Cooking? ist redaktionell aufgenommen, aber ohne Paket, solange die Skill-Lizenz nicht ausdrücklich entschieden ist.

Aktualisierung 2026-10-19: What Was I Cooking? ist als achter Skill unter MIT aufgenommen; aktuelle Namen und Abgrenzung in [skill-naming.md](skill-naming.md). Die übrige Tabelle dokumentiert die damalige Erstauswahl.
