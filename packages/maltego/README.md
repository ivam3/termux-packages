# maltego

> Maltego is a software focused mainly on forensic analysis and developed to make link analysis and data mining more conducive from IP domains, emails, telephones, geographic locations... that is, the starting point of an investigation.

## Overview

This package provides `maltego` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://www.maltego.com](https://www.maltego.com)

## Installation

```bash
pkg update
pkg install maltego
```

## Requirements

openjdk-21, curl, findutils

## Usage

```bash
maltego --help
```

For the complete command reference, see the upstream documentation.

## Package details

| Field | Value |
|---|---|
| Package | `maltego` |
| Version | `4.7.0-1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://www.maltego.com](https://www.maltego.com) |
| Dependencies | openjdk-21, curl, findutils |
| Suggests | i-haklab, xwayland |

## Troubleshooting

```bash
pkg update
pkg install maltego
```

Verify that the command is available with `command -v maltego`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
