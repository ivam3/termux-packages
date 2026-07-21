#!/data/data/com.termux/files/usr/bin/bash
# OmnIRoute environment setup for Termux
# Source this file in ~/.bashrc or ~/.zshrc for autocompletion:
#   source /data/data/com.termux/files/usr/share/omniroute/omniroute.sh

OMNIROUTE_DIR="${HOME}/.local/share/omniroute"
OMNIROUTE_BIN="${HOME}/.local/bin"

# Add to PATH if not already there
case ":${PATH}:" in
  *":${OMNIROUTE_BIN}:"*) ;;
  *) export PATH="${OMNIROUTE_BIN}:${PATH}" ;;
esac

# OmnIRoute environment variables
export OMNIROUTE_DATA_DIR="${HOME}/.omniroute"
export OMNIROUTE_PORT="${OMNIROUTE_PORT:-20128}"

# Completion helper (requires npm completion)
if [[ -f "${OMNIROUTE_DIR}/node_modules/.bin/omniroute-completion" ]]; then
  :
elif command -v omniroute &>/dev/null; then
  eval "$(omniroute completion bash 2>/dev/null)" || true
fi
