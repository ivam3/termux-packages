# androidsdk-cli

> Android SDK command line tools: sdkmanager, avdmanager, and apkanalyzer for managing Android SDK components from the terminal.

## Overview

This package provides `androidsdk-cli` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://developer.android.com/tools](https://developer.android.com/tools)
- **Website:** [https://developer.android.com/studio/index.html#command-tools](https://developer.android.com/studio/index.html#command-tools)

## Installation

```bash
pkg update
pkg install androidsdk-cli
```

## Requirements

curl, unzip, aapt, apksigner, adbfastboot, gradle, openjdk-21

## Usage

```bash
androidsdk-cli
```

> The postinst downloads Android SDK Command-Line Tools 22.0, installs `platforms;android-36` + `build-tools;36.0.0`, accepts licenses and adds `JAVA_HOME`/`ANDROID_SDK_ROOT` to your shell config. The sdkmanager/avdmanager/apkanalyzer binaries are available in `~/.local/share/androidsdk-cli/cmdline-tools/latest/bin/`. Run `androidsdk-cli` to see the available commands.

> [!NOTE]
> cmdline-tools 23.0+ ships a native `android` binary compiled for x86-64 which does not run on Termux (aarch64). Version 22.0 is the latest whose `sdkmanager` is pure Java and therefore supported on Android/Termux.

## Package details

| Field | Value |
|---|---|
| Package | `androidsdk-cli` |
| Version | `22.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://developer.android.com/tools](https://developer.android.com/tools) |
| Website | [https://developer.android.com/studio/index.html#command-tools](https://developer.android.com/studio/index.html#command-tools) |
| Dependencies | curl, unzip, aapt, apksigner, adbfastboot, gradle, openjdk-21 |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install androidsdk-cli
```

Verify that the command is available with `command -v androidsdk-cli`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
