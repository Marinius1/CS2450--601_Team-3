from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color
from button import Button


class Menu():
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
        '''
        self.name = name
        self.colors = Color(theme).colors
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.map(self.name + '.' + 'THStack', background=[('active', self.colors.a7)])
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

        self.test_button_0 = Button(self, name="test_hs_0", width=10, height=30, text="hs0", theme=theme, side=tk.LEFT)
        self.test_button_1 = Button(self, name="test_hs_1", width=10, height=30, text="hs1", theme=theme, side=tk.LEFT)
        self.test_button_2 = Button(self, name="test_hs_1", width=10, height=30, text="hs1", theme=theme, side=tk.LEFT)
        self.test_button_3 = Button(self, name="test_hs_1", width=10, height=30, text="hs1", theme=theme, side=tk.LEFT)
        self.test_button_4 = Button(self, name="test_hs_1", width=10, height=30, text="hs1", theme=theme, side=tk.LEFT)
        self.test_button_5 = Button(self, name="test_hs_1", width=10, height=30, text="hs1", theme=theme, side=tk.LEFT)

        '''

        self.file = tk.Menu(self, tearoff=0)
        self.add_cascade(label='File', menu=self.file)
        self.file.add_command(label ='New File', command=None)
        self.file.add_command(label ='Open...', command=None)
        self.file.add_command(label ='Save', command=None)
