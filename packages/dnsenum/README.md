# dnsenum

> Multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks.

## Overview

This package provides `dnsenum` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/SparrowOchon/dnsenum2](https://github.com/SparrowOchon/dnsenum2)

## Installation

```bash
pkg update
pkg install dnsenum
```

## Requirements

git, perl, curl

## Usage

```bash
dnsenum [options] <domain>
```

> Example: `dnsenum example.com` performs DNS enumeration (A records, nameservers, MX, AXFR zone transfer, subdomain brute force with `~/.local/share/dnsenum/dns.txt` and reverse lookups).
>
> Google scraping is disabled by default if `WWW::Mechanize`/`HTML::Parser` are not installed; use `--scrap` to enable it.

## Package details

| Field | Value |
|---|---|
| Package | `dnsenum` |
| Version | `1.3.2` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/SparrowOchon/dnsenum2](https://github.com/SparrowOchon/dnsenum2) |
| Dependencies | git, perl, curl |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install dnsenum
```

Verify that the command is available with `command -v dnsenum`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
