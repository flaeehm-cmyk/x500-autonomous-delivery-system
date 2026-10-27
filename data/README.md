# Flight-summary dataset

[`flight_segment_summary_2026-10-10.csv`](flight_segment_summary_2026-10-10.csv) preserves all 30 data rows and original column names from the project file `x500_flight_segment_summary.csv`, generated 10 October 2026. The table was recovered from that file's text extraction; it is a data transcription, not a byte-for-byte archival copy.

The earlier extraction grouped armed intervals and inferred airborne time from CTUN relative altitude above 2 m. Four armed source logs are represented: two on 18 September, one on 7 October, and one on 9 October. A separate unarmed placeholder log is absent from this table.

## Columns

| Field | Meaning / unit |
| --- | --- |
| `index` | Original zero-based row index |
| `file` | Source DataFlash log filename; its date is used for grouping |
| `flight` | Armed-interval identifier within that file, not necessarily an actual flight |
| `armed_s` | Armed duration, seconds |
| `airborne_s` | Time classified above 2 m by the earlier extraction, seconds |
| `max_alt_m` | Maximum recorded relative altitude, metres; near-ground values can be negative |
| `modes` | Slash-separated mode IDs observed during the armed interval |
| `min_voltage` | Minimum recorded pack voltage in the summarized interval, volts |
| `max_vib_xyz` | Summary maximum across vibration axes, m/s² |
| `clip_0_delta` | Primary-IMU clipping-counter increase over the interval |

Modes relevant here: 2 = AltHold, 3 = AUTO, 4 = GUIDED, 5 = LOITER, 6 = RTL. The analysis only uses exact mode token `3` to flag AUTO in an interval's mode set. The underlying mode definitions are in [ArduPilot's Copter source](https://github.com/ArduPilot/ardupilot/blob/master/ArduCopter/mode.h).

## Interpretation limits

- A mode appearing in an interval does not give the time spent in that mode or prove waypoint completion.
- A zero `airborne_s` can include very low hover; it is not conclusive proof the aircraft never left the ground.
- Voltage and vibration extrema may include takeoff, landing, and other ground/armed time.
- Summed airborne time across intervals and dates is not single-charge endurance.
- The table has no current or energy time series, payload masses, weather record, calibrated position errors, or battery-health characterization.
- No raw coordinates are present. Original DataFlash logs are not included.
- The precise earlier extractor is unavailable here. Treat its altitude/vibration summaries as derived records.

See the [evidence register](../docs/evidence.md) and [generated report](../analysis/results.md).
