# opencode-v2

> OpenCode v2 — AI coding agent (anomalyco fork). Native glibc build for Termux.
> Coexists with the `opencode` v1 package: this one installs the `opencode-v2` command.

## Installation

```bash
# glibc support is required
apt install glibc-repo
pkg install opencode-v2
```

## Info

| Field | Value |
|-------|-------|
| Version | `2.0.32` |
| Architecture | `aarch64` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [opencode.ai](https://opencode.ai) |

## Dependencies

`glibc, clang, patchelf, curl, tar`

## Usage

```bash
opencode-v2 [options]
```

v1 remains available as `opencode`. Both commands share neither configuration nor
session data.

> Update with `pkg update`, not with `opencode-v2 upgrade`: the self-updater
> replaces the binary and loses the ELF interpreter patch needed on Termux.

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
