# binwalk

> Fast, easy to use tool for analyzing, reverse engineering, and extracting firmware images.

## Overview

This package provides `binwalk` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk)

## Installation

```bash
pkg update
pkg install binwalk
```

## Requirements

rust, git

## Usage

```bash
binwalk firmware.bin
binwalk -e firmware.bin
binwalk -Me firmware.bin
```

`binwalk -e` extracts known file systems and compressed streams. `-M` enables
recursive scanning and `-e` extraction. Run `binwalk --help` for the complete
option list.

## Package details

| Field | Value |
|---|---|
| Package | `binwalk` |
| Version | `3.1.1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) |
| Dependencies | rust, git |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install binwalk
```

Verify that the command is available with `command -v binwalk`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
