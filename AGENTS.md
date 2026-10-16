# Cookbook maintenance

- Original projects are the only editable skill sources. `skills/` holds reviewed snapshots; never silently patch them independently.
- `catalog.json` is the curated selection, recipes, and per-file provenance. Keep absolute source paths in ignored `sources.local.json` only.
- Use Python standard library. Reuse skill-library for broad inventory; do not replace its registry or modify installations during catalog work.
- Update only explicitly reviewed runtime files, preserve each source LICENSE, update hashes and revision together. Never export entire repositories.
- Run build, check, check-sources where local sources exist, and unittest after packaging changes. Keep EN/DE documentation synchronized.
- Packaging checks are not independent agent behavior tests. No publication, external messages, remote creation or deployment without direct authorization.
- `bundle.json` explicitly selects the shared plugin contents. Generate Codex/Claude manifests, local marketplaces and ZIPs from it; never edit ignored `dist/` output. Preserve byte-identical skill files across individual and bundled packages.
