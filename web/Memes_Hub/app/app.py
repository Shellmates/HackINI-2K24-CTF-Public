from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
# home page with memes
def index():
    memes = ['salt.png', 'mrigla.png', 'stik-tak-tok.png']
    return render_template('index.html', memes=memes)

@app.route('/download',methods=['GET'])
def download():
    # cry until you get the flag
    file=request.args.get('file','cry-until-you-get-the-flag.png')

    # Always care about security, block directory traversals, this filter cannot be bypassed
    if (".." not in file) and ("%" not in file):

        # get files inside /memes/ directory
        meme_path = os.path.join(app.root_path,'memes', file)

        if os.path.isfile(meme_path):
            # send file to user
            return send_file(meme_path,as_attachment=True)
        
        # cry until you get the flag
        else: return send_file("memes/cry-until-you-get-the-flag.png",as_attachment=True)
    else:
        # cry until you get the flag
        return send_file("memes/cry-until-you-get-the-flag.png", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=False)
