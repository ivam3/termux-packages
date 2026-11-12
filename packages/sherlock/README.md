# sherlock

> Hunt down social media accounts by username across 300+ social networks.

## Overview

This package provides `sherlock` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)

## Installation

```bash
pkg update
pkg install sherlock
```

## Requirements

python, python-pip, python-numpy, python-pandas

## Usage

```bash
sherlock username
sherlock username1 username2
sherlock --help
```

Sherlock checks for a username across supported social networks. Use it only
for authorized research and respect each platform's terms.

## Package details

| Field | Value |
|---|---|
| Package | `sherlock` |
| Version | `0.16.0-1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) |
| Dependencies | python, python-pip, python-numpy, python-pandas |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install sherlock
```

Verify that the command is available with `command -v sherlock`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
