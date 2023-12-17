FROM python:3.10-alpine

RUN apk update && \
    apk add socat 

RUN adduser --disabled-password --no-create-home ctf

COPY challenge /usr/src/app/

WORKDIR /usr/src/app

RUN chmod +x ./entrypoint.sh

RUN chmod +x ./challenge.py

EXPOSE 1337

ENTRYPOINT ["./entrypoint.sh"]
