# evilginx2

> Standalone man-in-the-middle attack framework used for phishing login credentials along with session cookies, allowing for the bypass of 2-factor authentication.

## Overview

This package provides `evilginx2` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/kgretzky/evilginx2](https://github.com/kgretzky/evilginx2)

## Installation

```bash
pkg update
pkg install evilginx2
```

## Requirements

git, golang, make, curl

## Usage

```bash
evilginx2 [options]
```

Evilginx2 is built from source (there are no prebuilt `aarch64` binaries) and is installed in `~/.local/share/evilginx2`. Community phishlets are downloaded to `~/.local/share/evilginx2/phishlets` and loaded automatically when the interactive shell starts:

```bash
evilginx2
> config domain example.com
> phishlets enable office365
> phishlets get-url office365
> sessions
```

Configuration and captured sessions are stored in `~/.evilginx`.

## Package details

| Field | Value |
|---|---|
| Package | `evilginx2` |
| Version | `3.3.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/kgretzky/evilginx2](https://github.com/kgretzky/evilginx2) |
| Dependencies | git, golang, make, curl |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install evilginx2
```

Verify that the command is available with `command -v evilginx2`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
