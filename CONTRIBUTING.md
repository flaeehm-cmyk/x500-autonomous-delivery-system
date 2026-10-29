# Team workflow

1. Open a small issue: subsystem, owner, desired result, dependencies and completion evidence.
2. Create a working branch, such as `power/rail-budget` or `docs/payload-interface`.
3. Add the artifact and a short explanation of the change, result and limits.
4. Run relevant checks; open a pull request and include the issue link and subsystem reviewer.
5. Merge after one approving [code-owner review](.github/CODEOWNERS), a passing `summary` check and resolved review conversations. New reviewable commits dismiss old approvals.

These rules apply to administrators too. Use your own account and credit collaborators. Organization owners manage access; Write access is sufficient for working branches.

## Local workflow

From an existing clone:

```bash
git switch main
git pull --ff-only
git switch -c docs/describe-your-change
# Edit and commit the intended files.
git push -u origin docs/describe-your-change
```

Open a pull request into `main`. For changes to the included analysis, run:

```bash
python -m unittest discover -s tests -v
python analysis/summarize_segments.py --check
```

The `summary` check covers the offline utility and report consistency, not aircraft behavior.

## Keep records useful

Use the [test record template](docs/templates/test-record.md) for measured results. Identify configuration, units, method, author and evidence. Separate bench, simulation and flight results; mark synthetic data and preserve failed tests.

Keep one authoritative source per topic: ownership in [team](docs/team.md), interfaces in [architecture](docs/architecture.md), active work in Issues, significant choices in [decisions](docs/decisions.md). Update linked summaries in the same PR when those facts change.

Review exports for private locations, credentials and third-party content before publishing. Keep long session notes and raw private logs out of the README. For folder conventions and the weekly routine, see the [GitHub guide](docs/github-guide.md).
