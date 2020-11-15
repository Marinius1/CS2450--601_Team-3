import json

'''
IGNORE
'''

class upcoming_pay:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)

    def upcoming_salary(self, current):
        lyst = []
        with open(current) as infile:
            data1 = json.load(infile)

        for l in data1:
            lyst.append(l["Employee number"])
        for i in self.data:
            if i["Employee number"] in lyst:
                continue
            if i["Pay type"] == "Salary":
                j = i["Pay amount"]
                month_pay = round(float(j)/12, 2)
                pto = 80
                used_pto = pto // 3
                unused_pto = pto - used_pto
                data1.append({"Employee number": i["Employee number"], "Total pay": str(month_pay),
                                "PTO total": unused_pto, "PTO used": used_pto})
                with open(current, 'w') as outfile:
                    json.dump(data1, outfile)

    def upcoming_commission(self):
        lyst = []
        with open('cur_period.json') as infile:
            data1 = json.load(infile)
        with open("timecards.json") as f:
            data2 = json.load(f)

        for l in data1:
            lyst.append(l["Employee number"])
        for i in self.data:
            if i["Employee number"] in lyst:
                continue

            if i["Pay type"] == "Commission":
                p = i["Pay amount"]
                for t in data2:
                    if t["Employee number"] == i["Employee number"]:
                        paycheck = float(p) * float(t["Sales/Hours"])
                        month_pay = round(paycheck,2)
                        pto = float(t["Sales/Hours"]) / 8
                        used_pto = pto//3
                        unused_pto = pto - used_pto
                        data1.append({"Employee number": i["Employee number"], "Commission pay": str(month_pay), "Salary pay": 100,
                                  "PTO total": unused_pto, "PTO used": used_pto})
                    with open('cur_period.json', 'w') as outfile:
                            json.dump(data1, outfile)


    def upcoming_hourly(self):
        lyst = []
        with open('cur_period.json') as infile:
            data1 = json.load(infile)
        with open("timecards.json") as f:
            data2 = json.load(f)

        for l in data1:
            lyst.append(l["Employee number"])
        for i in self.data:
            if i["Employee number"] in lyst:
                continue

            if i["Pay type"] == "Hourly":
                p = i["Pay amount"]
                for t in data2:
                    if t["Employee number"] == i["Employee number"]:
                        paycheck = float(p) * float(t["Sales/Hours"])
                        month_pay = round(paycheck, 2)
                        pto = float(t["Sales/Hours"]) / 8
                        used_pto = pto // 3
                        unused_pto = pto - used_pto
                        data1.append({"Employee number": i["Employee number"], "Total pay": str(month_pay),
                                      "PTO total": unused_pto, "PTO used": used_pto})
                    with open('cur_period.json', 'w') as outfile:
                        json.dump(data1, outfile)

    def edit_PTO(self, employeeId, hours_used, hours_remain):
        with open("cur_period.json") as f:
            data1 = json.load(f)
        for i in data1:
            if i["Employee number"] == employeeId:
                z = data1.index(i)
                data1.pop(z)
                data1.append({"Employee number": i["Employee number"], "Total pay": i["Total pay"],
                              "PTO total": hours_remain, "PTO used": hours_used})
                with open('cur_period.json', 'w') as outfile:
                    json.dump(data1, outfile)

    def archive(self, file):
        with open("prev_period.json") as arc:
            x = json.load(arc)
            with open(file, 'w') as y:
                json.dump(x, y)


a = upcoming_pay("employee_file.json")
a.upcoming_hourly()
a.upcoming_commission()
a.upcoming_salary()
