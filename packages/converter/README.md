# converter

> Easy multimedia file converter for Termux.

## Overview

`converter` is a small command-line frontend for converting audio and video
files between common formats. The Termux package is distributed as a prebuilt
Debian package (`converter_2.0_all.deb`) and is maintained by Ivam3 for the
i-HakLab repository.

The application source is maintained privately by its original author. Package
updates and source changes are delegated to that author; this repository only
publishes the packaged artifact.

## Upstream source

- **Reference project:** [miluxmil/milux converter](https://github.com/miluxmil/milux/blob/master/converter)
- **Source availability:** Private; maintained by the original author.
- **Package maintainer:** Ivam3

## Installation

```bash
pkg update
pkg install converter
```

## Requirements

The package depends on the multimedia tools used by the converter. Install
`ffmpeg` if the package does not pull it automatically:

```bash
pkg install ffmpeg
```

## Usage

```bash
converter --help
```

Typical workflow:

```bash
converter input.mp4 output.mkv
converter input.wav output.mp3
```

The exact supported formats and options depend on the installed multimedia
backend. Run `converter --help` to see the options exposed by the current
package.

## Package details

| Field | Value |
|---|---|
| Package | `converter` |
| Version | `2.0` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Reference upstream | [miluxmil/milux converter](https://github.com/miluxmil/milux/blob/master/converter) |
| Source status | Private, maintained by the original author |
| Dependencies | Multimedia backend (for example, `ffmpeg`) |

## Notes

- This is a binary-only package. The source is not included in this repository.
- Do not redistribute or reverse engineer the package without the author's
  permission.
- If you need a feature or a fix, contact the package maintainer so the request
  can be forwarded to the original author.

## Troubleshooting

```bash
pkg update
pkg install ffmpeg
command -v converter
converter --help
```

If the command is missing, reinstall the package and open a new shell:

```bash
pkg install --reinstall converter
```

## License

See the original author's terms. The package is redistributed with permission
for the i-HakLab repository.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab)
ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
