FROM python:3.8-slim-buster

WORKDIR /app
RUN  apt update 
RUN  apt install -y tesseract-ocr
COPY ./app .

RUN pip3 install -r requirements.txt
  
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=1337"]
