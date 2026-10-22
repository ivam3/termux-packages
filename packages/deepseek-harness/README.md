# deepseek-harness

> DeepSeek Harness (`dsh`) — AI coding harness. Native glibc Node.js runtime adapted for Termux.

## Installation

```bash
pkg install deepseek-harness
```

## Usage

```bash
dsh web --no-open
```

Open `http://127.0.0.1:3080` in the Android browser.

Other profiles:

```bash
dsh headless
dsh sdk
dsh acp
```

## Layout

| Field | Value |
|-------|-------|
| Package | `deepseek-harness` |
| Command | `dsh` |
| Architecture | `aarch64` |
| Node.js | `24.22.1` (linux-arm64, glibc) |
| dsh | `0.2.1-rc.2` |
| User data | `~/.dsh` |
| Runtime | `~/.local/share/deepseek-harness` |

## Notes

- The package uses the Termux glibc loader; it does not replace the system Node.js.
- `dsh-npm`, `dsh-npx` and `dsh-pnpm` use the isolated glibc runtime.
- `dsh web` binds to `127.0.0.1:3080`; use `--no-open` because Termux has no desktop browser opener.
- On removal, `~/.dsh` is preserved. Use `pkg purge deepseek-harness` to delete it.
