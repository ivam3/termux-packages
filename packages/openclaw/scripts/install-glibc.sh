#!/usr/bin/env bash
# install-glibc.sh - Install glibc-runner (L2 conditional)
# Extracted from install-glibc-env.sh — glibc runtime only, no Node.js.
# Called by orchestrator when config.env PLATFORM_NEEDS_GLIBC=true.
#
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

OPENCLAW_DIR="$HOME/.openclaw-android"
GLIBC_LDSO="$PREFIX/glibc/lib/ld-linux-aarch64.so.1"
PACMAN_CONF="$PREFIX/etc/pacman.conf"

echo "=== Installing glibc Runtime ==="
echo ""

# ── Pre-checks ───────────────────────────────

if [ -z "${PREFIX:-}" ]; then
    echo -e "${RED}[FAIL]${NC} Not running in Termux (\$PREFIX not set)"
    exit 1
fi

ARCH=$(uname -m)
if [ "$ARCH" != "aarch64" ]; then
    echo -e "${RED}[FAIL]${NC} glibc environment requires aarch64 (got: $ARCH)"
    exit 1
fi

# ── Install supplementary glibc libraries (always runs) ──
# glibc-runner provides core libraries but not all libraries that
# third-party binaries may need (e.g., libcap.so.2 for codex-acp).
# This runs on both fresh install and update to ensure libraries are current.

GLIBC_LIB_DIR="$PREFIX/glibc/lib"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLIBC_LIBS_SRC="$SCRIPT_DIR/../patches_bak/glibc-libs"

if [ -d "$GLIBC_LIB_DIR" ] && [ -d "$GLIBC_LIBS_SRC" ]; then
    for lib in "$GLIBC_LIBS_SRC"/*.so.*; do
        [ -f "$lib" ] || continue
        filename=$(basename "$lib")
        soname=$(echo "$filename" | sed -E 's/^(lib[^.]+\.so\.[0-9]+)\..*/\1/')
        if [ ! -f "$GLIBC_LIB_DIR/$filename" ]; then
            cp "$lib" "$GLIBC_LIB_DIR/$filename"
            [ "$soname" != "$filename" ] && ln -sf "$filename" "$GLIBC_LIB_DIR/$soname"
            echo -e "${GREEN}[OK]${NC}   Installed $soname"
        fi
    done
fi

# ── Ensure glibc /etc/hosts exists (always runs) ──
# glibc's getaddrinfo reads $PREFIX/glibc/etc/hosts for localhost resolution.
# Neither glibc nor glibc-runner packages include this file; it comes from
# resolv-conf (via openssl-glibc) which may not be installed.
# Without it, dns.lookup('localhost') can return 0.0.0.0 → gateway bind failure.

GLIBC_ETC="$PREFIX/glibc/etc"
if [ -d "$GLIBC_ETC" ] && [ ! -f "$GLIBC_ETC/hosts" ]; then
    cat > "$GLIBC_ETC/hosts" <<'HOSTS'
127.0.0.1 localhost localhost.localdomain
::1 localhost ip6-localhost ip6-loopback
HOSTS
    echo -e "${GREEN}[OK]${NC}   Created glibc /etc/hosts"
fi

# Check if already installed
if [ -f "$OPENCLAW_DIR/.glibc-arch" ] && [ -x "$GLIBC_LDSO" ]; then
    echo -e "${GREEN}[SKIP]${NC} glibc-runner already installed"
    exit 0
fi

# ── Step 2: Initialize pacman ─────────────────

echo ""
echo "Initializing pacman..."
echo "  (This may take a few minutes for GPG key generation)"

# SigLevel workaround: Some devices have a GPGME crypto engine bug
# that prevents signature verification. Temporarily set SigLevel = Never.
SIGLEVEL_PATCHED=false
if [ -f "$PACMAN_CONF" ]; then
    if ! grep -q "^SigLevel = Never" "$PACMAN_CONF"; then
        cp "$PACMAN_CONF" "${PACMAN_CONF}.bak"
        sed -i 's/^SigLevel\s*=.*/SigLevel = Never/' "$PACMAN_CONF"
        SIGLEVEL_PATCHED=true
        echo -e "${YELLOW}[INFO]${NC} Applied SigLevel = Never workaround (GPGME bug)"
    fi
fi

# Initialize pacman keyring (may hang on low-entropy devices)
pacman-key --init 2>/dev/null || true
pacman-key --populate 2>/dev/null || true

# ── Step 3: Install glibc-runner ──────────────

echo ""
echo "Installing glibc-runner..."

# --assume-installed: these packages are provided by Termux's apt but pacman
# doesn't know about them, causing dependency resolution failures
if pacman -Sy glibc-runner --noconfirm --assume-installed bash,patchelf,resolv-conf 2>&1; then
    echo -e "${GREEN}[OK]${NC}   glibc-runner installed"
else
    echo -e "${RED}[FAIL]${NC} Failed to install glibc-runner"
    if [ "$SIGLEVEL_PATCHED" = true ] && [ -f "${PACMAN_CONF}.bak" ]; then
        mv "${PACMAN_CONF}.bak" "$PACMAN_CONF"
    fi
    exit 1
fi

# Restore SigLevel after successful install
if [ "$SIGLEVEL_PATCHED" = true ] && [ -f "${PACMAN_CONF}.bak" ]; then
    mv "${PACMAN_CONF}.bak" "$PACMAN_CONF"
    echo -e "${GREEN}[OK]${NC}   Restored pacman SigLevel"
fi

# ── Verify ────────────────────────────────────

if [ ! -x "$GLIBC_LDSO" ]; then
    echo -e "${RED}[FAIL]${NC} glibc dynamic linker not found at $GLIBC_LDSO"
    exit 1
fi
echo -e "${GREEN}[OK]${NC}   glibc dynamic linker available"

if command -v grun &>/dev/null; then
    echo -e "${GREEN}[OK]${NC}   grun command available"
else
    echo -e "${YELLOW}[WARN]${NC} grun command not found (will use ld.so directly)"
fi

# ── Create marker file ────────────────────────

mkdir -p "$OPENCLAW_DIR"
touch "$OPENCLAW_DIR/.glibc-arch"
echo -e "${GREEN}[OK]${NC}   glibc architecture marker created"

echo ""
echo -e "${GREEN}glibc runtime installed successfully.${NC}"
echo "  ld.so: $GLIBC_LDSO"
