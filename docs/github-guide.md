# GitHub owner's guide

Repository: [flaeehm-cmyk/x500-autonomous-delivery-system](https://github.com/flaeehm-cmyk/x500-autonomous-delivery-system)

## What the main features mean

A **repository** is the project folder and its saved change history. The **README** is the landing page. A **commit** is a named saved change. An **issue** tracks a task or test result. A **branch** lets someone work separately; a **pull request** presents their change for review before merging it into the main version.

The landing page focuses on the project, Mohammed's role, demonstrated results, and links to evidence. GitHub's [profile guide](https://docs.github.com/en/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume) recommends a concise README, setup/testing instructions, useful project details, and pinned work.

## Repository details

| Setting | Value |
| --- | --- |
| Name | `x500-autonomous-delivery-system` |
| Owner | `flaeehm-cmyk` |
| Visibility | Public |
| Default branch | `main` |
| License | None selected; choose with the team later |

Suggested About description: **Student UAV engineering project: X500 autonomous-flight validation, Jetson integration, and a supervised parcel-delivery system in development.**

Suggested topics: `ardupilot`, `uav`, `robotics`, `embedded-systems`, `power-electronics`, `jetson`, `flight-testing`, `autonomous-delivery`.

The commit history starts with repository setup. Earlier development is documented with its actual dates in the engineering log; it is not represented by fabricated historical commits.

## Find your way around

- **Code:** files, folders, and the rendered README.
- **Issues:** engineering tasks and test records using the included forms.
- **Pull requests:** proposed changes and teammate reviews.
- **Actions:** automated tests of the offline analysis utility. These checks do not test the aircraft.
- **Commits:** what changed, who changed it, and when.

No collaborator invitations have been sent. Add teammates using their confirmed GitHub handles when ready.

## Make a small documentation update

Open the relevant Markdown file, choose the pencil/edit control, make the change, and use **Commit changes** with a concrete message such as **Record load-cell calibration results**. For a team review, create a branch and pull request rather than changing the main branch directly.

A useful update includes the date, contributor, configuration, measured result, evidence path, and unresolved issue. Use the [test record template](templates/test-record.md).

## Work with a local copy

With Git and Python installed, clone and test the repository:

```bash
git clone https://github.com/flaeehm-cmyk/x500-autonomous-delivery-system.git
cd x500-autonomous-delivery-system
python -m unittest discover -s tests -v
python analysis/summarize_segments.py --check
```

On Windows, use `py -3` instead of `python` if needed. GitHub Desktop is an alternative to command-line Git for syncing and reviewing changes.

## Weekly maintenance

- Add the actual new code, CAD, schematic, measurement, or test record.
- Update project status only when the linked evidence supports it.
- Keep planned work and unresolved questions in Issues.
- Add a clear real-aircraft photograph and a concise demonstration clip when available.
- Review files for private locations, identifiers, and credentials before committing them.

Pin the repository on your GitHub profile and use its main URL on your résumé. Keep autonomous parcel delivery marked as in development until an integrated demonstration is documented.
