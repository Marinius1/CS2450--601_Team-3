from ui_node import UINode
import tkinter as tk
from tkinter import ttk
from color import Color


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

        # populate test data
        people_example = [
            {
                "name_amalgamated": "Helium Man",
                "first_name": "Helium",
                "last_name": "Man",
                "address": "123 Sesame St.",
                "city": "Las Vegas",
                "state": "NV",
                "phone": "123-456-7890",
                "ssn": "111-111-1111",
                "job_title": "Peasant",
                "team": "Executive",
                "role": "Top Dawg"
            },
        ]

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
                                     style='Header.TButton', command=self.set_default_values)
        self.people_add.grid(row=0, column=1, sticky=tk.E, padx=(0, 15))

        self.people_listbox = tk.Listbox(self.left_frame,
                                         foreground=self.colors.foreground,
                                         selectforeground=self.colors.background,
                                         background=self.colors.background,
                                         relief=tk.FLAT)
        self.people_listbox.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)


        self.populate_people(people_example)

        self.right_frame = tk.Frame(self.home_frame)
        self.right_frame.configure(background=self.colors.background, border=3,
                                   relief=tk.RIDGE)
        self.right_frame.grid(row=0, column=1, sticky=tk.NSEW)

        self.right_frame.rowconfigure(tuple(i for i in range(4)), weight=0)
        self.right_frame.columnconfigure(0, weight=1)

        self.field_name = ttk.Label(self.right_frame, text=people_example[0]["name_amalgamated"], style='Recent.TLabel')
        self.field_name.configure(font=('Roboto', 48))
        self.field_name.grid(row=0, column=0, sticky=tk.NW, padx=25, pady=15)

        self.people_save = ttk.Button(self.right_frame, text="Save",
                                         style='Header.TButton', command=self.save_employee())
        self.people_save.grid(row=0, column=2, sticky=tk.E)

        self.people_options = ttk.Button(self.right_frame, text="Options",
                                     style='Header.TButton')
        self.people_options.grid(row=0, column=3, sticky=tk.E, padx=(15, 25))

        self.info_identity_frame = tk.Frame(self.right_frame)
        self.info_identity_frame.grid(row=1, sticky=tk.EW, padx=25)

        self.info_identity_frame.rowconfigure(0, weight=1)

        self.field_first_name = self.create_text_entry(self.info_identity_frame, 'First Name', people_example[0]["first_name"], 0)
        self.field_last_name = self.create_text_entry(self.info_identity_frame, 'Last Name', people_example[0]["last_name"], 1)
        self.field_address = self.create_text_entry(self.info_identity_frame, 'Address', people_example[0]["address"], 2)
        self.field_city = self.create_text_entry(self.info_identity_frame, 'City', people_example[0]["city"], 3)

        self.states = ['NV', 'UT', 'AZ']
        self.drowdown_state = self.create_dropdown_menu(self.info_identity_frame, 'State', self.states, 4)
        self.field_phone = self.create_text_entry(self.info_identity_frame, 'Phone Number', people_example[0]["phone"], 5)

        self.birthday_label = ttk.Label(self.info_identity_frame, text='Date of Birth', background=self.colors.background)
        self.birthday_label.grid(row=6, column=0, sticky=tk.E)
        self.date_birthday = self.create_date_selector(self.info_identity_frame, 6)

        self.field_ssn = self.create_text_entry(self.info_identity_frame, 'SSN', people_example[0]["ssn"], 7)

        self.field_job_title = self.create_text_entry(self.info_identity_frame, 'Job Title', people_example[0]["job_title"], 8)
        self.field_team = self.create_text_entry(self.info_identity_frame, 'Team', people_example[0]["team"], 9)
        self.field_role = self.create_text_entry(self.info_identity_frame, 'Role', people_example[0]["role"], 10)

    def set_default_values(self):
        self.field_name.configure(text="Default Name")

        self.set_default_text_field(self.field_first_name, "First Name")
        self.set_default_text_field(self.field_last_name, "Last Name")
        self.set_default_text_field(self.field_address, "123 Example St.")
        self.set_default_text_field(self.field_city, "Example City")

        # state
        self.drowdown_state["value"].set('UT')

        # birthday
        self.date_birthday["day"]["value"].set('1')
        self.date_birthday["month"]["value"].set('1')
        self.date_birthday["year"]["value"].set('2000')

        self.set_default_text_field(self.field_phone, "000-000-0000")
        self.set_default_text_field(self.field_ssn, "XXX-XX-XXXX")
        self.set_default_text_field(self.field_job_title, "Default Job Title")
        self.set_default_text_field(self.field_team, "Default Team")
        self.set_default_text_field(self.field_role, "Default Role")

    def get_values(self):
        return {
            "name_amalgamated": self.field_name.cget("text"),
            "first_name": self.field_first_name["entry"].get(),
            "last_name": "Man",
            "address": "123 Sesame St.",
            "city": "Las Vegas",
            "state": "NV",
            "phone": "123-456-7890",
            "ssn": "111-111-1111",
            "job_title": "Peasant",
            "team": "Executive",
            "role": "Top Dawg"
        }

    def set_default_text_field(self, field, value):
        field["entry"].delete(0, 'end')
        field["entry"].insert(0, value)

    def add_employee(self):
        self.set_default_text_field()

    def save_employee(self):
        data = self.get_values()
        print(data)

    def populate_people(self, lyst):

        for i in range(len(lyst)):
            self.people_listbox.insert(tk.END, lyst[i]["name_amalgamated"])

            if i % 2 == 0:
                background = self.colors.background
            else:
                background = self.colors.a7

            self.people_listbox.itemconfigure(i, background=background)

    def create_text_entry(self, master, label, placeholder, row, column_start=0):
        label = ttk.Label(master, text=label)
        label.configure(background=self.colors.background)
        label.grid(row=row, column=column_start, sticky=tk.E)

        entry = ttk.Entry(master)
        entry.insert(0, placeholder)
        entry.grid(row=row, column=column_start + 1, sticky=tk.W, padx=(10, 0), pady=5)
        return {"label": label, "entry": entry}

    def create_dropdown_menu(self, master, label, options, row, column_start=0):

        label = ttk.Label(master, text=label)
        label.configure(background=self.colors.background)
        label.grid(row=row, column=column_start, sticky=tk.E)

        value = tk.StringVar(self.master)
        value.set(options[0])
        menu = ttk.OptionMenu(master, value, options[0], *options)
        menu.grid(row=row, column=column_start + 1, sticky=tk.W, padx=(10, 10), pady=5)
        return {"label": label, "menu": menu, "value": value}

    def create_date_selector(self, master, row):
        frame = tk.Frame(master, background=self.colors.background)
        frame.grid(row=row, column=1, columnspan=4, sticky=tk.W, padx=(10))
        frame.columnconfigure((0,1,2,3), weight=1)

        days = [i for i in range(1, 32)]
        day_dropdown = self.create_dropdown_menu(frame, 'Day', days, 0, 0)

        months = [
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
        months_dropdown= self.create_dropdown_menu(frame, 'Month', months, 0, 2)

        years = [i for i in range(1950, 2005)]
        years_dropdown= self.create_dropdown_menu(frame, 'Year', years, 0, 4)

        return {
            "day": {"label": day_dropdown["label"], "dropdown": day_dropdown["menu"], "value": day_dropdown["value"]},
            "month": {"label": months_dropdown["label"], "dropdown": months_dropdown["menu"], "value": months_dropdown["value"]},
            "year": {"label": years_dropdown["label"], "dropdown": years_dropdown["menu"], "value": years_dropdown["value"]},
        }