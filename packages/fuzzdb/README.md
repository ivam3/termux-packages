# fuzzdb

> Dictionary of attack patterns and primitives for black-box application fault injection and resource discovery.

## Overview

This package provides `fuzzdb` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/fuzzdb-project/fuzzdb](https://github.com/fuzzdb-project/fuzzdb)

## Installation

```bash
pkg update
pkg install fuzzdb
```

## Requirements

git

## Usage

```bash
fuzzdb
# Fuzz data base saved in: $HOME/.local/share/wordlist/fuzzdb
```

## Package details

| Field | Value |
|---|---|
| Package | `fuzzdb` |
| Version | `20.11.25` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/fuzzdb-project/fuzzdb](https://github.com/fuzzdb-project/fuzzdb) |
| Dependencies | git |
| Suggests | i-haklab, wfuzz |

## Troubleshooting

```bash
pkg update
pkg install fuzzdb
```

Verify that the command is available with `command -v fuzzdb`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
