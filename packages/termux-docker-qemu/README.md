Docker on Termux With QEMU [in a VM]
    * Install QEMU
       pkg install qemu-utils qemu-common qemu-system-x86_64-headless
    * Download Alpine Linux 3.12 (virt optimized) ISO
       mkdir alpine && cd $_
       wget http://dl-cdn.alpinelinux.org/alpine/v3.12/releases/x86_64/alpine-
      virt-3.12.3-x86_64.iso
    * Create disk (note it won't actually take 4GB of space, more like 500MB)
       qemu-img create -f qcow2 alpine.img 4G
    * Boot it up
      qemu-system-x86_64 -machine q35 -m 1024 -smp cpus=2 -cpu qemu64 \
        -drive if=pflash,format=raw,read-only,file=$PREFIX/share/qemu/edk2-
      x86_64-code.fd \
        -netdev user,id=n1,hostfwd=tcp::2222-:22 -device virtio-net,netdev=n1 \
        -cdrom alpine-virt-3.12.3-x86_64.iso \
        -nographic alpine.img
    * Login with user root (no password)
    * Setup network (press Enter to use defaults):
       localhost:~# setup-interfaces
       Available interfaces are: eth0.
       Enter '?' for help on bridges, bonding and vlans.
       Which one do you want to initialize? (or '?' or 'done') [eth0]
       Ip address for eth0? (or 'dhcp', 'none', '?') [dhcp]
       Do you want to do any manual network configuration? [no]
       localhost:~# ifup eth0
    * Create an answerfile to speed up installation:
      localhost:~# wget https://gist.githubusercontent.com/oofnikj/
      e79aef095cd08756f7f26ed244355d62/raw/answerfile
    * Patch setup-disk to enable serial console output on boot
      localhost:~# sed -i -E 's/(local kernel_opts)=.*/\1="console=ttyS0"/' /
      sbin/setup-disk
    * Run setup to install to disk
      localhost:~# setup-alpine -f answerfile
    * Once installation is complete, power off the VM (command poweroff) and boot again without cdrom:
      qemu-system-x86_64 -machine q35 -m 1024 -smp cpus=2 -cpu qemu64 \
        -drive if=pflash,format=raw,read-only,file=$PREFIX/share/qemu/edk2-
      x86_64-code.fd \
        -netdev user,id=n1,hostfwd=tcp::2222-:22 -device virtio-net,netdev=n1 \
        -nographic alpine.img
    * Install docker and enable on boot:
      alpine:~# apk update && apk add docker
      alpine:~# service docker start
      alpine:~# rc-update add docker
    * Useful keys:
          o Ctrl+a x: quit emulation
          o Ctrl+a h: toggle QEMU console
