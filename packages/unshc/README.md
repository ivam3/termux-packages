# unshc

> UnSHc is a tool to unpack and decompile SHC-compiled shell scripts back to readable source.

## Overview

This package provides `unshc` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/yanncam/UnSHc](https://github.com/yanncam/UnSHc)

## Installation

```bash
pkg update
pkg install unshc
```

## Requirements

curl

## Usage

```bash
unshc <shc-compiled-binary>
```

## Suggestions

Also install: `shc` — to compile shell scripts into binaries.

## Package details

| Field | Value |
|---|---|
| Package | `unshc` |
| Version | `0.1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/yanncam/UnSHc](https://github.com/yanncam/UnSHc) |
| Dependencies | curl |
| Suggests | i-haklab, shc |

## Troubleshooting

```bash
pkg update
pkg install unshc
```

Verify that the command is available with `command -v unshc`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
