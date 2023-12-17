FROM node:20-alpine

RUN apk update && apk upgrade
RUN apk add chromium 

ENV FLAG="shellmates{dONT_LET_PEOpl3_G0_wh3R3_you_DOnt_wAnT_tH3m_t0_6tb23c}"

RUN mkdir /app
WORKDIR /app
COPY ./challenge/ .
RUN PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true yarn
# create user `bot`
RUN adduser -D -u 1001 bot && \
    mkdir -p /home/bot && \
    chown -R bot:bot /home/bot

COPY . .
USER bot
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser
EXPOSE 3000
ENTRYPOINT ["node", "index.js"]
