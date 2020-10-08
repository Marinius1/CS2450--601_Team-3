"""
Root window creation logic. this can effectively be a singleton unless we
want to have multiple windows open, though that is not likely. Call once
On application init
"""
# TODO: implement singleton logic

import tkinter as tk
from tkinter import ttk

from color import Color


class Window(tk.Frame):
    """
    Window class: responsible for being the 'root' component of all other
    widgets, layout, etc.. has properties like height, width, etc. will most
    likely handle resize events as well.
    """

    def __init__(self, master=None, title: str = "Test Window",
                 width: int = 800, height: int = 600):
        """
        window class init function. Needs to create the window of course,
        and set up any window-level logic data pertinent to the view.
        """

        super().__init__(master)

        self.width = width
        self.height = height
        self.set_size()

        self.master.title(title)

        self.colors = Color().colors

        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.master.configure(background=self.colors.background)
        self.pack()


        self.style.configure('TButton',
                             background=self.colors.background,
                             foreground=self.colors.foreground,
                             width=20,
                             borderwidth=2,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10)

        self.style.map('TButton', background=[('active', self.colors.a7)])
        button1 = ttk.Button(self.master, text="1", style='TButton')
        button2 = ttk.Button(self.master, text="2", style='TButton')
        button3 = ttk.Button(self.master, text="3", style='TButton')
        button1.pack(side=tk.LEFT)
        button2.pack()
        button3.pack()

    @property
    def size(self):
        return [self.width, self.height]

    @size.setter
    def size(self, value: list):
        """manually resize window within setter"""
        self.width = value[0]
        self.height = value[1]
        self.set_size()

    def set_size(self):
        self.master.geometry(str(self.width) + "x" + str(self.height))
