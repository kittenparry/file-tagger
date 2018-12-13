import tkinter as tk

class Tags(tk.Frame):
    def __init__(self, F, master=None):
        tk.Frame.__init__(self, master)
        self.frame_tags = tk.Frame(F.col_one_bot_canv, bd=2, relief="ridge")
        self.frame_tags.grid(row=1, sticky="nsew")
        #self.frame_tags_scrolly = tk.Scrollbar(self.col_one, orient="vertical", command=self.frame_tags)
