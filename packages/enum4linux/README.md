# enum4linux

> Linux alternative to enum.exe for enumerating data from Windows and Samba hosts.

## Overview

This package provides `enum4linux` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/CiscoCXSecurity/enum4linux](https://github.com/CiscoCXSecurity/enum4linux)

## Installation

```bash
pkg update
pkg install enum4linux
```

## Requirements

perl, dnsutils, samba, openldap, curl

## Usage

```bash
enum4linux [options] <ip>
```

> Example: `enum4linux -a 192.168.1.10` performs a comprehensive enumeration of a Windows/Samba host.

## Package details

| Field | Value |
|---|---|
| Package | `enum4linux` |
| Version | `0.9.1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/CiscoCXSecurity/enum4linux](https://github.com/CiscoCXSecurity/enum4linux) |
| Dependencies | perl, dnsutils, samba, openldap, curl |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install enum4linux
```

Verify that the command is available with `command -v enum4linux`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
