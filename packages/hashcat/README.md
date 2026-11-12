# hashcat

> World's fastest and most advanced password recovery utility supporting 300+ highly optimized hashing algorithms.

## Overview

This package provides `hashcat` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/hashcat/hashcat](https://github.com/hashcat/hashcat)

## Installation

```bash
pkg update
pkg install hashcat
```

## Requirements

git, glibc-repo, libc++, clang, libiconv, make, ocl-icd, opencl-vendor-driver, rust

## Usage

```bash
hashcat -m 0 hash.txt wordlist.txt
hashcat --show hash.txt
```

## Package details

| Field | Value |
|---|---|
| Package | `hashcat` |
| Version | `7.1.2` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/hashcat/hashcat](https://github.com/hashcat/hashcat) |
| Dependencies | git, glibc-repo, libc++, clang, libiconv, make, ocl-icd, opencl-vendor-driver, rust |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install hashcat
```

Verify that the command is available with `command -v hashcat`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
