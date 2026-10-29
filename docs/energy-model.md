# Mission energy model

**Owners: Mohammed F and Jad. Status: planned; no fitted or flight-validated model is included yet.**

The model estimates how much battery energy a particular mission will use. It lets the system ask: **can this aircraft carry this package to this destination and complete its return or landing with a reserve?**

## How it works

1. **Measure:** collect calibrated battery voltage/current, timestamps, aircraft and payload mass, speed, mission phase and test conditions.
2. **Fit a simple baseline:** use measured average power by flight phase and load, or a small regression fitted within the tested range.
3. **Predict:** multiply each phase's expected power by its duration, then add the phases.
4. **Check:** compare the prediction, an uncertainty allowance and reserve against a conservative estimate of remaining usable battery energy.

Battery power is `P = V × I` in watts. Measured energy is approximately `sum(V × I × elapsed_seconds) / 3600` in watt-hours. ArduPilot's BAT log fields include voltage, current and consumed energy; availability and sensor calibration must be checked on the actual aircraft. [Log reference](https://ardupilot.org/copter/docs/logmessages.html#bat) · [Calibration reference](https://ardupilot.org/copter/docs/common-power-module-configuration-in-mission-planner.html)

## Mission budget

```text
required Wh = takeoff/climb
            + loaded outbound flight
            + placement/hover
            + return and landing
            + prediction uncertainty allowance
            + contingency reserve
```

The return estimate must match the outcome: normal release may allow an unloaded return, while failed release can require returning with the package. Evaluate the defined contingency instead of assuming the lighter return always happens.

**Illustration only:** a predicted mission of 35 Wh, a 5 Wh uncertainty allowance and a 10 Wh reserve requires 50 Wh. A remaining usable estimate of 55 Wh leaves 5 Wh of margin; 45 Wh fails the energy check. These are invented teaching numbers, not X500 results or recommended limits.

Passing this check is only one acceptance condition. Payload retention, mass/center-of-gravity limits, dimensions, navigation, route and operating conditions still have to pass.

## What the first model needs

| Input or result | Why it matters |
| --- | --- |
| Gross takeoff mass and package mass | Include the Jetson, mounts, wiring and retention hardware |
| Route distance, speed, climb and hover time | A short route can still consume more energy through longer hover or unfavorable conditions |
| Physical battery ID and usable-energy estimate | The label rating and voltage alone do not establish a mission budget |
| Configuration and environmental conditions | Predictions apply only within the measured operating range |
| Predicted versus measured Wh | Shows error, systematic bias and worst underprediction |

Measure at the battery boundary so propulsion, electronics and conversion losses are included. Do not add Jetson power a second time if it is already inside that measurement. Track battery usage across reconnects; unplugging a partially used pack does not recharge it.

## First deliverable

Mohammed F and Jad should first agree the measurement method and collect repeatable unloaded and secured-load data under an approved test plan. Publish a small dataset, a baseline notebook/script and an evaluation on **whole flights held out from fitting**. Adjacent samples from the same flight must not be split between training and validation.

Report absolute error, percentage error where meaningful, worst underprediction and the basis for the uncertainty allowance. Missing/stale battery data or conditions outside the tested range should produce a rejection or manual-review result.

The existing historical CSV lacks current/energy time series and payload mass. It cannot train or validate this model. ML is an option after a useful measured baseline exists.

**In one sentence:** Mohammed F and Jad build and validate the energy estimate; Ahmad integrates it into Jetson route decisions; Mohammed A supplies the package record.
