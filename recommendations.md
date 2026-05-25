# Recommendations

## Pi Pico Project Setup

- Use the Pi Pico only as a lab HID test device until written authorization exists for any other target.
- Label the device physically so it is not mistaken for an unknown USB drive.
- Keep payload notes small, readable, and reviewed before each run.
- Start with text-only validation in an already-open editor before testing anything more advanced.
- Keep raw evidence local and sanitize screenshots before blog or report use.

## Red-Team Workflow

- Complete `scope.md` first, then run the baseline test.
- Treat each payload as a change-controlled artifact: purpose, expected behavior, risk, cleanup.
- Log the exact insertion time so blue-team logs are easier to correlate.
- Avoid tests that depend on speed, stealth, credential prompts, network calls, or system changes until the lab has monitoring and rollback in place.

## Blue-Team Workflow

- Create a companion project named `USB HID Detection` under `project/blue-team/`.
- Collect endpoint logs before, during, and after Pi Pico insertion.
- Track device identifiers, driver events, and user-session activity.
- Tune for high-confidence events first: new keyboard device on sensitive endpoint, repeated device insertion, and unexpected HID device during locked or unattended sessions.

## Defensive Controls to Evaluate

- USB device-control policy.
- Endpoint detection and response visibility for new HID devices.
- Workstation auto-lock behavior.
- User reporting process for unknown devices.
- Physical security controls around exposed workstations.

## Suggested Next Command

From the workspace root, create a blue-team companion repo after creating the GitHub repository:

```bash
./scripts/create-blue-team-project.sh "USB HID Detection" https://github.com/aimansam/usb-hid-detection.git
```
