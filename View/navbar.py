import tkinter as tk
from tkinter import ttk
from .Colors.color import Color
from View.resize_utility import ResizeUtility
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

        self.resize_utility = ResizeUtility(window.master)

        self.name = name

        self.colors = Color(theme).colors
        self.style = ttk.Style()
        self.style.theme_use('alt')

        self.nav_frame = tk.Frame(self.master)
        self.nav_frame.configure(background=self.colors.background, border=3, relief=tk.RIDGE)
        self.nav_frame.grid(row=0, column=0, sticky=tk.EW)

        self.help_content = "./View/help_files/lorem.txt"

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

        self.style.configure(style='Nav.TButton', font=('Roboto', self.resize_utility.heading_three_text()))
        self.resize_utility.register_style(self.style, 'Nav.TButton', "h3")

        self.style.map('Help.TButton', background=[('active', self.colors.a8)],
                       foreground=[('active', self.colors.background)])
        self.style.configure('Help.TButton',
                             background=self.colors.a7,
                             foreground=self.colors.background,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10
                             )
        self.style.configure(style='Help.TButton', font=('Roboto', self.resize_utility.body_text()))
        self.resize_utility.register_style(self.style, 'Help.TButton', "h3")

        self.style.map('Help.TLabel')
        self.style.configure('Help.TLabel', font=('Roboto', self.resize_utility.heading_three_text()))


        self.nav_home = ttk.Button(self.nav_frame, text="Home", command=window.home)
        self.nav_home.configure(style='Help.TButton')
        self.nav_home.grid(row=0, column=6, sticky=tk.W, padx=(25, 25))

        # self.nav_people = ttk.Button(self.nav_frame, text="People", command=window.people)
        # self.nav_people.configure(style='Nav.TButton')
        # self.nav_people.grid(row=0, column=2, sticky=tk.NS)
        #
        # self.nav_pay = ttk.Button(self.nav_frame, text="Payroll", command=window.pay)
        # self.nav_pay.configure(style='Nav.TButton')
        # self.nav_pay.grid(row=0, column=3, sticky=tk.NS)
        #
        # self.nav_admin = ttk.Button(self.nav_frame, text="Admin", command=window.admin)
        # self.nav_admin.configure(style='Nav.TButton')
        # self.nav_admin.grid(row=0, column=4, sticky=tk.NS)

        # help button
        self.nav_frame.columnconfigure(6, weight=1)
        self.button_help = ttk.Button(self.nav_frame, text="Help", style='Help.TButton', command=self.help)
        self.button_help.grid(row=0, column = 6, sticky=tk.E, padx=(25, 25))


    def help(self):
        self.create_help_modal("Innovative EmpTrack")

    def set_help_content(self, path):
        self.help_content = path

    def create_help_modal(self, message):
        top = tk.Toplevel(self.master)

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        width = screen_width / 2
        height = screen_height / 2

        x_pos = (screen_width / 2) - (width / 2)
        y_pos = (screen_height / 2) - (height / 2)

        top.geometry("%dx%d%+d%+d" % (width, height, x_pos, y_pos))
        top.transient(self.master)
        top.grab_set()

        top.title("Help")

        top.rowconfigure(0, uniform='row', weight=1)
        top.rowconfigure(1, uniform='row', weight=6)
        top.rowconfigure(2, uniform='row', weight=1)
        top.columnconfigure(0, weight=1)

        frames = []
        for i in range(3):
            frame = tk.Frame(top, background=self.colors.background)
            frame.grid(row=i, sticky=tk.NSEW)
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0, weight=1)
            frames.append(frame)

        top_message = ttk.Label(frames[0], text=message, background=self.colors.background, style='Help.TLabel')
        top_message.grid(row=0)

        text_scrollbar = tk.Scrollbar(frames[1])
        text_scrollbar.grid(row=0, column=1, sticky=tk.NS)

        with open(self.help_content, 'r') as f:
            text = f.read()

        text_help = tk.Text(frames[1], font=('Roboto', 20), highlightthickness=0, yscrollcommand=text_scrollbar.set, wrap=tk.WORD)
        text_help.insert(tk.END, text)

        text_help.bind("<Key>", lambda x: "break")

        text_help.grid(row=0, sticky=tk.EW, padx=(10, 0))

        text_scrollbar.configure(command=text_help.yview)

        button_close = ttk.Button(frames[2], text="Close", style='Header.TButton', command=top.destroy)
        button_close.grid(row=0, sticky=tk.E, padx=(0, 25))

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
