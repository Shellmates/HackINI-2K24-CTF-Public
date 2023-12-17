#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)

flag = "shellmatess{c0ntr0l_th3_50urc3_p0rt5_4nd_y0u_c0ntr0l_th3_w0rld}"

@app.route("/", methods=["GET", "HEAD"])
def index():
    # check if there is a X-Forwarded-Port header then remote_port var gets the value of the header, else the remote_port var gets the value of the remote port
    remote_port = request.headers.get('X-Forwarded-Port', request.environ.get('REMOTE_PORT'))
    if type(remote_port) is str:
        remote_port = int(remote_port)

    if remote_port == 0o1337:
        return flag
    
    return f'The source port is {remote_port}, I want 0o1337.'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337, debug=False)
