# freebuff

> AI coding assistant that edits your codebase through natural language instructions. A buffcode free version with ad-supported — no subscription, no credits, no configuration.

## Overview

This package provides `freebuff` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/CodebuffAI/codebuff-community](https://github.com/CodebuffAI/codebuff-community)

## Installation

```bash
pkg update
pkg install freebuff
```

## Requirements

glibc, clang, python, jq, curl, tar

## Usage

```bash
freebuff
freebuff --help
```

The package installs the Freebuff binary and its environment file. Start the
agent from the project directory you want it to inspect.

## Package details

| Field | Value |
|---|---|
| Package | `freebuff` |
| Version | `0.2.36-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/CodebuffAI/codebuff-community](https://github.com/CodebuffAI/codebuff-community) |
| Dependencies | glibc, clang, python, jq, curl, tar |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install freebuff
```

Verify that the command is available with `command -v freebuff`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
