# xapt-management

Tkinter graphical frontend for APT on Termux. The package installs the upstream
Xapt 2.0.0 source in `~/.local/share/xapt-management` and provides the
`xapt-management` launcher plus the historical `xapt` alias.

Xapt is intentionally GUI-only. The `apt` command remains the authoritative
command-line interface.

## Requirements

- Termux with the X11 repository enabled.
- `python` and `python-tkinter`.
- An X11 server such as Termux:X11 or Xwayland.
- A desktop environment (Xfce, Fluxbox, OpenBox, LXQt, MATE, bspwm, etc.).

`x11-repo` and `python-tkinter` are declared as recommended packages because
`python-tkinter` is published in the X11 repository. Enable that repository
before installing Xapt:

```bash
pkg install x11-repo
pkg update
pkg install python-tkinter
```

The `preinst` script verifies `x11-repo`, `x11.list` and Tkinter. If any is
missing, it stops with the exact commands to run instead of letting APT report
an opaque `unmet dependencies` error. The package never writes
`x11.list` itself; `x11-repo` owns the mirror and keyring configuration.

## Install

```bash
pkg install xapt-management
```

The post-install script clones the upstream repository and removes the old 1.x
layout from `$PREFIX/share/applications/xapt` when present. The upstream source
lives in:

```text
~/.local/share/xapt-management/
├── main.py
├── xapt_core.py
├── requirements.txt
└── .deb/
```

## Run

```bash
xapt
# or
xapt-management
```

Start Termux:X11 first and verify that `DISPLAY` is set:

```bash
echo "$DISPLAY"
xapt
```

## Package layout

```text
packages/xapt-management/
├── manifest.json
├── xapt-management          # launcher installed into $PREFIX/bin
├── xapt-management.desktop  # desktop entry
├── img/xapt-management.png  # menu icon
├── preinst
├── postinst
├── prerm
└── postrm
```

The desktop entry is installed under
`$PREFIX/share/applications/xapt-management/` and the icon under
`$PREFIX/share/applications/xapt-management/img/`.

## Build the .deb

From the `termux-packages` repository:

```bash
cd packages/xapt-management
termux-create-package manifest.json
```

The generated package is `xapt-management_2.0.0_all.deb`. Move it to the
repository root only when you are ready to regenerate the APT index.

## Behavior

- The Xapt window lists packages from the real Termux `apt`/`apt-cache`.
- Search accepts a package name or summary text.
- Filters: all packages, installed, and upgradable.
- Details, dependencies, and installed files appear in separate tabs.
- Install, remove, purge, update, upgrade, autoremove, clean, hold and unhold
  actions are available.
- A running operation can be cancelled, including its APT process group.
- The search toolbar stays visible in landscape/short windows; the details and
  log panes shrink first.

## Upstream

- Repository: <https://github.com/ivam3/xapt-management>
- README: <https://github.com/ivam3/xapt-management/blob/main/README.md>
- Package index: <https://github.com/ivam3/termux-packages>

## License

GNU. See the upstream [LICENSE](https://github.com/ivam3/xapt-management/blob/main/LICENSE).
