# androidsdk-cli

> Android SDK command line tools: sdkmanager, avdmanager, and apkanalyzer for managing Android SDK components from the terminal.

## Installation

```bash
pkg install androidsdk-cli
```

## Info

| Field | Value |
|-------|-------|
| Version | `22.0` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [Android Tools](https://developer.android.com/tools) |

## Dependencies

`curl, unzip, aapt, apksigner, adbfastboot, gradle, openjdk-21`

## Usage

```bash
androidsdk-cli
```

> The postinst downloads Android SDK Command-Line Tools 22.0, installs `platforms;android-36` + `build-tools;36.0.0`, accepts licenses and adds `JAVA_HOME`/`ANDROID_SDK_ROOT` to your shell config. The sdkmanager/avdmanager/apkanalyzer binaries are available in `~/.local/share/androidsdk-cli/cmdline-tools/latest/bin/`. Run `androidsdk-cli` to see the available commands.

> [!NOTE]
> cmdline-tools 23.0+ ships a native `android` binary compiled for x86-64 which does not run on Termux (aarch64). Version 22.0 is the latest whose `sdkmanager` is pure Java and therefore supported on Android/Termux.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```