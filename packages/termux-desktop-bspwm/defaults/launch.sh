#!/data/data/com.termux/files/usr/bin/bash
# launch/relaunch polybar on the "main" bar
export DISPLAY="${DISPLAY:-:0}"
export XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR:-${TMPDIR:-/tmp}}"
SOCK_DIR="${TMPDIR:-/tmp}"
# wait for the bspwm socket (on Termux it lives in $TMPDIR, not /tmp)
for i in 1 2 3 4 5 6 7 8 9 10; do
  ls "$SOCK_DIR"/bspwm_*-socket >/dev/null 2>&1 && break
  sleep 0.5
done
# polybar honors BSPWM_SOCKET (its /tmp default does not exist on Android)
export BSPWM_SOCKET
BSPWM_SOCKET=$(ls "$SOCK_DIR"/bspwm_*-socket 2>/dev/null | head -n 1)
pkill -x polybar 2>/dev/null
sleep 1
polybar main -c "$HOME/.config/polybar/config.ini" 2>"$HOME/.config/polybar/polybar.log" &
disown
