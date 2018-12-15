from flask import Flask, render_template
from program.tree import *
from program.files import get_files

app = Flask(__name__)

title = "File Tagger"
path = r"E:\from4chan\4chan"
test_tags = ["screenshot", "meme", "high_resolution", "background", "food", "room"]
@app.context_processor
def processor():
    def split(e):
        if len(e.split(".")) == 2:
            v = 0
        else:
            v = len(e.split("."))
        return v
    return dict(split=split)

tree_maker("└📁", path)
@app.route('/')
def main():
    return render_template('main.html', title=title, ftab=ftab, idp=idp, tags=test_tags)

@app.route('/files/', defaults={'val': 'start'})
@app.route('/files/<string:val>')
def files(val):
    if val == "start":
        return "start here"
    else:
        files, thumbs = get_files(idp[val])
        thumbs = ['thumbs/' + thumb for thumb in thumbs]
        return render_template('files.html', val=val, idp=idp, files=files, thumbs=thumbs)


if __name__ == '__main__':
    app.run(debug=True)
