# Detections

## New USB HID Keyboard Connected

Objective: alert or record when a new keyboard-class USB HID device is connected to a monitored endpoint.

Data sources:

- Endpoint USB/device logs.
- EDR device-control logs.
- SIEM-normalized endpoint events.

Logic:

- Look for device insertion events where device class or driver indicates keyboard/HID behavior.
- Prioritize events where the device has not been seen on that host before.
- Correlate with the red-team insertion timestamp.

Severity: medium for sensitive endpoints; informational for general lab hosts until tuned.

Known false positives:

- New legitimate keyboards.
- Docking stations or KVM devices.
- Replaced peripherals.
- Accessibility devices.

Tuning notes:

- Maintain an allowlist of approved keyboards for sensitive systems.
- Correlate with user presence, screen lock state, and physical access logs where available.

## Rapid Keystroke Pattern After Device Insertion

Objective: identify suspicious keyboard behavior shortly after a new HID device appears.

Data sources:

- EDR telemetry.
- Endpoint control tooling.
- SIEM correlation of HID insertion plus suspicious follow-on behavior.

Logic:

- Look for a new HID device followed by unusual bursts of input or suspicious process activity within a short time window.
- Avoid collecting actual keystroke content; focus on metadata and follow-on behavior.

Severity: medium to high if correlated with command execution, scripting tools, credential prompts, or administrative consoles.

Known false positives:

- Power users using macros.
- Barcode scanners.
- Accessibility tooling.

Tuning notes:

- Start with lab-only validation.
- Tune after Mode 2 and Mode 1 results are documented.
