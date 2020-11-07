"""Model Module To communicate with control, and get data to display for the View."""

"""---Import employee file class"""
"""
If admin would like to add a file of employees, to the main employee file.
Main employee file will be Binary JSON To save on space, and help protect information.
Parse file and determine personal information, pay type, and hours. To help track pay, PTO, and personal information.
If employee already exists, ask to create duplicate or replace the employee.
If employee has same name, ensures that employee number is different
"""

"""---Add employee class"""
'''Aggregation of Import employee file class'''
"""
Add a single employee into the main employee file, 
create a temporary csv file formatted with correct information that is then fed through our Import employee file class
"""

"""---Employee Profile class"""
'''Composition of Import employee file class'''
"""
Search employee file for specific employee, by name or employee number.
If employee exists --- display employee information in GUI.
If user is admin display all information.
Else->display limited information
"""

"""---Employee list class"""
"""
Display scrollable list of employees; including their names, and employee numbers.
Default list will be sorted alphabetically.
List will be clickable and will take the user to that employee’s profile
"""

"""---Employee list sort class"""
'''Aggregation of Employee list class'''
"""
Search and sort functions to narrow and find specific employees.
Sort by name alphabetically or reverse alphabetically.
Sort by employee number
Sort by position
Sort by pay type
Sort by hire date
Sort by birth date
"""

"""---Paid time off class"""
'''Composition of Employee list class'''
'''Aggregation of Upcoming pay class'''
"""
Find specific employee in employee file, read their hours, and calculate paid time off accrued.
This is based on hours worked and will be standardized for employees, based on their position.
"""

"""---Upcoming pay class"""
'''Composition of Employee list class'''
'''Aggregation of Paid time off class'''
"""
Calculates the estimated pay of the user’s next check based on hours worked, 
but have yet to be paid. Based on hours worked stored in employee file
"""
