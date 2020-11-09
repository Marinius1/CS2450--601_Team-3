import tkinter as tk
from tkinter import ttk
from .Colors.color import Color
import random

class TimeCard:
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

        self.home_frame.rowconfigure((0,1), weight=1)

        # prevoius timecards/pay data
        self.scrollbar = tk.Scrollbar(self.home_frame)

        self.data_columns = []


        model_example = [
            ["2020-10-31", "2020-10-15", "2020-09-30"],
            ["32", "45", "42"],
            ["$2500", "3600", "3400"]
        ]

        headers_example = ['Pay Date', 'Hours Worked', 'Amount']

        self.create_table(headers_example, model_example)
        self.scrollbar.configure(command=self.yview)

        self.column_offset = len(self.data_columns)

        self.home_frame.columnconfigure(tuple(self.column_offset + i for i in range(2, 5)), weight=1)

        # current pay
        self.summary_current_pay = self.create_summary_frame(self.home_frame, 'Current Pay', "$2300", 0, self.column_offset + 2)

        # hours worked
        self.summary_hours_worked = self.create_summary_frame(self.home_frame, 'Hours Worked', "39", 1, self.column_offset + 2)

        # nex pay date
        self.summary_next_pay_date = self.create_summary_frame(self.home_frame, 'Next Pay Date', "11-15-20", 0, self.column_offset + 3)

        # pto available
        self.summary_pto_available = self.create_summary_frame(self.home_frame, 'PTO Available', "34 Hours", 1, self.column_offset + 3)


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

        lyst1_size = len(lyst1)

        for i in range(lyst1_size):

            self.home_frame.columnconfigure(i, weight=0)

            grid_frame = tk.Frame(self.home_frame, background='red')
            grid_frame.grid(row=0, column=i, rowspan=2, sticky=tk.NS)

            grid_frame.rowconfigure(0, weight=0)
            grid_frame.rowconfigure(1, weight=1)

            button = ttk.Button(grid_frame, text=lyst1[i],
                                style='Header.TButton')
            button.grid(row=0, column=0, sticky=tk.EW)

            column = tk.Listbox(grid_frame,
                                foreground=self.colors.foreground,
                                selectforeground=self.colors.background,
                                background=self.colors.background,
                                relief=tk.FLAT,
                                yscrollcommand=self.sync_yview)
            column.grid(row=1, column=0, sticky=tk.NS)

            for j in range(len(lyst2[i])):
                column.insert(tk.END, lyst2[i][j])

                if j % 2 == 0:
                    background = self.colors.background
                else:
                    background = self.colors.a7

                column.itemconfigure(j, background=background)
            # column.configure(height=len(lyst2[i]))

            self.data_columns.append(column)

        # self.home_frame.columnconfigure(lyst1_size + 1, weight=1)
        self.scrollbar.grid(row=0, column=lyst1_size + 1, rowspan=2, sticky=tk.N+tk.S+tk.E)

    def create_summary_frame(self, parent, title, content, row, column):
        summary_frame = tk.Frame(parent)
        summary_frame.configure(background=self.colors.background, border=3, relief=tk.RAISED)
        summary_frame.grid(row=row, column=column, sticky=tk.NSEW, padx=10, pady=10)

        summary_frame.rowconfigure(0, weight=1)
        summary_frame.rowconfigure(1, weight=3)
        summary_frame.columnconfigure(0, weight=1)

        summary_frame.grid_propagate(0)

        summary_frame_title = ttk.Label(summary_frame, text=title, style='Recent.TLabel')
        summary_frame_title.configure(font=('Roboto', 40))
        summary_frame_title.grid(row=0, column=0)

        summary_frame_content = ttk.Label(summary_frame, text=content, style='Recent.TLabel')
        summary_frame_content.configure(font=('Roboto', 150, 'bold'))
        summary_frame_content.grid(row=1, column=0)

        summary_frame.bind('<Configure>', lambda event: self.resize_summary_frame(event=event, title=summary_frame_title, content=summary_frame_content))

        return [summary_frame, summary_frame_title, summary_frame_content]

    def resize_summary_frame(self, event, title, content):
        title.configure(font=('Roboto', int(event.height * .1)))
        content.configure(font=('Roboto', int(event.height * .2), 'bold'))
