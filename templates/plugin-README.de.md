# Vibe Coding Cookbook — lokaler Plugin-Review

[English](README.md) · [Deutsch](README.de.md)

Dieses Skills-Bündel enthält Start It Right, Check Progress (Are We Cooking?), Did I Leak?, Will They Sue Me?, Let Them See It, What Did We Change und Finish This Chat (Close the Kitchen). Es ergänzt keine Hooks, MCP-Server, Konten oder Hintergrunddienste. Did I Leak benötigt bei Nutzung Python/Git und meldet optionale Scanner; rechtliche Aussagen im Produktreview benötigen aktuelle Primärquellen.

Der versteckte Manifest-Ordner zeigt das Ziel: `.codex-plugin` für Codex, `.claude-plugin` für Claude Code. Das ZIP enthält einen Plugin-Ordner, keinen Marketplace und keinen einzelnen Skill. Versteckte Dateien beim Entpacken erhalten. Version 0.1.4 bezeichnet den privaten Review-Build, keinen veröffentlichten Release.

## Lokal verwenden

Claude Code: Im entpackten Claude-Plugin-Ordner `claude plugin validate .` ausführen, danach mit `claude --plugin-dir .` eine isolierte Review-Sitzung starten. Darin `/vibe-coding-cookbook:let-them-see-it` mit deiner Aufgabe aufrufen. Beim Vergleich nicht gleichzeitig das Bündel und separate Kopien derselben Skills aktivieren.

Codex: Den entpackten Codex-Ordner in einem gewählten Review-Projekt unter `plugins/vibe-coding-cookbook` ablegen. Am Projektroot `.agents/plugins/marketplace.json` anlegen:

```json
{
  "name": "cookbook-local",
  "plugins": [{
    "name": "vibe-coding-cookbook",
    "source": {"source": "local", "path": "./plugins/vibe-coding-cookbook"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
    "category": "Developer Tools"
  }]
}
```

Den lokalen Desktop-Host neu laden und das verfügbare Plugin über dessen Plugin-Oberfläche prüfen/installieren. Entpacken allein installiert es nicht. Erkennung und Skill-Aufruf sind im jeweiligen Host zu verifizieren; die lokale Testregistrierung ist vorübergehend und wird nach Prüfung entfernt. Der Cookbook-Build erzeugt dieses komplette Review-Projekt zusätzlich unter `dist/codex/`.

## Inhalt und Grenzen

`SOURCES.json` dokumentiert Quellrevisionen und exakte SHA-256-Hashes jeder gebündelten Skill-Datei. Jede `skills/<id>/LICENSE` behält ihren Originalvermerk; die MIT-Lizenz am Root gilt für Cookbook-Verpackung und Texte. Are We Cooking? ist nach ausdrücklicher MIT-Lizenzwahl ebenfalls enthalten.

Einzelne Skills bleiben über die jeweiligen Cookbook-ZIPs separat installierbar. Aus diesem Archiv lässt sich auch der vollständige Ordner `skills/<id>` in ein leeres, zum Host passendes Skill-Ziel kopieren; Referenzen, Skripte und Lizenz erhalten. Bestehende Skills nicht überschreiben und den Plugin-Root nicht als einen Skill installieren.

Die Skill-Dateien sind geprüfte Quell-Snapshots. Für die fünf bisherigen Skills liegen authentifizierte Claude-Verhaltenstests vor; der Abschluss-Workflow ist separat unter Codex und Claude getestet. Paketgleichheit beweist kein identisches Host-Verhalten. Aktuelle Abdeckung und Grenzen stehen im Host-Testbericht des Cookbook. Nichts ist veröffentlicht.

Formatquellen: [Codex-Plugins](https://developers.openai.com/plugins/build/plugins), [Claude-Code-Plugins](https://code.claude.com/docs/en/plugins/create). Paketformate geprüft am 2026-10-15.
