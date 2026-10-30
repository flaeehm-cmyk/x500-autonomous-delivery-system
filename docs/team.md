# Team and subsystem ownership

Assignments updated on **30 October 2026**.

**Mohammed Flaeeh (Mohammed F)** leads the project. The team includes students at Saint Louis University and Washington University in St. Louis; this is an independent student project.

| Member | Ownership | Next concrete deliverable |
| --- | --- | --- |
| **Mohammed Flaeeh (Mohammed F)** — ECE, SLU | Overall system integration, requirements, flight validation, administrative work and coordination; **energy model with Jad** | Current aircraft configuration and mass record; calibrated energy-data collection plan with Jad |
| **Jad Khdeer** — ECE, SLU | **Complete power-distribution PCB**, intended to replace the PM02 power module, original PDB and temporary custom Jetson supply; **energy model with Mohammed F** | Power-tree and rail/load requirements, sensing plan, schematic and staged bench-test plan |
| **Yazan Ramadan** — ME, SLU | All mechanical work: payload mechanism, custom parts, fabrication, mounting and structural improvements; assists with flight-controller settings and physical constraints | Payload/mount CAD, measured mass and center of gravity, retention and release test plan |
| **Ahmad Hamzeh** — CompE, WashU | QR-code software with Mohammed A; Jetson setup and computing, computer vision, machine learning and reinforcement-learning exploration | Reproducible Jetson environment and camera/label-decoding pipeline integrated with Mohammed A's package validator |
| **Rizan Mohammed Althaf (Mohammed A)** — CS, SLU | QR-code software with Ahmad: label generation, package-data format and intake; integration with the Jetson workflow | Versioned label specification, generator and validation examples |
| **Alend Barwary** — CompE, SLU | Jetson–Pixhawk communication and mission integration: flight-path generation, mission upload and execution monitoring, working with Mohammed A and Ahmad | Simulated mission demo covering route generation, MAVLink upload acknowledgment and execution-status monitoring |

Ownership identifies responsibility, not completion. Finished work should link to code, CAD, measurements or test records under its actual contributors.

## Ahmad: Jetson runtime and perception

Ahmad deploys the camera/label-reading pipeline on the Jetson and integrates the package-label software developed jointly with Mohammed A. He collaborates with Alend on the onboard runtime and the handoff of validated package data to mission planning; Alend owns the Jetson–Pixhawk mission interface.

Start with a reproducible camera/label-decoding demo and connect it to Alend's simulated mission interface. Later CV/ML work should address a measured problem, such as unreliable label/placement-marker detection. Compare it with a simple baseline. Reinforcement learning remains an optional simulation research direction, outside the initial delivery demonstration.

## Shared boundaries

- **Mohammed A + Ahmad:** jointly develop the package schema, QR generation, decoding and validation; Ahmad also connects the pipeline to the Jetson camera/runtime.
- **Mohammed A + Ahmad → Alend:** validated package records and destination data → flight-path generation and mission integration.
- **Mohammed F + Jad → Alend:** versioned energy estimator, calibrated input requirements and prediction limits → route feasibility and planning.
- **Yazan → Mohammed F + Alend:** physical payload/clearance limits and attachment/release feedback → aircraft limits and mission states.
- **Mohammed F:** resolves cross-subsystem changes and coordinates integration acceptance.

## Alend: Jetson–Pixhawk communication and mission integration

Alend develops flight-path generation, mission upload and execution monitoring, working with Mohammed A and Ahmad to connect validated package data to the mission workflow. The Jetson prepares the route; the Pixhawk executes the uploaded, operator-approved mission.

Start with a simulated aircraft: generate a mission from validated destination data, upload it over MAVLink, verify acceptance and monitor mission progress. Document interface configuration and handling of rejected uploads or communication loss before hardware integration.

Use one owner per issue, list collaborators, and commit from each contributor's own account. See [workflow](../CONTRIBUTING.md).
