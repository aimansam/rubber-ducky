#!/usr/bin/env python3
"""Monitor local Linux USB HID device changes and optionally send sanitized alerts.

This script is for owned lab desktops only. It watches Linux sysfs for USB HID
devices, prints insertion/removal events, and can send sanitized Discord
notifications using a webhook stored outside Git.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path


USB_SYSFS = Path("/sys/bus/usb/devices")
HID_CLASS = "03"


@dataclass(frozen=True)
class HidDevice:
    sysfs_name: str
    vendor_id: str
    product_id: str
    manufacturer: str
    product: str

    @property
    def key(self) -> str:
        return f"{self.sysfs_name}:{self.vendor_id}:{self.product_id}:{self.manufacturer}:{self.product}"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def read_text(path: Path, default: str = "unknown") -> str:
    try:
        value = path.read_text(encoding="utf-8", errors="replace").strip()
    except OSError:
        return default
    return value or default


def is_usb_hid_device(device_path: Path) -> bool:
    if read_text(device_path / "bDeviceClass", "") == HID_CLASS:
        return True

    for interface_path in device_path.glob(f"{device_path.name}:*"):
        if read_text(interface_path / "bInterfaceClass", "") == HID_CLASS:
            return True

    return False


def list_hid_devices() -> dict[str, HidDevice]:
    devices: dict[str, HidDevice] = {}

    if not USB_SYSFS.exists():
        return devices

    for device_path in USB_SYSFS.iterdir():
        if not (device_path / "idVendor").exists() or not (device_path / "idProduct").exists():
            continue
        if not is_usb_hid_device(device_path):
            continue

        device = HidDevice(
            sysfs_name=device_path.name,
            vendor_id=read_text(device_path / "idVendor"),
            product_id=read_text(device_path / "idProduct"),
            manufacturer=read_text(device_path / "manufacturer"),
            product=read_text(device_path / "product"),
        )
        devices[device.key] = device

    return devices


def format_console_event(event_type: str, host_alias: str, device: HidDevice) -> str:
    details = asdict(device)
    return json.dumps(
        {
            "time": utc_now(),
            "host": host_alias,
            "event": event_type,
            "category": "usb-hid-device",
            "device": details,
        },
        sort_keys=True,
    )


def format_discord_message(event_type: str, host_alias: str, device: HidDevice) -> str:
    return "\n".join(
        [
            "[USB HID Detection]",
            "Severity: Medium",
            f"Host: {host_alias}",
            f"Event: {event_type}",
            f"Time: {utc_now()}",
            f"Device: {device.manufacturer} {device.product} ({device.vendor_id}:{device.product_id})",
            "Action: Review local endpoint USB logs.",
        ]
    )


def send_discord_alert(webhook_url: str, message: str) -> None:
    payload = json.dumps({"content": message}).encode("utf-8")
    request = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            if response.status >= 300:
                print(f"Discord alert returned HTTP {response.status}", file=sys.stderr)
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"Discord alert failed: {error}", file=sys.stderr)


def emit_event(event_type: str, host_alias: str, device: HidDevice, webhook_url: str | None) -> None:
    print(format_console_event(event_type, host_alias, device), flush=True)
    if webhook_url:
        send_discord_alert(webhook_url, format_discord_message(event_type, host_alias, device))


def monitor(interval: float, host_alias: str, webhook_url: str | None, once: bool) -> None:
    previous = list_hid_devices()

    print(f"[{utc_now()}] Monitoring USB HID devices on {host_alias}", flush=True)
    print(f"[{utc_now()}] Initial HID device count: {len(previous)}", flush=True)

    if once:
        for device in previous.values():
            print(format_console_event("current-usb-hid-device", host_alias, device), flush=True)
        return

    while True:
        time.sleep(interval)
        current = list_hid_devices()

        for key, device in current.items():
            if key not in previous:
                emit_event("new-usb-hid-device", host_alias, device, webhook_url)

        for key, device in previous.items():
            if key not in current:
                emit_event("removed-usb-hid-device", host_alias, device, webhook_url)

        previous = current


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Monitor local Linux USB HID device changes for an owned lab desktop."
    )
    parser.add_argument("--host-alias", default="linux-lab-01", help="Sanitized host name for logs and alerts.")
    parser.add_argument("--interval", type=float, default=2.0, help="Polling interval in seconds.")
    parser.add_argument("--once", action="store_true", help="Print current HID devices and exit.")
    parser.add_argument(
        "--discord",
        action="store_true",
        help="Send sanitized alerts to DISCORD_WEBHOOK_URL from the environment.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL") if args.discord else None

    if args.discord and not webhook_url:
        print("--discord requires DISCORD_WEBHOOK_URL to be set outside Git.", file=sys.stderr)
        return 2

    if not USB_SYSFS.exists():
        print("Linux USB sysfs path not found. This monitor is Linux-only.", file=sys.stderr)
        return 1

    monitor(args.interval, args.host_alias, webhook_url, args.once)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())