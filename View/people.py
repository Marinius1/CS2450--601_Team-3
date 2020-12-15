import tkinter as tk
from tkinter import ttk
from .Colors.color import Color
from View.resize_utility import ResizeUtility
import controller as Controller
import random

class People():
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
                             background=self.colors.a7,
                             foreground=self.colors.background,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10
                             )

        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3, relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure(0, weight=1)

        self.resize_utility = ResizeUtility(self.master)
        self.style.configure(style='Header.TButton', font=('Roboto', self.resize_utility.body_text()))

        self.scrollbar = tk.Scrollbar(self.home_frame)

        self.buttons = []
        self.data_columns = []

        self.model_example = Controller.List_Maker()


        self.headers_example = ['First name', 'Last name', 'Employee number', 'Phone', 'Role', 'Position', 'Team']
        self.header_buttons = []
        self.header_button_actions = [self.sort_descnding for i in range(len(self.headers_example))]

        self.table = self.create_table(self.headers_example, self.model_example.data)
        self.sort_ascending("Last name")
        self.scrollbar.configure(command=self.yview)


    def button_action(self, event):
        button_text = event.widget.cget('text')
        button_index = self.headers_example.index(button_text)

        self.header_button_actions[button_index](button_text)


    def sort_ascending(self, text):

        print(text, "Ascending")

        val_list = [self.model_example.data[i][text] for i in range(len(self.model_example.data))]
        val_list.sort()

        model_copy = self.model_example.data.copy()

        for i in self.table:
            i.delete(0, tk.END)

        count = 0
        for i in val_list:
            for j in model_copy:
                if i == j[text]:
                    for k in range(len(self.headers_example)):
                        self.table[k].insert(tk.END, j[self.headers_example[k]])

                        if count % 2 == 0:
                            background = self.colors.background
                            foreground = self.colors.a7
                        else:
                            background = self.colors.a7
                            foreground = self.colors.background

                        self.table[k].itemconfigure(tk.END, background=background, foreground=foreground)
                    count += 1

                    model_copy.pop(model_copy.index(j))


        self.header_button_actions[self.headers_example.index(text)] = self.sort_descnding

    def sort_descnding(self, text):

        val_list = [self.model_example.data[i][text] for i in range(len(self.model_example.data))]
        val_list.sort(reverse=True)

        model_copy = self.model_example.data.copy()

        for i in self.table:
            i.delete(0, tk.END)

        count = 0
        for i in val_list:
            for j in model_copy:
                if i == j[text]:
                    for k in range(len(self.headers_example)):
                        self.table[k].insert(tk.END, j[self.headers_example[k]])

                        if count % 2 == 0:
                            background = self.colors.background
                        else:
                            background = self.colors.a7

                        self.table[k].itemconfigure(tk.END, background=background)
                    count += 1

                    model_copy.pop(model_copy.index(j))


        self.header_button_actions[self.headers_example.index(text)] = self.sort_ascending

    def yview(self, *args):

        for i in self.data_columns:
            i.yview(*args)

            pos = i.yview()
            self.scrollbar.set(pos[0], pos[1])

    def sync_yview(self, *args):

        for i in range(len(self.data_columns)):
            data_columns_copy = self.data_columns.copy()
            data_columns_copy.pop(i)

            sync_check = [self.data_columns[i].yview() == j.yview() for j in data_columns_copy]

            if not all(sync_check):
                for k in range(len(self.data_columns)):
                    if k != i:
                        self.data_columns[k].yview_moveto(args[0])
                    self.scrollbar.set(*args)

    def create_table(self, lyst1, lyst2):

        table = []

        lyst1_size = len(lyst1)

        for i in range(lyst1_size):

            self.home_frame.columnconfigure(i, weight=0)

            grid_frame = tk.Frame(self.home_frame, background=self.colors.background)
            grid_frame.grid(row=0, column=i, sticky=tk.NS)

            grid_frame.rowconfigure(0, weight=0)
            grid_frame.rowconfigure(1, weight=1)

            button = ttk.Button(grid_frame, text=lyst1[i],
                                style='Header.TButton')
            button.grid(row=0, column=0, sticky=tk.EW)
            button.bind('<Button-1>', self.button_action)
            self.header_buttons.append(button)

            column = tk.Listbox(grid_frame,
                                foreground=self.colors.foreground,
                                selectforeground=self.colors.background,
                                background=self.colors.background,
                                relief=tk.FLAT,
                                yscrollcommand=self.sync_yview,
                                font=('Roboto', self.resize_utility.body_text()))
            column.grid(row=1, column=0, sticky=tk.NS)


            table.append(column)



            # column.configure(height=len(lyst2[i]))

            self.data_columns.append(column)


        self.home_frame.columnconfigure(lyst1_size + 1, weight=1)
        self.scrollbar.grid(row=0, column=lyst1_size + 1, sticky=tk.N+tk.S+tk.E)

        # self.home_frame.bind('<Configure>', lambda event: self.resize(event=event))

        for i in self.data_columns:
            self.resize_utility.register_element(i, "body")

        self.resize_utility.register_style(self.style, "Header.TButton", "body")

        return table

    def resize(self, event):
        for i in self.data_columns:
            i.configure(font=('Roboto', int(event.height * .02)))
