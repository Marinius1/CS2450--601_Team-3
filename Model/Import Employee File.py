import json
import random

EMPLOYEE_FILE = "employees.csv"
lyst = []

class addToEmployeeFile:

    def __init__(self, number, first, last, type, amount, address, state, city, zip, bDay, social, pNumber, start):
        self.start = start
        self.pNumber = pNumber
        self.social = social
        self.bDay = bDay
        self.number = number
        self.first = first
        self.last = last
        self.type = type
        self.amount = amount
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def add_to_employee_file(self):
        with open('data.json') as infile:
            data1 = json.load(infile)
            data1.append(
                {"Employee number": self.number, "First name": self.first, "Last name": self.last,
                     "Address": self.address, "City": self.city, "State": self.state,
                      "Pay type": self.type, "Pay amount": self.amount, "Birth date": self.bDay,
                 "Social security": self.social, "Phone": self.pNumber, "Start date": self.start, "Zip": self.zip})


        with open('data.json', 'w') as outfile:
            json.dump(data1, outfile)


def social():
    a = random.randint(100, 999)
    b = random.randint(10, 99)
    c = random.randint(1000, 9999)
    z = str(a) + "-" + str(b) + "-" + str(c)
    return z


def birth():
    a = random.randint(1, 12)
    b = random.randint(1, 30)
    c = random.randint(1948, 1965)
    z = str(a) + "/" + str(b) + "/" + str(c)
    return z


def phone():
    a = random.randint(100,999)
    b = random.randint(100,999)
    c = random.randint(1000,9999)
    z = str(a)+"-"+str(b)+"-"+str(c)
    return z

def start_date():
    a = random.randint(1, 12)
    b = random.randint(1, 30)
    c = random.randint(1965, 2004)
    z = str(a) + "/" + str(b) + "/" + str(c)
    return z


class getData:
    def __init__(self, file):
        self.file = file

    def load_employees(self):
        with open(self.file) as empFile:
            item = empFile.readlines()
            item.pop(0)
            for emp in item:
                i = emp.rstrip().split(',')
                empId = i[0]
                firstName = i[1]
                lastName = i[2]
                address = i[3]
                city = i[4]
                state = i[5]
                empZip = i[6]
                classification = i[7]
                salary = i[8]
                commission = i[9]
                hourly = i[10]
                if classification == "3":  # hourly
                    empClass = "Hourly"
                    empClassification = (str(hourly))
                elif classification == "1":  # salary
                    empClass = "Salary"
                    empClassification = (str(salary))
                elif classification == "2":  # classification
                    empClass = "Commission"
                    empClassification = (str(commission))



                i = addToEmployeeFile(str(empId), str(firstName), str(lastName), 
                                      str(address), str(state), str(city), 
                                      str(empClass), str(empClassification), str(birth()),
                                      str(social()), str(phone()), str(start_date()), str(empZip))
                i.add_to_employee_file()


a = getData(EMPLOYEE_FILE)

a.load_employees()
