from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color


class Admin(UINode):
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
        super().__init__(master)
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

        self.home_frame.rowconfigure(0, weight=1)

        self.home_frame.columnconfigure(0, weight=0)
        self.home_frame.columnconfigure(1, weight=0)

        self.left_frame = tk.Frame(self.home_frame)
        self.left_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.left_frame.grid(column=0, sticky=tk.NSEW)

        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=21)

        self.left_frame.columnconfigure(0, weight=5)
        self.left_frame.columnconfigure(1, weight=1)
        # self.left_frame.grid_propagate(0)

        self.people_label = ttk.Label(self.left_frame,
                                      text="People",
                                      style='Recent.TLabel')
        self.people_label.grid(row=0, column=0, sticky=tk.W, padx=15)

        self.people_add = ttk.Button(self.left_frame, text="Add",
                                     style='Header.TButton')
        self.people_add.grid(row=0, column=1, sticky=tk.E, padx=(0, 15))

        self.people_listbox = tk.Listbox(self.left_frame,
                                         foreground=self.colors.foreground,
                                         selectforeground=self.colors.background,
                                         background=self.colors.background,
                                         relief=tk.FLAT)
        self.people_listbox.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

        # populate test data
        people_example = [
            {"name_amalgamated": "Iron Man"},
            {"name_amalgamated": "Steel Man"},
            {"name_amalgamated": "Wood Man"},
            {"name_amalgamated": "Quartz Man"},
            {"name_amalgamated": "Helium Man"}
        ]

        self.populate_people(people_example)

        self.right_frame = tk.Frame(self.home_frame)
        self.right_frame.configure(background=self.colors.background, border=3,
                                   relief=tk.RIDGE)
        self.right_frame.grid(row=0, column=1, sticky=tk.NS + tk.W)

        self.right_frame.columnconfigure((0, 1, 2), weight=1)
        self.right_frame.rowconfigure((0, 1), weight=1)

    def populate_people(self, lyst):

        for i in range(len(lyst)):
            self.people_listbox.insert(tk.END, lyst[i]["name_amalgamated"])

            if i % 2 == 0:
                background = self.colors.background
            else:
                background = self.colors.a7

            self.people_listbox.itemconfigure(i, background=background)
