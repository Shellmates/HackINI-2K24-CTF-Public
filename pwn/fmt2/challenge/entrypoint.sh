#!/bin/sh

EXEC="./chall"
PORT=3000

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr