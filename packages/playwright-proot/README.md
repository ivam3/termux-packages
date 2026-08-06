# playwright-proot

> Playwright CLI for Termux via **proroot** (Ubuntu 24.04 rootless runtime). Full browser automation (Chromium) running inside a proroot glibc container.

## Installation

```bash
apt install playwright-proot
```

## Info

| Field | Value |
|-------|-------|
| Version | `1.62.0` |
| Architecture | `aarch64` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [playwright.dev](https://playwright.dev) |

## Dependencies

`proroot, curl, tar`

## Usage

```bash
playwright-proot run <comandos>     Ejecuta comandos en una sola sesion
playwright-proot open [url]         Sesion interactiva (Chromium headless en :9222)
playwright-proot close              Detiene Chromium
playwright-proot help               Ayuda
```

Ejemplos:

```bash
playwright-proot run "snapshot; screenshot --filename=p.png"
echo "goto http://localhost:8550; snapshot" | playwright-proot run
playwright-proot open http://localhost:8550
playwright-proot close
```

Funciona en modo headless (sin X11/Wayland).

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```
