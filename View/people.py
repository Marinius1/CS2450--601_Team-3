from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color


class People(UINode):
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
                       background=[('active', self.colors.a7)],
                       foreground=[('active', self.colors.background)])
        self.style.configure('Header.TButton',
                             background=self.colors.background,
                             foreground=self.colors.foreground,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10
                             )

        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure(0, weight=0)
        self.home_frame.rowconfigure(1, weight=1)
        # self.home_frame.columnconfigure(1, weight=1)

        # self.header = tk.Frame(self.home_frame)
        # self.header.configure(background=self.colors.background, border=3,
        #                       relief=tk.FLAT)
        # self.header.grid(row=0, column=0, sticky=tk.N + tk.E + tk.W)

        # self.recent_actions_label = ttk.Label(self.header,
        #                                       text="First Name",
        #                                       style='Recent.TLabel')
        # self.recent_actions_label.grid(row=0, column=0, sticky=tk.NW, padx=15)

        # self.table = tk.Frame(self.home_frame)
        # self.table.configure(background='red', border=3,
        #                      relief=tk.FLAT)
        # self.table.grid(row=1, column=0, sticky=tk.NSEW)
        '''
        self.column = tk.Listbox(self.table,
                                                 foreground=self.colors.foreground,
                                                 selectforeground=self.colors.background,
                                                 background=self.colors.background,
                                                 relief=tk.FLAT)
        self.recent_actions_listbox.grid(row=0, column=0, sticky=tk.NS, padx=(15, 15))

        for i in range(500):
            self.recent_actions_listbox.insert(tk.END, "Jacob")

        self.table = tk.Scrollbar(self.table)
        self.table.grid(row=1, column=1, sticky=tk.NS)

        self.column.configure(yscrollcommand=self.recent_actions_scrollbar.set)
        self.recent_actions_scrollbar.configure(command=self.recent_actions_listbox.yview)
        '''

        model_example = [
            # ['bob', 'cindy', 'lue', 'greg'],
            [i for i in range(1000)],
            [i for i in range(1000)],
            [i for i in range(1000)]
            # ['Jones', 'Lue', 'Suong', 'Borgerstrom'],
            # ['$11.00', '$12.00', 'More than you', 'Less than you']
        ]

        headers_example = ['First Name', 'Last Name', 'Wage']

        self.listboxes = []


        self.scrollbar = tk.Scrollbar(self.home_frame)
        # self.b1 = Listbox(master, yscrollcommand=scrollbar.set)
        # self.b2 = Listbox(master, yscrollcommand=scrollbar.set)
        self.scrollbar.config(command=self.yview)
        # self.b1.pack(side=LEFT, fill=BOTH, expand=1)
        # self.b2.pack(side=LEFT, fill=BOTH, expand=1)

        self.create_table(headers_example, model_example)
        self.scrollbar.grid(row=0, column=5)

    def yview(self, *args):

        for i in self.listboxes:
            i.yview()

    def create_table(self, lyst1, lyst2):

        for i in range(len(lyst1)):

            self.home_frame.columnconfigure(i, weight=0)

            grid_frame = tk.Frame(self.home_frame, background=self.colors.background)
            grid_frame.grid(row=0, column=i, sticky=tk.NS)

            button = ttk.Button(grid_frame, text=lyst1[i],
                                style='Header.TButton')
            button.grid(row=0, column=0, sticky=tk.EW)

            column = tk.Listbox(grid_frame,
                                foreground=self.colors.foreground,
                                selectforeground=self.colors.background,
                                background=self.colors.background,
                                relief=tk.FLAT,
                                yscrollcommand=self.scrollbar.set)
            column.grid(row=1, column=0, sticky=tk.NS)

            for j in range(len(lyst2[i])):
                column.insert(tk.END, lyst2[i][j])

                if (j % 2 == 0):
                    background = self.colors.background
                else:
                    background = self.colors.a7

                column.itemconfigure(j, background=background)
            column.configure(height=len(lyst2[i]))

            self.listboxes.append(column)


    def resize_summary_frame(self, event, title, content):
        title.configure(font=('Roboto', int(event.height * .1)))
        content.configure(font=('Roboto', int(event.height * .2), 'bold'))
