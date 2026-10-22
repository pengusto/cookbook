# Module catalog

Use this as a routing table, not as a checklist to apply everywhere.

| Signal | Recommend | Produces |
|---|---|---|
| New or unclear idea | Product brief and smallest useful flow | README or project brief |
| Unproven demand or crowded space | Research and alternatives check | research note, validation ticket |
| Several plausible product or architecture paths | Let Him Grill or inline decision gate | decision record, selected path |
| Durable multi-step work needs tracking | Existing tracker or versioned tickets | `docs/tickets/<slug>/ticket.md` |
| UI direction is still open | UI evaluation ticket | screenshots, decisions, prototype ticket |
| Multiple languages, regions, locale data, or RTL | i18n | locale contract and translation plan |
| Public source distribution | License decision and pre-publication scan | license, README/legal notes |
| Accounts or personal data | Auth, roles, privacy, deletion, retention | data/auth contract |
| External API or provider | Integration boundary and failure behavior | API/integration ticket |
| Persistent data | Schema, migration, backup, restore | data contract and recovery check |
| Visible human prose or content fixtures | Stop Slop; Deslopify only for a deeper pass | reviewed prose or fixture set |
| News, research, or public claims | Sources, evidence, rights, human approval | editorial contract and gate |
| Public website | Accessibility, SEO, legal pages, browser QA | audit and smoke evidence |
| Browser extension or store app | Permissions, packaging, store/privacy material | review checklist and artifact |
| Service or VPS runtime | Health, readiness, logs, monitoring, rollback | operations runbook |
| Reusable skill | `SKILL.md`, UI metadata, examples, validator | installable skill package |
| Public release | Changelog, version, tag, CI, reproducible artifact | release checklist |
| Need to learn from usage | KPI or feedback plan | measurement/feedback ticket |

## Always recommended at the right stage

Recommend a next executable action when useful work remains; accept a completed slice. A tiny project may only
get “write the product promise and test one path”. A public extension may get a
larger batch covering permissions, browser smoke, packaging, license, and store
copy.

## License gate

Do not select a license silently. Ask whether the project is private or public,
whether commercial reuse is allowed, whether copyleft is desired, and whether
code, documentation, images, and generated assets need separate treatment.
Candidates include no license for private work, MIT, Apache-2.0, GPL-3.0,
AGPL-3.0, proprietary, or separate licenses by asset type.

## i18n gate

Do not treat i18n as a translation-only task. Consider locale fallback,
dates, numbers, currencies, pluralization, text expansion, RTL, content
ownership, and localized URLs or SEO. Recommend it when the product's audience
or data makes those decisions relevant.
