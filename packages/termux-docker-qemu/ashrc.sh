[[ -e /dev/net/tun ]] || { mkdir -p /dev/net/ 2>/dev/null && mknod /dev/net/tun c 10 200;}
[[ -d /root/.local/bin ]] || { mkdir -p /root/.local/bin;}
[[ -e /etc/resolv.conf ]] || { touch /etc/resolv.conf;}
[[ -d /termux2alpine ]] || { mkdir /termux2alpine;}

r=$(stty size|awk -F " " '{print $1}')
c=$(stty size|awk -F " " '{print $2}')
stty rows $r columns $c

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

export PATH="/root/.local/bin:$PATH"

if ! command -v tmux >/dev/null; then
  echo "Installing tmux ..."
  apk update
  apk upgrade
  apk add tmux git perl
  cd;git clone https://github.com/gpakosz/.tmux.git
  ln -s -f .tmux/.tmux.conf
  cp .tmux/.tmux.conf.local .
fi

s=$(tmux list-session|grep "QEMU") 2>/dev/null
if [ -z $s ]; then 
  tmux new -s QEMU -n main 2>/dev/null
else
  tmux attach-session
fi
###   @Ivam3 
