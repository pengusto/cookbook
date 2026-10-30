---
name: how-do-i-start
description: Turn a free-form product idea or existing project into a focused implementation start. Use when beginning a project or choosing its next step; explain traces an existing flow and choose compares suitable options before implementation.
metadata:
  short-description: Turn ideas into an actionable project start
---

# How Do I Start?

Turn intent into the smallest useful next action while keeping the user in the
flow.

## Scope

Choose the smallest useful start. A clear small request can go directly to a
local implementation and one relevant check; it does not need modules, a ticket
tree, or a decision workshop. Recommend additional work only when it resolves a
real uncertainty. If the requested slice is complete, stop without inventing a
next task. These instructions apply to this invocation, not every later turn.

Do not ask for hosting, accounts or publication decisions when the requested slice is local brainstorming. Defer choices that do not block that slice.

## Modes

- Default: inspect the current context, infer the project type and maturity,
  recommend the next slice, and ask only material questions.
- `brainstorm`: clarify the product promise, riskiest assumption, smallest
  validation step, and suitable modules. Do not implement product code.
- `init`: after the user confirms the recommendations, create the selected
  project artifacts and leave one executable frontier ticket.
- `continue`: inspect the existing repository and continue from its first open,
  unblocked ticket or the next explicitly selected decision.
- `explain <flow>`: trace the real project and explain how the selected part
  works, without edits.
- `choose <decision>`: compare a few suitable options against the existing
  project and recommend one, without installing or implementing them.

For `explain` or `choose`, read [the focused mode guide](references/explain-and-choose.md)
and complete that mode instead of the implementation-start workflow below.

Treat mode words only when they are the first argument. Otherwise treat the
whole request as the product intent.

## Workflow

### 1. Orient

For an existing project, inspect the real repository root, Git status, nearest
`AGENTS.md`, README, design guidance, existing ticket conventions, and current
open work. Preserve unrelated changes and nested repositories. For a new
project, use the supplied idea as the initial context.

Record the minimum useful facts:

- product type and target user;
- current maturity: idea, validation, MVP, existing product, release, or
  post-release;
- visible user outcome;
- important trust, data, legal, platform, or cost boundaries;
- the riskiest unresolved assumption.

### 2. Recommend

Read [references/module-catalog.md](references/module-catalog.md) when the
project needs more than the basic product brief and MVP slice. Recommend only
modules triggered by the idea. Each recommendation needs a one-sentence reason.

Use these defaults:

- choose clear, reversible implementation details yourself;
- recommend a decision workshop only for material trade-offs;
- recommend research when evidence is missing, not for familiar straight-line
  work;
- recommend i18n when languages, regions, locale-sensitive data, or a future
  international audience make it useful;
- recommend a license decision before public source distribution;
- review visible prose and realistic content fixtures; suggest an available
  specialist only when it materially helps;
- recommend browser, device, runtime, or store checks when the product claims
  behavior that local unit tests cannot prove.

### 3. Ask once, in a batch

For a material choice, give a concise recommendation and alternatives. Use
checkboxes only when several independent selections genuinely help. Use unchecked boxes or ordinary bullets in static Markdown; checked boxes look completed and recommendations are not authorization. Ask only decisions that materially change scope,
security, ownership, cost, privacy, publication, or compatibility. Keep
straightforward work moving with safe assumptions.

If the user rejects a module, retain the rest of the plan and recommend the
next viable step. If a required human decision remains open, prepare everything
around it and stop at that gate.

### 4. Execute the confirmed slice

Read [references/artifact-contract.md](references/artifact-contract.md) when
creating project files or tickets. Use existing project patterns first.

- `.scratch/` is for private, temporary, raw, or rejected material and must be
  ignored by Git.
- `docs/tickets/` is for confirmed, durable, shareable work.
- A confirmed UI proposal gets `ticket.md` plus selected desktop/mobile images
  in the ticket's `assets/` directory.
- Use GitHub, Jira, Trello, or another external tracker only when the project
  already uses it or the user selects it.
- Never create a parallel task database or hidden project state.

Do not overwrite existing README, `AGENTS.md`, design guidance, tickets,
licenses, or changelog entries without inspecting and preserving their intent.
Do not install plugins, publish, push, deploy, contact people, or incur cost
without explicit authorization. Reuse authorization already given for that action.

### 5. Verify and hand off

Run the smallest relevant checks. Report changed files, checks, assumptions,
unverified external gates, and the next recommended action. For a skill, run
the bundled quick validator and inspect the examples before release.

## Fallbacks

Other skills and connectors may not be installed. Detect availability before
recommending them. If Let Him Grill is unavailable, ask the material decision
inline and continue. If Research, Browser QA, GitHub, or Stop Slop is
unavailable, keep the recommendation visible and state the missing evidence or
manual step. Never claim that a missing tool ran.

## Output shape

Match the user's language and lead with 🎯 the inferred project and stage and 💡 one concrete recommended starting slice. When several independent selections are useful, use a compact checkbox list with a brief reason for each relevant module, grouped as required, recommended, or optional; otherwise use a short list. Omit empty groups. A preselected recommendation is not a decision or authorization. Show one batched human decision if needed, then any selected artifacts or implementation result, checks, and remaining gates. When useful work remains, end with one ➡️ next recommended action. Use labels as well as icons, and adapt the detail to the selected mode.

For three representative flows, read [references/examples.md](references/examples.md).
