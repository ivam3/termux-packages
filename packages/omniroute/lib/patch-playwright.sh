#!/data/data/com.termux/files/usr/bin/bash
# Patch playwright-core for Android/Termux
# Usage:
#   patch-playwright.sh              → auto-detect: mock o full según playwright-proot
#   patch-playwright.sh --mock       → solo stub (crash prevention)
#   patch-playwright.sh --full       → parcheo completo + soporte proot CDP
#   patch-playwright.sh --status     → mostrar estado actual

set -Eeuo pipefail

PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
CYAN="\033[36m"; GREEN="\033[32m"; YELLOW="\033[33m"; RED="\033[31m"; DIM="\033[2m"; RESET="\033[0m"
info()  { printf "%b[..]%b %b%s%b\n" "$CYAN" "$RESET" "$DIM" "$*" "$RESET"; }
ok()    { printf "%b[✔]%b %s\n" "$GREEN" "$RESET" "$*"; }
warn()  { printf "%b[!]%b %s\n" "$YELLOW" "$RESET" "$*"; }
erro()  { printf "%b[ERR]%b %s\n" "$RED" "$RESET" "$*" >&2; }

INSTALL_DIR="${1:-${HOME}/.local/share/omniroute}"
NODE_MODULES="${INSTALL_DIR}/node_modules"
PATCHED_MARKER="__omniroute_patched"

# ── locate all playwright-core copies ──────────────────────────

find_pw_cores() {
  find "$NODE_MODULES" -path "*/playwright-core/index.js" -not -path "*/node_modules/.cache/*" 2>/dev/null
  find "$INSTALL_DIR" -path "*/dist/node_modules/playwright-core/index.js" 2>/dev/null
  # Also check npx caches
  for d in "${HOME}/.npm/_npx/"*/node_modules/playwright-core; do
    [[ -f "$d/index.js" ]] && echo "$d/index.js"
  done 2>/dev/null || true
}

# ── apply try/catch mock to index.js ──────────────────────────

apply_mock() {
  local idx="$1"
  local dir; dir=$(dirname "$idx")
  local marker="${dir}/${PATCHED_MARKER}"

  # Check if already patched with mock
  if grep -q "Unsupported platform" "$idx" 2>/dev/null; then
    return 0
  fi

  cp "$idx" "${idx}.bak.$$"
  cat > "$idx" << 'MOCKEOF'
try {
  require('./lib/bootstrap');
  module.exports = require('./lib/coreBundle').inprocess.playwright;
} catch (e) {
  if (e && e.message && e.message.includes('Unsupported platform')) {
    module.exports = {
      chromium: { connect: function() { return Promise.reject(new Error('Playwright browser unavailable on Android. Install playwright-proot: apt install playwright-proot')); } },
      firefox: {}, webkit: {},
      selectors: {}, devices: {}, errors: {},
      _android: { launcher: {} }
    };
  } else {
    throw e;
  }
}
MOCKEOF
  touch "$marker"
  return 0
}

# ── full patch: treat Android as Linux in platform checks ──────

apply_full_patch() {
  local pw_dir; pw_dir=$(dirname "$(dirname "$1")")
  local files_to_patch=(
    "$pw_dir/lib/coreBundle.js"
    "$pw_dir/lib/serverRegistry.js"
    "$pw_dir/lib/tools/cli-client/registry.js"
  )

  local count=0
  for f in "${files_to_patch[@]}"; do
    [[ ! -f "$f" ]] && continue
    # Skip if already patched
    if grep -q "process.platform === \"android\"" "$f" 2>/dev/null; then
      count=$((count+1))
      continue
    fi
    cp "$f" "${f}.bak.$$" 2>/dev/null || true

    # Replace `=== "linux"` with `=== "linux" || process.platform === "android"`
    # in all platform checks within this file
    sed -i \
      -e 's/if (process.platform === "linux")/if (process.platform === "linux" || process.platform === "android")/g' \
      -e 's/process\.platform === "linux" ?/process.platform === "linux" || process.platform === "android" ?/g' \
      "$f"
    count=$((count+1))
  done

  echo $count
}

