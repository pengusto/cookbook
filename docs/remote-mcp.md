# Remote MCP — local development / lokale Entwicklung

Status: local implementation only. No deployment, public endpoint, Store upload,
review submission or publication. The generated runtime is **not** a Store ZIP.
The existing skills-only Store ZIP and optional stdio sidebar remain separate.

## Experiment closed / Experiment abgeschlossen — 2026-10-27

The maintainer ended this experiment before connecting it to the actual OpenAI
host. Preserve the local implementation and its tests as an experimental result;
do not treat this document as a request to resume setup. No runtime API key or
ChatGPT custom plugin was created. Key/plugin creation forms were cancelled.
The downloaded tunnel client and local tunnel profile were removed; no client or
Cookbook server is left running. The portal configuration record is retained as
`Cookbook Local Test — CLOSED` with its ChatGPT workspace association removed.
This label is a closure note, not a platform disable switch. The unused record
has no connected runtime. No deployment, submission or publication took place.
All 61 tests and the byte-identical portable rebuild passed before closure;
actual OpenAI-host acceptance was never completed.

Deutsch: Auf Wunsch des Maintainers beendet, bevor eine Verbindung zum echten
OpenAI-Host hergestellt wurde. Lokale Umsetzung und Tests bleiben als Experiment
erhalten; keine automatische Fortsetzung. Kein Laufzeitschlüssel und kein
ChatGPT-Testplugin erstellt; beide Formulare abgebrochen. Tunnel-Client-Download
und lokales Profil entfernt, keine Testdienste aktiv. Der ungenutzte Portaleintrag
bleibt als `Cookbook Local Test — CLOSED` ohne ChatGPT-Workspace-Zuordnung erhalten.
Die Kennzeichnung ist eine Abschlussnotiz, kein technischer Deaktivierungsschalter.
61 Tests und bytegleicher portabler Neubau bestanden; echte OpenAI-Host-Abnahme
nicht durchgeführt. Kein Deployment, keine Einreichung oder Veröffentlichung.

Local verification on 2026-10-27: all six real loopback HTTP integration tests
and two remote UI state regression tests pass. Chrome preview and a local iframe
MCP Apps test host verified initialization, selection through `open_cookbook`,
search/results, no matches, invalid IDs, full instructions, copy success feedback,
tool failure/retry, naming synchronization, and a 390px-wide scrollable view.
No console errors or warnings were reported during the checked journeys.
The local test host simulates the documented bridge; acceptance in the actual
OpenAI host and on a physical mobile device remains a separate gate.

Deutsch: Sechs echte HTTP-Integrationstests und zwei UI-Regressionstests bestehen.
Chrome-Vorschau und lokaler iframe-Testhost prüfen Initialisierung, Rezeptauswahl,
Suche, leere Treffer, unbekannte IDs, vollständige Anleitung, Kopier-Erfolgsmeldung,
Fehler/Wiederholung, Namenswechsel und eine scrollbar bedienbare 390px-Ansicht.
Keine Konsolenfehler oder Warnungen in den geprüften Abläufen. Der Testhost bildet
die dokumentierte Brücke nach; echte OpenAI-Host- und Mobilgeräte-Abnahme bleibt offen.

Regression lessons: rank workflow purpose above incidental mentions (limits are
not search relevance); changing display names must update existing result labels
without changing runtime IDs; a failed current selection must remain retryable;
late replies must not overwrite a newer selection. These are covered in
`tests/test_remote.py` and `tests/test_remote_ui.py`. Remote-only search results
have a bounded scroll area so they do not consume the whole sidebar.

Deutsch: Zweck vor beiläufigen Suchworten gewichten; Namenswechsel auch auf Treffer
anwenden und IDs erhalten; aktuellen Treffer erneut laden können; verspätete
Antworten dürfen keine neuere Auswahl überschreiben. Die genannten Tests sichern
diese Fälle ab. Die Suchtreffer haben einen eigenen begrenzten Scrollbereich.

## Run locally / Lokal starten

From the repository root, build with `python3 scripts/cookbook.py build`, then run:

```sh
python3 dist/remote/kitchen/scripts/remote_server.py --port 8767
```

Open http://127.0.0.1:8767/preview for the shared recipe book with search and full
instructions. Connect a Streamable HTTP MCP client to http://127.0.0.1:8767/mcp.
Stop with Ctrl+C. For Plain naming use `dist/remote/plain` instead. Each runtime
serves one naming variant. Build output and ZIPs stay in ignored `dist/remote/`;
no host installation is changed. Python 3.10+, standard library only.

Deutsch: Im Repository zuerst bauen, dann den obigen Server starten. Die Vorschau
zeigt das vorhandene Kochbuch mit Suche und vollständigen Anleitungen. Der Dienst
bindet ausschließlich an `127.0.0.1`; es werden keine Ports öffentlich freigegeben.
Plain und Kitchen sind getrennte Laufzeitpakete aus derselben Quelle. Es findet
keine Installation oder automatische Ausführung eines Workflows statt.

## Tools / Werkzeuge

| Tool | Arguments / Argumente | Result / Ergebnis |
|---|---|---|
| `search_workflows` | Optional `query` (max. 500 characters), `chapter`, `limit` (1–18), `language` (`en`/`de`) | Ranked lexical matches, prerequisites, limits, version and recipe links. Empty query browses; no matches remains empty. |
| `get_workflow` | Required `id` from search; optional `language` | Rendered canonical SKILL.md, SHA-256, bundled reference/script files as text with hashes, prerequisites and limits. |
| `open_cookbook` | Optional `workflow_ids`, `selected_id`, `language` | Shared MCP App book, optionally focused on selected results. Only this tool attaches a UI resource. |

