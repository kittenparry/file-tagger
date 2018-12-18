from flask import Flask, render_template, request
import json
from program.tree import *
from program.files import get_files
from program.read_tags import read_tags

app = Flask(__name__)

title = "File Tagger"
path = r"E:\from4chan\4chan"
path_db = r"db\tags.json"
tags = read_tags(path_db)
tree_maker("└📁", path)

@app.context_processor
def processor():
    def split(e):
        if len(e.split(".")) == 2:
            v = 0
        else:
            v = len(e.split("."))
        return v
    def length(o):
        return len(o)
    return dict(split=split, len=length)

@app.route('/')
def main():
    return render_template('main.html', title=title, ftab=ftab, idp=idp, tags=tags)

@app.route('/files/', defaults={'val': 'start'})
@app.route('/files/<string:val>')
def files(val):
    if val == "start":
        return "start here"
    else:
        files, thumbs = get_files(idp[val])
        thumbs = ['thumbs/' + thumb for thumb in thumbs]
        return render_template('files.html', val=val, idp=idp, files=files, thumbs=thumbs)

@app.route('/handle_files', methods=['POST'])
def handle_files():
    im = []
    path = []
    #tag_dic = {}
    with open(path_db) as di: #get previous tags
        tag_dic = json.load(di)
    t = request.form['text_tags'].split(' ') #gets the entered value
    n = int(request.form['lab_len']) #get the number of images
    for i in range(n):
        try: #only the selected ones
            im.append(request.form[f'images{i}'])
            path.append(request.form[f'path{i}'])
        except:
            pass
    #discard one or the other below for they are useless
    try:
        a = request.form['sub_add']
    except:
        a = None
    try:
        r = request.form['sub_rem']
    except:
        r = None
    #add path to the dict if they don't exist
    for p in path:
        if p not in tag_dic:
            tag_dic.update({p:[]})
    #if add button clicked
    if r is None:
        msg = f"Added tags {t} to the images {im}."
        for i in range(len(path)):
            tag_dic[path[i]] = list(set(tag_dic[path[i]] + t))
            #add tags to the path
            #remove duplicates (set())
    else:
        msg = f"Removed tags {t} from the images {im}."
        for i in range(len(path)):
            try:
                for tag in t:
                    if tag in tag_dic[path[i]]:
                        tag_dic[path[i]].remove(tag)
            except:
                pass
    for p in path:
        msg += f"{p}\n"

    with open(path_db, 'w') as f:
        json.dump(tag_dic, f)

    return msg


if __name__ == '__main__':
    app.run(debug=True)
