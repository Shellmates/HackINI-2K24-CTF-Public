from flask import Flask
from flask import request
from flask import render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    blacklist = ['.', '_','[',']', 'base', 'import','mro','nc','bash','system','globals','print','popen','read()','map','builtins', 'request', 'application', 'render_template', 'cycler', 'joiner','curl','wget', 'namespace', 'os', 'config', '{{','}}','request','|join','map','process','passwd','range','read()']
    name = request.args.get('name') 
    if not name:
        return "<h1> Hi FRIEND!, my name is pathfinder. Let's become AMIGOS!!!<br> but first give me your ?name </h1>"

    for word in blacklist:
        if word in name:
            return "<h1>So you don't want to be my friend?, then DIE!!!</h1>"

    template = f"<h1>- Hello {name}!</h1>"
    return render_template_string(template)

if __name__ =='__main__':
    app.run(debug=False)  
