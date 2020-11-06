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
from menu import Menu
from navbar import NavBar
from homepage import Homepage
from people import People


class Window(UINode):
    """
    Window class: responsible for being the 'root' component of all other
    widgets, layout, etc.. has properties like height, width, etc. will most
    likely handle resize events as well.
    """

    def __init__(self, master=None, title: str = "Test Window",
                 width: int = 800, height: int = 600,
                 theme: str = "Builtin Light"):
        """
        window class init function. Needs to create the window of course,
        and set up any window-level logic data pertinent to the View.
        """

        super().__init__()
        self.master = master

        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.set_size()

        self.master.title(title)

        self.colors = Color(theme).colors

        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.master.configure(background=self.colors.background)

        self.master.rowconfigure(0, weight=0)
        self.master.rowconfigure(1, weight=1)

        self.master.columnconfigure(0, weight=1)

        self.nav = NavBar(self.master, name="nav", theme=theme),
        # self.page_home = Homepage(self.master, name="homepage", theme=theme)
        self.page_people = People(self.master, name="people", theme=theme)

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
