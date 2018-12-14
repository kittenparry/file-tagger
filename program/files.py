import os
from PIL import Image
import shutil

sizes = [(240, 240),
         #(720, 720), (1600, 1600),
         ]
#temp_dir = os.getcwd().split(":\\")[0] + ":\\__file-tagger_temp\\"
temp_dir = os.getcwd() + "\\static\\thumbs\\"
f_img = [".jpg", ".png", ".jpeg", ".bmp", ".webp"]
f_vid = [".webm", ".mp4", ".avi", ".flv", ".ts", ".mov", ".vmw", ".mkv", ".3gp", ".m4v", ".mpg"]
formats = f_img + f_vid
def get_files(path):
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    #empty folder from previous thumbs
    for d in os.listdir(temp_dir):
        os.unlink(os.path.join(temp_dir, d))
    #files = (file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)))
    files = []
    for file in os.listdir(path):
        for f in formats:
            if file.endswith(f):
                files.append(os.path.join(path, file))
    thumbs = []

    for image in files:
        i = image.split("\\")[-1]
        #thumbs.append(i)
        for size in sizes:
            im = Image.open(image)
            im.thumbnail(size)
            name = "thumb_%s_%s.jpg" % (i, "%d_%d" % (size))
            thumbs.append(name)
            im.save(r"%s%s" % (temp_dir, name))
    return files, thumbs
