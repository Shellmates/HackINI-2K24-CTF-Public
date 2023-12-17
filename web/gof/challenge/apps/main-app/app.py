from flask import Flask, request, render_template
from urllib.request import urlopen
from utli import run_curl

ACCOUNTING_DEP_LINK = "http://acc.dep.shellmates.org"
HR_DEP_LINK = "http://hr.dep.shellmates.org"


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', accLink=ACCOUNTING_DEP_LINK, hrLink=HR_DEP_LINK)

@app.route("/request", methods=['POST'])
def serve():
    html = run_curl(request.form['service'])
    return html

@app.errorhandler(404)
def not_found(e):
    return render_template("error-404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("error-500.html "), 500
