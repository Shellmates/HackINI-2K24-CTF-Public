from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

fixed_username = "student"
fixed_password = "student-2023"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == fixed_username and password == fixed_password:
        role = "student"
        if role == "student":
            return jsonify({'message': 'Login successful', 'role': role})
    else: return jsonify({'message': 'Not allowed'})

if __name__ == '__main__':
    app.run(debug=False)
