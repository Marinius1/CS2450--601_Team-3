import tkinter as tk
from tkinter import ttk
from .Colors.color import Color
from .button import Button
import os


class NavBar():
    """
    button input widget. allows the user to execute a defined action on
    click. is configurable to either show text, show an image, or both. also
    manages animation states.
    """

    def __init__(self, master=None, name: str = "", width: int = 10,
                 height: int = 10, theme=None, window=None):
        """
        init(name: str, text: str, image_path: str, children=[]:
        List<mixed>, type: int): void init method. calls super() to properly
        initialize all class data members. also calls appropriate class
        methods as needed.
        """
        self.master = master

        self.name = name

        self.colors = Color(theme).colors
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.nav_frame = tk.Frame(self.master)
        self.nav_frame.configure(background=self.colors.background, border=3, relief=tk.RIDGE)
        self.nav_frame.grid(row=0, column=0, sticky=tk.EW)


        menubar = tk.Menu(self.master)
        self.fileMenu = tk.Menu(self.master, tearoff=0)
        self.fileMenu.add_command(label="Exit")
        menubar.add_cascade(label="File", menu=self.fileMenu)

        # self.toolbar = tk.Frame(self.master)
        # self.toolbar.rowconfigure(0, weight=1)
        # self.toolbar.grid(row=0, sticky=tk.W)

        # setup logo
        self.eimg = tk.PhotoImage(file='./View/AnyEmployee.gif')
        self.eimg.subsample(100, 100)
        self.img_label = tk.Label(self.nav_frame, image=self.eimg,
                                  background=self.colors.background)
        self.img_label.grid(row=0, column=0, sticky=tk.W)
        self.style.map('Nav.TButton', background=[('active', self.colors.a7)],
                       foreground=[('active', self.colors.background)])
        self.style.configure('Nav.TButton',
                             background=self.colors.background,
                             foreground=self.colors.foreground,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10
                             )
        
        self.nav_home = ttk.Button(self.nav_frame, text="Home", command=window.home)
        self.nav_home.configure(style='Nav.TButton')
        self.nav_home.grid(row=0, column=1, sticky=tk.NS)

        self.nav_people = ttk.Button(self.nav_frame, text="People", command=window.people)
        self.nav_people.configure(style='Nav.TButton')
        self.nav_people.grid(row=0, column=2, sticky=tk.NS)

        self.nav_time = ttk.Button(self.nav_frame, text="Time Cards")
        self.nav_time.configure(style='Nav.TButton')
        self.nav_time.grid(row=0, column=3, sticky=tk.NS)

        self.nav_pay = ttk.Button(self.nav_frame, text="Payroll")
        self.nav_pay.configure(style='Nav.TButton')
        self.nav_pay.grid(row=0, column=4, sticky=tk.NS)

        self.nav_admin = ttk.Button(self.nav_frame, text="Admin", command=window.admin)
        self.nav_admin.configure(style='Nav.TButton')
        self.nav_admin.grid(row=0, column=5, sticky=tk.NS)

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
