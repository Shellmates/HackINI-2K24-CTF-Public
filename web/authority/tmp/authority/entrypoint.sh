#!/bin/sh


# cd /server/internal/
node /server/internal/internal.js &

# cd /server/hidden/
node /server/hidden/hidden.js &

cd /server/app/
node /server/app/app.js 