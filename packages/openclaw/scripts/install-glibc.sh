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

# ── Supplementary glibc libraries ─────────────
# glibc-runner provides core libraries but not all libraries that
# third-party binaries may need (e.g., libcap.so.2 for codex-acp).
# Called after glibc is present, both on fresh install and on update.

GLIBC_LIB_DIR="$PREFIX/glibc/lib"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GLIBC_LIBS_SRC="$SCRIPT_DIR/../runtime-assets/glibc-libs"

install_supplementary_libs() {
    [ -d "$GLIBC_LIB_DIR" ] && [ -d "$GLIBC_LIBS_SRC" ] || return 0

    local lib filename soname
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
}

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
if [ -x "$GLIBC_LDSO" ]; then
    mkdir -p "$OPENCLAW_DIR"
    install_supplementary_libs
    touch "$OPENCLAW_DIR/.glibc-arch"
    echo -e "${GREEN}[SKIP]${NC} glibc-runner already installed"
    exit 0
fi

# ── Step 2: Initialize pacman ─────────────────

echo ""
echo "Initializing pacman..."

if ! command -v pacman >/dev/null 2>&1; then
    echo -e "${RED}[FAIL]${NC} pacman not found"
    exit 1
fi

if [ ! -f "$PACMAN_CONF" ]; then
    echo -e "${RED}[FAIL]${NC} pacman config not found at $PACMAN_CONF"
    exit 1
fi

mkdir -p "${TMPDIR:-$PREFIX/tmp}"
PACMAN_TMP_CONF="$(mktemp "${TMPDIR:-$PREFIX/tmp}/openclaw-pacman.XXXXXX")"
trap 'rm -f "$PACMAN_TMP_CONF"' EXIT

sed 's/^[[:space:]]*SigLevel[[:space:]]*=.*/SigLevel = Never/' "$PACMAN_CONF" > "$PACMAN_TMP_CONF"
if ! grep -q '^SigLevel[[:space:]]*=[[:space:]]*Never' "$PACMAN_TMP_CONF"; then
    sed -i '/^\[options\]/a SigLevel = Never' "$PACMAN_TMP_CONF"
fi

echo ""
echo "Syncing pacman databases..."
if ! pacman -Sy --noconfirm --config "$PACMAN_TMP_CONF"; then
    echo -e "${RED}[FAIL]${NC} Failed to sync pacman databases"
    exit 1
fi

# ── Step 3: Install glibc-runner ──────────────

echo ""
echo "Installing glibc-runner..."

if pacman -S --noconfirm --config "$PACMAN_TMP_CONF" \
    --assume-installed bash=999 \
    --assume-installed patchelf=999 \
    --assume-installed resolv-conf=999 \
    glibc-runner; then
    echo -e "${GREEN}[OK]${NC}   glibc-runner installed"
else
    echo -e "${RED}[FAIL]${NC} Failed to install glibc-runner"
    exit 1
fi

# ── Verify ────────────────────────────────────

if [ ! -x "$GLIBC_LDSO" ]; then
    echo -e "${RED}[FAIL]${NC} glibc dynamic linker not found at $GLIBC_LDSO"
    exit 1
fi
echo -e "${GREEN}[OK]${NC}   glibc dynamic linker available"

install_supplementary_libs

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
