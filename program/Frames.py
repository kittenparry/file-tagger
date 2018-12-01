import tkinter as tk

class Frames(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.top_bar = tk.Frame(relief="raised")
        self.col_one_top = tk.Frame(master)
        self.col_one_top_canv = tk.Canvas(self.col_one_top)
        self.col_one_top_scroll = tk.Scrollbar(self.col_one_top, orient="vertical", command=self.col_one_top_canv.yview)
        self.col_one_top_canv.configure(yscrollcommand=self.col_one_top_scroll.set)
        self.col_one_bot = tk.Frame(master)
        self.col_one_bot_canv = tk.Canvas(self.col_one_bot)
        self.col_one_bot_scroll = tk.Scrollbar(self.col_one_bot, orient="vertical", command=self.col_one_bot_canv.yview)
        self.col_one_bot_canv.configure(yscrollcommand=self.col_one_bot_scroll.set)
        self.col_two_top = tk.Frame(master)
        self.col_two_bot = tk.Frame(master, bd=2, relief="ridge")
        self.col_two_bot_canv = tk.Canvas(self.col_two_bot)
        self.col_two_bot_scroll = tk.Scrollbar(self.col_two_bot, orient="vertical", command=self.col_two_bot_canv.yview)
        self.col_two_bot_canv.configure(yscrollcommand=self.col_two_bot_scroll.set)
        self.top_bar.grid(row=0, column=0, columnspan=5, sticky="ew")
        self.col_one_top.grid(row=1, column=0, sticky="ns", rowspan=2)
        self.col_one_top_canv.grid(row=0, column=0, sticky="nsew")
        self.col_one_top_scroll.grid(row=0, column=1, sticky="ns")
        self.col_one_bot.grid(row=3, column=0, sticky="ns")
        self.col_one_bot_canv.grid(row=0, column=0, sticky="nsew")
        self.col_one_bot_scroll.grid(row=0, column=1, sticky="ns")
        self.col_two_top.grid(row=1, column=1, sticky="nsew")
        self.col_two_bot.grid(row=2, column=1, sticky="ns", rowspan=2)
        self.col_two_bot_canv.grid(row=0, column=0, sticky="nsew")
        self.col_two_bot_scroll.grid(row=0, column=1, sticky="ns")
