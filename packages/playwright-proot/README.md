# playwright-proot

> Playwright CLI for Termux via proroot (Ubuntu 24.04). Enables browser automation (snapshot, screenshot, click, fill) for testing PWAs and web apps on Android.

## Overview

This package provides `playwright-proot` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://playwright.dev](https://playwright.dev)

## Installation

```bash
pkg update
pkg install playwright-proot
```

## Requirements

proroot, curl, tar

## Usage

```bash
playwright-proot run <commands>     Run commands in a single session
playwright-proot open [url]         Interactive session (headless Chromium on :9222)
playwright-proot close              Stop Chromium
playwright-proot help               Show help
```

Examples:

```bash
playwright-proot run "snapshot; screenshot --filename=p.png"
echo "goto http://localhost:8550; snapshot" | playwright-proot run
playwright-proot open http://localhost:8550
playwright-proot close
```

Runs in headless mode (no X11/Wayland required).

## Package details

| Field | Value |
|---|---|
| Package | `playwright-proot` |
| Version | `1.65.0-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://playwright.dev](https://playwright.dev) |
| Dependencies | proroot, curl, tar |

## Troubleshooting

```bash
pkg update
pkg install playwright-proot
```

Verify that the command is available with `command -v playwright-proot`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
