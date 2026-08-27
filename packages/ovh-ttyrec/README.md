# ovh-ttyrec

> OVH fork of ttyrec — a terminal session recorder and player. Records and replays shell sessions.

## Installation

```bash
pkg install ovh-ttyrec
```

## Info

| Field | Value |
|-------|-------|
| Version | `1.2.0.0` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [ovh-ttyrec](https://github.com/ovh/ovh-ttyrec) |

## Dependencies

`git`, `make`, `clang`, `libcompiler-rt`, `zstd` (Bionic-native, no `bionic-host`/`glibc-repo` required)

> Note: `bionic-host` was removed from Termux; `ovh-ttyrec` now builds natively with `clang` + `pty.h`/`libutil` + `libzstd`.

## Usage

```bash
ttyrec [options]   # record: ttyrec -h for help
ttyplay [options] ./ttyrecord  # replay
ttytime ./ttyrecord            # print timings
```

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```
