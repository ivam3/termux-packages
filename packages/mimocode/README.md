# mimocode

> AI coding agent tailored for Termux and Android. A lightweight alternative to full AI agents optimized for mobile ARM devices.

## Overview

This package provides `mimocode` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code)

## Installation

```bash
pkg update
pkg install mimocode
```

## Requirements

glibc, clang, python, jq, curl, tar

## Usage

```bash
mimocode
mimocode --help
```

The package installs the MiMo coding agent binary and its environment file.
Start it from the project directory you want to work on.

## Suggestions

Install also: `termux-oracle-skill`, `opencode`, `antigravity-cli`, `claude-code`, `codebuff`, `freebuff`

## Package details

| Field | Value |
|---|---|
| Package | `mimocode` |
| Version | `0.1.16-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) |
| Dependencies | glibc, clang, python, jq, curl, tar |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install mimocode
```

Verify that the command is available with `command -v mimocode`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
