#!/bin/sh

EXEC="./app"
socat -d -T60 tcp-l:6789,reuseaddr,fork,keepalive,su=nobody exec:$EXEC,stderr