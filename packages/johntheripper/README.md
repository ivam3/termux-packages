# johntheripper

> John the Ripper is a fast password cracker, currently available for many flavors of Unix, macOS, Windows, and more.

## Overview

This package provides `johntheripper` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/openwall/john](https://github.com/openwall/john)

## Installation

```bash
pkg update
pkg install johntheripper
```

## Requirements

git, make, clang, python, python-pip, opencl-vendor-driver

## Usage

```bash
john
john --help
john --wordlist=wordlist.txt hashes.txt
john --show hashes.txt
```

The package installs John the Ripper as `john`. Use the Jumbo community edition
rules and formats supported by the packaged build.

## Package details

| Field | Value |
|---|---|
| Package | `johntheripper` |
| Version | `1.9.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/openwall/john](https://github.com/openwall/john) |
| Dependencies | git, make, clang, python, python-pip, opencl-vendor-driver |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install johntheripper
```

Verify that the command is available with `command -v john`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
