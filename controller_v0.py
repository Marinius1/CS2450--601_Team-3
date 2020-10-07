
""" Controller module.
used to control information between the module and view.
Working "Main" module."""

"""Open view start window"""

"""Call authenticator"""

"""Control user input from view to authenticator, 
when response from authenticator module
is reciever, log account type.

--Admin module
If account = admin, call view_admin.
    initiate model pipe
    load employees list into memory
    send success message to view
    call view admin_home
    initialize event listeners "admin-home-events" (sustained in view module)

--employee module
If account type == employee, 
    initiate model pipe
    if employee == user
        load employee into memory
        send success message to view
        call view employee_home
        call event listeners "home-events" (sustained in view module)

else
    issue login fail attempt to view
    call button event handler
    on response from user, restart authenticator process.
"""

"""--Admin navigation--


    -Employee management-

    pay-
        on event trigger,
        pull string input from view field
        if string
            parse input to correct data type
            call model pay method with parsed data type
            check edit (if employee pay == new employee pay then good, else bad)
            update employee list in memory
            send success to view
            send updated employee list to view

        else
            call view input error module
            restart event handler

    permissions-
    on load event;
        send employee permissions list to view
     on change event;
        pull string input from view field
        if string
            parse input to correct data type
            call updater update-permissions method with parsed data type
            check edit (if employee pay == new employee pay then good, else bad)
            update employee list in memory
            send success to view
            send updated employee list to view

        else
            call view input error module
            restart event handler

    PTO-
    on event trigger,
        pull string input from view field
        if string
            parse input to correct data type
            call model PTO method with parsed data type
            check edit (if employee pay == new employee pay then good, else bad)
            update employee list in memory
            send success to view
            send updated employee list to view

        else
            call view input error module
            restart event handler
"""

"""
--Company info--
 On load event
    open company info txt file
    send to view

-Directory
    on event trigger,
    parse employee name, emp_number, emp_phone to list of list of strings
    [["Jack", "Employeeson", "123654789", "(***) 111-2222"], ["Jill", "ManagerLady", "987654321", "(***)333-4444"]]
    for element in list,
        call row maker from view with list element as var
    

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
        call view error response

-pay
    same info as metrics, but for single employee only.

-PTO
    on event trigger,
    send accrued PTO time to view
"""

"""
--Docs/Help--
    on event trigger,
    send available document choices to view
"""