# Power and compute case study

The established flight-power path is battery → PM02 V3 → original X500 PDB → ESCs, with the Pixhawk supplied by the PM02.

## Reported progress

- On 19 October, Mohammed F adjusted the voltage measurement from 16.405 V in Mission Planner versus 16.68 V on a meter to 16.68 V on both. This is single-point agreement; current calibration and usable energy remain open.
- Jetson Orin Nano Super / Samsung 1 TB NVMe setup and three successful subsequent boots were reported.
- A temporary custom Jetson supply is in development. Jad's complete power PCB is intended to replace that supply, the PM02 and the original PDB after qualification.

## Next measurements

Record the temporary supply's actual schematic, input/output rails, protection and complete installed load. Measure startup/load-step behavior, temperature and resets with the Jetson, SSD, cooling and selected camera.

Validate the battery sensing boundary so the [energy model](../energy-model.md) includes all loads. Track the physical battery across reconnects; a reset consumption counter is not a newly charged pack.

Publish the actual Jetson software versions and console results, then verify the MAVLink interface before airborne integration.

[Hardware ownership](../../hardware/README.md) · [Power architecture](../architecture.md) · [Evidence](../evidence.md) · [ArduPilot calibration reference](https://ardupilot.org/copter/docs/common-power-module-configuration-in-mission-planner.html)
