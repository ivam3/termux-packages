# enum4linux-ng

> A next generation version of enum4linux (a Windows/Samba enumeration tool) with additional features like JSON/YAML export.

## Installation

```bash
pkg install enum4linux-ng
```

## Info

| Field | Value |
|-------|-------|
| Version | `1.3.10` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [enum4linux-ng](https://github.com/cddmp/enum4linux-ng) |

## Dependencies

`python, python-pip, dnsutils, samba, openldap, curl`

## Usage

```bash
enum4linux-ng [options] <ip>
```

> Example: `enum4linux-ng -A 192.168.1.10` performs a comprehensive enumeration and `-oY out` exports results to YAML.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```
