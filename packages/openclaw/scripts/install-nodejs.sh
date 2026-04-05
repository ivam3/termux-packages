#!/usr/bin/env bash
# install-nodejs.sh - Install Node.js linux-arm64 with grun wrapper (L2 conditional)
# Extracted from install-glibc-env.sh — Node.js only, assumes glibc already installed.
# Called by orchestrator when config.env PLATFORM_NEEDS_NODEJS=true.
#
# What it does:
#   1. Download Node.js linux-arm64 LTS
#   2. Create grun-style wrapper scripts (ld.so direct execution)
#   3. Configure npm
#   4. Verify everything works
#
# patchelf is NOT used — Android seccomp causes SIGSEGV on patchelf'd binaries.
# All glibc binaries are executed via: exec ld.so binary "$@"
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

OPENCLAW_DIR="${HOME}/.openclaw-android"
NODE_DIR="$OPENCLAW_DIR/node"
BIN_DIR="$OPENCLAW_DIR/bin"
GLIBC_LDSO="$PREFIX/glibc/lib/ld-linux-aarch64.so.1"

# Node.js LTS version to install
NODE_VERSION="22.22.0"
NODE_TARBALL="node-v${NODE_VERSION}-linux-arm64.tar.xz"
NODE_URL="https://nodejs.org/dist/v${NODE_VERSION}/${NODE_TARBALL}"

echo "=== Installing Node.js (glibc) ==="
echo ""

# ── Pre-checks ───────────────────────────────

if [ -z "${PREFIX:-}" ]; then
    echo -e "${RED}[FAIL]${NC} Not running in Termux (\$PREFIX not set)"
    exit 1
fi

if [ ! -x "$GLIBC_LDSO" ]; then
    echo -e "${RED}[FAIL]${NC} glibc dynamic linker not found — run install-glibc.sh first"
    exit 1
fi

# Check if already installed (check BIN_DIR wrapper first, fall back to NODE_DIR)
_NODE_CMD=""
if [ -x "$BIN_DIR/node" ]; then
    _NODE_CMD="$BIN_DIR/node"
elif [ -x "$NODE_DIR/bin/node" ]; then
    _NODE_CMD="$NODE_DIR/bin/node"
fi
if [ -n "$_NODE_CMD" ]; then
    if "$_NODE_CMD" --version &>/dev/null; then
        INSTALLED_VER=$("$_NODE_CMD" --version 2>/dev/null | sed 's/^v//')
        if [ "$INSTALLED_VER" = "$NODE_VERSION" ]; then
            echo -e "${GREEN}[SKIP]${NC} Node.js already installed (v${INSTALLED_VER})"
            # Repair wrappers — ensure they exist in BIN_DIR (npm-safe location)
            mkdir -p "$BIN_DIR"
            _any_fixed=false
            # Ensure node wrapper exists in BIN_DIR (may be missing for pre-v1.0.16 installs)
            if [ ! -x "$BIN_DIR/node" ]; then
                # Ensure node.real exists
                if [ -f "$NODE_DIR/bin/node" ] && [ ! -L "$NODE_DIR/bin/node" ] && file "$NODE_DIR/bin/node" 2>/dev/null | grep -q ELF; then
                    mv "$NODE_DIR/bin/node" "$NODE_DIR/bin/node.real"
                fi
                if [ -f "$NODE_DIR/bin/node.real" ]; then
                    cat > "$BIN_DIR/node" << NODEWRAP
#!${PREFIX}/bin/bash
[ -n "\$LD_PRELOAD" ] && export _OA_ORIG_LD_PRELOAD="\$LD_PRELOAD"
unset LD_PRELOAD
export _OA_WRAPPER_PATH="$BIN_DIR/node"
_OA_COMPAT="\$HOME/.openclaw-android/patches/glibc-compat.js"
if [ -f "\$_OA_COMPAT" ]; then
    case "\${NODE_OPTIONS:-}" in
        *"\$_OA_COMPAT"*) ;;
        *) export NODE_OPTIONS="\${NODE_OPTIONS:+\$NODE_OPTIONS }-r \$_OA_COMPAT" ;;
    esac
fi
_LEADING_OPTS=""
_COUNT=0
for _arg in "\$@"; do
    case "\$_arg" in --*) _COUNT=\$((_COUNT + 1)) ;; *) break ;; esac
