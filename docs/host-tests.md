# Lokale Host-Tests am 2026-10-15

Aktueller Nachtrag: Authentifizierte Claude-Tests für Review 0.1.2 wurden anschließend ausgeführt; Ergebnisse am Ende dieses Dokuments. Frühere Anmeldeblockaden bleiben als historischer Prüfstand erhalten.

Die Tests verwenden ein eigens erzeugtes Git-Fixture mit einem kleinen Python-Programm, einem absichtlich übertriebenen Feature-Commit-Titel und einem später gelöschten, ausdrücklich unechten Demo-Marker. Es wurden keine echten Zugangsdaten verwendet, Originalprojekte verändert oder Pakete veröffentlicht. Rohprotokolle und Prompts bleiben lokal im ignorierten `.scratch/host-tests/`.

## Codex CLI 0.160.0

Der lokale Marketplace wurde vorübergehend registriert, das Plugin nativ installiert und aktiviert. Eine neue CLI-Sitzung erkannte alle fünf Skills unter dem installierten Plugin-Cache. Die Tests lasen diese Dateien, keine vorhandenen Einzelinstallationen. Wegen einer inkompatiblen bestehenden MCP-Konfiguration wurde die Benutzerkonfiguration per `--ignore-user-config` übersprungen; Authentifizierung blieb unverändert. CLI-Override: `-c plugins.vibe-coding-cookbook@cookbook-local.enabled=true` (ohne zusätzliche Anführungszeichen im Schlüssel). Der erste Override mit enthaltenen Schlüssel-Anführungszeichen führte zu einem Ladefehler und wurde korrigiert.

| Skill | Beobachtung | Bewertung |
|---|---|---|
| What Did We Change | Beide Tags und echten Diff geprüft; trotz Feature-Commit nur Formatierung erkannt; keine nutzerwirksamen Änderungen behauptet | Gezielter Smoke-Test bestanden |
| Start It Right | Kleine Portfolio-Struktur und genau einen nächsten Schritt empfohlen; Modulwahl als unbestätigt behandelt; nichts umgesetzt | Gezielter Smoke-Test bestanden |
| Let Them See It | Erst Bewertung mit belegten Lücken; nichts geändert oder veröffentlicht; fehlende Scan-Abdeckung sichtbar gehalten | Gezielter Smoke-Test bestanden |
| Did I Leak | Zwei aktuelle Dateien sowie sieben historische Blobs über vier Commits geprüft; gelöschte Demo-Datei gefunden, Wert nicht ausgegeben; Fixture-Hashes unverändert | Verhalten und begrenzte Heuristikabdeckung bestätigt; vollständiger Scannerlauf offen |
| Will They Sue Me | Installed Skill und Review-Map gelesen; fehlende Märkte, Zielgruppe, Datenflüsse und Anbieter benannt; keine pauschale Bannerpflicht oder rechtliche Freigabe behauptet | Scoping-Smoke-Test bestanden; keine rechtliche Produktprüfung |

Die ersten drei Szenarien liefen mit Plugin 0.1.0 in einer Nur-Lese-Sandbox; die letzten beiden mit 0.1.1 in workspace-write, zusätzlich ohne Schreibfreigabe im Testauftrag. Die Skill-Dateien sind zwischen diesen Versionen bytegleich; 0.1.1 ergänzt ausschließlich Paketmetadaten, Icons und Dokumentation. Codex 0.1.1 wurde erneut nativ installiert und alle fünf Skills erneut erkannt. Die Fixture-Dateien einschließlich Git-Inhalten blieben im zweiten Durchlauf hashgleich, Git-Status sauber.

Scan-Grenzen: Gitleaks scheiterte im Host-Sandbox-Kontext an macOS-Cache-/Berechtigungsfehlern und lieferte keine belastbare Abdeckung. TruffleHog fehlt. Der Agent kennzeichnete dies, statt den Scan als bestanden zu werten. Für den zweiten Test wurden die gebündelten Heuristiken im Speicher aufgerufen, um die normalerweise erzeugte Git-Cachedatei zu vermeiden. Das beweist nicht den unveränderten vollständigen Scanner-CLI-Ablauf. Keine Erkennung echter Secrets oder umfassende Sicherheitsbewertung behauptet.

Nach den Tests wurden das Cookbook-Plugin und sein temporärer Marketplace nativ entfernt. Vorhandene Plugins und einzelne Skills wurden nicht ersetzt. Dies ist CLI-Nachweis, keine Desktop-UI-Abnahme.

## Claude Code 2.1.295

Die vorhandene native Laufzeit aus dem Claude-App-Cache wurde verwendet; kein Installer, PATH-Eintrag oder API-Key hinzugefügt. `claude auth status` meldet `loggedIn: false`.

