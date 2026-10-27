# Case study: measurement and companion-computer integration

**Engineering question:** How can the project add onboard computing while maintaining a known flight-power arrangement and trustworthy energy data?

## Established power path

The recorded wiring is battery → Holybro PM02 V3 → original X500 PDB → ESCs. The Pixhawk is powered by the PM02. Two spare XT30 peripheral connections were identified on the PDB.

The planned Jetson branch uses appropriate branch protection and a regulator qualified for the actual input range and complete load. Pololu and DROK options were discussed; this snapshot does not record a selected, installed, or flight-qualified regulator.

## Voltage comparison

On 19 October, the project lead reported 16.405 V in Mission Planner versus 16.68 V on the multimeter before further adjustment. The reported subsequent comparison was 16.68 V on both.

This supports single-point agreement to the reported display resolution. It does not establish meter accuracy, agreement throughout discharge, current calibration, or true battery capacity. ArduPilot documents voltage and current calibration as related but distinct measurements. [Calibration reference](https://ardupilot.org/copter/docs/common-power-module-configuration-in-mission-planner.html)

The lead also reported reusing a pack after disconnecting and reconnecting it during the 19 October session. A restarted consumption counter must not be treated as a recharged battery.

## Jetson and SSD bring-up

The Orin Nano Super was selected and bench setup with a Samsung 1 TB NVMe drive was reported. The project lead reported three successful subsequent boots. This is useful bring-up evidence; it is not a quantified reliability result.

The exact JetPack / Jetson Linux version, SMART reports, storage-test command/output, and boot-test conditions should be captured as text in a future evidence update. The repository does not turn earlier software-version recommendations into an installed-version claim.

NVIDIA documents the developer kit's supported storage and interfaces, including NVMe and DisplayPort. Those hardware capabilities do not establish that a particular airborne installation has been tested. [Hardware reference](https://docs.nvidia.com/jetson/orin-nano-devkit/user-guide/latest/hardware_layout.html)

## Next experiment

On the bench, record the complete installed load: Jetson board, SSD, cooling, selected camera, regulator, connectors, and wiring. Measure startup and steady/load-step rail behavior, input current, regulator temperature, and reset events. Record instrument, configuration, ambient conditions, and duration.

After electrical qualification, verify the MAVLink connection and stale-data/link-loss behavior with the actual flight controller. Only then evaluate the fully assembled aircraft's mass, balance, vibration, and energy consumption.

**Current result:** voltage comparison and computer bring-up have reported progress. Current sensing, the aircraft supply branch, and airborne companion-computer operation remain open.
