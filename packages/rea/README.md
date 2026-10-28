# rea

Reverse engineering agent CLI for binaries, Android apps, JavaScript and web apps.

This package installs `rea-agents` 6.8.0 for Termux through npm and exposes the
`rea` command. The application itself runs on the Termux Node.js runtime.

Installation also installs the shared REA skill and registers the MCP server in
every supported agent that is already present. A small Termux entrypoint wrapper
applies the platform shim and Ghidra environment to `rea setup` and MCP
registrations, so agents launched outside the `rea` launcher still work.

## Installation

```bash
pkg install rea
```

The package installs `rea-agents` during `postinst`, so an internet connection is
required the first time it is installed or upgraded. During the same step it
detects supported agents and configures them automatically.

To skip agent setup during installation:

```bash
REA_SKIP_AGENT_SETUP=1 pkg install rea
```

For Ghidra-backed native analysis, install the companion package:

```bash
pkg install ghidra
```

After installing or updating an agent later, rerun the setup helper:

```bash
rea-setup
```

## Usage

```bash
rea --version
rea doctor --json
rea mcp doctor --json
rea
```

`rea doctor --json` is read-only and reports the providers available on this
device. It exits non-zero when a required check fails, so use `jq` when you only
want to inspect a specific provider. `rea mcp doctor --json` checks the MCP
server, tools and prompts.

`rea-setup` is idempotent. It installs or repairs the shared skill and runs
`rea setup --all-detected --yes`. `rea setup --client <name> --yes` remains
available for an existing client configuration.

On Termux, REA's setup uses hard links when publishing new files, which Android
rejects with `EACCES`. `rea-setup` works around this by copying the bundled skill
and pre-creating empty client configuration files before running REA's setup.

## Verification

After installing `ghidra`, verify the integration with:

```bash
rea doctor --json
rea mcp doctor --json
rea analyze /system/bin/toybox --provider ghidra --format json
rea decompile /system/bin/toybox main --provider ghidra --format json
```

The Ghidra provider checks should report `available: true`, the analysis profile
should name `ghidra` 12.1.x, and the decompile result should contain Ghidra
pseudocode. From the package source tree, the smoke test also covers this path:

```bash
bash packages/rea/rea-smoke-test.sh
```

## Layout

| Field | Value |
|-------|-------|
| Command | `rea` |
| Setup helper | `rea-setup` |
| Runtime | `~/.local/share/rea/app` |
| Launcher | `$PREFIX/bin/rea` |
| Entrypoint | `~/.local/share/rea/app/node_modules/rea-agents/scripts/rea.mjs` (wrapper) |
| User data | Preserved on removal |
| Fixer | `$PREFIX/bin/fixer` |

The runtime directory is separate from `~/.local/share/rea/hopper`, caches,
state, captures and Evidence files. Removing the package does not delete those
paths. The entrypoint wrapper sits at the same path used by earlier releases, so
existing MCP registrations keep working. It delegates to `rea-real.mjs`.

## Dependencies

The package depends on:

- `nodejs-lts` and `npm`
- `apktool` and `rizin`
- `procps` (`ps`)
- `curl` and `ca-certificates`
- `bash`, `coreutils` and `binutils`

`chromium`, `ghidra` and `i-haklab` are suggested. Install `ghidra` to enable
native analysis and `chromium` if you want to use browser observation.

## Supported providers

- JavaScript and Electron application analysis through the bundled Node runtime
- Ghidra 12.1.4 native analysis when the `ghidra` package is installed
- GNU `objdump`
- `rizin`
- `apktool`
- `adb` through `REA_ADB_PATH` or the default `PATH`
- Browser observation through CDP against an already-running Chromium-family
  browser

For `rizin`, GNU `objdump` and Ghidra commands, the `rea` launcher preloads a
small shim that reports `linux` instead of `android` to REA. This enables the
`/proc`-based process ownership those providers require and lets REA admit the
Termux arm64 Ghidra installation. The launcher auto-detects
`~/.local/share/ghidra` and exports `GHIDRA_INSTALL_DIR` when the variable is
not already set. It also selects `gobjdump` (GNU binutils) by default because
Termux's `objdump` command points to LLVM's `llvm-objdump`.

The entrypoint wrapper performs the same environment setup, and loads the shim
for `rea setup`, `rea mcp` and `rea --mcp`. This covers MCP servers that agents
start directly through the entrypoint instead of the launcher.

## Linux vs. Termux behavior

REA 6.8.0 treats Linux x86_64 as a supported host. This package runs the same
release on Android/arm64 (Termux), so behavior differs in three ways:

- **Host checks**: REA gates some integrations on `process.platform` and
  `process.arch`. Termux reports `android`/`arm64`.
- **The shim**: the launcher and the entrypoint wrapper make Rizin, GNU
  objdump and Ghidra-backed commands report `linux` so `/proc`-based process
  ownership works and REA admits the Termux arm64 Ghidra installation. The
  wrapper also shims `setup` and MCP startup. It does not change `arch`, and it
  is not applied to unrelated Android/Playwright/Electron/ADB commands.
- **Optional tools**: some integrations require tools or versions that are not
  packaged for Termux.