- Plugin-Ordner und Marketplace bestehen `claude plugin validate <pfad> --strict`. Eine zunächst fehlende Marketplace-Beschreibung wurde im Generator ergänzt. Die verbleibende README-Empfehlung ist ein unverbindlicher Hinweis auf einen öffentlichen Installationsbefehl; es wird keine erfundene GitHub-Adresse eingesetzt.
- Laden per `--plugin-dir` erkennt alle fünf namespaced Skills aus dem Ordner. Das finale 0.1.1-ZIP wurde ebenfalls direkt geladen: Init-Ereignis meldet das Plugin, Version 0.1.1 und alle fünf Skills.
- Der tatsächliche Modellaufruf endet mit `authentication_failed` / `Not logged in · Please run /login`, null Modell-Tokens und Exit 1. **Kein Claude-Verhaltenstest bestanden.** Ein Desktop-Login wurde weder übernommen noch neu eingerichtet.
- Keine permanente Claude-Plugin-Installation vorgenommen. Die vom Host angelegte temporäre ZIP-Extraktion wurde nach dem Test entfernt.

Fortsetzung nach bewusster Claude-Code-Anmeldung: In einem separaten Fixture mit `claude --plugin-dir <lokales-zip>` die fünf Szenarien aus diesem Bericht und `behavior-review.md` erneut ausführen, tatsächliche Tool-Aktionen reviewen und Paket-Hash protokollieren. Keine Login-Daten in Protokolle aufnehmen.

## Paket und Metadaten

Review-Version 0.1.1: englische Codex-Listing-Felder, deutsche Listing-Übersetzung, Claude-Anzeigename/Icon/Keywords, helle und dunkle 512-Pixel-PNGs sowie SVG-Originale. Angaben werden aus `bundle.json`, `store/` und `assets/` gebaut. Kein MCP-Server, kein Hook und keine automatisch installierten Scanner. Einzelpakete behalten identische Skill-Dateien und Lizenzen.

Finale ZIP-SHA256: Codex `02e35010c77745e1c59786885c6c3ba28d944ea55704d8538757767f9586d0bc`, Claude `a28a95af38d9ecd7c47f8cab6b0356cec100af1dfee7adae81012b8a42d8c20f`. Eine portable Kopie ohne Git, lokale Quellenregistrierung, dist, site und private Evidenz bestand Build, Check und acht Tests; alle sieben ZIP-Hashes stimmen mit der Arbeitskopie überein. Kopie und 201-MiB-Compiler-Cache wurden entfernt. Etwa 175 KiB private Roh-Evidenz bleiben bis zur Abnahme im ignorierten `.scratch/host-tests/`; sie enthalten das synthetische Fixture, keine Ersatzoriginale. Die native Deinstallation wurde zusätzlich durch leere Cookbook-Plugin-Liste und entfernte Konfigurationseinträge geprüft; der leere Rest-Cache wurde entfernt.

Build, Check, Quellenabgleich und acht Paketvertragstests prüfen die erzeugten Dateien, ZIPs, Metadatenlimits und Icons. Aktuelle ZIP-Prüfsummen stehen in `site/downloads/SHA256SUMS`; sie sind kein Store-Zertifikat. Offene Schritte: Claude-Anmeldung und Verhaltenstests, vollständige externe Scannerabdeckung, optionale Desktop-UI-Prüfung, bestätigte Publisher-/Zieladressen und später separat autorisierte Einreichung. Keine Annahme oder Freigabe behauptet.


## Icon-Anpassung: Review 0.1.2

Auf Nutzerwunsch wurden nur die Paket-Icons durch transparente Pfanne-/Ei-Symbole für kleine Navigationsflächen ersetzt. Skills unverändert. Die oben genannten Host-Tests und ZIP-Hashes beziehen sich auf den vorherigen 0.1.1-Stand; kein neuer Host-Verhaltenstest behauptet. Aktuelle Paket-Hashes stehen in site/downloads/SHA256SUMS. Build, Check, Quellenabgleich und acht Tests bestehen. Die tatsächliche Belegung der ganz linken Codex-Navigationsleiste konnte nicht bestätigt oder geändert werden; die verfügbare UI-Steuerung erlaubt keinen Zugriff auf Codex. Plugin-Manifest-Icons und diese native Leiste sind nicht als identische Fläche belegt.


## Authentifizierte Claude-Tests: Review 0.1.2, 2026-10-15

Nach Nutzeranmeldung bestätigt `auth status` einen Claude.ai-Login. Im eingeschränkten Shell-Kontext war der Schlüsselbund nicht lesbar; die Prüfung mit Schlüsselbundzugriff erkannte die Anmeldung. Keine Zugangsdaten oder Kontoidentifikatoren werden in diesen Bericht übernommen.

Claude Code 2.1.295 verwendete seine eingestellte Modellwahl `claude-opus-5-5`. Das finale Claude-ZIP 0.1.2 wurde lokal entpackt und mit `--plugin-dir` geladen; Init-Ereignisse enthalten alle fünf namespaced Skills und den Plugin-Pfad aus der ZIP-Extraktion. SHA-256 des getesteten Archivs: `fce54fa95fff8e36565dd77031700c8d19952274ed5771606b1c22ab01e9150a`. Keine permanente Claude-Plugin-Installation.

