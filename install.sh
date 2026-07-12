#!/data/data/com.termux/files/usr/bin/bash
set -e

# Si no se pasó ningún paquete, instala i-haklab
if [ $# -eq 0 ]; then
	set -- i-haklab
fi

# Dependencias
command -v gpg >/dev/null || apt install -y gnupg
command -v curl >/dev/null || apt install -y curl
command -v tee >/dev/null || apt install -y coreutils

# Agregar repositorio
mkdir -p "$PREFIX/etc/apt/sources.list.d"

curl -fsSL \
	"https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/ivam3-termux-packages.list" \
	-o "$PREFIX/etc/apt/sources.list.d/ivam3-termux-packages.list"

# Importar llave GPG
curl -fsSL \
	"https://raw.githubusercontent.com/ivam3/termux-packages/gh-pages/docs/dists/stable/public_key.gpg" |
	gpg --dearmor |
	tee "$PREFIX/etc/apt/trusted.gpg.d/ivam3.gpg" >/dev/null

# Actualizar índices
apt update

# Instalar uno o varios paquetes
apt install -y "$@"
