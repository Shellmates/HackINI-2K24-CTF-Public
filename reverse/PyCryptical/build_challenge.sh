#!/bin/bash
docker build -t pycryptical . && docker run -it -e PASSPHRASE="R3vers3_My_B3l0v3d__r3veR5e" -p 1337:1337 -it pycryptical

