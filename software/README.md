# Software status

## Runnable now

The repository contains one offline utility: [flight-segment summary analysis](../analysis/summarize_segments.py). It reads the included CSV, validates its structure and numeric values, and reproduces Markdown/JSON summaries. It needs Python 3.10+ and the standard library only.

This utility was created while preparing the repository. It is not flight-tested onboard software, a raw DataFlash decoder, or a mission planner.

## Proposed software boundaries

| Component | Responsibility | Status |
| --- | --- | --- |
| Order intake | Decode order ID, resolve approved record, reject malformed/unauthorized requests | Planned |
| Dispatch station interface | Read measured mass and parcel/station state | Planned |
| Energy model / planner | Predict mission components and reserve; report accept/reject reasons | Planned |
| Mission manager | Operator approval, upload verification, state transitions, recovery rules | Planned |
| Payload interface | Report physical state, enforce release conditions, confirm separation | Planned |
| Event recorder | Join orders, configurations, energy, state events, and outcomes under a mission ID | Planned |
| Perception | Camera intake and later marker-assisted placement | Planned; camera selection open |

Begin with deterministic interfaces and simulated aircraft I/O. Record units, timebase, acknowledgments, timeouts, and unknown-state behavior before hardware integration.

## Environment record still needed

Capture installed JetPack / Jetson Linux and package versions from the actual Jetson. Record flight-controller firmware and parameter-export version for each integration test. Prior recommendations are not an installed software manifest.

Do not add empty flight-code modules merely to imply implementation. Introduce each subsystem with its first working example, tests, and evidence.
