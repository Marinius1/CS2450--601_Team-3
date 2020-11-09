import tkinter as tk
from tkinter import ttk
from .Colors.color import Color
import controller as Controller
import datetime

class TimeCard():
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
        self.click_buffer = []

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
        self.left_frame.rowconfigure(1, weight=0)
        self.left_frame.rowconfigure(2, weight=21)

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
                                         relief=tk.FLAT)
        self.people_listbox.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)

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

        self.info_identity_frame = tk.Frame(self.right_frame)
        self.info_identity_frame.grid(row=1, sticky=tk.EW, padx=25)

        self.info_identity_frame.rowconfigure(0, weight=1)

        self.display_employee = self.create_text_display(self.info_identity_frame, 'Employee ID:', '', 0)

        self.display_pay_type = self.create_text_display(self.info_identity_frame, 'Pay Type:', '', 1)

        # salary specific widgets
        self.display_salary = None

        # hourly specific widgets
        self.display_hourly = None

        # commission specific widgets
        self.display_commission = None

        self.display_hours_worked = self.create_text_display(self.info_identity_frame, 'Hours Worked', '', 5)

        self.field_hours_modifier = self.create_text_entry(self.info_identity_frame, 'Hours modifier', '0.00', 5, 2)

        self.button_add_hours = ttk.Button(self.info_identity_frame, text="Add", style='Header.TButton', command=self.add_hours)
        self.button_add_hours.grid(row=5, column=4, padx=(10, 0))

        self.button_sub_hours = ttk.Button(self.info_identity_frame, text="Subtract", style='Header.TButton', command=self.sub_hours)
        self.button_sub_hours.grid(row=5, column=5, padx=(10, 0))

        self.set_values(self.people_example[0])

    def add_hours(self):
        current = self.display_hours_worked["entry"].cget('text')
        additional = self.field_hours_modifier["entry"].get()
        self.set_default_display_field(self.display_hours_worked, str(float(current) + float(additional)))

    def sub_hours(self):
        current = self.display_hours_worked["entry"].cget('text')
        additional = self.field_hours_modifier["entry"].get()

        new_hours = float(current) - float(additional)
        if new_hours < 0.0:
            new_hours = 0.0

        self.set_default_display_field(self.display_hours_worked, str(new_hours))

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
        self.set_default_display_field(self.display_employee, data["Employee number"])
        self.set_default_display_field(self.display_pay_type, data["Pay type"])

        self.set_default_display_field(self.display_hours_worked, "10.0")

        thing = list(filter(lambda person: person['Employee number'] == data['Employee number'], self.PTO))

        if len(thing) == 0:
            thing.append(data)

        # self.set_default_text_field(self.field_pto_total, thing[0]["PTO total"])
        # self.set_default_text_field(self.field_pto_used, thing[0]["PTO used"])
        #
        # self.dropdown_pay_type["value"].set(data["Pay type"])
        # self.set_default_text_field(self.field_pay_rate, data["Pay amount"])

        if data["Pay type"] == "Salary":
            if self.display_hourly is not None:
                self.display_hourly["entry"].destroy()
                self.display_hourly["label"].destroy()
                self.display_hourly = None

            if self.display_commission is not None:
                self.display_commission["entry"].destroy()
                self.display_commission["label"].destroy()
                self.display_commission = None

            if self.display_salary is None:
                self.display_salary = self.create_text_display(self.info_identity_frame, 'Expected Payout:', '', 3)
            self.set_default_display_field(self.display_salary, thing[0]["Total pay"])

        if data["Pay type"] == "Hourly":
            if self.display_salary is not None:
                self.display_salary["entry"].destroy()
                self.display_salary["label"].destroy()
                self.display_salary = None

            if self.display_commission is not None:
                self.display_commission["entry"].destroy()
                self.display_commission["label"].destroy()
                self.display_commission = None

            if self.display_hourly is None:
                self.display_hourly = self.create_text_display(self.info_identity_frame, 'Expected Payout:', '', 3)
            self.set_default_display_field(self.display_hourly, thing[0]["Total pay"])

        if data["Pay type"] == "Commission":

            if self.display_hourly is not None:
                self.display_hourly["entry"].destroy()
                self.display_hourly["label"].destroy()
                self.display_hourly = None

            if self.display_salary is None:
                self.display_salary = self.create_text_display(self.info_identity_frame, 'Expected Payout:', '', 3)
            self.set_default_display_field(self.display_salary, thing[0]["Total pay"])

            if self.display_commission is None:
                self.display_commission = self.create_text_display(self.info_identity_frame, 'Expected Payout:', '', 4)
            self.set_default_display_field(self.display_commission, thing[0]["Total pay"])


    #Get data from save button
    def get_values(self):
        data = {
            # "First name": self.field_first_name["entry"].cget("text"),
            # "Last name": self.field_last_name["entry"].cget("text"),
            #
            "Employee number": self.display_employee["entry"].cget("text"),
            #
            # "PTO total": self.field_pto_total["entry"].cget("text"),
            # "PTO used": self.field_pto_used["entry"].cget("text"),
            "Pay type": self.display_pay_type["entry"].cget("text"),
            "Hours worked": self.display_hours_worked["entry"].cget("text")
        }

        if self.display_salary is not None:
            data["Total pay"] = self.display_salary["entry"].cget('text')
        if self.display_hourly is not None:
            data["Total pay"] = self.display_hourly["entry"].cget('text')
        if self.display_commission is not None:
            data["Base pay"] = self.display_salary["entry"].cget('text')
            data["Total pay"] = self.display_commission["entry"].cget('text')

        print(data)

        return data

    def set_default_display_field(self, field, value):
        field["entry"].configure(text=value)

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
            "PTO total": "0",
            "PTO used": "0",
        }

        self.set_values(default_data)
        self.save_action = self.save_employee

    def save_employee(self):
        datax = self.get_values()
        Controller.Employee_Adder(datax)
        self.L.reload()
        self.people_example = self.L.data

        self.clear_listbox()
        self.populate_people(self.people_example)

    def edit_employee(self):
        datax = self.get_values()
        Controller.Employee_Editer(self.click_buffer, datax)
        self.L.reload()
        self.people_example = self.L.data

        self.clear_listbox()
        self.populate_people(self.people_example)

    def listbox_select(self, event, lyst):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(tk.ACTIVE)
        self.click_buffer = self.get_values()
        # print("selection:", selection[0], ": '%s'" % value)

        self.set_values(lyst[selection[0]])
        self.save_action = self.edit_employee

    def clear_listbox(self):
        self.people_listbox.delete(0, tk.END)

    def populate_people(self, lyst):

        #setup listbox click evnets
        self.people_listbox.bind("<Double-Button-1>", lambda event: self.listbox_select(event, lyst))

        for i in range(len(lyst)):
            self.people_listbox.insert(tk.END, lyst[i]["First name"] + " " + lyst[i]["Last name"] + " - " + lyst[i]["Employee number"])

            if i % 2 == 0:
                background = self.colors.background
            else:
                background = self.colors.a7

            self.people_listbox.itemconfigure(i, background=background)

    def create_text_display(self, master, label, placeholder, row, column_start=0, sticky=tk.E):
        label = ttk.Label(master, text=label)
        label.configure(background=self.colors.background)
        label.grid(row=row, column=column_start, sticky=sticky)

        entry = ttk.Label(master, text=placeholder, background=self.colors.background)
        entry.grid(row=row, column=column_start + 1, sticky=tk.W, padx=(10, 0), pady=5)
        return {"label": label, "entry": entry}

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

