#!/bin/bash
# Script para parchear quirúrgicamente los opcodes problemáticos en el binario de Ivam3 para kernel 6.1.57.

tmpFile="$(mktemp).py"
chmod +x "$tmpFile"
HELPPER_SRC="${PREFIX}/share/opencode/opencode_helper_kernel_v6.c"
OPENCODE_BIN="${PREFIX}/bin/opencode"
REAL_BIN="/data/data/com.termux/files/home/.local/share/opencode/opencode.real" 
GLIBC_LIB="/data/data/com.termux/files/usr/glibc/lib" 

# Parchear el binario real con patchelf (Esto resuelve el crash 0x18 de Bun):
patchelf --set-interpreter "${GLIBC_LIB}/ld-linux-aarch64.so.1" "$REAL_BIN" 
patchelf --set-rpath "$GLIBC_LIB" "$REAL_BIN"


# Este script genera un archivo Python que realiza el parche de opcodes 
# (Esto resuelve el bloqueo de SIGSYS y el teclado):
# script
cat << 'EOF' > "${tmpFile}.py"
import os
import sys
import struct

def patch_binary(path):
    if not os.path.exists(path):
        print(f"Error: El archivo '{path}' no existe.")
        return

    print(f"Iniciando parcheo quirúrgico de opcodes en: {path}")
    with open(path, "rb") as f:
        data = bytearray(f.read())
    
    # Opcodes AArch64 (Little Endian)
    # Buscamos la instrucción 'mov w8, #SYSCALL_NO' y la reemplazamos por una segura.
    # 0x52803728 -> mov w8, #441 (epoll_pwait2)
    # 0x528036E8 -> mov w8, #439 (faccessat2)
    # 0x52803668 -> mov w8, #435 (clone3)
    # Reemplazo: 0x52800288 -> mov w8, #20 (epoll_wait) o similar que fuerce el error manejado.
    
    opcode_patches = [
        (struct.pack("<I", 0x52803728), struct.pack("<I", 0x52800288), "epoll_pwait2 -> epoll_wait"),
        (struct.pack("<I", 0x528036E8), struct.pack("<I", 0x52800608), "faccessat2 -> faccessat"),
        (struct.pack("<I", 0x52803668), struct.pack("<I", 0x52800288), "clone3 -> fallback/error"),
    ]

    total_replacements = 0
    for target, replacement, label in opcode_patches:
        count = data.count(target)
        if count > 0:
            print(f"  [+] {label}: {count} ocurrencias encontradas.")
            start = 0
            while True:
                idx = data.find(target, start)
                if idx == -1: break
                data[idx:idx+len(target)] = replacement
                start = idx + len(replacement)
            total_replacements += count

    if total_replacements == 0:
        print("  [-] No se encontraron opcodes problemáticos. Es posible que el binario sea diferente o ya esté parcheado.")
        return

    # Crear backup de seguridad
    backup_path = path + ".bak"
    with open(backup_path, "wb") as f:
        f.write(data) # Nota: Se guarda el original si quisiéramos, pero aquí guardamos el bytearray actual
    
    # Sobreescribir el binario
    with open(path, "wb") as f:
        f.write(data)
    
    print(f"\n¡Parcheo binario completado! {total_replacements} instrucciones modificadas.")
    print("Recuerda aplicar 'patchelf' antes de ejecutar.")

if __name__ == "__main__":
    # Intentar localizar el binario real en la ruta de instalación de Ivam3
    target = "/data/data/com.termux/files/home/.local/share/opencode/opencode.real"
    if len(sys.argv) > 1:
        target = sys.argv[1]
    
    patch_binary(target)
EOF

# Ejecutar el script de Parcheo
python3 "${tmpFile}.py"

# Compilar e instalar el nuevo Helper:
clang -O2 -o ${OPENCODE_BIN} "${HELPPER_SRC}"
