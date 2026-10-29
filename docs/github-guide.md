# Repository organization and upkeep

## Keep one repository for now

The PCB, mechanics, package data, energy model and Jetson software share interfaces and a test plan. Keeping them together lets an integration change be reviewed in one pull request.

| Location | Purpose |
| --- | --- |
| Root README | Short overview, demonstrated progress and navigation |
| `docs/` | Shared architecture, interfaces, ownership, decisions and milestones |
| `hardware/` | PCB/CAD sources, readable exports, BOMs and assembly tests |
| `software/` | Package-label and Jetson application code |
| `analysis/` | Offline analysis, energy-model experiments and generated reports |
| `data/` | Small reviewed datasets with provenance and units |
| `tests/` | Automated software checks |

Add subsystem folders with their first real artifact: `hardware/power/`, `hardware/mechanical/`, `software/package-labels/`, `software/companion/` and `analysis/energy-model/`. Avoid empty scaffolding and copies of the same document in several places.

A separate repository becomes useful when a subsystem has a stable interface, its own releases/dependencies or a genuinely different access/storage requirement. Jad's board could eventually justify a dedicated hardware repository. If split, keep this repository as the system overview and record the exact compatible subsystem revision. One repository per teammate is unnecessary.

## Small weekly routine

1. Each member updates their active issue with progress, an evidence link, a blocker and the next action.
2. Mohammed F checks shared interfaces and priorities with the relevant owners.
3. Review small pull requests and close completed issues.
4. Update the README only for a demonstrated capability change; update the roadmap for milestone changes.

Use **Backlog → In progress → Review → Done** if a GitHub Project board becomes useful. An issue list is sufficient initially. Do not maintain duplicate task lists in a board, roadmap and weekly document.

## Making a change

A **branch** is a working copy of the project history. A **commit** saves a change. A **pull request (PR)** asks teammates to review it before it joins `main`.

In the browser: edit a file → **Commit changes** → create a new branch and pull request. Locally, follow [CONTRIBUTING.md](../CONTRIBUTING.md). The protected `main` branch requires a code-owner approval, the `summary` check and resolved review conversations, including for administrators.

Write access lets a teammate push working branches. Organization ownership manages membership/settings. GitHub Apps need separate authorization for the organization.

## Preserve useful history

Keep decisions that explain a meaningful constraint, tradeoff, failure or scope change. Mark4 → X500 and tracking → delivery belong in the history. Routine shopping, every chat and abandoned ideas without a consequence do not need a public narrative.

Keep earlier work in dated retrospective entries; do not recreate old commit dates. Put test detail beside its artifact and link it from the history. Keep source CAD/PCB files plus lightweight review exports; use an appropriate large-file/release workflow for bulky media or datasets.

[Repository](https://github.com/x500-delivery/x500-autonomous-delivery-system) · [GitHub's project-management guidance](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects)
