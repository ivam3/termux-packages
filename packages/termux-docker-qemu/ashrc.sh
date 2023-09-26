[[ ! -e /dev/net/tun ]] || { mkdir -p /dev/net/ 2>/dev/null && mknod /dev/net/tun c 10 200;}
[[ -e /etc/resolv.conf ]] || { touch /etc/resolv.conf;}
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
