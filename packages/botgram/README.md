# botgram

> Telegram group scraper and CLI utility for collecting member, comment and post data.

## Overview

This package provides `botgram` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/ivam3/botgram](https://github.com/ivam3/botgram)

## Installation

```bash
pkg update
pkg install botgram
```

## Requirements

- `git`
- `python`
- `python-pip`
- `python-pandas` (installed from the Termux APT repository, not with pip)

## Usage

```bash
botgram
```

The package launcher opens an interactive menu for the Botgram tools:

| Option | Action |
|---|---|
| `getdata` | Export members of a Telegram group to CSV. |
| `sendmsg` | Send messages from an exported CSV list. |
| `add2group` | Invite CSV members to a group. |
| `getUserComments` | Export one user's messages from a group. |
| `setup` | Open a submenu to configure credentials, install requirements or merge CSV files. |
| `exit` | Close the menu. |

Option `5` opens a setup submenu, so it never asks you to type command-line
parameters. Choose an action from the submenu:

| Setup option | Action |
|---|---|
| `1` | Create or update `config.data` (API ID, API hash and phone). |
| `2` | Install or refresh Telethon with pip. Pandas comes from APT. |
| `3` | Prompt for two CSV files and merge them. |
| `4` | Return to the main menu. |

The launcher and the package `postinst` install only Telethon with pip. They do
not call the legacy `setup.py --install` flow, which offered to install
`cython`, `numpy` and `pandas` with pip. `python-pandas` is provided by APT.

The same commands can be run directly from the package source directory with
`python getdata.py`, `python sendmsg.py`, `python add2group.py`,
`python getUserComments.py` and `python setup.py`. See the
[Botgram README](https://github.com/ivam3/botgram)
for configuration, CSV format, rate limits and security notes.

## Package details

| Field | Value |
|---|---|
| Package | `botgram` |
| Version | `2.0.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/ivam3/botgram](https://github.com/ivam3/botgram) |
| Dependencies | git, python, python-pip, python-pandas |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install botgram
```

Verify that the command is available with `command -v botgram`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
