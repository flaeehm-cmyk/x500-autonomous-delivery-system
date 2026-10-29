# Design decisions

Record choices that changed the architecture, cost, risk or test plan. Keep routine purchases and troubleshooting in issues or test records.

## ADR-001 — Move primary development from Mark4 to X500

**Adopted; historical rationale confirmed 28 October 2026.**

The Mark4 7-inch FPV platform was initially intended to be the smart aircraft. The team found that its available integration space was too limited for the planned computing and payload work, so the X500 became the main development platform.

This is a packaging/integration decision. No controlled Mark4-versus-X500 performance comparison is claimed.

## ADR-002 — Use the Jetson Orin Nano Super

**Adopted.**

Selected for the planned onboard perception and computing work after considering a Raspberry Pi 5 with an AI accelerator. The decision creates power, cooling, mounting and software-integration requirements. Workload performance and airborne power use still need measurement.

## ADR-003 — Change from tracking to parcel delivery

**Delivery scope adopted 17 October 2026.**

The earlier concept centered on tracking, including a possible second aircraft. The current objective is a supervised, single-parcel delivery workflow with package identification, energy-based feasibility and controlled placement.

Tracking belongs in the project's design history. It is not a current milestone or a demonstrated capability in this repository. The first delivery version uses manual loading and approved sites/routes.

## ADR-004 — Develop the full power PCB alongside temporary integration

**Current direction confirmed 28 October 2026.**

Retain the established PM02/PDB flight-power path while developing the temporary Jetson supply. Jad's PCB is intended to replace those assemblies with a complete power-distribution and sensing solution after bench qualification.

Record the two configurations separately so measurements and the energy model remain traceable.

## ADR-005 — Test payload mechanisms before selecting one

**Open.**

Compare EPM, continuously powered electromagnet and mechanical-latch options using assembled mass, retention under representative loads, power-loss behavior and confirmed release. Yazan owns the mechanical evaluation. No mechanism or payload rating is qualified yet.

## ADR-006 — Begin with a measured energy baseline

**Development approach; owners Mohammed F and Jad.**

Use calibrated measurements and a lookup table or small regression before evaluating ML. Include delivery, return/landing, uncertainty and reserve. Validate on whole flights excluded from fitting, including worst underprediction.

See [energy-model explanation](energy-model.md).

## ADR-007 — Encode package data in a QR label

**Current direction confirmed 28 October 2026.**

Mohammed A and Ahmad's QR software encodes package identity, mass, dimensions and an approved destination ID. The Jetson reads the label and validates the record before route evaluation. Physical measurements and current aircraft/battery state remain separate checks.

The first version uses one versioned QR format; additional barcode formats can follow a demonstrated need. See [package workflow](package-workflow.md).
