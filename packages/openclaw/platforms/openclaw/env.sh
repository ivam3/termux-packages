#!/usr/bin/env bash
# env.sh — OpenClaw platform environment variables
# Called by setup-env.sh; stdout is inserted into .bashrc block.
# Uses single-quoted heredoc to prevent variable expansion at install time
# (variables must expand at shell load time).

cat << 'EOF'
export CONTAINER=1
export CLAWDHUB_WORKDIR="$HOME/.openclaw/workspace"
export CPATH="$PREFIX/include/glib-2.0:$PREFIX/lib/glib-2.0/include"
EOF
