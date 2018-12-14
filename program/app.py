from flask import Flask, render_template
from program.tree import *

app = Flask(__name__)

title = "File Tagger"
path = r"D:\Archive"
@app.context_processor
def processor():
    def tree():
        tree_maker("CL1", path)
    return dict(tree=tree)

tree_maker("└📁", path)
@app.route('/')
def main():
    return render_template('main.html', title=title, files=files, tabs=tabs, ftab=ftab)

if __name__ == '__main__':
    app.run(debug=True)
