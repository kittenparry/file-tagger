import os

files = []
tabs = []
ftab = {}
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
                        val = len(entry2.split("."))
                        #print(entry2.split("."), item.name)
                        ftab.update({"%s %s" % (display, item.name): val})
                        '''
                        files.append("%s %s" % (entry, item.name))
                        if parent == entry:
                            tabs.append(True)
                        else:
                            tabs.append(False)
                        '''
                        #self.cl.hlist.add(entry, text=item.name)
                        #self.cl.setstatus(entry, "off")
                        tree_maker(display, item.path, entry2)
    except PermissionError:
        pass
