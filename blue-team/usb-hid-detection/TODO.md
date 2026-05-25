# USB HID Detection TODO

## Now

- [ ] Fill in the first lab host and OS in `../../scope.md`.
- [ ] Confirm which log source will be used first.
- [ ] Capture baseline logs before connecting the Pi Pico.
- [ ] Record Pi Pico insertion/removal timestamps from the red-team activity log.
- [ ] Search logs for new USB/HID device events.
- [ ] Save sanitized evidence under `../../evidence/`.

## Next

- [ ] Turn the observed log pattern into a detection note in `detections.md`.
- [ ] Validate the detection against Mode 2 Device Logging Validation.
- [ ] Add safe Discord alert notification testing with mock or sanitized lab events only.
- [ ] Update `../../reports/report.md` with the validation result.

## Later

- [ ] Compare Linux and Windows event visibility.
- [ ] Add device allowlist recommendations.
- [ ] Add tuning notes for legitimate keyboards, docks, KVMs, and accessibility devices.
- [ ] Link results back to the Rubber Ducky findings.

## Blockers

- Do not send raw logs or sensitive data to Discord.
- Do not use Discord as C2 or a data collection channel.
- Store webhook URLs outside Git.
