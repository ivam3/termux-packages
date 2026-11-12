# aguila-lang

> Aguila programming language (Spanish syntax, Rust speed) for Termux.

## Overview

This package provides `aguila-lang` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/emersonxinay/aguila](https://github.com/emersonxinay/aguila)

## Installation

```bash
pkg update
pkg install aguila-lang
```

## Requirements

tar, curl, rust

## Usage

```bash
aguila                        # start the REPL
aguila ejecutar file.ag       # run a program
aguila chequear file.ag       # static check
aguila compilar file.ag       # compile
aguila --version
```

## Notes

- On `aarch64` the package downloads a prebuilt Bionic binary.
- On other architectures, or if the download fails, it builds the pinned `v2.4.3` source with Rust (`rust` is installed on demand).

## Package details

| Field | Value |
|---|---|
| Package | `aguila-lang` |
| Version | `2.4.3-1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/emersonxinay/aguila](https://github.com/emersonxinay/aguila) |
| Dependencies | tar, curl, rust |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install aguila-lang
```

Verify that the command is available with `command -v aguila`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
