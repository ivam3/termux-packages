# Playwright-proot 🎭

**Playwright CLI** para Termux via **proroot** (Ubuntu 24.04). Permite automatización de navegador (snapshot, screenshot, click, fill, eval) para testing de PWAs y apps web en Android.

## 📥 Instalación

```bash
apt install playwright-proot
```

El `postinst` configura automáticamente:
1. proroot rootfs (dependencia)
2. Librerías glibc para Chromium
3. Node.js + @playwright/cli
4. Chromium headless (arm64)

## 🚀 Uso

### 1. Iniciar servidor target (ej: Flet)
```bash
flet run --web --port 8550 main.py
```

### 2. Abrir navegador + attach playwright
```bash
playwright-proot open http://localhost:8550
```

### 3. Ejecutar comandos
```bash
playwright-proot snapshot
playwright-proot click e2
playwright-proot screenshot
```

### 4. Cerrar
```bash
playwright-proot close
```

## 🏗️ Arquitectura

```
Termux (Host)
├── Python + Flet → flet run --web --port 8550 main.py
└── proroot (Ubuntu 24.04, sin ptrace)
    ├── Node.js + @playwright/cli
    ├── Chromium headless (glibc arm64)
    └── playwright-cli attach --cdp=http://localhost:9222
```

## 📋 Requisitos

- `proroot` (se instala automáticamente como dependencia)
- ~1.2GB de espacio para Ubuntu + Chromium
- Conexión a internet para la instalación inicial

## 🤝 Soporte

Reporta issues: https://t.me/Ivam3_Bot
