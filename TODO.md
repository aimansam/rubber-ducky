# Rubber Ducky TODO

## Now

- [ ] Use `LAB-RUNBOOK.md` for the first Pi Pico validation session.
- [ ] Fill in the lab workstation, VM, test account, and allowed test window in `scope.md`.
- [ ] Record Pi Pico details: board type, firmware, USB device name, serial/hardware ID if visible.
- [ ] Follow `NEXT-MOVE.md` for the current phase plan.
- [ ] Prepare one owned lab machine with no sensitive apps open.
- [ ] Enable or identify logs for USB device insertion.
- [ ] Review `MODE-OPTIONS.md` and keep the Pico default on Mode 0 Safe Idle.
- [ ] Run Mode 0 Safe Idle and record whether the host sees the device.
- [ ] Run Mode 2 Device Logging Validation and record insertion/removal logs.
- [ ] Run Mode 1 Baseline Text Entry only after Mode 0 and Mode 2 are documented.
- [ ] Capture sanitized evidence screenshot and log snippets under `evidence/`.

## Next

- [ ] Document endpoint behavior in `testing-notes.md`.
- [ ] Add any observed risk to `findings.md`.
- [ ] Update `reports/report.md` with a short test summary.
- [ ] Update `blue-team/usb-hid-detection/detections.md` with observed log patterns.
- [ ] Decide whether a sanitized Discord alert is useful for this event.
- [ ] Compare detection options across Linux and Windows lab hosts.

## Later

- [ ] Build a small library of safe lab-only mode notes.
- [ ] Add restricted pentest mode details only after written authorization and exact scope exist.
- [ ] Add device-control policy testing.
- [ ] Add user-awareness reporting workflow notes.
- [ ] Write a sanitized blog draft after the lab results are documented.

## Recommendation

Next best move: complete `scope.md`, then run only Mode 0 and Mode 2. Do not run Mode 1 until you have confirmed where USB/HID events appear in logs.

## Blockers

- Scope must be completed before testing.
- Only owned or explicitly authorized systems are allowed.
- No credential collection, persistence, destructive actions, or data exfiltration.
- Restricted pentest modes require written authorization and exact host scope.
