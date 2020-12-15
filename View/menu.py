import tkinter as tk
from tkinter import filedialog

from View.Colors.color import Color

class Menu():
    """
    the 'row' class. creates a View that arranges children horizontally within
    it's bounds. can auto wrap or truncate if needed. scrolling is also an
    option.
    """

    def __init__(self, master=None, window=None):
        """
        init(name: str, children[]: List<varies>): void
        calls super(). needs to populate the horizontal View. also needs to bind either
        truncate or wrap data when the contents of the horizontal View exceed the
        bounds.
        """


        self.master = master
        self.window = window

        self.menu = tk.Menu(self.master)

        self.menu_file = tk.Menu(self.menu, tearoff=0)
        self.menu_file.add_command(label="Dark Mode", command=self.set_dark_mode)
        self.menu_file.add_command(label="Light Mode", command=self.set_light_mode)
        self.menu_file.add_separator()

        self.menu_file.add_command(label="Logout", command=self.logout)
        self.menu_file.add_command(label="Exit", command=self.master.quit)

        self.menu.add_cascade(label="File", menu=self.menu_file)

        self.master.configure(menu=self.menu)

    def set_dark_mode(self):
        self.window.colors = Color(scheme="Builtin Dark").colors
        self.window.theme = "Builtin Dark"

        self.window.page_home.__init__(self.master, theme=self.window.theme, window=self.window)

        self.window.page_home.colors = self.window.colors



        if self.window.nav is not None:
            self.window.create_nav()


    def set_light_mode(self):
        self.window.colors = Color(scheme="Builtin Light").colors
        self.window.theme = "Builtin Light"

        self.window.page_home.__init__(self.master, theme=self.window.theme, window=self.window)
        self.window.page_home.colors = self.window.colors

        if self.window.nav is not None:
            self.window.create_nav()


    def logout(self):
        self.window.login()

