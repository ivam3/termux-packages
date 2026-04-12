#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../../scripts/lib.sh"

export CPATH="$PREFIX/include/glib-2.0:$PREFIX/lib/glib-2.0/include"

echo "=== Updating OpenClaw Platform ==="
echo ""

pkg install -y libvips binutils 2>/dev/null || true
if [ ! -e "$PREFIX/bin/ar" ] && [ -x "$PREFIX/bin/llvm-ar" ]; then
    ln -s "$PREFIX/bin/llvm-ar" "$PREFIX/bin/ar"
fi

CURRENT_VER=$(npm list -g openclaw 2>/dev/null | grep 'openclaw@' | sed 's/.*openclaw@//' | tr -d '[:space:]')
LATEST_VER=$(npm view openclaw version 2>/dev/null || echo "")
OPENCLAW_UPDATED=false

if [ -n "$CURRENT_VER" ] && [ -n "$LATEST_VER" ] && [ "$CURRENT_VER" = "$LATEST_VER" ]; then
    echo -e "${GREEN}[OK]${NC}   openclaw $CURRENT_VER is already the latest"
else
    echo "Updating openclaw npm package... ($CURRENT_VER → $LATEST_VER)"
    echo "  (This may take several minutes depending on network speed)"
    if npm install -g openclaw@latest --no-fund --no-audit --ignore-scripts; then
        echo -e "${GREEN}[OK]${NC}   openclaw $LATEST_VER updated"
        OPENCLAW_UPDATED=true
    else
        echo -e "${YELLOW}[WARN]${NC} Package update failed (non-critical)"
        echo "       Retry manually: npm install -g openclaw@latest"
    fi
fi

# Fix native bindings broken by --ignore-scripts (npm/cli#4828 workaround)
# Packages like @snazzah/davey use platform-specific optional deps that get
# skipped when --ignore-scripts is used. Reinstall them without the flag.
OPENCLAW_DIR="$(npm root -g)/openclaw"
if [ -d "$OPENCLAW_DIR/node_modules/@snazzah/davey" ]; then
    if ! node -e "require('$OPENCLAW_DIR/node_modules/@snazzah/davey')" 2>/dev/null; then
        echo "Fixing native bindings for @snazzah/davey..."
        (cd "$OPENCLAW_DIR" && npm install @snazzah/davey --no-fund --no-audit --no-save 2>/dev/null) || true
    fi
fi

bash "$SCRIPT_DIR/platforms/openclaw/patches/openclaw-apply-patches.sh"

if [ "$OPENCLAW_UPDATED" = true ]; then
    bash "$SCRIPT_DIR/patches/openclaw-build-sharp.sh" || true
else
    echo -e "${GREEN}[SKIP]${NC} openclaw $CURRENT_VER unchanged \u2014 sharp rebuild not needed"
fi

if command -v clawdhub &>/dev/null; then
    CLAWDHUB_CURRENT_VER=$(npm list -g clawdhub 2>/dev/null | grep 'clawdhub@' | sed 's/.*clawdhub@//' | tr -d '[:space:]')
    CLAWDHUB_LATEST_VER=$(npm view clawdhub version 2>/dev/null || echo "")
    if [ -n "$CLAWDHUB_CURRENT_VER" ] && [ -n "$CLAWDHUB_LATEST_VER" ] && [ "$CLAWDHUB_CURRENT_VER" = "$CLAWDHUB_LATEST_VER" ]; then
        echo -e "${GREEN}[OK]${NC}   clawdhub $CLAWDHUB_CURRENT_VER is already the latest"
    elif [ -n "$CLAWDHUB_LATEST_VER" ]; then
        echo "Updating clawdhub... ($CLAWDHUB_CURRENT_VER → $CLAWDHUB_LATEST_VER)"
        if npm install -g clawdhub@latest --no-fund --no-audit; then
            echo -e "${GREEN}[OK]${NC}   clawdhub $CLAWDHUB_LATEST_VER updated"
        else
            echo -e "${YELLOW}[WARN]${NC} clawdhub update failed (non-critical)"
        fi
    else
        echo -e "${YELLOW}[WARN]${NC} Could not check clawdhub latest version"
    fi
else
    if ask_yn "clawdhub (skill manager) is not installed. Install it?"; then
        echo "Installing clawdhub..."
        if npm install -g clawdhub --no-fund --no-audit; then
            echo -e "${GREEN}[OK]${NC}   clawdhub installed"
        else
            echo -e "${YELLOW}[WARN]${NC} clawdhub installation failed (non-critical)"
        fi
    else
        echo -e "${YELLOW}[SKIP]${NC} Skipping clawdhub"
    fi
fi

CLAWHUB_DIR="$(npm root -g)/clawdhub"
if [ -d "$CLAWHUB_DIR" ] && ! (cd "$CLAWHUB_DIR" && node -e "require('undici')" 2>/dev/null); then
    echo "Installing undici dependency for clawdhub..."
    if (cd "$CLAWHUB_DIR" && npm install undici --no-fund --no-audit); then
        echo -e "${GREEN}[OK]${NC}   undici installed for clawdhub"
    else
        echo -e "${YELLOW}[WARN]${NC} undici installation failed"
    fi
else
    UNDICI_VER=$(cd "$CLAWHUB_DIR" && node -e "console.log(require('undici/package.json').version)" 2>/dev/null || echo "")
    echo -e "${GREEN}[OK]${NC}   undici ${UNDICI_VER:-available}"
fi

OLD_SKILLS_DIR="$HOME/skills"
CORRECT_SKILLS_DIR="$HOME/.openclaw/workspace/skills"
if [ -d "$OLD_SKILLS_DIR" ] && [ "$(ls -A "$OLD_SKILLS_DIR" 2>/dev/null)" ]; then
    echo ""
    echo "Migrating skills from ~/skills/ to ~/.openclaw/workspace/skills/..."
    mkdir -p "$CORRECT_SKILLS_DIR"
    for skill in "$OLD_SKILLS_DIR"/*/; do
        [ -d "$skill" ] || continue
        skill_name=$(basename "$skill")
        if [ ! -d "$CORRECT_SKILLS_DIR/$skill_name" ]; then
            if mv "$skill" "$CORRECT_SKILLS_DIR/$skill_name" 2>/dev/null; then
                echo -e "  ${GREEN}[OK]${NC}   Migrated $skill_name"
            else
                echo -e "  ${YELLOW}[WARN]${NC} Failed to migrate $skill_name"
            fi
        else
            echo -e "  ${YELLOW}[SKIP]${NC} $skill_name already exists in correct location"
        fi
    done
    if rmdir "$OLD_SKILLS_DIR" 2>/dev/null; then
        echo -e "${GREEN}[OK]${NC}   Removed empty ~/skills/"
    else
        echo -e "${YELLOW}[WARN]${NC} ~/skills/ not empty after migration — check manually"
    fi
fi

python -c "import yaml" 2>/dev/null || pip install pyyaml -q || true
