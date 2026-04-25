#!/data/data/com.termux/files/usr/bin/bash

! command -v udocker &>/dev/null && { 
    dep=$(apt list 2>/dev/null | grep tur-repo | grep -o "installed")
    if [[ -z "$dep" ]]; then
        pkg i tur-repo
    fi
    pkg i udocker
}

echo "[📢] Working directories:
 ╰──────➤ workspace path: $(pwd)
 ╰──────➤ root path: ${HOME}/.opencode
 ╰──────➤ set your API keys in file: $(pwd)/.env or ${HOME}/.opencode/.env
 " 
read -p "Press [Enter] to continue"

echo "[+] Running OpenCode with udocker..."

# Búsqueda de variables de entorno en orden de prioridad
ENV_ARGS=()
if [ -f ".env" ]; then
    # 1. Local del proyecto
    ENV_ARGS+=(--env-file=".env")
elif [ -f "$HOME/.opencode/.env" ]; then
    # 2. Específico de la app (Por de faul)
    ENV_ARGS+=(--env-file="$HOME/.opencode/.env")
elif [ -f "$HOME/.config/opencode/.env" ]; then
    # 3. Estándar XDG
    ENV_ARGS+=(--env-file="$HOME/.config/opencode/.env")
elif [ -f "$HOME/.env" ]; then
    # 4. Global de termux
    ENV_ARGS+=(--env-file="$HOME/.env")
fi

udocker run --rm "${ENV_ARGS[@]}" --hostenv \
    -v $(pwd):/home/opencode/workspace \
    -v $HOME/.opencode:/home/opencode/.opencode \
    -w /home/opencode/workspace \
    ghcr.io/anomalyco/opencode "$@"

