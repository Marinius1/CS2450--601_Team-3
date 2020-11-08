
import tkinter as tk
from tkinter import ttk
from .Colors.color import Color

import random


class Payroll():
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
                       background=[('active', self.colors.a7)],
                       foreground=[('active', self.colors.background)])
        self.style.configure('Header.TButton',
                             background=self.colors.background,
                             foreground=self.colors.foreground,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a10
                             )

        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3, relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure(0, weight=1)

        self.scrollbar = tk.Scrollbar(self.home_frame)

        self.data_columns = []

        self.names_example = [
            "Cathrine Turek",
            "Danette Strachan",
            "Teodoro Schamber",
            "Johanne Sidener",
            "Willette Kirch",
            "Amal Gupton",
            "Leonor Slifer",
            "Olive Tesch",
            "Beulah Doby",
            "Desirae Twellman",
            "Roman Rippeon",
            "Juliann Mascorro",
            "Wynell Westbury",
            "Glen Overmyer",
            "Ilse Hoggard",
            "Leta Presson",
            "Kenya Lizaola",
            "Carmelina Kollman",
            "Mae Cherry",
            "Jimmie Felker",
            "Mia Wahl",
            "Joanie Stillwell",
            "Leonard Littlefield",
            "Meghan Tignor",
            "Candi Diangelo",
            "Zita Mangrum",
            "Bibi Campbell",
            "Jacalyn Cox",
            "Corrinne Glymph",
            "Norberto Stilwell",
            "Lashanda Alligood",
            "Josphine Atienza",
            "Krystina Breedlove",
            "Verlene Dye",
            "Hee Bugarin",
            "Fredia Mckinnie",
            "Marisha Ricci",
            "Jackie Slaugh",
            "Santina Suydam",
            "Leonora Gathings",
            "Rashad Ousley",
            "Reena Gitlin",
            "Loyd Vivas",
            "Astrid Pop",
            "Millard Allan",
            "Marianna Heisler",
            "Divina Barrus",
            "Jasmin Selke",
            "Petra Dahl",
            "Wilburn Agrawal",
            "Kimiko Digby",
            "Larisa Rouillard",
            "Allene Sprau",
            "Emma Duncan",
            "Brittani Paz",
            "Alvera Curlin",
            "Karrie Kovats",
            "Jacinta Cash",
            "Fatimah Ecker",
            "Rosann Valenti",
            "Christoper Greenhaw",
            "Myrtice Dorsey",
            "Vanessa Toland",
            "Cathi Cone",
            "Theodore Neiss",
            "Guadalupe Knittel",
            "Winnie Durham",
            "Tiny Tabares",
            "Rochell Garr",
            "Shandra Gillison",
            "Georgie Clinton",
            "Minta Battista",
            "Fatima Lauber",
            "Lyndia Burbridge",
            "Bari Alleyne",
            "Jacalyn Migues",
            "Katlyn Riess",
            "Annabell Mcfate",
            "Debroah Graffam",
            "Xavier Bodie",
            "Claud Locke",
            "Deandrea Pozo",
            "Crysta Fritch",
            "Janey Wendland",
            "Love Muriel",
            "Mozelle Kroenke",
            "Mckinley Chancy",
            "Cira Mace",
            "Milda Stamant",
            "Karl Levis",
            "Bettina Merlo",
            "Jong Fritts",
            "Elma Khang",
            "Magdalena Elzey",
            "Loreta Dole",
            "Beverlee Mota",
            "Manuel Link",
            "Michaela Ferrante",
            "Oswaldo Scriber "
        ]

        pay_types_example = ["Salary", "Hourly", "Commissioned"]

        model_example = [
            self.names_example,
            [pay_types_example[random.randint(0,2)] for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)]
        ]

        headers_example = ['Employee', 'Pay Type', 'Current Pay', 'Last Pay']

        self.create_table(headers_example, model_example)
        self.scrollbar.configure(command=self.yview)

    def yview(self, *args):

        for i in self.data_columns:
            i.yview(*args)

            pos = i.yview()
            self.scrollbar.set(pos[0], pos[1])

    def sync_yview(self, *args):

        for i in range(len(self.data_columns)):
            data_columns_copy = self.data_columns.copy()
            data_columns_copy.pop(i)

            sync_check = [self.data_columns[i].yview() == j.yview() for j in data_columns_copy]

            if not all(sync_check):
                for k in range(len(self.data_columns)):
                    if k != i:
                        self.data_columns[k].yview_moveto(args[0])
                    self.scrollbar.set(*args)

    def create_table(self, lyst1, lyst2):

        lyst1_size = len(lyst1)

        for i in range(lyst1_size):

            self.home_frame.columnconfigure(i, weight=0)

            grid_frame = tk.Frame(self.home_frame, background='red')
            grid_frame.grid(row=0, column=i, sticky=tk.NS)

            grid_frame.rowconfigure(0, weight=0)
            grid_frame.rowconfigure(1, weight=1)

            button = ttk.Button(grid_frame, text=lyst1[i],
                                style='Header.TButton')
            button.grid(row=0, column=0, sticky=tk.EW)

            column = tk.Listbox(grid_frame,
                                foreground=self.colors.foreground,
                                selectforeground=self.colors.background,
                                background=self.colors.background,
                                relief=tk.FLAT,
                                yscrollcommand=self.sync_yview)
            column.grid(row=1, column=0, sticky=tk.NS)

            for j in range(len(lyst2[i])):
                column.insert(tk.END, lyst2[i][j])

                if j % 2 == 0:
                    background = self.colors.background
                else:
                    background = self.colors.a7

                column.itemconfigure(j, background=background)
            # column.configure(height=len(lyst2[i]))

            self.data_columns.append(column)

        # self.home_frame.columnconfigure(lyst1_size + 1, weight=1)
        self.scrollbar.grid(row=0, column=lyst1_size + 1, sticky=tk.N+tk.S+tk.E)


