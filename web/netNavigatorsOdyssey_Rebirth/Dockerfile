FROM python:3.9-alpine

RUN apk add --update --no-cache libcurl curl-dev build-base supervisor

RUN apk add --no-cache iproute2

WORKDIR /app

COPY app .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN mv flag.txt /flag.txt

EXPOSE 5000

# Setup supervisor
COPY config/supervisord.conf /etc/supervisord.conf

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

# Run supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
