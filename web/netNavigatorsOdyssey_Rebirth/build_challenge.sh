#!/bin/bash
docker build -t phoenixrebirth . && docker run -p 5000:5000 -it phoenixrebirth