Jedes Szenario lief in einer eigenen Kopie des synthetischen Fixtures, ohne Remote. Nutzer-/Projekt-Settings wurden für die Tests ausgelassen, Hooks deaktiviert, fremde MCP-Server ausgeschlossen und keine Session-Persistenz verwendet. Nur Lese-, Such-, Skill- und eingeschränkte Shell-Werkzeuge standen zur Verfügung; keine Web-Recherche, Subagents oder Außenaktionen. Skill-Instruktionen und synthetische Fixture-Inhalte wurden im Rahmen der autorisierten Modelltests an Claude übertragen. Dies sind gezielte Smoke-Tests, keine umfassende Evaluation.

| Skill | Beobachtetes Verhalten | Bewertung |
|---|---|---|
| Start It Right | Passende kleine Portfolio-Empfehlung, Annahmen markiert, eine Rückfrage, konkreter nächster Schritt; nichts implementiert. Zusätzlicher Git-/Changelog-Kontext kam aus dem anfangs zu breit formulierten Testprompt | Gezielter Planungs-Smoke-Test bestanden |
| Will They Sue Me | Review-Map gelesen, fehlende Märkte/Betreiber/Datenflüsse benannt; keine universelle Bannerpflicht oder rechtliche Freigabe. Nicht vorhandenes Formular korrekt als ungeprüft bezeichnet | Gezielter Scoping-Smoke-Test bestanden; keine Rechtsprüfung |
| Let Them See It | Repository, Geschichte und Diff geprüft; fehlende Lizenz/README-Abdeckung und Scan-Lücke benannt; Evaluation vor Änderungen, nichts umgesetzt | Gezielter Evaluations-Smoke-Test bestanden; dessen angefragter Gitleaks-Lauf wurde von der Testfreigabe abgewiesen und nicht als bestanden behauptet |
| What Did We Change | Nach Wiederholung tatsächlichen Diff v0.1.0..v0.1.1 gelesen; nur Formatierung und keine neue Nutzerfunktion trotz Feature-Commit-Titel berichtet | Gezielter Diff-Smoke-Test bestanden |
| Did I Leak | Nach Wiederholung unveränderte gebündelte CLI mit --full --json ausgeführt. Gitleaks completed; TruffleHog unavailable. Vier erreichbare Commits, drei Tags, ein Branch, sieben historische Objekte, keine Heuristik-Kürzungen. GO WITH REVIEW, null Findings; Scanner-Exit 1 korrekt von erfolgreichem Modelllauf unterschieden | Ablauf-/Abdeckungsnachweis mit Grenze: keine erfolgreiche Secret-Erkennung belegt, Demo-Marker löste keinen Treffer aus; vollständige Scannerabdeckung offen |

Die erste Shell-Freigabeliste war für zusammengesetzte Befehle mit Variablen/Schleifen zu eng. Did I Leak und What Did We Change wurden mit expliziten einzelnen erlaubten Befehlen wiederholt; die finalen Wiederholungen enthalten keine Permission-Denials. Die ursprünglichen Abweisungen sind kein Authentifizierungs- oder Plugin-Ladefehler. Andere Szenarien nutzten nach abgewiesenen Hilfsbefehlen die erlaubten Lesewege und kennzeichneten verbleibende Lücken. Keine Berechtigungsumgehung und kein globales Deaktivieren von Freigaben.

Dateiverifikation: Alle Arbeitsdateien und die Git-Inhalte außer Indexdatei stimmen mit dem ursprünglichen Fixture überein; HEAD, Tags/Refs, Git-Objekte und gestagte Einträge sind gleich, Git-Status sauber. Bei Start It Right und Let Them See It aktualisierte Git die Index-Metadaten. Nur beim vollständigen Did-I-Leak-Lauf wurde erwartungsgemäß `.git/did-i-leak/state.json` erzeugt. Keine Quellprojekte oder Skill-Snapshots geändert, keine Veröffentlichung, Rotation oder History-Umschreibung.

Private Prompts, stream-json-Protokolle, Antworten, Paket-Hash und Dateiverifikation bleiben im ignorierten `.scratch/claude-review/` bis zur Review-Abnahme erhalten. Die sieben agentenerzeugten Fixture-Kopien und die ZIP-Extraktion wurden nach Prüfung entfernt; das frühere Original-Fixture unter `.scratch/host-tests/fixture` bleibt erhalten. Kein Login-Protokoll gespeichert.

English: Authenticated Claude Code 2.1.295 smoke-tested all five namespaced skills from the exact 0.1.2 archive. Four targeted behavior scenarios pass. Did I Leak completed the bundled full scan with Gitleaks, but TruffleHog is absent and the synthetic marker produced no finding, so successful secret detection is not established. Initial harness permission issues were corrected for scan and changelog retries. No source edits or publication occurred.

## Review 0.1.3: Abschluss, zwei Namen und sieben Quellen

