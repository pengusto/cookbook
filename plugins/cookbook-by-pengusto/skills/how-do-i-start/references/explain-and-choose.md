# Explain and choose

## Explain a real flow

For `explain <flow>`, identify the project and follow the actual entry
point through the relevant state, transformations, persistence and output.
Read the owning code/configuration and useful tests before explaining. Use
concrete file/function references and one small example that connects the
pieces. Explain important design choices when evidence supports them; label
inferred rationale and missing runtime coverage. Adapt to the user's familiarity.

Return how the flow works, where a related change belongs and the meaningful
unknowns. An explanation request does not authorize a rewrite, installation or
execution with external effects. Avoid a whole-codebase tour when one flow
answers the question.

## Choose within the real constraints

For `choose <decision>`, establish the intended outcome and inspect the
current implementation, installed tools, platform constraints and available
project references. Treat keeping the existing solution as a real option.
Reuse compatible platform/project capabilities before adding a dependency.
Consult a known catalog only when relevant and accessible; catalog notes are
leads, not proof of current maintenance or compatibility.

Compare a small number of viable options on the factors that change this
choice: integration effort, maintenance, supported platforms, cost, privacy,
recovery and migration where applicable. Verify changeable third-party facts
against current primary sources. State failed lookups and uncertainty rather
than guessing. Stars indicate attention, not suitability or safety.

Recommend one option, explain the decisive tradeoff, and give a small
validation step. Do not install, migrate, publish or create accounts solely
because an option won. If implementation is also explicitly requested,
continue through the authorized slice using the main workflow; do not ask
again for settled decisions. A material unresolved choice remains a question,
not permission inferred from silence.
