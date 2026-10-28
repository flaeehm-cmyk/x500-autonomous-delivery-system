# Development roadmap

This roadmap follows the 17 October scope. Dates are not promised; each milestone advances on evidence. Numerical targets below and in the validation plan remain proposed.

| Milestone | Deliverables | Evidence required to close | Current status |
| --- | --- | --- | --- |
| M0 — Flight foundation | X500 configuration, waypoint-flight record, initial log review | Traceable flight results | AUTO foundation documented; baseline cleanup remains open |
| M1 — Reliable baseline | Mass/power budget, calibrated battery measurements, mechanical/vibration review, configuration-specific failsafe tests | Repeatable unloaded results and reviewed limits | In progress; single-point voltage agreement reported |
| M2 — Companion integration | Protected power branch, mounted compute assembly, MAVLink interface | Bench rail/load/reset tests and verified communications | Jetson bench bring-up reported; aircraft integration planned |
| M3 — Dispatch and planning | Package QR/barcode label read by the Jetson camera, destination flight-path planning, measured mass, baseline energy model, operator decision | Runnable software dry run and rejection tests | Planned |
| M4 — Payload qualification | Fixture, retention mechanism, support/attachment sensing, controlled release | Load cases, restart/power-loss behavior, repeated bench cycles | Planned |
| M5 — Integrated prototype | Simulation, secured inert-load flights, supported placement, return/report | Tested operating envelope and repeatable delivery records | Planned |

## Ready-to-open engineering issues

Use the engineering-task issue template and assign the owner after team agreement.

| Priority | Issue title | Completion evidence |
| --- | --- | --- |
| 1 | Capture the current aircraft configuration and baseline mass | Dated parameter export, firmware version, wiring record, complete mass table |
| 1 | Validate battery current and voltage measurements | Instrument comparisons, test conditions, scale/offset settings, uncertainty |
| 1 | Reassess vibration after mechanical inspection | Shareable log extraction and matched maneuver comparison |
| 1 | Verify flight failsafes for the current configuration | Simulation/bench records and exact tested settings |
| 2 | Qualify the Jetson auxiliary power branch | Schematic, protection/connector rationale, startup and load-step measurements |
| 2 | Record Jetson software and storage baseline | Installed versions, SMART report, storage verification output, restart log |
| 2 | Verify the Jetson–Pixhawk MAVLink interface | Connection details, acknowledgments, timestamps, stale-data and restart cases |
| 3 | Define the package label format and read it with the Jetson camera | Label specification, sample labels, read results under test lighting/distances, rejected-label cases |
| 3 | Plan the flight path from the labelled destination | Route-planning examples and tests against approved destinations |
| 3 | Demonstrate dispatch workflow with simulated aircraft I/O | Label read, weigh, validate, plan, approve, and reject-case records |
| 3 | Compare payload retention mechanisms | Assembled mass, power, retention tests, supported release, fault behavior |
| 4 | Validate the mission-energy model on held-out flights | Dataset split, errors, worst underprediction, reserve method |
| 4 | Record the first integrated delivery demonstration | Full mission record, placement result, operator interventions, final energy |

## Portfolio release evidence

The next substantial release should add a real aircraft photograph, a concise demonstration clip, reviewed configuration records, actual team code, CAD/PCB artifacts as they become available, and measured outcomes. Show one rejected mission or a controlled simulated fault when the relevant subsystem works.

No code, CAD, PCB, delivery result, or flight video is currently claimed for an unimplemented workstream.
