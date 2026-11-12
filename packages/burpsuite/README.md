# burpsuite

> An integrated platform/graphical tool for performing security testing of web applications.

## Overview

This package provides `burpsuite` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://portswigger.net](https://portswigger.net)
- **Website:** [https://portswigger.net/burp](https://portswigger.net/burp)

## Installation

```bash
pkg update
pkg install burpsuite
```

## Requirements

openjdk-21, curl, libffi, giflib

## Usage

```bash
burpsuite
```

> Run `burpsuite` to launch the GUI (requires a desktop environment, e.g. `termux-desktop-xfce` or Termux:X11).
>
> The package ships Bionic-compiled native libraries so recent Burp versions (2026.7.3) work on Termux:
> - `libjnidispatch.so` (JNA) — fixes `Could not initialize class com.sun.jna.Native` (glibc `libc.so.6` vs Bionic `libc.so`).
> - `libudev.so` (stub) — fixes `Could not initialize class com.sun.jna.platform.linux.Udev` (Android has no udev); OSHI falls back to `/proc`.
>
> Jar checksum (2026.7.3, `type=jar`): md5 `5321f0652288665ea6b88e31d4e156ec`, sha256 `c8262dc5426f38bedc490d66c5d21b6ff77d6dc6d85cefe6a66c882690134069` (official, from the [release page](https://portswigger.net/burp/releases/professional-community-2026-7-3)).

## Package details

| Field | Value |
|---|---|
| Package | `burpsuite` |
| Version | `2026.7.3` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://portswigger.net](https://portswigger.net) |
| Website | [https://portswigger.net/burp](https://portswigger.net/burp) |
| Dependencies | openjdk-21, curl, libffi, giflib |
| Suggests | termux-desktop-xfce, termux-x11, xwayland, i-haklab |

## Troubleshooting

```bash
pkg update
pkg install burpsuite
```

Verify that the command is available with `command -v burpsuite`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
