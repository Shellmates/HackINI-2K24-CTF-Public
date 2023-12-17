FROM ubuntu:latest

RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive apt-get install -y \
        vim curl \
        apache2 libapache2-mod-wsgi-py3 \
        python3 python3-pip


COPY challenge/apps/ /var/www/

COPY challenge/requirements.txt /var/www/
RUN pip install -r /var/www/requirements.txt

COPY challenge/wsgi-apps.conf /etc/apache2/sites-available/000-default.conf
RUN a2ensite 000-default

COPY challenge/flag /flag
RUN chmod 111 /flag

ENV SECRET_KEY=b7bb70a3b3c95f570a8d31ece41bf7c5
CMD python3 /var/www/secret-service/app.py & echo "127.0.0.1 hr.dep.shellmates.org acc.dep.shellmates.org secret-service.dep.shellmates.org">>/etc/hosts && apachectl -D FOREGROUND
