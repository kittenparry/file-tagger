import tkinter as tk
from program.Strings import strings

class Search(tk.Frame):
    def __init__(self, F, master=None):
        tk.Frame.__init__(self, master)
        self.search_title = tk.Label(F.col_two_top, text=strings("l_search"))
        self.search_title.grid(row=0, column=0)
        self.search_bar = tk.Entry(F.col_two_top)
        self.search_bar.grid(row=0, column=1, sticky="ew")
