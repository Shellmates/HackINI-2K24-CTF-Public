#!/bin/sh

EXEC="./vuln"
PORT=3040

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr
