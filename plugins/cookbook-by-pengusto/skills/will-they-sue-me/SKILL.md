---
name: will-they-sue-me
description: Review an app or website for evidence-backed privacy, consumer-rights, accessibility, and asset-licensing gaps before launch or after changes. Determine which checks apply, trace actual behavior, and prepare scoped fixes; use for product compliance reviews rather than predicting lawsuits.
---

# Will They Sue Me?

Find the gap between what a product does, what it promises, and what its applicable obligations require. The name is playful; the output is a technical product review, not a legal certificate or a prediction about litigation.

## Choose review depth

Follow the requested scope. For a targeted review, trace the named flow and its
relevant obligations; do not expand into a complete launch audit. For a broad
launch review, use the conditional review map. If scope is unclear, start with
the concrete reported flow and state the boundary; ask only if the distinction
materially affects the result. A targeted review does not certify the product.

## Establish the recipe

Read the project instructions and trace its actual stack, deployment, data flows, checkout, and public claims before proposing fixes. Establish the operator and target markets, B2B/B2C model, payments/subscriptions, personal-data processing, and whether children are an intended audience. Use project evidence for answers; ask only for missing facts that materially change the review. Separate operator location from user markets. German UI or a `.de` domain alone does not establish jurisdiction.

If scope is unknown, continue the technical review with labeled assumptions and keep legal applicability unresolved. Never silently default to US rules or present Germany/EU rules as worldwide requirements. Read [the review map](references/review-map.md) for relevant checks and [the Germany/EU reference](references/germany-eu.md) only when those markets matter. For other markets, research the relevant regulator and legislation instead of transplanting the EU map.

## Inspect behavior, not just documents

Trace relevant source paths and configuration, then use existing browser/runtime tools when available. Distinguish code evidence, observed behavior, deployment configuration, operator statements, and unavailable evidence. Do not send real payments, marketing email, delete real accounts, or manipulate production consent to test a finding without authorization; use isolated test data when appropriate.

Follow SDKs, cookies, local storage, pixels, embedded content, browser/device permissions, server logs, subprocessors, and retention. Check before consent, after rejection, after acceptance, and after withdrawal where applicable. A banner alone does not establish that tracking is gated. Absence of cookies does not establish absence of personal data. Inspect processors and international transfers when relevant; don't fabricate contracts, hosting regions, or safeguards.

Review checkout, renewal, cancellation, withdrawal/refunds, pricing, reviews, product claims, accessibility, operator details, marketing, and asset provenance in proportion to the product. Classify each relevant area as applicable, not applicable with a reason, or applicability unresolved. Do not add a banner, terms page, age gate, or consent checkbox merely because a generic checklist lists it. Consent is not the only data-processing basis; a contact form does not automatically need a mandatory consent checkbox.

For legal requirements, verify current primary sources for the jurisdiction and date, including effective dates, exceptions, and transition rules. Link the rule supporting each legal conclusion. If research fails, mark the conclusion unverified and continue independent technical work; do not guess. Distinguish statutory obligations, platform requirements, and optional good practice.

A reported Tab skip alone does not establish that submission is impossible or prove its cause: the control could be intentionally disabled or another keyboard path could exist. Mark the report as needing reproduction, and propose a conditional fix only after tracing semantics and state. Do not claim personal verification of supplied observations.

## Plate the findings

Give a concise scope statement and a reviewable table with:

- Priority: launch blocker, should fix, or optional improvement. Explain the impact rather than inventing fines or assigning lawsuit probabilities.
- Finding and applicability: observed mismatch, relevant market, and requirement or good practice.
- Evidence: exact file/line, observed route/action, or operator-supplied fact; redact personal data and secrets.
- Basis: current primary-source link and checked date for legal claims; mark missing proof.
- Fix and verification: smallest concrete change and an observable acceptance check.

Keep **confirmed finding**, **needs evidence**, **not applicable**, and **checked with stated coverage** distinct. A scanner result or a passed automated accessibility check is not proof of comprehensive compliance. Close with remaining facts requiring operator input or qualified legal review; do not replace the review with a generic disclaimer.

## Fix within the requested scope

An audit request authorizes review, not arbitrary product changes. If fixes are requested, carry out authorized reversible work and verify the affected flows. Preserve existing business behavior unless a change is part of the requested fix. Explain material tradeoffs before changing billing, retention, age eligibility, or other subtle product rules. Use fictional data in examples and drafts; never invent the operator's identity, lawful basis, rights ownership, or retention periods.

Draft policy text from verified facts, flag unresolved inputs, and keep claims consistent with the code. A deletion workflow must address relevant processors, retention exceptions, and backup lifecycles; do not erase records with statutory retention requirements or promise immediate backup erasure without evidence.

Do not publish, change visibility, deploy, send externally, accept contracts, or perform destructive production actions unless the user has authorized them. Existing explicit authorization remains valid; do not request it again. Recheck affected behavior after fixes and report local, committed, pushed, deployed, and browser-verified states separately. Report remaining gaps without declaring the app “lawsuit-proof,” “GDPR compliant,” or “legally safe.”
