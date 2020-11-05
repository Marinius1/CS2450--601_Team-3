from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color


class Homepage(tk.Frame, UINode):
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
        self.master.configure(background="blue")
        self.configure(background="red")

        self.pack(fill=tk.BOTH, expand=1)

        window_width = self.winfo_screenwidth() * 0.3
        print(window_width)

        self.left_panel = tk.Frame(self, width=window_width, background=self.colors.background)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, expand=1)

        # self.listbox_title = tk.Label(self.left_panel, text="")

        self.listbox = tk.Listbox(self.left_panel, width=40, background=self.colors.background, foreground=self.colors.foreground)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, anchor=tk.NW, expand=1, pady=(10,0))


        for i in range(8):
            tmp_label = tk.Label(self, text=i)
            self.listbox.insert(tk.END, tmp_label)

        self.right_panel = tk.Frame(self, background=self.colors.background)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)



