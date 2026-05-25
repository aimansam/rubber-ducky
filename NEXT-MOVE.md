# Next Move Plan

This plan keeps the Pi Pico project moving without building C2, implants, credential collection, persistence, exfiltration, or destructive behavior.

## Current Objective

Validate USB HID risk safely with a Raspberry Pi Pico, then prove whether blue-team tooling can see and alert on the activity.

## Phase 1: Scope and Lab Readiness

- [ ] Fill in `scope.md` with the exact owned lab host or VM.
- [ ] Record Pi Pico details: board model, firmware, visible USB device name, and serial/hardware ID if available.
- [ ] Confirm the lab host has no sensitive apps, secrets, or personal data open.
- [ ] Decide which OS to test first: Linux lab host or Windows lab VM.
- [ ] Confirm where USB/HID logs will be collected.
- [ ] Keep the Pico default mode set to `0` Safe Idle.

## Phase 2: Safe Red-Team Validation

- [ ] Run Mode 0: Safe Idle.
- [ ] Run Mode 2: Device Logging Validation.
- [ ] Run Mode 1: Baseline Text Entry into an already-open editor.
- [ ] Capture insertion/removal timestamps.
- [ ] Store sanitized screenshots and log snippets under `evidence/`.
- [ ] Update `testing-notes.md` with what happened.

## Phase 3: Blue-Team Detection

- [ ] Update the USB HID Detection project with the exact log source used.
- [ ] Search for USB insertion, HID registration, and driver events.
- [ ] Document whether the Pi Pico was visible in logs.
- [ ] Create a detection note for new HID device insertion.
- [ ] Validate whether an alert could trigger from the event.

## Phase 4: Safe Discord Notification

- [ ] Use Discord only for defensive alert notifications from the blue-team project.
- [ ] Send sanitized alert summaries only, such as event type, lab host alias, timestamp, and detection name.
- [ ] Do not send raw logs, secrets, usernames, private IPs, tokens, cookies, files, screenshots with sensitive data, or target data.
- [ ] Store webhook URLs outside Git in environment variables or a local `.env` file that is ignored.

## Phase 5: Reporting

- [ ] Update `findings.md` with the risk observed.
- [ ] Update `reports/report.md` with test results and recommendations.
- [ ] Add blue-team results from the USB HID Detection project.
- [ ] Decide whether the result is suitable for a sanitized blog draft.

## Recommendation

Do the first live lab run in this order: Mode 0, Mode 2, Mode 1. After those three work, continue in the blue-team project and build a sanitized Discord alert bridge for notifications only.
