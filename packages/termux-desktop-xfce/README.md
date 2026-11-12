# termux-desktop-xfce

> Meta-package with data, themes, icons and wallpapers for an Xfce4 desktop environment on Termux.

## Overview

This package provides `termux-desktop-xfce` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/ivam3/termux-packages](https://github.com/ivam3/termux-packages)

## Installation

```bash
pkg update
pkg install termux-desktop-xfce
```

## Requirements

xfce4, adwaita-icon-theme, atk, binutils, dbus-glib, dconf, desktop-file-utils, dosbox, exo, feh, file-roller, firefox, findutils, fluent-gtk-theme, fluent-icon-theme, galculator, garcon, gcr, geany, geany-plugins, gnome-themes-extra, gsettings-desktop-schemas, gtk-update-icon-cache, gtk2-engines-murrine, gtk2, gtk3, gtksourceview4, gvfs, hicolor-icon-theme, htop, iso-codes, l3afpad, libcanberra, libepoxy, libfontenc, libhandy, libmatekbd, libnotify, libpciaccess, libvte, libwayland-protocols, libwayland, libwnck, libx11, libxcomposite, libxdamage, libxfce4ui, libxfce4util, libxfont2, libxinerama, libxkbfile, libxklavier, libxmu, libxslt, loqui, lxappearance, lxde-icon-theme, mousepad, mpv-x, mtpaint, neofetch, openjdk-21, papirus-icon-theme, parole, python, python-pip, python-tkinter, recordmydesktop, ristretto, sdl-net, sdl2, sdl, shared-mime-info, startup-notification, tar, termux-api, thunar-archive-plugin, thunar, tumbler, unzip, vim-gtk, webkit2gtk-4.1, wget, xarchiver, xapt-management, xcb-util, xfconf, xfdesktop, xfwm4, xkeyboard-config, xorg-iceauth, xorg-xauth, xorg-xhost, xorg-xkbcomp, xorg-xrdb, xwayland, zenity

This package is intended for the Termux X11 environment.

## Usage

```bash
desktop
```

`desktop` starts the Xfce4 session on Termux:X11. Install the matching desktop
packages and start a Termux:X11 session first. The i-HakLab command
`i-Haklab desktop` is the supported launcher in the i-HakLab environment.

## Suggestions

Also install: `burpsuite`, `ghidra`, `hydra`, `putty`, `maltego`, `zaproxy`

## Package details

| Field | Value |
|---|---|
| Package | `termux-desktop-xfce` |
| Version | `1.0.15` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/ivam3/termux-packages](https://github.com/ivam3/termux-packages) |
| Dependencies | xfce4, adwaita-icon-theme, atk, binutils, dbus-glib, dconf, desktop-file-utils, dosbox, exo, feh, file-roller, firefox, findutils, fluent-gtk-theme, fluent-icon-theme, galculator, garcon, gcr, geany, geany-plugins, gnome-themes-extra, gsettings-desktop-schemas, gtk-update-icon-cache, gtk2-engines-murrine, gtk2, gtk3, gtksourceview4, gvfs, hicolor-icon-theme, htop, iso-codes, l3afpad, libcanberra, libepoxy, libfontenc, libhandy, libmatekbd, libnotify, libpciaccess, libvte, libwayland-protocols, libwayland, libwnck, libx11, libxcomposite, libxdamage, libxfce4ui, libxfce4util, libxfont2, libxinerama, libxkbfile, libxklavier, libxmu, libxslt, loqui, lxappearance, lxde-icon-theme, mousepad, mpv-x, mtpaint, neofetch, openjdk-21, papirus-icon-theme, parole, python, python-pip, python-tkinter, recordmydesktop, ristretto, sdl-net, sdl2, sdl, shared-mime-info, startup-notification, tar, termux-api, thunar-archive-plugin, thunar, tumbler, unzip, vim-gtk, webkit2gtk-4.1, wget, xarchiver, xapt-management, xcb-util, xfconf, xfdesktop, xfwm4, xkeyboard-config, xorg-iceauth, xorg-xauth, xorg-xhost, xorg-xkbcomp, xorg-xrdb, xwayland, zenity |
| Suggests | i-haklab, burpsuite, ghidra, hydra, putty, maltego, zaproxy |

## Troubleshooting

```bash
pkg update
pkg install termux-desktop-xfce
```

Verify that the command is available with `command -v desktop`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
