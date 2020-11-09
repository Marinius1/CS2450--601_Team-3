import json


class choice:

    def __init__(self, number, first, last):
            self.number = number
            self.first = first
            self.last = last

    def delEmployee(self):
        return self.number, self.first, self.last

class delete_employee:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)

    def delete_this(self):
        #Need to get input from GUI to find the employee to delete
        c = choice('68-9609244','Jed','Netti')
        for i in self.data:
            if (i['Employee number'], i['First name'], i['Last name']) == c.delEmployee():
                z = self.data.index(i)
                self.data.pop(z)

        with open('employee_file.json', 'w') as outfile:
            json.dump(self.data, outfile)


d = delete_employee("employee_file.json")

d.delete_this()
