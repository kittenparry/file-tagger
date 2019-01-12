from flask import Flask, render_template, request
import json
from program.tree import folder_and_id, id_and_path, tree_maker
from program.files import get_files
from program.read_tags import read_tags
from program.constants import *

#import webbrowser
app = Flask(__name__)

tags = read_tags(PATH_DB)
tree_maker("└📁", PATH)

@app.context_processor
def processor():
    def split(e):
        if len(e.split(".")) == 2:
            val = 0
        else:
            val = len(e.split("."))
        return val
    def length(o):
        return len(o)
    return dict(split=split, len=length)

@app.route('/')
def main():
    return render_template('main.html', title=TITLE, ftab=folder_and_id,
                           idp=id_and_path, tags=tags)

@app.route('/files/', defaults={'val': 'start'})
@app.route('/files/<string:val>')
def files(val, msg = ""):
    if val == "start":
        return "start here"
    elif val.startswith("["):
        tags = val[1:-1].split(",")
        with open(PATH_DB) as di:
            tag_dic = json.load(di)
        path_files = []
        for file, file_tags in tag_dic.items():
            for tag in tags:
                if tag in file_tags:
                    path_files.append(file)
        #is this a slow and an inefficient method?
        path_files = list(set(path_files)) #to get rid of the duplicates
        files, thumbs = get_files(path_files, 1)
    else:
        files, thumbs = get_files(id_and_path[val])
    thumbs = ['thumbs/' + thumb for thumb in thumbs]
    return render_template('files.html', val=val, idp=id_and_path, files=files,
                           thumbs=thumbs, msg=msg)

@app.route('/handle_files', methods=['POST'])
def handle_files():
    images = []
    path = []
    val = request.form['files_val']
    #tag_dic = {}
    with open(PATH_DB) as di: #get previous tags
        tag_dic = json.load(di)
    tags = request.form['text_tags'].split(' ') #gets the entered value
    images_count = int(request.form['lab_len']) #get the number of images
    for i in range(images_count):
        try: #only the selected ones
            images.append(request.form[f'images{i}'])
            path.append(request.form[f'path{i}'])
        except:
            pass
    #discard one or the other below for they are useless
    try:
        sub_add = request.form['sub_add']
    except:
        sub_add = None
    try:
        sub_remove = request.form['sub_rem']
    except:
        sub_remove = None
    #add path to the dict if they don't exist
    for p in path:
        if p not in tag_dic:
            tag_dic.update({p:[]})
    #if add button clicked
    if sub_remove is None:
        ar = ["Added", "to"]
        for i in range(len(path)):
            tag_dic[path[i]] = list(set(tag_dic[path[i]] + tags))
            #add tags to the path
            #remove duplicates (set())
    else:
        ar = ["Removed", "from"]
        for i in range(len(path)):
            try:
                for tag in tags:
                    if tag in tag_dic[path[i]]:
                        tag_dic[path[i]].remove(tag)
            except:
                pass

    msg = f"{ar[0]} tag(s) {', '.join(tags)} {ar[1]} {len(images)} images."
    with open(PATH_DB, 'w') as f:
        json.dump(tag_dic, f)

    return files(val, msg)


if __name__ == '__main__':
    #webbrowser.open('http://127.0.0.1:5000/', new=2, autoraise=True)
    #webbrowser.open_new_tab('http://127.0.0.1:5000/')
    app.run(debug=True)
