import json
import random

class timeCards:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)

    def create_time_card(self, salary, sales_hours):
        lyst = []
        with open("timecards.json") as f:
            data1 = json.load(f)
            if len(data1) == 0:
                data1 = []
            else:
                pass

        if len(data1) > 1:
            for l in data1:
                lyst.append(l["Employee number"])
        else:
            pass

        for i in self.data:
            if i["Employee number"] in lyst:
                continue
            if i["Pay type"] == "Commission" or i["Pay type"] == "Hourly" or i["Pay type"] == "Salary":
                if i["Pay type"] == "Commission":
                    month = salary//2
                    data1.append({"Employee number": i["Employee number"],"Salary":month, "Sales/Hours": sales_hours})
                    with open('timecards.json', 'w') as outfile:
                            json.dump(data1, outfile)
                else:
                    data1.append({"Employee number": i["Employee number"], "Sales/Hours": sales_hours})
                    with open('timecards.json', 'w') as outfile:
                        json.dump(data1, outfile)


    def edit_time_card(self, employeeId, hours_sales):
        with open("timecards.json") as f:
            data1 = json.load(f)
        for i in data1:
            if i["Employee number"] == employeeId:
                z = data1.index(i)
                data1.pop(z)
                data1.append({"Employee number": i["Employee number"], "Sales/Hours": hours_sales})
                with open('timecards.json', 'w') as outfile:
                    json.dump(data1, outfile)


t = timeCards("employee_file.json")
#t.edit_time_card("47-2771794", 50)
