import os

folder_and_id = {}
id_and_path = {}
#try turning them into a dict again?
#d = {ftab, folder_paths} ?

def tree_maker(parent, path, entry = "0"):
    try:
        with os.scandir(path) as content:
            for i, item in enumerate(content):
                if item.is_dir():
                    if not item.name == "$RECYCLE.BIN":
                        entry2 = "{}.{}".format(entry, i)
                        #if parent == "└📁":
                        #    sub = "-"
                        #else:
                        #    sub = "+"
                        display = "{}{}{}".format("", parent, "")
                        #if parent == display:
                        #    val += 1
                        #val = int(entry2.split(".")[-1])
                        #below is useless
                        if len(entry2.split(".")) == 2:
                            val = 0
                        else:
                            val = len(entry2.split("."))
                        #print(entry2)
                        #print(entry2.split("."), item.name)
                        #folder_paths.append(item.path)
                        id_and_path.update({entry2: item.path})
                        folder_and_id.update({"%s %s" % (display, item.name): entry2})
                        tree_maker(display, item.path, entry2)
    except PermissionError:
        pass