2026-10-15. Alle sieben kuratierten Originalquellen haben ein eigenes lokales Git-Repository. What Did We Change wurde mit Git initialisiert; keine neuen Remotes oder Commits. UI-Anzeigenamen tragen jeweils Funktionsname und Koch-Titel, Frontmatter-IDs bleiben unverändert. Are We Cooking erhielt nach ausdrücklicher Nutzerwahl MIT. Der Abschluss-Skill wurde im vorhandenen `kill-the-todos`-Quellprojekt neu verfasst und mit dem früheren separaten Entwurf konsolidiert. Der offizielle `quick_validate.py` besteht für alle sieben Quellen; dafür wurde PyYAML 6.0.3 ausschließlich in einer temporären Testumgebung verwendet.

### Tatsächlich ausgeführte Verhaltenstests

Claude Code 2.1.295, mit vorhandener Anmeldung und temporärem `--plugin-dir`, ohne persistente Sitzungen, zusätzliche MCP-Server oder Hooks. Pro Szenario ein isoliertes Fixture mit zwei synthetischen Dateien. Keine permanente Plugin-Installation. Tool-Aufrufe, Antworten und Vorher-/Nachher-Hashes wurden geprüft.

| Szenario | Beobachtetes Ergebnis | Bewertung |
|---|---|---|
| Abschluss: nur Guide | Skill geladen; fehlender erfolgreicher Check bleibt offen, optionale Idee wird kein Auftrag; beide Dateien unverändert | Bestanden |
| Abschluss: bewusste Pause | Unerledigtes Ziel bleibt offen, konkrete Übergabe und Wiedereinstieg; Dateien unverändert, keine Archivierung | Bestanden |
| Abschluss: autorisierter Rest | Nur result.txt von `pending` auf exakt `ready` plus Newline geändert; STATE.md unverändert, keine Zusatzdateien, keine Commits/Publikation/Archivierung | Bestanden; genaue Bytes zusätzlich vom Test-Harness bestätigt |
| Nur Name „Close the Kitchen“ | Ohne technische Skill-ID korrekt `vibe-coding-cookbook:kill-the-todos` ausgewählt; Guide/Pause ohne Dateiänderung | Bestanden |
| Nur Name „Finish This Chat“ | Ohne technische Skill-ID denselben Skill ausgewählt; Guide-only ohne Dateiänderung | Bestanden |
| Check Progress / Are We Cooking? | `vibe-coding-cookbook:are-we-cooking` ausgewählt; Side quest anhand Fixture benannt und relevanten nächsten Check empfohlen; keine Dateiänderung | Gezielter Diagnostik-Test bestanden |

Beim Abschluss-Finish blockierte die schmale Testfreigabe zusammengesetzte Bash-Hilfsbefehle. Claude nutzte die verfügbaren Dateiwerkzeuge, las/prüfte den Inhalt und benannte die fehlende eigene Byteprüfung ausdrücklich. Der Harness bestätigt anschließend die exakten Dateibytes. Kein fehlgeschlagener Bash-Aufruf wird als erfolgreiche Prüfung gezählt. Dies war ein Zwei-Dateien-Szenario, kein echtes Checkout-System und kein Volltest beliebiger Abschlussaufgaben.

Codex CLI 0.160.0: separates Projekt-Fixture mit der bytegleichen `kill-the-todos`-Skillkopie, `--ignore-user-config`, `--ephemeral` und read-only Sandbox. Der Host las den Skill und STATE.md, ließ Dateien unverändert und lieferte die gewünschte Pause mit offenem Ziel und nächstem Wiedereinstieg. **Gezielter Guide-/Pause-Test bestanden.** Kein Codex-Ausführungs- oder Archivierungstest dieser Revision behauptet. Ein erster äußerer Sandbox-Versuch konnte den lokalen App-Server-Socket nicht initialisieren; der erfolgreiche Wiederholungslauf behielt die innere read-only Sandbox bei.

### Finale lokale Paketprüfung

Alle sieben Skills sind einzeln und bytegleich in den Codex-/Claude-Paketen enthalten. Die abschließende native Codex-`plugin/read`-Prüfung liest Bündel und optionale Sidebar. Claude besteht die strikte Manifestprüfung für Plugin und Marketplace. Der unverbindliche Hinweis auf einen öffentlichen Marketplace-Installationsbefehl bleibt offen, bis dessen echte Repository-Adresse feststeht; keine Platzhalter-Adresse eingefügt.

Build, Check, Quellenabgleich, vierzehn Vertragstests und portabler Neubau bestehen. Die Modelltests wurden vor finalen reinen Dokumentationsänderungen ausgeführt; die getesteten Abschluss-Skillbytes sind unverändert und per Hash mit den finalen Paketen abgeglichen. Die früheren fünf Skills erhalten keine pauschale neue Vollabnahme: ihre bisherigen gezielten Tests und Scannergrenzen bleiben maßgeblich.

Private Prompts, Rohprotokolle, Antworten, Status-/Hashprüfungen und Quell-Vorherkopien bleiben unter `.scratch/closing-update/` bis zur Review-Abnahme erhalten. Temporäre Validator-Abhängigkeiten und die agentenerzeugte Codex-Skillkopie werden nach Prüfung entfernt. Keine Originale oder bestehenden Installationen gelöscht. Keine Veröffentlichung, externen Nachrichten, Pushes oder Deployments.

