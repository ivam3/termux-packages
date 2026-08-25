# dnsenum

> Multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks.
>
> This package uses the maintained fork **dnsenum2** (v1.3.2), which keeps the original dnsenum working on modern systems.

## Installation

```bash
pkg install dnsenum
```

## Info

| Field | Value |
|-------|-------|
| Version | `1.3.2` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [dnsenum2](https://github.com/SparrowOchon/dnsenum2) |

## Dependencies

`git, perl, curl` + CPAN modules (`Net::IP`, `Net::DNS`, `Net::Netmask`, `XML::Writer`, `String::Random`)

## Usage

```bash
dnsenum [options] <domain>
```

> Example: `dnsenum example.com` performs DNS enumeration (A records, nameservers, MX, AXFR zone transfer, subdomain brute force with `~/.local/share/dnsenum/dns.txt` and reverse lookups).
>
> Google scraping is disabled by default if `WWW::Mechanize`/`HTML::Parser` are not installed; use `--scrap` to enable it.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```