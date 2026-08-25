# ntlmrelayx

> Impacket ntlmrelayx — tool to perform NTLM relay attacks (SMB, HTTP, LDAP, MSSQL, WinRM, etc.).

## Installation

```bash
pkg install ntlmrelayx
```

## Info

| Field | Value |
|-------|-------|
| Version | `0.13.1` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [impacket](https://github.com/fortra/impacket) |

## Dependencies

`python, python-pip, curl`

## Usage

```bash
ntlmrelayx [options]
```

Relay NTLM authentication from SMB/HTTP to various protocols:

```bash
ntlmrelayx -t smb://192.168.1.10 -tf targets.txt
ntlmrelayx -t ldap://dc.example.com --delegate-access
ntlmrelayx -t mssql://server --dump-shares
ntlmrelayx -tf targets.txt -smb2support
```

El script se instala en `~/.local/share/ntlmrelayx/ntlmrelayx.py` y `impacket` se instala vía pip.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```