
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pynput.mouse import Listener
import time
import os

from View.resize_utility import ResizeUtility
from .Colors.color import Color
import controller as Controller

import random


class PayRoll():
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

        self.master = master


        #Grabs data from the controller
        self.L = Controller.List_Maker()
        self.people = self.L.data

        #Sets the theme of the window
        self.theme = theme
        self.name = name
        self.colors = Color(theme).colors
        self.style = ttk.Style()
        self.style.theme_use('alt')

        #grabs needed TK and TTK widgets for frame creation

        self.home_frame = tk.Frame(self.master)
        self.left_frame = tk.Frame(self.home_frame, background=self.colors.background)
        self.table_frame = tk.Frame(self.left_frame, background=self.colors.background)
        self.scrollbar = tk.Scrollbar(self.table_frame)
        self.resize_utility = ResizeUtility(self.master, scrollbar=self.scrollbar, yView=self.yview)

        #Styling
        self.style.map('Recent.TLabel',
                       background=[('active', self.colors.a7)],
                       foreground=[('active', self.colors.background)])
        self.style.configure('Recent.TLabel',
                             background=self.colors.background,
                             foreground=self.colors.foreground,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             font=('Roboto', 24)
                             )

        self.style.configure(style='Recent.TLabel', font=('Roboto', self.resize_utility.body_text()))
        self.resize_utility.register_style(self.style, 'Recent.TLabel', "body")




        self.style.map('Pay.TButton',
                       background=[('active', self.colors.a2)],
                       foreground=[('active', self.colors.background)])
        self.style.configure('Pay.TButton',
                             background=self.colors.a7,
                             foreground=self.colors.background,
                             borderwidth=0,
                             bordercolor=self.colors.a0,
                             focusthickness=3,
                             focuscolor=self.colors.a11,
                             font=('Roboto', 24)
                             )
        self.style.configure(style='Pay.TButton', font=('Roboto', self.resize_utility.body_text()))
        self.resize_utility.register_style(self.style, 'Pay.TButton', "body")

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

        #Sizing utility
        self.resize_utility.register_style(self.style, 'Header.TButton', "body")

        self.home_frame.configure(background=self.colors.background, border=3, relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure(0, weight=1)
        self.home_frame.rowconfigure(1, weight=1)

        self.home_frame.columnconfigure(0, weight=0)
        self.home_frame.columnconfigure(1, weight=1)

        self.left_frame.grid(row=0, rowspan=2, column=0, sticky=tk.NSEW)

        self.left_frame.rowconfigure((0,2), weight=0)
        self.left_frame.rowconfigure(1, weight=1)
        self.left_frame.columnconfigure(0, weight=1)

        self.nav_frame = tk.Frame(self.left_frame, background=self.colors.background)
        self.nav_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.nav_frame.columnconfigure((0,2), weight=0)
        self.nav_frame.columnconfigure(1, weight=1)

        self.search_value = tk.StringVar()
        self.search_value.set("Search")
        self.search_value.trace("w", self.search)
        self.entry_search = ttk.Entry(self.nav_frame, textvariable=self.search_value)
        # self.entry_search.bind("<Key>", self.search)
        # self.entry_search.bind("<Button-1>", lambda x: "break")
        self.entry_search.grid(row=0, column=0)

        self.search_options = ["First name", "Last name", "Employee number"]
        self.search_option_value = tk.StringVar(self.master)
        self.search_option_value.set(self.search_options[0])
        self.dropdown_search = ttk.OptionMenu(self.nav_frame, self.search_option_value, self.search_options[0], *self.search_options)
        self.dropdown_search.grid(row=0, column=1, sticky=tk.W)

        self.pay_periods = ['1', '2', '3']
        self.period_select = self.create_dropdown_menu(self.nav_frame, "Period", self.pay_periods, 0, 2)

        self.font_config = ('Roboto', 16)

        self.table_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.table_frame.rowconfigure(1, weight=1)
        self.table_frame.columnconfigure(0, weight=1)

        self.canvas_columns = []
        self.data_columns = []

        self.scroll_poll = time.time()
        self.headers_example = ['First name', 'Last name', 'Employee number', 'Pay type', 'Hourly', 'Salary', 'Commission', 'PTO total', 'PTO used', 'Hours/sales','Total']
        self.values_list = ['First name', 'Last name', 'Employee number', 'Pay type', 'Hourly', 'Salary', 'Commission', 'PTO', 'PTOused', 'Timecard','Total']

        self.model_example = [
            [random.randint(25,50) for i in range(100)],
            [random.randint(25,50) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)]
        ]

        self.actions = []
        self.create_table(self.table_frame, self.headers_example, self.values_list)

        self.sort_ascending("Last name")

        self.can_listen = False
        self.is_first_draw = True
        self.listener = None

        # self.master.bind('<Configure>', lambda event: self.resize_column(event=event))

        self.scrollbar.configure(command=self.yview)

        self.right_frame = tk.Frame(self.home_frame, background=self.colors.background)
        self.right_frame.grid(row=0, rowspan=2, column=1, sticky=tk.NSEW)

        self.right_frame.rowconfigure((0,1,2), weight=0)
        self.right_frame.columnconfigure(0, weight=1)

        self.right_buttons = tk.Frame(self.right_frame, background=self.colors.background)
        self.right_buttons.grid(row=0, sticky=tk.NSEW)
        self.right_buttons.rowconfigure(0, weight=1)
        self.right_buttons.rowconfigure(1, weight=1)
        self.right_buttons.rowconfigure(2, weight=1)
        self.right_buttons.rowconfigure(3, weight=1)
        self.right_buttons.columnconfigure(0, weight=1)

        self.save_button = ttk.Button(self.right_buttons, text='Save', style='Header.TButton', command=lambda: self.create_are_you_sure("Confirm Changes?", self.save_changes))
        self.save_button.grid(row=0, sticky=tk.NSEW, padx=10, pady=10, columnspan=2)

        self.new_period_button = ttk.Button(self.right_buttons, text='New Pay Period', style='Header.TButton', command=lambda: self.create_are_you_sure("Confirm Changes? This will set all values to zero", self.create_pay_period))
        self.new_period_button.grid(row=1, sticky=tk.NSEW, padx=10, pady=10, columnspan=2)

        self.import_time_button = ttk.Button(self.right_buttons, text='Import Timecards', style='Header.TButton', command=self.import_hourly)
        self.import_time_button.grid(row=2, sticky=tk.NSEW, padx=10, pady=10, columnspan=2)

        self.import_reciept_button = ttk.Button(self.right_buttons, text='Import Reciepts', style='Header.TButton', command=self.import_sales)
        self.import_reciept_button.grid(row=3, sticky=tk.NSEW, padx=10, pady=10, columnspan=2)

        # self.metrics_frame = tk.Frame(self.right_frame, background=self.colors.background)
        # self.metrics_frame.grid(row=1, column=0, sticky=tk.EW)
        #
        # self.metrics_frame.rowconfigure((0,1,2,3,4), weight=0)
        # self.metrics_frame.columnconfigure(0, weight=1)
        #
        # self.metrics_title = tk.Label(self.metrics_frame, text="Metrics", font=('Roboto', 24, 'bold'), background=self.colors.background)
        # self.metrics_title.grid(row=0, sticky=tk.W)
        #
        # self.expected_payout_label = tk.Label(self.metrics_frame, text="Expected payout: ", font=('Roboto', 22), background=self.colors.background)
        # self.expected_payout_label.grid(row=1, sticky=tk.W)
        #
        # self.expected_payout_data = tk.StringVar()
        # self.expected_payout_data.set("$10,000")
        # self.expected_payout_display = tk.Label(self.metrics_frame, textvariable=self.expected_payout_data, font=('Roboto', 22), background=self.colors.background)
        # self.expected_payout_display.grid(row=1, column=1, sticky=tk.W)
        #
        # self.last_payout_label= tk.Label(self.metrics_frame, text="Last payout:", font=('Roboto', 22), background=self.colors.background)
        # self.last_payout_label.grid(row=2, sticky=tk.W)
        #
        # self.last_payout_data = tk.StringVar()
        # self.last_payout_data.set("$10,000")
        # self.expected_payout_display = tk.Label(self.metrics_frame, textvariable=self.last_payout_data, font=('Roboto', 22), background=self.colors.background)
        # self.expected_payout_display.grid(row=2, column=1, sticky=tk.W)

        self.pay_frame = tk.Frame(self.right_frame, background=self.colors.background)
        self.pay_frame.grid(row=2, column=0, sticky=tk.EW)

        self.pay_frame.rowconfigure(0, weight=1)
        self.pay_frame.columnconfigure(0, weight=1)

        self.pay_button = ttk.Button(self.pay_frame, text='Pay', style='Header.TButton', command=self.pay)
        self.pay_button.grid(row=0, column=0, sticky=tk.EW+tk.N, padx=10, pady=10)

        # self.get_table_data()

    def save_changes(self):
        print("save")

        staged_data = self.get_table_data()

        data = []

        for i in staged_data:
            if i["First name"] != '':
                data.append(i)
        Editer=Controller.Save_Payroll_Shits
        Editer(data)
        

    def search(self, *args):


        value = self.search_value.get()

        if value == "Search":
            return

        elif value == '':
            self.set_table_data(self.people)
        else:
            self.set_table_data([
                {
                    "First name": '',
                    "Last name": '',
                    "Employee number": '',
                    "Pay type": '',
                    "Hourly": '',
                    "Salary": '',
                    "Commission": '',
                    "PTO": '',
                    "PTOused": '',
                    "Hours/sales": '',
                    "Total": '',
                }
            ])
            results = []

            search_filter = self.search_option_value.get()

            data = self.people

            for i in data:
                if value in i[search_filter]:
                    results.append(i)



            # print(results)
            self.set_table_data(results)

    def create_pay_period(self):
        self.NP=Controller.New_Pay
        self.NP()
        self.L = Controller.List_Maker()
        self.people = self.L.data

        self.set_table_data([
            {
                "First name": '',
                "Last name": '',
                "Employee number": '',
                "Pay type": '',
                "Hourly": '',
                "Salary": '',
                "Commission": '',
                "PTO": '',
                "PTOused": '',
                "Hours/sales": '',
                "Total": '',
            }
        ])

        self.set_table_data(self.people)


    def create_dropdown_menu(self, master, label, options, row, column_start=0):

        label = ttk.Label(master, text=label)
        label.configure(background=self.colors.background)
        label.grid(row=row, column=column_start, sticky=tk.E)

        value = tk.StringVar(self.master)
        value.set(options[0])
        menu = ttk.Combobox(master, textvariable=value, value=options[0], values=options, height=3)
        menu.grid(row=row, column=column_start + 1, sticky=tk.W, padx=(10, 10), pady=5)
        return {"label": label, "menu": menu, "value": value}

    def sum_pay(self, data):
        return "$" + "{:,}".format(sum(data))

    def pay(self):
        self.pay=Controller.payPay
        self.pay()

        with open('./Payroll.csv') as infile:
            data = infile.readlines()
            datastr = ""
            for i in data:
                datastr += i
            print(data)

        self.create_pay_modal("This is your payroll data\n", datastr)

    def yview(self, *args):
        if time.time() - self.scroll_poll >= .1:
            self.scroll_poll = time.time()
            for i in self.canvas_columns:

                if args[0] == 'moveto':
                    i.yview(args[0], float(args[1]))

                pos = i.yview()
                self.scrollbar.set(pos[0], pos[1])

    def sync_yview(self, *args):

        for i in range(len(self.canvas_columns)):
            data_columns_copy = self.canvas_columns.copy()
            data_columns_copy.pop(i)

            sync_check = [self.canvas_columns[i].yview() == j.yview() for j in data_columns_copy]

            if not all(sync_check):
                for k in range(len(self.canvas_columns)):
                    if k != i:
                        self.canvas_columns[k].yview_moveto(args[0])
                    self.scrollbar.set(*args)

    def get_table_data(self):

        staged_data = []

        for i in self.data_columns:
            temp_data = []
            for j in i:
                try:
                    temp_data.append(j.get())
                except:
                    temp_data.append(j.cget('text'))

            staged_data.append(temp_data)


        rotated_data = list(zip(*staged_data))

        data = []

        for i in rotated_data:

            data.append({
                "First name": i[0],
                "Last name": i[1],
                "Employee number": i[2],
                "Pay type": i[3],
                "Hourly": i[4],
                "Salary": i[5],
                "Commission": i[6],
                "PTO": i[7],
                "PTOused": i[8],
                "Hours/sales": i[9],
                "Total": i[10],
            })

        # print(data)
        # self.set_table_data(data)
        return data


    def set_table_data(self, data):


        if len(data) <= 1:
            for i in self.data_columns:
                for j in range(len(i)):
                    if isinstance(i[j], tk.Entry):
                        i[j].delete(0, tk.END)
                        i[j].insert(tk.END, '')
                    else:
                        i[j].configure(text='')
            if len(data) == 0:
                return

        staged_data = []

        for i in data:
            tmp_list = []
            tmp_list.append(i["First name"])
            tmp_list.append(i["Last name"])
            tmp_list.append(i["Employee number"])
            tmp_list.append(i["Pay type"])
            tmp_list.append(i["Hourly"])
            tmp_list.append(i["Salary"])
            tmp_list.append(i["Commission"])
            tmp_list.append(i["PTO"])
            tmp_list.append(i["PTOused"])
            new_hours_str = i["Hours/sales"].replace("[","")
            new_hours_str = new_hours_str.replace("]","")
            tmp_list.append(new_hours_str)
            tmp_list.append("-")
            staged_data.append(tmp_list)

        new_data = list(zip(*staged_data))


        for i in self.data_columns:
            for j in range(len(new_data[self.data_columns.index(i)])):
                if isinstance(self.data_columns[self.data_columns.index(i)][j], tk.Entry):
                    # print(new_data[self.data_columns.index(i)][j])
                    self.data_columns[self.data_columns.index(i)][j].delete(0, tk.END)
                    self.data_columns[self.data_columns.index(i)][j].insert(tk.END, new_data[self.data_columns.index(i)][j])
                else:
                    # print(new_data[self.data_columns.index(i)][j])
                    self.data_columns[self.data_columns.index(i)][j].configure(text=new_data[self.data_columns.index(i)][j])



    def create_table(self, master, lyst1, lyst2):

        # print(self.people)

        lyst1_size = len(lyst1)

        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        ratio = 7.0/8.0

        initial_width = (width * ratio) / lyst1_size

        for i in range(lyst1_size):
            self.actions.append(self.sort_ascending)

        for i in range(lyst1_size):

            # if lyst1[i] == "Hours/sales":
            #     lyst1[i] = "Timecard"

            master.columnconfigure(i, weight=0)

            grid_frame = tk.Frame(master, background=self.colors.background)
            grid_frame.grid(row=0, column=i, rowspan=2, sticky=tk.NSEW)

            grid_frame.rowconfigure(0, weight=0)
            grid_frame.rowconfigure(1, weight=1)
            grid_frame.columnconfigure(0, weight=1)

            button = ttk.Button(grid_frame, text=lyst1[i],
                                style='Header.TButton')
            if i <= 3:
                button.bind('<Button-1>', self.button_action)

            button.grid(row=0, column=0, sticky=tk.EW)

            if i < 7:

                column = tk.Frame(grid_frame, bd=0, width=initial_width, background=self.colors.background, relief=tk.SUNKEN)
                column.grid(row=1, column=0, sticky=tk.NS)
                column.grid(row=1, column=0, sticky=tk.NS, pady=(0, 0))
                column.rowconfigure(0, weight=1)
                column.columnconfigure(0, weight=1)
                self.resize_utility.register_frame(column)

