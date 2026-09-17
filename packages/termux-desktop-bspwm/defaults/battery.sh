#!/data/data/com.termux/files/usr/bin/sh
# battery via Termux:API (/sys is not readable for polybar on Android)
if command -v termux-battery-status >/dev/null 2>&1; then
  termux-battery-status 2>/dev/null | grep -o '"percentage": *[0-9]*' | grep -o '[0-9]*' | head -n 1 | sed 's/^/BAT /;s/$/%/'
else
  echo "BAT --"
fi
