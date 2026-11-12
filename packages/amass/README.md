# amass

> Performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques.

## Overview

This package provides `amass` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/OWASP/Amass](https://github.com/OWASP/Amass)

## Installation

```bash
pkg update
pkg install amass
```

## Requirements

golang

## Usage

```bash
amass [options]
```

> The postinst builds amass v5 from source via `CGO_ENABLED=0 go install -v github.com/owasp-amass/amass/v5/cmd/amass@main`, then run `amass [options]` to perform attack surface mapping and subdomain enumeration.

## Package details

| Field | Value |
|---|---|
| Package | `amass` |
| Version | `5.1.1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/OWASP/Amass](https://github.com/OWASP/Amass) |
| Dependencies | golang |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install amass
```

Verify that the command is available with `command -v amass`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
