#!/bin/bash
# Script para instalar Claude Code en udocker con Alpine
set -e

CONTAINER_NAME="claude-env"
IMAGE="alpine"
URL="https://github.com/anthropics/claude-code/releases/download/v2.1.119/claude-linux-arm64-musl.tar.gz"

echo "[*] Descargando imagen $IMAGE..."
udocker pull $IMAGE

echo "[*] Creando contenedor $CONTAINER_NAME..."
# Si ya existe, lo borramos para reinstalar limpiamente
udocker rm $CONTAINER_NAME 2>/dev/null || true
udocker create --name=$CONTAINER_NAME $IMAGE

echo "[*] Configurando dependencias y descargando Claude..."
udocker run $CONTAINER_NAME /bin/sh -c "
  apk add --no-cache curl tar ca-certificates && \
  curl -L $URL -o /tmp/claude.tar.gz && \
  tar -zxf /tmp/claude.tar.gz -C /usr/local/bin && \
  rm /tmp/claude.tar.gz && \
  chmod +x /usr/local/bin/claude
"

echo "[+] Instalación completada con éxito."
