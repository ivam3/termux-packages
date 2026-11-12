# getadusers

> This script will gather data about the domain's users and their corresponding email addresses.

## Overview

This package provides `getadusers` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/fortra/impacket/blob/master/examples/GetADUsers.py](https://github.com/fortra/impacket/blob/master/examples/GetADUsers.py)
- **Website:** [https://github.com/SecureAuthCorp/impacket](https://github.com/SecureAuthCorp/impacket)

## Installation

```bash
pkg update
pkg install getadusers
```

## Requirements

python, python-pip, curl, rust

## Usage

```bash
getadusers -dc-ip <dc-ip> domain/user:pass
```

## Package details

| Field | Value |
|---|---|
| Package | `getadusers` |
| Version | `0.11.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/fortra/impacket/blob/master/examples/GetADUsers.py](https://github.com/fortra/impacket/blob/master/examples/GetADUsers.py) |
| Website | [https://github.com/SecureAuthCorp/impacket](https://github.com/SecureAuthCorp/impacket) |
| Dependencies | python, python-pip, curl, rust |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install getadusers
```

Verify that the command is available with `command -v getadusers`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
