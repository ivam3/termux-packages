# xleak

> A fast terminal Excel viewer with an interactive TUI interface.

## Overview

This package provides `xleak` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/bgreenwell/xleak](https://github.com/bgreenwell/xleak)

## Installation

```bash
pkg update
pkg install xleak
```

## Requirements

git, python, rust, clang, make, build-essential, libtool, patch, libxcb, libx11, termux-api

This package is intended for the Termux X11 environment.

## Usage

```bash
xleak
xleak --help
```

`xleak` is a terminal Excel viewer with an interactive TUI. Open a workbook from
the command line and use the on-screen key bindings to inspect sheets and cells.

## Package details

| Field | Value |
|---|---|
| Package | `xleak` |
| Version | `0.2.5` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/bgreenwell/xleak](https://github.com/bgreenwell/xleak) |
| Dependencies | git, python, rust, clang, make, build-essential, libtool, patch, libxcb, libx11, termux-api |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install xleak
```

Verify that the command is available with `command -v xleak`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
