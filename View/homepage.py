from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color


class Homepage(UINode):
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

        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure(0, weight=1)

        self.home_frame.columnconfigure(0, weight=1)
        self.home_frame.columnconfigure(1, weight=8)

        self.left_frame = tk.Frame(self.home_frame)
        self.left_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.left_frame.grid(column=0, sticky=tk.NSEW)

        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=21)

        self.left_frame.columnconfigure(0, weight=1)

        self.recent_actions_label = ttk.Label(self.left_frame,
                                              text="Recent Actions",
                                              style='Recent.TLabel')
        self.recent_actions_label.grid(row=0, sticky=tk.EW, padx=15)

        self.recent_actions_listbox = tk.Listbox(self.left_frame,
                                                 foreground=self.colors.foreground,
                                                 selectforeground=self.colors.background,
                                                 background=self.colors.background,
                                                 relief=tk.FLAT)
        self.recent_actions_listbox.grid(row=1, sticky=tk.NSEW, padx=(15, 15))

        for i in range(50):
            self.recent_actions_listbox.insert(tk.END, "Jacob Jenson was fired - 2020-11-05")

        self.right_frame = tk.Frame(self.home_frame)
        self.right_frame.configure(background=self.colors.background, border=3,relief=tk.RIDGE)
        self.right_frame.grid(row=0, column=1, sticky=tk.NSEW)

        self.right_frame.columnconfigure((0, 1, 2), weight=1)
        self.right_frame.rowconfigure((0, 1), weight=1)

        self.summary_frame_0 = tk.Frame(self.right_frame)
        self.summary_frame_0.configure(background=self.colors.background, border=3, relief=tk.RAISED)
        self.summary_frame_0.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=10)

        self.summary_frame_0.rowconfigure(0, weight=1)
        self.summary_frame_0.rowconfigure(1, weight=5)
        self.summary_frame_0.columnconfigure(0, weight=1)
        #
        # self.summary_frame_0_title = ttk.Label(self.summary_frame_0, text="Weekly Hours Worked", style='Recent.TLabel')
        # self.summary_frame_0_title.grid(row=0, column=0)
        #
        # self.summary_frame_0_content = ttk.Label(self.summary_frame_0, text="153", style='Recent.TLabel')
        # self.summary_frame_0_content.configure(font=('Roboto', 152))
        # self.summary_frame_0_content.grid(row=1, column=0)

        self.summary_frame_1 = tk.Frame(self.right_frame)
        self.summary_frame_1.configure(background=self.colors.background, border=3, relief=tk.RAISED)
        self.summary_frame_1.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=10)

        self.summary_frame_2 = tk.Frame(self.right_frame)
        self.summary_frame_2.configure(background=self.colors.background, border=3, relief=tk.RAISED)
        self.summary_frame_2.grid(row=0, column=2, sticky=tk.NSEW, padx=10, pady=10)

        self.summary_frame_3 = tk.Frame(self.right_frame)
        self.summary_frame_3.configure(background=self.colors.background, border=3, relief=tk.RAISED)
        self.summary_frame_3.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)

        self.summary_frame_4 = tk.Frame(self.right_frame)
        self.summary_frame_4.configure(background=self.colors.background, border=3, relief=tk.RAISED)
        self.summary_frame_4.grid(row=1, column=1, sticky=tk.NSEW, padx=10, pady=10)

        self.summary_frame_5 = tk.Frame(self.right_frame)
        self.summary_frame_5.configure(background=self.colors.background, border=3, relief=tk.RAISED)
        self.summary_frame_5.grid(row=1, column=2, sticky=tk.NSEW, padx=10, pady=10)