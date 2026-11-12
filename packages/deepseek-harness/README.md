# deepseek-harness

> DeepSeek Harness (`dsh`) — AI coding harness. Native glibc Node.js runtime adapted for Termux.

## Overview

This package provides `deepseek-harness` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)

## Installation

```bash
pkg update
pkg install deepseek-harness
```

## Requirements

glibc, clang, make, python, pkg-config, curl, tar, xz-utils, ca-certificates, bash, coreutils

## Usage

```bash
dsh
dsh --help
dsh-npm --version
dsh-npx --version
```

The package provides `dsh`, its bundled Node.js runtime and the `dsh-npm`,
`dsh-npx` and `dsh-pnpm` helpers. Run `dsh` from the project you want to work
on.

## Notes

- The package uses the Termux glibc loader; it does not replace the system Node.js.
- `dsh-npm`, `dsh-npx` and `dsh-pnpm` use the isolated glibc runtime.
- `dsh web` binds to `127.0.0.1:3080`; use `--no-open` because Termux has no desktop browser opener.
- On removal, `~/.dsh` is preserved. Use `pkg purge deepseek-harness` to delete it.

## Layout

| Field | Value |
|-------|-------|
| Package | `deepseek-harness` |
| Command | `dsh` |
| Architecture | `aarch64` |
| Node.js | `24.22.1` (linux-arm64, glibc) |
| dsh | `0.2.1-rc.2` |
| User data | `~/.dsh` |
| Runtime | `~/.local/share/deepseek-harness` |

## Package details

| Field | Value |
|---|---|
| Package | `deepseek-harness` |
| Version | `0.2.1-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) |
| Dependencies | glibc, clang, make, python, pkg-config, curl, tar, xz-utils, ca-certificates, bash, coreutils |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install deepseek-harness
```

Verify that the command is available with `command -v dsh`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
