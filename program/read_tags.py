import json
import os
from collections import Counter

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
    #probably doesn't need the first return since the second one has both
    #return list(set(tags)), count_tags(tags)
    return count_tags(tags)

def count_tags(dic):
    return sorted(Counter(dic).items(), key=lambda x: x[1])
