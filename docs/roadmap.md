# Development roadmap

Current responsibilities are in [team ownership](team.md). Subsystem development can proceed in parallel; integration advances when the preceding evidence is available.

## Next deliverables

| Priority | Deliverable | Owner | Done when |
| --- | --- | --- | --- |
| 1 | Aircraft and measurement baseline | Mohammed F + Jad; Yazan assists with mechanical/configuration work | Current firmware/parameter export, installed mass, voltage/current checks and reviewed baseline flight record are linked |
| 1 | Power architecture and PCB requirements | Jad | Temporary supply and future PCB have separate power trees, rail/load budgets, sensing coverage and bench-test plans |
| 1 | Payload and mounting design | Yazan | CAD, mass/center-of-gravity estimate and a retention/release test plan support the chosen prototype |
| 2 | Package QR specification and generator | Mohammed A | Valid labels and defined rejection cases can be generated and parsed reproducibly |
| 2 | Jetson camera and mission-interface demo | Ahmad; companion-integration role proposed | Recorded software environment, camera decoding demo and simulated mission/telemetry interface work together |
| 2 | Baseline energy estimator | Mohammed F + Jad | Calibrated dataset, reproducible predictions and errors on held-out flights are published |

Alend's assignment is open. A bench weighing/validation station is the proposed starter contribution, subject to agreement.

## Integration sequence

1. **Software dry run:** package input → validation → candidate-route/energy evaluation → operator decision, with simulated aircraft I/O.
2. **Bench integration:** qualify compute power, communications, physical payload sensing and release behavior.
3. **Controlled flight integration:** use secured inert loads and a reviewed configuration/test plan.
4. **Delivery demonstration:** record package, route, predicted/measured energy, placement/release outcome and operator interventions.

An implementation or flight result closes a milestone; a document describing the intended behavior does not. Record acceptance criteria before testing using the [validation plan](validation-plan.md).

## Keep the plan current

Use GitHub Issues for active tasks and blockers. Each issue needs one owner, collaborators if relevant, and an observable completion criterion. Update this page only when priorities or milestones change; put weekly details and evidence in the issues.
