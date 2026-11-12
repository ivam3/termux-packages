# enum4linux-ng

> A next generation version of enum4linux (a Windows/Samba enumeration tool) with additional features like JSON/YAML export.

## Overview

This package provides `enum4linux-ng` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/cddmp/enum4linux-ng](https://github.com/cddmp/enum4linux-ng)

## Installation

```bash
pkg update
pkg install enum4linux-ng
```

## Requirements

python, python-pip, dnsutils, samba, openldap, curl

## Usage

```bash
enum4linux-ng [options] <ip>
```

> Example: `enum4linux-ng -A 192.168.1.10` performs a comprehensive enumeration and `-oY out` exports results to YAML.

## Package details

| Field | Value |
|---|---|
| Package | `enum4linux-ng` |
| Version | `1.3.10` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/cddmp/enum4linux-ng](https://github.com/cddmp/enum4linux-ng) |
| Dependencies | python, python-pip, dnsutils, samba, openldap, curl |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install enum4linux-ng
```

Verify that the command is available with `command -v enum4linux-ng`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
