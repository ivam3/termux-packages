# shc

> Shell script compiler — converts shell scripts to binaries. The script is encrypted and will be decrypted and run at runtime.

## Overview

This package provides `shc` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [http://www.datsi.fi.upm.es/~frosal/sources/shc.html](http://www.datsi.fi.upm.es/~frosal/sources/shc.html)
- **Website:** [https://github.com/yanncam/UnSHc](https://github.com/yanncam/UnSHc)

## Installation

```bash
pkg update
pkg install shc
```

## Requirements

curl, tar, cmake, make, automake

## Usage

```bash
shc --help
```

For the complete command reference, see the upstream documentation.

## Suggestions

Also install: `unshc` — to decompile SHC-compiled scripts back to source.

## Package details

| Field | Value |
|---|---|
| Package | `shc` |
| Version | `3.8.9b` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [http://www.datsi.fi.upm.es/~frosal/sources/shc.html](http://www.datsi.fi.upm.es/~frosal/sources/shc.html) |
| Website | [https://github.com/yanncam/UnSHc](https://github.com/yanncam/UnSHc) |
| Dependencies | curl, tar, cmake, make, automake |
| Suggests | i-haklab, unshc |

## Troubleshooting

```bash
pkg update
pkg install shc
```

Verify that the command is available with `command -v shc`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
