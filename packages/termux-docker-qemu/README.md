# termux-docker-qemu

> Manage Docker containers from Linux x86, x86_64, ARMv7 and AArch64 virtual machines using QEMU (Quick EMUlator).

## Installation

```bash
pkg install termux-docker-qemu
```

## Info

| Field | Value |
|-------|-------|
| Version | `0.9.4` |
| Architecture | `all` |
| Maintainer | [Ivam3](https://t.me/Ivam3_Bot) |
| Homepage | [termux-docker-qemu](https://github.com/ivam3/termux-packages/blob/gh-pages/packages/termux-docker-qemu/README.md) |

## Dependencies

`openssh, wget, samba, procps, net-tools, xorg-xrandr, xfwm4, xdotool, termux-x11-nightly, qemu-utils, qemu-common, qemu-system-x86-64`

## Usage

```bash
termux-docker-qemu [options]
```

### Modes of Operation

**1. Headless (no display, SSH only)**

```bash
termux-docker-qemu alpine
```

Starts the VM without any graphical output. Connect via SSH on port 2222:

```bash
ssh root@localhost -p 2222
```

**2. X11 / SDL display (VirtIO 3D Hardware Accelerated)**

```bash
termux-docker-qemu alpine x11 sdl
```

Launches the VM with an SDL window using VirtIO-GPU 3D (virgl) through Termux:X11.

**3. X11 / VNC display**

```bash
termux-docker-qemu alpine x11 vnc
```

Starts the VM with a VNC server. Connect with any VNC client to `localhost:5900`.

**4. Direct X11 TCP Bridge (Ultra Lightweight)**

```bash
termux-docker-qemu alpine x11 tcp
```

Launches QEMU in headless mode (`-nographic`) while bridging host Termux:X11 socket to TCP port 6000 via `socat`. Alpine apps send X11 drawing commands directly over TCP to the host Termux:X11 display without QEMU frame translation overhead. Inside Alpine:

```sh
source /termux2alpine/x11_env.sh
xfce4-terminal &   # or xfce4-session &
```

---

### Initial Setup (manual)

```bash
# 1. Install QEMU
pkg install qemu-utils qemu-common qemu-system-x86-64

# 2. Download Alpine Linux (virt-optimised) ISO
mkdir alpine && cd $_
wget http://dl-cdn.alpinelinux.org/alpine/v3.12/releases/x86_64/alpine-virt-3.12.3-x86_64.iso

# 3. Create disk image (~500 MB actual usage)
qemu-img create -f qcow2 alpine.img 4G

# 4. Boot the installer
qemu-system-x86_64 -machine q35 -m 1024 -smp cpus=2 -cpu qemu64 \
  -drive if=pflash,format=raw,read-only=on,file=$PREFIX/share/qemu/edk2-x86_64-code.fd \
  -netdev user,id=n1,hostfwd=tcp::2222-:22 -device virtio-net,netdev=n1 \
  -cdrom alpine-virt-3.12.3-x86_64.iso \
  -nographic alpine.img

# 5. Login as root (no password), set up network
setup-interfaces   # press Enter for defaults
ifup eth0

# 6. Download answerfile and patch serial console
wget https://gist.githubusercontent.com/oofnikj/e79aef095cd08756f7f26ed244355d62/raw/answerfile
sed -i -E 's/(local kernel_opts)=.*/\1="console=ttyS0"/' /sbin/setup-disk

# 7. Run installation
setup-alpine -f answerfile

# 8. Power off, then boot without CD-ROM
qemu-system-x86_64 -machine q35 -m 1024 -smp cpus=2 -cpu qemu64 \
  -drive if=pflash,format=raw,read-only,file=$PREFIX/share/qemu/edk2-x86_64-code.fd \
  -netdev user,id=n1,hostfwd=tcp::2222-:22 -device virtio-net,netdev=n1 \
  -nographic alpine.img

# 9. Install Docker and enable on boot
apk update && apk add docker
service docker start
rc-update add docker
```

### Useful Key Bindings

| Shortcut | Action |
|----------|--------|
| `Ctrl+a x` | Quit QEMU emulation |
| `Ctrl+a h` | Toggle QEMU monitor console |

---

## VirtIO-GPU Acceleration

Starting with **version 0.9.4**, `termux-docker-qemu` supports hardware-accelerated graphics via the **virgl** (VirtIO-GPU 3D) pipeline.

### How It Works

Instead of the default software renderer, the VM is started with:

```bash
-device virtio-vga-gl \
-display sdl,gl=on
```

- `-device virtio-vga-gl` — exposes a VirtIO-GPU device with OpenGL passthrough to the guest.
- `-display sdl,gl=on` — enables the SDL display backend with host OpenGL acceleration, feeding real GPU frames to the guest through virgl.

This replaces software rendering (llvmpipe/softpipe) with the host GPU pipeline, delivering significantly better 2D/3D performance inside the VM.

### Guest Setup (Alpine Linux)

After booting with VirtIO-GPU, install the required Mesa drivers inside Alpine:

```bash
apk add mesa-dri-gallium mesa-egl mesa-gl
```

- `mesa-dri-gallium` — Gallium3D DRI drivers (virgl backend).
- `mesa-egl` — EGL support for hardware-accelerated rendering.
- `mesa-gl` — OpenGL library.

### Requirements

- Termux:X11 must be running before launching the VM.
- The host device must support OpenGL ES 3.0 or higher (most modern Android devices).
- Use `sdl` mode (`termux-docker-qemu alpine x11 sdl`) to take advantage of GPU acceleration.

---

## Direct X11 TCP Bridge (Ultra-Lightweight Display)

Starting with **version 0.9.4**, `termux-docker-qemu` also introduces the **TCP Bridge** mode (`termux-docker-qemu alpine x11 tcp`).

### How It Works

1. **Zero QEMU Framebuffer Overhead**: QEMU runs in `-nographic` mode, consuming minimal host CPU.
2. **Dynamic Socket Bridge**: A `socat` background process bridges host TCP port `6000` directly to Termux:X11's UNIX domain socket (`${PREFIX}/tmp/.X11-unix/X0`).
3. **Dynamic Host IP Resolution**: Automatically computes host gateway IP (`${ipnet}2`, e.g. `192.168.1.2` on WiFi or `10.0.2.2` offline) and exports it into `/termux2alpine/x11_env.sh`.

### Usage inside Alpine

```sh
source /termux2alpine/x11_env.sh  # exports DISPLAY=${host_ip}:0
xfce4-terminal &                 # opens window directly in Termux:X11
# or launch full session:
xfce4-session &
```

---

## Part of i-HakLab

This package is part of the [i-HakLab](https://github.com/Ivam3/i-HakLab) ecosystem — a comprehensive hacking toolkit for Android/Termux.

```bash
pkg install i-haklab
```
