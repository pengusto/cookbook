---
name: kill-the-todos
description: Bring the current chat to completion by reconciling open todos, completing authorized work, resolving consequential decisions, and preparing precise remaining human steps. Use when the user wants to finish or wrap up the current conversation and its outstanding work.
---

# Kill the TODOs

Finish the work agreed in the current chat. A summary and a plan are intermediate results; continue through execution and verification wherever authorization and available access allow.

## Reconstruct the finish line

Read the available conversation, including carried-over context. Identify the intended outcome, accepted decisions, constraints, promises, and unfinished todos. Reconcile them with current evidence: completed, actionable now, needs a decision, or needs a human action. Drop superseded and cancelled work; do not revive rejected ideas or optional suggestions as commitments.

Use tools to resolve factual uncertainty before asking the user. If missing conversation context materially affects scope, ask for that specific gap instead of inventing prior agreements. Stay within this chat's agreed work; do not sweep other projects or create tasks, goals, or automations unless requested.

Briefly state the finish line and the remaining execution plan. Keep the checklist in the conversation unless a saved artifact is useful or requested.

## Resolve decisions with little effort

Ask only questions whose answers materially change the outcome, scope, cost, access, or an irreversible action. Choose routine implementation details yourself. Stress-test consequential assumptions with concrete tradeoffs, without turning completion into an open-ended interview.

Prefer an available native Codex question tool when its current mode and tool rules permit. Otherwise use numbered questions with lettered options so the user can answer `1a 2c 3a`. Give each question only as many meaningful choices as needed, usually two to four, and mark a recommendation with a short reason. Allow a free-text answer. Group independent questions; ask dependent questions after their prerequisite is answered. Avoid re-asking settled questions.

For example:

1. Where should the finished draft go?
   a. Stay local (recommended; ready for your review).
   b. Prepare it in the agreed publishing system as a draft.

Do useful independent work while answers are pending. Do not treat silence, a preselected option, or elapsed time as approval. Follow the environment's rules for requesting actual authorization; a preference question must not hide a publishing or deployment approval.

## Execute to the human boundary

Complete authorized work, incorporating answers as they arrive. Preserve earlier limits such as no edits, no commits, or no deployment. The request to finish the chat does not grant new external permissions.

Before asking for a human intervention, finish the preparation that makes it concrete and reviewable. Identify exactly what is missing, why it is needed, where the user performs the step, and how completion will be verified. For credentials, use the appropriate secure entry or local secret storage; do not ask the user to paste tokens into the chat.

When a gate blocks one branch, finish the other authorized branches. If a tool repeatedly fails for the same reason, diagnose it or report the specific blocker instead of retrying indefinitely. Once only human-dependent work remains, present the handoff and wait for the user. After they respond, resume the remaining work and verify the result.

## Check whether we can call it done

Compare the result against the original finish line and every remaining commitment. Run relevant checks and distinguish implementation from tested behavior, local work from published or deployed work, and an attempted operation from confirmed success.

End with a compact account of what is complete, verification evidence, and any remaining human steps or unresolved decisions. If nothing remains, say so. If a gate remains, say the work is prepared up to that gate; do not call the entire chat finished. Do not append new improvement ideas or a generic offer to continue.
