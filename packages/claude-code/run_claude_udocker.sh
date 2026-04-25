#!/bin/bash
# Script para ejecutar Claude Code en el contenedor udocker
set -e

CONTAINER_NAME="claude-env"

# Verificamos si el contenedor existe
if ! udocker ps | grep -q "$CONTAINER_NAME"; then
    echo "[!] Error: El contenedor $CONTAINER_NAME no existe. Corre primero ./install_claude_udocker.sh"
    exit 1
fi

echo "[*] Iniciando Claude Code..."
# Correr en modo interactivo con el binario instalado
udocker run --terminal "$CONTAINER_NAME" /usr/local/bin/claude "$@"
