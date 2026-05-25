# Mode 00: Safe Idle

## Purpose

Confirm the Pi Pico can connect to an owned lab host without performing keyboard actions.

## Expected Behavior

- No keystrokes.
- No command execution.
- No file, network, or clipboard access.
- Endpoint may log device insertion.

## Evidence

- Device insertion timestamp.
- Endpoint USB/HID log if available.
