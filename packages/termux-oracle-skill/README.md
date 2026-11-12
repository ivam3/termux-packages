# termux-oracle-skill

> A termux skill for AI coding agents with all context about termux, i-Haklab and Ivam3 termux-packages.

## Overview

This package provides `termux-oracle-skill` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/ivam3/termux-oracle](https://github.com/ivam3/termux-oracle)

## Installation

```bash
pkg update
pkg install termux-oracle-skill
```

## Requirements

git, tar, curl, wget, termux-api, termux-tools, termux-services, termux-exec

## Usage

The skill file is installed at:

```bash
~/.agents/skills/termux-oracle/SKILL.md
```

AI coding agents (e.g. `antigravity-cli`, `opencode`, `claude-code`, `codebuff`, `mimocode`) will automatically pick up the skill context from that path.

## Suggestions

Also install: `antigravity-cli`, `opencode`, `claude-code`, `codebuff`, `freebuff`, `openclaw`, `mimocode`, `mistral-vibe`

## Package details

| Field | Value |
|---|---|
| Package | `termux-oracle-skill` |
| Version | `0.4.2` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/ivam3/termux-oracle](https://github.com/ivam3/termux-oracle) |
| Dependencies | git, tar, curl, wget, termux-api, termux-tools, termux-services, termux-exec |
| Suggests | i-haklab, antigravity-cli, opencode, claude-code, codebuff, freebuff, openclaw, mimocode, mistral-vibe, zcode |

## Troubleshooting

```bash
pkg update
pkg install termux-oracle-skill
```

Verify that the skill file exists at `~/.agents/skills/termux-oracle/SKILL.md`. AI agents read it directly; no standalone command is installed.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
