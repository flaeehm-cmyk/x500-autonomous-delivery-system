# Case study: establishing the autonomous-flight baseline

**Platform:** Holybro X500 V2 ARF · Pixhawk 6C Mini · ArduCopter 4.7.1 as recorded in the October review.

**Engineering question:** What do the available logs demonstrate, and what must be resolved before payload integration?

## Evidence and method

An existing 10 October review examined DataFlash records for arming, mode changes, mission commands, altitude, battery voltage, vibration, navigation, and estimator status. Four armed log files produced the included 30-row CSV. A fifth placeholder log did not contain an armed session.

For this repository, the summary table was preserved and a new script aggregates it. Relative altitude greater than 2 m was the earlier extraction's airborne heuristic. Very low hover can therefore be excluded. The raw logs and original extraction code are not part of this package.

## Findings

| Observation | Interpretation |
| --- | --- |
| The review documents airborne AUTO waypoint sequences on 7 and 9 October. | Programmed autonomous flight is supported by the reviewed record. This is distinct from autonomous parcel delivery. |
| On 9 October, reported segments 7 and 9 reached spline waypoint 6 and entered mission RTL 7. | These specific sequences support mission-progress and return-command claims. |
| Segment 10 on 9 October reached the 80 m waypoint, with a recorded maximum relative altitude of 79.4 m, and remained in AUTO until manual RTL. | Terminal mission behavior needs explicit design and verification. The altitude is a historical measurement, not a recommended test height. |
| The review reports a 33.3 m/s² primary-IMU Z-vibration peak during that airborne segment, with no clipping in that segment. | A reason to inspect mechanics and isolation; insufficient evidence to choose PID gains or close the vibration issue. |
| The final near-ground armed segment accumulated 11 primary-IMU clipping events in the summary. | Segment-level context matters; a ground run should not be presented as an airborne event. |
| The older logs lacked usable current / consumed-charge data according to the review. | These records cannot establish Wh use, usable pack capacity, energy-model accuracy, or delivery range. |

ArduPilot explains that excessive vibration can degrade state estimation and position/altitude-dependent modes. Its guidance places roughly 30 m/s² as a useful review threshold, not a stand-alone vehicle acceptance criterion. [Measurement guidance](https://ardupilot.org/copter/docs/common-measuring-vibration.html)

## Design consequences

1. Include an intentional terminal action in the approved mission and verify the uploaded mission contents.
2. Review props, motor/arm security, flight-controller isolation, and cable contact before attributing all shaking to gains.
3. Calibrate and validate voltage/current before building the energy dataset.
4. Associate failsafe tests with the exact parameter export used for that test. Earlier successful flights do not prove later parameter changes.
5. Close the unloaded-flight baseline before adding payload hardware.

ArduPilot's [AUTO documentation](https://ardupilot.org/copter/docs/auto-mode.html) describes onboard mission execution and the need for satisfactory underlying altitude and position control.

## Reproduce and extend

Run `python analysis/summarize_segments.py` from the root. The [generated report](../../analysis/results.md) groups intervals by source date and preserves caveats around mode sets and armed-period extrema.

The next evidence package should include a reviewed, shareable extraction from new logs; its processing code; the corresponding configuration; measured mass and battery condition; and a short flight clip. Compare like-for-like maneuvers rather than assuming a later calendar date means lower vibration.

**Conclusion:** the records establish a waypoint-flight foundation and specific unresolved integration questions. They do not yet establish a tuned payload aircraft, verified failsafe matrix, or delivery system.
