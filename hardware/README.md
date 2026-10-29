# Hardware

## Current platform

| Assembly | Hardware | Status |
| --- | --- | --- |
| Airframe and propulsion | Holybro X500 V2 ARF with original PDB and propulsion system | Built and flown |
| Flight controller | Pixhawk 6C Mini; M9N GPS; RadioMaster control link | Installed |
| Flight power | Holybro PM02 V3; Tattu 4S 5200 mAh battery | Installed; current calibration remains open |
| Companion computer | NVIDIA Jetson Orin Nano Super; Samsung 1 TB NVMe | Bench setup reported |
| Jetson supply | Temporary custom power solution | In development; qualification record pending |
| Camera | Selection under evaluation | No final installation recorded |
| Payload mechanism | Magnetic and mechanical options under evaluation | Design work; no qualified payload limit |
| Integrated power PCB | Jad's replacement for PM02, PDB and temporary Jetson supply | In development; design files not yet included |

The battery's nominal rating is **14.8 V × 5.2 Ah = 76.96 Wh**. Usable energy must be measured for the actual pack and operating conditions.

## Power PCB — Jad

The intended board combines propulsion distribution, regulated flight-controller and companion/peripheral supplies, battery voltage/current sensing and appropriate branch protection. Confirm rail voltages, peak/continuous loads, connector limits, grounding and sensor coverage before layout.

Publish the schematic and native PCB files with readable PDF exports, BOM, board revision and bench measurements. Qualify the sensing and each supply before replacing the established flight-power path. The temporary Jetson supply remains a separate documented assembly until then.

## Mechanical system — Yazan

Owns payload retention/release, custom mounts and parts, fabrication, structural changes, mass and center of gravity. Coordinates physical constraints and relevant flight-controller settings with Mohammed F.

Publish native CAD and reviewable exports, assembly drawings, measured mass, material/fastener information and retention/release evidence. No EPM, electromagnet or latch is selected as a qualified flight mechanism yet.

## File placement

As the first artifacts arrive, use `hardware/power/` for PCB work and `hardware/mechanical/` for CAD and fabrication. Keep each assembly's source, BOM, exports and test notes together. These paths are conventions, not claims that design files already exist.

[Power architecture](../docs/architecture.md) · [Power case study](../docs/case-studies/power-and-compute.md) · [Earlier Mark4 work](../docs/engineering-log.md)
