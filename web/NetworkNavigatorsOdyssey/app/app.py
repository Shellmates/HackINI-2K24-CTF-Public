from flask import Flask, render_template, request
import subprocess

whitelist = ["address", "link", "maddress" , "neighbor", "netconf", "ntable", "route", "rule", "tcpmetrics", "token"]
blacklist = [" ", "&", ";", "cat", "-", "less", "more", "head", "tail", "nl", "awk", "sed", "echo","tac", "rev", "strings", "paste", "cut","sort", "fmt", "xxd", "ob"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def ip():
    option = request.form['option']
    if any(character in option for character in blacklist):
        return "Malicious input detected."

    if not any(opt in option for opt in whitelist):
        return f"Sorry, but only these options are availabe: {whitelist}"
    
    try:
        result = subprocess.run(f"ip {option} show", shell=True, capture_output=True, text=True)
        return f'{result.stdout}'
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
