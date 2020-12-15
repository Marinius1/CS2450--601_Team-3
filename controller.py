"""
Module contains all data agregation methods and classes for use between the model and view.
"""


import json
import os
import math
from Model.Add_Employee import add_employee
from Model.Delete_Employee import delete_employee
import Model.newFile
import Model.updateHours
import Model.EditEmployeeFile
import Model.payRoll


#Creates employee list for input into View

class List_Maker:

    def __init__(self):
        self.data = []

        with open('Model/employee_file.json') as infile:
            self.data = json.load(infile)
            infile.close()

    def reload(self):
        with open('Model/employee_file.json') as infile:
            self.data = json.load(infile)
            infile.close()



class Employee_Adder:
    def __init__(self, dicton):
        add = add_employee(dicton["Employee number"], dicton["First name"], dicton["Last name"], 
                         dicton["Pay type"], dicton["Salary"], dicton["Commission"], dicton["Hourly"],
                         dicton["Address"], dicton["State"], dicton["City"], dicton["Social security"],
                         dicton["Phone"], dicton["Zip"], dicton["Birth day"],
                         dicton["Birth month"], dicton["Birth year"], dicton["Start day"], dicton["Start month"],
                         dicton["Start year"], dicton["Role"], dicton["Position"], dicton["Team"])
        add.add_to_employee_file()


class Employee_Deleter:
    def __init__(self, dicton):
        d = delete_employee()
        d.delete_this(dicton["Employee number"], dicton["First name"], dicton["Last name"])


class Employee_Editer:
    def __init__(self, dicton1, dicton):
        d = delete_employee()
        d.delete_this(dicton1["Employee number"], dicton1["First name"], dicton1["Last name"])
        add = add_employee(dicton["Employee number"], dicton["First name"],
                         dicton["Last name"], dicton["Pay type"], dicton["Salary"], dicton["Commission"], dicton["Hourly"],
                         dicton["Address"], dicton["State"], dicton["City"], dicton["Social security"],
                         dicton["Phone"], dicton["Zip"], dicton["Birth day"],
                         dicton["Birth month"], dicton["Birth year"], dicton["Start day"], dicton["Start month"],
                         dicton["Start year"], dicton["Role"], dicton["Position"], dicton["Team"])
        add.add_to_employee_file()

class New_Pay:
    def __init__(self):
        Ex=Model.newFile.new("Model/employee_file.json")
        Ex.stupid_function()
        Wy=Model.updateHours.updateHours("Model/employee_file.json")
        Wy.setTozero()


class Import_Hourly:
    def __init__(self, file):
        FT=Model.updateHours.updateHours('Model/employee_file.json')
        FT.updateHourly(file)
        FT.updateSalary(file)

class Import_Sales:
    def __init__(self, file):
        FT=Model.updateHours.updateHours('Model/employee_file.json')
        FT.updateCommission(file)

class Save_Payroll_Shits:
    def __init__(self, lyst):
        SPS=Model.EditEmployeeFile.editThis(lyst)
        SPS.edit()


class payPay:
    def __init__(self):
        PP=Model.payRoll.payRoll("Payroll.csv")
        PP.payroll()


        

""" Controller module.
used to control information between the module and View.
Working "Main" module."""