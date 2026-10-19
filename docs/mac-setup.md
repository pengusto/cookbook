# Cookbook auf einem anderen Mac

Das Beta-Repo ist https://github.com/pengusto/cookbook. Auf dem zweiten Mac brauchst du Git, Python 3.10+ sowie Codex und/oder Claude Code. Melde dich in den jeweiligen Apps separat an; das Repo enthält keine Zugangsdaten.

## Erstmalig klonen und bauen

```sh
git clone https://github.com/pengusto/cookbook.git
cd cookbook
python3 scripts/launch_check.py
```

Der Check baut die Pakete, prüft die gemeinsamen Quellen, führt Tests aus und vergleicht einen portablen Neubau. `dist/` und `site/` werden lokal erzeugt. Es werden keine bisherigen Einzelrepos benötigt. Der gewählte Checkout-Pfad sollte anschließend bestehen bleiben, weil lokale Marketplace-Registrierungen darauf zeigen.

## Genau eine Namenswelt wählen

`plain` = einfache Fragen, `kitchen` = Koch-Namen. Alle folgenden Beispiele zeigen Kitchen. Für Plain nur `kitchen` im Pfad ersetzen. Niemals beide Varianten oder zusätzlich die alten gleichartigen Einzel-Skills aktivieren.

Vor der ersten Installation in der Plugin-Verwaltung prüfen, ob `vibe-coding-cookbook` oder einzelne Kopien schon installiert sind. Diese erst bewusst sichern und deaktivieren/ablösen. Der Build verändert sie nicht.

Codex:

```sh
codex plugin marketplace add ./dist/kitchen/codex
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Claude Code, falls `claude` auf dem PATH verfügbar ist:

```sh
claude plugin marketplace add ./dist/kitchen/claude --scope user
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

Danach neue Host-Sitzung starten bzw. die App neu laden und genau acht Skills in der gewählten Namenswelt prüfen. In Claude heißen Aufrufe z. B. `/cookbook-by-pengusto:close-the-kitchen`, in Codex `$close-the-kitchen`. Die optionale Sidebar ist separat; sie ist für die Skills nicht notwendig.

## Spätere Updates

Im vorhandenen Checkout:

```sh
git status --short
git pull --ff-only
python3 scripts/launch_check.py
```

Eigene Änderungen vorher committen oder separat sichern. Bei Fehlern stoppen; kein Reset, kein Force-Pull. Der Pull aktualisiert ausschließlich freigegebene Commits auf GitHub. Änderungen auf dem ersten Mac müssen dafür bewusst committet und gepusht werden.

Ein Neubau aktualisiert noch keinen bereits zwischengespeicherten Plugin-Inhalt. Für einen sicheren Refresh auch bei gleicher Paketversion: zuvor die bisher installierte Paketkopie außerhalb von `dist/` sichern, das Cookbook-Plugin gezielt nativ entfernen und aus dem bestehenden lokalen Marketplace neu installieren. Nur ausführen, wenn es schon installiert ist:

```sh
codex plugin remove cookbook-by-pengusto@cookbook-by-pengusto-local
codex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local
```

Claude Code:

```sh
claude plugin uninstall cookbook-by-pengusto@cookbook-by-pengusto-local --scope user --keep-data
claude plugin install cookbook-by-pengusto@cookbook-by-pengusto-local --scope user
```

Damit wird ausschließlich der native Cache dieses Plugins ersetzt; Quellen und Git-Historie bleiben erhalten. Bei einem Variantenwechsel zusätzlich nur den Cookbook-Marketplace abmelden und den anderen lokalen Pfad registrieren, wie in der Haupt-README beschrieben. Kein automatischer Variantenwechsel und kein Hintergrund-Updater. Neue Host-Sitzung starten und Namen/Anzahl erneut prüfen.

## Grenzen

Das öffentliche Beta-Repository ist keine Store-Einreichung und veröffentlicht keine Website. Authentifizierung und sichtbare Desktop-Abnahme auf dem zweiten Mac stehen dort noch aus. Historische `history/*`-Branches bewahren die früheren Repos; ihre Commits sind außerdem Vorfahren von `main`. Die vier früheren GitHub-Einzelrepos wurden auf Maintainer-Wunsch entfernt; ihre importierte Git-Historie bleibt im Cookbook erhalten.
