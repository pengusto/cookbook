---
name: close-the-kitchen
description: Close the Kitchen. Guide the current conversation to a verified finish or an intentional pause by reconciling commitments, proposing a small closing plan, completing authorized work and preparing a handoff. Use when the user wants to wrap up, wind down, hand over or close this chat; a guide-only request does not authorize execution.
---

# Close the Kitchen

Bring the current chat to a deliberate stopping point. Use `$close-the-kitchen` to invoke this workflow.

For `$close-the-kitchen handoff <destination>`, read [the targeted handoff guide](references/handoff.md).
Treat `handoff` as a mode only when it is the first argument. Preparing a handoff
does not itself authorize a host transfer or a message to another chat.

## Establish the finish line

Reconstruct the agreed outcome, accepted decisions and remaining commitments from the available conversation and actual artifacts. Resolve material factual uncertainty with relevant tools. Reuse observed results from this chat when the relevant state has not changed; do not rerun checks just to produce a closing message. Ask for missing context only when it materially affects scope; do not invent prior agreements.

Separate work that is verified complete, actionable now, needs a decision or human action, or has been deferred or cancelled. Do not revive rejected ideas or promote optional suggestions into commitments. Stay within this chat; do not sweep unrelated projects or create tasks, goals or automations unless requested.

When reconciling earlier recommendations, identify what was merely proposed,
accepted, started, verified implemented, deferred/rejected or not evidenced.
Check only material uncertainties against the owning artifacts. Report an old
claim as historical when it cannot be refreshed; do not reopen proven work
just to fill a checklist. A dropped requirement is not completed work.

For an upstream contribution, distinguish local commits, pushed branch, PR
head, CI, maintainer feedback and merge status. Before proposing fork or branch
cleanup, check all relevant own commits and retained recovery references,
including squash/cherry-pick equivalents where appropriate. A merged PR alone
does not establish that every branch is disposable. Report what remains;
deletion and external follow-up need their own authorization.

## Give a closing guide first

Briefly recommend a useful stopping point and the smallest remaining plan, explaining any failed check or unresolved gate. Distinguish finishing the agreed work from intentionally pausing it. A pause is a valid stopping point, but the original objective remains open.

If the user asks only for a guide or says to pause, prepare the guide or handoff without changing files, task states or jobs. Otherwise continue through the already authorized local work without asking again for settled permissions. Ask only when a missing decision materially changes the result, scope, cost, access or an irreversible action. Use the host's question tools when available and permitted; offer a recommendation and keep working on independent branches while an answer is pending. Silence is not approval.

## Finish the selected slice

Complete and verify the necessary authorized work before requesting a remaining human step. Make that step concrete and reviewable: what is ready, what input or permission is missing, where the user acts, and how success will be checked. Use secure credential entry rather than requesting secrets in chat.

Earlier limits such as no edits, no commits, or no publication remain in force. A request to close the chat does not authorize pushing, deployment, external messages, deletion or history rewrites. Do not cancel active jobs or remove staging, backups or temporary copies just because they appear unfinished; inspect ownership, active references and retention requirements first. Diagnose repeated failures or report the specific blocker instead of retrying indefinitely.

Dropping a TODO is not completing it. Change persisted task status only when requested or already authorized, and only to reflect actual work. Do not hide failing checks to produce a clean finish.

## Review cleanup and backups together

When this chat created or downloaded files, or the user requests cleanup, include a scoped cleanup review in the closing plan. Consider backups, staging, test outputs, superseded build packages, downloaded installers and exported documents such as PDFs imported into a document archive. Inspect only relevant locations and distinguish originals, retained recovery copies, reproducible intermediates and uncertain files. Age, filename and apparent duplication alone do not establish that a file is disposable.

For each proposed removal, give its exact path or identifier, size when available, purpose, reason for removal and the retained recovery source. Verify that source is accessible and covers the data being removed; use an integrity or restore check appropriate to the risk. Check active references and retention requirements. Keep unique originals, the only verified recovery copy and anything with unresolved ownership, recovery coverage or retention needs.

For an exported PDF or other document reportedly imported into Paperless or a similar service, verify the actual destination record and retrieve or inspect the stored original to confirm completeness. An upload attempt, receipt, filename match or search hit alone is insufficient. An archive entry does not resolve legal or original-document retention requirements. If destination access or retention is unclear, retain the local file and ask the user for the missing decision. For installers, check whether the installed application still depends on the download and whether a trusted replacement is available for the required version or recovery needs.

Present a short keep/remove/needs-check recommendation so the user can decide together with the agent. Ask about unclear purpose or retention before proposing removal. A cleanup review does not authorize deletion. If exact removals are not already authorized, ask for approval of the concrete list after completing the independent checks; do not treat silence as approval. Guide-only and pause requests remain read-only. Prefer recoverable removal when supported, then verify authorized removals and report what remains, its size when available and the condition for later cleanup. Never broaden this into a machine-wide file purge.

## Leave a verified handoff

Compare the outcome with the finish line and run checks relevant to the selected slice. Distinguish local files, commits, pushes and deployments; attempted checks and confirmed results; complete, deferred and blocked work. State important coverage limits.

Default to three short points: complete with evidence, remaining work, and a re-entry action only if pausing unfinished work. A fully completed small request needs no handoff document or new task. Include paths, refs or active job identifiers only when useful for resuming. Do not add fresh improvement ideas after reaching the stopping point.

Preparing to close is not a request to archive or end a voice call. Use a supported host action only when the user explicitly requests that action. If unavailable, explain the manual step without claiming it happened. Never mark an unfinished objective complete to make the chat look closed.