# ── restore original files from backups ────────────────────────

restore_originals() {
  find "$NODE_MODULES" "$INSTALL_DIR" -name "*.bak.*" -path "*/playwright-core/*" 2>/dev/null | while read -r bak; do
    local orig="${bak%.bak.*}"
    if [[ -f "$bak" ]] && [[ -f "$orig" ]]; then
      cp "$bak" "$orig"
      rm "$bak"
    fi
  done
  # Remove markers
  find "$NODE_MODULES" "$INSTALL_DIR" -name "$PATCHED_MARKER" -path "*/playwright-core/*" -delete 2>/dev/null || true
}

# ── detect playwright-proot ────────────────────────────────────

has_playwright_proot() {
  command -v playwright-proot &>/dev/null
}

has_proot_chromium() {
  # Check if Chromium is accessible via proot
  proot-distro login ubuntu --shared-tmp -- /bin/bash -c \
    'ls /root/.cache/ms-playwright/chromium-*/chrome-linux/chrome 2>/dev/null' &>/dev/null
}

# ── main ───────────────────────────────────────────────────────

MODE="${1:-auto}"

case "$MODE" in
  --mock|-m)
    info "Applying mock patch (crash prevention only)..."
    COUNT=0
    for idx in $(find_pw_cores); do
      apply_mock "$idx" && COUNT=$((COUNT+1))
    done
    ok "Mock applied to $COUNT playwright-core copy(ies)."
    ;;

  --full|-f)
    info "Applying full Android-compatibility patch..."
    COUNT_MOCK=0
    COUNT_FULL=0
    for idx in $(find_pw_cores); do
      apply_mock "$idx" && COUNT_MOCK=$((COUNT_MOCK+1))
      local result
      result=$(apply_full_patch "$idx" 2>/dev/null || echo 0)
      COUNT_FULL=$((COUNT_FULL + result))
    done
    ok "Mock: $COUNT_MOCK copy(ies). Full patch: $COUNT_FULL file(s)."

    if has_playwright_proot; then
      ok "playwright-proot detected."
      echo ""
      echo "  Para usar Chromium via CDP, configura en omniroute:"
      echo "    PLAYWRIGHT_BROWSERS_PATH=/root/.cache/ms-playwright"
      echo "    PLAYWRIGHT_CDP_URL=http://localhost:9222"
      echo ""
      echo "  O inicia Chromium manualmente:"
      echo "    playwright-proot open http://localhost:20128"
    else
      warn "playwright-proot no instalado. Los proveedores web no funcionarán."
      warn "  Para soporte completo de navegador: apt install playwright-proot"
    fi
    ;;

  --status|-s)
    info "Playwright patch status:"
    for idx in $(find_pw_cores); do
      local dir; dir=$(dirname "$idx")
      local marker="${dir}/${PATCHED_MARKER}"
      if [[ -f "$marker" ]]; then
        ok "  $(dirname "$idx") → mock applied"
      elif grep -q "process.platform === \"android\"" "$dir/lib/coreBundle.js" 2>/dev/null; then
        ok "  $(dirname "$idx") → full patch (Android as Linux)"
      else
        warn "  $(dirname "$idx") → NOT patched"
      fi
    done
    if has_playwright_proot; then
      ok "  playwright-proot: INSTALLED"
      has_proot_chromium && ok "  Chromium in proot: AVAILABLE" || warn "  Chromium in proot: NOT FOUND (run 'playwright-proot open')"
    else
      warn "  playwright-proot: NOT INSTALLED"
    fi
    ;;

  --restore|-r)
    info "Restoring original playwright-core files..."
    restore_originals
    ok "Restored."
    ;;

  auto|"")
    # Auto-detect: if playwright-proot installed, full patch; else mock only
    if has_playwright_proot && has_proot_chromium; then
      info "playwright-proot + Chromium detected. Applying full patch..."
      exec "$0" --full
    else
      info "playwright-proot not detected. Applying mock patch..."
      exec "$0" --mock
    fi
    ;;

  *)
    echo "Usage: $0 [--mock|--full|--status|--restore]"
    exit 1
    ;;
esac
