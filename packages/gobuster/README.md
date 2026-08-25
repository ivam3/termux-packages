# gobuster

> Directory/File, DNS and VHost busting tool written in Go.

## Installation

```bash
pkg install gobuster
```

## Info

| Field | Value |
|-------|-------|
| Version | `3.8.2` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [gobuster](https://github.com/OJ/gobuster) |

## Dependencies

`golang`

## Usage

```bash
gobuster dir -u http://example.com -w wordlist.txt
gobuster dns -d example.com -w subdomains.txt
gobuster vhost -u http://example.com -w vhosts.txt
```

Gobuster se compila desde el código fuente con `go install github.com/OJ/gobuster/v3@v3.8.2` y el binario queda en `~/.local/bin` / `~/go/bin`.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```