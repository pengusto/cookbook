# Pflege und Provenienz

## Kleine Struktur

- catalog.json: kuratierte Rezepte und exakte Dateihashes; die einzige shareable Auswahl-Datei.
- skills/<id>/: geprüfte Kopien, keine zweiten editierbaren Originalprojekte.
- scripts/cookbook.py: Build, Check, Driftprüfung, explizite Installation und Loopback-Vorschau.
- templates/index.html: lokale Darstellung ohne externe Abhängigkeiten.
- docs/: Auswahl, Rechte, Evaluation und Übergabe; übersetzte README unter docs/readme/.
- site/: generierte Vorschau, ZIPs und SHA256SUMS; nicht versioniert.
- bundle.json: ausdrückliche Auswahl für Codex-/Claude-Plugin-Bündel, mit gemeinsamer Review-Version.
- dist/: generierte Plugin-Ordner und lokale Marketplaces; nicht versioniert. Nur im Build erzeugen, nie separat editieren.
- sources.local.json und .scratch/: ignorierte lokale Quellzuordnung und private Review-Evidenz.

## Gezielte Aktualisierung

1. `python3 scripts/cookbook.py check-sources` vergleicht ausgewählte Bytes mit lokalen Originalen. Ohne lokale Registry bleibt der portable Build vollständig nutzbar.
2. Im betroffenen Original Änderungen, Git-Status und Rechte prüfen. Für Vergleiche gegen einen Remote zuerst dessen relevanten Stand fetchen; lokale Hashes sind keine Aussage über Remote-Gleichheit.
3. Nur die bisher erlaubten Dateien aus catalog.json im Original prüfen. Neue Abhängigkeiten/Referenzen bewusst hinzufügen, keine ganzen Ordner automatisch exportieren. Keine Originale umbenennen oder verschieben; nur ausdrücklich beauftragte Änderungen am Original durchführen.
4. Den ausgewählten Skill-Snapshot nach Review ersetzen; Original-LICENSE erhalten. Pro Datei SHA-256 über die exakten Bytes ermitteln, beispielsweise mit `shasum -a 256 skills/<id>/SKILL.md`. Revision nur angeben, wenn sie im owning Git-Repository belegt ist; uncommittete Änderungen im privaten Prüfprotokoll kennzeichnen.
5. catalog.json aktualisieren; Rezept, Grenzen und beide README-Versionen bei verändertem Ablauf synchronisieren. Paketnamen bleiben die Skill-ID. Entfernte Skills samt alten generierten ZIPs bewusst bereinigen, damit keine veralteten Downloads verbleiben.
6. Build, Check und Tests laufen lassen; zwei Builds müssen identische ZIP-Hashes ergeben. Isolierte Installation und relevante Verhaltensszenarien prüfen. Keine produktive Installation automatisch ersetzen.
7. Erst danach Cookbook-Diff reviewen und einen lokalen Commit erwägen. Push, Release und Deployment benötigen eine direkte Freigabe.

Die Originale sind nicht Teil der Cookbook-Git-Historie. Der Katalog verlinkt Quellprojekte, behauptet aber weder deren öffentliche Sichtbarkeit noch Remote-Aktualität. Alle sieben Quellen haben eigene lokale Git-Repositories. Die Namensänderungen in den vier bestehenden GitHub-Quellen sind weiterhin uncommittet. Are We Cooking, What Did We Change und der Abschluss-Skill haben seit der lokalen Repository-Vorbereitung eigene lokale Commits; keine neuen Remotes oder Pushes. Dateihashes identifizieren die Snapshots unabhängig davon. Siehe [Repository-Stand](repositories.md). Are We Cooking ist nach ausdrücklicher MIT-Lizenzwahl ebenfalls redistribuierbar aufgenommen. Aktuelle Rechtsquellen sind bei jedem konkreten Will-They-Sue-Me-Review zu prüfen; die gebündelten Referenzen sind Einstiegspunkte.

## Installationsvertrag

Ein ZIP enthält <id>/SKILL.md plus erlaubte Runtime-Dateien und Original-LICENSE. Der Installer prüft Hashes und lehnt vorhandene Ziele einschließlich dangling symlinks ab. Keine Globalinstallation wurde in dieser Vorbereitung vorgenommen. Für einen bereits installierten Skill das Original oder bestehende Symlink-Ziel pflegen; keine automatische Cookbook-Kopie darüber schreiben.
