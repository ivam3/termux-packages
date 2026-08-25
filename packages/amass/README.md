# amass

> In-depth attack surface mapping and asset discovery.

## Installation

```bash
pkg install amass
```

## Info

| Field | Value |
|-------|-------|
| Version | `v5.1.1` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [OWASP Amass](https://github.com/OWASP/Amass) |

## Dependencies

`golang`

## Usage

```bash
amass [options]
```

> The postinst builds amass v5 from source via `CGO_ENABLED=0 go install -v github.com/owasp-amass/amass/v5/cmd/amass@main`, then run `amass [options]` to perform attack surface mapping and subdomain enumeration.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```