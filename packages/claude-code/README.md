# claude-code

> NATIVE adaptation of Claude Code for Termux. Agentic coding tool that understands your codebase and helps you code faster through natural language commands.

## Overview

This package provides `claude-code` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code)

## Installation

```bash
pkg update
pkg install claude-code
```

## Requirements

glibc, clang, python, jq, curl, tar

## Usage

```bash
claude
claude --help
```

The package installs the `claude` bootstrapper and the Anthropic Claude Code
runtime. Authentication and account setup are handled by the upstream CLI.

## Suggestions

Also install: `termux-oracle-skill`, `opencode`, `antigravity-cli`, `codebuff`, `freebuff`

## Package details

| Field | Value |
|---|---|
| Package | `claude-code` |
| Version | `2.1.319-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/anthropics/claude-code](https://github.com/anthropics/claude-code) |
| Dependencies | glibc, clang, python, jq, curl, tar |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install claude-code
```

Verify that the command is available with `command -v claude`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
