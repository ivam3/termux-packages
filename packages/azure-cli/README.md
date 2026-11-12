# azure-cli

> Microsoft Azure Command-Line Interface — manage Azure services from the terminal.

## Overview

This package provides `azure-cli` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/Azure/azure-cli](https://github.com/Azure/azure-cli)

## Installation

```bash
pkg update
pkg install azure-cli
```

## Requirements

tur-repo, python3.10, curl, openssl

## Usage

```bash
az login
az account show
az group list
az vm list --output table
```

Run `az --help` or `az <group> --help` for the full command reference.

## Package details

| Field | Value |
|---|---|
| Package | `azure-cli` |
| Version | `2.89.1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/Azure/azure-cli](https://github.com/Azure/azure-cli) |
| Dependencies | tur-repo, python3.10, curl, openssl |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install azure-cli
```

Verify that the command is available with `command -v az`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
