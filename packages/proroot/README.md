# proroot

> Rootless Linux runtime for Android. Drop-in proot replacement with zero ptrace overhead. Run full glibc Linux userspace (Node.js, Python, Git, Chromium) inside Android without root.

## Overview

This package provides `proroot` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/coderredlab/proroot](https://github.com/coderredlab/proroot)

## Installation

```bash
pkg update
pkg install proroot
```

## Requirements

wget

## Usage

```bash
proroot --help
```

For the complete command reference, see the upstream documentation.

## Package details

| Field | Value |
|---|---|
| Package | `proroot` |
| Version | `1.2.8-2` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/coderredlab/proroot](https://github.com/coderredlab/proroot) |
| Dependencies | wget |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install proroot
```

Verify that the command is available with `command -v proroot`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
