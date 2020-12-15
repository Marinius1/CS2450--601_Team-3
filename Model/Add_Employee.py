import json
import random

'''
Adds a new employee to the employee employee_file.json file.
Also checks to make sure that the employee doesn't already exist.
'''
class add_employee:

    def __init__(self, eNum, first, last, type, amount, address, state, city, social, phone, zip,
                 bDay, bMonth, bYear, sDay, sMonth, sYear, role, pos, team, timecard, PTO, PTOused):
        self.PTO = PTO
        self.PTOused = PTOused
        self.timecard = timecard
        self.role = role
        self.pos = pos
        self.team = team
        self.eNum = eNum
        self.zip = zip
        self.first = first
        self.last = last
        self.type = type
        self.amount = amount
        self.address = address
        self.city = city
        self.state = state
        self.social = social
        self.phone = phone
        self.bDay = bDay
        self.bMonth = bMonth
        self.bYear = bYear
        self.sDay = sDay
        self.sMonth = sMonth
        self.sYear = sYear


    def add_to_employee_file(self):
        data = []
        j = True
        with open('employee_file.json') as infile:
            data1 = json.load(infile)

            for i in data1:
                if self.eNum == i['Employee number'] and self.first == i["First name"] and self.last == i["Last name"]:
                    raise Exception("Sorry, employee already exists.")

            if j == True:

                if len(data1) > 0:
                    data1.append({"Employee number": self.eNum,"First name": self.first, "Last name": self.last, "Phone": self.phone,
                                          "Address": self.address, "City": self.city, "State": self.state, "Social security": self.social,
                                          "Birth day": self.bDay, "Birth month": self.bMonth, "Birth year": self.bYear, "Pay type": self.type,
                                          "Pay amount": self.amount,"Start day": self.sDay, "Start month": self.sMonth, "Start year": self.sYear ,
                                          "Zip": self.zip, "Role": self.role, "Position": self.pos, "Team": self.team,
                                         "Timecard": self.timecard, "PTO": self.PTO, "PTOused": self.PTOused})
                    with open('employee_file.json', 'w') as outfile:
                        json.dump(data1, outfile)

                else:
                    data.append({"Employee number": self.eNum,"First name": self.first, "Last name": self.last, "Phone": self.phone,
                                          "Address": self.address, "City": self.city, "State": self.state, "Social security": self.social,
                                          "Birth day": self.bDay, "Birth month": self.bMonth, "Birth year": self.bYear, "Pay type": self.type,
                                          "Pay amount": self.amount,"Start day": self.sDay, "Start month": self.sMonth, "Start year": self.sYear ,
                                          "Zip": self.zip, "Role": self.role, "Position": self.pos, "Team": self.team,
                                          "Timecard": self.timecard, "PTO": self.PTO, "PTOused": self.PTOused})
                    with open('employee_file.json', 'w') as outfile:
                        json.dump(data, outfile)

            elif j == False:
                pass




'''
employee_num = "55-555555"
first = "Sean"
last = "McNees"
phone = "385-225-8880"
pay_type = "Salary"
pay_amount = "3.00"
birth_day = "06"
birth_month = "10"
birth_year = "1990"
address = "62 N. 50 S."
city = "Orem"
state =  "UT"
social = "385-11-3380"
start_day = "11"
start_month = "11"
start_year = "2011"
zzip = "84058"
role = "Worker"
teams = "Team 1"
position = "Warehouse"
timecard = str([24,32,96])
PTO = str(random.randint(2, 10))
PTOused =  str(random.randint(0,2))

# a = add_employee(employee_num, first, last, pay_type, pay_amount, address,state, city, social,
#                  phone, zzip, birth_day, birth_month, birth_year, start_day, start_month,
#                  start_year, role, position, teams, timecard,PTO, PTOused)
#
# a.add_to_employee_file()
'''