# Pi Pico Mode Options

Purpose: define selectable Pi Pico Rubber Ducky lab modes for authorized, non-destructive HID validation.

Use these as project modes, not as production payloads. Every mode must be reviewed against `scope.md` before testing.

## Mode Table

| Mode | Name | Purpose | Risk | Status |
| --- | --- | --- | --- | --- |
| 0 | Safe Idle | Device connects but performs no keyboard action. | Low | Recommended default |
| 1 | Baseline Text Entry | Types a harmless lab message into an already-open text editor. | Low | First test |
| 2 | Device Logging Validation | Connects as HID so blue-team logs can capture insertion and removal. | Low | Good for SIEM testing |
| 3 | User Awareness Demo | Types a short awareness message into an already-open editor for training. | Low | Lab/training only |
| 4 | Timing/Rate Test | Types the same harmless message at different speeds to compare logging and detection. | Medium | Only after Mode 1 succeeds |
| 5 | Restricted Pentest Validation | Approval-gated mode for authorized engagement testing and control validation. | High | Written approval required |
| 6 | Restricted Detection Trigger | Approval-gated mode to validate whether defensive tooling catches explicitly approved HID behavior. | High | Written approval required |
| 9 | Locked/Blocked | Reserved for disallowed behavior. | High | Do not implement |

## Mode 0: Safe Idle

Goal: confirm the Pico can connect without performing actions.

Expected behavior:

- No keystrokes.
- No command execution.
- No file access.
- Endpoint may log USB device insertion.

Use this as the default mode when the device is not actively being tested.

## Mode 1: Baseline Text Entry

Goal: prove HID input risk safely.

Expected behavior:

- Operator manually opens a text editor.
- Pico types the approved lab message only.
- No shortcuts, shell commands, browser actions, downloads, or settings changes.

Approved message:

```text
Rubber Ducky lab test - authorized local HID validation.
```

## Mode 2: Device Logging Validation

Goal: help blue-team validate logs and alerts for new HID devices.

Expected behavior:

- Device connects and remains idle.
- Operator records insertion and removal time.
- Blue-team project checks endpoint/SIEM logs.

## Mode 3: User Awareness Demo

Goal: demonstrate why unknown USB devices are risky without doing anything harmful.

Expected behavior:

- Operator manually opens a text editor or training slide.
- Pico types a short awareness message.
- No commands are executed.

Example message:

```text
Training demo: unknown USB devices can act like keyboards. Report unknown devices.
```

## Mode 4: Timing/Rate Test

Goal: compare whether defensive tooling can notice very fast typing behavior after HID insertion.

Expected behavior:

- Same harmless text as Mode 1.
- Different delays between keystrokes.
- No command execution or system changes.

Only run this after the baseline mode is documented and detection logging is ready.

## Mode 5: Restricted Pentest Validation

Goal: reserve a mode for actual authorized pentest work where the rules of engagement explicitly allow HID-based validation beyond harmless typing.

This mode is a planning placeholder, not a payload. Do not add executable steps here until the engagement scope, test window, target list, and client approval are documented.

Required approval details:

- Written authorization allows USB HID testing.
- Approved target hosts are listed in `scope.md`.
- Test window is defined.
- Expected behavior is reviewed before execution.
- Blue team, client contact, or emergency contact is known.
- Rollback and cleanup are documented.

Allowed examples, only if explicitly approved:

- Non-destructive command-execution validation.
- Endpoint control prompt/alert validation.
- Application focus and input-handling validation.
- Detection and response workflow validation.

Still disallowed here:

- Credential theft or phishing prompts.
- Persistence.
- Data exfiltration.
- Destructive actions.
- Security-tool bypass.
- Stealth or evasion behavior.
- Running on systems outside the approved scope.

## Mode 6: Restricted Detection Trigger

Goal: trigger approved blue-team detections in a controlled pentest or purple-team exercise.

This mode should exist only to validate monitoring, alerting, and response. It should not collect sensitive data or modify the target system unless the rules of engagement explicitly allow that behavior.

Required evidence:

- Exact insertion time.
- Exact selected mode.
- Target hostname or approved asset ID.
- Expected detection name.
- SIEM/EDR alert screenshot or query result.
- Cleanup confirmation.

Use this mode only after Mode 2 Device Logging Validation works reliably.

## Mode 9: Locked/Blocked

Do not implement modes that perform credential theft, persistence, stealth, destructive actions, data exfiltration, endpoint-control bypass, or unauthorized command execution.

If a mode idea falls into this category, document it as out of scope in `findings.md` or `scope.md` instead of building it.

## Mode Selection Design

Recommended safe design:

- Default to Mode 0 Safe Idle.
- Store the selected mode in a simple local config file on the Pico, such as `mode.txt`.
- Require physical access to change modes.
- Use an LED blink pattern or serial output to show the selected mode before any HID action.
- Add a short arming delay so the operator can unplug the device before execution.
- Keep a printed or local copy of this mode table during testing.

## Pre-Run Checklist

- [ ] Scope allows USB HID testing.
- [ ] Target is owned or explicitly authorized.
- [ ] Selected mode is listed in this file.
- [ ] Mode does not collect secrets, personal data, or out-of-scope information.
- [ ] Command execution, if any, is explicitly authorized and non-destructive.
- [ ] Blue-team logging is started if needed.
- [ ] Operator is ready to record exact insertion/removal time.

## Restricted Mode Approval Checklist

Complete this before Mode 5 or Mode 6:

- [ ] Written authorization explicitly allows USB HID testing.
- [ ] Scope names the exact hosts where the mode may run.
- [ ] Test window is approved.
- [ ] Expected behavior has been reviewed by the operator and engagement owner.
- [ ] Emergency stop contact is known.
- [ ] Cleanup plan is documented.
- [ ] Evidence handling and redaction rules are understood.
