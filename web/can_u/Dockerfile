FROM python:3.10-alpine
    
RUN apk update && \
    apk add socat

RUN mkdir /challenge

WORKDIR /challenge

RUN pip3 install flask

EXPOSE 1337

COPY challenge/challenge.py /challenge/challenge.py

ENTRYPOINT ["python3", "/challenge/challenge.py"]