English: Six isolated Claude scenarios pass, covering guide-only, pause, authorized finish, both natural-language closing names and the newly licensed progress skill. One Codex read-only guide/pause scenario passes. All seven sources pass the official skill validator; final native host manifest checks, fourteen contract tests and a reproducible portable rebuild pass. These are scoped checks, not complete cross-host behavioral certification. IDs remain stable and nothing was published.

## Finale native Installation beider Plugins: 0.1.3, 2026-10-15

Beide finalen ZIPs wurden in getrennte lokale Marketplace-Testordner entpackt, nativ registriert und installiert: Codex CLI 0.160.0 mit `plugin marketplace add` / `plugin add`, Claude Code 2.1.295 mit `plugin marketplace add --scope local` / `plugin install --scope local`. Claude verwendete in diesem Durchlauf **kein `--plugin-dir`**. Die bestehende Anmeldung blieb unverändert.

| Prüfung | Codex | Claude Code |
|---|---|---|
| Native Installation und Aktivierung | Bestanden, Version 0.1.3 | Bestanden, Version 0.1.3 |
| Installierte Dateien gegen finales ZIP | Alle 37 Dateien bytegleich | Alle 37 Dateien bytegleich |
| Neue Sitzung: sieben Skills erkannt | Native `skills/list`-Discovery aus Plugin-Cache | Init enthält sieben namespaced Skill-Aufrufe |
| Alle sieben Skills tatsächlich geladen | Alle SKILL.md und agents/openai.yaml aus installiertem Cache gelesen | Alle sieben über natives Skill-Werkzeug geladen |
| Beide sichtbaren Namen zugeordnet | Bestanden | Bestanden |
| Synthetische Testdateien unverändert | Bestanden | Bestanden |

Erfasste IDs: `start-it-right`, `are-we-cooking`, `did-i-leak`, `will-they-sue-me`, `let-them-see-it`, `what-did-we-change`, `kill-the-todos`. Der Claude-Host liest bei lokalen Ordner-Marketplaces aus dem registrierten `readFromFolder`; sowohl dieser Ordner als auch der Installationscache entsprachen dem ZIP. Beide Modellläufe endeten erfolgreich. Claude meldet keine Permission-Denials. Referenzen, Skripte und Lizenzen sind durch den vollständigen Dateiabgleich erfasst; eine Modell-Ausführung jeder Hilfsdatei wird nicht behauptet.

Diese Durchläufe prüfen Installation, Discovery, Laden und Namenszuordnung. Die vollständigen Workflows wurden dabei nicht erneut ausgeführt. Maßgeblich für Verhalten und Scannergrenzen bleiben die zuvor dokumentierten gezielten Szenarien. Codex lief ohne Benutzerkonfiguration, ohne persistente Sitzung und mit innerer read-only Sandbox; Claude mit lokalen Settings, deaktivierten Hooks, ohne zusätzliche MCP-Server und ausschließlich Read/Skill-Werkzeugen. Keine Originalprojekte oder Zugangsdaten in Testfixtures.

Getestete finale ZIP-SHA256:

- Codex: `65a2c1fd66577baa0f0101f4fa8f71774f8dd7f7c6d0c89bb43ab0a46c584a99`
- Claude: `90b8f97aebd46d2f5108a2506e875c7c0032107f928a9db8790118a176b3ce32`

Nach den Tests wurden beide temporären Plugins und Marketplaces nativ entfernt. Codex-Plugin-Liste und Konfiguration entsprechen dem Ausgangszustand; die Konfiguration ist bytegleich. Die bestehende Cookbook-Sidebar blieb erhalten. Claude meldet wieder eine leere Plugin-Liste; die ausschließlich erzeugten leeren lokalen Test-Settings wurden entfernt. Der zurückgebliebene Claude-Cache wurde nach erneutem ZIP-Abgleich entfernt; lediglich der native Deinstallationsmarker `.orphaned_at` war hinzugekommen. Beide Testextraktionen wurden entfernt. Originalarchive bleiben erhalten.

Prompts, Antworten, Protokolle, Hashprüfungen und synthetische Sitzungstestdateien bleiben bis zur Review-Abnahme lokal im ignorierten `.scratch/final-install/`. `verification.json` und `cleanup.json` fassen Ergebnisse und Bereinigung zusammen. Die sichtbare Codex-Desktop-Abnahme bleibt offen: Die verfügbare UI-Steuerung verweigert Zugriff auf Codex. Keine Veröffentlichung, Store-Einreichung oder externe Repository-Änderung.

English: Both exact 0.1.3 archives passed native installation, seven-skill discovery and loading, dual-name checks and unchanged-fixture checks. All installed package files matched their ZIPs. These are installation smoke tests, not repeated full behavior tests. Temporary registrations and test copies were removed, prior Codex configuration was restored byte-for-byte, and the existing sidebar was retained. Visible desktop acceptance remains open.

## Review 0.1.4: lokale Ausführung und erneute native Installation

