"""
Root window creation logic. this can effectively be a singleton unless we
want to have multiple windows open, though that is not likely. Call once
On application init
"""
# TODO: implement singleton logic

import tkinter as tk
from tkinter import ttk

from color import Color
from ui_node import UINode
from button import Button
from label import Label
from hstack import HStack
from menu import Menu
from navbar import NavBar
from homepage import Homepage


class Window(tk.Frame, UINode):
    """
    Window class: responsible for being the 'root' component of all other
    widgets, layout, etc.. has properties like height, width, etc. will most
    likely handle resize events as well.
    """

    def __init__(self, master=None, title: str = "Test Window",
                 width: int = 800, height: int = 600,
                 theme: str = "Ubuntu"):
        """
        window class init function. Needs to create the window of course,
        and set up any window-level logic data pertinent to the View.
        """

        super().__init__(master)

        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.set_size()

        self.master.title(title)

        self.colors = Color(theme).colors

        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.master.configure(background=self.colors.background)

        self.master.config(menu=Menu(self, name="nav", width=50, height=35, theme=theme))

        self.configure(background=self.colors.background)

        self.nodes = [
            NavBar(self.master, name="nav", theme=theme),
            Homepage(self, name="homepage", theme=theme)
        ]

        # set app toolbar
        self.master.configure(menu=self.nodes[0])
        # self.nodes[0].pack()

        self.pack(fill=tk.BOTH, expand=1)

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
        """manual window sizing event that can be called"""
        self.master.geometry(str(self.width) + "x" + str(self.height))
