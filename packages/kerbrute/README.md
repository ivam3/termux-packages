# kerbrute

> A fast Kerberos pre-auth bruteforcing tool for enumerating valid Active Directory users and spraying passwords.

## Overview

This package provides `kerbrute` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/ropnop/kerbrute](https://github.com/ropnop/kerbrute)

## Installation

```bash
pkg update
pkg install kerbrute
```

## Requirements

go, git, make

## Usage

```bash
kerbrute userenum --domain <domain> users.txt
```

## Package details

| Field | Value |
|---|---|
| Package | `kerbrute` |
| Version | `10.03.2023` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/ropnop/kerbrute](https://github.com/ropnop/kerbrute) |
| Dependencies | go, git, make |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install kerbrute
```

Verify that the command is available with `command -v kerbrute`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
