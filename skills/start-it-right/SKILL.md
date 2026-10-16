---
name: start-it-right
description: Turn a free-form product idea or existing project into a recommended, checkbox-driven implementation start. Use when beginning a project, feature, app, service, extension, CLI, game, or agent skill, or when the next project step is unclear.
metadata:
  short-description: Turn ideas into an actionable project start
---

# {{TITLE}}

Turn intent into the smallest useful next action while keeping the user in the
flow.

## Core rule

Every turn ends with a recommendation pass:

- recommend one concrete next step;
- recommend only the modules or skills that fit the current project;
- mark open human decisions and external gates;
- present recommendations as a short, preselected checkbox list when the host
  supports it, otherwise as compact Markdown;
- let the user reject a recommendation without making them restate the idea.

If no specialist module is needed, say why and recommend the smallest useful
check or the next open, unblocked ticket. Do not stop at “no action needed”.

## Modes

- Default: inspect the current context, infer the project type and maturity,
  recommend the next slice, and ask only material questions.
- `brainstorm`: clarify the product promise, riskiest assumption, smallest
  validation step, and suitable modules. Do not implement product code.
- `init`: after the user confirms the recommendations, create the selected
  project artifacts and leave one executable frontier ticket.
- `continue`: inspect the existing repository and continue from its first open,
  unblocked ticket or the next explicitly selected decision.

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
- recommend Stop Slop for visible human-facing prose and realistic content
  fixtures, not for code or structured data;
- recommend browser, device, runtime, or store checks when the product claims
  behavior that local unit tests cannot prove.

### 3. Ask once, in a batch

Present the recommended modules as selected checkboxes grouped as required,
recommended, and optional. Ask only decisions that materially change scope,
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
without explicit action-time approval.

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

Keep the response compact and concrete:

1. inferred project and current stage;
2. recommended checkbox modules with reasons;
3. one batched human decision, if needed;
4. selected artifacts or implementation result;
5. checks and remaining gates;
6. exactly one next recommended action.

For three representative flows, read [references/examples.md](references/examples.md).
