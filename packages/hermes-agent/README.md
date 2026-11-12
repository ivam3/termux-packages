# hermes-agent

> Personal AI agent by Nous Research with CLI, TUI, messaging gateway, and browser automation. Runs the same agent core across Telegram, Discord, Slack, and 20+ platforms. Features persistent memory, skill learning, subagent delegation, scheduled cron jobs, and terminal/browser control.

## Overview

This package provides `hermes-agent` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

## Installation

```bash
pkg update
pkg install hermes-agent
```

## Requirements

python, nodejs-lts, python-pip, python-psutil, python-cryptography, clang, rust, make, pkg-config, libffi, openssl, ca-certificates, curl, git, ripgrep, ffmpeg, playwright-proot, termux-api, termux-oracle-skill

## Usage

```bash
hermes
hermes --help
```

The package installs the Hermes agent as `hermes`. Run it from a terminal to
start the CLI or TUI.

## Package details

| Field | Value |
|---|---|
| Package | `hermes-agent` |
| Version | `2026.9.24-1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) |
| Dependencies | python, nodejs-lts, python-pip, python-psutil, python-cryptography, clang, rust, make, pkg-config, libffi, openssl, ca-certificates, curl, git, ripgrep, ffmpeg, playwright-proot, termux-api, termux-oracle-skill |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install hermes-agent
```

Verify that the command is available with `command -v hermes`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
