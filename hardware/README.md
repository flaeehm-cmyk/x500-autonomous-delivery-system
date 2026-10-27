# Hardware inventory and integration status

This is a documented inventory, not a fully measured mass/power bill of materials. Exact assembly mass, connector limits, and power consumption must be captured on the installed hardware.

| Subsystem | Documented hardware / choice | Status |
| --- | --- | --- |
| Primary airframe | Holybro X500 V2 ARF | Built and flown |
| Flight controller | Pixhawk 6C Mini, Model A in the log review | Installed |
| Navigation | M9N GPS | Documented installed |
| RC link | RadioMaster RP3 receiver / RadioMaster control link | Documented installed; configuration-specific failsafe verification open |
| Main power measurement / FC supply | Holybro PM02 V3 | Installed; single-point voltage agreement reported |
| Propulsion distribution | Original X500 ARF PDB and stock propulsion system | Installed; two spare XT30 peripheral connections identified |
| Flight battery | Tattu 4S 5200 mAh, 14.8 V nominal, 35C | Documented test pack; usable energy is not established by its label |
| Companion computer | NVIDIA Jetson Orin Nano Super Developer Kit | Bench setup reported |
| Storage | Samsung 990-family 1 TB NVMe | Installed in reported Jetson bench setup; retain exact model from device report in next update |
| Auxiliary regulator / branch protection | Candidate evaluation in progress | Not recorded as installed or qualified |
| Camera | USB/CSI options under evaluation | No final selection recorded |
| Payload mechanism and sensing | Electromagnet concept; EPM/latch comparison in scope | Planned |
| Weighing / dispatch station | Load-cell station concept | Planned |
| Custom power board | Jad's assigned design workstream | In development; no schematic/PCB artifact included |

The nominal pack-label product is 14.8 V × 5.2 Ah = 76.96 Wh. It is a nominal rating, not measured usable energy and not a mission budget.

## Integration records to add

Use versioned schematics and CAD exports, with units, revision, author, component designators, and connector labels. Record total installed mass and input power, including mounting, wiring, cooling, regulator losses, and payload interface.

Document the exact regulator before selecting protection, wiring, or connectors. Do not transplant earlier proposed part values into an approved design.

## Historical Mark4 platform

Project notes describe a Mark4 7-inch frame, EMAX ECO II 2807 1300 KV motors, HGLRC 60 A four-in-one ESC, Pixhawk 6C Mini, M9N GPS, and RadioMaster RP3 integration. This is historical inventory; the current repair/flight condition is not established. The July HGLRC stack reference screenshots are not a substitute for its final as-built wiring.

See [architecture](../docs/architecture.md), [decision record](../docs/decisions.md), and [power case study](../docs/case-studies/power-and-compute.md).
