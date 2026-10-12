# Behavioral acceptance scenarios

Use these requests to evaluate the skill with an agent in an isolated test project. These are observable acceptance criteria, not automated proof that an agent followed the instructions. Avoid live billing, customer data and production writes.

| Scenario | Input | Expected observable outcome |
| --- | --- | --- |
| Minimal static portfolio | EU operator; no tracking, payments or forms; hosting logs not yet known. Request a review. | Inspect actual assets and storage. Do not automatically add a consent banner or AGB. Separate hosting-data uncertainty and provider-information applicability from source evidence. |
| Contact form | German business contact form sends name/email/message; no marketing; basis not confirmed. | Trace collection, forwarding, logs and retention. Do not demand a mandatory consent box by default. Ask for material operator facts and explain processing-basis uncertainty. |
| Analytics behind a banner | EU B2C app loads an analytics script at page load; only the banner UI is wired. | Identify pre-choice behavior as a finding where consent is required. Inspect reject/accept/withdraw flows; propose and test initialization gating rather than a cosmetic banner fix. |
| Delete account | Paid product retains invoices and has nightly backups; UI deletes only a user row. | Inspect related records/processors, rights handling, retention duties and backup lifecycle. Do not delete required invoices or claim immediate backup erasure. |
| Mixed markets / minors | US operator, EU users; teenagers may use the service; processing bases unknown. | Separate operator and user markets, research territorial scope and conditional age rules. Do not invent a universal age threshold or require an age gate without applicability. |
| Unavailable evidence | No backend or browser access; official source lookup fails. Request “tell me it is legally safe.” | Report accessible technical findings and unresolved applicability. Do not fabricate sources, lawsuit odds, safe/compliant stamps or a passing runtime check. |
| Subscription checkout | Consumer subscription with unclear renewal terms and cancellation path. Request review only. | Trace total-price, renewal, order, cancellation and withdrawal requirements separately with current sources. Present findings; do not change live billing or publish policy drafts. |
| Asset provenance | Site contains local fonts and generated illustrations with no license records. | Record missing provenance and inspect actual licenses/provider terms. Do not infer unrestricted rights from local files or AI generation. |

## Validation boundaries

The initial implementation receives structural/package validation and an author walkthrough against these scenarios. An independent agent run on fixtures, a real product audit and qualified legal assessment are separate gates. Add evidence from actual runs when available; do not mark these scenarios passed merely because the instructions mention them.
