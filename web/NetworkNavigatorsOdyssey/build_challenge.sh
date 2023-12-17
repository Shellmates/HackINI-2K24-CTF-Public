#!/bin/bash
docker build -t networknavigatorsoddyssey . && docker run -p 5000:5000 -it networknavigatorsoddyssey

