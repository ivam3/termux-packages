# hashcat

> World's fastest and most advanced password recovery utility supporting 300+ highly optimized hashing algorithms.

## Installation

```bash
pkg install hashcat
```

## Info

| Field | Value |
|-------|-------|
| Version | `7.1.2` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [hashcat](https://github.com/hashcat/hashcat) |

## Dependencies

`git, glibc-repo, libc++, clang, libiconv, make, ocl-icd, opencl-vendor-driver, rust`

## Usage

```bash
hashcat -m 0 hash.txt wordlist.txt
hashcat --show hash.txt
```

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```