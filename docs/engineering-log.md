# Engineering log

This is a retrospective project record assembled on 26 October 2026. Dates below describe work or observations; they do not imply commits were made on those dates.

| Period | Work and observations | Status / next step |
| --- | --- | --- |
| June–August 2026 | Mark4 7-inch development platform; propulsion and Pixhawk integration; receiver/GPS wiring and pre-arm troubleshooting. Project notes record damage to GPS/telemetry connections after a July crash. | Historical project-lead account. Original build media and repair evidence are not included here. |
| August–September 2026 | Moved the main integration effort to the Holybro X500 V2 ARF. Established PM02/PDB/flight-controller power arrangement. Selected the Jetson Orin Nano Super after considering a Pi 5 plus AI accelerator. | Hardware/design history; no quantified platform-comparison result. |
| 18 September 2026 | Reviewed summary contains short armed sessions and several inferred airborne AltHold/RTL intervals. | Included CSV. Mode changes on the ground are not counted as flight. |
| 5–9 October 2026 | Investigated AltHold drift and Loiter shaking. Subsequent records document airborne AUTO waypoint sequences. | Flight foundation demonstrated; vibration investigation remains open. |
| 10 October 2026 | Reviewed five log files, including one unarmed placeholder. Four armed source files contribute the 30-row summary. Identified battery measurement, vibration, mission termination, and failsafe-verification questions. | Historical review; its proposed parameters are not a current approved configuration. |
| 17 October 2026 | Adopted autonomous parcel-delivery scope revision 1.1 and proposed six workstreams. | Scope established; proposed ownership is not evidence of completed subsystem work. |
| 19 October 2026 | Lead reported two mission flights using the same battery across a disconnect/reconnect. Voltage comparison improved from 16.405 V in Mission Planner versus 16.68 V on a meter to 16.68 V on both. Mechanical fasteners were inspected/tightened. | Single-point voltage agreement reported. Revalidate current measurements, configuration, and vibration on new logs. |
| October 2026, through 25 October | Jetson / Samsung 1 TB NVMe setup and storage checks; three subsequent successful boots reported. Camera and auxiliary-regulator options evaluated. | Bench progress. Final OS version, camera choice, and flight power integration are not verified in this snapshot. |
| 26 October 2026 | Prepared this repository, curated the evidence register, and added an offline script for the historical summary. | Documentation/tooling work. This does not establish new flight or delivery capability. |

## Next update format

Each new entry should name the date, author, configuration, test or change, result, evidence path, unresolved issue, and next action. Link the related issue or pull request. Preserve unsuccessful tests when they explain a decision.
