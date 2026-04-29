#!/data/data/com.termux/files/usr/bin/bash
ALPINE_ROOT="/data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/alpine"
LOADER="$ALPINE_ROOT/lib/ld-musl-aarch64.so.1"
LIB_PATH="$ALPINE_ROOT/lib"
BINARY_PATH="$ALPINE_ROOT/bin/claude"

[[ -d ${HOME}/.claude ]] || { mkdir -p ${HOME}/.claude >/dev/null ;}
# Limpiar LD_PRELOAD para evitar errores de símbolos con Bionic
unset LD_PRELOAD

# Ejecutar Claude
$LOADER --library-path $LIB_PATH $BINARY_PATH "$@"
####::: REPORT ISSUES AT https://t.me/Ivam3_Bot :::####
