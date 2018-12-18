import json
import os

def read_tags(path):
    if not os.path.exists(path):
        with open(path, 'w') as f:
            json.dump({}, f)
        return {}
    with open(path) as di:
        tag_dic = json.load(di)
    tags = []
    for v in tag_dic.values():
        tags += v
    return list(set(tags))
