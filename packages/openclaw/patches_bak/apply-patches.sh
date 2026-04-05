#!/usr/bin/env bash
# apply-patches.sh - Apply all patches for OpenClaw on Termux (glibc architecture)
set -euo pipefail

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PATCH_DEST="$HOME/.openclaw-android/patches"
LOG_FILE="$HOME/.openclaw-android/patch.log"

echo "=== Applying Patches ==="
echo ""

# Ensure destination exists
mkdir -p "$PATCH_DEST"

# Start logging
echo "Patch application started: $(date)" > "$LOG_FILE"

# 1. Copy glibc-compat.js (replaces bionic-compat.js in glibc architecture)
if [ -f "$SCRIPT_DIR/glibc-compat.js" ]; then
    cp "$SCRIPT_DIR/glibc-compat.js" "$PATCH_DEST/glibc-compat.js"
    echo -e "${GREEN}[OK]${NC}   Copied glibc-compat.js to $PATCH_DEST/"
    echo "  Copied glibc-compat.js" >> "$LOG_FILE"
else
    echo -e "${RED}[FAIL]${NC} glibc-compat.js not found in $SCRIPT_DIR"
    echo "  FAILED: glibc-compat.js not found" >> "$LOG_FILE"
    exit 1
fi

# 2. Install systemctl stub (Termux has no systemd)
if [ -f "${PREFIX}/bin/systemctl" ]; then
    chmod +x "$PREFIX/bin/systemctl"
    echo -e "${GREEN}[OK]${NC}   Installed systemctl stub to $PREFIX/bin/"
    echo "  Installed systemctl stub" >> "$LOG_FILE"
else
    echo -e "${RED}[FAIL]${NC} systemctl stub not found in $SCRIPT_DIR"
    echo "  FAILED: systemctl not found" >> "$LOG_FILE"
    exit 1
fi

# 3. Run path patches
echo ""
if [ -f "$SCRIPT_DIR/patch-paths.sh" ]; then
    bash "$SCRIPT_DIR/patch-paths.sh" 2>&1 | tee -a "$LOG_FILE"
else
    echo -e "${RED}[FAIL]${NC} patch-paths.sh not found in $SCRIPT_DIR"
    echo "  FAILED: patch-paths.sh not found" >> "$LOG_FILE"
    exit 1
fi

echo ""
echo "Patch log saved to: $LOG_FILE"
echo -e "${GREEN}All patches applied.${NC}"
echo "Patch application completed: $(date)" >> "$LOG_FILE"
