## GitHub Pages completion check

Apply this section when GitHub Pages is part of the approved scope. Reuse an existing repository and its declared package manager, build and deployment workflow. If installed, use `publish-to-pages` for its applicable prerequisite, input and publishing steps. Its single-file publishing script is suitable for standalone HTML or converted documents; do not use it to replace an existing application workflow, publish source as the site, or create a duplicate repository.

Before deployment:

- Confirm the owner, repository, visibility, intended branch and commit, and whether this is a project site (`/<repo>/`) or a root/custom-domain site. Preserve existing publication authorization; preparation alone does not authorize publishing.
- Run the real production build with the intended base path. Verify that the framework produces a supported static artifact and that HTML, scripts, styles, images, favicon, workers, runtime files, downloads and legal/docs links resolve under that path. Test direct navigation and reload as well as the home page.
- Reuse CI for meaningful build and behavior checks. Check Pages configuration, artifact directory, least-required permissions and deployment dependencies. Do not add redundant deployment workflows or commit generated output unless the repository explicitly uses that model.

After an authorized deployment:

- Follow the existing CI and Pages deployment to a terminal result, using bounded waits. Record the workflow run URL, deployed source SHA and reported site URL. A push or successful build alone is not a completed deployment.
- Open the live URL in a browser and verify meaningful rendered content, one core interaction, navigation/reload and required assets. Check browser errors and failed required requests. Use the repository's subpath in every test. An HTTP 200 response alone is not browser proof.
- Link the working demo in the primary README, approved README translations and GitHub About website field. Verify link destinations and report unavailable metadata permissions instead of claiming completion.
- Confirm the deployed SHA matches the intended commit using deployment/run evidence. Distinguish local, committed, pushed, CI-passed, deployed and browser-verified states, and state any remaining gap explicitly.

For an existing successful deployment, verify it before triggering another run. Report the repository, live page, deployment evidence and exact verification boundaries. Do not claim installation counts, test coverage or release status without current evidence.

