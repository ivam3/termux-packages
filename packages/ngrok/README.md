# ngrok

> Secure tunnels to localhost. Expose local servers behind NATs and firewalls to the public internet over secure tunnels.

## Overview

This package provides `ngrok` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://ngrok.com](https://ngrok.com)

## Installation

```bash
pkg update
pkg install ngrok
```

## Requirements

curl, proot, openssh

## Usage

```bash
ngrok --help
```

For the complete command reference, see the upstream documentation.

## Package details

| Field | Value |
|---|---|
| Package | `ngrok` |
| Version | `3.15.1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://ngrok.com](https://ngrok.com) |
| Dependencies | curl, proot, openssh |

## Troubleshooting

```bash
pkg update
pkg install ngrok
```

Verify that the command is available with `command -v ngrok`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
