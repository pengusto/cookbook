---
name: are-we-cooking
description: Check whether a running task is making evidenced progress toward the user's goal. Use for progress checks, stalled work, side quests, repeated attempts, or requests such as "are we cooking?" and "kommen wir voran?". Focus on the current task and its next useful move; use here-we-go-again for historical recurrence analysis. Also known as Check Progress.
---

# Are We Cooking?

Are we making progress, or just keeping the VPS warm?

Give a short, evidence-based course correction for the current task. Match the user's language. Keep the joke in the framing; make findings specific and fair, including the assistant's own decisions.

## Check the course

- Recover the user's intended outcome, accepted scope changes, constraints and completion criteria from the conversation. Distinguish the original goal from assistant-proposed additions.
- Compare that outcome with observable results: working behavior, resolved uncertainty, artifacts, relevant checks and remaining blockers. Activity, tool-call volume and commits alone are not progress. Investigation counts when it eliminates a plausible cause or informs a decision.
- Start with current context and inspect only the relevant files, checks or task summaries needed to resolve uncertainty. Identify what cannot be verified. Do not scan unrelated tasks by default.
- Trace repeated attempts: what changed, what was learned and why another attempt is justified. Look for side quests, premature deployment, unsuitable test data, missing reproduction and tests that fail to exercise the affected behavior. These are hypotheses, not mandatory findings.
- Revisit accepted recommendations relevant to the next step. Separate suggestions from commitments, intentional deferrals and implementation not evidenced. Do not turn every AI suggestion into a todo.
- Recommend the smallest next action that either moves the goal forward or resolves its main uncertainty. State the expected observable result and when to change approach if it fails. A local sandbox is useful only when it can reproduce the relevant behavior; account for remote-only dependencies.

## Response

Lead with a supported verdict: **Cooking**, **Stalled**, **Side quest**, or **Unclear**. Follow with the goal, evidence of progress or drift, and the next useful move. Keep this to a few short paragraphs or bullets; say what to stop or defer only when there is actual waste. If work is on track, say so without inventing changes.

This invocation is a diagnostic checkpoint, not permission to start new implementation, deploy, mutate other tasks or create automation. When embedded in an already authorized task, report the checkpoint and continue work within that scope; do not introduce a new approval gate.

If evidence suggests the same cause has recurred across tasks, suggest `$here-we-go-again` and name the suspected pattern. Do not invoke it recursively or require it to complete this check. If a prior retrospective is available, check the relevant agreed improvement rather than repeating the retrospective.
