# polenum

> Polenum extracts the password policy information from a Windows machine. Uses the Impacket library.

## Overview

This package provides `polenum` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/Wh1t3Fox/polenum](https://github.com/Wh1t3Fox/polenum)

## Installation

```bash
pkg update
pkg install polenum
```

## Requirements

python, python-pip, curl

## Usage

```bash
polenum [options]
```

Extracts the password policy from a Windows machine using the Impacket library:

```bash
polenum -u <username> -p <password> -d <domain/ip>
polenum user:password@127.0.0.1
```

The script is installed at `~/.local/share/polenum/polenum.py`, and `impacket` is installed with pip.

## Package details

| Field | Value |
|---|---|
| Package | `polenum` |
| Version | `2025.03.01` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/Wh1t3Fox/polenum](https://github.com/Wh1t3Fox/polenum) |
| Dependencies | python, python-pip, curl |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install polenum
```

Verify that the command is available with `command -v polenum`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