| Area | Linux x86_64 (configured) | Termux package |
| --- | --- | --- |
| Host report | `linux` / `x64` | `android` / `arm64`; shimmed provider commands report `linux` |
| Native analysis (Ghidra/Hopper/IDA) | Supported when the provider is configured | Ghidra 12.1.4 is supported through the `ghidra` package and the launcher shim; Hopper/IDA are not packaged |
| Android class/method analysis (JADX) | Supported on x64 with `REA_JADX_MCP_JAR` | Blocked by REA's x64 host gate; apktool-based decoding still works |
| Offline ELF layout / crash (pwntools) | Supported on Linux x64 | Blocked by the x64 host gate |
| JavaScript source recovery (Wakaru) | Supported on Linux x64 | Blocked by the x64 host gate |
| EVM interface inspection | Supported on Linux x64 | Blocked by the x64 host gate |
| Firmware extraction/inspection | Supported with Binwalk/Unblob + prlimit | Not enabled: the shim does not cover these commands; `binwalk` is installable, `unblob` is not packaged |
| Packet capture (TShark) | Supported with TShark 4.x + prlimit | Unavailable: TShark is not packaged; the pure-JS pcap lane is also blocked by the platform gate |
| Signal decoding (sigrok) | Supported with sigrok-cli 0.7.2 | Unavailable: sigrok-cli is not packaged |
| WASM inspection | Supported with WABT 1.0.42 | Supported after `pkg install wabt` and setting `REA_WABT_BIN_DIRECTORY` |
| Browser/Electron dynamic work | Playwright-managed browsers and CDP | CDP against an external Chromium; Playwright-managed downloads are not packaged |
| GDB sessions | Supported on Linux | Blocked by the Linux platform gate; the shim is not applied to GDB |
| Process capture | Supported on Linux | Unavailable: ownership capture is not enabled for Android |
| ADB operations | Supported with an adb client | Supported with an authorized device |
| macOS/Apple utilities | macOS only | Unavailable |

Commands whose behavior changes most visibly:

| Command | Linux x86_64 | Termux |
| --- | --- | --- |
| `rea doctor --json` | Reports the Linux host and configured providers | Reports the shimmed Linux host and Ghidra readiness when `ghidra` is installed |
| `rea execute-rizin-command` | Works | Works (shim) |
| `rea inspect-with-objdump` | Works | Works with `gobjdump` (shim) |
| `rea debug-with-gdb` | Works on Linux | Fails the platform gate |
| `rea inspect-android-package` | Works with JADX on x64 | Fails the x64 host gate |
| `rea inspect-binary-layout` | Works with pwntools on Linux x64 | Fails the x64 host gate |
| `rea analyze <ELF> --provider ghidra` | Works with Ghidra 12.1.x | Works after `pkg install ghidra` (shim) |
| `rea analyze-javascript-application` | Works | Works |
| `rea extract-firmware` | Works with Binwalk/Unblob | Fails the platform gate |
| `rea capture-process` | Works on Linux | Unavailable |

The shim does not spoof `process.arch`. Features that require an x64 host stay
unavailable on Termux even when the external tool is installed.

## Termux limitations

These limitations are enforced by REA 6.8.0, not by this package:

- **Ghidra**: install the `ghidra` package and run `rea doctor --json` to
  confirm the provider. The launcher auto-detects `~/.local/share/ghidra`,
  exports `GHIDRA_INSTALL_DIR`, and applies the Linux shim to Ghidra-backed
  commands. Override `GHIDRA_INSTALL_DIR` or `JAVA_HOME` in the environment if
  your installation lives elsewhere.
- **JADX**: REA requires its own `jadx-headless-mcp` jar through
  `REA_JADX_MCP_JAR`. The `jadx` package from apt is not used by this provider.
  The Android host check also blocks it in this release.
- **GDB**: persistent and one-shot GDB sessions are gated to
  `process.platform === "linux"` in this release. The launcher does not apply
  the Linux shim to GDB commands, so GDB remains unavailable here.
- **Hopper**: the installer expects `/etc/os-release`, which is not writable on
  Termux; the Hopper provider is unavailable.
- **Frida**: REA imports the Node.js `frida` bindings. There is no Android
  Node.js prebuild for this package, and the Python `frida` module does not
  satisfy the provider. The optional dependency is intentionally omitted.
- **Playwright browser launch**: CDP observation of an external browser is
  supported. Playwright-managed browser downloads are not part of this package.

## Browser observation

Start a Chromium-family browser with a loopback debugging port, then point REA
at it:

```bash
chromium --remote-debugging-port=9222 --user-data-dir="$HOME/.cache/rea/chromium"
rea doctor --json
```

Use `cdp_endpoint` with `http://127.0.0.1:9222` in the relevant REA command.
Do not expose the debugging port on a non-loopback interface.

## Script fixer

`postinst` installs the shared `fixer` helper in `$PREFIX/bin/fixer`. It is kept
on removal because other i-HakLab packages use it.

## Removal

```bash
pkg uninstall rea
```

This removes the launcher, `rea-setup` and the npm runtime. It preserves
`~/.local/share/rea/hopper`, REA caches, state, captures, Evidence files and the
`fixer` helper. MCP registrations and the installed skill are also left in
place; remove those from each agent if you no longer want REA available there.
Use REA's own cleanup commands if you also want to remove user data.
