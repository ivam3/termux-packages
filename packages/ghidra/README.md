# ghidra

> A software reverse engineering (SRE) framework developed by NSA. Supports disassembly, decompilation, scripting, and graphing.

## Overview

This package provides `ghidra` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

## Installation

```bash
pkg update
pkg install ghidra
```

## Requirements

tur-repo, openjdk-21, clang, llvm, lldb, gradle, ndk-multilib, swig, make, curl, unzip

## Usage

```bash
ghidra
```

The first install downloads the official Ghidra 12.1.4 archive, verifies its
SHA-256, and builds the Linux ARM64 native components with the Android NDK. This
can take a while and needs free space for the archive, the staging tree, and the
previous installation. On upgrade, the previous installation is kept as
`~/.local/share/ghidra.backup-<timestamp>` until the new build succeeds. If the
native build fails, the previous installation remains active.

The GUI wrapper exports `GHIDRA_INSTALL_DIR` to `~/.local/share/ghidra`. For
headless use:

```bash
export GHIDRA_INSTALL_DIR="$HOME/.local/share/ghidra"
"$GHIDRA_INSTALL_DIR/support/analyzeHeadless" --help
```

## REA integration

The `rea` package detects `~/.local/share/ghidra` automatically. Its launcher
exports `GHIDRA_INSTALL_DIR`, sets `JAVA_HOME` for the Termux JDK, and applies
the Linux platform shim required by REA's Ghidra provider. No manual environment
setup is needed when both packages are installed.

Verify the provider with:

```bash
rea doctor --json
rea analyze /system/bin/toybox --provider ghidra --format json
```

After confirming the new installation, remove an old backup with:

```bash
rm -rf ~/.local/share/ghidra.backup-*
```

## Package details

| Field | Value |
|---|---|
| Package | `ghidra` |
| Version | `12.1.4-1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) |
| Dependencies | tur-repo, openjdk-21, clang, llvm, lldb, gradle, ndk-multilib, swig, make, curl, unzip |
| Suggests | i-haklab, termux-desktop-xfce, rea |

## Troubleshooting

```bash
pkg update
pkg install ghidra
```

Verify that the command is available with `command -v ghidra`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
