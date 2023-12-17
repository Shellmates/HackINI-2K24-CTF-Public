FROM golang:1.21.5-alpine3.19

RUN apk add socat

COPY  challenge /challenge

WORKDIR /challenge

RUN chmod +x entrypoint.sh app

EXPOSE 6789

ENTRYPOINT ["./entrypoint.sh"]