import os

import tkinter as tk
from tkinter import ttk
from .Colors.color import Color
from .navbar import NavBar
from .homepage import Homepage


class Login():
    """
    the 'row' class. creates a View that arranges children horizontally within
    it's bounds. can auto wrap or truncate if needed. scrolling is also an
    option.
    """

    def __init__(self, master=None, name: str = "", width: int = 10,
                 height: int = 10, theme=None, window=None):
        """
        init(name: str, children[]: List<varies>): void
        calls super(). needs to populate the horizontal View. also needs to bind either
        truncate or wrap data when the contents of the horizontal View exceed the
        bounds.
        """

        self.master = master
        self.window = window
        self.theme = theme

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
                             font=('Roboto', 36)
                             )
        self.style.map('Header.TButton',
                       background=[('active', self.colors.a8)],
                       foreground=[('active', self.colors.background)])
        self.style.configure('Header.TButton',
                         background=self.colors.a7,
                         foreground=self.colors.background,
                         borderwidth=0,
                         bordercolor=self.colors.a0,
                         focusthickness=3,
                         focuscolor=self.colors.a10,
                         )

        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure((0,1,2), uniform="row", weight=1)
        self.home_frame.columnconfigure((0,1,2), uniform="col", weight=1)


        self.frames_login = {}
        # debug_colors = ['red', 'blue', 'green', 'purple', 'pink', 'yellow', 'magenta', 'gray', 'orange']
        count = 0
        for x in range(3):
            for y in range(3):
                debug_frame = tk.Frame(self.home_frame)
                debug_frame.grid(row=x, column=y, sticky=tk.NSEW)
                self.frames_login[str((x,y))] = debug_frame
                count += 1

        # setup logo
        self.eimg = tk.PhotoImage(file='./View/AnyEmployee.gif')
        self.eimg.subsample(100, 100)
        self.img_label = tk.Label(self.home_frame, image=self.eimg,
                                  background=self.colors.background)
        self.img_label.grid(row=0, column=0, sticky=tk.NW)

        self.frames_login[str((1,1))].columnconfigure(0, weight=1)
        self.frames_login[str((1,1))].rowconfigure(1, weight=1)

        self.info_login = ttk.Label(self.frames_login[str((1,1))], text="Login", style='Recent.TLabel')
        self.info_login.grid(row=0, column=0, sticky=tk.N)

        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.frame_login_data = tk.Frame(self.frames_login[str((1,1))])
        self.frame_login_data.grid(row=1, column=0, sticky=tk.NSEW, pady=(self.screen_height / 20, 0))
        self.frame_login_data.columnconfigure((0,1), weight=1)

        self.field_username = self.create_text_entry(self.frame_login_data, "Username", "username", 0)
        self.field_password = self.create_text_entry(self.frame_login_data, "Password", "password", 1, password=True)

        self.button_login = ttk.Button(self.frame_login_data, text="Login", style='Header.TButton', command=self.login)
        self.button_login.grid(row=2, columnspan=2, sticky=tk.EW, padx=(self.screen_width / 10), pady=(self.screen_height / 42, 0))

    def login(self):

        login_data = self.get_data()
        # print(login_data)

        self.window.create_nav()
        self.window.home()

    def get_data(self):
        return {
            "username": self.field_username["entry"].get(),
            "password": self.field_password["entry"].get(),
        }

    def create_text_entry(self, master, label, placeholder, row, column_start=0, password=False):
        label = ttk.Label(master, text=label)
        label.configure(background=self.colors.background)
        label.grid(row=row, column=column_start, sticky=tk.E)

        entry = ttk.Entry(master, show='*' if password else '')
        entry.insert(0, placeholder)
        entry.grid(row=row, column=column_start + 1, sticky=tk.W, padx=(10, 0), pady=5)
        return {"label": label, "entry": entry}







