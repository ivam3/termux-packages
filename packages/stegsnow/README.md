# stegsnow

> Steganography tool that conceals messages in ASCII text by appending whitespace to the ends of lines.

## Overview

This package provides `stegsnow` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://www.kali.org/tools/stegsnow](https://www.kali.org/tools/stegsnow)

## Installation

```bash
pkg update
pkg install stegsnow
```

## Requirements

curl, make, automake

## Usage

```bash
stegsnow --help
```

For the complete command reference, see the upstream documentation.

## Package details

| Field | Value |
|---|---|
| Package | `stegsnow` |
| Version | `20130616` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://www.kali.org/tools/stegsnow](https://www.kali.org/tools/stegsnow) |
| Dependencies | curl, make, automake |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install stegsnow
```

Verify that the command is available with `command -v stegsnow`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
