# Scripts

## `desktop_usb_hid_monitor.py`

Monitors your own Linux desktop for USB HID device insertion/removal events. It is intended for the Pi Pico lab and does not execute payloads, collect target data, or control any host.

Run a one-time inventory:

```bash
python3 scripts/desktop_usb_hid_monitor.py --once --host-alias kali-desktop
```

Monitor continuously:

```bash
python3 scripts/desktop_usb_hid_monitor.py --host-alias kali-desktop
```

Send sanitized Discord notifications:

```bash
export DISCORD_WEBHOOK_URL='https://discord.com/api/webhooks/...'
python3 scripts/desktop_usb_hid_monitor.py --host-alias kali-desktop --discord
```

Do not commit `.env` files, webhook URLs, raw logs, secrets, personal data, or screenshots with sensitive information.