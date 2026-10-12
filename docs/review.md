# Maintainer review and publication handoff

## Prepared scope

- Experimental agent skill with a conditional twenty-area review map and Germany/EU research entry points.
- English and German README, MIT license, Codex UI metadata.
- Static landing page, downloadable reproducible skill ZIP and project-path local preview.
- CI package/link checks and private review artifact; manual-only Pages workflow.

## Review before publication

1. Review the skill's findings contract and scenarios. Test it on an actual isolated product before relying on its recommendations.
2. Confirm operator identification and privacy-controller/contact information applicable to the public landing page. The pre-publication privacy page flags the missing operator information; it is not a complete legal notice. Do not invent an address or copy private information into the repository.
3. Confirm release readiness and website visibility. Publishing from a private repository may expose the site and downloadable package publicly.
4. Check available Pages plan and repository settings; the repo is not made public automatically. If appropriate, configure Pages to use GitHub Actions, then manually dispatch the Pages workflow with `PUBLISH` only after explicit approval.
5. Inspect the completed run, deployed SHA and actual live site. Test download, prompt copy, documentation, privacy link and mobile layout under `/will-they-sue-me/`.
6. Only after verified deployment, add the live demo to the READMEs and GitHub About website field. Do not use an expected URL as proof of deployment.

## Useful GitHub surfaces

Repository description and focused topics help explain the product. CI provides a repeatable build and private downloadable review artifact. A release can wait for a meaningful version and behavioral evidence. Discussions, Sponsors, funding links and citation metadata are unnecessary for this initial skill. No maintenance SLA, security mailbox or social proof is invented.

## Checks to record in the review

- `python3 scripts/project.py check`: metadata, local links, artifact boundaries, package hashes, ZIP integrity and reproducibility.
- Skill creator's `quick_validate.py`: frontmatter and skill conventions, when available.
- Browser checks: desktop/mobile, navigation and download, copied prompt and console/network errors.
- Secret scanner: tracked working tree and reachable history; record scanner coverage, never secret values.
- Fresh-clone install: generated `dist/skill/` works without local untracked files; distinguish installation proof from agent execution.
- CI terminal result, remote visibility and local/remote commit match.

External source links and third-party action versions can drift; verify them before deployment. The package is intentionally dependency-free at runtime and no other skill is required to use it.

## Initial verification — 2026-10-12

- Project checks and official skill-creator validator passed.
- Installation into an isolated skill directory from a fresh committed checkout passed the same checks and official validator. This verifies installation structure, not independent agent behavior.
- Browser review at desktop and emulated 320 px: no horizontal overflow, required site/download/doc links returned 200, prompt-copy interaction succeeded, no browser console warnings/errors were observed. The landing page made no external asset requests.
- Gitleaks inspected the working directory and the one-commit reachable history with redaction enabled; no findings. This is scanner coverage, not proof of absence of all sensitive material or of third-party rights.
- The first private GitHub CI run completed successfully: [review build](https://github.com/pengusto/will-they-sue-me/actions/runs/38249262016). Repository visibility was verified as private. Pages was not configured or dispatched; no live deployment is claimed.
- Behavioral scenarios received an author instruction walkthrough only. Independent agent executions, a live-product audit and qualified legal review remain separate verification steps.
- Retained naming alternative: [Can I Serve This?](naming.md). The current name remains unchanged.

Outcome: **ready for private maintainer review, with stated publication limitations**. Operator/privacy information and explicit publication approval remain required for public launch.
