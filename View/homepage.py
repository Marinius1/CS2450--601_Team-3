import tkinter as tk
from tkinter import ttk
from .Colors.color import Color


class Homepage():
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

        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure(0, weight=1)

        self.home_frame.columnconfigure(0, weight=0)
        self.home_frame.columnconfigure(1, weight=8)

        self.left_frame = tk.Frame(self.home_frame)
        self.left_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        # self.left_frame.grid(column=0, sticky=tk.NSEW)

        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=21)

        self.left_frame.columnconfigure(0, weight=1)

        # self.recent_actions_label = ttk.Label(self.left_frame,
        #                                       text="Recent Actions",
        #                                       style='Recent.TLabel')
        # self.recent_actions_label.grid(row=0, sticky=tk.EW, padx=15)
        #
        # self.recent_actions_listbox = tk.Listbox(self.left_frame,
        #                                          foreground=self.colors.foreground,
        #                                          selectforeground=self.colors.background,
        #                                          background=self.colors.background,
        #                                          relief=tk.FLAT)
        # self.recent_actions_listbox.grid(row=1, column=0, sticky=tk.NSEW, padx=(15, 15))
        #
        # for i in range(50):
        #     self.recent_actions_listbox.insert(tk.END, "Jacob Jenson was fired - 2020-11-05")
        #
        # self.recent_actions_scrollbar = tk.Scrollbar(self.left_frame)
        # self.recent_actions_scrollbar.grid(row=1, column=1, sticky=tk.NS)
        #
        # self.recent_actions_listbox.configure(yscrollcommand=self.recent_actions_scrollbar.set)
        # self.recent_actions_scrollbar.configure(command=self.recent_actions_listbox.yview)

        self.right_frame = tk.Frame(self.home_frame)
        self.right_frame.configure(background=self.colors.background, border=3,relief=tk.RIDGE)
        self.right_frame.grid(row=0, column=1, sticky=tk.NSEW)

        self.right_frame.columnconfigure((0, 1, 2), weight=1)
        self.right_frame.rowconfigure((0, 1), weight=1)

        self.summary_0 = self.create_summary_frame(parent=self.right_frame, title="Payroll", content="153", row=0, column=0)
        self.summary_1 = self.create_summary_frame(parent=self.right_frame, title="People", content="42", row=0, column=1)
        self.summary_2 = self.create_summary_frame(parent=self.right_frame, title="Admin", content="$3.50", row=0, column=2)
        # self.summary_3 = self.create_summary_frame(parent=self.right_frame, title="Next Payout", content="$2500", row=1, column=0)
        # self.summary_4 = self.create_summary_frame(parent=self.right_frame, title="Deductibles", content="$5000", row=1, column=1)
        # self.summary_5 = self.create_summary_frame(parent=self.right_frame, title="Quarterly Overtime", content="$18", row=1, column=2)

        self.summary_0[0].bind("<Button-1>", lambda event: window.pay())
        self.summary_1[0].bind("<Button-1>", lambda event: window.people())
        self.summary_2[0].bind("<Button-1>", lambda event: window.admin())

    def create_summary_frame(self, parent, title, content, row, column):
        summary_frame = tk.Frame(parent)
        summary_frame.configure(background=self.colors.background, border=3, relief=tk.RAISED)
        summary_frame.grid(row=row, column=column, sticky=tk.NSEW, padx=10, pady=10)

        summary_frame.rowconfigure(0, weight=1)
        summary_frame.columnconfigure(0, weight=1)

        summary_frame.grid_propagate(0)

        summary_frame_title = ttk.Label(summary_frame, text=title, style='Recent.TLabel')
        summary_frame_title.configure(font=('Roboto', 52, 'bold'))
        summary_frame_title.grid(row=0, column=0)

        # summary_frame_content = ttk.Label(summary_frame, text=content, style='Recent.TLabel')
        # summary_frame_content.configure(font=('Roboto', 150, 'bold'))
        # summary_frame_content.grid(row=1, column=0)

        summary_frame.bind('<Configure>', lambda event: self.resize_summary_frame(event=event, title=summary_frame_title))


        return [summary_frame, summary_frame_title]

    def resize_summary_frame(self, event, title):
        title.configure(font=('Roboto', int(event.height * .1)))