Deutsch: Suche und Abruf liefern strukturierte Daten ohne eine neue Ansicht zu
öffnen. `open_cookbook` zeigt die vorhandene Buchansicht; Treffer und Auswahl werden
über die MCP-Apps-Brücke übernommen. Die Suche und Kurzbeschreibungen unterstützen
DE/EN; die Buchansicht behält ihre zwölf UI-Sprachen. Vollständige Anleitungen und
Referenzen bleiben in ihrer Ausgangssprache. Ergebnisse sind Suchtreffer, keine
verbindlichen Empfehlungen oder Freigaben.

The server only returns public Cookbook content. It cannot inspect a repository,
run a scanner, install a skill or authorize external actions. A `$skill` command
requires a corresponding local installation. Returned relative reference/script
paths require the client to materialize the supplied files before use. Review
instructions and execute only when the user's request and host permissions allow.
The book's copy button copies instructions, not an assumed installed invocation.

Deutsch: Der Server liest keine lokalen Nutzerdateien und führt keine Skripte aus.
Relative Referenz-/Skriptpfade funktionieren erst nach Bereitstellung der gelieferten
Dateien im Client. Ein `$skill`-Aufruf setzt eine lokale Installation voraus.
Der Kopieren-Button liefert deshalb die Anleitung. Auswahl allein startet nichts.

## Architecture and boundaries / Architektur und Grenzen

- `catalog.json`, allowlisted `skills/` files and `ui/locales.json` generate one
  versioned data snapshot per naming variant. Hash checks run before generation.
- The existing `sidebar_files` book renderer embeds a remote-only bridge from
  `ui/remote.js`; local sidebar and public website do not get remote controls.
- `scripts/remote_server.py` serves stateless Streamable HTTP with JSON responses.
  It does not implement SSE streams, sessions, legacy HTTP+SSE or server-initiated
  messages. GET/DELETE on `/mcp` return 405; notifications return empty 202.
- Exact Host/Origin checks, protocol versions, schemas, content negotiation,
  request size and socket timeouts are validated. No permissive CORS, arbitrary
  file routes, outbound requests, request-body logging, database or user accounts.
- `/preview` calls the same MCP tools directly on the local origin. Embedded UI
  uses `ui/initialize`, `tools/call` and `ui/notifications/tool-result` through its
  parent host. Host messages are untrusted; only known recipe IDs are applied.

Deutsch: Daten und Ansicht werden aus den bestehenden Quellen erzeugt. Transport
und UI-Brücke sind getrennt vom bisherigen stdio-Server. Nur `/mcp` und `/preview`
sind verfügbar. Host/Origin, Protokoll, Argumente, Größe und Zeitlimits sind eng
begrenzt. Es gibt keine Speicherung von Suchanfragen oder Projektinformationen.
Die lokale Vorschau ersetzt keine Abnahme der eingebetteten App im echten Host.

## Verification and future gates / Prüfung und spätere Voraussetzungen

Run `python3 scripts/launch_check.py` for build, artifact checks, source hashes,
unit/integration tests and byte-identical portable rebuilds, including remote ZIPs.
Tests exercise real loopback HTTP initialization, tools, UI resources, invalid
requests and canonical content parity. Browser preview checks cover the book,
search and selection; embedded-host acceptance must be reported separately.

To reproduce the local bridge check, run `python3 tests/remote_host.py --port 8768`
after building and open http://127.0.0.1:8768/test-host. The test host is not
packaged. Its controls send a real `open_cookbook` result, empty/unknown selections,
or one synthetic tool failure. Select 390px to test the narrow layout. Repeat a
result click after the failure to recover. Only the test host permits same-origin
child frames; the runtime preview's stricter CSP remains unchanged. Stop with Ctrl+C.

Deutsch: Für den lokalen Brückentest nach dem Build den Testhost starten und die
obige Adresse öffnen. Die Schaltflächen senden Auswahl/Leerauswahl/unbekannte IDs
oder simulieren einen Abruffehler. Derselbe Treffer muss danach wieder funktionieren.
390px prüft die schmale Ansicht. Der Testhost wird nicht ausgeliefert; nur er erlaubt
gleichartige Unterframes, die strengere CSP der Laufzeitvorschau bleibt bestehen.

Before any public deployment: explicitly authorize it, choose a production HTTP
runtime/proxy, HTTPS hostname and allowed origins, add operational rate/concurrency
limits and failure metrics without query-body logs, review privacy/retention
language, and test the actual MCP host on desktop and mobile. The development
HTTP server and loopback policy are deliberately not a production deployment.
No production hostname or public MCP configuration is invented in this package.

For Store submission: verify current eligibility, domain ownership, scans, five
positive and three negative review cases, demo recording and metadata. The portal
currently does not support adding an MCP to an existing skills-only plugin;
a new entry would require separate authorization. Admission is not guaranteed.

Deutsch: Vor öffentlichem Betrieb sind eine ausdrückliche Freigabe, produktives
Hosting/HTTPS, passende Origins, Betriebsgrenzen, Fehlerüberwachung und angepasste
Datenschutzhinweise nötig. Danach echte Host-Tests auf Desktop und Mobilgeräten.
Store-Zulassung, Domainprüfung, Scans, Testfälle und Demo bleiben eigene Schritte.
Dieses lokale Paket ist weder eine Einreichung noch eine Zulassungszusage.

References checked 2026-10-27:
[MCP Streamable HTTP](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports),
[OpenAI server guide](https://developers.openai.com/plugins/build/mcp-server),
[MCP Apps UI](https://developers.openai.com/plugins/build/chatgpt-ui),
[Submission](https://developers.openai.com/plugins/deploy/submission).
