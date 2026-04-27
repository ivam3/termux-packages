# Opencode for Termux 🚀

**Opencode** es un potente agente de codificación basado en IA, diseñado específicamente para la terminal. Esta versión está optimizada para **Termux (Android)**, utilizando un entorno híbrido con Alpine Linux para garantizar compatibilidad total y alto rendimiento sin abandonar tu sesión de terminal.

---

## 🛠 Características

- **Agente de IA Nativo:** Ejecuta el binario oficial de alto rendimiento (134MB+).
- **Entorno Robusto:** Utiliza la infraestructura de `proot-distro` para evitar conflictos de memoria con binarios de dirección fija (non-PIE).
- **Herencia de Entorno:** Mapeo automático de variables de entorno desde Termux a Alpine (claves de API, configuración de terminal, etc.).
- **Integración Transparente:** Tu carpeta `$HOME` de Termux es totalmente accesible dentro de Opencode.
- **Conectividad Estable:** Resolución DNS nativa y validación SSL/TLS configurada automáticamente.

---

## 📥 Instalación

Para instalar Opencode en tu entorno Termux, asegúrate de tener instalados los requisitos previos:

### Requisitos previos
- `proot-distro` (con la distribución `alpine` instalada)
- `curl`

### Preparación de Alpine
```bash
proot-distro install alpine
proot-distro login alpine -- apk add --no-cache musl ca-certificates libstdc++ libgcc gcompat
```

> **Nota:** El comando `opencode` se encargará de gestionar el puente entre Termux y Alpine automáticamente.

---

## ⚙️ Configuración

### 1. Variables de Entorno (Recomendado)
Opencode heredará automáticamente cualquier variable de entorno que exportes en Termux. Puedes añadir tus claves a tu `.bashrc` o `.zshrc`:
```bash
export ANTHROPIC_API_KEY="tu_clave_aqui"
```

### 2. Archivo .env
También puedes usar el archivo de configuración tradicional:
```bash
nano ~/.opencode/.env
```

---

## 🚀 Uso

Simplemente ejecuta el comando en tu terminal de Termux:

```bash
opencode
```

Opencode se iniciará en tu carpeta personal (`/data/data/com.termux/files/home`) mapeada internamente, permitiéndote trabajar sobre tus proyectos locales directamente.

---

## 🔍 Detalles Técnicos (The "Bridge" Implementation)

A diferencia de otros ports, esta implementación utiliza un enfoque de **Aislamiento dinámico**:

1. **Gestión de Memoria:** Dado que el binario de Opencode es un ejecutable de tipo `EXEC` (dirección fija), se utiliza `proot-distro` para inicializar un mapa de memoria limpio que evita colisiones con las librerías de Android (Bionic).
2. **Puente de Entorno:** Un script envolvente filtra y traslada dinámicamente tus variables de sesión hacia el contenedor Alpine, excluyendo aquellas que causarían inestabilidad (como `PATH` o `LD_PRELOAD`).
3. **Mapeo de Red:** Se utiliza un montaje quirúrgico de los servicios de resolución de nombres de Alpine para asegurar que las llamadas a las APIs de LLM nunca fallen por problemas de DNS o certificados SSL.

---

## 🤝 Soporte y Reportes

Si encuentras algún problema o tienes sugerencias:

- **Mantenedor:** [Ivam3](https://t.me/Ivam3_Bot)
- **Repositorio Original:** [opencode-ai/opencode](https://github.com/opencode-ai/opencode)

---

## 💡 Créditos

- Basado en el trabajo original de **AnomalyCo**.
- Optimización y puente de arquitectura para Termux por **Ivam3**.
- ¡Gracias por potenciar el desarrollo móvil con IA!
