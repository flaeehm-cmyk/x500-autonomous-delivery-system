# Evidence register

Snapshot: 26 October 2026. The purpose of this register is to make each portfolio claim traceable.

## Source hierarchy

1. Raw artifacts with configuration and timestamps: strongest basis for independent reproduction.
2. Dated derived reports or datasets: useful, but dependent on the earlier extraction.
3. Project-lead observations: explicitly reported, with supporting artifacts to be added.
4. Design requirements and targets: planned work.

This package contains a derived flight-summary CSV and newly reproducible aggregation. It does not include raw DataFlash logs, a current parameter export, schematics, CAD, flight video, or full Jetson console transcripts.

## Claim-to-source map

| ID | Claim / material | Source and status | Limit |
| --- | --- | --- | --- |
| E01 | Airborne AUTO waypoint sequences on 7 and 9 October | `X500_Flight_Log_Review_2026-10-10.pdf`, existing AI-assisted review of uploaded logs | Raw logs were not reprocessed for this repository. Curated findings appear in the flight case study. |
| E02 | 30 armed intervals across four source files | `x500_flight_segment_summary.csv`, generated 10 October; full table reproduced in [data](../data/flight_segment_summary_2026-10-10.csv) | CSV fields were preserved from the source's text extraction. The original binary log-to-CSV extractor is not packaged. |
| E03 | 16.68 V / 16.68 V voltage comparison | Project-lead report, 19 October | One reported comparison, not a multi-point calibration or current validation. |
| E04 | NVMe setup and three successful subsequent boots | Project-lead setup thread, through 25 October | Console captures and OS version are not packaged. No airborne-compute claim. |
| E05 | Delivery objective, team workstreams, and test targets | `X500_Autonomous_Parcel_Delivery_Project_Scope.docx`, revision 1.1, 17 October | Design intent. Team assignments are proposed; numerical targets are not achieved results. |
| E06 | Mark4 build and migration to X500 | Project-lead historical account, June–September | No original Mark4 flight dataset or comparative performance result in this snapshot. |
| E07 | 19 October flights and battery reuse across a reconnect | Project-lead report, 19 October | Later raw logs are not included in the historical CSV. No new aggregate numbers are inferred from the account. |
| E08 | Recomputed summary statistics | [Script](../analysis/summarize_segments.py), [results](../analysis/results.md), and [tests](../tests/test_summarize_segments.py) created 26 October | Tests validate the aggregation and input handling, not the underlying aircraft measurements. |

## Material reviewed but not presented as project results

The July screenshots supplied with the project are pages from HGLRC F460 6S V1 stack documentation, including HGLRCF405V2 firmware references. They are vendor reference material, not photographs of the assembled aircraft or evidence of the X500 configuration. They have not been republished as original team work.

The 10 October flight review contains proposed parameter changes. Those proposals are not supplied as an installable configuration because later changes and their verification are not captured here.

## Publication boundaries

The included CSV has no GPS coordinates, home positions, or personal identifiers. Before adding original logs, screenshots, or media, review their actual contents for private locations, identifiers, credentials, and third-party material. A file extension or `.gitignore` rule does not establish that a file is ready to publish.

Keep source filenames, configuration version, processing method, and limitations next to any exported result. Record synthetic and simulated data as such. Never silently replace a previous measurement with a target.
