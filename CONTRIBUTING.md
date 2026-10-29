# Team contribution workflow

Make each update a small, reviewable piece of engineering work.

1. Open an issue describing the problem, owner, dependency, and evidence needed to finish.
2. Create a branch with a descriptive name, such as `docs/power-budget` or `analysis/current-calibration`.
3. Add the actual artifact and its explanation: what changed, why, configuration, result, and limits.
4. Run the relevant check. For the included Python utility: `python -m unittest discover -s tests -v`.
5. Open a pull request into `main` using the supplied template. GitHub requests reviewers from [CODEOWNERS](.github/CODEOWNERS); include the relevant subsystem contributor in the review.
6. Merge after at least one approving code-owner review, a passing `summary` check, and resolution of review conversations. Update status only when the linked evidence supports it.

Use your own GitHub account for your work. Credit collaborators in the relevant document or pull request.

## Repository access and branches

The repository belongs to the [x500-delivery organization](https://github.com/x500-delivery). Use your own account with repository Write access (or a higher role) to push a working branch. Organization owners manage membership and repository settings.

Start from an up-to-date `main` and use a separate branch for each change:

```bash
git switch main
git pull --ff-only
git switch -c docs/describe-your-change
# Edit, review, and commit the intended files.
git push -u origin docs/describe-your-change
```

Open a pull request from that branch into `main`. Changes to `main` follow the review and check requirements above, including changes made by administrators. The `summary` check validates the offline analysis utility and its reproducible reports; it does not validate aircraft hardware or flight behavior.

## Results and records

Use the [test record template](docs/templates/test-record.md). Separate bench, simulation, and flight results. Mark synthetic examples clearly. Keep an unsuccessful test and its follow-up instead of replacing it with a successful result.

For configuration changes, include the version actually used and the reason for the change. Proposed parameter values are not approved flight configurations.

## Public materials

Publish reviewed exports and appropriately sized media. Keep raw private flight logs, credentials, local environment files, and unreviewed media outside the tracked tree. The ignore rules are a convenience; inspect changes before committing.

A root README update should help a new reader understand the current project. Detailed session notes belong in the engineering log or a case study. Do not backdate commits to recreate work that happened before the repository existed.
