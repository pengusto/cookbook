# Lokale Plugins für Codex und Claude Code

Neu: Eine separate [lokale Sidebar-App](sidebar-app.md) ist auf Nutzerwunsch installiert. Sie registriert Cookbook mit Pfanne/Ei in der globalen Navigation; native MCP-Discovery bestätigt, sichtbare Desktop-Abnahme offen. Die folgenden Skill-Bündel enthalten weiterhin keinen MCP-Server.

Stand 2026-10-15. Lokal vorbereitet und vorübergehend nativ in beiden Hosts installiert und getestet; die Testinstallationen sind wieder entfernt. Nichts veröffentlicht oder deployed. Paketversion 0.1.4 bezeichnet einen Review-Build.

Distribution-Metadaten und helle/dunkle Icons sind lokal ergänzt. [Host-Tests und Grenzen](host-tests.md) sowie [Listing-Entwürfe](../store/README.md) dokumentieren den aktuellen Stand; keine Store-Freigabe. Website-Markup bleibt ein eigener lokaler Entwurf in [structured-data.md](structured-data.md).

## Ein Inhalt, drei Installationswege

`bundle.json` wählt ausdrücklich sieben Skills: Start It Right, Are We Cooking?, Did I Leak?, Will They Sue Me?, Let Them See It, What Did We Change und Kill the TODOs (Finish This Chat / Close the Kitchen). Jeder Skill trägt zusätzlich seinen sichtbaren Koch-Titel; technische IDs bleiben gleich. `catalog.json` dokumentiert weiterhin Rezepte, Quellrevisionen und Dateihashes. Daraus entstehen Einzel-ZIPs und zwei Plugin-ZIPs. Die Skill-Dateien bleiben in allen drei Ausgaben bytegleich; nur die Plugin-Manifeste unterscheiden sich. Keine zweite Sammlung manuell gepflegter Skill-Texte.

Alle sieben enthaltenen Skills sind MIT-lizenziert; Are We Cooking? wurde nach ausdrücklicher Lizenzwahl aufgenommen. Neue Skills werden nicht automatisch Teil des Bündels, nur weil sie im Katalog stehen. Die Auswahl muss in bundle.json nach Inhalts-, Rechte- und Verhaltensreview ausdrücklich ergänzt werden.

```sh
python3 scripts/cookbook.py build
python3 scripts/cookbook.py check
python3 -m unittest discover -s tests
```

Ausgabe:

```text
dist/
  codex/
    .agents/plugins/marketplace.json
    plugins/vibe-coding-cookbook/
      .codex-plugin/plugin.json
      skills/<id>/...
      LICENSE
      SOURCES.json
      README.md
      README.de.md
  claude/
    .claude-plugin/marketplace.json
    plugins/vibe-coding-cookbook/
      .claude-plugin/plugin.json
      skills/<id>/...
      LICENSE
      SOURCES.json
      README.md
      README.de.md
site/downloads/
  <skill-id>.zip
  vibe-coding-cookbook-codex.zip
  vibe-coding-cookbook-claude.zip
  SHA256SUMS
```

Die Plugin-ZIPs enthalten jeweils nur den einen Plugin-Ordner inklusive verstecktem Manifest, nicht den Marketplace. Die generierten dist-Ordner enthalten zusätzlich den passenden lokalen Marketplace. dist und site sind ignorierte, reproduzierbare Ausgabe. SOURCES.json im Plugin dokumentiert jedes gebündelte Skill-Byte ohne private Quellpfade.

## Codex: lokaler Review

Codex verwendet hier das weiterhin dokumentierte Kompatibilitätsformat `.codex-plugin/plugin.json` mit `skills: ./skills/`. Das hält die Ausgabe klein und benötigt keinen eigenen MCP-Server. Im generierten Review-Root dist/codex liegt die Registrierung unter `.agents/plugins/marketplace.json`; der darin enthaltene Quellpfad wird vom Marketplace-Root aus aufgelöst.

Lokale Installation aus dem Cookbook-Root:

```sh
codex plugin marketplace add ./dist/codex
codex plugin add vibe-coding-cookbook@cookbook-local
```

Eine neue Sitzung muss alle sieben Plugin-Skills erkennen. Für den finalen Installationstest wurde der Marketplace aus einer separaten Extraktion des finalen ZIPs aufgebaut; native Installation, Cache-Abgleich und Laden aller sieben Skills bestanden. Die Testregistrierung wurde danach entfernt. Codex CLI 0.160.0 wurde verwendet; sichtbare Desktop-Abnahme bleibt offen. Der Build selbst registriert nichts im Host. Das generierte Codex-Manifest setzt seit Review 0.1.4 `requires_local_executor: true` auf oberster Ebene, wie für dieses Kompatibilitätsformat dokumentiert. Die Skills benötigen lokale Werkzeuge; das Claude-Manifest erhält kein Codex-spezifisches Feld. Siehe [Launch-Prüfstand](launch-readiness.md).

