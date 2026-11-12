# wpscan

> WordPress security scanner — identify vulnerabilities in WordPress installations, plugins and themes.

## Overview

This package provides `wpscan` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/wpscanteam/wpscan](https://github.com/wpscanteam/wpscan)

## Installation

```bash
pkg update
pkg install wpscan
```

## Requirements

git, ruby, ndk-multilib

## Usage

```bash
wpscan --url https://example.com --enumerate vp
wpscan --url https://example.com --enumerate u --passwords rockyou.txt
```

## Package details

| Field | Value |
|---|---|
| Package | `wpscan` |
| Version | `4.1.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/wpscanteam/wpscan](https://github.com/wpscanteam/wpscan) |
| Dependencies | git, ruby, ndk-multilib |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install wpscan
```

Verify that the command is available with `command -v wpscan`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
