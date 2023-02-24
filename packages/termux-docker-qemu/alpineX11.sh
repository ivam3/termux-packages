echo "Installing x11 dependencies and setting file ..."
setup-xorg-base xfce4 xfce4-terminal dbus-x11 thunar-volman
rc-service dbus start
rc-update add dbus
rc-service udev start
rc-update add udev
apk add lightdm-gtk-greeter
rc-update add lightdm
apk add polkit consolekit2 firefox
echo "Installation finished."
echo "The system will shutdown"
echo "Re-start it with 'termux-docker-qemu alpine x11' for a graphical enviroment"
echo "Press ENTER to continue."
poweroff
