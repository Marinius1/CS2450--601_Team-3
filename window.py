"""
Root window creation logic. this can effectively be a singleton unless we
want to have multiple windows open, though that is not likely. Call once
On application init
"""
# TODO: implement singleton logic

import tkinter as tk
from tkinter import ttk
from controller import *
from View.menu import Menu
from View.Colors.color import Color
from View.navbar import NavBar
from View.homepage import Homepage
from View.people import People
from View.admin import Admin
from View.login import Login
from View.timecard import TimeCard
from View.payroll import PayRoll


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

        self.menu = Menu(self.master, self)

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

    def login(self):
        self.nav.nav_frame.grid_forget()
        self.nav = None
        self.page_home = Login(self.master, theme=self.theme, window=self)

    def home(self):
        self.nav.help_content = "./View/help_files/home.txt"
        self.page_home = Homepage(self.master, name="Home", theme=self.theme)

    def people(self):
        self.nav.help_content = "./View/help_files/people.txt"
        self.page_home = People(self.master, name="people", theme=self.theme)

    def admin(self):
        self.nav.help_content = "./View/help_files/admin.txt"
        self.page_home = Admin(self.master, name="admin", theme=self.theme)

    def timecard(self):
        self.nav.help_content = "./View/help_files/timecard.txt"
        self.page_home = TimeCard(self.master, theme=self.theme)

    def pay(self):
        self.nav.help_content = "./View/help_files/payroll.txt"
        self.page_home = PayRoll(self.master, theme=self.theme)

if __name__=="__main__":
    root = tk.Tk()
    window = Window(root)
    root.mainloop()