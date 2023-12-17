from flask import Flask,request,jsonify
from secret import flag
from Crypto.Util.number import getPrime,bytes_to_long,long_to_bytes


p, q = getPrime(1024), getPrime(1024) 

n = p * q


phi = (p-1)*(q-1)

app = Flask(__name__)



@app.route('/')
def hello():
    return 'Hello, Welcome to my Encryption plateform!'

@app.route('/encrypt_message',methods=['POST'])
def encrypt():
    message, e = request.json["message"],request.json["e"]

    cipher_hex = long_to_bytes(pow(bytes_to_long(message.encode()), e, n)).hex()
    
    return jsonify({"cipher":cipher_hex,"n":n})

@app.route('/encrypt_flag',methods=['POST'])
def encrypt_flag():
    e = request.json["e"]
    try:
        assert e>1000
        cipher_hex = long_to_bytes(pow(bytes_to_long(flag.encode()), e, n)).hex()
        
        return jsonify({"cipher":cipher_hex,"n":n})
    except:
        return jsonify({"msg":"it won't be that easy"})

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")
