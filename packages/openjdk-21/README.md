# openjdk-21

> OpenJDK 21 LTS for Android/Termux via glibc-runner. Enables Java applications including Metasploit, Ghidra, Burp Suite and more.

## Overview

This package provides `openjdk-21` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://jdk.java.net](https://jdk.java.net)

## Installation

```bash
pkg update
pkg install openjdk-21
```

## Requirements

wget

## Usage

```bash
java -version
javac -version
jar --version
keytool -help
```

The package provides a Java 21 runtime and development tools. Run Java
applications with `java`, compile with `javac`, package with `jar` and manage
keystores with `keytool`. The APT package name is `openjdk-21`; the commands are
the standard Java tools.

## Package details

| Field | Value |
|---|---|
| Package | `openjdk-21` |
| Version | `21.1.1-1` |
| Architecture | `aarch64` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://jdk.java.net](https://jdk.java.net) |
| Dependencies | wget |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install openjdk-21
```

Verify that the command is available with `command -v java`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
