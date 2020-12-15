import json

'''
Adjusts employee time cards.
Employee info is updated in employee file so their hours or commissions will be accurate.
run setZero to set timecards back to Zero for new pay period.
'''

class updateHours:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)
            file.close()


    def updateHourly(self, file1):
        for i in self.data:
            if i["Pay type"] == "Hourly":
                p = i["Employee number"]
                with open(file1, 'r') as f:
                    for line in f:
                        strippedLine = line.strip()
                        line_list = strippedLine.split(',')
                        if line_list[0] == p:
                            total = []
                            line_list.pop(0)
                            for j in line_list:
                                total.append(float(j))
                            i["Hours/sales"] = str(sum(total))
                            i["Timecard"] = str(total)
        with open("Model/employee_file.json", 'w') as file:
            json.dump(self.data, file)
            file.close()


    def updateCommission(self, file1):
        for i in self.data:
            if i["Pay type"] == "Commission":
                p = i["Employee number"]
                with open(file1, 'r') as f:
                    for line in f:
                        strippedLine = line.strip()
                        line_list = strippedLine.split(',')
                        if line_list[0] == p:
                            total = []
                            line_list.pop(0)
                            for j in line_list:
                                total.append(float(j))
                            i["Hours/sales"] = str(sum(total))
                            i["Timecard"] = str(total)
        with open("Model/employee_file.json", 'w') as file:
            json.dump(self.data, file)
            file.close()


    def updateSalary(self, file1):
        for i in self.data:
            if i["Pay type"] == "Salary":
                p = i["Employee number"]
                with open(file1, 'r') as f:
                    for line in f:
                        strippedLine = line.strip()
                        line_list = strippedLine.split(',')
                        if line_list[0] == p:
                            total = []
                            line_list.pop(0)
                            for j in line_list:
                                total.append(float(j))
                            i["Hours/sales"] = str(sum(total))
                            i["Timecard"] = str(total)
        with open("Model/employee_file.json", 'w') as file:
            json.dump(self.data, file)
            file.close()


    def setTozero(self):
        for i in self.data:
            if i["Pay type"] == "Salary" or i["Pay type"] == "Commission" or i["Pay type"] == "Hourly":
                i["Hours/sales"] = "0"
                i["Timecard"] = "[]"
        with open("employee_file.json", 'w') as file:
            json.dump(self.data, file)
            file.close()



#u = updateHours("employee_file.json")
#u.updateHourly("timecards.csv")
#u.updateCommission("timecards.csv")
#u.updateSalary("timecards.csv")
#u.setTozero()
