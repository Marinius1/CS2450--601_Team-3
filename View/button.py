from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color


class Button(ttk.Button, UINode):
    """
    button input widget. allows the user to execute a defined action on
    click. is configurable to either show text, show an image, or both. also
    manages animation states.
    """

    def __init__(self, master=None, name: str = "", width: int = 10,
                 height: int = 10, text="", theme=None, side=tk.TOP, padx=0, pady=0):
        """
        init(name: str, text: str, image_path: str, children=[]:
        List<mixed>, type: int): void init method. calls super() to properly
        initialize all class data members. also calls appropriate class
        methods as needed.
        """
        super().__init__(master)

        self.name = name
        self.colors = Color(theme).colors
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.map(self.name + '.' + 'TButton', background=[('active', self.colors.a7)])
        self.style.configure(self.name + '.' + 'TButton',
                             background=self.colors.background,
                             foreground=self.colors.foreground,
                             width=width,
                             height=height,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10
                             )
        self.master.configure(width=width, height=height, background=self.colors.background, border=0)

        self.configure(text=text, style=self.name + '.' + 'TButton')

        self.pack(side=side, padx=padx, pady=pady, fill=tk.Y)

        # self.button = ttk.Button(self.master, text=text, style=self.name + '.' + 'TButton')


'''
@abstract method implementation
do(): void
class level implementation of this method. will emit an appropriate
signal to the controller.
'''

'''
click(): void
method bound to the button click event. executes the do() method as well as any
additional logic that may be needed.
'''

'''
set_text(text: str): void
overrides the current text data member with a new value.
'''

'''
set_image_path(image_path: str): void
override the current image path with a new value. force image reload if needed.
'''

'''
set_type(type: int): void
set the type of the button widget. (0: text, 1: image, 2: both) and rebuild.
'''
