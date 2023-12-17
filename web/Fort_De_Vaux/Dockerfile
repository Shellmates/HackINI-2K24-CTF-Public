FROM python:3.8-slim-buster

COPY app /app
WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=1337"]
