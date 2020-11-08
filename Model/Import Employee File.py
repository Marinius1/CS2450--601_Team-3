import json
import random

EMPLOYEE_FILE = "employees.csv"

class addToEmployeeFile:

    def __init__(self, number, first, last, type, amount, address, state, city, zip, bDay, social, pNumber):
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
        with open('dataFile.json') as infile:
            data1 = json.load(infile)
            data1.append(
                {"Employee number": self.number, "First name": self.first, "Last name": self.last,
                     "Address": self.address, "City": self.city, "State": self.state,
                      "Pay type": self.type, "Pay amount": self.amount})


        with open('dataFile.json', 'w') as outfile:
            json.dump(data1, outfile)


def phone():
    a = random.randint(100,999)
    b = random.randint(100,999)
    c = random.randint(1000,9999)
    return str(a)+"-"+str(b)+"-"+str(c)

def birth():
    a = random.randint(1, 12)
    b = random.randint(1, 30)
    c = random.randint(1965, 2004)
    return str(a) + "/" + str(b) + "/" + str(c)

def social():
    a = random.randint(100, 999)
    b = random.randint(10, 99)
    c = random.randint(1000, 9999)
    return str(a) + "-" + str(b) + "-" + str(c)

def load_employees():
    with open(EMPLOYEE_FILE) as empFile:
        item = empFile.readlines()
        item.pop(0)
        for emp in item:
            employeeFields = emp.rstrip().split(',')
            empId = employeeFields[0]
            firstName = employeeFields[1]
            lastName = employeeFields[2]
            address = employeeFields[3]
            city = employeeFields[4]
            state = employeeFields[5]
            empZip = employeeFields[6]
            classification = employeeFields[7]
            salary = employeeFields[8]
            commission = employeeFields[9]
            hourly = employeeFields[10]
        if classification == "3":  # hourly
            empClass = "Hourly"
            empClassification = (str(hourly))
        elif classification == "1":  # salary
            empClass = "Salary"
            empClassification = (str(salary))
        else:  # classification
            empClass = "Commission"
            empClassification = (str(commission))


        i = addToEmployeeFile(str(empId), str(firstName), str(lastName),str(empClass),str(empClassification),
                                str(address),str(state),str(city),str(empZip), str(birth()), str(social()),str(phone()))
        i.add_to_employee_file()


load_employees()