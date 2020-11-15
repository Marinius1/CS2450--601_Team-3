
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pynput.mouse import Listener

from .Colors.color import Color

import random


class PayRoll():
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


        self.home_frame = tk.Frame(self.master)
        self.home_frame.configure(background=self.colors.background, border=3, relief=tk.RIDGE)
        self.home_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.home_frame.rowconfigure(0, weight=1)
        self.home_frame.rowconfigure(1, weight=1)

        self.home_frame.columnconfigure(0, weight=0)
        self.home_frame.columnconfigure(1, weight=1)

        self.left_frame = tk.Frame(self.home_frame, background=self.colors.background)
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
        self.search_value.trace("w", lambda x: print(*x))
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

        self.table_frame = tk.Frame(self.left_frame, background=self.colors.background)
        self.table_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.table_frame.rowconfigure(1, weight=1)
        self.table_frame.columnconfigure(0, weight=1)

        self.data_columns = []
        self.scrollbar = tk.Scrollbar(self.table_frame)
        headers_example = ['First name', 'Last name', 'Employee ID', 'Pay Type', 'Hours Worked', 'Expected Pay', 'PTO accumulated', 'PTO  used']

        model_example = [
            [random.randint(25,50) for i in range(100)],
            [random.randint(25,50) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)],
            [random.randint(0,3000) for i in range(100)]
        ]

        self.create_table(self.table_frame, headers_example, model_example)

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
        self.right_buttons.columnconfigure(0, weight=1)

        self.save_button = ttk.Button(self.right_buttons, text='Save', style='Header.TButton')
        self.save_button.grid(row=0, column=1, sticky=tk.NE, padx=10, pady=10)

        self.new_period_button = ttk.Button(self.right_buttons, text='New Pay Period', style='Header.TButton', command=self.create_pay_period)
        self.new_period_button.grid(row=0, column=0, sticky=tk.NW, padx=10, pady=10)

        self.import_time_button = ttk.Button(self.right_buttons, text='Import Timecards', style='Header.TButton', command=self.import_file)
        self.import_time_button.grid(row=1, sticky=tk.NSEW, padx=10, pady=10, columnspan=2)

        self.import_reciept_button = ttk.Button(self.right_buttons, text='Import Reciepts', style='Header.TButton', command=self.import_file)
        self.import_reciept_button.grid(row=2, sticky=tk.NSEW, padx=10, pady=10, columnspan=2)

        self.metrics_frame = tk.Frame(self.right_frame, background=self.colors.background)
        self.metrics_frame.grid(row=1, column=0, sticky=tk.EW)

        self.metrics_frame.rowconfigure((0,1,2,3,4), weight=0)
        self.metrics_frame.columnconfigure(0, weight=1)

        self.metrics_title = tk.Label(self.metrics_frame, text="Metrics", font=('Roboto', 24, 'bold'))
        self.metrics_title.grid(row=0, sticky=tk.W)

        self.expected_payout_label = tk.Label(self.metrics_frame, text="Expected payout: ", font=('Roboto', 22))
        self.expected_payout_label.grid(row=1, sticky=tk.W)

        self.expected_payout_data = tk.StringVar()
        self.expected_payout_data.set("$10,000")
        self.expected_payout_display = tk.Label(self.metrics_frame, textvariable=self.expected_payout_data, font=('Roboto', 22))
        self.expected_payout_display.grid(row=1, column=1, sticky=tk.W)

        self.last_payout_label= tk.Label(self.metrics_frame, text="Last payout:", font=('Roboto', 22))
        self.last_payout_label.grid(row=2, sticky=tk.W)

        self.last_payout_data = tk.StringVar()
        self.last_payout_data.set("$10,000")
        self.expected_payout_display = tk.Label(self.metrics_frame, textvariable=self.last_payout_data, font=('Roboto', 22))
        self.expected_payout_display.grid(row=2, column=1, sticky=tk.W)

        self.pay_frame = tk.Frame(self.right_frame, background=self.colors.background)
        self.pay_frame.grid(row=2, column=0, sticky=tk.EW)

        self.pay_frame.rowconfigure(0, weight=1)
        self.pay_frame.columnconfigure(0, weight=1)

        self.pay_button = ttk.Button(self.pay_frame, text='Pay', style='Header.TButton')
        self.pay_button.grid(row=0, column=0, sticky=tk.EW+tk.N, padx=10, pady=10)

        self.get_table_data()

      
    def create_pay_period(self):
        pass

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
        amount = self.current_payroll[2].cget("text")
        print(amount)

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

    def get_table_data(self):

        staged_data = []

        for i in self.data_columns:
            staged_data.append(i.get(0, tk.END))

        rotated_data = list(zip(*staged_data))

        data = []

        for i in rotated_data:
            data.append({
                "First name": i[0],
                "Last name": i[1],
                "Employee number": i[2],
                "Pay type": i[3],
                "Hours worked": i[4],
                "Pay amount": i[5],
                "PTO total": i[6],
                "PTO used": i[7]
            })

        print(data)
        self.set_table_data(data)
        return data


    def set_table_data(self, data):

        staged_data = []

        for i in data:
            tmp_list = []
            tmp_list.append(i["First name"])
            tmp_list.append(i["Last name"])
            tmp_list.append(i["Employee number"])
            tmp_list.append(i["Pay type"])
            tmp_list.append(i["Hours worked"])
            tmp_list.append(i["Pay amount"])
            tmp_list.append(i["PTO total"])
            tmp_list.append(i["PTO used"])
            staged_data.append(tmp_list)

        new_data = list(zip(*staged_data))

        for i in self.data_columns:
            i.delete(0, tk.END)
            for j in range(len(new_data[self.data_columns.index(i)])):
                i.insert(tk.END, new_data[self.data_columns.index(i)][j])

                if j % 2 == 0:
                    background = self.colors.background
                else:
                    background = self.colors.a7

                i.itemconfigure(j, background=background)


    def create_table(self, master, lyst1, lyst2):

        lyst1_size = len(lyst1)

        for i in range(lyst1_size):

            master.columnconfigure(i, weight=0)

            grid_frame = tk.Frame(master, background=self.colors.background)
            grid_frame.grid(row=0, column=i, rowspan=2, sticky=tk.NS)

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
                                yscrollcommand=self.sync_yview,
                                font=('Roboto', 16),
                                width=19)
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



    def on_click(self, x, y, button, pressed):
        # print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        if not pressed:
            # Stop listener
            width = self.home_frame.winfo_width()
            # print(int(width))
            for i in self.data_columns:
                i.configure(font=('Roboto', int(width * .01)), width=int(width * .01))

            self.can_listen = False
            self.listener.stop()
            self.listener = None

            return False

    def import_file(self):
        file_name = filedialog.askopenfilename(initialdir="/",
                                               title="Select file",
                                               filetypes=(("CSV Files", "*.csv"),)
                                               )
        print(file_name)
