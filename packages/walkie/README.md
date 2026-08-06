# walkie

> P2P communication CLI for AI agents. No server. No setup. Just talk.

## Installation

```bash
pkg install walkie
```

## Info

| Field | Value |
|-------|-------|
| Version | `1.5.0` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [walkie](https://github.com/vikasprogrammer/walkie) |

## Dependencies

`nodejs, git, curl`

## Usage

```bash
walkie chat <channel>                 # Interactive chat
walkie agent <channel> --cli claude   # AI agent that listens and responds
walkie pair <channel> --task "..."    # Two agents collaborate (brain + executor)
walkie connect <channel>              # Join a channel programmatically
walkie send <channel> "msg"           # Send a message
walkie read <channel> --wait          # Read pending messages
walkie watch <channel> --exec CMD     # Trigger a script per message
walkie leave <channel>                # Leave a channel
walkie web                            # Web UI at localhost:3000
walkie status                         # Show channels and peers
walkie stop                           # Stop the background daemon
```

Same channel name = same room. Use `channel:secret` for private channels.

### Any AI agent with `walkie agent --cli`

Upstream walkie only accepts `--cli claude` / `--cli codex`. This package
applies a patch (`lib/patch-agents.js`, idempotent) that relaxes the check and
injects a generic runner, so any agent CLI can power `walkie agent`:

```bash
walkie agent ops:secret --cli vibe
walkie agent ops:secret --cli agy --agent-args "-p"
walkie agent ops:secret --cli opencode
walkie agent ops:secret --cli qwen-code
walkie agent ops:secret --cli codex --skip-git-repo-check   # codex fuera de un repo git
```

**Local AI with Ollama** — if a local Ollama server is running
(`http://127.0.0.1:11434`, override with `OLLAMA_HOST`), use it as the agent:

```bash
walkie agent ops:secret --cli ollama --model qwen2.5-coder:1.5b
walkie agent ops:secret --cli ollama                        # auto-detect local model
walkie pair ops:secret --brain ollama --exec-cli ollama --model qwen2.5-coder:1.5b
```

The Ollama runner keeps a rolling conversation history in memory, so the local
LLM has context across messages. Model resolution: `--model` → `OLLAMA_MODEL`
→ first local model → `qwen2.5-coder:1.5b`.

Known invocation registry (prompt flag per agent):

| CLI | Args |
|-----|------|
| `agy` | `-p` |
| `vibe` | `-p --output text` |
| `opencode` | `run` |
| `gemini`, `qwen`, `qwen-code`, `mimo`, `mimocode`, `kilo`, `kilocode`, `minimax`, `mmx` | `-p` |
| `copilot`, `copilot-cli`, `codebuff`, `freebuff`, `hermes`, `openclaw` | (prompt posicional, subcomando vía `--agent-args`) |
| `ollama` | (local LLM via HTTP API, no CLI) |
| cualquier otro | `<cli> <prompt>` (fallback genérico) |

`walkie pair` also benefits via `--brain` / `--exec-cli`. `claude`/`codex` keep
their dedicated runners untouched.

Note: on Termux, node-based CLIs (`gemini`, `qwen`, `copilot`, ...) may fail
to spawn because their shebang is `#!/usr/bin/env` (which doesn't exist on
Android). A wrapper in `~/.local/bin/<cli>` fixes them, like the existing one
for `codex`.

## Android / Termux note

Android SELinux blocks `bind()` on `AF_NETLINK` for non-root apps, which
prevents udx-native from watching network interfaces. The package applies a
patch that degrades gracefully to `interfaces=[]`. The daemon keeps working;
local IP falls back to `127.0.0.1` (LAN shortcut and network-change detection
are disabled, WAN discovery still works).

## Installation mode

By default walkie is installed **locally** (isolated in
`~/.local/share/walkie`), so it cannot affect any other globally installed
npm package. If the local install fails on some device architecture
(prebuild conflict, permissions, etc.), `postinst` automatically falls back
to a **global** install (`${PREFIX}/lib/node_modules`).

- Default: local (recommended, zero impact on other tools).
- Automatic fallback: local fails → global.
- Force global: `WALKIE_INSTALL_GLOBAL=1 dpkg --configure -a` (or reinstall
  with `pkg reinstall walkie` after setting the env var).
- The launcher `/data/data/com.termux/files/usr/bin/walkie` works with both
  modes; it just points to whichever install exists.

## Version note

walkie is installed from the git main branch (v1.5.0), which includes
`chat`, `agent` and `pair` — these commands are not yet published to npm
(npm latest is 1.4.0). To use the stable npm release instead, reinstall with:

```bash
WALKIE_USE_140=1 pkg reinstall walkie
```

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```
