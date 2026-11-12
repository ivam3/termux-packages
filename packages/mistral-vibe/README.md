# mistral-vibe

> Minimal CLI coding assistant/agent powered by Mistral's models.

## Overview

This package provides `mistral-vibe` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe)

## Installation

```bash
apt install mistral-vibe
```

The package requires a working `glibc-repo` installation. The standalone
binary is installed in `$PREFIX/lib/mistral-vibe` and exposed as `vibe`.

## Requirements

coreutils, curl, unzip, glibc-repo, glibc, patchelf

## Usage

```bash
vibe
vibe --help
vibe --version
```

The package installs the Mistral Vibe CLI as `vibe`. Authentication and model
selection are handled by the upstream CLI.

## Notes

- No `uv` or `pip` build is performed during installation.
- `vibe-acp` is not included in the standalone CLI build; use the official
  upstream release if you need ACP mode.
- The standalone build version is pinned to the release selected by `updateAIpkg`.

## Help

```bash
i-Haklab about mistral-vibe
```

---

*Integrated into the i-Haklab ecosystem.*

## Package details

| Field | Value |
|---|---|
| Package | `mistral-vibe` |
| Version | `2.26.1-4` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe) |
| Dependencies | coreutils, curl, unzip, glibc-repo, glibc, patchelf |
| Suggests | i-haklab, neovim, termux-oracle-skill |

## Troubleshooting

```bash
pkg update
pkg install mistral-vibe
```

Verify that the command is available with `command -v vibe`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
