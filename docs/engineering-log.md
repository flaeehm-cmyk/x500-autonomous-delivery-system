# Project history

A concise retrospective of work that shaped the current system. Earlier activity predates this repository's commits; reported progress is distinguished from included artifacts in the [evidence register](evidence.md).

| Period | Work or decision | Result / lesson |
| --- | --- | --- |
| Early development, before the X500 | Built and worked with the Mark4 7-inch platform as the intended smart drone | Available space constrained the planned computing/payload integration |
| August–September 2026 | Moved primary development to the X500; established the PM02/PDB/Pixhawk power arrangement; selected the Jetson | A larger integration platform became the project baseline |
| Earlier concept, before 17 October | Explored an autonomous tracking / multi-UAV scope | Superseded concept; no completed tracking demonstration is documented |
| September–October 2026 | Flight testing, AltHold/Loiter troubleshooting and AUTO waypoint missions | The included CSV records 30 armed intervals; the October review documents airborne AUTO sequences |
| 10 October 2026 | Reviewed flight logs and produced the historical segment summary | Identified measurement, vibration and mission-termination questions; current/energy data were insufficient for an energy model |
| 17 October 2026 | Changed the objective to supervised autonomous parcel delivery | Package intake, energy feasibility and controlled placement became the integration goal |
| 19 October 2026 | Adjusted voltage measurement and inspected/tightened mechanical fasteners | Reported Mission Planner/multimeter agreement at 16.68 V; current calibration and repeat flight evidence remain open |
| October 2026, through 25 October | Jetson / NVMe setup and restart checks | Three successful subsequent boots reported; aircraft integration pending |
| 26–28 October 2026 | Added reproducible summary analysis, transferred the repository to the team organization and clarified subsystem ownership | Shared development workflow; energy model assigned to Mohammed F and Jad |

## Keep future entries selective

Add an entry when a test closes a question, a failure changes the design, or a subsystem reaches a milestone. Include the date, contributor, result and link to the issue/PR or test record. Keep detailed session notes with that evidence.

[Design rationale](decisions.md) · [Current roadmap](roadmap.md)
