# opencode

> OpenCode — open source AI coding agent. Works with any model provider (OpenAI, Anthropic, Groq, Ollama). Runs in the terminal.

## Overview

This package provides `opencode` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/opencode-ai/opencode](https://github.com/opencode-ai/opencode)

## Installation

```bash
pkg update
pkg install opencode
```

## Requirements

glibc, clang, python, jq, curl, tar

## Usage

```bash
opencode
opencode --help
```

The package installs the OpenCode v1 binary and its environment file. Start it
inside a project directory. OpenCode v2 can be installed alongside it as
`opencode-v2`.

## Suggestions

Install also: `termux-oracle-skill`, `antigravity-cli`, `claude-code`, `codebuff`, `freebuff`

## Package details

| Field | Value |
|---|---|
| Package | `opencode` |
| Version | `1.19.5-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/opencode-ai/opencode](https://github.com/opencode-ai/opencode) |
| Dependencies | glibc, clang, python, jq, curl, tar |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install opencode
```

Verify that the command is available with `command -v opencode`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
