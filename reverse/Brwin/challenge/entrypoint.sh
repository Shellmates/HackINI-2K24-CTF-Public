#!/bin/sh

EXEC="./checker"
PORT=9001

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr