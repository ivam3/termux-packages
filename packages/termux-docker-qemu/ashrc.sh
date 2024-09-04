### FIX NETWORK CONECDTI0N 
[[ -e /dev/net/tun ]] || { mkdir -p /dev/net/ 2>/dev/null && mknod /dev/net/tun c 10 200;}
[[ -d /root/.local/bin ]] || { mkdir -p /root/.local/bin;}
[[ -e /etc/resolv.conf ]] || { touch /etc/resolv.conf;}
[[ -d /termux2alpine ]] || { mkdir /termux2alpine;}

## SET SCREEN SIZE 
set rows
set columns
if [ -z $rows ] || [ -z $columns ]; then
  echo "[+] Set screen size (recommend | 31rows & 131columns)"
  for i in rows columns; do
    while read -p "Number of $i: " d && [ -z $d ]; do
      continue
    done
    sed -i "s|set $i|$i=$d|" /etc/profile.d/ashrc.sh
  done
fi
stty rows $row columns $columns 2>/dev/null

## SET SHARED DIRECTORY BETWEEN BOTH OS 
! $(command -v grep) "termux2alpine" /etc/fstab >/dev/null && {
  mount -t 9p -o trans=virtio termux2alpine /termux2alpine
  echo "termux2alpine  /termux2alpine 9p trans=virtio 0 0" >> /etc/fstab
}

## SET APK MIRRORS
! $(command -v grep) "@testining" /etc/apk/repositories >/dev/null && {
  echo """http://dl-cdn.alpinelinux.org/alpine/latest-stable/main
http://dl-cdn.alpinelinux.org/alpine/latest-stable/community
@testing https://dl-cdn.alpinelinux.org/alpine/edge/testing
""" > /etc/apk/repositories
}

## SET DNS 
chk=$(grep -oE "8.8.8.8" /etc/resolv.conf)
if [[ -z $chk ]]; then
  echo "nameserver 8.8.8.8" >> /etc/resolv.conf
fi

## EXPORT B8NARIES PATH 
export PATH="/root/.local/bin:$PATH"

## CONF PIP TO FORCE MODULE INSTALLATION IN ALPINE OS ENVIROMENT 
if command -v python3 >/dev/null; then 
  python3 -m pip config set global.break-system-packages true
fi

## INSTALL AND RUN DOCKER SERVICE 
if ! command -v docker >/dev/null; then
  apk update
  apk upgrade
  apk add docker
  service docker start
  rc-update add docker
fi

## INSTALL AND RUN PLEX TERMINAL TMUX 
if ! command -v tmux >/dev/null; then
  echo "Installing tmux ..."
  apk update
  apk upgrade
  apk add tmux git perl
  cd;git clone https://github.com/gpakosz/.tmux.git
  ln -s -f .tmux/.tmux.conf
  cp .tmux/.tmux.conf.local .
fi

#s=$(tmux list-session|grep "Alpine") 2>/dev/null
#if [ -z $s ]; then 
#  tmux new -s i-Haklab -n main 2>/dev/null
#else
#  tmux attach-session
#fi


###   @Ivam3 
