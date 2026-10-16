# Cookbook by Pengusto maintenance

- This repository is the single maintained source. Edit workflow content only in `skills/<stable-id>/`; original repositories are retained archives, not live dependencies.
- `catalog.json` holds one runtime allowlist and hashes per source, and plain/kitchen display names and invocation IDs. Regenerate hashes after reviewed source changes.
- Render the two naming variants from the same source. Never maintain separate workflow bodies or expose both naming worlds within one installed variant.
- Both variants use the same plugin identity and marketplace name; install one variant at a time. Never silently overwrite existing host installations.
- Preserve LICENSE files, imported history/* branches and merge ancestry. No deletion, remote creation, push, deployment or publication without direct authorization.
- Use Python standard library. Run build, check, check-sources, unit tests and the portable rebuild after packaging changes.
- Generated site/, dist/, private .scratch/ and legacy sources.local.json remain ignored. Never edit generated outputs manually. Keep EN/DE instructions aligned.
