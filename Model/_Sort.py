import json

'''
Can sort the employees file by first name, last name, employee number, pay type, pay amount, and birth date.
It can sort in both ascending and descending order.
'''
class _sort:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)

    def a_first_name_sort(self):
        d = sorted(self.data, key=lambda i: i["First name"])
        return d

    def a_last_name_sort(self):
        d = sorted(self.data, key=lambda i: i["Last name"])
        return d

    def a_employee_number_sort(self):
        d = sorted(self.data, key=lambda i: i["Employee number"])
        return d

    def a_pay_type_sort(self):
        d = sorted(self.data, key=lambda i: i["Pay type"])
        return d

    def a_pay_amount_sort(self):
        d = sorted(self.data, key=lambda i: i["Pay amount"])
        return d

    def d_first_name_sort(self):
        d = sorted(self.data, key=lambda i: i["First name"], reverse=True)
        return d

    def d_last_name_sort(self):
        d = sorted(self.data, key=lambda i: i["Last name"], reverse=True)
        return d

    def d_employee_number_sort(self):
        d = sorted(self.data, key=lambda i: i["Employee number"], reverse=True)
        return d

    def d_pay_type_sort(self):
        d = sorted(self.data, key=lambda i: i["Pay type"], reverse=True)
        return d

    def d_pay_amount_sort(self):
        d = sorted(self.data, key=lambda i: i["Pay amount"], reverse=True)
        return d

s = _sort("employee_file.json")


for i in s.a_first_name_sort():
    print (i["First name"], i["Last name"])
