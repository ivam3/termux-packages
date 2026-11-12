# cactus

> Hybrid edge-cloud AI engine for mobile devices: on-device LLM/VLM/speech inference (Cactus Engine), quantization, kernels and CLI.

## Overview

This package provides `cactus` for Termux. It is maintained as part of the i-HakLab package collection.

## Upstream source

- **Source:** [https://github.com/cactus-compute/cactus](https://github.com/cactus-compute/cactus)

## Installation

```bash
pkg update
pkg install cactus
```

## Requirements

python, python-pip, huggingface, git, cmake, build-essential, binutils, pkg-config, libcurl, rust, python-numpy, python-pillow, python-torch, python-torchvision, python-scipy, python-tokenizers, termux-elf-cleaner

## Usage

```text
cactus auth <pat|hf>                authenticate against Hugging Face / Cactus
cactus download <model>             download a model
cactus list                         list cached models
cactus run <model>                  run a model (for example Cactus-Compute/needle)
cactus transcribe <model> --file f  transcribe speech
cactus serve <model> --port 8080    start an OpenAI-compatible API
cactus convert <HF model>           convert weights
cactus build --python               rebuild the native engine
```

The package keeps its runtime data under `~/.local/share/cactus`:

| Path | Purpose |
|---|---|
| `~/.local/share/cactus` | Runtime root |
| `~/.local/share/cactus/cactus-engine/build/libcactus_engine.so` | Native engine |
| `~/.local/share/cactus/weights` | Downloaded model weights |
| `~/.local/share/cactus/build.log` | Build log |

## Package details

| Field | Value |
|---|---|
| Package | `cactus` |
| Version | `2.0.1-3` |
| Architecture | `all` |
| Maintainer | Ivam3 <https://t.me/Ivam3_Bot> |
| Source | [https://github.com/cactus-compute/cactus](https://github.com/cactus-compute/cactus) |
| Dependencies | python, python-pip, huggingface, git, cmake, build-essential, binutils, pkg-config, libcurl, rust, python-numpy, python-pillow, python-torch, python-torchvision, python-scipy, python-tokenizers, termux-elf-cleaner |
| Suggests | i-haklab |

## Troubleshooting

```bash
pkg update
pkg install cactus
```

Verify that the command is available with `command -v cactus`. If the package was recently installed, open a new shell so the updated `PATH` is loaded.

## License

See the upstream source for the license terms that apply to this package and its bundled sources.

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem, a cybersecurity and pentesting toolkit for Android/Termux.

```bash
pkg install i-haklab
```
