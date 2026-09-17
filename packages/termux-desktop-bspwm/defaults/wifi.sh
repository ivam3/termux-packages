#!/data/data/com.termux/files/usr/bin/sh
# wifi via Termux:API (netlink is blocked by SELinux, internal/network is useless)
if command -v termux-wifi-connectioninfo >/dev/null 2>&1; then
  SSID=$(termux-wifi-connectioninfo 2>/dev/null | grep -o '"ssid": *"[^"]*"' | head -n 1 | sed 's/"ssid": *//;s/"//g')
  case "$SSID" in
    ""|"<unknown ssid>") echo "NET --" ;;
    *) echo "NET $SSID" ;;
  esac
else
  echo "NET --"
fi
