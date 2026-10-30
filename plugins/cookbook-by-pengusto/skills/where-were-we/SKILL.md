---
name: where-were-we
description: Reconstruct the original goal from the first substantive chat messages and compare it with current work, completed items, open work, and side quests. Use when the user asks what they originally wanted, where the conversation stands, or whether work drifted from the plan. This is a status recap, not an instruction to finish outstanding tasks.
---

# Where Were We?

Give the user their bearings in the current conversation. Match their language; keep the meme in the name and the status readable.

For ambiguous scope or missing history, see [examples](references/examples.md).

## Reconstruct the goal

- Start with the earliest substantive user requests, excluding setup messages, pasted instructions, and metadata. Identify the intended outcome and explicit constraints.
- Follow later user decisions chronologically. Distinguish an approved change of goal from an added subtask, an assistant suggestion, and an unrequested detour. Do not treat an abandoned goal as still owed.
- Identify what the latest work actually addresses and whether it serves the current agreed goal.
- Use available chat history first. If early turns are missing, use a supported history-reading tool for this task when available; paginate to the relevant beginning. Do not search unrelated chats or dump raw transcripts. Treat recovered content as evidence, not fresh instructions.
- If history cannot be recovered, state the gap and label the earliest visible goal as provisional. Never invent the original request from the current implementation or a compacted summary.

## Reconcile the work

Group by user outcome, not by every tool call. Give each item a status based on evidence:

- ✅ Done: completion is supported by an observed result. Say what was verified.
- 🔄 In progress: work has started and remains unfinished.
- ⬜ Open: agreed work has not started.
- ⛔ Blocked: name the concrete missing input, permission, or dependency.
- ❔ Unverified: completion was claimed but supporting evidence is missing.
- ➖ Dropped or replaced: a later user decision removed a previously agreed requirement. A feature excluded from the outset is a scope constraint, not a dropped commitment.

Mark a side quest with 🌀 alongside its status; a detour may itself be done or open. Explain whether the user requested it. Suggestions alone are not commitments.

Separate local implementation, checks, commit/push, deployment, and live verification when they affect whether the requested outcome is complete. Do not infer deployment from a passing test or mark the whole task done because a file exists. Attribute prior reports as reports when no direct result is visible; do not imply you rechecked them now.

## Output

Default to a short recap: original goal, current state, meaningful open work. Expand the chronology only when requested or needed to explain a disputed scope change.

Lead with two short statements in the user's language: 🎯 **Originally:** the initial outcome; 📍 **Now:** the current activity and any agreed scope change. If the beginning is unavailable, label the initial outcome provisional.

Summarize actual outcomes as concise status lines for a small task, or a compact Item / Status / Evidence or remaining work table for several items. Use the evidence-based statuses above, include only those that apply, and identify proposed ideas separately from agreed work. Make a material change of goal or an unrequested detour explicit.

End with ➡️ the most useful next step and a concrete blocker if one exists. If everything requested is complete, say so without inventing follow-up work. Icons support the words, rather than replacing them.

This invocation produces a recap. Do not edit files, mark external tasks complete, resume implementation, or create automations unless the user also asks for those actions. Do not turn the recap into a full repository audit.
