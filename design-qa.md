# Cookbook reference alignment

Source visual truth: `.scratch/landing-review/reference.png` (selected green-white mockup, 1024 × 1536). Implementation: `.scratch/landing-review/reference-desktop-final.png`; normalized comparison `.scratch/landing-review/comparison-final.jpg`. State: German Kitchen, all details collapsed, top of page.

CSS viewport 1024 × 1536. Browser zoom reports devicePixelRatio 0.8 and exports a padded 1280 × 1920 surface; comparison uses its top-left 1024 × 1536 content region without stretching. Mobile checks used actual CSS widths 390 and 320, not the requested physical override values.

## Findings and comparison history

- Earlier P1: landscape image with excessive empty space made the book and pan much smaller than the selected reference. Replaced with a portrait image generated with that exact reference attached. Original retained until acceptance.
- Earlier P2: buttons and naming switch lacked their book, download, chef and conversation symbols. Added vendored MIT Tabler assets and retained text labels.
- Earlier P2: rows omitted numbers and had small icons. Added 01–07, larger icon circles and consistent arrow controls.
- During verification, browser caching mixed new HTML with old CSS. Added content-based asset query versions; local link validation now resolves the URL path. A first capture exposed overflow from that stale combination; final capture and 320/390 checks have none.
- Final P3: the existing Cookbook book-and-pan logo is retained rather than the mock's standalone pan. System-font glyph shapes and the generated photography are close interpretations, not pixel-identical source assets. Exact workflow summaries intentionally retain the approved catalog's narrower claims.

## Required fidelity surfaces

- Typography: three-line large forest-green hero, compact navigation and bold row titles. Adjusted tablet headline to 69px and section title to 40px after comparison; system font remains dependency-free.
- Spacing: measured hero starts below the header, list begins around CSS y807 as in the source; numbered rows, separators, icon circles and pill switch follow the source. Small-screen layout stacks without horizontal overflow.
- Color: white, forest green, orange CTAs, pale neutral circles and thin gray-green rules. Selected/hover/focus states remain visible.
- Images: separate sharp portrait book/pan illustration, no screenshot used as the website. Standard icons are licensed external SVG assets, locally served through masks; previous custom row drawings removed.
- Content: seven canonical skills and unchanged invocation IDs; DE/EN and Plain/Kitchen stay aligned. Local release status and verified package instructions remain below the reference's depicted area.

Full comparison: `.scratch/landing-review/comparison-final.jpg`. Focused hero/buttons: `.scratch/landing-review/compare-hero.jpg`. Focused row icons, rules and descriptions: `.scratch/landing-review/compare-rows.jpg`. These were opened together with the source and implementation for visual inspection.

## Verification

19 automated tests, source/hash/package/link checks and portable rebuild passed. Browser: native skill disclosure opened with the correct invocation/download; English navigation and Plain questions switched to the seven correct titles; German/Kitchen navigation preserved the chosen language; no horizontal overflow at 1024, 390 or 320 CSS pixels; zero broken images in the desktop check and no recorded console errors. Export allowlist includes only the specific vendored icons and their license/readme.

## Implementation checklist

- [x] Replace hero with reference-aligned portrait asset.
- [x] Add library symbols, numbered rows and matching CTA treatment.
- [x] Check reference and focused crops, desktop/mobile and primary navigation.
- [x] Complete existing automated checks.
- [ ] User visual acceptance; optional P3 logo/font refinement afterward.

Previous complete project commit 8ff03a4 is on private GitHub. This subsequent design revision is local. No website deployment or store publication.

final result: passed

## Skill-icon follow-up

Seven skill symbols replaced with finer 1.5-stroke Lucide assets: cooking pot and serving cloche now match the selected motives. Native browser screenshot verified the outline rendering and all seven motifs. At the intermediate browser width the naming heading squeezed the switch; added a wrapping breakpoint at 761–1000 CSS pixels. Previous icon files retained locally for design acceptance.

## Dark-mode follow-up

System dark styles and matching generated hero added. Evidence: .scratch/public-release/dark-desktop.png and dark-mobile.png. Browser API lacks color-scheme emulation: isolated local HTML/CSS fixtures force only the dark/light media branches, while production files retain prefers-color-scheme. Verified dark body rgb(17,27,23), foreground rgb(240,245,239), light brand asset, dark hero, seven readable icons, disclosure and help page; light branch restores white background and light hero. No broken images, overflow at actual 320 CSS px, or console errors observed. Test fixture copies are removed after capture; screenshots retained through acceptance. Final result remains passed for the described scope; no claim of a physical OS theme-switch test.
