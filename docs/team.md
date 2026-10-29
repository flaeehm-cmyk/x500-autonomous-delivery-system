# Team and subsystem ownership

Assignments confirmed by Mohammed F on **28 October 2026**. Proposed additions are marked below.

**Mohammed Flaeeh (Mohammed F)** leads the project. The team includes students at Saint Louis University and Washington University in St. Louis; this is an independent student project.

| Member | Ownership | Next concrete deliverable |
| --- | --- | --- |
| **Mohammed F** — ECE, SLU | Overall system integration, requirements, flight validation, administrative work and coordination; **energy model with Jad** | Current aircraft configuration and mass record; calibrated energy-data collection plan with Jad |
| **Jad** — ECE, SLU | **Complete power-distribution PCB**, intended to replace the PM02 power module, original PDB and temporary custom Jetson supply; **energy model with Mohammed F** | Power-tree and rail/load requirements, sensing plan, schematic and staged bench-test plan |
| **Yazan** — ME, SLU | All mechanical work: payload mechanism, custom parts, fabrication, mounting and structural improvements; assists with flight-controller settings and physical constraints | Payload/mount CAD, measured mass and center of gravity, retention and release test plan |
| **Ahmad** — CompE, WashU | Jetson setup and computing, computer vision, machine learning and reinforcement-learning exploration | Reproducible Jetson environment and camera pipeline; proposed companion-integration scope below |
| **Mohammed A** — CS, SLU | QR-label generation, package-data format and intake software; integration of decoded package records with the Jetson workflow | Versioned label specification, generator and validation examples |
| **Alend** — CompE, SLU | **Not assigned yet** | Suggested starter contribution below, subject to team agreement |

Ownership identifies responsibility, not completion. Finished work should link to code, CAD, measurements or test records under its actual contributors.

## Ahmad: proposed subsystem

**Companion autonomy and perception** gives Ahmad a defined integration role: deploy the camera/label-reading pipeline on the Jetson, connect it to Mohammed A's package records, integrate the energy model and route evaluator, and manage the Jetson–Pixhawk mission interface.

Start with a reproducible camera demo and a simulated mission interface. Later CV/ML work should address a measured problem, such as unreliable label/placement-marker detection. Compare it with a simple baseline. Reinforcement learning remains an optional simulation research direction, outside the initial delivery demonstration.

## Shared boundaries

- **Mohammed A → Ahmad:** package schema, generated labels and validation rules → camera decoding and onboard execution.
- **Mohammed F + Jad → Ahmad:** versioned energy estimator, calibrated input requirements and prediction limits → route feasibility and planning.
- **Yazan → Mohammed F + Ahmad:** physical payload/clearance limits and attachment/release feedback → aircraft limits and mission states.
- **Mohammed F:** resolves cross-subsystem changes and coordinates integration acceptance.

## Alend: suggested starter task

A **bench weighing and package-validation station** is a useful bounded contribution: read a load cell, calibrate against reference masses, report mass with a timestamp, and detect disagreement with the QR label. Begin with a laptop test and then connect it to Mohammed A's validator.

This is a recommendation, not an assignment. If the team chooses it, define a small first issue and agree who will mentor/review it.

Use one owner per issue, list collaborators, and commit from each contributor's own account. See [workflow](../CONTRIBUTING.md).
