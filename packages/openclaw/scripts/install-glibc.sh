#!/usr/bin/env bash
# install-glibc.sh - Install glibc-runner (L2 conditional)
# Extracted from install-glibc-env.sh — glibc runtime only, no Node.js.
# Called by orchestrator when config.env PLATFORM_NEEDS_GLIBC=true.
#
# What it does:
#   1. Initialize pacman and glibc-runner 
#   2. Verify glibc dynamic linker
#   3. Create marker file
set -euo pipefail
OPENCLAW_DIR="${HOME}/.openclaw-android"
GLIBC_LDSO="$PREFIX/glibc/lib/ld-linux-aarch64.so.1"
PACMAN_CONF="$PREFIX/etc/pacman.conf"
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
NC='\033[0m'

ARCH=$(uname -m)
if [ "$ARCH" != "aarch64" ]; then
    echo -e "${RED}[FAIL]${NC} glibc environment requires aarch64 (got: $ARCH)"
    exit 1
fi

# Check if already installed
if [ -f "$OPENCLAW_DIR/.glibc-arch" ] && [ -x "$GLIBC_LDSO" ]; then
    echo -e "${GREEN}[SKIP]${NC} glibc-runner already installed"
    exit 0
fi

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
