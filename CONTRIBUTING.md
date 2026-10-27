# Team contribution workflow

Make each update a small, reviewable piece of engineering work.

1. Open an issue describing the problem, owner, dependency, and evidence needed to finish.
2. Create a branch with a descriptive name, such as `docs/power-budget` or `analysis/current-calibration`.
3. Add the actual artifact and its explanation: what changed, why, configuration, result, and limits.
4. Run the relevant check. For the included Python utility: `python -m unittest discover -s tests -v`.
5. Open a pull request using the supplied template. Request review from the subsystem owner or project lead.
6. Merge after review and update status only when the linked evidence supports it.

Use your own GitHub account for your work. Credit collaborators in the relevant document or pull request.

## Results and records

Use the [test record template](docs/templates/test-record.md). Separate bench, simulation, and flight results. Mark synthetic examples clearly. Keep an unsuccessful test and its follow-up instead of replacing it with a successful result.

For configuration changes, include the version actually used and the reason for the change. Proposed parameter values are not approved flight configurations.

## Public materials

Publish reviewed exports and appropriately sized media. Keep raw private flight logs, credentials, local environment files, and unreviewed media outside the tracked tree. The ignore rules are a convenience; inspect changes before committing.

A root README update should help a new reader understand the current project. Detailed session notes belong in the engineering log or a case study. Do not backdate commits to recreate work that happened before the repository existed.
