# adbfastboot

> Android Debug Bridge (adb) and fastboot tools from Android platform-tools.

## Overview

This package provides `adbfastboot` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://developer.android.com/studio/command-line/adb](https://developer.android.com/studio/command-line/adb)

## Installation

```bash
pkg update
pkg install adbfastboot
```

## Requirements

brotli, libc++, liblz4, libprotobuf, libusb, pcre2, zlib, zstd

## Usage

```bash
adb devices
adb shell
adb install app.apk
fastboot devices
fastboot flash boot boot.img
fastboot reboot
```

`adbfastboot` installs the Android platform tools. Run `adb --help` or
`fastboot --help` for the full command reference.

## Package details

| Field | Value |
|---|---|
| Package | `adbfastboot` |
| Version | `1.0.41a-33.0.3f` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://developer.android.com/studio/command-line/adb](https://developer.android.com/studio/command-line/adb) |
| Dependencies | brotli, libc++, liblz4, libprotobuf, libusb, pcre2, zlib, zstd |
| Suggests | i-haklab, ghost, phonesploit |

## Troubleshooting

```bash
pkg update
pkg install adbfastboot
```

Verify that the command is available with `command -v adb`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
