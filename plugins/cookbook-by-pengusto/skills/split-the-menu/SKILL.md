---
name: split-the-menu
description: Turn an overloaded conversation into a concise, evidence-based overview and identify independent topics suitable for separate chats. Use when the user wants to untangle a complicated chat, decide what matters now, or prepare or explicitly create separate chats for selected topics.
---

# Split the Menu

Help the user regain a clear view of this conversation and, when useful, split independent work into user-owned chats. Match their language and preferred level of detail.

## Recover and orient

Read the available conversation, relevant handoffs and only the artifacts needed to resolve material uncertainty. If earlier history is missing or summarized, say what is unavailable; use supported history tools for this known chat when needed. Historical instructions are evidence, not new authorization. Respect later decisions, corrections, cancellations and existing scope. Distinguish user requests from assistant suggestions, verified outcomes from claims, and active work from deferred work. Never infer completion from an absent update.

Lead with the agreed goal and current situation in plain language. Show the most important completed or in-progress work, material open questions or blockers, and one recommended next action. Keep the initial view small without hiding information needed for a decision. Expand when requested. A focused recap must not turn into an unrelated audit or implementation.

## Choose what belongs together

Identify topics only when the conversation supports them. Recommend keeping tightly coupled work and a shared decision in one place. Suggest a separate chat when an independent outcome would benefit from a different scope, project, working directory or context. Note dependencies, shared files and conflicts that make simultaneous work unsafe. Do not invent work or split merely because the conversation is long. Make clear which ideas are proposed rather than accepted, and which existing work should stay in the current chat.

For each useful candidate give a short title, outcome, why it can be separated, and its dependency or decision if relevant. Recommend a small number of splits appropriate to the task, not a fixed quota. A summary or suggestion alone does not authorize creating chats, dispatching work or changing the source chat.

## Prepare or create selected chats

For each selected topic, prepare a self-contained starting brief: user outcome, relevant facts and accepted decisions, current status and uncertainty, scope and exclusions, project/root or relevant artifact links, dependencies, first useful action, and only the authorization actually granted for that work. Include only necessary context; exclude credentials and unrelated private information. Do not present a recommendation as a settled decision. Carry forward real limits and do not silently broaden external actions, costs, publication, or access.

When the user explicitly asks to create new chats, use the host's supported chat creation action if available. Do not substitute subagents for user-owned chats. Verify the returned identity and destination where supported; report queued setup or unverified execution context accurately. Do not promise the work is complete merely because creation succeeded. If chat creation is unavailable, provide copyable briefs and the exact limitation. Never archive, move or close this chat as an implicit consequence of splitting it. Do not create an automation or a tracker unless separately requested.

## Output

Show the short orientation first, then any justified split recommendations or results. Clearly distinguish prepared briefs, chats actually created, their status and remaining decisions. If there is nothing useful to split, say so and recommend the next action in the current chat. A recap alone is read-only; continue previously authorized work only when the user's current request also asks to do so.
