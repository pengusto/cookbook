---
name: name-that-dish
description: Generate, compare and refine product, project or skill names from the user's brief and existing naming conventions. For Cookbook skills, propose paired Plain and Kitchen names with both invocation IDs and a short rationale. Use for naming or renaming requests, not for release notes. Do not infer a name selection from a question.
---

# Name That Dish

Find names people can naturally say around the product's use. Match the user's language while respecting the product's chosen naming language.

## Read the naming context

Use the supplied brief, audience, desired feeling and current project metadata. Inspect a small relevant sample of existing names when useful; treat existing names as reserved for new candidates. Do not search unrelated personal projects or require a private naming corpus. Distinguish user choices from exploratory questions and assistant recommendations.

Identify the usage moment, intended outcome, one concrete object and a strong verb. Ask one question only if the purpose cannot be inferred; otherwise state the assumption. Keep technical or internal tools descriptive where playful branding would confuse.

## Generate paired variants when relevant

For Cookbook, default to paired Plain/Kitchen proposals unless the user requests one side. Plain makes the action or question understandable. Kitchen uses the cookbook's spoken culinary tone through preparation, cooking, recipes, dishes or serving. Prefer short natural English and Title Case; a pronoun is welcome when natural, never compulsory.

Each pair names the same workflow and scope. First distinguish nearby purposes: current-task progress, current-chat goal recap, returning after a pause and learning from past failures. Do not hide a different capability behind the second name.

Show a ranked table with Plain name, proposed Plain invocation ID, Kitchen name, proposed Kitchen invocation ID and a short reason. Use kebab-case IDs. Keep alternatives together on one row, grouped by function. For a short comparison offer three to five pairs per function; respect a requested count. For broader personal-product exploration, vary questions, direct requests, playful language and reassurance rather than filling a fixed quota with near-duplicates.

## Preserve naming decisions

This naming workflow's confirmed pair is Plain **Which Name Wins?** (`which-name-wins`) / Kitchen **Name That Dish** (`name-that-dish`). Installed invocation for this selected package is `$name-that-dish`; a display-name switch does not install the other variant. Stable source IDs, display names and installed invocation IDs are different fields.

Check names and proposed IDs against both current catalog families when available. Show an existing name only as a retained choice, never a new invention. Preserve confirmed names and stable IDs unless a rename is requested. Never treat a question about a Kitchen name as approval of a mapping.

Remove awkward wording, misleading promises, unexplained invented words, startup filler and near-duplicate candidates. For a recommendation, explain the usage fit and one meaningful risk. Do not claim domain, repository, store or trademark availability without checking that specific current source. Naming proposals alone do not authorize renaming files, installing aliases or publishing.
