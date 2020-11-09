import json


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

class upcoming_pay:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)

    def upcoming_salary(self):
        with open('this_pay_period.json') as infile:
            data1 = json.load(infile)
        for i in self.data:
            if i["Pay type"] == "Salary":
                j = i["Pay amount"]
                month_pay = round(float(j)/12, 2)
                pto = 80
                used_pto = pto // 3
                unused_pto = pto - used_pto
                data1.append({"Employee number": i["Employee number"], "Total pay": str(month_pay), "PTO unused": unused_pto, "PTO used": used_pto})
                with open('this_pay_period.json', 'w') as outfile:
                    json.dump(data1, outfile)

    def upcoming_commission(self):
        with open('this_pay_period.json') as infile:
            data1 = json.load(infile)
        for i in self.data:
            if i["Pay type"] == "Commission":
                p = i["Pay amount"]
                t = i["Hours/sales"]
                paycheck = float(p) * float(t)
                month_pay = round(paycheck,2)
                pto = float(t) / 8
                used_pto = pto//3
                unused_pto = pto - used_pto
                data1.append({"Employee number": i["Employee number"], "Total pay": str(month_pay), "PTO unused": unused_pto, "PTO used": used_pto})
                with open('this_pay_period.json', 'w') as outfile:
                    json.dump(data1, outfile)


    def upcoming_hourly(self):
        with open('this_pay_period.json') as infile:
            data1 = json.load(infile)
        for i in self.data:
            if i["Pay type"] == "Hourly":
                p = i["Pay amount"]
                t = i["Hours/sales"]
                paycheck = float(t) * float(p)
                month_pay = round(paycheck, 2)
                pto = float(t)/8
                used_pto = pto//3
                unused_pto = pto - used_pto
                data1.append({"Employee number": i["Employee number"], "Total pay": str(month_pay), "PTO unused": unused_pto, "PTO used": used_pto})
                with open('this_pay_period.json', 'w') as outfile:
                    json.dump(data1, outfile)


a = upcoming_pay("employee_file.json")
a.upcoming_salary()
a.upcoming_commission()
a.upcoming_hourly()