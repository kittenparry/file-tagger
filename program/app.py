from flask import Flask, render_template
import os

app = Flask(__name__)

title = "File Tagger"
@app.route('/')
def main():
    return render_template('main.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
