# hashid

> A python script to identify the different types of hashes used to encrypt data and especially passwords.

## Overview

This package provides `hashid` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://gitlab.com/kalilinux/packages/hash-identifier](https://gitlab.com/kalilinux/packages/hash-identifier)

## Installation

```bash
pkg update
pkg install hashid
```

## Requirements

curl, python

## Usage

```bash
hashid --help
```

For the complete command reference, see the upstream documentation.

## Package details

| Field | Value |
|---|---|
| Package | `hashid` |
| Version | `1.2` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://gitlab.com/kalilinux/packages/hash-identifier](https://gitlab.com/kalilinux/packages/hash-identifier) |
| Dependencies | curl, python |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install hashid
```

Verify that the command is available with `command -v hashid`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
