# slowhttptest

> SlowHTTPTest is a highly configurable tool that simulates some Application Layer Denial of Service attacks by prolonging HTTP connections in different ways.

## Overview

This package provides `slowhttptest` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/shekyan/slowhttptest](https://github.com/shekyan/slowhttptest)

## Installation

```bash
pkg update
pkg install slowhttptest
```

## Requirements

git, make, automake

## Usage

```bash
slowhttptest --help
```

For the complete command reference, see the upstream documentation.

## Package details

| Field | Value |
|---|---|
| Package | `slowhttptest` |
| Version | `1.8.3` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/shekyan/slowhttptest](https://github.com/shekyan/slowhttptest) |
| Dependencies | git, make, automake |
| Suggests | i-haklab, dos-a-tool |

## Troubleshooting

```bash
pkg update
pkg install slowhttptest
```

Verify that the command is available with `command -v slowhttptest`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
