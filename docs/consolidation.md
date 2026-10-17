> Historical preparation record. For current Beta status, installation and limitations, use the [README](../README.md) and [public release review](public-release-review.md).

# Zusammenführung: Cookbook by Pengusto

Stand 2026-10-16 · Review 0.2.0 · privater GitHub-Abgleich auf ausdrücklichen Nutzerwunsch; keine öffentliche Veröffentlichung.

## Eine Quelle, zwei Installationen

skills/ ist ab jetzt die einzige gepflegte Quelle. Beide Namenswelten ersetzen nur Titel und Aufrufnamen, keine Workflow-Logik. Plain und Kitchen werden für Codex und Claude gebaut. Jede Installation zeigt genau einen Titel pro Skill; Website und optionale Sidebar haben passende getrennte Ansichten. Die alte Abhängigkeit von externen Originalrepos entfällt.

| Stabile Quell-ID | Plain | Kitchen |
|---|---|---|
| start-it-right | How Do I Start? (`how-do-i-start`) | Prep the Kitchen (`prep-the-kitchen`) |
| are-we-cooking | Am I Making Progress? (`am-i-making-progress`) | Are We Cooking? (`are-we-cooking`) |
| did-i-leak | Did I Leak? (`did-i-leak`) | Keep the Recipe Secret (`keep-the-recipe-secret`) |
| will-they-sue-me | Will They Sue Me? (`will-they-sue-me`) | Can I Serve This? (`can-i-serve-this`) |
| let-them-see-it | Am I Ready to Share? (`am-i-ready-to-share`) | Ready to Serve (`ready-to-serve`) |
| what-did-we-change | What Did We Change? (`what-did-we-change`) | What’s New on the Menu? (`whats-new-on-the-menu`) |
| kill-the-todos | Can We Finish? (`can-we-finish`) | Close the Kitchen (`close-the-kitchen`) |

## Vollständige Historie erhalten

Alle folgenden Spitzen sind als history/*-Branches und als Vorfahren von main erhalten. Kein Squash und kein Rebase. Der spätere private GitHub-Abgleich wurde separat autorisiert. Originalrepos sind unveränderte Archive. Aktuelle uncommittete Quell-Dateien wurden vor der Umstellung gegen die bisherigen Paket-Hashes geprüft; sie waren bereits als Cookbook-Snapshots erfasst.

| Historischer Branch | Erhaltene Spitze |
|---|---|
| `history/start-it-right` | `cb7d6153e5be27f486f35c7822310b1acc90e069` |
| `history/are-we-cooking` | `f32f94c0c58e7d1f6a36676daf4ac80a31129819` |
| `history/did-i-leak` | `f3bd587b35c4fa9f8ad3e741e107cde0b12c44fc` |
| `history/will-they-sue-me` | `9c2fac2ba85f3624322ce48b7d18560ddd155222` |
| `history/let-them-see-it` | `908abc50d43aba0f9e3f85cc25f30dd47d8ab47e` |
| `history/what-did-we-change` | `1432a3311628553146eeda84915532aaefe6b9ae` |
| `history/kill-the-todos` | `c309e60b17be484005c0004d127f5508c41a9576` |

Vergangene Dateien lassen sich beispielsweise mit `git show history/did-i-leak:SKILL.md` lesen. Die alten Einzelrepos werden nicht gelöscht oder auf GitHub archiviert. Eine frühere Cookbook-Bundle-Sicherung und private Migrationsnachweise liegen ignoriert unter .scratch/consolidation. Die vorherige generierte Website bleibt dort unter website-before-0.2.0 erhalten. Alte dist-Ausgaben bleiben erhalten, damit bestehende 0.1.x-Installationen nicht durch den Build unterbrochen werden.

## Lokale Installation und Prüfung

Installationsbefehle stehen in der README. Beide Varianten verwenden dieselbe Plugin-Identität cookbook-by-pengusto und denselben Marketplace cookbook-by-pengusto-local. Zum Wechsel sichern und nativ neu installieren; nicht beide Namenswelten parallel aktivieren. Der Einzelinstaller verweigert bereits vorhandene Gegenvarianten. Bestehende 0.1.4-Nutzerinstallationen werden durch diesen Build nicht automatisch ersetzt.

Die neuen strukturierten Daten beschreiben nur die sichtbare Namenswelt; alternateName entfällt, weil der zweite Titel auf der jeweiligen Seite nicht angezeigt wird. Historische Schema.org-/Google-Ergebnisse gelten für 0.1.x und sind keine erneute offizielle Validator-Abnahme der neuen Seiten.

Geprüft für 0.2.0:

- Build, Allowlist/Hashes, 18 ZIPs, Prüfsummen und lokale Links: bestanden.
- 17 Vertragstests und portabler Neubau mit identischen Artefakt-Hashes: bestanden.
- Codex native plugin/read: beide Skill-Pakete und beide optionalen Sidebar-Pakete eingelesen.
- Claude Manifestvalidierung: beide Skill-Pakete bestanden.
- Claude-Modelltest nach ausdrücklicher Freigabe: je Variante sieben Skills über ihre neuen Namespaces entdeckt und geladen. Ausschließlich künstlicher Leseauftrag; Testdatei unverändert, keine Workflows ausgeführt.
- Browser: Plain/Kitchen-Umschaltung, jeweils sieben einzelne Titel und passende Downloads sichtbar geprüft.
- Gitleaks über alle 37 bisher erhaltenen Commits: keine Funde. Das ersetzt keine vollständige manuelle Prüfung der Historie.

Die aktive 0.1.4-Installation wurde nicht automatisch verändert. Sichtbare Desktop-Abnahme und vollständige Workflow-Ausführung der neuen Variante bleiben offen. Öffentliche Ziele, Rechtsseiten, Store-Zugang, zusätzliche Scannerabdeckung und ausdrückliche Veröffentlichungsfreigabe bleiben offen. Nur das private GitHub-Repo pengusto/cookbook ist für den Abgleich zwischen eigenen Macs autorisiert. Keine öffentliche Veröffentlichung, kein Deployment und keine gelöschten Originale.

English: One maintained repository with seven canonical sources renders two alternative naming installations. All seven full Git histories are preserved as history/* branches and main ancestry; old repositories and output archives remain unchanged. Generated names and invocation IDs vary while workflow content, helpers and licenses share one source. Existing host installations are not silently switched. Private GitHub sync is authorized separately; no public publication.
