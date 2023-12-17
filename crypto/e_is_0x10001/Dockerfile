FROM python:3.8-slim

WORKDIR /app

COPY challenge /challenge

WORKDIR /challenge

RUN pip install -r requirements.txt

CMD ["python", "app.py"]