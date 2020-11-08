"""
Root window creation logic. this can effectively be a singleton unless we
want to have multiple windows open, though that is not likely. Call once
On application init
"""
# TODO: implement singleton logic

import tkinter as tk
from tkinter import ttk

from .Colors.color import Color
from .menu import Menu
from .navbar import NavBar
from .homepage import Homepage
from .people import People
from .admin import Admin
from .login import Login


class Window():
    """
    Window class: responsible for being the 'root' component of all other
    widgets, layout, etc.. has properties like height, width, etc. will most
    likely handle resize events as well.
    """

    def __init__(self, master=None, title: str = "AnyEmployee",
                 theme: str = "Builtin Light"):
        """
        window class init function. Needs to create the window of course,
        and set up any window-level logic data pertinent to the View.
        """

        self.master = master

        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        self.set_size()

        self.master.title(title)

        self.colors = Color(theme).colors

        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.theme = theme

        self.master.configure(background=self.colors.background)

        self.master.rowconfigure(0, weight=0)
        self.master.rowconfigure(1, weight=1)

        self.master.columnconfigure(0, weight=1)

        self.nav = None
        self.page_home = Login(self.master, theme=theme, window=self)
        # self.nav = NavBar(self.master, name="nav", theme=theme, window=self)
        # self.page_home = Homepage(self.master, name="homepage", theme=theme)

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

    def create_nav(self):
        self.nav = NavBar(self.master, name="nav", theme=self.theme, window=self)

    def home(self):
        self.page_home = Homepage(self.master, name="Home", theme=self.theme)

    def people(self):
        self.page_home = People(self.master, name="people", theme=self.theme)

    def admin(self):
        self.page_home = Admin(self.master, name="people", theme=self.theme)

