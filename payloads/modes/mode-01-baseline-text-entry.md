# Mode 01: Baseline Text Entry

## Purpose

Safely demonstrate USB HID keyboard injection risk in an owned lab environment.

## Expected Behavior

- Operator manually opens a text editor.
- Pi Pico types only the approved lab message.
- No commands, shortcuts, downloads, credential prompts, or settings changes.

## Approved Message

```text
Rubber Ducky lab test - authorized local HID validation.
```

## Evidence

- Screenshot of typed message.
- Exact insertion time.
- Endpoint USB/HID logs.
