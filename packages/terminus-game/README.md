# terminus-game

> Terminal port of Terminus, the Linux learning adventure game.

## Overview

This package provides `terminus-game` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/mprat/Terminus](https://github.com/mprat/Terminus)

## Installation

```bash
pkg update
pkg install terminus-game
```

## Requirements

nodejs-lts

## Usage

```sh
terminus-game                 # play (auto-saves)
terminus-game --reset         # start a new game
terminus-game --no-save       # play without saving
terminus-game --save FILE     # use a custom save file
terminus-game --script FILE   # run commands from a file
terminus-game --images=chafa  # render images with chafa
terminus-game --images=open   # open images with termux-open
terminus-game --images=off    # disable images
terminus-game --esp           # play in Spanish
terminus-game --lang es       # same as --esp
terminus-game --help
```

## Language

The game is in English by default. Use `--esp` (or `--lang es`) to play in
Spanish. The setting can also be made permanent for your shell with:

```sh
export TERMINUS_LANG=es
```

Room names, item names, commands and the books used by the `grep` puzzle stay
in English; their descriptions and all messages are translated. Saves are
compatible between languages.

## Images

Room and item pictures are rendered inline with `chafa` when available and the
output is a terminal (`--images=auto`). Install it with:

```sh
pkg install chafa
```

If `chafa` is missing, the game remains fully playable as text. With
`--images=open`, images are opened in an external app through `termux-open`
(package `termux-api`).

## Save data

Progress is stored in:

```
$XDG_DATA_HOME/terminus-game/save.json
```

which defaults to `~/.local/share/terminus-game/save.json`. Set `TERMINUS_SAVE`
to override it. The save file survives package upgrades, reinstallation and
removal; delete it (or use `--reset`) to start over.

## Package details

| Field | Value |
|---|---|
| Package | `terminus-game` |
| Version | `1.0.0-4` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/mprat/Terminus](https://github.com/mprat/Terminus) |
| Dependencies | nodejs-lts |
| Suggests | chafa, termux-api, i-haklab |

## Troubleshooting

```bash
pkg update
pkg install terminus-game
```

Verify that the command is available with `command -v terminus-game`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

The game is licensed under the GNU General Public License v2.0. The vendored
upstream sources are unmodified and kept under `vendor/terminus/` together with
their original license. See `LICENSE` and `vendor/terminus/LICENSE.md`.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
