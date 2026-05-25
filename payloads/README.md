# Payloads

Use this folder for authorized lab-only HID payload notes.

Start with harmless payloads that demonstrate keyboard injection risk without running commands, collecting data, changing settings, or creating persistence.

## Safe Baseline Payload Behavior

- Types a short lab message into an already-open text editor.
- Does not open terminals, browsers, settings, or system tools.
- Does not access files, credentials, network resources, or clipboard data.
- Does not disable controls or alter configuration.

## Mode Options

Use `../MODE-OPTIONS.md` as the source of truth for Pi Pico modes.

Start with:

- Mode 0: Safe Idle
- Mode 1: Baseline Text Entry
- Mode 2: Device Logging Validation

Restricted pentest modes:

- Mode 5: Restricted Pentest Validation
- Mode 6: Restricted Detection Trigger

Modes 5 and 6 require written authorization, exact target scope, a test window, cleanup notes, and evidence-handling rules before use.

Keep `mode.txt.example` as a simple model for choosing a default safe mode. The default should be `0` until scope and lab readiness are complete.

## Payload Review Checklist

- [ ] Scope allows USB HID testing.
- [ ] Target is owned or explicitly authorized.
- [ ] Payload has been reviewed before execution.
- [ ] Payload does not collect secrets or personal data.
- [ ] Payload does not persist or change system settings.
- [ ] Any command execution is explicitly authorized, non-destructive, and limited to approved hosts.
- [ ] Cleanup and evidence handling are documented.
