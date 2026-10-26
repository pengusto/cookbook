---
name: can-we-simplify
description: Find unnecessary complexity in a selected change or code path and propose smaller behavior-preserving alternatives. Use for requests to simplify, remove overengineering or reduce duplication; implement only when the user also asks for changes. This is a focused pass, not a whole-repository rewrite.
---

# Can We Simplify?

Make the selected work easier to understand and maintain while preserving its contracts. Invoke with `$can-we-simplify <scope>`.

## Establish what must stay true

Identify the selected diff or flow and inspect its callers, tests and project conventions before proposing removals. If comparing branches, fetch the relevant remote and pin the comparison. Preserve unrelated changes. Trace validation, error behavior, permissions, data formats, migrations, accessibility and supported consumers. An export with no local caller may still be a public contract; absence from a text search is not proof of non-use.

## Find the smallest useful reduction

Look for actual duplication, unused configuration, indirection with no current benefit, speculative compatibility paths and abstractions that hide a simple operation. Prefer project patterns and platform facilities. Compare the current implementation with the smaller alternative and explain what maintenance burden disappears. Similar-looking code can have different semantics; share it only when the shared responsibility is real. Fewer lines alone is not the goal.

Separate proven redundancy from uncertainty and optional style preferences. Keep a mechanism when removing it would weaken recovery, security, logging, compatibility or another established contract. If no worthwhile simplification is supported, report that outcome instead of inventing a refactor.

## Recommend or apply

For a review request, present a short ranked list with location, proposed reduction, preserved behavior, risk and a concrete check. Leave files unchanged. A request such as “simplify this” also authorizes the necessary reversible implementation in that scope; do not ask again for settled permission.

Implement a small coherent change at a time when authorized. Use existing behavioral checks and add a regression check for a meaningful uncovered contract, not assertions mirroring the refactor. Verify the original user outcome and affected callers, not only compilation or line count. Report changed files, relevant checks and any unresolved consumer coverage. Deletion of user data, publication or history rewrites require their own authorization.
