# zaproxy

> The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications.

## Overview

This package provides `zaproxy` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/zaproxy/zaproxy](https://github.com/zaproxy/zaproxy)

## Installation

```bash
pkg update
pkg install zaproxy
```

## Requirements

curl, openjdk-21

## Usage

```bash
zaproxy
```

`zaproxy` launches the OWASP Zed Attack Proxy desktop application. Use it only
against applications you own or have permission to test.

## Package details

| Field | Value |
|---|---|
| Package | `zaproxy` |
| Version | `2.17.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/zaproxy/zaproxy](https://github.com/zaproxy/zaproxy) |
| Dependencies | curl, openjdk-21 |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install zaproxy
```

Verify that the command is available with `command -v zaproxy`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
