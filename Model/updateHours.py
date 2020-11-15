import json

'''
Adjusts employee time cards.
Employee info is updated in employee file so their hours or commissions will be accurate.
'''

class updateHours:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)

    def updateHourly(self, fileCSV):
        for i in self.data:
            if i["Pay type"] == "Hourly":
                p = i["Employee number"]
                with open(fileCSV, 'r') as f:
                    for line in f:
                        strippedLine = line.strip()
                        line_list = strippedLine.split(',')
                        if line_list[0] == p:
                            total = []
                            line_list.pop(0)
                            for j in line_list:
                                total.append(float(j))
                            i["Hours/sales"] = str(sum(total))
        with open("employee_file.json", 'w') as file:
            json.dump(self.data, file)


    def updateCommission(self, fileCSV):
        for i in self.data:
            if i["Pay type"] == "Commission":
                p = i["Employee number"]
                with open(fileCSV, 'r') as f:
                    for line in f:
                        strippedLine = line.strip()
                        line_list = strippedLine.split(',')
                        if line_list[0] == p:
                            total = []
                            line_list.pop(0)
                            for j in line_list:
                                total.append(float(j))
                            i["Hours/sales"] = str(sum(total))

    def updateSalary(self, fileCSV):
        for i in self.data:
            if i["Pay type"] == "Salary":
                p = i["Employee number"]
                with open(fileCSV, 'r') as f:
                    for line in f:
                        strippedLine = line.strip()
                        line_list = strippedLine.split(',')
                        if line_list[0] == p:
                            total = []
                            line_list.pop(0)
                            for j in line_list:
                                total.append(float(j))
                            i["Hours/sales"] = str(sum(total))

'''
u = updateHours("employee_file.json")
u.updateHourly("timecards.csv")
'''