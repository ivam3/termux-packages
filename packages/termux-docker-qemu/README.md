
# Create an answerfile to speed up installation
wget --tries=20 --quiet \
  https://gist.githubusercontent.com/oofnikj/e79aef095cd08756f7f26ed244355d62/raw/answerfile
# Patch setup-disk to enable serial console output on boot
localhost:~# sed -i -E 's/(local kernel_opts)=.*/\1="console=ttyS0"/' /sbin/setup-disk
# Run setup to install to disk
localhost:~# setup-$os -f answerfile
# Once installation is complete, power off the VM (command poweroff) and boot again without cdrom:

# Useful keys:
##Ctrl+a x: quit emulation
##Ctrl+a h: toggle QEMU console
#
