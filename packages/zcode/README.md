# zcode

> ZCode — AI vibe coding harness (GLM-5.3) native glibc aarch64 for termux-x11.

## Overview

This package provides `zcode` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://zcode.z.ai](https://zcode.z.ai)

## Installation

```bash
pkg update
pkg install zcode
```

## Requirements

x11-repo, termux-x11-nightly, glibc-repo, glibc, curl, tar, jq, patchelf-glibc, fontconfig-glibc, freetype-glibc, gnome-themes-extra

This package is intended for the Termux X11 environment.

## Usage

```bash
zcode
zcode --help
```

`zcode` is the Z.ai coding harness for Termux. Start it inside a project
directory; authentication and model selection are handled by the CLI.

## Suggestions

Also install: `i-haklab`, `termux-x11-nightly`

## Package details

| Field | Value |
|---|---|
| Package | `zcode` |
| Version | `3.17.2-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://zcode.z.ai](https://zcode.z.ai) |
| Dependencies | x11-repo, termux-x11-nightly, glibc-repo, glibc, curl, tar, jq, patchelf-glibc, fontconfig-glibc, freetype-glibc, gnome-themes-extra |
| Suggests | i-haklab, termux-desktop-xfce |

## Troubleshooting

```bash
pkg update
pkg install zcode
```

Verify that the command is available with `command -v zcode`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
