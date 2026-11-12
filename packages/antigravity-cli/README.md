# antigravity-cli

> Google Antigravity CLI — an autonomous AI coding agent that runs entirely in your terminal. Powered by Gemini.

## Overview

This package provides `antigravity-cli` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/google-antigravity/antigravity-cli](https://github.com/google-antigravity/antigravity-cli)

## Installation

```bash
pkg update
pkg install antigravity-cli
```

## Requirements

clang, python, jq, curl, tar, glibc

## Usage

```bash
agy
agy --help
```

The package installs the `agy` bootstrapper. The upstream CLI is available
through that command.

## Suggestions

Also install: `termux-oracle-skill`, `opencode`, `claude-code`, `codebuff`, `freebuff`

## Package details

| Field | Value |
|---|---|
| Package | `antigravity-cli` |
| Version | `1.5.2-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/google-antigravity/antigravity-cli](https://github.com/google-antigravity/antigravity-cli) |
| Dependencies | clang, python, jq, curl, tar, glibc |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install antigravity-cli
```

Verify that the command is available with `command -v agy`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
