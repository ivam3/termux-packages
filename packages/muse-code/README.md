# muse-code

> Meta Muse Code interactive terminal AI coding agent for Termux. Runs under proot to work around Android app-data isolation.

## Overview

This package provides `muse-code` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://developer.meta.com/ai/products/muse-code](https://developer.meta.com/ai/products/muse-code)

## Installation

```bash
pkg update
pkg install muse-code
```

## Requirements

proot, curl, coreutils, python

## Usage

```bash
muse-code
```

`muse-code` starts the packaged Muse launcher inside a proot environment. The
launcher uses the Termux prefix and binds Android storage and system paths so the
agent can access the project files you expose to it. Run it from the project
directory you want the agent to work on.

## Package details

| Field | Value |
|---|---|
| Package | `muse-code` |
| Version | `0.1.0~R708.1-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://developer.meta.com/ai/products/muse-code](https://developer.meta.com/ai/products/muse-code) |
| Dependencies | proot, curl, coreutils, python |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install muse-code
```

Verify that the command is available with `command -v muse-code`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
