import json


'''
Delete employee from employee file.
'''

class choice:

    def __init__(self, number, first, last):
            self.number = number
            self.first = first
            self.last = last

    def delEmployee(self):
        return self.number, self.first, self.last

class delete_employee:

    def __init__(self):
        with open('Model/employee_file.json') as infile:
            self.data = json.load(infile)

    def delete_this(self, empId, first, last):
        c = choice(empId,first,last)
        for i in self.data:
            if (i['Employee number'], i['First name'], i['Last name']) == c.delEmployee():
                z = self.data.index(i)
                self.data.pop(z)

            with open('Model/employee_file.json', 'w') as outfile:
                json.dump(self.data, outfile)

        with open('Model/employee_file.json', 'w') as outfile:
            json.dump(self.data, outfile)



d = delete_employee()
d.delete_this("51-4678119", "Issie", "Scholard")

