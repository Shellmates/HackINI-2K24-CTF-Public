FROM python:3.9-alpine

RUN apk add --update --no-cache libcurl curl-dev build-base supervisor

RUN apk add --no-cache iproute2

WORKDIR /app

COPY app .

RUN mv flag.txt /flag$(cat /dev/urandom | tr -cd 'a-f0-9' | head -c 10).txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

COPY config/supervisord.conf /etc/supervisord.conf

ENV PYTHONDONTWRITEBYTECODE=1

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