#This line is weird. Future change for dynamic compatability.
                canvas = tk.Canvas(column, border=0, width=initial_width, height=height, highlightthickness=0, yscrollcommand=self.sync_yview, scrollregion=(0,0,150,((self.resize_utility.body_text() + 6) * len(self.people))))
                canvas.grid(row=0, column=0, sticky=tk.NSEW)
                canvas.bind("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))

                self.resize_utility.register_canvas(canvas, (0,0,initial_width,((self.resize_utility.body_text() + 6) * len(self.people))))
                data_items = []
                for j in range(len(self.people)):
                    if j % 2 == 0:
                        background = self.colors.background
                        foreground = "#000000" if self.theme == "Builtin Light" else self.colors.a7
                    else:
                        background = self.colors.a7
                        foreground = "#000000" if self.theme == "Builtin Light" else self.colors.background

                    try:
                        new_value = self.people[j][lyst2[i]]
                    except:
                        new_value = 0

                    entry = tk.Label(canvas, border=0, highlightthickness=0, background=background, foreground=foreground, font=('Roboto', str(self.resize_utility.body_text())), text=new_value, anchor=tk.CENTER)

                    entry.bind("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
                    self.resize_utility.register_element(entry, "body")
                    canvas.create_window(0, ((self.resize_utility.body_text() + 6) * j), window=entry, anchor=tk.NW, width=initial_width)
                    data_items.append(entry)

                bbox = canvas.bbox("all")
                canvas.configure(scrollregion=bbox)

                self.data_columns.append(data_items)
                self.canvas_columns.append(canvas)
            else:
                column = tk.Frame(grid_frame, bd=0, background=self.colors.background, relief=tk.SUNKEN)
                column.grid(row=1, column=0, sticky=tk.NS, pady=(0, 0))
                column.rowconfigure(0, weight=1)
                column.columnconfigure(0, weight=1)
#This line is weird. Future change for dynamic compatability.
                if i == 9:
                    canvas = tk.Canvas(column, border=0, width=initial_width, height=height,highlightthickness=0, yscrollcommand=self.sync_yview, scrollregion=(0,0,400,((self.resize_utility.body_text() + 6) * len(self.people))))
                else:
                    canvas = tk.Canvas(column, border=0, width=initial_width, height=height,highlightthickness=0, yscrollcommand=self.sync_yview, scrollregion=(0,0,400,((self.resize_utility.body_text() + 6) * len(self.people))))
                canvas.grid(row=0, column=0, sticky=tk.NSEW)
                self.resize_utility.register_canvas(canvas, (0,0,initial_width,((self.resize_utility.body_text() + 6) * len(self.people))))

                canvas.bind("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))

                data_items = []
                for j in range(len(self.people)):
                    if j % 2 == 0:
                        background = self.colors.background
                        foreground = "#000000" if self.theme == "Builtin Light" else self.colors.a7
                    else:
                        background = self.colors.a7
                        foreground = "#000000" if self.theme == "Builtin Light" else self.colors.background
                    if i == 10:
                        new_value = 12
                        entry = tk.Label(canvas, border=0, highlightthickness=0, background=background, foreground=foreground, font=('Roboto', str(self.resize_utility.body_text())), text=new_value, anchor=tk.CENTER)
                        canvas.create_window(0, ((self.resize_utility.body_text() + 6) * j), window=entry, anchor=tk.NW, width=initial_width)
                    elif i ==9:
                        entry = tk.Entry(canvas, border=1, highlightthickness=0, background=background, foreground=foreground, font=('Roboto', str(self.resize_utility.body_text())), width=50, relief=tk.FLAT, justify=tk.CENTER)
                        canvas.create_window(0, ((self.resize_utility.body_text() + 6) * j), window=entry, anchor=tk.NW, width=initial_width)
                    else:
                        entry = tk.Entry(canvas, border=1, highlightthickness=0, background=background, foreground=foreground, font=('Roboto', str(self.resize_utility.body_text())), width=40, relief=tk.FLAT, justify=tk.CENTER)
                        canvas.create_window(0, ((self.resize_utility.body_text() + 6) * j), window=entry, anchor=tk.NW, width=initial_width)

                    entry.bind("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))


                    self.resize_utility.register_element(entry, "body")
                    if i != 10:
                        entry.insert(tk.END, self.people[j][lyst2[i]])
                    data_items.append(entry)

                bbox = canvas.bbox("all")
                canvas.configure(scrollregion=bbox)
                self.data_columns.append(data_items)
                self.canvas_columns.append(canvas)



            # column.configure(height=len(lyst2[i]))

        # self.home_frame.columnconfigure(lyst1_size + 1, weight=1)
        self.scrollbar.grid(row=0, column=lyst1_size + 1, rowspan=2, sticky=tk.N+tk.S+tk.E)




    def create_summary_frame(self, parent, title, content, row, column):


        summary_frame = tk.Frame(parent)
        summary_frame.configure(background=self.colors.background, border=3, relief=tk.RAISED)
        summary_frame.grid(row=row, column=column, sticky=tk.NSEW, padx=10, pady=10)

        summary_frame.rowconfigure(0, weight=1)
        summary_frame.rowconfigure(1, weight=3)
        summary_frame.columnconfigure(0, weight=1)

        summary_frame.grid_propagate(0)

        summary_frame_title = ttk.Label(summary_frame, text=title, style='Recent.TLabel')
        summary_frame_title.configure(font=('Roboto', 40))
        summary_frame_title.grid(row=0, column=0)

        summary_frame_content = ttk.Label(summary_frame, text=content, style='Recent.TLabel')
        summary_frame_content.configure(font=('Roboto', 150, 'bold'))
        summary_frame_content.grid(row=1, column=0)

        summary_frame.bind('<Configure>', lambda event: self.resize_summary_frame(event=event, title=summary_frame_title, content=summary_frame_content))

        return [summary_frame, summary_frame_title, summary_frame_content]

    def resize_summary_frame(self, event, title, content):
        title.configure(font=('Roboto', int(event.height * .1)))
        content.configure(font=('Roboto', int(event.height * .2), 'bold'))

    def resize_column(self, event):

        if not self.can_listen and not self.can_listen and not self.is_first_draw:
            self.can_listen = True

            # print('resize')
            # Collect events until released
            self.listener = Listener(on_click=self.on_click)
            self.listener.start()

        if self.is_first_draw:
            # print('first event')
            self.is_first_draw = False

    def on_mousewheel(self, event, canvas):
        shift = (event.state & 0x1) != 0
        scroll = -1 if event.delta > 0 else 1
        if shift:
            canvas.xview_scroll(scroll, "units")
        else:
            canvas.yview_scroll(scroll, "units")

    def on_click(self, x, y, button, pressed):
        # print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        if not pressed:
            # Stop listener
            width = self.home_frame.winfo_width()
            # print(int(width))
            for i in self.canvas_columns:
                i.configure(font=('Roboto', int(width * .01)), width=int(width * .01))

            self.can_listen = False
            self.listener.stop()
            self.listener = None

            return False

    def import_file(self):
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(),
                                               title="Select file",
                                               filetypes=(("CSV Files", "*.csv"),)
                                               )
        return file_name

    def import_hourly(self):
        file=self.import_file()

        if not file:
            return

        IO=Controller.Import_Hourly
        IO(file)
        self.L = Controller.List_Maker()
        self.people = self.L.data

        self.set_table_data([
            {
                "First name": '',
                "Last name": '',
                "Employee number": '',
                "Pay type": '',
                "Hourly": '',
                "Salary": '',
                "Commission": '',
                "PTO": '',
                "PTOused": '',
                "Hours/sales": '',
                "Total": '',
            }
        ])
        self.set_table_data(self.people)

    def import_sales(self):
        file=self.import_file()

        if not file:
            return

        IO=Controller.Import_Sales
        IO(file)
        self.L = Controller.List_Maker()
        self.people = self.L.data

        self.set_table_data([
            {
                "First name": '',
                "Last name": '',
                "Employee number": '',
                "Pay type": '',
                "Hourly": '',
                "Salary": '',
                "Commission": '',
                "PTO": '',
                "PTOused": '',
                "Hours/sales": '',
                "Total": '',
            }
        ])

        self.set_table_data(self.people)


    def button_action(self, event):
        button_text = event.widget.cget('text')
        button_text = button_text if button_text != "Pay rate" else "Pay amount"
        button_index = self.values_list.index(button_text)

        self.actions[button_index](button_text)

    def sort_ascending(self, key):
        print(key)

        data = self.get_table_data()
        data_copy = []

        for i in range(len(data)):
            # print(data, "\n\n####\n\n")
            if not data[i]["First name"] == '':
                data_copy.append(data[i])

        sorted_data = sorted(data_copy, key=lambda i: i[key])

        # print(sorted_data)
        self.set_table_data(sorted_data)

        self.actions[self.values_list.index(key)] = self.sort_descending


    def sort_descending(self, key):
        print(key)

        data = self.get_table_data()
        data_copy = []

        for i in range(len(data)):
            # print(data, "\n\n####\n\n")
            if not data[i]["First name"] == '':
                data_copy.append(data[i])

        sorted_data = sorted(data_copy, key=lambda i: i[key], reverse=True)

        # print(sorted_data)
        self.set_table_data(sorted_data)

        self.actions[self.values_list.index(key)] = self.sort_ascending


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

    def create_pay_modal(self, message, payroll):
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

        top.title("Payroll")

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

        # with open(self.help_content, 'r') as f:
        #     text = f.read()

        text = payroll

        text_pay = tk.Text(frames[1], font=('Roboto', 14), highlightthickness=0, yscrollcommand=text_scrollbar.set)
        text_pay.insert(tk.END, text)

        text_pay.bind("<Key>", lambda x: "break")

        text_pay.grid(row=0, sticky=tk.EW, padx=(10, 0))

        text_scrollbar.configure(command=text_pay.yview)

        button_close = ttk.Button(frames[2], text="Close", style='Header.TButton', command=top.destroy)
        button_close.grid(row=0, sticky=tk.E, padx=(0, 25))