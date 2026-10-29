# Flight case study: the autonomous-flight baseline

**Platform:** X500 V2, Pixhawk 6C Mini, ArduCopter 4.7.1 as recorded in the October review.

## Method

The 10 October review examined DataFlash logs for arming, modes, mission progress, altitude, battery and vibration. Four armed logs produced the included 30-row CSV; an unarmed placeholder was excluded. Relative altitude above 2 m was used to infer airborne time.

The repository's Python tool aggregates that existing table. It does not reprocess the raw logs, which are not included.

## Findings and consequences

| Finding from the historical review | Engineering consequence |
| --- | --- |
| Airborne AUTO waypoint sequences on 7 and 9 October; two 9 October segments reached spline waypoint 6 and mission RTL 7 | Establishes programmed-flight progress as the integration baseline |
| A later 9 October segment reached 79.4 m relative altitude and stayed in AUTO until manual RTL | Define and verify the mission's terminal action |
| Primary-IMU Z-vibration peak of 33.3 m/s² during that segment; 11 clipping events in the final near-ground armed segment | Review mechanics/isolation and compare equivalent maneuvers; distinguish ground and flight events |
| No usable current / consumed-charge data in those older records | Collect calibrated measurements before claiming Wh consumption, endurance or energy-model accuracy |

These measurements describe historical tests, not recommended flight settings. The 30 armed intervals include ground activity; 16 have inferred airborne time. Neither their count nor summed duration establishes single-charge endurance.

## Next test

Capture a current parameter export, installed mass and battery condition. Reassess vibration after the mechanical inspection, validate voltage/current and verify configuration-specific recovery behavior before payload integration.

[Reproduced results](../../analysis/results.md) · [Data method and limits](../../data/README.md) · [Evidence sources](../evidence.md)

References: [ArduPilot AUTO mode](https://ardupilot.org/copter/docs/auto-mode.html) and [vibration measurement](https://ardupilot.org/copter/docs/common-measuring-vibration.html).
