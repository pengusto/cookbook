---
name: youre-the-chef
description: >-
  Execute vague or detailed project goals autonomously while preserving the
  user's product intent. Inspect the real repository, infer safe missing
  details, establish an observable quality bar, implement, test, critique, and
  review the integrated result. Use for requests such as "$youre-the-chef make
  this prototype really good", finishing a project for public demonstration,
  substantial builds, stepwise execution and workload planning, polish passes,
  game work, focused audits, or usertest requests to exercise a real user
  journey and report findings.
---

# You’re the Chef

The user supplies intent. Determine the rest and act.

## Parse the invocation

- `$youre-the-chef <goal>`: execute the scoped goal autonomously.
- `$youre-the-chef gauntlet <goal>`: use the aggressive quality loop below.
- `$youre-the-chef plan <goal>`: assess the work and discuss a practical scope without
  starting implementation unless the user also requests it.
- `$youre-the-chef audit` or `$youre-the-chef audit <area>`: inspect and report;
  do not implement major new functionality unless the request also clearly
  asks for fixes.
- `$youre-the-chef usertest <flow>`: exercise a concrete user journey and report
  observed behavior; implement fixes only when separately requested.
- Treat `gauntlet`, `plan`, `audit` and `usertest` as mode words only when they are the first
  argument. Otherwise treat the whole message as the goal.

## Start with evidence

Before asking a question:

1. Find the actual project root and inspect its status.
2. Read applicable `AGENTS.md`, README files, project docs, tests, configs,
   assets, screenshots, and the code paths relevant to the goal.
3. Trace the user-visible or operational flow end to end. Run the cheapest
   useful checks and inspect real output where the task is visual or runtime-
   sensitive.
4. Infer non-critical missing details conservatively. Record important
   assumptions, decisions, blockers, and risks.

Ask only when the missing decision materially changes product scope, core user
intent, security or privacy, destructive or irreversible behavior, external
cost, or major compatibility expectations. Do not ask for implementation
details the repository can reveal or the agent can choose safely.

Preserve explicit instructions and existing product intent. Change
implementation freely when it improves the requested result, but escalate a
major direction change instead of silently replacing the idea.

## Set the quality bar

Choose the strongest practical, inspectable bar for the actual domain. Use a
provided reference; otherwise infer a credible shipped product, mature CLI,
reliable backend, ergonomic library, or equivalent target. Translate vague
words such as "good" or "production-ready" into observable checks: rendered
frames, behavior, latency, failure handling, accessibility, tests, recovery,
or other evidence that matters to this project.

Do not apply an irrelevant generic checklist. Inspect the dimensions that can
make this particular result weak: incomplete flows, empty/loading/error
states, keyboard and responsive behavior, performance, security, persistence,
onboarding, integration gaps, placeholders, documentation, or polish.

## Work

- Let the task determine the architecture and decomposition.
- Keep tightly coupled work under one coherent owner.
- Prefer one authoritative checkout and app installation. Reuse compatible build
  outputs and dependencies; create separate worktrees, app bundles, or test
  environments only when isolation is needed, and identify which is canonical.
- Protect user sessions and unsaved work. Track test processes and artifacts you
  create, close your test instances when finished after checking their state, and
  retain or remove files only within existing authorization and recovery needs.
  Check storage before large downloads or duplicate builds; report retained
  test artifacts and any material resource usage or cleanup decision.
- Parallelize only genuinely independent work; integrate it before judging
  completion.
- For important quality-sensitive work, use a builder and a separate
  fresh-context critic when the host supports it. Have the critic inspect the
  actual result and the quality bar, not the builder's summary.
- Implement the smallest complete change. Reuse existing patterns and
  dependencies. Do not add a framework, agent-management layer, state
  machine, database, scoreboard, or fixed team/iteration protocol.
- Run relevant tests and checks. For non-trivial logic leave one runnable
  regression check when the project has no better existing coverage.