2026-10-15. Ausschließlich Paketmetadaten und zugehörige Dokumentation geändert: Codex erhält top-level `requires_local_executor: true` im Kompatibilitätsmanifest. Beide Review-Pakete tragen Version 0.1.4; die sieben Skill-Inhalte, IDs und Lizenzen sind unverändert. Der bestehende Manifestvertrag prüft das Pflichtfeld bei Codex und seine Abwesenheit bei Claude.

Beide neu gebauten finalen ZIPs wurden erneut in separate Marketplace-Fixtures entpackt und nativ installiert. Native Codex-Discovery erkennt 7/7 Skills aus dem installierten Cache; Claude-Init meldet 7/7 namespaced Skills und lädt sie alle per Skill-Werkzeug, ausdrücklich ohne `--plugin-dir`. Vollständiger Cache-/ZIP-Abgleich: 37 Dateien pro Host bytegleich. Codex liest alle sieben SKILL.md und agents/openai.yaml aus dem installierten Cache. Beide Antworten ordnen beide sichtbaren Namen korrekt zu, enden erfolgreich und lassen STATE.md unverändert. Keine erneute vollständige Ausführung aller Workflows behauptet.

Codex verwendete zunächst versehentlich die zsh-Spezialvariable `path` und verlor dadurch `cat` aus dem Suchpfad; der Befehl scheiterte mit Exit 127. Der korrigierte Wiederholungsschritt mit `skill_file` und absolutem `/bin/cat` lief erfolgreich. Das ist ein korrigierter Modell-Hilfsbefehl, kein bestandener Erstversuch oder Plugin-Defekt. Claude meldet keine Permission-Denials.

- Codex ZIP-SHA256: `496de7acd6d28c365753c52aeeed60c0e3c46fee67dc8d2941646f856dbc33aa`
- Claude ZIP-SHA256: `e6984eff035cd8a51bd3ee12a6f34d01dc4033fe392dbbb0a5d3ca744cbea4f4`

Build, Quellenabgleich, vierzehn Vertragstests und ein bytegleicher portabler Neubau bestehen. Nach dem Test wurden beide Plugins und Marketplaces nativ abgemeldet. Lokale Plugin-Einträge entsprechen dem Ausgangszustand, die Codex-Konfiguration ist bytegleich, die bestehende Sidebar bleibt erhalten. Die vollständige entfernte Katalogansicht wurde nicht als identische Baseline gewertet: Der eingeschränkte erste Aufruf lieferte einen Fallback, der spätere Aufruf mit Netzwerkzugriff den aktuellen Remote-Katalog. Kein externer Katalog wurde zurückgesetzt. Eigene Testextraktionen, Installationscaches und leere lokale Claude-Testsettings wurden nach Prüfung entfernt.

Die Rohprotokolle, Prompts, Antworten, Hash-/Bereinigungsnachweise und synthetischen Sitzungstestdateien bleiben im ignorierten `.scratch/executor-review/` bis zur Review-Abnahme erhalten. Die vor dem Neubau gesicherten 0.1.3-Archive liegen dort unter `previous-0.1.3/`; es sind frühere generierte Artefakte, keine Ersatzoriginale. Keine Veröffentlichung oder sichtbare Desktop-Abnahme.

### Kontrollierter Detektionsnachweis

Der unveränderte gebündelte Did-I-Leak-CLI lief mit `--full --json` gegen ein neues isoliertes Git-Fixture: zwei ausdrücklich künstliche, nicht verwendbare GitHub-PAT-förmige Testwerte, einer aktuell und einer nach Commit wieder gelöscht. Zwei erreichbare Commits, ein Branch, drei historische Objekte, keine Heuristik-Kürzungen. Gitleaks `completed`, beide Testwerte korrekt als aktuelle beziehungsweise historische Blocker erkannt; erwartetes Urteil `NO-GO`, Scanner-Prozess Exit 2. Dieser erwartete Fund-Exit ist kein Installationsfehler.

Gespeicherter Bericht und stderr wurden gegen beide Rohwerte geprüft; keiner ist enthalten. TruffleHog bleibt `unavailable`; kein globales Tool installiert und keine Verifikation von Credentials über externe Dienste ausgeführt. Der erfolgreiche gezielte Detektionsnachweis ersetzt keine Prüfung echter Secrets oder aller Detektoren. Das agentenerzeugte Git-Fixture wurde nach Bericht-/Hashprüfung entfernt; redigierter Bericht und Nachweis bleiben unter `.scratch/executor-review/detection-*.json`.

English: Both exact 0.1.4 archives passed native installation, seven-skill discovery/loading and dual-name checks after declaring local Codex execution. Installed bytes matched the ZIPs; fixtures were unchanged and temporary registrations were removed. A corrected Codex shell helper was retried successfully. A separate synthetic Gitleaks regression detected both current and deleted historical probes without exposing values; TruffleHog remains unavailable. No publication or desktop visual acceptance is claimed.

## Vorbereitung der sichtbaren Nutzerabnahme

