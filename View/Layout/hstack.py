from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color
from label import Label
from button import Button


class HStack(tk.Frame, UINode):
    """
    the 'row' class. creates a View that arranges children horizontally within
    it's bounds. can auto wrap or truncate if needed. scrolling is also an
    option.
    """

    def __init__(self, master=None, name: str = "", width: int = 10,
                 height: int = 10, theme=None, nodes=None):
        """
        init(name: str, children[]: List<varies>): void
        calls super(). needs to populate the horizontal View. also needs to bind either
        truncate or wrap data when the contents of the horizontal View exceed the
        bounds.
        """
        super().__init__(master)

        self.name = name
        self.colors = Color(theme).colors
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.map(self.name + '.' + 'THStack',
                       background=[('active', self.colors.a7)])
        self.style.configure(self.name + '.' + 'THStack',
                             background="red",
                             foreground=self.colors.foreground,
                             width=width,
                             height=height,
                             borderwidth=2,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10
                             )
        # self.master.configure(background="blue", border=0)
        # self.pack()

        self.pack(side=tk.TOP, anchor=tk.NW, fill=tk.X, expand=False)

        self.nodes = nodes




