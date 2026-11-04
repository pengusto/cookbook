# Examples

## Default execution

```text
${{ID}} Make the settings flow feel production-ready.
```

The skill inspects the real flow, identifies the highest-value gaps, implements the smallest complete improvement, and verifies the integrated result.

## Gauntlet mode

```text
${{ID}} gauntlet Improve this game until the first five minutes feel polished.
```

Use this when the work benefits from a finite quality loop. The skill builds against a concrete reference, critiques the real output, fixes the largest remaining gap, and re-checks it. It stops when the remaining improvements are diminishing returns or a product decision is required.

## Choosing continuation

For a large project, inspect the actual remaining work first. Offer a concise
choice between working now, a supported persistent Goal, or a supported timed
follow-up; recommend what fits and let the user decide. If only a small task
remains, say a loop is unnecessary. If the requested host lacks scheduling,
state that limit and offer the available alternative. No Goal or schedule is
created merely by invoking the skill.

## Audit mode

```text
${{ID}} audit payment retry behavior
```

Audit mode reports prioritized, evidence-backed findings and does not turn an inspection into a broad rewrite unless the request also asks for fixes.

## User test mode

```text
${{ID}} usertest Create a draft, save it, reload and open it again. Use the local test account; report findings without fixes.
```

Exercise the real journey and report reproduced defects, usability judgments
and coverage gaps separately. This is an agent-run check, not a study with
human participants. A test request alone does not authorize repairs or real
external effects.

## Mode words inside a goal

```text
${{ID}} Fix the audit export button.
```

This uses default execution: `Fix` is the first argument. The word `audit`
inside the goal does not select audit mode.

## Good goals

```text
${{ID}} Finish the onboarding flow for public demo use. Keep the current visual direction.
${{ID}} Add an empty state and recoverable error state to the search page.
${{ID}} Review this API integration for data-loss and authentication risks.
```

The goal supplies intent. The repository supplies implementation details.
