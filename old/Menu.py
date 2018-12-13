import tkinter as tk
from program.Strings import strings

class Menu(tk.Frame):
    def __init__(self, F, master=None):
        tk.Frame.__init__(self, master)
        self.menu = tk.Menubutton(F.top_bar, text=strings("m_file"), underline=0)
        self.menu.grid(row=0, column=0)
        self.menu_sub = tk.Menu(self.menu, tearoff=0)
        self.menu['menu'] = self.menu_sub
        self.menu_sub.add_command(label=strings("m1"), underline=0)
        self.menu_sub.add_command(label=strings("m2"), underline=0)
        self.menu_sub.add_command(label=strings("m3"), underline=0)
        self.menu_sub.add_separator()
        self.menu_sub.add_command(label=strings("m_exit"), command=self.exit_func)
    def exit_func(self):
        self.quit()
