import tkinter as tk
from tkinter import ttk

class Gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.top_bar = tk.Frame(relief='raised')
        self.col_one = tk.Frame(master)
        self.col_two = tk.Frame(master)
        self.top_bar.grid(row=0, column=0, columnspan=2)
        self.col_one.grid(row=1, column=0)
        self.col_two.grid(row=1, column=1)
        #self.col_one.grid_columnconfigure(1, weight=1)
        #self.col_two.grid_columnconfigure(1, weight=2)
        self.add_elements()
    def add_elements(self):
        self.menu = tk.Menubutton(self.top_bar, text=strings("tm"), underline=0)
        self.menu.grid(row=0, column=0)
        self.menu_sub = tk.Menu(self.menu, tearoff=0)
        self.menu['menu'] = self.menu_sub
        self.menu_sub.add_command(label=strings("m1"), underline=0)
        self.menu_sub.add_command(label=strings("m2"), underline=0)
        self.menu_sub.add_command(label=strings("m3"), underline=0)
        self.menu_sub.add_separator()
        self.menu_sub.add_command(label=strings("menu_exit"), command=self.exit_func)

        #self.label_filler = tk.Label(self.col_one, text=strings("tl"))
        self.label_filler2 = tk.Label(self.col_one, text=strings("t2"))
        self.label_filler3 = tk.Label(self.col_two, text=strings("t3"))
        self.label_filler4 = tk.Label(self.col_two, text=strings("t4"))

        #self.label_filler.grid(row=0)
        self.label_filler2.grid(row=1)
        self.label_filler3.grid(row=0)
        self.label_filler4.grid(row=1)

        self.file_tree = ttk.Treeview(self.col_one)
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

    def exit_func(self):
        self.quit()

def strings(s):
    str = {
        "title": "File Tagger",
        "ver": "0.00",

        "tl": "tree",
        "t2": "tags",
        "t3": "search",
        "t4": "files",

        "tm": "File",
        "m1": "menu1",
        "m2": "menu2",
        "m3": "menu3",
        "menu_exit": "Exit",

    }
    return str.get(s)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("{} v{}".format(strings("title"), strings("ver")))
    w, h, p, d = root.winfo_screenwidth(), root.winfo_screenheight(), 250, 15
    #root.geometry("%dx%d+0+0" % (w, h)) <- use instead for fullscreen*
    #root.geometry("%dx%d+%d+0" % (w-p, h-p, int(w/d)))
    root.geometry("%dx%d+%d+0" % (w/2, h/2, int(w/(d/4))))
    app = Gui(master=root)
    app.mainloop()