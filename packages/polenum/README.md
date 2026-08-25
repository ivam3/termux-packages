# polenum

> Polenum extracts the password policy information from a Windows machine. Uses the Impacket library.

## Installation

```bash
pkg install polenum
```

## Info

| Field | Value |
|-------|-------|
| Version | `2025.03.01` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [polenum](https://github.com/Wh1t3Fox/polenum) |

## Dependencies

`python, python-pip, curl`

## Usage

```bash
polenum [options]
```

Extrae la política de contraseñas de una máquina Windows usando la librería Impacket:

```bash
polenum -u <username> -p <password> -d <domain/ip>
polenum user:password@127.0.0.1
```

El script se instala en `~/.local/share/polenum/polenum.py` y `impacket` se instala vía pip.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```