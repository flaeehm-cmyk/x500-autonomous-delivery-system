# Evidence register

Updated 28 October 2026. **Included** means the artifact is in this repository; **reported** means a team account; **planned** means design work.

| Claim / material | Basis | Limit |
| --- | --- | --- |
| AUTO waypoint sequences on 7 and 9 October | Historical `X500_Flight_Log_Review_2026-10-10.pdf`; findings summarized in the [flight case study](case-studies/flight-validation.md) | Derived AI-assisted review; raw logs and original review PDF are not packaged here |
| 30 armed intervals from four source logs | [Included CSV](../data/flight_segment_summary_2026-10-10.csv), transcribed from the 10 October summary | Original log-to-CSV extractor is not included; altitude heuristic and field limits are in the [data guide](../data/README.md) |
| Reproducible summary and 10 tests | Included [script](../analysis/summarize_segments.py), [results](../analysis/results.md) and [tests](../tests/test_summarize_segments.py) | Tests cover aggregation/input handling, not aircraft measurements |
| 16.68 V agreement between Mission Planner and meter | Mohammed F's report, 19 October | Single comparison; not current calibration or measured battery capacity |
| Jetson / NVMe setup and three successful subsequent boots | Mohammed F's report, through 25 October | Console records and actual OS version remain to be added |
| Mark4 space constraint, X500 migration and former tracking scope | Project-lead retrospective, clarified 28 October | Design history; no comparative platform benchmark or demonstrated tracking result |
| Delivery scope and current ownership | 17 October scope document plus Mohammed F's 28 October clarification | Responsibilities and planned behavior, not completed subsystem results |
| Temporary custom Jetson supply, replacement power PCB and delivery subsystems | 28 October team update | Work in development; no qualification record or integrated delivery result included |

The source files named above but not linked are historical project records, not repository downloads. Vendor-manual screenshots are reference material, not photographs or evidence of the team's assembled aircraft.

For new results, include the configuration, method, units, source/processing details and a shareable artifact. Keep private location/identity data out of public exports and mark synthetic or simulated data clearly.

[History](engineering-log.md) · [Attribution](../ATTRIBUTION.md)
