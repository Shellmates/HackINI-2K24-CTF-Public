FROM ubuntu:22.04


RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 socat \
    && apt-get clean

RUN useradd ctf && \
    mkdir /challenge

COPY challenge /challenge

WORKDIR /challenge

RUN chown -R root:root . && \
    chmod +x vuln entrypoint.sh

EXPOSE 3040

USER ctf

ENTRYPOINT [ "./entrypoint.sh" ]
