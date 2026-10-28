# ghidra

> A software reverse engineering (SRE) framework developed by NSA. Supports disassembly, decompilation, scripting, and graphing.

## Installation

```bash
pkg install ghidra
```

## Info

| Field | Value |
|-------|-------|
| Version | `12.1.4` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [ghidra-sre.org](https://ghidra-sre.org) |

## Dependencies

`tur-repo, openjdk-21, clang, llvm, lldb, gradle, ndk-multilib, swig, make, curl, unzip`

Ghidra 12.1.4 requires JDK 21. The build uses the Gradle wrapper bundled with
Ghidra and the Android NDK to produce the `linux_arm_64` native components.

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

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```
