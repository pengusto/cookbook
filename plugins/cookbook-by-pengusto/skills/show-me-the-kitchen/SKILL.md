---
name: show-me-the-kitchen
description: Explain Cookbook, orient new users to its available workflows, help choose the right skill and show concrete invocation examples. Use for collection onboarding, questions about which workflow to use, naming variants or how the Cookbook fits together. Explain and recommend; do not execute the selected workflow unless separately requested.
---

# Show Me the Kitchen

Be the readable introduction to Cookbook by Pengusto, not a second implementation of every recipe. Reply in the user's language and adapt the detail to their question.

## Establish what is available

Use the host's actual skill inventory and relevant installed Cookbook documentation. A maintained catalog can describe both naming variants; distinguish it from the variant actually installed in the current host. Do not assume a proposal, a source directory or a name in an old conversation is installed. If inventory cannot be inspected, qualify the coverage rather than fabricate availability.

Explain Cookbook as a collection of focused coding-agent workflows. The host and selected model carry out the work; a skill provides guidance, not a safety certification, guaranteed outcome or independent background agent. Never impersonate Pengusto or imply live contact with the maintainer.

## Explain the collection through the user's need

For an open-ended introduction, briefly explain the collection, then give a compact overview of available workflows grouped by use moment: starting and planning, autonomous implementation, checking progress, recovering context, reviewing before sharing, preparing release notes and handoff, learning from attempts, drafting prompts and finding names. Use only entries actually supported by the inspected version. Do not count this introductory guide as a separate implementation of those workflows.

For a specific need, recommend one best-fitting workflow, explain why, and show one ready-to-edit example using the host's actual invocation syntax and installed ID. Mention a second option only when its different purpose helps the choice. If the user's situation is essential and missing, ask one short question.

Keep similar recipes distinct: a progress check assesses the current approach; a conversation recap reconstructs goals and decisions; reentry after a long pause refreshes today's state; a retrospective learns from previous attempts. Autonomous project execution turns an authorized goal into a verified result; prompt completion only drafts a request rather than executing it. Naming compares alternatives rather than silently renaming the project.

Use a typical user sentence and the expected result to make the choice concrete:

| User's need | Select the available workflow that… |
|---|---|
| “Are we getting anywhere?” | checks progress and recommends a course correction |
| “What did I originally ask for?” | reconstructs this chat's goal and decisions |
| “I have been away for weeks.” | refreshes the project against its current state |
| “This button or check fails now.” | reproduces and diagnoses the current failure |
| “Why do we keep making this mistake?” | studies past attempts and preventive lessons |
| “Does checkout work for a user?” | exercises the journey in autonomous execution's `usertest` mode |
| “Build or improve this for me.” | implements an authorized goal through verification |
| “Help me finish writing this request.” | drafts the prompt without executing it |
| “Can I share this repository?” | prepares the repository's documentation and installation for sharing |
| “Can we stop here?” | reconciles commitments, cleanup proposals and handoff |
| “Review this diff for bugs.” | reviews the selected change and its affected contracts |
| “Can this implementation be simpler?” | proposes behavior-preserving reductions in a selected scope |
| “Where did we start that project?” | finds and verifies the right chat, repository or artifact |
| “Put this chat in the right project.” | identifies a suitable project and assigns the existing chat when requested |
| “How does this code path work?” | traces the existing flow in project-start's `explain` mode |
| “Which option fits this project?” | compares suitable options in project-start's `choose` mode |
| “Is this version really delivered?” | checks the delivery chain in sharing-preparation's `verify-live` mode |
| “Prepare a handoff for the other machine.” | prepares a destination-specific `handoff` in the closing workflow |

Choose from the inspected inventory, not from this table as an assumed list
of installed IDs. Show only the selected naming variant and actual host syntax.
Distinguish a product/legal review from an interactive journey test; neither
replaces the other. `usertest` simulates a user's actions, not human usability
research. Never run the recommended mode merely to demonstrate its invocation.

## Names, interface and limits

Plain and Kitchen name the same underlying workflows. Changing the visible language or display-name preference does not install another invocation alias. Explain the relevant host's syntax without treating slash commands and dollar-prefixed skills as interchangeable. Refer to a fresh-session refresh only when an installation changed or the host inventory is stale, not as an automatic repair for every missing entry.

Explain the optional visual Cookbook sidebar, its language and system/light/dark controls only when that interface is available or documented for this version. The skills-only plugin and the separate local MCP sidebar are different packages; do not promise that installing one enables the other. Do not alter theme settings, install plugins or enable a disabled sidebar while merely explaining.

Stay at orientation by default. A recommendation is not authorization to scan files, create tickets, execute the recommended skill, publish or change settings. When the user separately asks to act, follow their actual scope and permissions instead of making the guide a mandatory extra approval step.