- For visual or runtime work, inspect the integrated product, not only source,
  generated assets, a mockup, or a tool viewport.

For visual and game projects, choose the strongest available asset route:
reuse project assets first; use image generation for flat sprites, textures,
icons, UI art, or concepts; use real 3D tooling for geometry that must behave
as geometry; use code or shaders when they are the right fit. Always integrate
assets into the real product and judge the in-product result. Asset work never
replaces playable or usable product work. Note unavailable tools rather than
pretending their output was verified.

## Work in useful steps

For a substantial goal, distinguish the agreed outcome from optional ideas. Map
the major work remaining, relevant dependencies, the next useful slice, and any
material uncertainty. Gauge scope from evidence; if time, cost, or effort cannot
be estimated credibly, say so rather than inventing a number. Use an existing
project plan or task list when useful instead of creating a parallel system.

Keep working through authorized, unblocked slices. After a meaningful work
block, briefly report progress, remaining work, and any concrete decision or
blocker; continue without waiting for confirmation when the agreed direction is
clear. When the user asks to discuss how much to do, compare a small useful
scope with a broader readiness scope, explain the trade-offs, recommend one, and
invite a choice. Continue work independent of that choice while waiting. A
budget, selected limit, or pause is not evidence that the goal is complete.

Identify improvements needed for the user's stated finish line and propose
additional ideas separately, with a reason and next step. Do not present an
unrequested optional enhancement as agreed work or add it silently. When the
requested result is complete, stop rather than inventing an endless backlog.

## Choose a continuation method

A skill invocation, `gauntlet`, and progress notes do not create a scheduler or
guarantee another turn. When substantial work may need continuation, or the
user asks about a loop, first inspect the goal, agreed remaining work, current
state, dependencies and available host capabilities. Distinguish verified
open tasks from ideas or unverified claims; do not invent tasks, estimates or a
fixed minimum task count to justify a loop. If little actionable work remains,
say so and recommend completing it directly. If the scope or finish line is
unclear, explain that and ask only the decision needed to choose a useful path.

Present the relevant choices briefly, with a recommendation and practical
trade-offs: continue the authorized work in this turn; use a persistent Goal
when the host supports one; or set up a timed continuation when a supported
scheduler is available. Explain any unavailable option and an actionable
fallback. Mention combining a Goal and a schedule only when that combination
addresses a real need and the host supports it; do not create redundant or
competing loops. A Codex Goal is event-driven and may continue at an idle
boundary, not every 30 minutes. A scheduled heartbeat is a separate mechanism;
its delivery and availability depend on the host. Neither guarantees unattended
completion or bypasses permissions.

Let the user choose before creating a Goal or schedule, unless their existing
instructions already explicitly authorize the specific choice. Do not turn
silence into a decision, interrupt authorized work merely to wait for a timer,
or stop independent work that is already unblocked. If the user chooses a Goal,
use the supported host action with a concrete outcome, verification and
constraints; check the existing Goal first. If the user chooses a schedule, use
the supported scheduler for the correct conversation and requested cadence,
while respecting permissions, stopping conditions and notification preferences.
Do not run overlapping work or continue a completed or paused task; a blocker
must be resolved before dependent work resumes. Do not invent a host command,
install cron or hooks, or create a second scheduler as a workaround. Report
creation only after the host confirms it; a recommendation is not active work.

## Modes

### Plan

For `$youre-the-chef plan <goal>`, inspect the relevant project and its current state,
then give an evidence-based view of what remains: completed work, the next
steps in dependency order, material unknowns, and reasonable alternatives for
how far to go. Describe work and likely scope qualitatively unless a reliable
estimate is available. Separate the user's existing commitments from new
suggestions. Recommend a practical starting scope and ask only for the choice
that materially changes direction or scope. A planning-only request does not
authorize implementation, task creation, publication or external side effects.
If the user also requests implementation, proceed within that authorization.

### User test

