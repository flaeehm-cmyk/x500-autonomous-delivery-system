# Validation plan

Set measurable pass/fail criteria before each test. Payload limits, reserve values and performance targets remain to be established for the assembled aircraft; this page is not an approved flight envelope.

| Area | Evidence to produce |
| --- | --- |
| Flight baseline | Exact configuration, repeatable unloaded behavior, reviewed vibration/navigation and tested recovery behavior |
| Battery and power | Voltage/current comparison, uncertainty, complete sensing coverage, usable-energy method, rail/load/thermal measurements and reset observations |
| QR intake | Read results under stated distance/lighting; malformed, unsupported-version and unknown-destination cases rejected |
| Physical package checks | Scale calibration; mass mismatch and dimension/fit limits handled; aircraft/package attachment mass accounted for |
| Mission decisions | Over-mass, insufficient-energy, stale-data and unsupported-condition cases rejected with reasons |
| Payload | Retention under defined load/alignment cases; physical attachment/support/release evidence; restart and loss-of-power behavior |
| Energy estimator | Whole-flight holdout evaluation, error distribution, worst underprediction and justified uncertainty/reserve assumptions |
| Integrated mission | Predicted versus measured Wh, route execution, placement/release result, interventions and return/landing outcome |

Publish sample counts and failures. Select targets that follow from the actual requirements rather than using an arbitrary percentage or a small run count as proof of reliability.

## Fault and integration cases

Define responses for companion reset, communications loss, unknown payload state, stale telemetry, duplicate requests, failed release and a partially used battery reconnected after reboot. A successful command acknowledgment does not establish physical attachment or release.

Test software/fault behavior in simulation and on the bench first. Remove propellers for bench work involving motor outputs. Flight progression requires a reviewed test plan, measured mass/center of gravity and established operational limits; begin payload integration with secured inert loads.

Use the [test record template](templates/test-record.md) for configuration, method, instruments, expected/observed result and evidence. Preserve failed tests and retests separately.
