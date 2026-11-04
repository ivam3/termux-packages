# Mistral Vibe (mistral-vibe)

Mistral Vibe is Mistral AI's terminal coding assistant. This package installs
the official standalone Linux build for Termux aarch64/x86_64; it does not
compile Rust extensions on the device.

## Installation

```bash
apt install mistral-vibe
```

The package requires a working `glibc-repo` installation. The standalone
binary is installed in `$PREFIX/lib/mistral-vibe` and exposed as `vibe`.

## Usage

```bash
export MISTRAL_API_KEY="your-key"
vibe
```

Useful options:

```bash
vibe --help
vibe --setup
vibe -p "describe this repository"
```

Configuration is stored in `~/.vibe`.

## Notes

- No `uv` or `pip` build is performed during installation.
- `vibe-acp` is not included in the standalone CLI build; use the official
  upstream release if you need ACP mode.
- The standalone build version is pinned to the release selected by `updateAIpkg`.

## Help

```bash
i-Haklab about mistral-vibe
```

---

*Integrated into the i-Haklab ecosystem.*
