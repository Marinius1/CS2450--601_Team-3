import tkinter as tk
from tkinter import ttk
from .Colors.color import Color
from View.resize_utility import ResizeUtility
import controller as Controller
import datetime

class Admin():
    """
    the 'row' class. creates a View that arranges children horizontally within
    it's bounds. can auto wrap or truncate if needed. scrolling is also an
    option.
    """

    def __init__(self, master=None, name: str = "", width: int = 10,
                 height: int = 10, theme=None, window=None):
        """
        init(name: str, children[]: List<varies>): void
        calls super(). needs to populate the horizontal View. also needs to bind either
        truncate or wrap data when the contents of the horizontal View exceed the
        bounds.
        """

        #potential changes detected flag
        self.changes_detected = False
        # populate test data
        self.L = Controller.List_Maker()
        self.people_example = self.L.data
        self.click_buffer = []
      
        self.master = master
        self.theme=theme
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.resize_utility = ResizeUtility(self.master)

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

        self.style.configure(style='Recent.TLabel', font=('Roboto', self.resize_utility.body_text()))
        self.resize_utility.register_style(self.style, 'Recent.TLabel', "body")


        self.style.map('Entry.TEntry')
        self.style.configure(
            'Entry.TLabel',
            foreground=self.colors.foreground,
            background=self.colors.background,
            borderwidth=1,
            bordercolor=self.colors.foreground,
            relief=tk.SUNKEN,
            padding=[10,1,1,1],
            font=('Roboto', 24)
        )
        self.resize_utility.register_style(self.style, 'Entry.TEntry', "body")

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
                             font=('Roboto', 16)
                             )

        self.style.configure(style='Header.TButton', font=('Roboto', self.resize_utility.body_text()))
        self.resize_utility.register_style(self.style, 'Header.TButton', "body")

        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure(0, weight=1)

        self.home_frame.columnconfigure(0, weight=1)
        self.home_frame.columnconfigure(1, weight=9)

        self.left_frame = tk.Frame(self.home_frame)
        self.left_frame.configure(background=self.colors.background, border=3,
                                  relief=tk.RIDGE)
        self.left_frame.grid(column=0, sticky=tk.NSEW)

        self.left_frame.rowconfigure(0, weight=1)
        self.left_frame.rowconfigure(1, weight=0)
        self.left_frame.rowconfigure(2, weight=21)

        self.left_frame.columnconfigure(0, weight=2)
        self.left_frame.columnconfigure(1, weight=1)
        # self.left_frame.grid_propagate(0)

        self.people_label = ttk.Label(self.left_frame,
                                      text="People",
                                      style='Recent.TLabel')
        self.people_label.grid(row=0, column=0, sticky=tk.W, padx=15)

        self.people_add = ttk.Button(self.left_frame, text="Add",
                                     style='Header.TButton', command=self.add_employee)
        self.people_add.grid(row=0, column=1, sticky=tk.E, padx=(0, 15))

        self.frame_search = tk.Frame(self.left_frame, background=self.colors.background)
        self.frame_search.grid(row=1, column=0, columnspan=2, sticky=tk.EW)

        self.search_value = tk.StringVar()
        self.search_value.set("Search")
        self.search_value.trace("w", self.search)
        self.entry_search = ttk.Entry(self.frame_search, textvariable=self.search_value)
        # self.entry_search.bind("<Key>", self.search)
        # self.entry_search.bind("<Button-1>", lambda x: "break")

        self.entry_search.grid(row=0, column=0)

        self.search_options = ["First name", "Last name", "Employee number"]
        self.search_option_value = tk.StringVar(self.master)
        self.search_option_value.set(self.search_options[0])
        self.dropdown_search = ttk.OptionMenu(self.frame_search, self.search_option_value, self.search_options[0], *self.search_options)
        self.dropdown_search.grid(row=0, column=1, sticky=tk.E)

        self.people_listbox = tk.Listbox(self.left_frame,
                                         foreground=self.colors.foreground,
                                         selectforeground=self.colors.background,
                                         background=self.colors.background,
                                         relief=tk.FLAT,
                                         font=('Roboto', 16))
        self.people_listbox.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)

        self.resize_utility.register_element(self.people_listbox, "body")

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

        self.save_action = self.save_employee

        self.people_save = ttk.Button(self.right_frame, text="Save",
                                         style='Header.TButton', command=lambda: self.create_are_you_sure("Confirm Changes?", self.save_action))
        self.people_save.grid(row=0, column=2, sticky=tk.E)

        self.people_delete = ttk.Button(self.right_frame, text="Delete",
                                     style='Header.TButton', command=lambda: self.create_are_you_sure("Confirm Delete?", self.del_employee))
        self.people_delete.grid(row=0, column=3, sticky=tk.E, padx=(15, 25))

        self.info_identity_frame = tk.Frame(self.right_frame, background=self.colors.background)
        self.info_identity_frame.grid(row=1, sticky=tk.EW, padx=25)

        self.info_identity_frame.rowconfigure(0, weight=1)

        self.section_info = tk.Label(self.info_identity_frame, text="Employee Info", font=('Roboto', 20), foreground=self.colors.background, background=self.colors.a7)
        self.section_info.grid(row=0, column=0, pady=self.screen_height * 0.025, columnspan=5, sticky=tk.EW)
        self.resize_utility.register_element(self.section_info, "heading-large")

        self.field_first_name = self.create_text_entry(self.info_identity_frame, 'First Name', '', 1)
        self.field_last_name = self.create_text_entry(self.info_identity_frame, 'Last Name', '', 1, 2)
        self.field_address = self.create_text_entry(self.info_identity_frame, 'Address', '', 2)
        self.field_city = self.create_text_entry(self.info_identity_frame, 'City', '', 2, 2)

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
        self.field_phone['label'].grid(pady=self.screen_height * 0.025)
        self.field_phone['entry'].grid(pady=self.screen_height * 0.025)

        self.birthday_label = ttk.Label(self.info_identity_frame, text='Date of Birth', background=self.colors.background)
        self.birthday_label.grid(row=6, column=0, sticky=tk.E)
        self.date_birthday = self.create_date_selector(self.info_identity_frame, 6)

        self.field_ssn = self.create_text_entry(self.info_identity_frame, 'SSN', '', 7)
        self.field_ssn['label'].grid(pady=(0, self.screen_height * 0.025))
        self.field_ssn['entry'].grid(pady=(0, self.screen_height * 0.025))

        self.section_job_info = tk.Label(self.info_identity_frame, text="Job Info", font=('Roboto', 20), foreground=self.colors.background, background=self.colors.a7)
        self.section_job_info.grid(row=8, column=0, pady=self.screen_height * 0.025, columnspan=5, sticky=tk.EW)
        self.resize_utility.register_element(self.section_job_info, "heading-large")

        self.field_job_title = self.create_text_entry(self.info_identity_frame, 'Job Title', '', 9)
        self.field_team = self.create_text_entry(self.info_identity_frame, 'Team', '', 9, 2)
        self.field_role = self.create_text_entry(self.info_identity_frame, 'Role', '', 10)
        self.field_id = self.create_text_entry(self.info_identity_frame, 'Employee ID', '', 10, 2)

        self.start_employment_label = ttk.Label(self.info_identity_frame, text='Start Date', background=self.colors.background)
        self.start_employment_label.grid(row=12, column=0, sticky=tk.E)
        self.date_start_employment = self.create_date_selector(self.info_identity_frame, 12)

        self.info_start_employment_label = tk.Label(self.info_identity_frame, text='Total months with company: ', background=self.colors.background)
        self.info_start_employment_label.grid(row=12, column=5, sticky=tk.E)

        self.info_start_employment_data = tk.Label(self.info_identity_frame, text='', background=self.colors.background)
        self.info_start_employment_data.grid(row=12, column=6, sticky=tk.E)

        self.label_pay_type = tk.Label(self.info_identity_frame, text="Pay type", background=self.colors.background)
        self.label_pay_type.grid(row=15, column=0, sticky=tk.E)

        self.pay_types = ["Salary", "Hourly", "Commission"]
        # self.dropdown_pay_type = self.create_dropdown_menu(self.info_identity_frame, 'Pay Type', self.pay_types, 15)
        self.value_pay_type = tk.StringVar()

        self.field_pay_rate = self.create_text_entry(self.info_identity_frame, 'Pay Rate', '', 16)
        self.field_pay_salary = self.create_text_entry(self.info_identity_frame, 'Salary', '', 16, 2)

        self.radio_hourly = tk.Radiobutton(self.info_identity_frame, text="Hourly", variable=self.value_pay_type, value=self.pay_types[1], background=self.colors.background, command=lambda: self.toggle_hourly_fields());
        self.radio_hourly.grid(row=15, column=1)

        self.radio_salary = tk.Radiobutton(self.info_identity_frame, text="Salary", variable=self.value_pay_type, value=self.pay_types[0], background=self.colors.background, command=lambda: self.toggle_salary_fields());
        self.radio_salary.grid(row=15, column=2)

        self.radio_commission = tk.Radiobutton(self.info_identity_frame, text="Commission", variable=self.value_pay_type, value=self.pay_types[2], background=self.colors.background, command=lambda: self.toggle_commission_fields());
        self.radio_commission.grid(row=15, column=3)



        self.set_values(self.people_example[0])

    def search(self, *args):


        value = self.search_value.get()

        if value == "Search":
            return

        if value == '':
            self.clear_listbox()
            self.populate_people(self.people_example)

        self.clear_listbox()

        results = []

        search_filter = self.search_option_value.get()

        for i in self.people_example:
            if value in i[search_filter]:
                results.append(i)

        self.populate_people(results)


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
        self.timewith = datetime.date.today() -  datetime.date(int(data["Start year"]), int(data["Start month"]), int(data["Start day"]))
        self.info_start_employment_data.config(text=str(int(self.timewith.days / 31)))
        #print(datetime.date.today())
        #thing = list(filter(lambda person: person['Employee number'] == data['Employee number'], self.PTO))

        #if len(thing) == 0:
            #thing.append(data)
   

        # self.dropdown_pay_type["value"].set(data["Pay type"])
        self.value_pay_type.set(data["Pay type"])

        if data["Commission"] == "None" and data["Salary"] == "None":

            self.set_default_text_field(self.field_pay_rate, data["Hourly"])
        elif data["Hourly"] == "None" and data["Commission"] != "None":

            self.set_default_text_field(self.field_pay_rate, data["Commission"])
            self.set_default_text_field(self.field_pay_salary, data["Salary"])
        else:

            self.set_default_text_field(self.field_pay_salary, data["Salary"])



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
            # "Pay type": self.dropdown_pay_type["value"].get(),
            "Pay type": self.value_pay_type.get(),
            "Hourly": self.field_pay_rate["entry"].get(),
            "Commission": self.field_pay_rate["entry"].get(),
            "Salary": self.field_pay_salary["entry"].get(),
        }

    def set_default_text_field(self, field, value):
        field["entry"].delete(0, 'end')
        field["entry"].insert(0, value)

    def del_employee(self):
        datay = self.get_values()

        emp_identifier = {
            "Employee number": datay["Employee number"],
            "First name": datay["First name"],
            "Last name": datay["Last name"]
        }
        Controller.Employee_Deleter(emp_identifier)
        self.L.reload()
        self.people_example = self.L.data

        self.clear_listbox()
        self.populate_people(self.people_example)

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
        }

        self.set_values(default_data)
        self.save_action = self.save_employee

    def save_employee(self):
        self.changes_detected = False
        datax = self.get_values()
        Controller.Employee_Adder(datax)
        self.L.reload()
        self.people_example = self.L.data

        self.clear_listbox()
        self.populate_people(self.people_example)

    def edit_employee(self):
        self.changes_detected = False
        datax = self.get_values()
        Controller.Employee_Editer(self.click_buffer, datax)
        self.L.reload()
        self.people_example = self.L.data

        self.clear_listbox()
        self.populate_people(self.people_example)

    def listbox_select(self, event, lyst):
        if (self.changes_detected):
            self.create_are_you_sure("Would you like to save your changes?", self.save_action, self.set_changes_flag)
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(tk.ACTIVE)
        self.click_buffer = self.get_values()
        # print("selection:", selection[0], ": '%s'" % value)

        self.toggle_pay_fields(lyst[selection[0]])

        self.set_values(lyst[selection[0]])
        self.save_action = self.edit_employee

    def toggle_pay_fields(self, data):
        if data["Commission"] == "None" and data["Salary"] == "None":
            self.field_pay_salary["label"].grid_remove()
            self.field_pay_salary["entry"].grid_remove()

            self.field_pay_rate["label"].grid()
            self.field_pay_rate["entry"].grid()

        elif data["Hourly"] == "None" and data["Commission"] != "None":
            self.field_pay_salary["label"].grid()
            self.field_pay_salary["entry"].grid()
            self.field_pay_rate["label"].grid()
            self.field_pay_rate["entry"].grid()

        else:
            self.field_pay_salary["label"].grid()
            self.field_pay_salary["entry"].grid()
            self.field_pay_rate["label"].grid_remove()
            self.field_pay_rate["entry"].grid_remove()

    def toggle_salary_fields(self):
        self.field_pay_salary["label"].grid()
        self.field_pay_salary["entry"].grid()
        self.field_pay_rate["label"].grid_remove()
        self.field_pay_rate["entry"].grid_remove()

    def toggle_commission_fields(self):
        self.field_pay_salary["label"].grid()
        self.field_pay_salary["entry"].grid()
        self.field_pay_rate["label"].grid()
        self.field_pay_rate["entry"].grid()

    def toggle_hourly_fields(self):
        self.field_pay_salary["label"].grid_remove()
        self.field_pay_salary["entry"].grid_remove()

        self.field_pay_rate["label"].grid()
        self.field_pay_rate["entry"].grid()

    def clear_listbox(self):
        self.people_listbox.delete(0, tk.END)

    def populate_people(self, lyst):

        #setup listbox click evnets
        self.people_listbox.bind("<Double-Button-1>", lambda event: self.listbox_select(event, lyst))

        for i in range(len(lyst)):
            self.people_listbox.insert(tk.END, lyst[i]["First name"] + " " + lyst[i]["Last name"] + " - " + lyst[i]["Employee number"])

            if i % 2 == 0:
                background = self.colors.background
                foreground = "#000000" if self.theme == "Builtin Light" else self.colors.a7
            else:
                background = self.colors.a7
                foreground = "#000000" if self.theme == "Builtin Light" else self.colors.background

            self.people_listbox.itemconfigure(i, background=background, foreground=foreground)

    def create_text_entry(self, master, label, placeholder, row, column_start=0, sticky=tk.E):
        label = ttk.Label(master, text=label, style='Recent.TLabel')
        label.configure(background=self.colors.background)
        label.grid(row=row, column=column_start, sticky=sticky)

        entry = ttk.Entry(master, style='Entry.TEntry')
        entry.bind('<Key>', lambda event: self.set_changes_flag(True))
        entry.insert(0, placeholder)
        entry.grid(row=row, column=column_start + 1, sticky=tk.W, padx=(10, 0), pady=5)
        return {"label": label, "entry": entry}

    def create_dropdown_menu(self, master, label, options, row, column_start=0):

        label = ttk.Label(master, text=label, style='Recent.TLabel')
        label.configure(background=self.colors.background)
        label.grid(row=row, column=column_start, sticky=tk.E)

        value = tk.StringVar(self.master)
        value.set(options[0])
        menu = ttk.Combobox(master, textvariable=value, value=options[0], values=options, height=3)
        menu.grid(row=row, column=column_start + 1, sticky=tk.W, padx=(10, 10), pady=5)
        menu.bind('<Button>', lambda event: self.set_changes_flag(True))
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

    def create_are_you_sure(self, message, on_success, on_cancel=None):
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
        if on_cancel: cancel_button = ttk.Button(button_frame, text="Cancel", style='Header.TButton',command=lambda:[on_cancel(False),top.destroy()])
        else: cancel_button = ttk.Button(button_frame, text="Cancel", style='Header.TButton',command=lambda:top.destroy())
        cancel_button.grid(row=0, column=1, sticky=tk.E, padx=(0, width / 10))


    def set_changes_flag(self, flag):
        self.changes_detected = flag

