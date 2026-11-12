# huggingface

> Client library for the Hugging Face Hub (huggingface_hub): download, publish and version AI models/datasets; provides the 'huggingface-cli' tool.

## Overview

This package provides `huggingface` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/huggingface/huggingface_hub](https://github.com/huggingface/huggingface_hub)

## Installation

```bash
pkg update
pkg install huggingface
```

## Requirements

python, python-pip

## Usage

The package provides the `huggingface-cli` command and the `huggingface_hub`
Python library.

```bash
huggingface-cli login
huggingface-cli whoami
huggingface-cli download <model>
huggingface-cli upload <model> <path>
```

```python
from huggingface_hub import snapshot_download

snapshot_download("org/model")
```

Termux uses classic HTTP downloads because the optional `hf-xet` accelerator
has no Termux wheel and is not compatible with Python 3.14. The package sets
`HF_HUB_DISABLE_XET=1` through `etc/profile.d/huggingface.sh`.

## Notes

See the official documentation at https://huggingface.co/docs/huggingface_hub for the complete Python and CLI reference.

## Package details

| Field | Value |
|---|---|
| Package | `huggingface` |
| Version | `1.27.0-1` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/huggingface/huggingface_hub](https://github.com/huggingface/huggingface_hub) |
| Dependencies | python, python-pip |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install huggingface
```

Verify that the command is available with `command -v huggingface-cli`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
