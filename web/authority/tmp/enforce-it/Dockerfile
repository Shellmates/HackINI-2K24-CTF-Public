FROM node:16-alpine

RUN apk add --update curl-dev #libcurl4-openssl-dev

RUN mkdir -p /server/app /server/app/views /server/app/views/server/internal /server/hidden

WORKDIR /server/app

COPY app/views/*.ejs views/
COPY app/package.json .
COPY app/app.js .

RUN npm install

WORKDIR /server/internal

COPY internal/package.json .
COPY internal/internal.js .

RUN npm install

WORKDIR /server/hidden

COPY hidden/package.json .
COPY hidden/hidden.js .

RUN npm install

WORKDIR /server

COPY .env /server/

COPY entrypoint.sh /

RUN chmod u+x /entrypoint.sh

EXPOSE 8080

CMD [ "/entrypoint.sh" ]
