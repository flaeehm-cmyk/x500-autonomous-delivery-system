# Validation plan

These are proposed checks and acceptance targets adapted from scope revision 1.1. None is marked passed by this document. Flight conditions and limits must be established for the actual assembled system.

## Evidence required per test

Record test ID, date, author, hardware/software configuration, procedure, instruments, input conditions, raw or derived evidence path, expected result, measured result, pass/fail decision, and limitations. Capture failures and retests as separate records.

## Verification matrix

| ID | Area | Proposed criterion / output | Setting |
| --- | --- | --- | --- |
| V01 | Baseline flight | Stable unloaded behavior; reviewed vibration/navigation; configuration-specific recovery behavior | Simulation, bench, supervised flight |
| V02 | Battery measurements | Voltage/current comparison across relevant conditions, documented uncertainty, and usable-energy method | Bench and subsequent flight logs |
| V03 | Electrical integration | No FC/companion reset in defined startup and load-step cases; measured rails and temperatures within selected component limits | Bench |
| V04 | Parcel intake | At least 19/20 valid labels read under stated lighting; all defined malformed/unauthorized examples rejected | Bench/software |
| V05 | Weighing | Within ±10 g over the intended parcel range using reference masses | Bench |
| V06 | Mission decisions | Reject all defined over-mass, insufficient-energy, unknown-destination, stale-data, and unsupported-dimension cases; preserve reason/model version | Software/simulation |
| V07 | Payload handling | At least 30 bench attachment/release cycles with physical confirmation and no unintended release; separate load, alignment, restart, power-loss, and sensor-fault cases | Bench |
| V08 | Energy model | Initial target: MAPE ≤15% on at least six held-out missions; also publish worst underprediction and test conditions | Offline analysis |
| V09 | Integrated delivery | Five consecutive completed deliveries within the tested envelope, with no uncommanded release or safety-critical anomaly | Supervised flight after earlier gates |
| V10 | Optimization comparison | At least three matched baseline/optimized pairs where practical; publish Wh, time, distance, conditions, and uncertainty | Offline analysis / controlled flights |

These sample sizes are prototype targets. Meeting them would not by itself establish reliability certification or a commercial operating envelope.

## Failure cases to define

- Companion reset or communications loss: retain payload, inhibit release, and execute the previously tested response for the particular flight state.
- Unknown attachment, support, or release state: do not treat the command as proof of the physical state.
- Insufficient energy or navigation degradation: terminate the delivery attempt through the validated contingency plan; avoid an indefinite hold.
- Battery reconnect: maintain physical-pack accounting across boot sessions.
- Duplicate or stale order/command: preserve mission identity and prevent an unintended repeat release.

## Flight integration boundaries

Use simulation and bench testing before introducing faults to an aircraft. Bench work involving motor outputs is done with propellers removed. Initial flight integration uses secured inert loads and an operator-approved test plan, within visual line of sight and applicable site/airspace requirements.

Before payload flight, document measured takeoff mass, payload mass/dimensions, center of gravity, clearance, speed/acceleration and environmental limits, battery condition, reserve, and placement geometry. This repository supplies no ready-to-load flight configuration or approved numeric flight envelope.

See the [test record template](templates/test-record.md).
