from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color


class Label(ttk.Label, UINode):
    """
    read-only text area that can show messages to the user as needed. can color
    text as well.
    """

    def __init__(self, master=None, name: str = "", width: int = 10,
                 height: int = 10, text="", theme=None, side=tk.TOP):
        """
        init(name: str, children: List<varied>): void
        call super(). initially this is not visible, set the desired message text if
        provided. configure proper colors such as 'error', 'warning', etc..
        """
        super().__init__(master)

        self.name = name
        self.colors = Color(theme).colors
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.map(self.name + '.' + 'TLabel', background=[('active', self.colors.a7)])
        self.style.configure(self.name + '.' + 'TLabel',
                             background=self.colors.background,
                             foreground=self.colors.foreground,
                             width=width,
                             height=height,
                             borderwidth=2,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10
                             )
        self.master.configure(width=width, height=height, background=self.colors.background, border=0)

        self.configure(text=text, style=self.name + '.' + 'TLabel')
        self.pack(side=side)

