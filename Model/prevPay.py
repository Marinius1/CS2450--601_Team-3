import json
import random

class previous_month_pay:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)

    def month_hourly(self):
        with open('last_pay_period.json') as infile:
            data1 = json.load(infile)
        for i in self.data:
            if i["Pay type"] == "Hourly":
                p = i["Employee number"]
                with open('timecards.csv','r') as f:
                    for line in f:
                        strippedLine = line.strip()
                        line_list = strippedLine.split(',')
                        if line_list[0] == p:
                            total = []
                            line_list.pop(0)
                            for j in line_list:
                                z = float(j) * float(i["Pay amount"])
                                total.append(z)
                            totalT = round(sum(total), 2)

                            data1.append({"Employee number":i["Employee number"], "Total pay": str(totalT)})
            with open('last_pay_period.json', 'w') as outfile:
                json.dump(data1, outfile)

    def month_commission(self):
        with open('last_pay_period.json') as infile:
            data1 = json.load(infile)
        for i in self.data:
            if i["Pay type"] == "Commission":
                p = i["Employee number"]
                with open('receipts.csv','r') as f:
                    for line in f:
                        strippedLine = line.strip()
                        line_list = strippedLine.split(',')
                        if line_list[0] == p:
                            line_list.pop(0)
                            this_list = [float(k) for k in line_list]

                            totalT = round(sum(this_list),2)
                            data1.append({"Employee number": i["Employee number"], "Total pay": str(totalT)})
                            with open('last_pay_period.json', 'w') as outfile:
                                json.dump(data1, outfile)

    def month_salary(self):
        with open('last_pay_period.json') as infile:
            data1 = json.load(infile)
        for i in self.data:
            if i["Pay type"] == "Salary":
                j = i["Pay amount"]
                month_pay = round(float(j)/12, 2)
                data1.append({"Employee number": i["Employee number"], "Total pay": str(month_pay)})
                with open('last_pay_period.json', 'w') as outfile:
                    json.dump(data1, outfile)
