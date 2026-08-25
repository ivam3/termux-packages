# azure-cli

> Microsoft Azure Command-Line Interface — manage Azure services from the terminal.

## Installation

```bash
pkg install azure-cli
```

## Info

| Field | Value |
|-------|-------|
| Version | `2.89.1` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [Azure CLI](https://learn.microsoft.com/cli/azure) |

## Dependencies

`tur-repo, python3.10, curl, openssl`

## Usage

```bash
az [command]
```

> The postinst installs azure-cli 2.89.1 with `pip install --target ${PREFIX}/opt/az` (requires the `python3.10` package from tur-repo), then runs `az [command]` to manage Azure services from the terminal.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```