Use `$youre-the-chef usertest <flow>` when the user wants to know whether a real task
works from a user's perspective. This is an agent-run journey check, not
research with human participants or evidence of what all users will understand.

Establish the intended user, task, target environment and observable success
condition from the product and request. Select a small representative journey,
including relevant empty, loading, error and recovery states. Exercise the
actual interface with available browser, app or CLI tools; check keyboard and
small-screen behavior when applicable. Source inspection and unit tests alone
do not establish that the journey works. Report unavailable interaction tools
as a coverage gap rather than inventing a successful walkthrough.

Use isolated test data and the least consequential environment that can
represent the flow. Do not register real users, send messages, incur charges,
alter production records or delete data without specific authorization.
Ask about a missing account, role or environment only when it prevents a
useful test; never request passwords in chat. Record agent-created test data
and clean it up only within the existing authorization.

For each important finding give the action, expected and observed result,
reproduction evidence and impact. Separate reproduced defects, usability
judgments and untested paths. Report covered scenarios even when no defect
was found, without claiming comprehensive QA. A test request authorizes
inspection, not repairs; if repairs are also requested, fix within scope and
retest the original journey. Stop at the selected coverage boundary.

### Default

Infer what is safe to infer, establish the quality bar, build, test, review,
and stop when no important actionable gap remains inside the intended scope,
further work has diminishing value, a capability blocks meaningful progress,
or a genuine product decision is required.

### Gauntlet

Use a stronger external reference and an aggressive but finite loop:

1. Build or improve the requested result against the reference.
2. Have a fresh critic inspect the real output and compare it with the bar.
3. Identify the largest remaining meaningful gap.
4. Fix that gap, then re-check the integrated result.
5. Use blind A/B comparison when it is genuinely useful and possible.

Repeat only while actionable, in-scope gaps remain. Do not make the loop
logically infinite, lower the reference, or replace product work with endless
asset generation or capture tooling.

### Audit

Do not turn an audit into a build by default. Inspect the requested area and
its neighboring flow, then report prioritized, actionable findings with exact
files or surfaces, evidence, impact, and the smallest useful next step. Make
only clearly requested fixes. Check integration, drift, risks, missing
requirements, and the highest-value improvement rather than producing a
ceremonial checklist.

## Game-aware pass

When the project is a game, automatically select the relevant dimensions from
the actual project: core loop, controls, movement, combat and game feel,
enemies or AI, level design, feedback, animation, VFX, audio, UI, visual
cohesion, asset quality, performance, onboarding, and playability. Compare
real in-game frames or interaction against the chosen reference. Do not let
art generation hide weak gameplay or let a capture setup make the game
unplayable.

## Lightweight progress

For a substantial task, maintain one concise project-local `.gauntlet.md` (or
an existing equally simple project-appropriate artifact) with only:

- Goal
- Quality bar
- Current focus
- Completed work
- Largest current gap
- Important assumptions, decisions, blockers, and likely next step

Create or update it only when it helps the user return later. Never build a
dashboard, round ledger, scoring service, or process around it.

## Completion gate

Before declaring completion:

1. Inspect the integrated real output.
2. Compare it with the chosen quality bar and check for product drift.
3. Run relevant tests and checks.
4. Use an independent final critic where the risk or quality sensitivity
   warrants it.
5. Perform a final domain-specific missing-things sweep.

Report what changed, what was checked, and what remains unverified. Never
claim browser, runtime, external integration, deployment, or human approval
without direct evidence.

## Fit within Cookbook

This workflow owns execution from a project goal through a checked result. A prompt-drafting workflow only completes the request; a progress check diagnoses the approach; a recap or reentry workflow reconstructs context; release preparation and product reviews have narrower evidence and permission boundaries. Do not turn those neighboring workflows into mandatory dependencies or duplicate their detailed checklists. Use an available focused workflow only when its actual purpose helps the requested goal, and keep the user's original authorization boundaries.