Auf Nutzerauftrag wurden beide finalen 0.1.4-Pakete aus den stabilen lokalen dist-Marketplaces erneut installiert und aktiviert. Claude Code verwendet diesmal Benutzer-Scope, damit eine neue Sitzung im isolierten Testordner das Plugin findet. Je 37 installierte Dateien stimmen bytegleich mit dem final getesteten ZIP überein; alle sieben Skill-Ordner sind vorhanden. Beide Registrierungen bleiben für die Nutzerabnahme installiert; die bestehende Sidebar wurde nicht verändert. Keine sichtbare Abnahme behauptet. Die manuellen Schritte stehen in [desktop-acceptance.md](desktop-acceptance.md). Synthetische STATE.md-Dateien, ein lokaler Claude-Starthelfer und maschinenbezogener Installationsnachweis bleiben ausschließlich ignoriert unter `.scratch/desktop-acceptance/` bis zur Abnahme erhalten. Nichts veröffentlicht.

English: Both exact final 0.1.4 packages are now installed and enabled from stable local marketplace outputs for user visual acceptance. Claude uses user scope. All installed bytes match the final ZIPs; registrations remain installed, the existing sidebar is unchanged, and visual results are pending.

## 2026-10-26 · 0.7.0 · lokale Erweiterung auf 18 Workflows

Drei zusätzliche Workflows: Review My Changes / Taste Before Serving,
Can We Simplify? / Trim the Recipe und Find Our Work / Find the Recipe.
Vorhandene Abläufe ergänzen `explain`, `choose`, `verify-live` und `handoff`;
Abschlussabgleich und Dokumentationskonsistenz bleiben Zweige bestehender
Workflows. Der zuvor lokal ergänzte Debugging-Workflow und `usertest` sind
enthalten. Alle acht README-Fassungen und zwölf Rezeptoberflächen enthalten
die neuen Einträge; Übersetzungen sind nicht durchgehend muttersprachlich
abgenommen.

Build, Paketprüfung, Quellenabgleich und 46 Tests bestehen. Ein portabler
Neubau erzeugt bytegleiche Archive. Der Skill-Validator besteht für die neun
neuen/geänderten Workflow-Quellen in beiden gerenderten Namensvarianten.
Ein Paketvertrag prüft zusätzlich relative Anleitungslinks und ungelöste
Platzhalter in allen Markdown-Runtime-Dateien.

Eine unabhängige Subagent-Prüfung führte zwölf synthetische Szenarien aus:
Diff-Review mit absichtlicher Rechenregression; Vereinfachung mit neun
Verhaltensfällen einschließlich Auslassen/Leeren; Suche bei ähnlich benannten
Quellen; Auslieferungsabgleich mit altem Download trotz grünem Build;
zielbezogene Übergabe; Wahl zwischen vorhandener Standardbibliothek und
neuer Abstraktion; Untersuchung ohne Änderungen; usertest ohne verfügbare
Interaktionswerkzeuge; Erklärung eines Persistenzpfads; Zusagen-/Beitragsabgleich;
Karakeep-Zugangsentscheidung mit begrenzten Connector-Fähigkeiten; unterstützte
Projektzuordnung bei noch unverändertem Runtime-Kontext. Alle 25 Fixture-Dateien
behielten ihre Hashes. Kein Anweisungsdefekt wurde in diesen einzelnen
Trajektorien reproduziert. Die beiden lokalen Zugriffs-/Zuordnungsanweisungen
wurden separat validiert; sie gehören nicht zum Cookbook-Runtime-Paket.

Browser-Stichprobe: lokale deutsche Oberfläche im Desktop-Viewport,
alle drei neuen Rezeptseiten und Kitchen/Plain-Wechsel mit passendem Such-Skill-
Aufruf. Keine neue vollständige mobile oder native Desktop-Abnahme. Es gab
keine reale Connector-Mutation, Chatverschiebung, Store-Prüfung oder
Installation von 0.7.0; die synthetischen Szenarien sind keine frischen
nativen Codex-/Claude-Plugin-Aufrufe und belegen keine allgemeine Zuverlässigkeit.

English: Local-only 0.7.0 preparation, 18 shared workflows. Build, source and
package checks, 46 tests, eighteen rendered skill validations and a byte-identical
portable rebuild pass. Twelve independent synthetic scenarios and a scoped
German desktop browser check pass with the stated coverage. No publication,
installed-plugin refresh, native host acceptance or real external mutation is
implied. Relative runtime instruction links are now covered by the package tests.

### Reihenfolge und Navigation, ebenfalls 26.10.2026

Die 18 Workflows sind jetzt nach Orientierung/Wiedereinstieg, Planung,
Umsetzung, Prüfung, Veröffentlichung und Abschluss geordnet. Katalog, Bundle,
alle zwölf Rezeptsprachen, Farben und acht README-Menüs wurden gemeinsam
umgeordnet; die Inhaltszuordnung wurde pro stabiler Quell-ID mit dem Stand vor
der Umsortierung verglichen. Startseiten-Verknüpfungen verwenden Quell-IDs
statt Positionsnummern. Ein ausführbarer UI-Vertrag prüft dieselben Ziele bei
zwei verschiedenen Rezeptreihenfolgen. Der Gesamtcheck besteht nun mit
47 Tests und bytegleichem portablem Neubau. Im lokalen Browser öffneten
„Ein Projekt beginnen“ das fünfte Rezept und „Rezepte entdecken“ die erste
Orientierungsanleitung. Kein Plugin-Update oder Deployment ausgeführt.

