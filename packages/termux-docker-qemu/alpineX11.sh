echo "Installing x11 dependencies and setting file ..."
setup-xorg-base
apk add xfce4 xfce4-terminal dbus-x11 thunar-volman
rc-service dbus start
rc-update add dbus
rc-service udev start
rc-update add udev
apk add lightdm-gtk-greeter
rc-update add lightdm
apk add polkit consolekit2
echo "autologin-user=root" >> /etc/lightdm/lightdm.conf
apk add firefox
echo "Installation finished."
echo "The system will shutdown"
echo "Re-start it with: termux-docker-qemu alpine x11 sdl"
echo "Press ENTER to continue."
poweroff
