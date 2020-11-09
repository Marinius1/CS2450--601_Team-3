import tkinter as tk
from tkinter import ttk
from .Colors.color import Color
import controller as Controller
import datetime

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
        self.L = Controller.List_Maker()
        self.P = Controller.PTO_Maker()
        self.people_example = self.L.data
        self.PTO = self.P.PTO_lyst
        '''
            {
                "name": "Helium Man",
                "first_name": "Helium",
                "last_name": "Man",
                "address": "123 Sesame St.",
                "city": "Las Vegas",
                "state": "NV",
                "zip": "84062",
                "birthday": {
                    "day": "12",
                    "month": "March",
                    "year": "1999"
                },
                "phone": "123-456-7890",
                "ssn": "111-111-1111",
                "job_title": "Peasant",
                "team": "Executive",
                "role": "Top Dawg",
                "id": "12345",
                "start_employment": {
                    "day": "12",
                    "month": "March",
                    "year": "1999"
                },
                "total_time": "52",
                "total_pto": "32",
                "used_pto": "7",
                "pay_type": "Salary",
                "pay_rate": "$32,000"
            },
            {
                "name": "Carbon Man",
                "first_name": "Carbon",
                "last_name": "Man",
                "address": "Google Rd.",
                "city": "Sacramento",
                "state": "NV",
                "zip": "84062",
                "birthday": {
                    "day": "12",
                    "month": "March",
                    "year": "1999"
                },
                "phone": "123-456-7890",
                "ssn": "111-111-1111",
                "job_title": "Peasant",
                "team": "Executive",
                "role": "Top Dawg",
                "id": "56789",
                "start_employment": {
                    "day": "12",
                    "month": "March",
                    "year": "1999"
                },
                "total_time": "52",
                "total_pto": "32",
                "used_pto": "7",
                "pay_type": "Hourly",
                "pay_rate": "$32,000"
            }
        ]
            '''
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
                                     style='Header.TButton', command=self.add_employee)
        self.people_add.grid(row=0, column=1, sticky=tk.E, padx=(0, 15))

        self.people_listbox = tk.Listbox(self.left_frame,
                                         foreground=self.colors.foreground,
                                         selectforeground=self.colors.background,
                                         background=self.colors.background,
                                         relief=tk.FLAT)
        self.people_listbox.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

        self.populate_people(self.people_example)

        self.right_frame = tk.Frame(self.home_frame)
        self.right_frame.configure(background=self.colors.background, border=3,
                                   relief=tk.RIDGE)
        self.right_frame.grid(row=0, column=1, sticky=tk.NSEW)

        self.right_frame.rowconfigure(tuple(i for i in range(4)), weight=0)
        self.right_frame.columnconfigure(0, weight=1)

        self.field_name = ttk.Label(self.right_frame, text='', style='Recent.TLabel')
        self.field_name.configure(font=('Roboto', 48))
        self.field_name.grid(row=0, column=0, sticky=tk.NW, padx=25, pady=15)

        self.people_save = ttk.Button(self.right_frame, text="Save",
                                         style='Header.TButton', command=lambda: self.create_are_you_sure("Confirm Changes?", self.save_employee))
        self.people_save.grid(row=0, column=2, sticky=tk.E)

        self.people_delete = ttk.Button(self.right_frame, text="Delete",
                                     style='Header.TButton', command=lambda: self.create_are_you_sure("Confirm Delete?", self.delete_employee))
        self.people_delete.grid(row=0, column=3, sticky=tk.E, padx=(15, 25))

        self.info_identity_frame = tk.Frame(self.right_frame)
        self.info_identity_frame.grid(row=1, sticky=tk.EW, padx=25)

        self.info_identity_frame.rowconfigure(0, weight=1)

        self.field_first_name = self.create_text_entry(self.info_identity_frame, 'First Name', '', 0)
        self.field_last_name = self.create_text_entry(self.info_identity_frame, 'Last Name', '', 1)
        self.field_address = self.create_text_entry(self.info_identity_frame, 'Address', '', 2)
        self.field_city = self.create_text_entry(self.info_identity_frame, 'City', '', 3)

        self.states = ["Alaska",
                  "Alabama",
                  "Arkansas",
                  "American Samoa",
                  "Arizona",
                  "California",
                  "Colorado",
                  "Connecticut",
                  "District of Columbia",
                  "Delaware",
                  "Florida",
                  "Georgia",
                  "Guam",
                  "Hawaii",
                  "Iowa",
                  "Idaho",
                  "Illinois",
                  "Indiana",
                  "Kansas",
                  "Kentucky",
                  "Louisiana",
                  "Massachusetts",
                  "Maryland",
                  "Maine",
                  "Michigan",
                  "Minnesota",
                  "Missouri",
                  "Mississippi",
                  "Montana",
                  "North Carolina",
                  " North Dakota",
                  "Nebraska",
                  "New Hampshire",
                  "New Jersey",
                  "New Mexico",
                  "Nevada",
                  "New York",
                  "Ohio",
                  "Oklahoma",
                  "Oregon",
                  "Pennsylvania",
                  "Puerto Rico",
                  "Rhode Island",
                  "South Carolina",
                  "South Dakota",
                  "Tennessee",
                  "Texas",
                  "Utah",
                  "Virginia",
                  "Virgin Islands",
                  "Vermont",
                  "Washington",
                  "Wisconsin",
                  "West Virginia",
                  "Wyoming"]
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
            "December"]
        self.dropdown_state = self.create_dropdown_menu(self.info_identity_frame, 'State', self.states, 4)

        self.field_zip = self.create_text_entry(self.info_identity_frame, "Zip", '', 4, 2)

        self.field_phone = self.create_text_entry(self.info_identity_frame, 'Phone Number', '', 5)

        self.birthday_label = ttk.Label(self.info_identity_frame, text='Date of Birth', background=self.colors.background)
        self.birthday_label.grid(row=6, column=0, sticky=tk.E)
        self.date_birthday = self.create_date_selector(self.info_identity_frame, 6)

        self.field_ssn = self.create_text_entry(self.info_identity_frame, 'SSN', '', 7)

        self.field_job_title = self.create_text_entry(self.info_identity_frame, 'Job Title', '', 8)
        self.field_team = self.create_text_entry(self.info_identity_frame, 'Team', '', 9)
        self.field_role = self.create_text_entry(self.info_identity_frame, 'Role', '', 10)
        self.field_id = self.create_text_entry(self.info_identity_frame, 'Employee ID', '', 11)

        self.start_employment_label = ttk.Label(self.info_identity_frame, text='Start Date', background=self.colors.background)
        self.start_employment_label.grid(row=12, column=0, sticky=tk.E)
        self.date_start_employment = self.create_date_selector(self.info_identity_frame, 12)

        self.info_start_employment_label = tk.Label(self.info_identity_frame, text='Total months with company: ')
        self.info_start_employment_label.grid(row=12, column=5, sticky=tk.E)

        self.info_start_employment_data = tk.Label(self.info_identity_frame, text='')
        self.info_start_employment_data.grid(row=12, column=6, sticky=tk.E)


        self.field_pto_total = self.create_text_entry(self.info_identity_frame, 'Total PTO', '', 13)
        self.field_pto_used = self.create_text_entry(self.info_identity_frame, 'Used PTO', '', 14)

        self.pay_types = ["Salary", "Hourly", "Commission"]
        self.dropdown_pay_type = self.create_dropdown_menu(self.info_identity_frame, 'Pay Type', self.pay_types, 15)
        self.field_pay_rate = self.create_text_entry(self.info_identity_frame, 'Pay Rate', '', 16)

        self.set_values(self.people_example[0])

    def set_values(self, data):
        self.field_name.configure(text=data["First name"] + " " + data["Last name"])
        self.set_default_text_field(self.field_first_name, data["First name"])
        self.set_default_text_field(self.field_last_name, data["Last name"])
        self.set_default_text_field(self.field_address, data["Address"])
        self.set_default_text_field(self.field_city, data["City"])

        # state
        self.dropdown_state["value"].set(data["State"])
        self.set_default_text_field(self.field_zip, data["Zip"])
        # birthday
        self.date_birthday["day"]["value"].set(data["Birth day"])
        self.date_birthday["month"]["value"].set(self.months[int(data["Birth month"]) - 1])
        self.date_birthday["year"]["value"].set(data["Birth year"])

        self.set_default_text_field(self.field_phone, data["Phone"])
        self.set_default_text_field(self.field_ssn, data["Social security"])
        self.set_default_text_field(self.field_job_title, data["Position"])
        self.set_default_text_field(self.field_team, data["Team"])
        self.set_default_text_field(self.field_role, data["Role"])
        self.set_default_text_field(self.field_id, data["Employee number"])

        self.date_start_employment["day"]["value"].set(data["Start day"])
        self.date_start_employment["month"]["value"].set(self.months[int(data["Start month"]) -1])
        self.date_start_employment["year"]["value"].set(data["Start year"])
        timewith = datetime.date.today() -  datetime.date(int(data["Start year"]), int(data["Start month"]), int(data["Start day"]))
        self.info_start_employment_data.config(text=str(int(timewith.days / 31)))
        print(datetime.date.today())
        thing = list(filter(lambda person: person['Employee number'] == data['Employee number'], self.PTO))

        if len(thing) == 0:
            thing.append(data)

        self.set_default_text_field(self.field_pto_total, thing[0]["PTO total"])
        self.set_default_text_field(self.field_pto_used, thing[0]["PTO used"])

        self.dropdown_pay_type["value"].set(data["Pay type"])
        self.set_default_text_field(self.field_pay_rate, data["Pay amount"])


    #Get data from save button
    def get_values(self):
        return {
            "First name": self.field_first_name["entry"].get(),
            "Last name": self.field_last_name["entry"].get(),
            "Address": self.field_address["entry"].get(),
            "City": self.field_city["entry"].get(),
            "State": self.dropdown_state["value"].get(),
            "Zip": self.field_zip["entry"].get(),
            "Birth day": self.date_birthday["day"]["value"].get(),
            "Birth month": str(self.months.index(self.date_birthday["month"]["value"].get()) +1),
            "Birth year": self.date_birthday["year"]["value"].get(),
            "Phone": self.field_phone["entry"].get(),
            "Social security": self.field_ssn["entry"].get(),
            "Position": self.field_job_title["entry"].get(),
            "Team": self.field_team["entry"].get(),
            "Role": self.field_role["entry"].get(),
            "Employee number": self.field_id["entry"].get(),
            "Start day": self.date_start_employment["day"]["value"].get(),
            "Start month": str(self.months.index(self.date_start_employment["month"]["value"].get()) + 1),
            "Start year": self.date_start_employment["year"]["value"].get(),
            "PTO total": self.field_pto_total["entry"].get(),
            "PTO used": self.field_pto_used["entry"].get(),
            "Pay type": self.dropdown_pay_type["value"].get(),
            "Pay amount": self.field_pay_rate["entry"].get()
        }

    def set_default_text_field(self, field, value):
        field["entry"].delete(0, 'end')
        field["entry"].insert(0, value)

    def delete_employee(self):
        print("delete employee method")

    def add_employee(self):

        default_data = {
            "Employee number": "xx-xxxxx",
            "First name": "First Name",
            "Last name": "Last Name",
            "Pay type": "Hourly",
            "Pay amount": "00.00",
            "Address": "123 Example St.",
            "State": "Alaska",
            "City": "Anchorage",
            "Zip": "00000",
            "Birth day": "1",
            "Birth month": "1",
            "Birth year": "2000",
            "Social security": "xxx-xx-xxxx",
            "Phone": "xxx-xxx-xxxx",
            "Start day": "1",
            "Start month": "1",
            "Start year": "2000",
            "Hours/sales": "1",
            "Role": "Example Role",
            "Position": "Example",
            "Team": "Example Team",
            "PTO total": "0",
            "PTO used": "0",
        }

        self.set_values(default_data)

    def save_employee(self):
        datax = self.get_values()
        Controller.Employee_Adder(datax)
        self.L.reload
        self.people_example = self.L.data



    def listbox_select(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(tk.ACTIVE)
        # print("selection:", selection[0], ": '%s'" % value)

        self.set_values(self.people_example[selection[0]])

    def populate_people(self, lyst):

        #setup listbox click evnets
        self.people_listbox.bind("<Double-Button-1>", self.listbox_select)

        for i in range(len(lyst)):
            self.people_listbox.insert(tk.END, lyst[i]["First name"] + " " + lyst[i]["Last name"])

            if i % 2 == 0:
                background = self.colors.background
            else:
                background = self.colors.a7

            self.people_listbox.itemconfigure(i, background=background)

    def create_text_entry(self, master, label, placeholder, row, column_start=0, sticky=tk.E):
        label = ttk.Label(master, text=label)
        label.configure(background=self.colors.background)
        label.grid(row=row, column=column_start, sticky=sticky)

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

        months_dropdown = self.create_dropdown_menu(frame, 'Month', self.months, 0, 2)

        years = [i for i in range(1950, 2005)]
        years_dropdown= self.create_dropdown_menu(frame, 'Year', years, 0, 4)

        return {
            "day": {"label": day_dropdown["label"], "dropdown": day_dropdown["menu"], "value": day_dropdown["value"]},
            "month": {"label": months_dropdown["label"], "dropdown": months_dropdown["menu"], "value": months_dropdown["value"]},
            "year": {"label": years_dropdown["label"], "dropdown": years_dropdown["menu"], "value": years_dropdown["value"]},
        }

    def create_are_you_sure(self, message, on_success):
        top = tk.Toplevel(self.master)

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        width = screen_width / 6
        height = screen_height / 6

        x_pos = (screen_width / 2) - (width / 2)
        y_pos = (screen_height / 2) - (height / 2)

        top.geometry("%dx%d%+d%+d" % (width, height, x_pos, y_pos))
        top.transient(self.master)
        top.grab_set()

        top.title("Are You Sure?")

        top.rowconfigure((0,1), weight=1)
        top.columnconfigure((0,1,2), weight=1)

        question = ttk.Label(top, text=message, background=self.colors.background)
        question.grid(row=0, column=1)

        button_frame = tk.Frame(top)
        button_frame.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW, pady=(height / 10, 0))
        button_frame.columnconfigure((0,1), weight=1)

        yes_button = ttk.Button(button_frame, text="Yes", style='Header.TButton', command=lambda:[on_success(), top.destroy()])
        yes_button.grid(row=0, column=0, sticky=tk.W, padx=(width / 10, 0))

        cancel_button = ttk.Button(button_frame, text="Cancel", style='Header.TButton',command=top.destroy)
        cancel_button.grid(row=0, column=1, sticky=tk.E, padx=(0, width / 10))
