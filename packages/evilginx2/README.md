# evilginx2

> Standalone man-in-the-middle attack framework used for phishing login credentials along with session cookies, allowing for the bypass of 2-factor authentication.

## Installation

```bash
pkg install evilginx2
```

## Info

| Field | Value |
|-------|-------|
| Version | `3.3.0` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [evilginx2](https://github.com/kgretzky/evilginx2) |

## Dependencies

`git, golang, make, curl`

## Usage

```bash
evilginx2 [options]
```

Evilginx2 es compilado desde el código fuente (no hay binarios precompilados para `aarch64`) y se instala en `~/.local/share/evilginx2`. Los phishlets de la comunidad se descargan a `~/.local/share/evilginx2/phishlets` y se cargan automáticamente al lanzar el shell interactivo:

```bash
evilginx2
> config domain example.com
> phishlets enable office365
> phishlets get-url office365
> sessions
```

La configuración y las sesiones capturadas se guardan en `~/.evilginx`.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```