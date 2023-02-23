[[ -e /etc/resolv.conf ]] || { touch /etc/resolv.conf;}
chk=$(grep -oE "8.8.8.8" /etc/resolv.conf)
if [[ -z $chk ]]; then
  echo "nameserver 8.8.8.8" >> /etc/resolv.conf
fi