done
if [ \$_COUNT -gt 0 ] && [ \$_COUNT -lt \$# ]; then
    while [ \$# -gt 0 ]; do
        case "\$1" in
            --*) _LEADING_OPTS="\${_LEADING_OPTS:+\$_LEADING_OPTS }\$1"; shift ;;
            *) break ;;
        esac
    done
    export NODE_OPTIONS="\${NODE_OPTIONS:+\$NODE_OPTIONS }\$_LEADING_OPTS"
fi
exec "$GLIBC_LDSO" --library-path "$PREFIX/glibc/lib" "$NODE_DIR/bin/node.real" "\$@"
NODEWRAP
                    chmod +x "$BIN_DIR/node"
                    _any_fixed=true
                fi
            fi
            if [ -f "$NODE_DIR/lib/node_modules/npm/bin/npm-cli.js" ]; then
                cat > "$BIN_DIR/npm" << 'NPMWRAP'
#!__PREFIX__/bin/bash
"__BIN_DIR__/node" "__NODE_DIR__/lib/node_modules/npm/bin/npm-cli.js" "$@"
_npm_exit=$?
case "$*" in *-g*openclaw*|*--global*openclaw*|*openclaw*-g*|*openclaw*--global*)
    _oc_bin="__PREFIX__/bin/openclaw"
    _oc_mjs="__PREFIX__/lib/node_modules/openclaw/openclaw.mjs"
    if [ -f "$_oc_mjs" ]; then
        [ -L "$_oc_bin" ] && rm -f "$_oc_bin"
        printf '#!__PREFIX__/bin/bash\nexec "__BIN_DIR__/node" "%s" "$@"\n' "$_oc_mjs" > "$_oc_bin"
        chmod +x "$_oc_bin"
    fi
    ;;
esac
exit $_npm_exit
NPMWRAP
                sed -i "s|__PREFIX__|$PREFIX|g; s|__BIN_DIR__|$BIN_DIR|g; s|__NODE_DIR__|$NODE_DIR|g" "$BIN_DIR/npm"
                chmod +x "$BIN_DIR/npm"
                _any_fixed=true
            fi
            if [ -f "$NODE_DIR/lib/node_modules/npm/bin/npx-cli.js" ]; then
                cat > "$BIN_DIR/npx" << 'NPXWRAP'
#!__PREFIX__/bin/bash
exec "__BIN_DIR__/node" "__NODE_DIR__/lib/node_modules/npm/bin/npx-cli.js" "$@"
NPXWRAP
                sed -i "s|__PREFIX__|$PREFIX|g; s|__BIN_DIR__|$BIN_DIR|g; s|__NODE_DIR__|$NODE_DIR|g" "$BIN_DIR/npx"
                chmod +x "$BIN_DIR/npx"
                _any_fixed=true
            fi
            if [ -f "$NODE_DIR/bin/corepack" ] && head -1 "$NODE_DIR/bin/corepack" 2>/dev/null | grep -q '#!/usr/bin/env node'; then
                sed -i "1s|#!/usr/bin/env node|#!$BIN_DIR/node|" "$NODE_DIR/bin/corepack"
                _any_fixed=true
            fi
            if [ "$_any_fixed" = true ]; then
                echo -e "${YELLOW}[FIX]${NC}  wrappers repaired in $BIN_DIR"
            fi
            exit 0
        fi
        LOWEST=$(printf '%s\n%s\n' "$INSTALLED_VER" "$NODE_VERSION" | sort -V | head -1)
        if [ "$LOWEST" = "$INSTALLED_VER" ] && [ "$INSTALLED_VER" != "$NODE_VERSION" ]; then
            echo -e "${YELLOW}[INFO]${NC} Node.js v${INSTALLED_VER} -> v${NODE_VERSION} (upgrading)"
        else
            echo -e "${GREEN}[SKIP]${NC} Node.js v${INSTALLED_VER} is newer than target v${NODE_VERSION}"
            exit 0
        fi
    else
        echo -e "${YELLOW}[INFO]${NC} Node.js exists but broken — reinstalling"
    fi
fi

# ── Step 1: Download Node.js linux-arm64 ──────

echo "Downloading Node.js v${NODE_VERSION} (linux-arm64)..."
echo "  (File size ~25MB — may take a few minutes depending on network speed)"
mkdir -p "$NODE_DIR"

