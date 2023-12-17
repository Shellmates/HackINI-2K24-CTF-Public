FROM python:3-alpine

RUN apk update && \
	apk add socat

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN mkdir /challenge/

WORKDIR /challenge/

COPY ./challenge/ ./

RUN pip install -r requirements.txt

EXPOSE 1337

ENTRYPOINT ["/entrypoint.sh"]