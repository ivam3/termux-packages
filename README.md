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
| [acccheck](packages/acccheck/README.md) | Windows SMB Password Dictionary Attack Tool |
| [adbfastboot](packages/adbfastboot/README.md) | Versatile command-line tool that facilitates a variety of device actions |
| [aguila-lang](packages/aguila-lang/README.md) | Aguila programming language (Spanish syntax, Rust speed) for Termux |
| [aircrack-ng](packages/aircrack-ng/README.md) | Wi-Fi security auditing and monitoring suite |
| [amass](packages/amass/README.md) | In-depth Attack Surface Mapping and Asset Discovery |
| [androidsdk-cli](packages/androidsdk-cli/README.md) | Official command line Integrated Development Environment (IDE) for Android app development |
| [antigravity-cli](packages/antigravity-cli/README.md) | Official Antigravity CLI with real-time VA39 memory patching for Termux |
| [apktool](packages/apktool/README.md) | command-line tool used for reverse engineering Android application package (APK) |
| [appshark](packages/appshark/README.md) | An static taint analysis platform to scan vulnerabilities in an Android app |
| [argus](packages/argus/README.md) | All-in-one Python-powered toolkit for information gathering and reconnaissance |
| [axmlprinter2](packages/axmlprinter2/README.md) | Prints XML document from binary XML file (with correct namespace handing & attribute formatting) |
| [azure-cli](packages/azure-cli/README.md) | Set of commands used to create and manage Azure resources |
| [beef](packages/beef/README.md) | powerful and intuitive security tool focuses on leveraging browser vulnerabilities to assess the security posture of a target |
| [binwalk](packages/binwalk/README.md) | Tool for analyzing, reverse engineering and extracting firmware images. |
| [bitb](packages/bitb/README.md) | Phishing technique that simulates a browser window within the browser to spoof a legitimate domain. |
| [botgram](packages/botgram/README.md) | Telegram group scraper and CLI utility for member, comment and post data |
| [burpsuite](packages/burpsuite/README.md) | Graphical tool for performing security testing of web applications |
| [cactus](packages/cactus/README.md) | Hybrid edge-cloud AI engine for mobile: on-device LLM/VLM/speech inference (Cactus Engine), quantization, kernels and CLI |
| [cewl](packages/cewl/README.md) | Custom word lists spidering a targets website |
| [claude-code](packages/claude-code/README.md) | Agentic AI coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands |
| [cloudbunny](packages/cloudbunny/README.md) | Capture the real IP of the server that uses a WAF as a proxy or protection |
| [code-server](packages/code-server/README.md) | VS Code with Nodejs development environment running on a remote server |
| [codebuff](packages/codebuff/README.md) | AI coding assistant that edits your codebase through natural language instructions (Native glibc version for Termux) |
| [converter](packages/converter/README.md) | Easy multimedia file converter |
| [cryptovenom](packages/cryptovenom/README.md) | Test the user credentials provided on several popular websites to see if the password has been reused on any of them |
| [deepseek-harness](packages/deepseek-harness/README.md) | DeepSeek Harness (`dsh`): AI coding agent with a local web interface; native glibc Node.js runtime for Termux |
| [dex2jar](packages/dex2jar/README.md) | Toolkit to work with android .dex and java .class files |
| [dnsenum](packages/dnsenum/README.md) | Enumerate DNS information |
| [DoS-A-Tool](packages/DoS-A-Tool/README.md) | Performs denial of service attacks under the SYN Flood method |
| [embed](packages/embed/README.md) | Embed metasploit payload into a legtim APK |
| [engram](packages/engram/README.md) | Persistent memory system for AI coding agents. Agent-agnostic Go binary with SQLite + FTS5, MCP server, HTTP API, CLI, and TUI. |
| [enum4linux](packages/enum4linux/README.md) | Linux alternative to enum.exe for enumerating data from Windows and Samba hosts |
| [enum4linux-ng](packages/enum4linux-ng/README.md) | A next generation version of enum4linux (a Windows/Samba enumeration tool) with additional features like JSON/YAML export |
| [evilginx2](packages/evilginx2/README.md) | Standalone man-in-the-middle attack framework used for phishing login credentials along with session cookies, allowing for the bypass of 2-factor authentication. |
| [exif](packages/exif/README.md) | Extract information (meta data) from files. |
| [exploitdb](packages/exploitdb/README.md) | The official [Exploit Database](https://www.exploit-db.com) repository |
| [finalrecon](packages/finalrecon/README.md) | All In One Web Recon. |
| [freebuff](packages/freebuff/README.md) | AI coding assistant that edits your codebase through natural language instructions. A buffcode free version with ad-supported — no subscription, no credits, no configuration (Native glibc version for Termux) |
| [fuzzdb](packages/fuzzdb/README.md) | Dictionary of attack patterns and primitives for black-box application fault injection and resource discovery |
| [geo-recon](packages/geo-recon/README.md) | An OSINT CLI tool desgined to fast track IP Reputation and Geo-locaton look up for Security Analysts. |
| [getadusers](packages/getadusers/README.md) | Gather data about the domain's users and their corresponding email addresses |
| [getnpusers](packages/getnpusers/README.md) | Attempt to list and get TGTs for those users that have the property 'Do not require Kerberos preauthentication' set |
| [getuserspns](packages/getuserspns/README.md) | Try to find Service Principal Names that are associated with normal user account. |
| [ghidra](packages/ghidra/README.md) | A software reverse engineering (SRE) framework with Ghidra 12.1.4 and native ARM64 decompiler support for Termux. |
| [ghost](packages/ghost/README.md) | Android post-exploitation framework that exploits the Android Debug Bridge to remotely access an Android device. |
| [ghunt](packages/ghunt/README.md) | An OSINT offensive Google framework. |
| [git-filter-repo](packages/git-filter-repo/README.md) | Quickly rewrite git repository history (filter-branch replacement). |
| [gobuster](packages/gobuster/README.md) | Directory/File, DNS and VHost busting tool written in Go |
| [gophish](packages/gophish/README.md) | Open-Source advance phishing toolkit |
| [hashcat](packages/hashcat/README.md) | World's fastest and most advanced password recovery utility |
| [hasher](packages/hasher/README.md) | Hash cracker with auto detect hash |
| [hashid](packages/hashid/README.md) | Software to identify the different types of hashes used to encrypt data and especially passwords. |
| [hatcloud](packages/hatcloud/README.md) | Make bypass in CloudFlare for discover real IP. |
| [hcdecryptor](packages/hcdecryptor/README.md) | Decryptor for HTTP Custom, HTTP Injector, APK Custom, eProxy, NapsternetV and SocksHTTP-based configuration files |
| [herdr](packages/herdr/README.md) | the runtime your coding agents live on - static binary for Termux (installs to $PREFIX/bin via postinst, always latest stable) |
| [hermes-agent](packages/hermes-agent/README.md) | Personal AI agent by Nous Research with CLI, TUI, messaging gateway, and browser automation. |
| [huggingface](packages/huggingface/README.md) | Client library for the Hugging Face Hub (huggingface_hub): download, publish and version AI models/datasets; provides the 'huggingface-cli' tool |
| [hydra-gtk](packages/hydra-gtk/README.md) | Number one brute forcing tool in ciber security. |
| [infoga](packages/infoga/README.md) | Gathering email accounts informations from different public source and check if emails was leaked using haveibeenpwned.com API. |
| [ipgeolocation](packages/ipgeolocation/README.md) | A tool to retrieve IP Geolocation information. |
| [johntheripper](packages/johntheripper/README.md) | Advanced offline password cracker, which supports hundreds of hash and cipher types, and runs on many operating systems, CPUs, GPUs, and even some FPGAs. |
| [jython-lts](packages/jython-lts/README.md) | Jython LTS 2.7.4 for Termux; the official Termux `jython` package is separate. |
| [kerbrute](packages/kerbrute/README.md) | An script to perform kerberos bruteforcing by using the Impacket library. |
| [maltego](packages/maltego/README.md) | Maltego is a software focused mainly on forensic analysis and developed to make link analysis and data mining more conducive from IP domains, emails, telephones, geographic locations... that is, the starting point of an investigation. |
| [markdown-viewer](packages/markdown-viewer/README.md) | A lightweight application developed using the Python programming language and the flet module. |
| [metasploit-framework](packages/metasploit-framework/README.md) | World's leading open-source penetrating framework |
| [mimikatz](packages/mimikatz/README.md) | Mini shell to control a remote mimikatz RPC server. |
| [mimocode](packages/mimocode/README.md) | An open-source AI coding agent with cross-session memory. Built for the terminal (Native glibc version for Termux). |
| [mistral-vibe](packages/mistral-vibe/README.md) | Minimal CLI coding assistant/agent powered by Mistral's models (Native glibc version for Termux). |
| [muse-code](packages/muse-code/README.md) | Meta Muse Code interactive terminal AI coding agent. |
| [ngrok](packages/ngrok/README.md) | Globally distributed reverse proxy fronting your web services running in any cloud or private network, or your machine. |
| [nikto](packages/nikto/README.md) | A web server scanner. |
| [ntlmrelayx](packages/ntlmrelayx/README.md) | Impacket ntlmrelayx tool to perform NTLM relay attacks (SMB, HTTP, LDAP, MSSQL, WinRM, etc.). |
| [omniroute](packages/omniroute/README.md) | Smart AI Router with 160+ providers, auto-fallback and OpenAI-compatible APIs (Termux-native) |
| [openclaw](packages/openclaw/README.md) | Open-source autonomous artificial intelligence agent. |
| [opencode](packages/opencode/README.md) | A powerful AI coding agent. Built for the terminal patching for Termux. |
| [opencode-v2](packages/opencode-v2/README.md) | OpenCode v2 AI coding agent (native glibc, coexists with opencode v1). |
| [openjdk-21](packages/openjdk-21/README.md) | Java development kit and runtime. |
| [osintgram](packages/osintgram/README.md) | A OSINT tool on Instagram. It offers an interactive shell to perform analysis on Instagram account of any users by its nickname. |
| [ovh-ttyrec](packages/ovh-ttyrec/README.md) | Terminal recorder and player (an alternative of ttyrec). |
| [penelope](packages/penelope/README.md) | A powerful shell handler built as a modern netcat replacement for RCE exploitation, aiming to simplify, accelerate, and optimize post-exploitation workflows. |
| [phonesploit](packages/phonesploit/README.md) | A tool for remote ADB exploitation for all Machines. |
| [playwright-proot](packages/playwright-proot/README.md) | Playwright CLI for Termux via proot-distro Ubuntu. Enables browser automation (snapshot, screenshot, click, fill) for testing PWAs and web apps on Android |
| [polenum](packages/polenum/README.md) | Extracts the password policy information from a Windows machine using the Impacket library |
| [proroot](packages/proroot/README.md) | Rootless Linux runtime for Android. Drop-in proot replacement with zero ptrace overhead. Run full glibc Linux userspace (Node.js, Python, Git, Chromium) inside Android without root. |
| [putty](packages/putty/README.md) | PuTTY graphical SSH, Telnet, Rlogin and serial-console client |
| [quack](packages/quack/README.md) | Toolkit with SMS attack tool, HTTP attack tool and many other attack tools. |
| [rea](packages/rea/README.md) | Reverse engineering agent CLI for binaries, Android apps, JavaScript and web apps, with automatic Ghidra 12.1.x native analysis and MCP agent setup. |
| [recon-ng](packages/recon-ng/README.md) | Open Source Intelligence gathering tool aimed at reducing the time spent harvesting information from open sources. |
| [recondog](packages/recondog/README.md) | Reconnaissance Swiss Army Knife |
| [routersploit](packages/routersploit/README.md) | Open-source exploitation framework dedicated to embedded devices. |
| [seclists](packages/seclists/README.md) | SecLists it's a collection of multiple types of lists used during security assessments, collected in one place. |
| [shc](packages/shc/README.md) | The Shell Script Compiler (SHC) encodes and encrypts shell scripts into executable binaries. |
| [sherlock](packages/sherlock/README.md) | Hunt down social media accounts by username across social networks. |
| [slowhttptest](packages/slowhttptest/README.md) | A highly configurable tool that simulates some Application Layer Denial of Service attacks by prolonging HTTP connections in different ways. |
| [stegsnow](packages/stegsnow/README.md) | Hide messages in ASCII text by appending whitespaces to the end of lines |
| [sublist3r](packages/sublist3r/README.md) | Fast subdomains enumeration tool for penetration testers. |
| [terminus-game](packages/terminus-game/README.md) | Terminal port of Terminus, a Linux learning adventure game. |
| [termux-desktop-bspwm](packages/termux-desktop-bspwm/README.md) | Meta-package and default configs for a bspwm tiling desktop on termux-x11. |
| [termux-desktop-xfce](packages/termux-desktop-xfce/README.md) | Set up a beautiful xfce desktop on termux-x11. |
| [termux-docker-qemu](packages/termux-docker-qemu/README.md) | Manage Docker containers from Linux VMs (x86/x86_64/ARMv7/AArch64) using QEMU. Includes VirtIO-GPU acceleration via virgl. |
| [termux-oracle-skill](packages/termux-oracle-skill/README.md) | Termux skill for AI coding agents with all context about termux, i-Haklab and Ivam3 termux-packages. |
| [unshc](packages/unshc/README.md) | The Shell Script UnCompiler (UNSHC) decode and decrypt SHC file on X86/x64 architecture. |
| [vulnx](packages/vulnx/README.md) | An intelligent bot auto shell injector that detects vulnerabilities in multiple types of cms. |
| [walkie](packages/walkie/README.md) | P2P communication CLI for AI agents. No server. No setup. Just talk. Termux adaptation with netlink/SELinux patch for Android. |
| [websploit](packages/websploit/README.md) | MITM framework. |
| [whatweb](packages/whatweb/README.md) | Recognises web technologies including content management systems (CMS), blogging platforms, statistic/analytics packages, JavaScript libraries, web servers, and embedded devices. |
| [wpscan](packages/wpscan/README.md) | WordPress security scanner. |
| [xapt-management](https://github.com/ivam3/xapt-management) | Tkinter graphical frontend for APT on Termux |
| [xleak](packages/xleak/README.md) | A fast terminal Excel viewer with an interactive TUI |
| [xml2axml](packages/xml2axml/README.md) | Encoding xml to axml OR decoding axml to xml |
| [zaproxy](packages/zaproxy/README.md) | The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications |
| [zcode](packages/zcode/README.md) | AI vibe coding harness (GLM-5.3) native glibc aarch64 for termux-x11 |

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