TMP_DIR=$(mktemp -d "$PREFIX/tmp/node-install.XXXXXX") || {
    echo -e "${RED}[FAIL]${NC} Failed to create temp directory"
    exit 1
}
trap 'rm -rf "$TMP_DIR"' EXIT

if ! curl -fL --max-time 300 "$NODE_URL" -o "$TMP_DIR/$NODE_TARBALL"; then
    echo -e "${RED}[FAIL]${NC} Failed to download Node.js v${NODE_VERSION}"
    exit 1
fi
echo -e "${GREEN}[OK]${NC}   Downloaded $NODE_TARBALL"

# Extract
echo "Extracting Node.js... (this may take a moment)"
if ! tar -xJf "$TMP_DIR/$NODE_TARBALL" -C "$NODE_DIR" --strip-components=1; then
    echo -e "${RED}[FAIL]${NC} Failed to extract Node.js"
    exit 1
fi
echo -e "${GREEN}[OK]${NC}   Extracted to $NODE_DIR"

# ── Step 2: Create wrapper scripts ────────────
#
# Wrappers are placed in BIN_DIR (~/.openclaw-android/bin/), separate from
# NODE_DIR/bin/ which npm manages. This prevents npm from overwriting our
# wrappers when users run 'npm install -g npm' or similar commands.

echo ""
echo "Creating wrapper scripts (grun-style, no patchelf)..."
mkdir -p "$BIN_DIR"

# Move original node binary to node.real
if [ -f "$NODE_DIR/bin/node" ] && [ ! -L "$NODE_DIR/bin/node" ]; then
    mv "$NODE_DIR/bin/node" "$NODE_DIR/bin/node.real"
fi

# Create node wrapper script in BIN_DIR
# This uses grun-style execution: ld.so directly loads the binary
# LD_PRELOAD must be unset to prevent Bionic libtermux-exec.so from
# being loaded into the glibc process (causes version mismatch crash)
# glibc-compat.js is auto-loaded to fix Android kernel quirks (os.cpus() returns 0,
# os.networkInterfaces() throws EACCES) that affect native module builds and runtime.
cat > "$BIN_DIR/node" << WRAPPER
#!${PREFIX}/bin/bash
[ -n "\$LD_PRELOAD" ] && export _OA_ORIG_LD_PRELOAD="\$LD_PRELOAD"
unset LD_PRELOAD
export _OA_WRAPPER_PATH="$BIN_DIR/node"
_OA_COMPAT="\$HOME/.openclaw-android/patches/glibc-compat.js"
if [ -f "\$_OA_COMPAT" ]; then
    case "\${NODE_OPTIONS:-}" in
        *"\$_OA_COMPAT"*) ;;
        *) export NODE_OPTIONS="\${NODE_OPTIONS:+\$NODE_OPTIONS }-r \$_OA_COMPAT" ;;
    esac
fi
_LEADING_OPTS=""
_COUNT=0
for _arg in "\$@"; do
    case "\$_arg" in --*) _COUNT=\$((_COUNT + 1)) ;; *) break ;; esac
done
if [ \$_COUNT -gt 0 ] && [ \$_COUNT -lt \$# ]; then
    while [ \$# -gt 0 ]; do
        case "\$1" in
            --*) _LEADING_OPTS="\${_LEADING_OPTS:+\$_LEADING_OPTS }\$1"; shift ;;
            *) break ;;
        esac
    done
    export NODE_OPTIONS="\${NODE_OPTIONS:+\$NODE_OPTIONS }\$_LEADING_OPTS"
fi
exec "$GLIBC_LDSO" --library-path "$PREFIX/glibc/lib" "$NODE_DIR/bin/node.real" "\$@"
WRAPPER
chmod +x "$BIN_DIR/node"
echo -e "${GREEN}[OK]${NC}   node wrapper created ($BIN_DIR/node)"

# ── Step 2.5: Create npm/npx wrapper scripts in BIN_DIR ──
#
# npm/npx wrappers go in BIN_DIR (not NODE_DIR/bin/) so npm can't overwrite them.
echo "Creating npm/npx wrapper scripts..."
if [ -f "$NODE_DIR/lib/node_modules/npm/bin/npm-cli.js" ]; then
    cat > "$BIN_DIR/npm" << 'NPMWRAP'
