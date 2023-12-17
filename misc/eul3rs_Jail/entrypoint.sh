#!/bin/sh
EXEC="python3 script.py"
PORT=1337
socat -dd -T300 tcp-listen:"$PORT",reuseaddr,fork,keepalive,su=nobody exec:"$EXEC",stderr
