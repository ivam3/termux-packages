# xleak

> A fast terminal Excel viewer with an interactive TUI interface.

## Installation

```bash
pkg install xleak
```

## Info

| Field | Value |
|-------|-------|
| Version | `0.2.5` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [xleak](https://github.com/bgreenwell/xleak) |

## Dependencies

`git, python, rust, clang, make, build-essential, libtool, patch, libxcb, libx11, termux-api`

## Usage

The patch script is installed at:

```bash
$PREFIX/share/xleak/xleak_patch.py
```

Run it to apply compatibility patches for Termux:

```bash
python $PREFIX/share/xleak/xleak_patch.py
```

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```
