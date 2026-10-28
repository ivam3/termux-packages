#!/data/data/com.termux/files/usr/bin/bash
set -Eeuo pipefail

TMPDIR=${TMPDIR:-/data/data/com.termux/files/usr/tmp}
APK=${APK:-"$TMPDIR/test/base.apk"}
ELF=${ELF:-/system/bin/toybox}

if [[ ! -f "$APK" ]]; then
  APK=/system/app/CompanionDeviceManager/CompanionDeviceManager.apk
fi

ok() { printf 'ok - %s\n' "$1"; }
fail() { printf 'FAIL - %s\n' "$1" >&2; exit 1; }

command -v rea >/dev/null || fail "rea no está en PATH"
command -v rea-setup >/dev/null || fail "rea-setup no está en PATH"
command -v jq >/dev/null || fail "jq no está instalado"

[[ -f "$APK" ]] || fail "no se encontró un APK de prueba"
[[ -f "$ELF" ]] || fail "no se encontró el ELF de prueba: $ELF"

[ "$(rea --version)" = "6.8.0" ] || fail "versión de REA inesperada: $(rea --version)"
ok "version 6.8.0"

entry="${HOME}/.local/share/rea/app/node_modules/rea-agents/scripts/rea.mjs"
real_entry="${HOME}/.local/share/rea/app/node_modules/rea-agents/scripts/rea-real.mjs"
[[ -x "$entry" ]] || fail "no se encontró el entrypoint wrapper"
[[ -f "$real_entry" ]] || fail "no se encontró rea-real.mjs"
[ "$(node "$entry" --version)" = "6.8.0" ] || fail "el wrapper no ejecuta REA"
ok "entrypoint wrapper"

setup_home="$(mktemp -d "${TMPDIR}/rea-smoke-XXXXXX")"
mkdir -p "$setup_home/.config/opencode" "$setup_home/.local/share/rea"
ln -s "${HOME}/.local/share/rea/app" "$setup_home/.local/share/rea/app"
printf '{}\n' > "$setup_home/.config/opencode/opencode.json"
if ! setup_plan="$(HOME="$setup_home" timeout 60 rea setup --dry-run --client opencode --format json 2>/dev/null)"; then
  rm -rf "$setup_home"
  fail "rea setup --dry-run falló"
fi
if ! jq -e '
  .plannedActions[]
  | select(.id == "configure_client:opencode")
  | ((.detail | contains("node_modules/rea-agents/scripts/rea.mjs"))
     and ((.detail | contains("rea-real.mjs")) | not))
' <<<"$setup_plan" >/dev/null; then
  rm -rf "$setup_home"
  fail "setup no registra el entrypoint wrapper"
fi
rm -rf "$setup_home"
ok "setup registra el wrapper"

mcp_doctor="$(timeout 120 rea mcp doctor --json 2>/dev/null)" \
  || fail "rea mcp doctor falló"
jq -e '
  .healthy == true
  and (.inventory.tools.missing | length == 0)
  and (.inventory.prompts.missing | length == 0)
' <<<"$mcp_doctor" >/dev/null \
  || fail "el inventario MCP está incompleto"
ok "MCP sano"

doctor="$(rea doctor --json 2>/dev/null || true)"
jq -e '.checks[] | select(.name == "host") | .detail == "linux arm64"' \
  <<<"$doctor" >/dev/null || fail "doctor no reporta el host shimmeado linux arm64"
ok "host shimmeado linux arm64"

if [[ -d "${HOME}/.local/share/ghidra" ]]; then
  jq -e '.providerInspections[] | select(.id == "ghidra") | .available == true' \
    <<<"$doctor" >/dev/null || fail "Ghidra no está disponible para REA"
  ok "Ghidra disponible"

  if ! ghidra_analysis="$(rea analyze "$ELF" --provider ghidra --format json 2>/dev/null)"; then
    fail "Ghidra no pudo analizar el ELF"
  fi
  jq -e '
    .analysis_profile.parameters.upstream_analysis_profile.provider.id == "ghidra"
    and (.normalized_result.procedure_count > 0)
  ' <<<"$ghidra_analysis" >/dev/null \
    || fail "el análisis no provino de Ghidra o no encontró procedimientos"
  ok "Ghidra analiza ELF"
fi

rea inspect-artifact "$ELF" --format json \
  | jq -e '.subject.format == "elf"' >/dev/null \
  || fail "inventario ELF"
ok "inventario ELF"

rea execute-rizin-command "$ELF" iI --format json \
  | jq -e '.provider.id == "rizin" and .normalized_result.exit_code == 0' >/dev/null \
  || fail "rizin"
ok "rizin"

rea inspect-with-objdump "$ELF" file_headers --format json \
  | jq -e '.provider.id == "gnu.objdump" and .normalized_result.exit_code == 0' >/dev/null \
  || fail "objdump GNU"
ok "objdump GNU"

rea inspect-apk-signature "$APK" --format json \
  | jq -e '.operation == "inspect_apk_signature" and .provider.id == "apk-signature"' >/dev/null \
  || fail "firma APK"
ok "firma APK"

jadx_out="$(rea inspect-android-package "$APK" --format json 2>&1 || true)"
jq -e '.details.diagnostics.failure_code == "unsupported_host"' \
  <<<"$jadx_out" >/dev/null \
  || fail "JADX no falló con unsupported_host"
ok "JADX bloqueado como se esperaba"

printf '\nTodo OK\n'
