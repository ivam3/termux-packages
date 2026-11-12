# beef

> The Browser Exploitation Framework. BeEF is a penetration testing tool that focuses on the web browser.

## Overview

This package provides `beef` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/beefproject/beef](https://github.com/beefproject/beef)
- **Website:** [https://www.beefproject.com](https://www.beefproject.com)

## Installation

```bash
pkg update
pkg install beef
```

## Requirements

git, curl, ruby, nodejs-lts, imagemagick, geoip2-database

## Usage

```bash
beef-installer
```

> Run the installer first to set up BeEF and its dependencies, then use `beef` to launch the framework.

## Package details

| Field | Value |
|---|---|
| Package | `beef` |
| Version | `6.0.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/beefproject/beef](https://github.com/beefproject/beef) |
| Website | [https://www.beefproject.com](https://www.beefproject.com) |
| Dependencies | git, curl, ruby, nodejs-lts, imagemagick, geoip2-database |
| Suggests | i-haklab, metasploit-framework |

## Troubleshooting

```bash
pkg update
pkg install beef
```

Verify that the command is available with `command -v beef`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
