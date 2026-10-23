# Pflege und gemeinsame Quelle

## Namen und Referenzen

Der Projektname ist **Cookbook by Pengusto**, das GitHub-Repository heißt [`pengusto/cookbook`](https://github.com/pengusto/cookbook). Öffentliche Quellcode-, Issue-, Clone- und Marketplace-Referenzen verwenden dieses Repository; die Website liegt unter `https://pengusto.github.io/cookbook/`. Die technische Plugin-ID bleibt `cookbook-by-pengusto`, die Marketplace-ID `cookbook-by-pengusto-local`; beide Varianten teilen diese Identität. Der lokale übergeordnete Ordnername ist keine öffentliche Repository-Referenz.

Frühere Namen in datierten Prüfberichten, importierter Herkunft und alten Installationsnachweisen bleiben als historische Belege erhalten. Sie sind keine aktuellen Installations- oder Veröffentlichungsziele. Aktuelle Namen und Befehle stehen in der [README](../README.md).

## Gemeinsame Quelle

Seit Review 0.2.0 ist dieses Repo die einzige gepflegte Quelle. `skills/<stabile-id>/` enthält die vierzehn Workflows; catalog.json wählt Laufzeitdateien aus, hält SHA256 und legt die beiden Namenswelten fest. Original-LICENSE bleibt pro Workflow erhalten. Neue Runtime-Dateien bewusst in die Allowlist aufnehmen; nichts automatisch aus anderen Repos synchronisieren.

SKILL.md behält die stabile Quell-ID im Frontmatter. Überschrift und Host-Metadaten verwenden `{{TITLE}}`, Selbstaufrufe `{{ID}}`. Beim Paketbau werden nur diese Namen/Aufrufe und die installierte Frontmatter-ID ersetzt; der Ablauf wird nicht dupliziert. Direkte Installation der Vorlagen ist nicht vorgesehen.

Nach einer Inhaltsänderung die betroffenen Hashes in catalog.json aktualisieren und Build, Check, check-sources, Tests und portablen Neubau ausführen. `check-sources` prüft jetzt die gemeinsamen lokalen Quellen, nicht mehr externe Archive. Dateien, Symlinks und unerwartete Runtime-Dateien bleiben durch die Paketverträge geschützt.

site/ und dist/ sind generierte ignorierte Ausgaben; niemals manuell pflegen. .scratch/ und die frühere sources.local.json bleiben ignoriert. Alte 0.1.x-dist-Ordner werden für bestehende Installationen erhalten, aber nicht mehr gebaut; die neuen aktiven Ziele sind dist/plain und dist/kitchen. Für die neue Website wurde die vorherige generierte Ausgabe vollständig unter .scratch/consolidation/website-before-0.2.0 erhalten.

Beide Namenswelten nutzen dieselbe Plugin-/Marketplace-Identität. Für einen Wechsel das bisherige Paket sichern und nativ wechseln; ein identisches Versionscache darf nicht als Nachweis der anderen Variante gelten. Einzelinstaller verweigert parallele Varianten desselben Workflows. Kein automatischer Host-Wechsel beim Build.

Die sieben vollständigen Git-Historien sind als history/* und über einen Merge ohne Squash als Vorfahren von main erhalten. Keine history/*-Branches entfernen. Die vier alten GitHub-Repos wurden am 2026-10-18 auf Nutzerwunsch gelöscht; die sieben importierten Historien bleiben erhalten. Der achte Skill what-was-i-cooking wurde aus einer nicht versionierten, selbst verfassten Quelle integriert; Herkunft und Lizenz stehen in docs/skill-naming.md. Vor einer späteren Veröffentlichung die gesamte importierte Historie einschließlich privater Ursprünge prüfen; nichts pushen oder veröffentlichen ohne ausdrückliche Freigabe.

## You Got This · lokale Übernahme 0.6.0

`you-got-this` / `youre-the-chef` ist der Ausführungsworkflow vom Projektziel bis zum geprüften Ergebnis. Die Einzelquelle samt ursprünglicher MIT-Lizenz wurde übernommen; Herkunft, Abgrenzung und weiterhin erhaltenes Originalrepo stehen in [you-got-this-import.md](you-got-this-import.md). Keine Installation, Veröffentlichung oder Archivierung durch den Build.
