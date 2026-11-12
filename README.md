# Termux Packages

### for i-HakLab

[![GitHub stars](https://img.shields.io/github/stars/ivam3/termux-packages?style=flat-square)](https://github.com/ivam3/termux-packages/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/ivam3/termux-packages?style=flat-square)](https://github.com/ivam3/termux-packages/issues)
[![License](https://img.shields.io/badge/license-GNU-blue?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.html)
[![DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ivam3/termux-packages)

This repository provides easy and fast access to tools and frameworks from the
[i-HakLab](https://github.com/ivam3/i-Haklab) cybersecurity and pentesting
laboratory for Android under [Termux](https://github.com/termux/termux-app).

The packages are published through a signed APT repository, so they can be
installed and updated with the same package manager used by Termux.

## Quick start

Add the repository and its signing key:

```bash
pkg install gnupg
mkdir -p $PREFIX/etc/apt/sources.list.d
curl -s https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/ivam3-termux-packages.list \
  -o $PREFIX/etc/apt/sources.list.d/ivam3-termux-packages.list
curl -fsSL "https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/docs/dists/stable/public_key.gpg" \
  | gpg --dearmor | tee "$PREFIX/etc/apt/trusted.gpg.d/ivam3.gpg" >/dev/null
pkg update
```

Or use the one-line installer:

```bash
yes | pkg install gnupg && mkdir -p $PREFIX/etc/apt/sources.list.d && curl -s https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/ivam3-termux-packages.list -o $PREFIX/etc/apt/sources.list.d/ivam3-termux-packages.list && curl -fsSL "https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/docs/dists/stable/public_key.gpg" | gpg --dearmor | tee "$PREFIX/etc/apt/trusted.gpg.d/ivam3.gpg" >/dev/null && pkg update
```

Install a package by name:

```bash
pkg install acccheck
```

## Video tutorial

[![Termux packages installation tutorial](https://img.youtube.com/vi/wKg7dZ1zC2o/0.jpg)](https://youtu.be/wKg7dZ1zC2o)

## Available tools and frameworks

Each tool links to its own README with installation, usage, dependencies and
upstream attribution. The table is the package index; the individual README is
the source of truth for that package.

| Tool | Description |
|---|---|
| [i-HakLab](https://github.com/ivam3/i-Haklab) | Cybersecurity and pentesting laboratory for Termux |
| [acccheck](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/acccheck/README.md) | Windows SMB Password Dictionary Attack Tool |
| [adbfastboot](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/adbfastboot/README.md) | Versatile command-line tool that facilitates a variety of device actions |
| [aguila-lang](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/aguila-lang/README.md) | Aguila programming language (Spanish syntax, Rust speed) for Termux |
| [aircrack-ng](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/aircrack-ng/README.md) | Wi-Fi security auditing and monitoring suite |
| [amass](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/amass/README.md) | In-depth Attack Surface Mapping and Asset Discovery |
| [androidsdk-cli](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/androidsdk-cli/README.md) | Official command line Integrated Development Environment (IDE) for Android app development |
| [antigravity-cli](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/antigravity-cli/README.md) | Official Antigravity CLI with real-time VA39 memory patching for Termux |
| [apktool](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/apktool/README.md) | command-line tool used for reverse engineering Android application package (APK) |
| [appshark](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/appshark/README.md) | An static taint analysis platform to scan vulnerabilities in an Android app |
| [argus](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/argus/README.md) | All-in-one Python-powered toolkit for information gathering and reconnaissance |
| [axmlprinter2](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/axmlprinter2/README.md) | Prints XML document from binary XML file (with correct namespace handing & attribute formatting) |
| [azure-cli](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/azure-cli/README.md) | Set of commands used to create and manage Azure resources |
| [beef](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/beef/README.md) | powerful and intuitive security tool focuses on leveraging browser vulnerabilities to assess the security posture of a target |
| [binwalk](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/binwalk/README.md) | Tool for analyzing, reverse engineering and extracting firmware images. |
| [bitb](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/bitb/README.md) | Phishing technique that simulates a browser window within the browser to spoof a legitimate domain. |
| [botgram](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/botgram/README.md) | Telegram group scraper and CLI utility for member, comment and post data |
| [burpsuite](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/burpsuite/README.md) | Graphical tool for performing security testing of web applications |
| [cactus](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/cactus/README.md) | Hybrid edge-cloud AI engine for mobile: on-device LLM/VLM/speech inference (Cactus Engine), quantization, kernels and CLI |
| [cewl](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/cewl/README.md) | Custom word lists spidering a targets website |
| [claude-code](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/claude-code/README.md) | Agentic AI coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands |
| [cloudbunny](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/cloudbunny/README.md) | Capture the real IP of the server that uses a WAF as a proxy or protection |
| [code-server](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/code-server/README.md) | VS Code with Nodejs development environment running on a remote server |
| [codebuff](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/codebuff/README.md) | AI coding assistant that edits your codebase through natural language instructions (Native glibc version for Termux) |
| [converter](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/converter/README.md) | Easy multimedia file converter |
| [cryptovenom](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/cryptovenom/README.md) | Test the user credentials provided on several popular websites to see if the password has been reused on any of them |
| [deepseek-harness](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/deepseek-harness/README.md) | DeepSeek Harness (`dsh`): AI coding agent with a local web interface; native glibc Node.js runtime for Termux |
| [dex2jar](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/dex2jar/README.md) | Toolkit to work with android .dex and java .class files |
| [dnsenum](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/dnsenum/README.md) | Enumerate DNS information |
| [DoS-A-Tool](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/DoS-A-Tool/README.md) | Performs denial of service attacks under the SYN Flood method |
| [embed](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/embed/README.md) | Embed metasploit payload into a legtim APK |
| [engram](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/engram/README.md) | Persistent memory system for AI coding agents. Agent-agnostic Go binary with SQLite + FTS5, MCP server, HTTP API, CLI, and TUI. |
| [enum4linux](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/enum4linux/README.md) | Linux alternative to enum.exe for enumerating data from Windows and Samba hosts |
| [enum4linux-ng](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/enum4linux-ng/README.md) | A next generation version of enum4linux (a Windows/Samba enumeration tool) with additional features like JSON/YAML export |
| [evilginx2](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/evilginx2/README.md) | Standalone man-in-the-middle attack framework used for phishing login credentials along with session cookies, allowing for the bypass of 2-factor authentication. |
| [exif](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/exif/README.md) | Extract information (meta data) from files. |
| [exploitdb](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/exploitdb/README.md) | The official [Exploit Database](https://www.exploit-db.com) repository |
| [finalrecon](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/finalrecon/README.md) | All In One Web Recon. |
| [freebuff](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/freebuff/README.md) | AI coding assistant that edits your codebase through natural language instructions. A buffcode free version with ad-supported — no subscription, no credits, no configuration (Native glibc version for Termux) |
| [fuzzdb](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/fuzzdb/README.md) | Dictionary of attack patterns and primitives for black-box application fault injection and resource discovery |
| [geo-recon](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/geo-recon/README.md) | An OSINT CLI tool desgined to fast track IP Reputation and Geo-locaton look up for Security Analysts. |
| [getadusers](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/getadusers/README.md) | Gather data about the domain's users and their corresponding email addresses |
| [getnpusers](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/getnpusers/README.md) | Attempt to list and get TGTs for those users that have the property 'Do not require Kerberos preauthentication' set |
| [getuserspns](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/getuserspns/README.md) | Try to find Service Principal Names that are associated with normal user account. |
| [ghidra](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/ghidra/README.md) | A software reverse engineering (SRE) framework with Ghidra 12.1.4 and native ARM64 decompiler support for Termux. |
| [ghost](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/ghost/README.md) | Android post-exploitation framework that exploits the Android Debug Bridge to remotely access an Android device. |
| [ghunt](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/ghunt/README.md) | An OSINT offensive Google framework. |
| [git-filter-repo](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/git-filter-repo/README.md) | Quickly rewrite git repository history (filter-branch replacement). |
| [gobuster](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/gobuster/README.md) | Directory/File, DNS and VHost busting tool written in Go |
| [gophish](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/gophish/README.md) | Open-Source advance phishing toolkit |
| [hashcat](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/hashcat/README.md) | World's fastest and most advanced password recovery utility |
| [hasher](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/hasher/README.md) | Hash cracker with auto detect hash |
| [hashid](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/hashid/README.md) | Software to identify the different types of hashes used to encrypt data and especially passwords. |
| [hatcloud](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/hatcloud/README.md) | Make bypass in CloudFlare for discover real IP. |
| [hcdecryptor](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/hcdecryptor/README.md) | Decryptor for HTTP Custom, HTTP Injector, APK Custom, eProxy, NapsternetV and SocksHTTP-based configuration files |
| [herdr](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/herdr/README.md) | the runtime your coding agents live on - static binary for Termux (installs to $PREFIX/bin via postinst, always latest stable) |
| [hermes-agent](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/hermes-agent/README.md) | Personal AI agent by Nous Research with CLI, TUI, messaging gateway, and browser automation. |
| [huggingface](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/huggingface/README.md) | Client library for the Hugging Face Hub (huggingface_hub): download, publish and version AI models/datasets; provides the 'huggingface-cli' tool |
| [hydra-gtk](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/hydra-gtk/README.md) | Number one brute forcing tool in ciber security. |
| [infoga](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/infoga/README.md) | Gathering email accounts informations from different public source and check if emails was leaked using haveibeenpwned.com API. |
| [ipgeolocation](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/ipgeolocation/README.md) | A tool to retrieve IP Geolocation information. |
| [johntheripper](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/johntheripper/README.md) | Advanced offline password cracker, which supports hundreds of hash and cipher types, and runs on many operating systems, CPUs, GPUs, and even some FPGAs. |
| [jython-lts](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/jython-lts/README.md) | Jython LTS 2.7.4 for Termux; the official Termux `jython` package is separate. |
| [kerbrute](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/kerbrute/README.md) | An script to perform kerberos bruteforcing by using the Impacket library. |
| [maltego](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/maltego/README.md) | Maltego is a software focused mainly on forensic analysis and developed to make link analysis and data mining more conducive from IP domains, emails, telephones, geographic locations... that is, the starting point of an investigation. |
| [markdown-viewer](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/markdown-viewer/README.md) | A lightweight application developed using the Python programming language and the flet module. |
| [metasploit-framework](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/metasploit-framework/README.md) | World's leading open-source penetrating framework |
| [mimikatz](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/mimikatz/README.md) | Mini shell to control a remote mimikatz RPC server. |
| [mimocode](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/mimocode/README.md) | An open-source AI coding agent with cross-session memory. Built for the terminal (Native glibc version for Termux). |
| [mistral-vibe](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/mistral-vibe/README.md) | Minimal CLI coding assistant/agent powered by Mistral's models (Native glibc version for Termux). |
| [muse-code](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/muse-code/README.md) | Meta Muse Code interactive terminal AI coding agent. |
| [ngrok](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/ngrok/README.md) | Globally distributed reverse proxy fronting your web services running in any cloud or private network, or your machine. |
| [nikto](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/nikto/README.md) | A web server scanner. |
| [ntlmrelayx](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/ntlmrelayx/README.md) | Impacket ntlmrelayx tool to perform NTLM relay attacks (SMB, HTTP, LDAP, MSSQL, WinRM, etc.). |
| [omniroute](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/omniroute/README.md) | Smart AI Router with 160+ providers, auto-fallback and OpenAI-compatible APIs (Termux-native) |
| [openclaw](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/openclaw/README.md) | Open-source autonomous artificial intelligence agent. |
| [opencode](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/opencode/README.md) | A powerful AI coding agent. Built for the terminal patching for Termux. |
| [opencode-v2](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/opencode-v2/README.md) | OpenCode v2 AI coding agent (native glibc, coexists with opencode v1). |
| [openjdk-21](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/openjdk-21/README.md) | Java development kit and runtime. |
| [osintgram](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/osintgram/README.md) | A OSINT tool on Instagram. It offers an interactive shell to perform analysis on Instagram account of any users by its nickname. |
| [ovh-ttyrec](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/ovh-ttyrec/README.md) | Terminal recorder and player (an alternative of ttyrec). |
| [penelope](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/penelope/README.md) | A powerful shell handler built as a modern netcat replacement for RCE exploitation, aiming to simplify, accelerate, and optimize post-exploitation workflows. |
| [phonesploit](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/phonesploit/README.md) | A tool for remote ADB exploitation for all Machines. |
| [playwright-proot](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/playwright-proot/README.md) | Playwright CLI for Termux via proot-distro Ubuntu. Enables browser automation (snapshot, screenshot, click, fill) for testing PWAs and web apps on Android |
| [polenum](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/polenum/README.md) | Extracts the password policy information from a Windows machine using the Impacket library |
| [proroot](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/proroot/README.md) | Rootless Linux runtime for Android. Drop-in proot replacement with zero ptrace overhead. Run full glibc Linux userspace (Node.js, Python, Git, Chromium) inside Android without root. |
| [putty](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/putty/README.md) | PuTTY graphical SSH, Telnet, Rlogin and serial-console client |
| [quack](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/quack/README.md) | Toolkit with SMS attack tool, HTTP attack tool and many other attack tools. |
| [rea](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/rea/README.md) | Reverse engineering agent CLI for binaries, Android apps, JavaScript and web apps, with automatic Ghidra 12.1.x native analysis and MCP agent setup. |
| [recon-ng](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/recon-ng/README.md) | Open Source Intelligence gathering tool aimed at reducing the time spent harvesting information from open sources. |
| [recondog](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/recondog/README.md) | Reconnaissance Swiss Army Knife |
| [routersploit](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/routersploit/README.md) | Open-source exploitation framework dedicated to embedded devices. |
| [seclists](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/seclists/README.md) | SecLists it's a collection of multiple types of lists used during security assessments, collected in one place. |
| [shc](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/shc/README.md) | The Shell Script Compiler (SHC) encodes and encrypts shell scripts into executable binaries. |
| [sherlock](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/sherlock/README.md) | Hunt down social media accounts by username across social networks. |
| [slowhttptest](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/slowhttptest/README.md) | A highly configurable tool that simulates some Application Layer Denial of Service attacks by prolonging HTTP connections in different ways. |
| [stegsnow](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/stegsnow/README.md) | Hide messages in ASCII text by appending whitespaces to the end of lines |
| [sublist3r](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/sublist3r/README.md) | Fast subdomains enumeration tool for penetration testers. |
| [terminus-game](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/terminus-game/README.md) | Terminal port of Terminus, a Linux learning adventure game. |
| [termux-desktop-bspwm](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/termux-desktop-bspwm/README.md) | Meta-package and default configs for a bspwm tiling desktop on termux-x11. |
| [termux-desktop-xfce](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/termux-desktop-xfce/README.md) | Set up a beautiful xfce desktop on termux-x11. |
| [termux-docker-qemu](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/termux-docker-qemu/README.md) | Manage Docker containers from Linux VMs (x86/x86_64/ARMv7/AArch64) using QEMU. Includes VirtIO-GPU acceleration via virgl. |
| [termux-oracle-skill](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/termux-oracle-skill/README.md) | Termux skill for AI coding agents with all context about termux, i-Haklab and Ivam3 termux-packages. |
| [unshc](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/unshc/README.md) | The Shell Script UnCompiler (UNSHC) decode and decrypt SHC file on X86/x64 architecture. |
| [vulnx](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/vulnx/README.md) | An intelligent bot auto shell injector that detects vulnerabilities in multiple types of cms. |
| [walkie](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/walkie/README.md) | P2P communication CLI for AI agents. No server. No setup. Just talk. Termux adaptation with netlink/SELinux patch for Android. |
| [websploit](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/websploit/README.md) | MITM framework. |
| [whatweb](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/whatweb/README.md) | Recognises web technologies including content management systems (CMS), blogging platforms, statistic/analytics packages, JavaScript libraries, web servers, and embedded devices. |
| [wpscan](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/wpscan/README.md) | WordPress security scanner. |
| [xapt-management](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/xapt-management/README.md) | Tkinter graphical frontend for APT on Termux (Xapt 2.0.0) |
| [xleak](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/xleak/README.md) | A fast terminal Excel viewer with an interactive TUI |
| [xml2axml](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/xml2axml/README.md) | Encoding xml to axml OR decoding axml to xml |
| [zaproxy](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/zaproxy/README.md) | The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications |
| [zcode](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/zcode/README.md) | AI vibe coding harness (GLM-5.3) native glibc aarch64 for termux-x11 |

> **Note:** The official Termux `jython` package is separate from this
> repository's `jython-lts` package. `putty` and `dos-a-tool` are the package
> names used by APT; their project names are PuTTY and DoS-A-Tool.

## Repository layout

```text
termux-packages/
├── packages/                 # Package sources, manifests and per-tool READMEs
│   ├── acccheck/
│   │   ├── manifest.json
│   │   └── README.md
│   └── ...
├── docs/                     # APT repository metadata
├── install.sh                # Repository installer
├── ivam3-termux-packages.list
└── README.md
```

Most packages contain a `manifest.json`, a wrapper or launcher, and a README.
Packages with a complex installation or runtime also include their own setup,
post-install and removal scripts.

## Package sources and attribution

Each package README documents the upstream project from which the package was
adapted. The upstream link is kept there rather than in this index, so the
package list remains focused on discovery and installation.

Some packages are binary-only redistributions maintained with permission from
their authors. Their READMEs state that the source is private and that updates
are delegated to the original author.

## Documentation

- [i-HakLab](https://github.com/ivam3/i-Haklab)
- [DeepWiki for this repository](https://deepwiki.com/ivam3/termux-packages)
- [Our website](https://ivam3.github.io)

## Contributing

1. Add or update the package under `packages/<name>/`.
2. Keep the package README in English and document the upstream source.
3. Test the package on Termux before opening a pull request.
4. Do not include credentials, private keys or generated build artifacts.

## Support

- Telegram: [@Ivam3_Bot](https://t.me/Ivam3_Bot)
- Community: [Ivam3byCinderella](https://ivam3.github.io/#/redes)
- Issues: [GitHub Issues](https://github.com/ivam3/termux-packages/issues)

## License

GNU. See the upstream license of each package for the terms that apply.

##### Follow me on [Socials Network](https://ivam3.github.io/#/redes)
