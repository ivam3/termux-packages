# codebuff

> AI coding agent that edits your codebase via natural language. Pair program with AI directly in your terminal.

## Overview

This package provides `codebuff` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/CodebuffAI/codebuff](https://github.com/CodebuffAI/codebuff)

## Installation

```bash
pkg update
pkg install codebuff
```

## Requirements

glibc, clang, python, jq, wget, tar

## Usage

```bash
codebuff
codebuff --help
```

The package installs the Codebuff binary and its environment file. Start the
interactive agent from a project directory.

## Suggestions

Also install: `termux-oracle-skill`, `opencode`, `antigravity-cli`, `claude-code`, `freebuff`

## Package details

| Field | Value |
|---|---|
| Package | `codebuff` |
| Version | `1.0.420-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/CodebuffAI/codebuff](https://github.com/CodebuffAI/codebuff) |
| Dependencies | glibc, clang, python, jq, wget, tar |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install codebuff
```

Verify that the command is available with `command -v codebuff`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
