# openclaw

> OpenRouter-powered AI coding agent for Termux. Access multiple AI models (GPT-4, Claude, Mistral) from a single terminal interface.

## Overview

This package provides `openclaw` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android)

## Installation

```bash
pkg update
pkg install openclaw
```

## Requirements

android-tools, git, curl, nodejs-lts, pacman, python, python-pip, make, cmake, clang, binutils, proot, tar, xz-utils, file

## Usage

```bash
openclaw
openclaw --help
phone_control --help
phone_agent --help
```

OpenClaw is an autonomous agent with optional Android device-control helpers.
The package also installs `phone_control` and `phone_agent` for ADB, root or
`rish`-based automation. Review the agent's commands before granting device
control.

## Suggestions

Install also: `termux-oracle-skill`, `antigravity-cli`, `claude-code`, `codebuff`, `freebuff`

## Package details

| Field | Value |
|---|---|
| Package | `openclaw` |
| Version | `2026.11.1-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) |
| Dependencies | android-tools, git, curl, nodejs-lts, pacman, python, python-pip, make, cmake, clang, binutils, proot, tar, xz-utils, file |
| Suggests | i-haklab, botgram |

## Troubleshooting

```bash
pkg update
pkg install openclaw
```

Verify that the command is available with `command -v openclaw`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
