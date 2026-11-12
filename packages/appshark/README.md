# appshark

> AppShark is a static taint analysis platform to scan vulnerabilities in Android apps.

## Overview

This package provides `appshark` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/bytedance/appshark](https://github.com/bytedance/appshark)

## Installation

```bash
pkg update
pkg install appshark
```

## Requirements

openjdk-21, git

## Usage

```bash
appshark-installer
```

> Run the installer first, then use `appshark [options]` to perform static taint analysis on Android APKs.

## Package details

| Field | Value |
|---|---|
| Package | `appshark` |
| Version | `0.1.2` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/bytedance/appshark](https://github.com/bytedance/appshark) |
| Dependencies | openjdk-21, git |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install appshark
```

Verify that the command is available with `command -v appshark`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
