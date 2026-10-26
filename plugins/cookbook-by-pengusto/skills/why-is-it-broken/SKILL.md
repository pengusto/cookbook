---
name: why-is-it-broken
description: Diagnose a current bug, failing check or unexpected result by reproducing the symptom, tracing the affected flow and testing hypotheses. Use when something is broken now; a retrospective instead examines patterns across past attempts. Implement a fix when requested, or report the diagnosis without edits when asked only to investigate.
---

# Why Is It Broken?

Turn a concrete failure into an evidenced explanation and, when requested, a verified fix. Invoke with `$why-is-it-broken <symptom>`; match the user's language.

## Establish the failure

Inspect the relevant project instructions, working tree and actual failing path. Recover expected versus observed behavior, reproduction steps, environment and recent relevant changes from available evidence before asking the user. Ask only for facts that materially change the investigation. Preserve unrelated work and redact sensitive logs.

Reproduce with the smallest representative input and a bounded check. Prefer isolated local or test environments. Production mutations, real payments, external messages and destructive probes require specific authorization. If reproduction needs unavailable access, distinguish the reported symptom from what you observed and continue useful static investigation. Do not call a hypothesis a confirmed cause.

## Test the explanation

Trace the affected flow across its actual boundaries: input, state, transformation, persistence and output. Compare a working case when available. State the leading hypothesis and choose a check that could disprove it. Change one relevant variable at a time; record what each meaningful result rules in or out. Distinguish application defects from test fixtures, environment, credentials, infrastructure and stale generated output.

Avoid speculative patch stacks, unrelated refactoring, disabled validation or repeated deployment retries without a changed hypothesis. After repeated failed hypotheses, reassess the reproduction and evidence; stop when further investigation cannot distinguish causes without missing input. Explain the next discriminating check instead of retrying indefinitely.

## Fix and verify

A request to fix the bug authorizes the necessary reversible implementation within its scope. An investigation-only request does not. Once evidence supports a cause, make the smallest complete correction at its source, preserving error handling, permissions and compatibility. Explain material changes to business rules before applying them.

Where the project supports it, add or update a behavioral regression check that reproduces the failure before the correction and passes afterward. Re-run the original reproduction and relevant nearby checks. A green build alone does not prove the reported behavior is fixed; report unavailable runtime or integration coverage. Do not publish, deploy or rewrite history without authorization.

## Return the result

Report the symptom, supported cause or remaining hypothesis, correction if any, and verification with its limits. If unresolved, give the most useful next check and exact missing input. Keep historical process analysis outside this investigation unless requested.
