import json


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


