# apktool

> A tool for reverse engineering Android apk files.

## Overview

This package provides `apktool` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool)
- **Website:** [https://apktool.org/](https://apktool.org/)

## Installation

```bash
pkg update
pkg install apktool
```

## Requirements

openjdk-21, aapt, wget

## Usage

```bash
apktool --help
```

For the complete command reference, see the upstream documentation.

## Package details

| Field | Value |
|---|---|
| Package | `apktool` |
| Version | `3.0.3` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool) |
| Website | [https://apktool.org/](https://apktool.org/) |
| Dependencies | openjdk-21, aapt, wget |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install apktool
```

Verify that the command is available with `command -v apktool`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
