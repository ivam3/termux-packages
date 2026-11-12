# axmlprinter2

> Prints XML document from binary XML file (with correct namespace handing & attribute formatting).

## Overview

This package provides `axmlprinter2` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://code.google.com/archive/p/android4me](https://code.google.com/archive/p/android4me)

## Installation

```bash
pkg update
pkg install axmlprinter2
```

## Requirements

curl, openjdk-21

## Usage

```bash
axmlprinter2 [options]
```

> The postinst downloads the AXMLPrinter2 jar (original android4me build from the Google Code Archive) to `~/.local/share/AXMLPrinter2.jar` and installs the `axmlprinter2` wrapper.

## Package details

| Field | Value |
|---|---|
| Package | `axmlprinter2` |
| Version | `2.10.08` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://code.google.com/archive/p/android4me](https://code.google.com/archive/p/android4me) |
| Dependencies | curl, openjdk-21 |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install axmlprinter2
```

Verify that the command is available with `command -v axmlprinter2`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
