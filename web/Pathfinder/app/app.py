from flask import Flask
from flask import request
from flask import render_template_string

app = Flask(__name__)
@app.route('/')
def index():
    
    name = request.args.get('name') 
    if name:
       template = f"<h1>- Hello {name}!</h1>"
       return render_template_string(template)
    else :
        return "<h1> Hi FRIEND!, my name is pathfinder. Let's become AMIGOS!!!<br> but first give me your ?name </h1>"
if __name__ =='__main__':
    app.run(debug=False)