# Discord Alerting Plan

Purpose: send sanitized defensive notifications for USB HID detection events to a Discord channel.

This is a blue-team alerting workflow only. Do not use Discord for C2, implants, target data collection, credential collection, file transfer, persistence, exfiltration, or remote control.

## Allowed Alert Content

- Detection name.
- Sanitized lab host alias, such as `linux-lab-01`.
- Timestamp.
- Event category, such as `new-usb-hid-device`.
- Severity.
- Link or reference to local evidence stored in this project.
- Short analyst action, such as `review endpoint USB logs`.

## Do Not Send

- Raw logs.
- Tokens, cookies, API keys, passwords, or session values.
- Personal identifiers.
- Private IP addresses or hostnames unless approved and sanitized.
- Screenshots with sensitive data.
- Files collected from endpoints.
- Command output from target systems.

## Recommended Alert Format

```text
[USB HID Detection]
Severity: Medium
Host: linux-lab-01
Event: new-usb-hid-device
Time: YYYY-MM-DD HH:MM UTC
Action: Review endpoint USB logs.
Evidence: evidence/YYYYMMDD-usb-hid-validation-note.md
```

## Implementation Notes

- Store the Discord webhook URL in an environment variable or local `.env` file.
- Keep `.env` out of Git.
- Test with mock events before using real lab alerts.
- Redact before sending any notification outside the lab.

## Validation Checklist

- [ ] Webhook URL is not committed.
- [ ] Test alert uses mock data.
- [ ] Real alert uses sanitized lab data only.
- [ ] Alert does not include raw target output.
- [ ] Evidence remains local in this project repo.
