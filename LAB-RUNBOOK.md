# Lab Runbook

Use this runbook for the first authorized Pi Pico HID validation session.

## Goal

Confirm that an owned lab host can observe a Pi Pico acting as a USB HID device, then document what the red-team action produced and what the blue-team side detected.

## Before You Plug In The Pico

- [ ] Confirm the target is owned or explicitly authorized.
- [ ] Fill in `scope.md` with host, OS, test account, and test window.
- [ ] Close sensitive apps and remove secrets from the desktop/session.
- [ ] Open a plain text editor manually if running Mode 1.
- [ ] Start or identify endpoint logs for USB/HID events.
- [ ] Keep the Pico mode at `0` Safe Idle until ready.

## First Run Order

1. Mode 0: Safe Idle.
2. Mode 2: Device Logging Validation.
3. Mode 1: Baseline Text Entry.

Do not skip Mode 0. It confirms the device can be connected without action.

## Evidence To Record

| Item | Where To Record |
| --- | --- |
| Lab host alias and OS | `scope.md` |
| Pico board/firmware details | `scope.md` |
| Insertion/removal timestamps | `testing-notes.md` |
| Mode selected | `testing-notes.md` |
| Endpoint log source | `blue-team/usb-hid-detection/TODO.md` |
| Detection result | `blue-team/usb-hid-detection/detections.md` |
| Sanitized screenshots/log snippets | `evidence/` |
| Summary and recommendation | `reports/report.md` |

## Blue-Team Checks

- [ ] Did the host log new USB device insertion?
- [ ] Did logs identify keyboard/HID behavior?
- [ ] Is the device name, vendor, product, or serial visible?
- [ ] Can the event be searched reliably?
- [ ] Would this event be worth a Discord notification after sanitization?

## Discord Alert Rule

Discord is only for sanitized defensive notifications. Do not send raw logs, secrets, personal identifiers, target output, files, or screenshots with sensitive data.

Use this safe format:

```text
[USB HID Detection]
Severity: Medium
Host: linux-lab-01
Event: new-usb-hid-device
Time: YYYY-MM-DD HH:MM UTC
Action: Review endpoint USB logs.
```

## Stop Conditions

- Scope is incomplete or unclear.
- The host is not owned or authorized.
- The selected mode would collect data, change settings, persist, bypass controls, or execute unapproved actions.
- Logs show unexpected behavior.
- Sensitive data appears in evidence.

## After The Run

- [ ] Update `testing-notes.md`.
- [ ] Update `findings.md` if there is an observed risk.
- [ ] Update `blue-team/usb-hid-detection/detections.md`.
- [ ] Update `reports/report.md`.
- [ ] Sanitize evidence before sharing or blogging.
