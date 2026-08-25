# burpsuite

> Burp Suite Community Edition — integrated platform for web application security testing.

## Installation

```bash
pkg install burpsuite
```

## Info

| Field | Value |
|-------|-------|
| Version | `2026.7.3` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [Burp Suite](https://portswigger.net/burp) |

## Dependencies

`openjdk-21, curl, libffi, giflib`

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

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```