### ERROR: Ejecutable desalineado en ARM64 Bionic

- input 
```
cactus run Cactus-Compute/gemma-4-E2B-it 
```
- ouput
```
Running: /data/data/com.termux/files/home/.local/share/cactus/weights/gemma-4-e2b-it-cq4

error: "/data/data/com.termux/files/home/.local/share/cactus/python/cactus/bin/run": executable's TLS segment is underaligned: alignment is 8, needs to be at least 64 for ARM64 Bionic
```

NOTA1: en base al error anterior se procedio con el siguiente analisis


### Análisis del Error

**Error reportado:**
```text
error: "/data/data/com.termux/files/home/.local/share/cactus/python/cactus/bin/run": executable's TLS segment is underaligned: alignment is 8, needs to be at least 64 for ARM64 Bionic
```

#### 🔍 Causa Raíz
1. **Requisito del Linker de Android (`linker64` / Bionic):**
   En arquitecturas ARM64 (aarch64) bajo Android 10+ (API level 29+), el cargador dinámico de Android exige que el segmento **`PT_TLS` (Thread Local Storage)** de cualquier ejecutable ELF tenga una alineación de memoria (`p_align`) de **al menos 64 bytes (`0x40`)**.
2. **Compilador / Toolchain de Origen:**
   El ejecutable descargado por Cactus ([run](file:///data/data/com.termux/files/home/.local/share/cactus/python/cactus/bin/run)) fue compilado con una herramienta (NDK/Rust/GCC genérico) que generó un segmento `PT_TLS` con alineación de **8 bytes (`0x8`)**.
3. **Bloqueo de Ejecución:**
   Al intentar ejecutar `cactus run`, el linker de Android verifica `p_align < 64` y aborta inmediatamente la ejecución antes de iniciar el proceso.

---

### Plan de Soluciones y Estado Actual

#### Solución 1 (Aplicada y Verificada): Parchear el segmento TLS en la cabecera ELF
Modificamos directamente en la cabecera del archivo ejecutable la propiedad `p_align` del segmento `PT_TLS` para elevarla de `8` a `64` bytes (`0x40`).

Se ejecutó la siguiente modificación binaria:
```python
import struct

path = "/data/data/com.termux/files/home/.local/share/cactus/python/cactus/bin/run"

with open(path, "rb") as f:
    data = bytearray(f.read())

e_phoff, = struct.unpack("<Q", data[32:40])
e_phentsize, = struct.unpack("<H", data[54:56])
e_phnum, = struct.unpack("<H", data[56:58])

for i in range(e_phnum):
    off = e_phoff + i * e_phentsize
    p_type, = struct.unpack("<I", data[off:off+4])
    if p_type == 7:  # PT_TLS
        data[off+48:off+56] = struct.pack("<Q", 64)
        print("Alineación PT_TLS actualizada a 64 bytes")

with open(path, "wb") as f:
    f.write(data)
```

> **Estado:** **Resuelto**. El binario [run](file:///data/data/com.termux/files/home/.local/share/cactus/python/cactus/bin/run) ya tiene alineación `0x40` y se ejecuta sin errores en Termux.

---

#### Solución 2: Usar `termux-elf-cleaner`
Si en futuras actualizaciones de Cactus se descarga un nuevo ejecutable con este problema, se puede usar la herramienta de limpieza de ejecutables ELF propia de Termux:

```bash
pkg install termux-elf-cleaner
termux-elf-cleaner ~/.local/share/cactus/python/cactus/bin/run
```

---

#### Solución 3: Recompilar los binarios nativos con `cactus build`
En lugar de depender de los binarios precompilados descargados, puedes forzar a Cactus a generar los ejecutables utilizando los compiladores nativos de Termux (`clang`/`llvm` ajustados a la ABI de Bionic):

```bash
cactus build --android
```

---

### Resumen de Trabajo Realizado
- Se inspeccionó la cabecera ELF del ejecutable con `readelf` confirmando la desalineación de `PT_TLS` (`0x8`).
- Se creó una copia de seguridad (`run.bak`) y se aplicó el parche binario para cambiar la alineación a `0x40` (64 bytes).
- Se confirmó la correcta carga del modelo `Cactus-Compute/gemma-4-E2B-it` mediante `cactus run`.

---
Valida si la solucion aplicada  en **plan de solucion y estado actual** seria la corecta para el paquete cactus ($PWD) de termux-packages o es necesario la solucion 3
---
