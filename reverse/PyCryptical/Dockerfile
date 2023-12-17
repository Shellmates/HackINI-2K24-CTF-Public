FROM python:2-alpine

WORKDIR /app

COPY . /app

ENV PASSPHRASE=R3vers3_My_B3l0v3d__r3veR5e

EXPOSE 1337

CMD ["nc", "-lk", "-np", "1337", "-e", "python", "chall.py"]
