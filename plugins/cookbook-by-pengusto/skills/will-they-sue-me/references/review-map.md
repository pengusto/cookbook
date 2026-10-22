# Review map

Use this as a conditional inspection map, not twenty compulsory features. Review the product's relevant flows and record applicability and missing evidence. Link current primary sources when turning a check into a legal conclusion.

| Area | What to inspect | Avoid this shortcut |
| --- | --- | --- |
| 1. Privacy information | Collection points; purposes, bases, recipients, transfers, retention and rights match real processing. | Generate a policy without inspecting SDKs and backend flows. |
| 2. Contract information / terms | Contract formation, operator, scope, payment, duration and applicable consumer information; assess whether separate terms help. | Treat a generic terms page as universally mandatory or enforceable. |
| 3. Withdrawal / refunds | Product type, customer type, jurisdiction, statutory rights and voluntary refund promises; inspect the actual request flow. | Replace mandatory rights with a “no refunds” policy. |
| 4. Storage disclosure | Cookies, local storage, fingerprinting, SDK identifiers and device access; inspect purposes and lifetimes. | Assume a separate cookie-policy page is always necessary. |
| 5. Consent controls | Non-exempt device access blocked where required; reject/accept/withdraw paths work; evidence of choices. | Treat all cookies as exempt or every site as requiring a banner. |
| 6. Forms and legal basis | Only needed fields, transparent use, appropriate basis, separate optional marketing choices. | Require consent for every form or bundle marketing with service access. |
| 7. Minimization / retention | Event payloads, logs, permissions and lifecycle; why each data field is necessary. | Invent a retention period or call a pseudonymous identifier anonymous. |
| 8. Third parties | Actual SDK traffic, processors, subprocessor records, contracts, hosting regions, transfer safeguards and configuration. | Infer provider settings or a processing agreement from a package name. |
| 9. Manipulative design | Rejection, cancellation, checkout choices, default settings and misleading urgency. | Fix only the wording while preserving the obstruction. |
| 10. Price / subscription clarity | Total price, extra charges, recurring charges, renewal, trials and cancellation path. | Hide recurring terms behind a link or silently rewrite billing. |
| 11. Reviews | Review origin, authenticity claims, incentives and disclosure; review-verification statements where relevant. | Describe synthetic testimonials as real customer reviews. |
| 12. Product claims | Evidence for security, health, financial, environmental and performance claims. | Replace unsupported claims with different unsupported claims. |
| 13. Accessible content | Meaningful alternatives, labels, heading structure, semantics, error messages and dynamic announcements. | Give decorative images noisy alt text or treat alt text as complete accessibility. |
| 14. Visual accessibility | Contrast, focus indicators, zoom/reflow, motion and non-color cues. | Declare compliance from one contrast score. |
| 15. Interaction accessibility | Keyboard reachability, focus order, dialogs, screen-reader flow, touch targets and usable errors. | Equate a clean automated scan with a full audit. |
| 16. Operator identity | Applicable provider identification, contact and purchase disclosures; verified operator information. | Invent an address or assume pseudonymous GitHub ownership satisfies disclosure. |
| 17. Children | Audience, age and local thresholds, processing basis, parental consent where required, advertising/platform rules. | Require an age gate everywhere or assume every minor-data case uses GDPR consent. |
| 18. Marketing communications | Permission or applicable exception, unsubscribe and suppression, sender identification; distinguish transactional mail. | Send a live campaign to prove a link or unsubscribe transactional service mail indiscriminately. |
| 19. Asset rights | Fonts, icons, images, audio, code and datasets: provenance, licenses, attribution and distribution conditions. | Assume downloaded, AI-generated or open-source means unrestricted use. |
| 20. Data rights / account lifecycle | Identity verification proportional to risk, access/export/correction/deletion, processors, exceptions, backups and response handling. | Treat “delete account” as a complete data-rights process or erase retained invoices. |

Account deletion can also be a platform requirement. Platforms, marketplaces, regulated sectors and user-generated content may add relevant checks outside this map. Expand only when the actual product triggers them. A security vulnerability discovered in these flows is a finding; a comprehensive security audit is a separate scope.