## Claude Code: lokale Installation oder einzelne Sitzung

Mit verfügbarem Claude-Code-Binary aus dem Cookbook-Root:

```sh
claude plugin validate ./dist/claude/plugins/vibe-coding-cookbook --strict
claude plugin marketplace add ./dist/claude --scope local
claude plugin install vibe-coding-cookbook@cookbook-local --scope local
```

Danach in einer neuen Sitzung beispielsweise `/vibe-coding-cookbook:let-them-see-it` mit einer konkreten Review-Aufgabe aufrufen. Alternativ ohne Registrierung:

```sh
claude --plugin-dir ./dist/claude/plugins/vibe-coding-cookbook
```

Der Flag zeigt auf den Plugin-Ordner, nicht den Marketplace-Root. Claude Code 2.1.295 aus der vorhandenen lokalen Laufzeit wurde nach Nutzeranmeldung erfolgreich getestet, ohne zusätzlichen Installer. Der finale native Installationstest nutzte ausdrücklich keinen `--plugin-dir`: Alle sieben Skills wurden über die installierte Registrierung erkannt und per Skill-Werkzeug geladen. Bei lokalen Ordner-Marketplaces liest Claude aus dem registrierten Quellordner; Quelle und Cache wurden gegen das finale ZIP abgeglichen. Die temporäre lokale Installation und ihr Marketplace sind wieder entfernt. Frühere gezielte Verhaltenstests und ihre Grenzen stehen in [host-tests.md](host-tests.md). Den verfügbaren Binary-Pfad lokal bestimmen; keine maschinenspezifischen Pfade versionieren.

## Einzelinstallation und optionale Teile

Die bisherigen Einzel-ZIPs und `python3 scripts/cookbook.py install <id> --dest <leeres-ziel>` bleiben bestehen. Wer nur einen Workflow benötigt, installiert diesen Skill. Das Plugin ist ein gemeinsames Bündel; es wird kein plattformübergreifender Installer mit einzeln abwählbaren Skills behauptet. Bedingte Referenzen werden innerhalb eines Skills nur bei Bedarf gelesen.

Bei Vergleichen eine saubere Sitzung verwenden und separate Kopien derselben Skills nicht gleichzeitig aktivieren. Vorhandene Installationen und Originalrepo-Symlinks werden nicht überschrieben. Die unveränderten Anleitungen enthalten teilweise Codex-bezogene Begriffe; Paketgleichheit beweist keine vollständige Claude-Kompatibilität. Die Szenarien in behavior-review.md müssen je Host geprüft werden, insbesondere Quellpfade, verfügbare Werkzeuge und Aufrufkonventionen.

## Nutzung für einzelne Skill-Websites

Die bestehenden Websites bleiben eigenständig und wurden nicht verändert. Langfristig kann jede Seite auf Folgendes verweisen:

1. Den Anker der eigenen Cookbook-Rezeptkarte, beispielsweise site/index.html#let-them-see-it.
2. Das einzelne Skill-ZIP, wenn nur diese Funktion gewünscht ist.
3. Die Codex-/Claude-Bündel als klar beschriftete Alternative: sieben Skills gemeinsam.

Die Downloads stammen aus demselben Build; keine Website pflegt eine zusätzliche Skill-Kopie. Für eine spätere Veröffentlichung einen versionierten Download-Ort festlegen, ZIPs samt SHA256SUMS zusammen bereitstellen und die einzelnen Websites erst nach direkter Freigabe verlinken. Ein lokaler dist-Pfad oder eine 127.0.0.1-Adresse ist kein öffentlicher Download. Websites, Repositories und Installationspakete sind getrennte Flächen und müssen nicht dieselbe Repo-Aufteilung haben.

## Formatquellen

- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins) — Codex-Kompatibilitätsformat und lokale Marketplaces.
- [Claude Code: Create a plugin](https://code.claude.com/docs/en/plugins/create) — Layout, Validierung und lokale Sitzung.
- [Claude Code: Manifest reference](https://code.claude.com/docs/en/plugins-reference) — Manifest-Felder und Pfadregeln.

Am 2026-10-15 gelesen. Diese Referenzen begründen das Paketformat; ein erfolgreicher Host-Test wird separat dokumentiert.
