# herdr

> Runtime for coding agents, distributed as a static Termux binary.

## Overview

This package provides `herdr` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/herdrdev/herdr](https://github.com/herdrdev/herdr)

## Installation

```bash
pkg update
pkg install herdr
```

## Requirements

curl, coreutils, gawk

## Usage

```bash
herdr
herdr --help
```

`herdr` is the runtime for coding agents. The package installs a static binary
and its launcher; see the upstream project for agent configuration.

## Install via deb (recommended, strict aarch64)

```sh
apt update && apt install herdr
herdr --version  # should print 0.8.2+
```

## What postinst does

- Detects `linux-aarch64` (strict deb arch `aarch64`, warns if host differs but still installs correct `TARGET`)
- Fetches `https://herdr.dev/latest.json` → parses `assets[TARGET]` + `sha256[TARGET]` with `awk` (no jq)
- Downloads `https://github.com/herdrdev/herdr/releases/download/.../herdr-linux-aarch64` with `curl --retry 3`
- Verifies `SHA-256` via `sha256sum`/`shasum`/`openssl`
- Installs to `$PREFIX/bin/herdr` (`chmod +x`), verifies `herdr --version`
- Installs `fixer` to `$PREFIX/bin/fixer` (ivam3 helper)

No wrappers, no pip, no git clone. Binary is statically linked (works with Android Bionic).

## Fallback: cargo build (only if network blocks herdr.dev/GitHub or you need a custom build)

Upstream `cargo build --release` as-is fails on Termux because `build.rs` only maps `aarch64-unknown-linux-gnu` targets, not `aarch64-linux-android`.

```sh
pkg install rust zig
git clone https://github.com/herdrdev/herdr && cd herdr
rustup target add aarch64-unknown-linux-gnu
cargo build --target aarch64-unknown-linux-gnu --release
cp target/aarch64-unknown-linux-gnu/release/herdr $PREFIX/bin/herdr
chmod +x $PREFIX/bin/herdr
herdr --version
```

See `build.rs:zig_target()` and `cargo --version / rustc --version / zig version` for toolchain details.

## Uninstall

- `prerm` asks `[Y/n]` before removing user data: `~/.config/herdr`, `~/.local/share/herdr`, `~/.cache/herdr`
- `postrm` removes `$PREFIX/bin/herdr` (installed by postinst, not tracked by dpkg data_files)
- `fixer` is intentionally kept (shared by other ivam3 packages)

## Issues

https://t.me/Ivam3_Bot

## Package details

| Field | Value |
|---|---|
| Package | `herdr` |
| Version | `0.9.5-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/herdrdev/herdr](https://github.com/herdrdev/herdr) |
| Dependencies | curl, coreutils, gawk |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install herdr
```

Verify that the command is available with `command -v herdr`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
