# code-server

> Code-server is VS Code with Node.js development environment running on a remote server, accessible through the browser.

## Overview

This package provides `code-server` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/coder/code-server](https://github.com/coder/code-server)
- **Website:** [https://coder.com/docs/code-server](https://coder.com/docs/code-server)

## Installation

```bash
pkg update
pkg install code-server
```

## Requirements

build-essential, tar, wget, nodejs-lts, yarn

## Usage

```bash
code-server
code-server --help
code-server --bind-addr 0.0.0.0:8080
```

The package provides the `code-server` command and its installer. See the
upstream documentation for TLS, authentication and extension configuration.

## Suggestions

Also install: `termux-desktop-xfce`

## Package details

| Field | Value |
|---|---|
| Package | `code-server` |
| Version | `4.7.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/coder/code-server](https://github.com/coder/code-server) |
| Website | [https://coder.com/docs/code-server](https://coder.com/docs/code-server) |
| Dependencies | build-essential, tar, wget, nodejs-lts, yarn |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install code-server
```

Verify that the command is available with `command -v code-server`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
