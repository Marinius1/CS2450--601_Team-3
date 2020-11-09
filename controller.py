"""
Module contains all data agregation methods and classes for use between the model and view.
"""
import json
import os
import math
from .Model.Add_Employee import add_employee

#Creates employee list for input into View

class List_Maker:

    def __init__(self):
        self.data = []

        with open('Model/employee_file.json') as infile:
            self.data = json.load(infile)

    def reload(self):
        with open('Model/employee_file.json') as infile:
            self.data = json.load(infile)
            print(self.data)


class Employee_Adder:
    def __init__(self, dict):
        self.data = []
        self.data.append(dict["First name"], dict["Last name"],
                         dict["Pay type"], dict["Pay amount"], dict["Birth date"],
                         dict["Address"], dict["State"], dict["City"], dict["Social security"],
                         dict["Phone"], dict["Start date"], dict["Zip"], dict["Hours/sales"])

            




""" Controller module.
used to control information between the module and View.
Working "Main" module."""



"""Control user input from View to authenticator, 
when response from authenticator module
is reciever, log account type.

--Admin module
If account = admin, call view_admin.
    initiate model pipe
    load employees list into memory
    send success message to View
    call View admin_home
    initialize event listeners "admin-home-events" (sustained in View module)

--employee module
If account type == employee, 
    initiate model pipe
    if employee == user
        load employee into memory
        send success message to View
        call View employee_home
        call event listeners "home-events" (sustained in View module)

else
    issue login fail attempt to View
    call button event handler
    on response from user, restart authenticator process.
"""

"""--Admin navigation--


    -Employee management-

    pay-
        on event trigger,
        pull string input from View field
        if string
            parse input to correct data type
            call model pay method with parsed data type
            check edit (if employee pay == new employee pay then good, else bad)
            update employee list in memory
            send success to View
            send updated employee list to View

        else
            call View input error module
            restart event handler

    permissions-
    on load event;
        send employee permissions list to View
     on change event;
        pull string input from View field
        if string
            parse input to correct data type
            call updater update-permissions method with parsed data type
            check edit (if employee pay == new employee pay then good, else bad)
            update employee list in memory
            send success to View
            send updated employee list to View

        else
            call View input error module
            restart event handler

    PTO-
    on event trigger,
        pull string input from View field
        if string
            parse input to correct data type
            call model PTO method with parsed data type
            check edit (if employee pay == new employee pay then good, else bad)
            update employee list in memory
            send success to View
            send updated employee list to View

        else
            call View input error module
            restart event handler
"""

"""
--Company info--
 On load event
    open company info txt file
    send to View

-Directory
    on event trigger,
    parse employee name, emp_number, emp_phone to list of list of strings
    [["Jack", "Employeeson", "123654789", "(***) 111-2222"], ["Jill", "ManagerLady", "987654321", "(***)333-4444"]]
    for element in list,
        call row maker from View with list element as var
    

-Metrics
    Undecided on particular metrics.
    Options are total paid out per year, per quarter, per month, per 2 week period
    average expected payouts next period, average expected payouts next quarter,
    average expected payouts per month, per year.
    Number of employees
    Number of employees gained
    average No. of hours worked

"""

"""
--Employee info--
on load event
    if current user == employee in list employees
        load employee data
    else
        call View error response

-pay
    same info as metrics, but for single employee only.

-PTO
    on event trigger,
    send accrued PTO time to View
"""

"""
--Docs/Help--
    on event trigger,
    send available document choices to View
"""

'''
   admin_data = list_maker()
   print(admin_data.data)
   Admin.people_example = admin_data.data
   print(Admin.people_example)
   root = tk.Tk()
   window = Window(root)
   root.mainloop()
'''
