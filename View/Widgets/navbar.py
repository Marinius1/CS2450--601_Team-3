from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color
from label import Label
from hstack import HStack
from button import Button


class NavBar(tk.Frame, UINode):
    """
    button input widget. allows the user to execute a defined action on
    click. is configurable to either show text, show an image, or both. also
    manages animation states.
    """

    def __init__(self, master=None, name: str = "", width: int = 10,
                 height: int = 10, theme=None):
        """
        init(name: str, text: str, image_path: str, children=[]:
        List<mixed>, type: int): void init method. calls super() to properly
        initialize all class data members. also calls appropriate class
        methods as needed.
        """
        super().__init__(master)


        self.name = name

        '''
        self.colors = Color(theme).colors
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.style.map(self.name + '.' + 'TNavBar',
                       background=[('active', self.colors.a7)])
        self.style.configure(self.name + '.' + 'TNavBar',
                             background=self.colors.background,
                             foreground=self.colors.foreground,
                             width=width,
                             height=height,
                             borderwidth=2,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10
                             )
        # self.master.configure(width=width, height=height, background=self.colors.background, border=0)

        self.configure(style=self.name + '.' + 'TNavBar')
        '''

        menubar = tk.Menu(self.master)
        self.fileMenu = tk.Menu(self.master, tearoff=0)
        self.fileMenu.add_command(label="Exit")
        menubar.add_cascade(label="File", menu=self.fileMenu)

        toolbar = tk.Frame(self.master, bd=0)

        Button(toolbar, text="Test", theme="Ubuntu", side=tk.LEFT)
        Button(toolbar, text="Test", theme="Ubuntu", side=tk.LEFT)
        Button(toolbar, text="Test", theme="Ubuntu", side=tk.LEFT)



        self.nodes = [
            '''
            Label(self, name="nav_label", text="Any Employee",
                width=25, height=25, theme=theme, side=tk.LEFT, padx=(30, 0)),
            Button(self, name="nav_home", width=10, height=30, text="Home", theme=theme, side=tk.LEFT),
            Button(self, name="nav_people", width=10, height=30, text="People", theme=theme, side=tk.LEFT),
            Button(self, name="nav_time", width=10, height=30, text="Time Cards", theme=theme, side=tk.LEFT),
            Button(self, name="nav_reciepts", width=10, height=30, text="Reciepts", theme=theme, side=tk.LEFT),
            Button(self, name="nav_admin", width=10, height=30, text="Admin", theme=theme, side=tk.LEFT)
            '''
        ]

        toolbar.pack(side=tk.TOP, fill=tk.X)
        self.master.config(menu=menubar)
        self.pack()

        # self.button = ttk.Button(self.master, text=text, style=self.name + '.' + 'TNavBar')


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
