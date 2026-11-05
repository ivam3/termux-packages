#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/lib.sh"

PWS=$(printf '%s\n' "${SHELL:-bash}" | awk -F '/' '{print $NF}')
PLATFORM=$(detect_platform) || true

PATH_DIRS='$HOME/.local/bin'
PATH_DIRS_FISH='$HOME/.local/bin'
if [ -n "$PLATFORM" ]; then
    load_platform_config "$PLATFORM" "$(dirname "$(dirname "$0")")" 2>/dev/null || true
    if [ "${PLATFORM_NEEDS_NODEJS:-}" = true ]; then
        PATH_DIRS='$HOME/.openclaw-android/bin:$HOME/.openclaw-android/node/bin:$HOME/.local/bin'
        PATH_DIRS_FISH='$HOME/.openclaw-android/bin $HOME/.openclaw-android/node/bin $HOME/.local/bin'
    fi
fi

PLATFORM_BASH=""
PLATFORM_FISH=""
PLATFORM_ENV_SCRIPT="${HOME}/.openclaw/platforms/$PLATFORM/env.sh"
if [ -n "$PLATFORM" ] && [ -f "$PLATFORM_ENV_SCRIPT" ]; then
    PLATFORM_BASH=$(bash "$PLATFORM_ENV_SCRIPT")
    PLATFORM_FISH=$(printf '%s\n' "$PLATFORM_BASH" | sed -E 's/^export ([A-Za-z_][A-Za-z0-9_]*)=(.*)$/set -gx \1 \2/')
fi

# OpenClaw's fs-safe native binding uses openat2(), which Android's seccomp
# filter terminates with SIGSYS. The JavaScript fallback is safe and slower,
# but it lets the CLI, SQLite worker and updater run on Android.
BASH_BLOCK=$(cat <<EOF
${BASHRC_MARKER_START}
# platform: ${PLATFORM:-none}
export PATH="${PATH_DIRS}:\$PATH"
export TMPDIR="\$PREFIX/tmp"
export TMP="\$TMPDIR"
export TEMP="\$TMPDIR"
export OA_GLIBC=1
export FS_SAFE_NATIVE_MODE=off
export OPENCLAW_FS_SAFE_NATIVE_MODE=off
export NODE_OPTIONS=--dns-result-order=ipv4first
${PLATFORM_BASH}
${BASHRC_MARKER_END}
EOF
)

FISH_BLOCK=$(cat <<EOF
${BASHRC_MARKER_START}
# platform: ${PLATFORM:-none}
set -gx PATH ${PATH_DIRS_FISH} \$PATH
set -gx TMPDIR \$PREFIX/tmp
set -gx TMP \$TMPDIR
set -gx TEMP \$TMPDIR
set -gx OA_GLIBC 1
set -gx FS_SAFE_NATIVE_MODE off
set -gx OPENCLAW_FS_SAFE_NATIVE_MODE off
set -gx NODE_OPTIONS --dns-result-order=ipv4first
${PLATFORM_FISH}
${BASHRC_MARKER_END}
EOF
)

resolve_target() {
    local file="$1"
    if [ -L "$file" ]; then
        readlink -f "$file" 2>/dev/null || printf '%s' "$file"
    else
        printf '%s' "$file"
    fi
}

remove_block() {
    local file
    file=$(resolve_target "$1")
    [ -f "$file" ] || return 0
    if grep -qF "$BASHRC_MARKER_START" "$file"; then
        # Operate on the symlink target; sed -i would otherwise replace
        # ~/.bashrc (an i-Haklab symlink) with a regular file.
        sed -i "\|${BASHRC_MARKER_START}|,\|${BASHRC_MARKER_END}|d" "$file"
    fi
    # Remove the standalone line written by older package versions. It is
    # now part of the managed block and is invalid fish syntax.
    sed -i '/^export NODE_OPTIONS=--dns-result-order=ipv4first$/d' "$file"
}

write_block() {
    local file
    file=$(resolve_target "$1")
    local block="$2"
    mkdir -p "$(dirname "$file")"
    touch "$file"
    remove_block "$file"
    printf '\n%s\n' "$block" >> "$file"
}

# Older versions wrote bash export syntax into the system fish config. Remove
# that stale block before installing the fish-compatible user block.
SYSTEM_FISH_CONFIG="${PREFIX}/etc/fish/config.fish"
remove_block "$SYSTEM_FISH_CONFIG"

# Always maintain a bash-compatible block: verification and non-login shells
# rely on ~/.bashrc, even when fish is the interactive login shell.
write_block "${HOME}/.bashrc" "$BASH_BLOCK"

case "$PWS" in
    fish)
        # Fish follows XDG_CONFIG_HOME when it is set, but Termux users often
        # keep their configuration in ~/.config/fish. Maintain both paths so
        # the block is present whichever config fish loads.
        USER_FISH_CONFIG="${HOME}/.config/fish/config.fish"
        write_block "$USER_FISH_CONFIG" "$FISH_BLOCK"
        if [ -n "${XDG_CONFIG_HOME:-}" ] && \
           [ "${XDG_CONFIG_HOME}/fish/config.fish" != "$USER_FISH_CONFIG" ]; then
            write_block "${XDG_CONFIG_HOME}/fish/config.fish" "$FISH_BLOCK"
        fi
        ;;
    zsh)
        write_block "${HOME}/.zshrc" "$BASH_BLOCK"
        ;;
esac

if [ ! -e "${PREFIX}/bin/ar" ] && [ -x "${PREFIX}/bin/llvm-ar" ]; then
    ln -s "${PREFIX}/bin/llvm-ar" "${PREFIX}/bin/ar"
fi
