# nikto

> Nikto is an open source web server scanner that performs comprehensive tests against web servers for multiple items.

## Overview

This package provides `nikto` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/sullo/nikto](https://github.com/sullo/nikto)

## Installation

```bash
pkg update
pkg install nikto
```

## Requirements

git, perl

## Usage

```bash
nikto --help
```

For the complete command reference, see the upstream documentation.

## Package details

| Field | Value |
|---|---|
| Package | `nikto` |
| Version | `2.1.6` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/sullo/nikto](https://github.com/sullo/nikto) |
| Dependencies | git, perl |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install nikto
```

Verify that the command is available with `command -v nikto`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
