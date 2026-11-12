# dex2jar

> Tools to work with android .dex and java .class files.

## Overview

This package provides `dex2jar` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/pxb1988/dex2jar](https://github.com/pxb1988/dex2jar)

## Installation

```bash
pkg update
pkg install dex2jar
```

## Requirements

curl, unzip, openjdk-21

## Usage

```bash
dex2jar                      # list available tools
dex2jar <tool> <options + arguments>
```

> Example: `dex2jar d2j-dex2jar -f ~/path/to/apk_to_decompile.apk` converts a DEX file to JAR.
>
> The tool scripts are downloaded to `~/.local/share/dex2jar` on install and are executed with `openjdk-21`.

## Suggestions

Also install: `fixer`

## Package details

| Field | Value |
|---|---|
| Package | `dex2jar` |
| Version | `2.4` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/pxb1988/dex2jar](https://github.com/pxb1988/dex2jar) |
| Dependencies | curl, unzip, openjdk-21 |
| Suggests | fixer |

## Troubleshooting

```bash
pkg update
pkg install dex2jar
```

Verify that the command is available with `command -v dex2jar`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
