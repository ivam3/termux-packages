# terminus-game

Terminal port of [Terminus](https://github.com/mprat/Terminus), the Linux
learning adventure game by Michele Pratusevich. Explore a text world and learn
`cd`, `ls`, `less`, `pwd`, `cp`, `mv`, `rm`, `grep`, `touch` and `sudo` while
solving the game's puzzles.

The upstream JavaScript game logic is vendored unchanged and executed with
Node.js; only the browser terminal has been replaced with a native CLI.
Vendored from commit `a62d0e53f77bc53d0b1941e6baf89403ed25a129`.

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

## License

The game is licensed under the GNU General Public License v2.0. The vendored
upstream sources are unmodified and kept under `vendor/terminus/` together with
their original license. See `LICENSE` and `vendor/terminus/LICENSE.md`.
