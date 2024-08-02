[[ -e /dev/net/tun ]] || { mkdir -p /dev/net/ 2>/dev/null && mknod /dev/net/tun c 10 200;}
[[ -d /root/.local/bin ]] || { mkdir -p /root/.local/bin;}
[[ -e /etc/resolv.conf ]] || { touch /etc/resolv.conf;}
[[ -d /termux2alpine ]] || { mkdir /termux2alpine;}

# RESIZE SCREEN run in Termux session 'tty size' to get the real value of your screen 
stty rows 18 columns 140 # CHANGE IT IF YOUR SCREEN SIZE IS DIFERENT 

! $(command -v grep) "termux2alpine" /etc/fstab >/dev/null && {
  mount -t 9p -o trans=virtio termux2alpine /termux2alpine
  echo "termux2alpine  /termux2alpine 9p trans=virtio 0 0" >> /etc/fstab
}

chk=$(grep -oE "8.8.8.8" /etc/resolv.conf)

if [[ -z $chk ]]; then
  echo "nameserver 8.8.8.8" >> /etc/resolv.conf
fi

if ! command -v docker >/dev/null; then
  apk update
  apk upgrade
  apk add docker
  service docker start
  rc-update add docker
fi

if ! command -v tmux >/dev/null; then
  apk update
  apk upgrade
  apk add tmux perl
  cd;git clone https://github.com/gpakosz/.tmux.git 
  ln -s -f .tmux/.tmux.conf
  cp .tmux/.tmux.conf.local .
fi

command -v tmux attach-session 2>/dev/null || tmux new -s i-Haklab -n main

export PATH="/root/.local/bin:$PATH"
###   @Ivam3 
