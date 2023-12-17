#!/bin/bash

socat -dd -T60 TCP-LISTEN:8000,reuseaddr,fork,su=root EXEC:/challenge/challenge.py,stderr
