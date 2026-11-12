# hydra-gtk

> Number one brute forcing tool in ciber security on cli and x11(graphical interface).

## Overview

This package provides `hydra-gtk` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra)

## Installation

```bash
pkg update
pkg install hydra-gtk
```

## Requirements

autoconf-archive, git, cmake, make, automake, gtk2, libgcrypt, libgpg-error, libssh, libidn, libxfixes, mariadb, openssl, openssl-tool, pcre, pcre2, postgresql, subversion

## Usage

```bash
xhydra
```

`xhydra` is the GTK frontend for Hydra. Configure the target, service, username
list, password list and task options in the graphical dialog, then start the
attack. Use it only against systems you are authorized to test.

## Package details

| Field | Value |
|---|---|
| Package | `hydra-gtk` |
| Version | `9.6` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra) |
| Dependencies | autoconf-archive, git, cmake, make, automake, gtk2, libgcrypt, libgpg-error, libssh, libidn, libxfixes, mariadb, openssl, openssl-tool, pcre, pcre2, postgresql, subversion |
| Suggests | i-haklab, x11-repo, xwayland |

## Troubleshooting

```bash
pkg update
pkg install hydra-gtk
```

Verify that the command is available with `command -v xhydra`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
