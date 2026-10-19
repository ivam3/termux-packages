# aguila-lang

> Aguila programming language (Spanish syntax, Rust speed) for Termux.

## Installation

```bash
pkg install aguila-lang
```

## Info

| Field | Value |
|-------|-------|
| Version | `2.4.3-1` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [aguila](https://github.com/emersonxinay/aguila) |

## Dependencies

`curl`

## Notes

- On `aarch64` the package downloads a prebuilt Bionic binary.
- On other architectures, or if the download fails, it builds the pinned `v2.4.3` source with Rust (`rust` is installed on demand).

## Usage

```bash
aguila                        # start the REPL
aguila ejecutar file.ag       # run a program
aguila chequear file.ag       # static check
aguila compilar file.ag       # compile
aguila --version
```

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```
