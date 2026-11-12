# opencode-v2

> OpenCode v2 AI coding agent. Native glibc build for Termux, coexists with opencode v1.

## Overview

This package provides `opencode-v2` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/anomalyco/opencode](https://github.com/anomalyco/opencode)

## Installation

```bash
pkg update
pkg install opencode-v2
```

## Requirements

glibc, clang, patchelf, curl, tar

## Usage

```bash
opencode-v2
opencode-v2 --help
```

The package installs OpenCode v2 as `opencode-v2`, so it can coexist with the
v1 `opencode` package. Start it inside a project directory.

## Paths (isolated from v1)

| Data | Path |
|------|------|
| Config | `~/.opencode-v2/config/opencode/opencode.json(c)` |
| Data / DB | `~/.opencode-v2/data/opencode/` |
| Cache | `~/.opencode-v2/cache/opencode/` |
| State | `~/.opencode-v2/state/opencode/` |
| API keys | `~/.opencode-v2/.env` |
| Binary | `~/.local/share/opencode-v2/opencode.real` |

Inspect the effective paths at any time:

```bash
opencode-v2 debug paths
```

## Removal

```bash
pkg uninstall opencode-v2          # keeps config and sessions
pkg uninstall --purge opencode-v2  # removes config and sessions
```

## Suggestions

Install also: `i-haklab`, `termux-oracle-skill`, `antigravity-cli`, `claude-code`, `codebuff`, `freebuff`

## Package details

| Field | Value |
|---|---|
| Package | `opencode-v2` |
| Version | `2.0.32-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/anomalyco/opencode](https://github.com/anomalyco/opencode) |
| Dependencies | glibc, clang, patchelf, curl, tar |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install opencode-v2
```

Verify that the command is available with `command -v opencode-v2`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
