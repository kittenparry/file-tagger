import os
import time
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

sizes = [(240, 240),
         #(720, 720), (1600, 1600),
         ]
#temp_dir = os.getcwd().split(":\\")[0] + ":\\__file-tagger_temp\\"
temp_dir = os.getcwd() + "\\static\\thumbs\\"
formats_image = [".jpg", ".png", ".jpeg", ".bmp", ".webp"]
formats_video = [".webm", ".mp4", ".avi", ".flv", ".ts", ".mov", ".vmw", ".mkv", ".3gp", ".m4v", ".mpg"]
formats = formats_image + formats_video
#tags switch for directly getting filenames
def get_files(path, tags = 0):
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    #empty folder from previous thumbs
    for file in os.listdir(temp_dir):
        os.unlink(os.path.join(temp_dir, file))
    #files = (file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)))
    files = []
    if tags == 1:
        files = list(path)
    else:
        for file in os.listdir(path):
            for format in formats:
                if file.endswith(format):
                    files.append(os.path.join(path, file))
    thumbs = []
    error = {}
    error_time = time.strftime("%Y.%m.%d %H:%M:%S") + "\n"
    error_count = 0
    for image_file in files:
        image_name = image_file.split("\\")[-1]
        #thumbs.append(i)
        for size in sizes:
            try:
                image = Image.open(image_file)
                image.thumbnail(size)
                thumb_name = "thumb_%s_%s.jpg" % (image_name, "%d_%d" % (size))
                thumbs.append(thumb_name)
                image.save(r"%s%s" % (temp_dir, thumb_name))
            except Exception as e:
                error_count += 1
                error.update({str(e): image_file})
    error_time = "" + error_time
    for e, p in error.items():
        error_time += f"\t{e}\n"
        error_time += f"\t\t{p}\n"
    if error_count > 0:
        with open(r"image_errors.log", 'a') as f:
            f.write(error_time)
    return files, thumbs
