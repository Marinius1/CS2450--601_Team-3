import json
'''
Adds a new employee to the employee employee_file.json file.
'''
class add_employee:

    def __init__(self, first, last, type, amount, birthday, address, state, city, social, phone, start, zip, hours_sales):
        self.hours_sales = hours_sales
        self.zip = zip
        self.start = start
        self.first = first
        self.last = last
        self.type = type
        self.amount = amount
        self.birthday = birthday
        self.address = address
        self.city = city
        self.state = state
        self.social = social
        self.phone = phone

    def add_to_employee_file(self):
        data = []
        with open('employee_file.json') as infile:
            data1 = json.load(infile)
            f = open('employee_number.txt', 'r')
            line = f.readlines()
            num = line.pop(0)
            num = num.rstrip('\n')
            if len(data1) > 0:
                data1.append({"Employee number": num,"First name": self.first, "Last name": self.last, "Phone": self.phone,
                              "Address": self.address, "City": self.city, "State": self.state, "Social security": self.social,
                              "Birth date": self.birthday, "Pay type": self.type,
                              "Pay amount": self.amount,"Start date": self.start, "Zip": self.zip, "Hours/sales": self.hours_sales})
            else:
                data.append({"Employee number": num, "First name": self.first, "Last name": self.last, "Phone": self.phone,
                             "Address": self.address, "City": self.city, "State": self.state, "Social security": self.social,
                             "Birth date": self.birthday, "Pay type": self.type,
                             "Pay amount": self.amount, "Start date": self.start, "Zip": self.zip, "Hours/sales": self.hours_sales})

            with open("employee_number.txt", "w") as f1:
                for _ in line:
                    j = line.pop(0)
                    f1.write(j)

        with open('employee_file.json', 'w') as outfile:
            json.dump(data1,outfile)

first = "Isaac"
last = "Dobbins"
phone = "385-225-8880"
pay_type = "Salary"
pay_amount = "3.00"
birth_date = "06/06/1997"
address = "62 N. 50 S."
city = "Orem"
state =  "UT"
social = "385-111-3380"
start = "11/08/2019"
zip = "84058"
hours_sales = 82
a = add_employee(first, last, pay_type, pay_amount, birth_date, address, state, city, social, phone, start, zip, hours_sales)

a.add_to_employee_file()