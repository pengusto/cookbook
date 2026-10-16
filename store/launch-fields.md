# Noch einzusetzende Store-Angaben / Remaining store inputs

Lokale Vorbereitung 2026-10-15. Die vorhandenen Listing-Texte, Namen, Icons, Keywords und Starter-Prompts sind im Build enthalten. Die folgenden Angaben werden erst mit bestätigten öffentlichen Zielen ergänzt; keine ausgedachten URLs im Paket.

| Benötigtes Ziel | Codex `interface` | Claude `plugin.json` |
|---|---|---|
| Öffentliche Produkt-/Dokumentationsseite | `websiteURL` | `documentationUrl` |
| Tatsächlicher Supportkanal | `supportURL` | `supportUrl` |
| Hosting-/Produkt-Datenschutzerklärung | `privacyPolicyURL` | `privacyPolicyUrl` |
| Tatsächlich geltende Nutzungsbedingungen, falls benötigt | `termsOfServiceURL` | `termsOfServiceUrl` |

Für das Codex-Skills-only-Paket sind nicht alle vier URLs automatisch Pflicht der Metadatenvalidierung. Bei einer öffentlich zu prüfenden MCP-App sind sie laut OpenAI erforderlich. Claude verlangt bei Verwendung HTTPS-URLs. Kein zweckfremdes Help-Fragment als fertige Rechtstextseite einsetzen.

Zusätzlich zu bestätigen: öffentliches Repository samt gewünschtem Marketplace-Installationsbefehl, verifizierter Publisher und Directory-Kategorie im echten Portal. `Pengusto` ist das lokale Autorenlabel; damit ist keine geprüfte rechtliche Identität behauptet. Identitätsnachweise gehören nicht ins Repository.

Website: Domain und Hosting zuerst festlegen, dann Anbieterkennzeichnung, Datenschutz, Support und gegebenenfalls Bedingungen vervollständigen. Anschließend Canonical, Sitemap, Social-Preview und JSON-LD mit realen URLs ergänzen. Öffentliche Metadaten gehören erst in einen erneut geprüften Release-Build. Die aktuelle Review-Website bleibt `noindex,nofollow`.

Für die optionale Sidebar-App ist die Partnerfreischaltung für lokale MCP-Einreichungen ein zusätzlicher Gate. Das Skills-only-Bündel und die lokale Sidebar-App getrennt einreichen und beschreiben.

English: Listing text and image assets are prepared. Confirm actual public documentation, support, privacy and applicable terms destinations before inserting their host-specific fields. Verify publisher identity in the portal. Do not publish private paths, identity evidence or placeholder URLs. The local MCP sidebar has a separate partner eligibility requirement.

Siehe [Launch-Bericht](../docs/launch-readiness.md) und dessen offizielle Referenzen.
