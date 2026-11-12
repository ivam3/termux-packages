# metasploit-framework

> The world's most used penetration testing framework. Metasploit gives you the power to exploit vulnerabilities, generate payloads, and manage post-exploitation.

## Overview

This package provides `metasploit-framework` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework)

## Installation

```bash
pkg update
pkg install metasploit-framework
```

## Requirements

build-essential, ruby, python, libcap, openjdk-21, termux-tools, autoconf, patchelf, binutils, bison, yarn, clang, coreutils, curl, findutils, gumbo-parser, apr, apr-util, postgresql, openssl, readline, libffi, libgmp, libpcap, libsqlite, libgrpc, libtool, libxml2, libxslt, make, ncurses-utils, ncurses, git, unzip, xz-utils, zip, zlib, tar, xml2axml, termux-elf-cleaner, pkg-config, resolv-conf, aapt, apksigner, apktool

## Usage

```bash
msfconsole
msfvenom --help
msfdb init
```

The package provides the Metasploit Framework console, `msfvenom` and the
database helpers. Start with `msfconsole` and use `help` inside the console.

## Package details

| Field | Value |
|---|---|
| Package | `metasploit-framework` |
| Version | `6.4.134` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework) |
| Dependencies | build-essential, ruby, python, libcap, openjdk-21, termux-tools, autoconf, patchelf, binutils, bison, yarn, clang, coreutils, curl, findutils, gumbo-parser, apr, apr-util, postgresql, openssl, readline, libffi, libgmp, libpcap, libsqlite, libgrpc, libtool, libxml2, libxslt, make, ncurses-utils, ncurses, git, unzip, xz-utils, zip, zlib, tar, xml2axml, termux-elf-cleaner, pkg-config, resolv-conf, aapt, apksigner, apktool |
| Suggests | embed, i-haklab |

## Troubleshooting

```bash
pkg update
pkg install metasploit-framework
```

Verify that the command is available with `command -v msfconsole`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
