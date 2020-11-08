import os

import tkinter as tk
from tkinter import ttk
from .Colors.color import Color


class Login():
    """
    the 'row' class. creates a View that arranges children horizontally within
    it's bounds. can auto wrap or truncate if needed. scrolling is also an
    option.
    """

    def __init__(self, master=None, name: str = "", width: int = 10,
                 height: int = 10, theme=None):
        """
        init(name: str, children[]: List<varies>): void
        calls super(). needs to populate the horizontal View. also needs to bind either
        truncate or wrap data when the contents of the horizontal View exceed the
        bounds.
        """

        self.master = master

        self.name = name
        self.colors = Color(theme).colors
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.map('Recent.TLabel',
                       background=[('active', self.colors.a7)],
                       foreground=[('active', self.colors.background)])
        self.style.configure('Recent.TLabel',
                             background=self.colors.background,
                             # background='red',
                             foreground=self.colors.foreground,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             font=('Roboto', 24)
                             )

        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure((0,1,2), weight=1)
        self.home_frame.columnconfigure((0,1,2), weight=1)
        debug_colors = ['red', 'blue', 'green', 'purple', 'pink', 'yellow', 'magenta', 'gray', 'orange']

        count = 0
        for x in range(3):
            for y in range(3):
                debug_frame = tk.Frame(self.home_frame, background=debug_colors[count])
                debug_frame.grid(row=x, column=y, sticky=tk.NSEW)
                count += 1

        # setup logo
        self.eimg = tk.PhotoImage(file='./View/AnyEmployee.gif')
        self.eimg.subsample(100, 100)
        self.img_label = tk.Label(self.home_frame, image=self.eimg,
                                  background=self.colors.background)
        self.img_label.grid(row=0, column=0, sticky=tk.NW)




        self.info_login = tk.Label(self.home_frame, text="Login", background='red')
        self.info_login.grid(row=1, column=1)





