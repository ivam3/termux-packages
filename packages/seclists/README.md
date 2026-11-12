# seclists

> SecLists is the security tester's companion. It is a collection of multiple types of lists used during security assessments: usernames, passwords, URLs, fuzzing payloads, patterns and more.

## Overview

This package provides `seclists` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)

## Installation

```bash
pkg update
pkg install seclists
```

## Requirements

unzip, curl

## Usage

```bash
seclists
# SecLists saved in: $HOME/.local/share/wordlist/SecLists-master
```

## Package details

| Field | Value |
|---|---|
| Package | `seclists` |
| Version | `8.23.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) |
| Dependencies | unzip, curl |
| Suggests | i-haklab, dirb, gobuster |

## Troubleshooting

```bash
pkg update
pkg install seclists
```

Verify that the command is available with `command -v seclists`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
