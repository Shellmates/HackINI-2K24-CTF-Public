from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

flag = os.popen("/flag").read()

@app.route("/flag", methods=["POST"])
def flag():
    try:
        data = request.get_json()
        secret = data.get('secret')
        if secret == SECRET_KEY:
            flag = os.popen("/flag").read()
            return jsonify({'success': True, 'flag': flag})
        else:
            return jsonify({'success': False, 'error': 'Invalid secret'})
    except Exception as e:
        return jsonify({'success': False, 'error': "Something Went wrong"})



@app.route("/flag", methods=["GET"])
def test():
    return "you can test your GET payloads here"


if __name__ == "__main__":
    app.run(port=5000)