# gobuster

> Directory/File, DNS and VHost busting tool written in Go.

## Overview

This package provides `gobuster` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/OJ/gobuster](https://github.com/OJ/gobuster)

## Installation

```bash
pkg update
pkg install gobuster
```

## Requirements

golang

## Usage

```bash
gobuster dir -u http://example.com -w wordlist.txt
gobuster dns -d example.com -w subdomains.txt
gobuster vhost -u http://example.com -w vhosts.txt
```

Gobuster is compiled from source with `go install github.com/OJ/gobuster/v3@v3.8.2`; the binary is placed in `~/.local/bin` / `~/go/bin`.

## Package details

| Field | Value |
|---|---|
| Package | `gobuster` |
| Version | `3.8.2` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/OJ/gobuster](https://github.com/OJ/gobuster) |
| Dependencies | golang |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install gobuster
```

Verify that the command is available with `command -v gobuster`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
