import sqlite3
from flask import Flask, render_template, request, g, flash, request, redirect

from . import ocr



def connect_db():
    return sqlite3.connect(app.database+RO)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


ALLOWED_EXTENSIONS = {'png', 'jpg','jpeg'}

RO="?mode=ro"
def initdb(app) : 
    connection=sqlite3.connect(app.database)
    c = connection.cursor()
    c.execute("""DROP TABLE IF EXISTS flag""")
    c.execute("""DROP TABLE IF EXISTS users""")
    c.execute("""CREATE TABLE flag(flag TEXT)""")
    c.execute("""CREATE TABLE users(username TEXT)""")
    c.execute('INSERT INTO users VALUES("admin")')
    c.execute('INSERT INTO flag VALUES("Challenge inspired by this meme: https://imgur.com/a/TnUBNou . here is your flag: shellmates{YEaH_y0u_re_rigHt_who_WOULD_Do_THIs_?_XD}")')
    connection.commit()
    connection.close()

app = Flask(__name__)

app.database = "file:./data.db"

app.config['MAX_CONTENT_LENGTH'] = 1024*1024 ; 

initdb(app)
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    try :
        if request.method == 'POST':
            
                if 'file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file = request.files['file']
                if file.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                if file and allowed_file(file.filename):
                    uname = ocr.ocr(file).strip()
                    print(uname,"uname")
                    g.db = connect_db()
                    cur = g.db.execute('SELECT * FROM users WHERE username = "%s"'%(uname))
                    if res:=cur.fetchone():
                        return render_template("logged.html",user=res[0],admin=(uname=="admin"))
                    else:
                        return render_template("error.html")
        return render_template('index.html')
    except :
        return render_template("error.html",error ="Something went wrong !")



@app.errorhandler(413)
def page_not_found(e):
    return render_template("error.html",erro="File too big")


@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('error.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error=error)


