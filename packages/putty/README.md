# putty

> Graphical terminal program that supports the SSH, telnet, and rlogin protocols and connecting to serial ports.

## Overview

This package provides `putty` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://www.chiark.greenend.org.uk/~sgtatham/putty/](https://www.chiark.greenend.org.uk/~sgtatham/putty/)

## Installation

```bash
pkg update
pkg install putty
```

## Requirements

x11-repo, clang, cmake, openssh, curl, tar, putty-tools

This package is intended for the Termux X11 environment.

## Usage

```bash
putty
```

`putty` is the graphical SSH, Telnet, Rlogin and serial-console client. Launch it
from the desktop menu or the command above, then create and save a session.
`puttygen` and `pscp` are separate upstream tools and are not part of this
package.

## Package details

| Field | Value |
|---|---|
| Package | `putty` |
| Version | `0.77` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://www.chiark.greenend.org.uk/~sgtatham/putty/](https://www.chiark.greenend.org.uk/~sgtatham/putty/) |
| Dependencies | x11-repo, clang, cmake, openssh, curl, tar, putty-tools |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install putty
```

Verify that the command is available with `command -v putty`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
