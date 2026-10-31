# Assets and licenses

Cookbook's original code, documentation and thirteen skill sources use MIT licenses; each source retains its own LICENSE. Imported Git histories retain their original attribution and files.

Website icons in `assets/icons/` are from Tabler (MIT) and Lucide (ISC, with some MIT-derived portions); see the included LICENSE, LUCIDE-LICENSE and README for per-file sources. Lucide skill icons use a thinner 1.5 stroke. These assets are included in the website export with their license texts.

`assets/cookbook-hero-transparent.png` and the preserved original JPEG illustrations are AI-generated brand illustrations prepared from the maintainer-selected visual concept. They illustrate a skill collection, not a physical product. No external font or stock-photo service is required. The repository license is not a claim of exclusive rights to generated artwork, third-party trademarks, or historical vendor material.

The product and documentation mention Codex, Claude Code, GitHub and their respective owners solely to identify supported tools. Cookbook is an independent project; no affiliation or endorsement is implied.

The optional Cookbook sidebar bundles Anime.js 4.5.0 from the official juliangarnier/anime repository (MIT) and Cormorant Garamond / Caveat from Google Fonts (SIL Open Font License). Source records, checksums and license texts are in `assets/vendor/`; the sidebar package includes the license texts. Assets are embedded locally, with no runtime font or animation CDN.

The individual cookbook recipe illustrations and decorative sheet in `assets/cookbook/` were generated for this project. `SOURCES.json` records the delivered recipe image hashes; the original generated images are preserved separately.

## README banner illustrations

`assets/readme/cookbook-banner-storybook-v3.png` (light) and `assets/readme/cookbook-banner-storybook-dark.png` (dark) are AI-generated illustrations selected by the maintainer. The supplied profile illustration was used as a penguin identity reference, with the existing Cookbook logo as a brand reference. They depict a kitchen rising from an open recipe book; they are not product screenshots or evidence of host acceptance. The dark companion preserves the same scene and character while adapting background, lettering and lighting for contrast.

The eight READMEs select the appropriate image with native `picture/source` markup. No automatic image generation or new update service is added. Source roles, generation prompts and SHA-256 checksums are recorded in [the banner source record](assets/readme/SOURCES.json). Original logo masters and font notices remain unchanged. Generated artwork carries no claim of exclusive rights or trademark clearance.

The open cookbook embeds Lenis 1.3.27 (MIT) from darkroomengineering/lenis for desktop scroll smoothing. Runtime, stylesheet, pinned source records and license are vendored under `assets/vendor/lenis/`; the offline companion includes the license. No CDN is contacted at runtime.

`assets/cookbook/food/` contains seventeen AI-generated dish-and-ingredient illustration sheets, one for each workflow or information page. The built-in image generator produced the originals; existing cwebp tooling encoded runtime WebP copies. Per-sheet subjects, prompt records, original/runtime checksums and historical sprite regions and 85 separate padded square cutouts (dimensions, method and checksums) are in `assets/cookbook/food/SOURCES.json`. Original generated PNGs and earlier illustrations are preserved. The artwork is a visual metaphor for coding workflows, not evidence of real cooking instructions or product screenshots.

The square food cutouts were prepared once with Pillow from the bundled workspace runtime, separating alpha-connected painted silhouettes and preserving translucent edges and crumbs. These prepared assets add no runtime or build dependency. Original illustration sheets remain intact.

The preserved You Got This paper-atelier banner pair is historical AI-generated design work, not the Cookbook product banner. Exact prompts, checksums, source roles and rights reservations are in [design/you-got-this-retirement/SOURCES.json](design/you-got-this-retirement/SOURCES.json). The original MIT workflow attribution and imported Git histories remain intact.
