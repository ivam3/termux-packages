# termux-desktop-bspwm

> Meta-package and default configuration for a bspwm tiling desktop on Termux:X11.

## Overview

This package installs and configures a lightweight bspwm desktop for
Termux:X11. It includes a launcher, keyboard shortcuts, polybar, picom, kitty,
rofi and a set of default applications.

The package is intended for Termux X11 sessions and provides a complete starting
point that can be customized through the generated configuration files.

## Upstream source

- **Package source:** [ivam3/termux-packages](https://github.com/ivam3/termux-packages)
- **bspwm upstream:** [baskerville/bspwm](https://github.com/baskerville/bspwm)

## Installation

```bash
pkg update
pkg install termux-desktop-bspwm
```

Start a Termux:X11 session and launch the desktop with:

```bash
startbspwm
```

## Requirements

- `x11-repo`
- `termux-x11-nightly`
- `bspwm`, `sxhkd`, `kitty`, `rofi`, `polybar`, `picom`
- `tint2`, `dmenu`, `feh`, `xorg-xsetroot`, `xfce4-screenshooter`
- `dbus`, `firefox`, `thunar`, `mousepad`, `pulseaudio`
- `glow`, `papirus-icon-theme`, `hicolor-icon-theme`, `unzip`, `fontconfig`

## Usage

```bash
startbspwm
```

The desktop starts bspwm, sxhkd, picom, polybar and the wallpaper helper. Use
`super` (the Windows/Command key) as the main modifier. If your keyboard does
not send `super` to Termux:X11, use the `alt` alternatives listed below.

## 1. What is bspwm?

**bspwm** is a tiling window manager based on binary space partitioning. Unlike
a floating desktop such as Xfce, windows automatically share the screen and are
controlled with the keyboard. There are no minimize, maximize or close buttons
by default; use the shortcuts instead (`super+w` closes a window, `super+m`
toggles monocle mode and `super+f` toggles fullscreen).

## 2. What is sxhkd?

**sxhkd** (*Simple X Hotkey Daemon*) reads keyboard shortcuts from
`~/.config/sxhkd/sxhkdrc` and runs `bspc` commands or applications. bspwm does
not provide its own shortcut daemon, so sxhkd must be running for the keyboard
bindings to work.

> **Note:** `super` is the Windows/logo key or Command (⌘) on a Mac. If your
> keyboard does not forward it to Termux:X11, use the `alt` fallback column.

## 3. Installed components

| Component | Package | Description |
|---|---|---|
| **bspwm** | `bspwm` | Main tiling window manager. |
| **sxhkd** | `sxhkd` | Keyboard shortcut daemon. |
| **kitty** | `kitty` | Primary GPU-accelerated terminal with transparency. |
| **xfce4-terminal** | `xfce4-terminal` | Fallback terminal. |
| **rofi** | `rofi` | Application and command launcher (gruvbox-dark-hard theme). |
| **polybar** | `polybar` | Top bar with desktops, CPU, RAM, battery, WiFi, clock and volume. |
| **picom** | `picom` | Compositor for transparency and vsync. |
| **dmenu** | `dmenu` | Generic menu and rofi fallback. |
| **feh** | `feh` | Wallpaper manager. |
| **xsetroot** | `xorg-xsetroot` | Normal cursor and solid-color fallback. |

## 4. Window and desktop management

Two desktops are configured (`I`–`II`). Firefox is assigned to desktop `II`.

### Split the screen between windows

1. Open the first application; it fills the desktop.
2. Preselect a side with `super+ctrl+h/j/k/l` (a border preview appears).
3. Open the second application; it is placed on the selected side.
4. Adjust the split ratio with `super+ctrl+5` (50%), `super+ctrl+7` (70%), and
   so on.

## 5. Keyboard shortcuts

### Applications and session

| Shortcut | `alt` fallback | Description |
|---|---|---|
| `super+Return` | `alt+Return` | Open kitty. |
| `super+shift+Return` | — | Open the xfce4-terminal fallback. |
| `super+space` | `alt+space` | Open rofi (applications). |
| `super+shift+space` | — | Open rofi (commands). |
| `super+Escape` | — | Reload sxhkd shortcuts. |
| `super+shift+q` | `alt+shift+q` | Exit bspwm (closes the session, not X11). |
| `super+shift+r` | — | Restart bspwm. |
| `Print` | — | Take a screenshot with xfce4-screenshooter. |

### Windows: closing and states

| Shortcut | Description |
|---|---|
| `super+w` | Close the focused window. |
| `super+shift+w` | Force-kill the focused window. |
| `super+m` | Toggle tiled/monocle mode (maximize). |
| `super+t` / `super+shift+t` / `super+s` / `super+f` | Tiled / pseudo-tiled / floating / fullscreen. |
| `super+g` | Swap with the largest window. |
| `super+y` | Send the marked node to the preselected node. |

### Focus and movement (`h`=left, `j`=down, `k`=up, `l`=right)

| Shortcut | Description |
|---|---|
| `super+h/j/k/l` | Move focus in that direction. |
| `super+shift+h/j/k/l` | Move the focused window in that direction. |
| `super+c` / `super+shift+c` | Next / previous window on the desktop. |
| `super+Tab` | Last focused window. |
| `super+o` / `super+i` | Focus history (back / forward). |
| `super+p/b/,/.` | Focus by jump (parent, brother, first, second). |

### Desktops (I–II)

| Shortcut | Description |
|---|---|
| `super+1..2` | Go to desktop N. |
| `super+shift+1..2` | Move the focused window to desktop N. |
| `super+[` / `super+]` | Previous / next desktop. |
| `super+grave` | Last desktop. |

### Node flags

| Shortcut | Description |
|---|---|
| `super+ctrl+m` | Mark a node. |
| `super+ctrl+x` | Lock a node. |
| `super+ctrl+y` | Sticky (visible on every desktop). |
| `super+ctrl+z` | Private. |

### Preselection (manual split)

| Shortcut | Description |
|---|---|
| `super+ctrl+h/j/k/l` | Preselect a direction for the next application. |
| `super+ctrl+1..9` | Preselect a ratio (0.1–0.9). |
| `super+ctrl+space` | Cancel the node preselection. |
| `super+ctrl+shift+space` | Cancel the desktop preselection. |

### Move and resize

| Shortcut | Description |
|---|---|
| `super+alt+h/j/k/l` | Expand the window toward that side. |
| `super+alt+shift+h/j/k/l` | Shrink the window. |
| `super+arrow keys` | Move a floating window (20 px). |

## 6. Essential `bspc` commands

These commands work from any terminal with `DISPLAY=:0`:

| Command | Description |
|---|---|
| `bspc query -D --names` | List desktops. |
| `bspc query -N` | List open window IDs. |
| `bspc rule -l` | List per-application rules. |
| `bspc config border_width` | Show the current value of an option. |
| `bspc config window_gap 16` | Change the window gap at runtime. |
| `bspc wm -r` | Restart bspwm and reload `bspwmrc`. |
| `pkill -USR1 -x sxhkd` | Reload `sxhkdrc` without restarting. |
| `pkill -SIGUSR1 -x kitty` | Reload `kitty.conf` in open terminals. |

## 7. Configuration layout

- `~/.config/bspwm/bspwmrc`: desktops, borders, gaps, rules and autostart
  (sxhkd, wallpaper, picom, polybar).
- `~/.config/bspwm/wallpaper.jpg`: default wallpaper (see section 10).
- `~/.config/sxhkd/sxhkdrc`: all keyboard shortcuts (section 5).
- `~/.config/polybar/config.ini`: bar and modules. `launch.sh` waits for the
  socket and exports `BSPWM_SOCKET`. `battery.sh` and `wifi.sh` use Termux:API.
- `~/.config/picom/picom.conf`: compositor settings; log at
  `~/.config/picom/picom.log`.
- `~/.config/kitty/kitty.conf`: terminal settings (section 8).
- `~/.config/rofi/config.rasi`: rofi settings. The theme is selected on the
  command line with `-theme` (section 9).
- `~/bin/startbspwm`: desktop launcher.

## 8. Terminal (kitty)

| Option | Value | Description |
|---|---|---|
| `font_family` | `Hack Nerd Font Mono` | Font with icon support. |
| `font_size` | `15.0` | Font size; decimals are accepted. |
| `background_opacity` | `0.92` | Subtle transparency; requires picom. |
| `dynamic_background_opacity` | `yes` | `ctrl+shift+a` toggles solid/transparent. |
| `cursor_shape` | `beam` | Bar cursor. |
| `scrollback_lines` | `5000` | Scrollback per terminal. |
| `copy_on_select` | `yes` | Copy text when selected. |
| `confirm_os_window_close` | `0` | Close without confirmation (`super+w`). |

## 9. System options (bspwmrc + polybar)

### bspwm (`bspwmrc`)

| Option | Value | Description |
|---|---|---|
| `border_width` | `2` | Window border width. |
| `window_gap` | `12` | Gap between windows. |
| `split_ratio` | `0.52` | Automatic split ratio. |
| `borderless_monocle` | `true` | No border in monocle mode. |
| `gapless_monocle` | `true` | No gap in monocle mode. |
| `focused_border_color` | `#7aa2f7` | Active window border. |
| `normal_border_color` | `#3b4261` | Inactive window border. |
| `focus_follows_pointer` | `true` | Focus follows the mouse pointer. |

### polybar (`config.ini`)

| Module | Type | Description |
|---|---|---|
| `bspwm` | internal | Desktops I–II (click to switch). Requires `BSPWM_SOCKET`, set by `launch.sh`. |
| `cpu` / `memory` | internal | Percentage, refreshed every 2–3 seconds. |
| `battery` | script | `battery.sh` uses Termux:API every 30 seconds. The internal module does not work on Android because of SELinux. |
| `wifi` | script | `wifi.sh` uses Termux:API every 15 seconds. `internal/network` is denied by netlink restrictions. |
| `date` | internal | `%H:%M %d/%m`. |
| `pulseaudio` | internal | Volume. Requires `XDG_RUNTIME_DIR=$TMPDIR`, set by `launch.sh`. |
| `font-0/1` | — | `monospace:size=15`. If you increase the font size, increase `height` (38) as well. |

## 10. Manual configuration guide

### Change the wallpaper

```sh
cp /path/to/image.jpg ~/.config/bspwm/wallpaper.jpg
DISPLAY=:0 feh --no-fehbg --bg-fill ~/.config/bspwm/wallpaper.jpg
```

`bspwmrc` always uses that file, or a solid color if it is missing.

### Change the terminal font and size

Edit `~/.config/kitty/kitty.conf` (`font_family`, `font_size`) and reload
without closing the terminals:

```sh
pkill -SIGUSR1 -x kitty
```

### Change transparency

Set `background_opacity 0.85` in `kitty.conf`; lower values are more
transparent. Press `ctrl+shift+a` to toggle at runtime. If kitty reports
`Failed to enable transparency`, picom is not running:

```sh
pgrep -x picom || (DISPLAY=:0 picom -b --log-file ~/.config/picom/picom.log &)
```

### Change the polybar font

Edit `font-0`/`font-1` in `config.ini`, adjust `height`, then restart polybar:

```sh
DISPLAY=:0 XDG_RUNTIME_DIR=$TMPDIR bash ~/.config/polybar/launch.sh
```

### Add a shortcut

1. Open `~/.config/sxhkd/sxhkdrc`.
2. Add a block, for example `super+d` for Thunar:

```text
super + d
	thunar &
```

3. Reload with `super+Escape` or `pkill -USR1 -x sxhkd`.

### Add a per-application rule

Add the rule to `bspwmrc` (for example, keep Telegram floating) and apply it
with `bspc wm -r`:

```sh
bspc rule -a TelegramDesktop state=floating
```

Find the window class with `xprop | grep WM_CLASS` and click the window.

## Package details

| Field | Value |
|---|---|
| Package | `termux-desktop-bspwm` |
| Version | `0.1.1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [ivam3/termux-packages](https://github.com/ivam3/termux-packages) |
| Website | [baskerville/bspwm](https://github.com/baskerville/bspwm) |
| Dependencies | `x11-repo`, `termux-x11-nightly`, `bspwm`, `sxhkd`, `kitty`, `rofi`, `polybar`, `picom`, `tint2`, `dmenu`, `feh`, `xorg-xsetroot`, `xfce4-screenshooter`, `dbus`, `firefox`, `thunar`, `mousepad`, `pulseaudio`, `glow`, `papirus-icon-theme`, `hicolor-icon-theme`, `unzip`, `fontconfig` |
| Suggests | `i-haklab` |

## Troubleshooting

```bash
pkg update
pkg install x11-repo termux-x11-nightly bspwm sxhkd kitty rofi polybar picom tint2 dmenu feh xorg-xsetroot xfce4-screenshooter dbus firefox thunar mousepad pulseaudio glow papirus-icon-theme hicolor-icon-theme unzip fontconfig
startbspwm
```

If the desktop does not start, verify that the Termux:X11 session is running
and that `DISPLAY` is set. Check the logs for `bspwm`, `sxhkd`, `picom` and
`polybar` in the terminal where the session was started.

## License

See the upstream sources for the license terms that apply to bspwm, sxhkd and
the bundled configuration files.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab)
ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
