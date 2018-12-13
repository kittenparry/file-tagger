import tkinter as tk
from tkinter import ttk, tix
import os
import time

class Tree(tk.Frame):
    def __init__(self, F, master=None):
        tk.Frame.__init__(self, master)
        #get only folders, not files
        #try printing a tree structure into console
        #use marmoset hexels 3 for folder icons?
        '''
        self.file_tree = ttk.Treeview(F.col_one_top_canv)
        self.file_tree["columns"] = ("one", "two")
        self.file_tree.column("one", width=100)
        self.file_tree.column("two", width=100)
        self.file_tree.heading("one", text="col A")
        self.file_tree.heading("two", text="col B")
        self.file_tree.insert("", 0, text="Line 1", values= ("1A", "1B"))
        id2 = self.file_tree.insert("", 1, "dir2", text="Dir 2")
        self.file_tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A", "2B"))
        self.file_tree.insert("", 3, "dir3", text="Dir 3")
        self.file_tree.insert("dir3", 3, text="sub dir 3", values=("3A", "3B"))
        self.file_tree.grid(row=0)
        '''

        #self.path

        #self.path = "D:\pycharmworkspace\\file-tagger"
        self.path = r"D:\Archive"
        self.onlyfolders =  [f for f in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, f))]
        print(self.onlyfolders)
        self.cl = tix.CheckList(F.col_one_top_canv, width=300, height=200, browsecmd=self.selectItem)
        self.t1 = time.time()
        self.makeCheckList()
        print("Took %.1f seconds to load." % (time.time() - self.t1))

    #this is faster
    def check(self, parent, path):
        try:
            with os.scandir(path) as content:
                for i, item in enumerate(content):
                    if item.is_dir():
                        if not item.name == "$RECYCLE.BIN":
                            entry = "{}.Item{}".format(parent, i)
                            self.cl.hlist.add(entry, text=item.name)
                            self.cl.setstatus(entry, "off")
                            self.check(entry, item.path)
        except PermissionError:
            pass
    def makeCheckList(self):  # no need of any extra argument here
        #self.cl = tix.CheckList(F.col_one_top_canv, browsecmd=self.selectItem)
        self.cl.pack(fill='both', expand="yes")
        # add the root directory in the tree
        self.cl.hlist.add("CL1", text=self.path)
        self.cl.setstatus("CL1", "off")
        # build the tree
        self.check("CL1", self.path)

        self.cl.autosetmode()

    def selectItem(self, item):
        print(self.cl.getstatus(item))
        print(self.cl.getselection("on"))
