import tkinter as tk
from tkinter import ttk

class Tree(tk.Frame):
    def __init__(self, F, master=None):
        tk.Frame.__init__(self, master)
        #get only folders, not files
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
