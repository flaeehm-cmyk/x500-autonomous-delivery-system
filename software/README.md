# Software

## Runnable now

[Flight-summary analysis](../analysis/summarize_segments.py) is an offline Python 3.10+ utility using only the standard library. It validates the included CSV and generates Markdown/JSON reports. See [run instructions](../README.md#run-the-analysis).

## Delivery software under development

| Component | Owner / proposed lead | Responsibility |
| --- | --- | --- |
| QR-code software and package intake | Mohammed A + Ahmad | Generate/read QR labels, define versioned package records and validate decoded data |
| Jetson perception and runtime | Ahmad | Camera acquisition, label decoding and reproducible onboard software environment |
| Companion autonomy integration | Ahmad, proposed | Integrate route evaluation, mission state handling and the Pixhawk interface |
| Energy estimator | Mohammed F + Jad | Predict mission Wh and uncertainty from calibrated measurements |
| System integration | Mohammed F | Agree interfaces, aircraft constraints and end-to-end tests with subsystem owners |

The label describes a delivery request. The validator, energy estimator, route evaluator and operator must all accept it before execution. See [package workflow](../docs/package-workflow.md) and [energy model](../docs/energy-model.md).

Use `software/package-labels/` and `software/companion/` when their first runnable artifacts are added; keep offline model work in `analysis/energy-model/`. Each component should include a small runnable example, dependency versions and tests for its inputs and failure cases.

Develop against simulated aircraft I/O first. Record the actual JetPack/Jetson Linux version and camera/MAVLink configuration when hardware integration begins. ML/RL experiments should have their own reproducible evaluations and a baseline comparison.
