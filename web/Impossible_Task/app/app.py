from flask import Flask, request, jsonify, render_template
import requests
from unidecode import unidecode
app = Flask(__name__)
FLAG="shellmates{GETT1nG_FAT_w1Th_UN1C0DE_inj3CtiON}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/operation', methods=['GET',
                                # 'POST' I hope this should fix the issue
                                ])
def print_body_param():
    body_param = request.get_json()
    url = body_param.get('url', None)
    if url:
        # no points and no % => no external urls
        if ("%" in url) or ("." in url):
            return jsonify({"msg":"only requests to localhost are allowed"}),401
        # cleaning the url to store it later
        url=unidecode(url)
        url=url.replace(" ","")
        # sending request to local services
        try:
            res=requests.get(url+f"?secret={FLAG}")
            return jsonify({"msg":"request sent succesfully"}),200
        except:
            return jsonify({"msg":"soomething went wrong"}),500
    else:
        return jsonify({"msg":"no url was provided"}),400

if __name__ == '__main__':
    app.run(debug=False)
