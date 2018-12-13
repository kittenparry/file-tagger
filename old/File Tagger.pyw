import tkinter as tk
from PIL import Image, ImageTk
from tkinter import tix

from program.Strings import strings
from program.Frames import Frames
from program.Menu import Menu
from program.Tree import Tree
from program.Tags import Tags
from program.Search import Search

class Gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.Frames = Frames()

        #db storing path to files as tags?
        #tags = {
        #   "tag1": {"path/to/file1", "path/to/file2"},
        #   "tag2": ... } #^ does this even work?
		
		#get the programming in cmd first
		#then gui?

        #put below into a separate function
        #also a lot of numbers into something similar to strings
        #along with thumbs
        #val("thumbs")
        #val("sw") etc?
        self.sw = root.winfo_reqwidth()
        self.sh = root.winfo_reqheight()
        self.def_row = 0
        self.def_col = 0
        self.def2_row = 0
        self.def2_col = 0
        self.def2_ar = []
        self.thumbs = strings("thumbs")

        self.add_elements()
        self.pop()
    def add_elements(self):
        self.Menu = Menu(self.Frames)
        self.Tree = Tree(self.Frames)
        self.Tags = Tags(self.Frames)
        self.Search = Search(self.Frames)

        #self.file_canvas = tk.Canvas(self.col_two, width=self.sw, height=self.sh)
        #self.file_canvas.grid(row=1, column=0, columnspan=2, sticky="nsew")
        #self.file_canvas.create_line(0, 0, 200, 100)

        self.img0 = Image.new('RGB', (50, 50), (230,230,230))
        self.img0.save(self.thumbs + 'test0.png')
        #self.img1 = tk.PhotoImage(file='test1.png')
        #self.file_canvas.create_image((0,0), image=self.img1)
        self.img2 = ImageTk.PhotoImage(Image.open(self.thumbs + 'test2.png').resize((50,50), Image.ANTIALIAS))
        self.img3 = ImageTk.PhotoImage(Image.open(self.thumbs + 'test3.png').resize((50,50), Image.ANTIALIAS))
        self.img1 = ImageTk.PhotoImage(Image.open(self.thumbs + 'test1.png').resize((50,50), Image.ANTIALIAS))

        #TODO: no .py folder for files section
    def populate_canvas(self, fname, thumb):
        temp = tk.Canvas(self.Frames.col_two_bot_canv, width=100, height=100)
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
        tk.Checkbutton(self.Tags.frame_tags, relief="sunken", variable=self.def2_ar.append(0), onvalue=1, offvalue=0, text=self.def2_ar[self.def2_row]).grid(row=self.def2_row, column=0, sticky="ns")
        tk.Label(self.Tags.frame_tags, text=tag, relief="sunken").grid(row=self.def2_row, column=1, sticky="ns")
        tk.Label(self.Tags.frame_tags, text=str(num), relief="sunken").grid(row=self.def2_row, column=2, sticky="ns")
        self.def2_row += 1

    def pop(self):
        for i in range(25):
            self.populate_tags(strings("t_tag"), i)
        for i in range(20):
            self.populate_canvas(strings("t_fname"), self.img3)

if __name__ == '__main__':
    root = tix.Tk()
    root.title("{} v{}".format(strings("title"), strings("ver")))
    w, h, p, d = root.winfo_screenwidth(), root.winfo_screenheight(), 250, 15
    #root.geometry("%dx%d+0+0" % (w, h)) <- use instead for fullscreen*
    #root.geometry("%dx%d+%d+0" % (w-p, h-p, int(w/d)))
    root.geometry("%dx%d+%d+0" % (w/2, h/2, int(w/(d/4))))
    app = Gui(master=root)
    app.mainloop()
