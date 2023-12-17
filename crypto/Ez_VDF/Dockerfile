FROM python:3.10-alpine

RUN apk add socat

RUN pip3 install pycryptodome 

RUN mkdir /challenge

WORKDIR /challenge

EXPOSE 8000

COPY ./entrypoint.sh .
COPY ./challenge/challenge.py .
RUN chmod +x /challenge/entrypoint.sh 
RUN chmod +x /challenge/challenge.py

CMD ["sh", "/challenge/entrypoint.sh"]
