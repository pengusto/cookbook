# Artifact contract

Create only the artifacts selected by the user or required by the inferred
project stage.

## Baseline

- README with product promise and current next step
- short project instructions when repository behavior needs a stable rule
- `.gitignore` when `.scratch/` or generated output exists
- curated `CHANGELOG.md` when the project has user-visible changes or the user
  selected release tracking

## Product start ticket

Use a versioned ticket such as `docs/tickets/000-project-start/ticket.md` when
the user confirms the initial direction. Include:

```md
# Title

Status: ready | blocked | in-progress | done
Type: product | feature | research | ui | release

## Goal
## Product promise
## Smallest useful flow
## Selected modules
## Acceptance
## Out of scope
## Evidence
## Human gates
## Next action
```

Private alternatives, raw research, rejected options, and machine-local
evidence stay under `.scratch/` until a durable decision exists.

## UI proposal ticket

Store selected reference images beside the ticket:

```text
docs/tickets/<slug>/
├── ticket.md
└── assets/
    ├── proposal-desktop.png
    └── proposal-mobile.png
```

The ticket records the user problem, visible states, chosen and rejected
elements, responsive behavior, accessibility, and acceptance criteria. Do not
turn a beautiful screenshot into an implementation contract without a decision
and a smaller prototype ticket.

## Existing repositories

Inspect before writing. Preserve unrelated changes, nested repositories,
existing ticket routing, design tokens, licenses, and user-authored changelog
entries. Prefer a focused patch over a generated project rewrite.
