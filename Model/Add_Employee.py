import json
'''
Adds a new employee to the employee employee_file.json file.
'''
class add_employee:

    def __init__(self, eNum, first, last, type, amount, address, state, city, social, phone, zip,
                 bDay, bMonth, bYear, sDay, sMonth, sYear, role, pos, team):
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
        with open('./Model/employee_file.json') as infile:
            data1 = json.load(infile)
            if len(data1) > 0:
                data1.append({"Employee number": self.eNum,"First name": self.first, "Last name": self.last, "Phone": self.phone,
                              "Address": self.address, "City": self.city, "State": self.state, "Social security": self.social,
                              "Birth day": self.bDay, "Birth month": self.bMonth, "Birth year": self.bYear, "Pay type": self.type,
                              "Pay amount": self.amount,"Start day": self.sDay, "Start month": self.sMonth, "Start year": self.sYear ,
                              "Zip": self.zip, "Role": self.role, "Position": self.pos, "Team": self.team})
            else:
                data.append({"Employee number": self.eNum,"First name": self.first, "Last name": self.last, "Phone": self.phone,
                              "Address": self.address, "City": self.city, "State": self.state, "Social security": self.social,
                              "Birth day": self.bDay, "Birth month": self.bMonth, "Birth year": self.bYear, "Pay type": self.type,
                              "Pay amount": self.amount,"Start day": self.sDay, "Start month": self.sMonth, "Start year": self.sYear ,
                              "Zip": self.zip, "Role": self.role, "Position": self.pos, "Team": self.team})


        with open('./Model/employee_file.json', 'w') as outfile:
            json.dump(data1,outfile)
'''
employee_num = "646-1234567"
first = "Isaac"
last = "Dobbins"
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
a = add_employee(employee_num, first, last, pay_type, pay_amount, address,state, city, social,
                 phone, zzip, birth_day, birth_month, birth_year, start_day, start_month, start_year, role, position, teams)

a.add_to_employee_file()
'''