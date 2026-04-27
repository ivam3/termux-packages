# Opencode for Termux 🚀

**Opencode** es un potente agente de codificación basado en IA, diseñado específicamente para la terminal. Esta versión está optimizada para ejecutarse de forma nativa en **Termux (Android)**, utilizando un puente de compatibilidad con librerías de Alpine Linux para garantizar el máximo rendimiento sin salir de tu entorno local.

---

## 🛠 Características

- **Agente de IA Nativo:** Ejecuta el binario oficial de alto rendimiento.
- **Entorno Híbrido:** Utiliza librerías `musl` de Alpine dentro de Termux (Bionic) mediante un cargador dinámico.
- **Conectividad Total:** Implementación de un túnel quirúrgico con `proot` para resolución DNS y validación SSL/TLS desde Android.
- **Ligero y Rápido:** No requiere iniciar una sesión completa de proot-distro; se ejecuta como un comando estándar de Termux.

---

## 📥 Instalación

Para instalar Opencode en tu entorno Termux, asegúrate de tener instalados los requisitos previos y ejecuta el script de instalación:

### Requisitos previos
- `proot-distro`
- `curl`

### Comando de Instalación
```bash
# El instalador descarga el binario y prepara el entorno
# (Asegúrate de ejecutar el script de post-instalación proporcionado)
```

> **Nota del Mantenedor:** El instalador configurará automáticamente un entorno Alpine mínimo necesario para las dependencias de ejecución.

---

## ⚙️ Configuración

Antes de empezar, debes configurar tus claves de API para que el agente pueda comunicarse con los modelos de lenguaje (LLM).

1. Crea o edita el archivo de entorno:
   ```bash
   nano ~/.opencode/.env
   ```
2. Añade tus credenciales (ejemplo):
   ```env
   ANTHROPIC_API_KEY=tu_api_key_aqui
   # Otras variables de configuración
   ```

---

## 🚀 Uso

Simplemente ejecuta el comando en tu terminal:

```bash
opencode
```

---

## 🔍 Detalles Técnicos (The "Bridge" Implementation)

Este proyecto utiliza una técnica avanzada de ejecución para superar la incompatibilidad entre la `libc` de Android (Bionic) y la de Linux estándar (Musl):

1. **Loader Musl:** Se utiliza el cargador dinámico de Alpine (`ld-musl-aarch64.so.1`) para mapear las librerías necesarias en memoria.
2. **PRoot Binding:** Para solucionar problemas de conexión ("Cannot connect to API"), el ejecutor mapea quirúrgicamente archivos críticos del sistema de archivos de Alpine hacia el entorno de ejecución:
   - `/etc/resolv.conf` & `/etc/hosts` para DNS.
   - `/etc/ssl` para certificados CA.
3. **Optimización de Memoria:** Al no ejecutar un sistema operativo completo, el impacto en la RAM es mínimo.

---

## 🤝 Soporte y Reportes

Si encuentras algún problema o tienes sugerencias, puedes contactar al mantenedor o reportar issues en:

- **Mantenedor:** [Ivam3](https://t.me/Ivam3_Bot)
- **Repositorio Original:** [opencode-ai/opencode](https://github.com/opencode-ai/opencode)

---

## 💡 Créditos

- Basado en el trabajo original de **AnomalyCo**.
- Empaquetado y optimización para Termux por **Ivam3**.
- ¡Gracias por usar este paquete!
