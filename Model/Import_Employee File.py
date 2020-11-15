import json
import random

'''
Imports a list of employees from csv file
'''
EMPLOYEE_FILE = "employees.csv"
lyst = []

class addToEmployeeFile:

    def __init__(self, number, first, last, type, amount, address, state,
                 city, zip, bDay, bMonth, bYear, social, pNumber, sDay, sMonth, sYear,
                 hours_sales, role, pos, team):
        self.pos = pos
        self.team = team
        self.role = role
        self.hours_sales = hours_sales
        self.sDay = sDay
        self.sMonth = sMonth
        self.sYear = sYear
        self.pNumber = pNumber
        self.social = social
        self.bDay = bDay
        self.bMonth = bMonth
        self.bYear = bYear
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
        with open('employee_file.json') as infile:
            data1 = json.load(infile)
            data1.append(
                {"Employee number": self.number, "First name": self.first,
                 "Last name": self.last,"Pay type": self.type, "Pay amount": self.amount,
                     "Address": self.address, "State": self.state, "City": self.city, "Zip": self.zip,
                       "Birth day": self.bDay, "Birth month": self.bMonth, "Birth year": self.bYear,
                 "Social security": self.social, "Phone": self.pNumber, "Start day": self.sDay,
                 "Start month": self.sMonth, "Start year": self.sYear, "Hours/sales": self.hours_sales,
                 "Role": self.role, "Position": self.pos, "Team": self.team})


        with open('employee_file.json', 'w') as outfile:
            json.dump(data1, outfile)


def social():
    a = random.randint(100, 999)
    b = random.randint(10, 99)
    c = random.randint(1000, 9999)
    zz = str(a) + "-" + str(b) + "-" + str(c)
    return zz


def phone():
    a = random.randint(100,999)
    b = random.randint(100,999)
    c = random.randint(1000,9999)
    z = str(a)+"-"+str(b)+"-"+str(c)
    return z

def position():
    global z
    x = random.randint(1,3)
    if x == 1:
        z = "Warehouse"
    elif x == 2:
        z = "Office"
    elif x == 3:
        z = "Corporate"
    return z

def role():
    global z
    x = random.randint(1, 3)
    if x == 1:
        z = "Worker"
    elif x == 2:
        z = "Team lead"
    elif x == 3:
        z = "Manager"
    return z

def teams():
    global y
    x = random.randint(1, 4)
    if x == 1:
        y = "Team 1"
    elif x == 2:
        y = "Team 2"
    elif x == 3:
        y = "Team 3"
    elif x == 4:
        y = "Team 4"
    return y

class getData:
    def __init__(self, file):
        self.file = file

    def load_employees(self):
        with open(self.file) as empFile:
            item = empFile.readlines()
            item.pop(0)
            for emp in item:
                day1 = random.randint(1, 28)
                month1 = random.randint(1, 12)
                year1 = random.randint(1965, 2004)

                day2 = random.randint(1, 28)
                month2 = random.randint(1, 12)
                year2 = random.randint(1965, 2004)

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
                    hours_sales = random .randint(0, 160)
                elif classification == "1":  # salary
                    empClass = "Salary"
                    empClassification = (str(salary))
                    hours_sales = None
                elif classification == "2":  # classification
                    empClass = "Commission"
                    empClassification = (str(commission))
                    hours_sales = random.randint(0, 160)

                i = addToEmployeeFile(str(empId), str(firstName), str(lastName), str(empClass), str(empClassification),
                                      str(address), str(state),str(city), str(empZip), str(day1), str(month1), str(year1), str(social()),
                                      str(phone()),str(day2), str(month2), str(year2),str(hours_sales),str(role()),str(position()),str(teams()))
                i.add_to_employee_file()


a = getData(EMPLOYEE_FILE)

a.load_employees()