#!__PREFIX__/bin/bash
"__BIN_DIR__/node" "__NODE_DIR__/lib/node_modules/npm/bin/npm-cli.js" "$@"
_npm_exit=$?
# Re-patch openclaw CLI wrapper after global install/update
case "$*" in *-g*openclaw*|*--global*openclaw*|*openclaw*-g*|*openclaw*--global*)
    _oc_bin="__PREFIX__/bin/openclaw"
    _oc_mjs="__PREFIX__/lib/node_modules/openclaw/openclaw.mjs"
    if [ -f "$_oc_mjs" ]; then
        [ -L "$_oc_bin" ] && rm -f "$_oc_bin"
        printf '#!__PREFIX__/bin/bash\nexec "__BIN_DIR__/node" "%s" "$@"\n' "$_oc_mjs" > "$_oc_bin"
        chmod +x "$_oc_bin"
    fi
    ;;
esac
exit $_npm_exit
NPMWRAP
    sed -i "s|__PREFIX__|$PREFIX|g; s|__BIN_DIR__|$BIN_DIR|g; s|__NODE_DIR__|$NODE_DIR|g" "$BIN_DIR/npm"
    chmod +x "$BIN_DIR/npm"
    echo -e "${GREEN}[OK]${NC}   npm wrapper created ($BIN_DIR/npm)"
fi
if [ -f "$NODE_DIR/lib/node_modules/npm/bin/npx-cli.js" ]; then
    cat > "$BIN_DIR/npx" << 'NPXWRAP'
#!__PREFIX__/bin/bash
exec "__BIN_DIR__/node" "__NODE_DIR__/lib/node_modules/npm/bin/npx-cli.js" "$@"
NPXWRAP
    sed -i "s|__PREFIX__|$PREFIX|g; s|__BIN_DIR__|$BIN_DIR|g; s|__NODE_DIR__|$NODE_DIR|g" "$BIN_DIR/npx"
    chmod +x "$BIN_DIR/npx"
    echo -e "${GREEN}[OK]${NC}   npx wrapper created ($BIN_DIR/npx)"
fi
# corepack uses a different structure — shebang patch is sufficient
if [ -f "$NODE_DIR/bin/corepack" ] && head -1 "$NODE_DIR/bin/corepack" 2>/dev/null | grep -q '#!/usr/bin/env node'; then
    sed -i "1s|#!/usr/bin/env node|#!$BIN_DIR/node|" "$NODE_DIR/bin/corepack"
    echo -e "${GREEN}[OK]${NC}   corepack shebang patched"
fi

# ── Step 3: Configure npm ─────────────────────

echo ""
echo "Configuring npm..."

# Set script-shell to ensure npm lifecycle scripts use the correct shell
# On Android 9+, /bin/sh exists. On 7-8 it doesn't.
# Using $PREFIX/bin/sh is always safe.
export PATH="$BIN_DIR:$NODE_DIR/bin:$PATH"
"$BIN_DIR/npm" config set script-shell "$PREFIX/bin/sh" 2>/dev/null || true
echo -e "${GREEN}[OK]${NC}   npm script-shell set to $PREFIX/bin/sh"

# ── Step 4: Verify ────────────────────────────

echo ""
echo "Verifying glibc Node.js..."

NODE_VER=$("$BIN_DIR/node" --version 2>/dev/null) || {
    echo -e "${RED}[FAIL]${NC} Node.js verification failed — wrapper script may be broken"
    exit 1
}
echo -e "${GREEN}[OK]${NC}   Node.js $NODE_VER (glibc, grun wrapper)"

NPM_VER=$("$BIN_DIR/npm" --version 2>/dev/null) || {
    echo -e "${YELLOW}[WARN]${NC} npm verification failed"
}
if [ -n "${NPM_VER:-}" ]; then
    echo -e "${GREEN}[OK]${NC}   npm $NPM_VER"
fi

# Quick platform check
PLATFORM=$("$BIN_DIR/node" -e "console.log(process.platform)" 2>/dev/null) || true
if [ "$PLATFORM" = "linux" ]; then
    echo -e "${GREEN}[OK]${NC}   platform: linux (correct)"
else
    echo -e "${YELLOW}[WARN]${NC} platform: ${PLATFORM:-unknown} (expected: linux)"
fi

echo ""
echo -e "${GREEN}Node.js installed successfully.${NC}"
echo "  Node.js: $NODE_VER ($BIN_DIR/node)"
