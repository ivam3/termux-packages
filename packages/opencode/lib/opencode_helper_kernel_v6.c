#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char** argv) {
    // 1. Limpiar entorno de Android/Termux para evitar conflictos con Bionic
    unsetenv("LD_PRELOAD");
    unsetenv("LD_LIBRARY_PATH");

    // 2. Forzar modo compatible para Bun en Android 14 (Kernel 6.1)
    // Desactivar el JIT es crítico para evitar SIGTRAP en Android 14
    setenv("JSC_useJIT", "false", 1);
    
    // Indica a Bun que estamos en un entorno con ejecución transparente
    setenv("BUN_RUNTIME_TRANSPARENT_EXEC", "1", 1);
    
    // TMPDIR es vital: Bun necesita escribir archivos temporales y /tmp no existe
    setenv("TMPDIR", "/data/data/com.termux/files/home/.opencode", 1);

    // 3. Ruta al binario real de opencode (ya parcheado con patchelf)
    char* real_bin = "/data/data/com.termux/files/home/.local/share/opencode/opencode.real";
    
    // 4. Ejecutar directamente el binario real
    // Como ya usamos 'patchelf --set-interpreter', el binario sabe cargar su glibc solo.
    if (execv(real_bin, argv) == -1) {
        perror("Error al ejecutar opencode.real (¿Existe el archivo?)");
        return 1;
    }

    return 0;
}
