# ntlmrelayx

> Impacket ntlmrelayx — tool to perform NTLM relay attacks (SMB, HTTP, LDAP, MSSQL, WinRM, etc.).

## Overview

This package provides `ntlmrelayx` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/fortra/impacket](https://github.com/fortra/impacket)

## Installation

```bash
pkg update
pkg install ntlmrelayx
```

## Requirements

python, python-pip, curl

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

The script is installed at `~/.local/share/ntlmrelayx/ntlmrelayx.py`, and `impacket` is installed with pip.

## Package details

| Field | Value |
|---|---|
| Package | `ntlmrelayx` |
| Version | `0.13.1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/fortra/impacket](https://github.com/fortra/impacket) |
| Dependencies | python, python-pip, curl |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install ntlmrelayx
```

Verify that the command is available with `command -v ntlmrelayx`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
