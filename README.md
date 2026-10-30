# X500 Autonomous Parcel Delivery

An independent six-person student project developing a supervised parcel-delivery system on the **Holybro X500 V2**, with **Pixhawk / ArduPilot** flight control and **NVIDIA Jetson Orin Nano Super** onboard computing.

The intended workflow is to read a package's QR label, validate its mass, dimensions and destination, estimate the energy needed for delivery and return, then execute an operator-approved mission.

**Current stage:** waypoint flight is documented; the integrated delivery system is in development.

## Progress

| Area | Current result |
| --- | --- |
| Flight | AUTO waypoint sequences documented in the October flight review. [Flight case study](docs/case-studies/flight-validation.md) |
| Analysis | Python utility and 10 tests reproduce a summary of 30 armed intervals from four logs. [Results](analysis/results.md) |
| Onboard computing | Jetson / NVMe bench setup and three successful subsequent boots reported. Aircraft integration remains open. |
| Delivery | Package-label software, energy prediction, custom power PCB and payload hardware are development work. |

The [evidence register](docs/evidence.md) distinguishes included artifacts from team-reported progress. No integrated parcel-delivery demonstration is claimed yet.

## System

The Pixhawk runs flight control and uploaded missions. The Jetson is intended to handle camera input, package validation and mission planning. A laptop provides operator review.

[Architecture](docs/architecture.md) · [Package workflow](docs/package-workflow.md) · [Energy model](docs/energy-model.md)

## Team

| Member | Responsibility |
| --- | --- |
| **Mohammed Flaeeh (Mohammed F)** | Project lead; systems integration, coordination, flight validation; energy model with Jad |
| **Jad Khdeer** | Complete power-distribution PCB; energy model with Mohammed F |
| **Yazan Ramadan** | Mechanical design, fabrication, payload and structural work; support for flight-controller configuration |
| **Ahmad Hamzeh** | QR-code software with Mohammed A; Jetson computing, computer vision and ML |
| **Rizan Mohammed Althaf (Mohammed A)** | QR-code software with Ahmad: label generation, package-data format and intake |
| **Alend Barwary** | Assignment pending |

See [team ownership and deliverables](docs/team.md).

## Explore the work

- [Hardware](hardware/README.md) and [software](software/README.md): subsystem boundaries and current artifacts.
- [Roadmap](docs/roadmap.md): next deliverables and who owns them.
- [Project history](docs/engineering-log.md): Mark4 development, the move to X500 and the change from tracking to delivery.
- [Design decisions](docs/decisions.md): the constraints behind those choices.

## Run the analysis

Python 3.10+; standard library only. From the repository root:

```bash
python analysis/summarize_segments.py
python -m unittest discover -s tests -v
python analysis/summarize_segments.py --check
```

On Windows, use `py -3` if needed. The tool analyzes the included summary CSV. Its airborne-time totals are not battery endurance; the dataset does not contain the current measurements needed for energy modeling.

[Data and method](data/README.md) · [Team workflow](CONTRIBUTING.md) · [GitHub guide](docs/github-guide.md) · [Attribution](ATTRIBUTION.md)
