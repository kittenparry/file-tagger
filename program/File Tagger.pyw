import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.top_bar = tk.Frame(relief="raised")
        self.col_one = tk.Frame(master)
        self.col_two_top = tk.Frame(master)
        self.col_two_bot = tk.Frame(master, bd=2, relief="ridge")
        self.top_bar.grid(row=0, column=0, columnspan=5, sticky="ew")
        self.col_one.grid(row=1, column=0, sticky="ns", rowspan=2)
        self.col_two_top.grid(row=1, column=1, sticky="nsew")
        self.col_two_bot.grid(row=2, column=1, sticky="ns")
        #self.col_one.grid_columnconfigure(1, weight=1)
        #self.col_two.grid_columnconfigure(1, weight=2)
        self.sw = root.winfo_reqwidth()
        self.sh = root.winfo_reqheight()
        self.def_row = 0
        self.def_col = 0
        self.def2_row = 0
        self.def2_col = 0
        self.def2_ar = []
        self.add_elements()
        self.pop()
    def add_elements(self):
        self.menu = tk.Menubutton(self.top_bar, text=strings("m_file"), underline=0)
        self.menu.grid(row=0, column=0)
        self.menu_sub = tk.Menu(self.menu, tearoff=0)
        self.menu['menu'] = self.menu_sub
        self.menu_sub.add_command(label=strings("m1"), underline=0)
        self.menu_sub.add_command(label=strings("m2"), underline=0)
        self.menu_sub.add_command(label=strings("m3"), underline=0)
        self.menu_sub.add_separator()
        self.menu_sub.add_command(label=strings("m_exit"), command=self.exit_func)

        #self.label_filler = tk.Label(self.col_one, text=strings("tl"))
        #self.label_filler2 = tk.Label(self.col_one, text=strings("t2"))
        #self.label_filler3 = tk.Label(self.col_two, text=strings("t3"))
        #self.label_filler4 = tk.Label(self.col_two, text=strings("t4"))

        #self.label_filler.grid(row=0)
        #self.label_filler2.grid(row=1)
        #self.label_filler3.grid(row=0)
        #self.label_filler4.grid(row=1)


        #get only folders, not files
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

        self.frame_tags = tk.Frame(self.col_one, bd=2, relief="ridge")
        self.frame_tags.grid(row=1, sticky="nsew")
        #self.frame_tags_scrolly = tk.Scrollbar(self.col_one, orient="vertical", command=self.frame_tags)


        self.search_title = tk.Label(self.col_two_top, text=strings("l_search"))
        self.search_title.grid(row=0, column=0)
        self.search_bar = tk.Entry(self.col_two_top)
        self.search_bar.grid(row=0, column=1, sticky="ew")

        #self.file_canvas = tk.Canvas(self.col_two, width=self.sw, height=self.sh)
        #self.file_canvas.grid(row=1, column=0, columnspan=2, sticky="nsew")
        #self.file_canvas.create_line(0, 0, 200, 100)


        self.img0 = Image.new('RGB', (50, 50), (230,230,230))
        self.img0.save('test0.png')
        #self.img1 = tk.PhotoImage(file='test1.png')
        #self.file_canvas.create_image((0,0), image=self.img1)
        self.img2 = ImageTk.PhotoImage(Image.open('test2.png').resize((50,50), Image.ANTIALIAS))
        self.img3 = ImageTk.PhotoImage(Image.open('test3.png').resize((50,50), Image.ANTIALIAS))
        self.img1 = ImageTk.PhotoImage(Image.open('test1.png').resize((50,50), Image.ANTIALIAS))


    def populate_canvas(self, fname, thumb):
        temp = tk.Canvas(self.col_two_bot, width=100, height=100)
        #temp.create_image((self.def_pos_x, self.def_pos_y), image=thumb)
        temp.create_image((50,25), image=thumb)
        #temp.create_text((self.def_pos_x, self.def_pos_y + 25), text=fname)
        #temp.create_text((50,25), text=fname)
        t = str(self.def_row) + " " + str(self.def_col)
        temp.create_text((50,25), text=t)
        temp.create_text((50,75), text=fname)
        temp.grid(row=self.def_row, column=self.def_col)
        self.def_col += 1
        if self.def_col >= 5:
            self.def_col = 0
            self.def_row += 1

    def populate_tags(self, tag, num):
        tk.Checkbutton(self.frame_tags, relief="sunken", variable=self.def2_ar.append(0), onvalue=1, offvalue=0, text=self.def2_ar[self.def2_row]).grid(row=self.def2_row, column=0, sticky="ns")
        tk.Label(self.frame_tags, text=tag, relief="sunken").grid(row=self.def2_row, column=1, sticky="ns")
        tk.Label(self.frame_tags, text=str(num), relief="sunken").grid(row=self.def2_row, column=2, sticky="ns")
        self.def2_row += 1

    def pop(self):
        for i in range(5):
            self.populate_tags(strings("t_tag"), i)
        for i in range(20):
            self.populate_canvas(strings("t_fname"), self.img3)

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

        "m_file": "File",
        "m1": "menu1",
        "m2": "menu2",
        "m3": "menu3",
        "m_exit": "Exit",

        "t_fname": "test1.png",
        "t_fname2": "test2.png",
        "t_fname3": "test3.png",

        "l_search": "Search:",
        "t_tag": "Test tag",

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
