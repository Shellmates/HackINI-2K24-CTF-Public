FROM ubuntu:latest

RUN apt-get update &&  apt-get install socat -y && apt-get install gcc-multilib -y

COPY challenge /challenge

WORKDIR /challenge

RUN chmod +x ./9indil/entrypoint.sh && \
    chown -R root:root . && \
    chmod +x ./9indil/9indil
WORKDIR /challenge/9indil
EXPOSE 1337

ENTRYPOINT ["/challenge/9indil/entrypoint.sh"]
