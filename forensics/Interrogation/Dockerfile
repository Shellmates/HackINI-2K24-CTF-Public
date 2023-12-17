FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server sudo cron

RUN apt-get install -y software-properties-common && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 1484120AC4E9F8A1A577AEEE97A80C63C9D8B80B && \
    add-apt-repository 'deb [arch=amd64] https://pkg.osquery.io/deb deb main' 

RUN apt-get update && \
    apt-get install osquery

RUN useradd -rm -d /home/Moriarty -s /bin/bash Moriarty && \
    echo Moriarty:240335692a813479f810e7a79eb0d834 | chpasswd

RUN usermod -aG root Moriarty

RUN groupadd -g 1010 APT221

RUN useradd -rm -d /home/ctf -s /bin/bash ctf && \
    echo ctf:ctf | chpasswd

RUN mkdir /home/ctf/.osquery 

COPY challenge/sudoers /etc/sudoers

COPY ./challenge /challenge

RUN chmod o-rwx /challenge 

RUN chmod o-x /usr/bin/*

RUN chmod o+x /bin/bash /usr/bin/sudo /usr/bin/su 

RUN chmod g+x /usr/bin/osqueryi

RUN ln -s /dev/null /home/ctf/.osquery/.history

RUN /challenge/challenge
RUN ln -s /dev/null /home/ctf/.bash_history
ENTRYPOINT service ssh start \
        && tail -f /dev/null
