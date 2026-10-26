# Examples

## Default execution

```text
$youre-the-chef Make the settings flow feel production-ready.
```

The skill inspects the real flow, identifies the highest-value gaps, implements the smallest complete improvement, and verifies the integrated result.

## Gauntlet mode

```text
$youre-the-chef gauntlet Improve this game until the first five minutes feel polished.
```

Use this when the work benefits from a finite quality loop. The skill builds against a concrete reference, critiques the real output, fixes the largest remaining gap, and re-checks it. It stops when the remaining improvements are diminishing returns or a product decision is required.

## Audit mode

```text
$youre-the-chef audit payment retry behavior
```

Audit mode reports prioritized, evidence-backed findings and does not turn an inspection into a broad rewrite unless the request also asks for fixes.

## User test mode

```text
$youre-the-chef usertest Create a draft, save it, reload and open it again. Use the local test account; report findings without fixes.
```

Exercise the real journey and report reproduced defects, usability judgments
and coverage gaps separately. This is an agent-run check, not a study with
human participants. A test request alone does not authorize repairs or real
external effects.

## Mode words inside a goal

```text
$youre-the-chef Fix the audit export button.
```

This uses default execution: `Fix` is the first argument. The word `audit`
inside the goal does not select audit mode.

## Good goals

```text
$youre-the-chef Finish the onboarding flow for public demo use. Keep the current visual direction.
$youre-the-chef Add an empty state and recoverable error state to the search page.
$youre-the-chef Review this API integration for data-loss and authentication risks.
```

The goal supplies intent. The repository supplies implementation details.
