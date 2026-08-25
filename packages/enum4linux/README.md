# enum4linux

> Linux alternative to enum.exe for enumerating data from Windows and Samba hosts.

## Installation

```bash
pkg install enum4linux
```

## Info

| Field | Value |
|-------|-------|
| Version | `0.9.1` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [enum4linux](https://github.com/CiscoCXSecurity/enum4linux) |

## Dependencies

`perl, dnsutils, samba, openldap, curl`

## Usage

```bash
enum4linux [options] <ip>
```

> Example: `enum4linux -a 192.168.1.10` performs a comprehensive enumeration of a Windows/Samba host.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```
