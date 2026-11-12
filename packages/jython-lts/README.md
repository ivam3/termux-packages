# jython-lts

> Jython LTS 2.7.4 implements Python 2.7 on the JVM, giving Python programs access to Java classes and libraries.

## Overview

This package provides `jython-lts` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/jython/jython](https://github.com/jython/jython)

## Installation

```bash
pkg update
pkg install jython-lts
```

## Requirements

openjdk-21, curl, giflib

## Usage

```bash
jython
jython --help
jython -m pip --version
```

The package installs the Jython launcher as `jython`; the APT package name is
`jython-lts` to avoid confusion with the official Termux `jython` package. Use
`jython` for the JVM-based Python 2.7 runtime provided by this project.

## Package details

| Field | Value |
|---|---|
| Package | `jython-lts` |
| Version | `2.7.4` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/jython/jython](https://github.com/jython/jython) |
| Dependencies | openjdk-21, curl, giflib |
| Suggests | i-haklab, burpsuite |

## Troubleshooting

```bash
pkg update
pkg install jython-lts
```

Verify that the command is available with `command -v jython`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
