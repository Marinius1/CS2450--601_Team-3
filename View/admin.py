import tkinter as tk
from tkinter import ttk
from .Colors.color import Color


class Admin():
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

        self.style.map('Header.TButton',
                       background=[('active', self.colors.a8)],
                       foreground=[('active', self.colors.background)])
        self.style.configure('Header.TButton',
                             background=self.colors.a7,
                             foreground=self.colors.background,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10,
                             )

        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure(0, weight=1)

        self.home_frame.columnconfigure(0, weight=0)
        self.home_frame.columnconfigure(1, weight=1)

        self.left_frame = tk.Frame(self.home_frame)
        self.left_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.left_frame.grid(column=0, sticky=tk.NSEW)

        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=21)

        self.left_frame.columnconfigure(0, weight=5)
        self.left_frame.columnconfigure(1, weight=1)
        # self.left_frame.grid_propagate(0)

        self.people_label = ttk.Label(self.left_frame,
                                      text="People",
                                      style='Recent.TLabel')
        self.people_label.grid(row=0, column=0, sticky=tk.W, padx=15)

        self.people_add = ttk.Button(self.left_frame, text="Add",
                                     style='Header.TButton')
        self.people_add.grid(row=0, column=1, sticky=tk.E, padx=(0, 15))

        self.people_listbox = tk.Listbox(self.left_frame,
                                         foreground=self.colors.foreground,
                                         selectforeground=self.colors.background,
                                         background=self.colors.background,
                                         relief=tk.FLAT)
        self.people_listbox.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

        # populate test data
        people_example = [
            {"name_amalgamated": "Iron Man"},
            {"name_amalgamated": "Steel Man"},
            {"name_amalgamated": "Wood Man"},
            {"name_amalgamated": "Quartz Man"},
            {"name_amalgamated": "Helium Man"}
        ]

        self.populate_people(people_example)

        self.right_frame = tk.Frame(self.home_frame)
        self.right_frame.configure(background=self.colors.background, border=3,
                                   relief=tk.RIDGE)
        self.right_frame.grid(row=0, column=1, sticky=tk.NSEW)

        self.right_frame.rowconfigure(tuple(i for i in range(4)), weight=0)
        self.right_frame.columnconfigure(0, weight=1)

        self.field_name = ttk.Label(self.right_frame, text='Iron Man', style='Recent.TLabel')
        self.field_name.configure(font=('Roboto', 48))
        self.field_name.grid(row=0, column=0, sticky=tk.NW, padx=25, pady=15)

        self.people_save = ttk.Button(self.right_frame, text="Save",
                                         style='Header.TButton')
        self.people_save.grid(row=0, column=2, sticky=tk.E)

        self.people_options = ttk.Button(self.right_frame, text="Options",
                                     style='Header.TButton')
        self.people_options.grid(row=0, column=3, sticky=tk.E, padx=(15, 25))

        self.info_identity_frame = tk.Frame(self.right_frame)
        self.info_identity_frame.grid(row=1, sticky=tk.EW, padx=25)

        self.info_identity_frame.rowconfigure(0, weight=1)

        self.create_text_entry(self.info_identity_frame, 'First Name', 'Iron', 0)
        self.create_text_entry(self.info_identity_frame, 'Last Name', 'Man', 1)
        self.create_text_entry(self.info_identity_frame, 'Address', '123 Sesame St.', 2)
        self.create_text_entry(self.info_identity_frame, 'City', 'Las Vegas', 3)

        self.states = ['NV', 'UT', 'AZ']
        self.create_dropdown_menu(self.info_identity_frame, 'State', self.states, 4)
        self.create_text_entry(self.info_identity_frame, 'Phone Number', '123-456-7890', 5)

        self.birthday_label = ttk.Label(self.info_identity_frame, text='Date of Birth')
        self.birthday_label.configure(background=self.colors.background)
        self.birthday_label.grid(row=6, column=1, sticky=tk.W, padx=(10))

        self.days = [i for i in range(1, 32)]
        self.create_dropdown_menu(self.info_identity_frame, 'Day', self.days, 7)

        self.months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        self.create_dropdown_menu(self.info_identity_frame, 'Month', self.months, 8)

        self.years = [i for i in range(1950, 2005)]
        self.create_dropdown_menu(self.info_identity_frame, 'Year', self.years, 9)

        self.create_text_entry(self.info_identity_frame, 'SSN', 'XXX-XX-XXXX', 10)

        self.create_text_entry(self.info_identity_frame, 'Job Title', 'Peasant', 11)
        self.create_text_entry(self.info_identity_frame, 'Team', 'Executive', 12)
        self.create_text_entry(self.info_identity_frame, 'Role', 'Top Dawg', 12)

    def populate_people(self, lyst):

        for i in range(len(lyst)):
            self.people_listbox.insert(tk.END, lyst[i]["name_amalgamated"])

            if i % 2 == 0:
                background = self.colors.background
            else:
                background = self.colors.a7

            self.people_listbox.itemconfigure(i, background=background)

    def create_text_entry(self, master, label, placeholder, row):
        label = ttk.Label(master, text=label)
        label.configure(background=self.colors.background)
        label.grid(row=row, column=0, sticky=tk.E)

        entry = ttk.Entry(master)
        entry.insert(0, placeholder)
        entry.grid(row=row, column=1, sticky=tk.E, padx=(10, 0), pady=5)

    def create_dropdown_menu(self, master, label, options, row):

        label = ttk.Label(master, text=label)
        label.configure(background=self.colors.background)
        label.grid(row=row, column=0, sticky=tk.E)

        value = tk.StringVar(self.master)
        value.set(options[0])
        menu = ttk.OptionMenu(master, value, options[0], *options)
        menu.grid(row=row, column=1, sticky=tk.W, padx=(10, 0), pady=5)

