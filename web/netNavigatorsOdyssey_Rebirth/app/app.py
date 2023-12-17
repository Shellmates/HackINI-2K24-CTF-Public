from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def ip():
    option = request.form['option']
    # Check that user input doesn't contain any spaces
    if " " in option:
        return "No spaces are allowed."
    # Double the check by spliting user input into an array before passing it securely to subprocess.check_output()
    option = ['/sbin/ip'] + option.split()
    
    try:
        # Use shell=False to prevent any shell injections
        result = subprocess.check_output(option, text=True,timeout=1,stderr=subprocess.STDOUT, shell=False)
        return f'{result}'
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output}'
    except Exception as e:
        return f"Error {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
