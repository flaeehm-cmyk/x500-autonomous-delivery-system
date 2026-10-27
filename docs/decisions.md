# Engineering decision record

This record distinguishes decisions made from options still being evaluated. Historical rationale is reconstructed from project notes; it is not a quantitative trade study unless measurements are attached.

## ADR-001 — Use the X500 as the primary integration platform

**Decision:** selected, August–September 2026.

The earlier Mark4 7-inch build established experience with propulsion, flight-controller wiring, receiver/GPS integration, and troubleshooting. Its integration constraints led the project toward the Holybro X500 V2 ARF for the companion-computer and payload program.

The X500 became the primary flight-test platform. The Mark4 remains a possible later research vehicle; the delivery demonstration does not depend on a second aircraft.

**Consequence:** prioritize one validated aircraft and carry forward the earlier build lessons. No measured Mark4/X500 endurance or payload comparison is claimed.

## ADR-002 — Select the Jetson Orin Nano Super

**Decision:** selected; bench setup subsequently reported.

The project considered a Raspberry Pi 5 with an AI accelerator before selecting the Jetson for its intended perception and onboard-computing work. This records a project choice, not a measured performance win.

**Consequence:** the system must account for the development board, SSD, cooling, camera, mounting, and conversion losses in its mass and power budget. The final airborne compute configuration remains unqualified.

**Evidence still needed:** representative workload latency, total input power, startup behavior, thermal response, and the flight-time effect with the actual installation.

## ADR-003 — Start with supervised parcel delivery at fixed sites

**Decision:** adopted in the 17 October scope, revision 1.1.

The initial concept expanded from tracking toward parcel delivery. The first demonstration was narrowed to one parcel, manual loading, an approved route, a prepared delivery area, supported placement or landing, and operator oversight.

**Consequence:** QR intake, measured mass, explainable mission feasibility, and release confirmation have priority. Autonomous airborne pickup, a full multi-UAV system, and advanced ML are deferred.

## ADR-004 — Keep the established flight power path

**Decision:** retained; auxiliary branch design remains open.

Use the existing battery → PM02 V3 → original PDB path, with the Pixhawk supplied by the PM02. Qualify a separate protected regulator branch for the Jetson while the custom power module develops.

**Consequence:** a companion-computer prototype need not wait for the full custom board. The branch must still be measured and tested with the actual load.

## ADR-005 — Evaluate payload retention before selecting a gripper

**Decision:** open.

The concept began with a continuously energized electromagnet. The scope now compares an electropermanent magnet and a mechanical latch against total mass, power demand, retention during loss of auxiliary power, packaging strength, and verified release.

A reinforced attachment interface and pull, shear, peel, alignment, and restart tests are part of the proposed evaluation. No gripper is recorded as installed, and no holding force or payload limit is claimed.

**Next evidence:** candidate comparison with measured assembled mass, representative retention tests, support sensing, and release confirmation.

## ADR-006 — Fit a baseline energy model before adding ML

**Decision:** proposed in the delivery scope.

Begin with a lookup or simple regression model, then evaluate additional complexity against held-out measurements. Include loaded outbound, placement, return, uncertainty, and reserve in the mission decision.

**Consequence:** first establish valid current/voltage measurements and comparable test missions. Lower mean prediction error alone is insufficient if worst-case underprediction becomes worse.
