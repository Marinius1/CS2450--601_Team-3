import json

class editThis:

    def __init__(self,empID):
        self.empID = empID

    def edit(self):
        with open("employee_file.json") as file:
            data = json.load(file)
            for i in data:
                if i["Employee number"] == self.empID:
                    with open("timecards.csv") as infile:
                        for line in infile:
                            strippedLine = line.strip()
                            line_list = strippedLine.split(',')
                            if line_list[0] == self.empID:
                                total = []
                                line_list.pop(0)
                                for j in line_list:
                                    total.append(float(j))
                        if i["Timecard"] != str(total):
                            i["Timecard"] = str(total)
                        elif i["Hours/sales"] != str(sum(total)):
                            i["Hours/sales"] = str(sum(total))
                        elif i["PTO"] != str(round(sum(total),2)//8):
                            i["PTO"] = str(round(sum(total),2)//8)

        with open("employee_file.json", 'w') as f:
            json.dump(data, f)

'''
e = editThis("51-4678119")
e.edit()
'''