English: Reordered all eighteen workflows and retained every translated recipe's
content by source identity. Welcome navigation now uses stable source IDs; a
runtime UI regression test covers reordered arrays. Forty-seven tests and the
portable rebuild pass. Scoped local browser navigation checks pass.

### Kapitel und Schrittzahlen, 26.10.2026

Sechs Kapitel gliedern das Inhaltsverzeichnis und erscheinen als Kontext auf
der Rezeptseite. Kapitelmitgliedschaft kommt aus dem Katalog, Titel aus allen
zwölf UI-Sprachen. Tastaturfokus und Sichtbarkeitssteuerung adressieren die
tatsächlichen Rezept-Buttons auch innerhalb verschachtelter Kapitel. Die
Schrittzahlen sind dekorative, für Screenreader ausgeblendete DOM-Elemente
in gleich großen Kreisen; Grid-Zentrierung und tabellarische Ziffern ersetzen
die frühere Grundlinienausrichtung. Die geordnete Liste bleibt semantisch
erhalten.

49 Tests, Quellen-/Paketprüfungen und portabler Neubau bestehen. Neue Verträge
prüfen vollständige Kapitelübersetzungen und Tastaturnavigation über
Kapitelgrenzen. Desktop-Browser-Stichprobe: sechs Gruppen, Kapitelkontext,
sichtbar zentrierte Zahlen sowie Pfeil-ab von Rezept 04 zu Rezept 05 mit
korrektem Fokus und Kapitelwechsel. Keine neue mobile visuelle Abnahme oder
Veröffentlichung.

English: Six localized chapters, continuous recipe numbering and centered
decorative step numbers. Forty-nine tests and the portable rebuild pass.
Desktop keyboard navigation crosses chapter boundaries with correct focus.
No new mobile visual acceptance, plugin installation or deployment implied.

### Visuelle Verfeinerung der Kapitel, 26.10.2026

Kapitelköpfe verwenden jetzt farbige Registerbänder mit passenden vorhandenen
Küchen-Symbolen und größerer Serifenschrift. Die gestalterische Hierarchie
liegt auf den Kapiteln; Rezeptnamen bleiben ruhiger und ohne eigene Zählspalte.
Schrittzahlen behalten eine feine Kontur und die zentrierte Ausrichtung.
Die Desktop-Vorschau wurde im dunklen Systemtheme geprüft; der Gesamtcheck
besteht weiterhin mit 49 Tests und bytegleichem portablem Neubau. Das ist eine
lokale visuelle Stichprobe, keine vollständige responsive oder native Abnahme.

### Navigation, Lesetypografie und Kopieraktion, 26.10.2026

Der kompakte Markenkopf gibt dem Kapitelregister mehr Platz. Rezepttexte und
Schritterläuterungen verwenden größere Schrift und mehr Zeilenabstand. Die
Aufrufkarte ist gerade gesetzt; ein sichtbarer, in zwölf Sprachen beschrifteter
Button kopiert den aktuellen Aufruf und meldet Erfolg. Bei verweigertem
Zwischenablagezugriff bleibt die manuelle Textauswahl erhalten. Ein neuer
UI-Vertrag prüft Codex- und Claude-Aufrufe, beide Clipboard-Ausgänge sowie das
Zurücksetzen des Labels nach einem Sprachwechsel. Alle 50 Tests und der
portable Neubau bestehen. Desktop-Browser-Stichprobe in Hell und System/Dunkel;
der reale Kopierklick zeigte die Erfolgsrückmeldung. Keine neue vollständige
mobile Abnahme, Veröffentlichung oder Plugin-Aktualisierung.

English: Compact navigation header, larger reading typography and a visible
localized copy-command action. Fifty tests and reproducible packaging pass;
copy success, denied-clipboard fallback and feedback reset are covered by a
runtime UI contract. Scoped light/dark desktop checks pass. No deployment or
installed-plugin update implied.

### Schema: 18 Skills und sechs Kapitel, 26.10.2026

Die öffentlichen Buchseiten enthalten zusätzlich zur flachen Skill-Liste sechs
CreativeWork-Kapitel mit hasPart-Zuordnung aus dem Katalog. Namen und
Beschreibungen bleiben bei allen zwölf UI-Sprachen und beiden Namensvarianten
synchron; ein ausführbarer Regressionstest prüft diese Wechsel. Die
Skill-Anzahl in Installations- und Über-uns-Texten kommt aus dem Katalog,
damit frühere feste Zahlen nicht erneut abweichen. 51 Tests und der
bytegleiche portable Neubau bestehen. Kein externes Rich-Results-Testurteil
oder Google-Suchergebnis wird damit behauptet.

English: The public book JSON-LD now includes six chapter CreativeWorks and
their exact skill membership. Runtime tests cover all twelve interface
languages and both naming variants. Public skill counts derive from the
catalog. Fifty-one tests and the portable rebuild pass; external rich-result
eligibility and search appearance are not verified.
