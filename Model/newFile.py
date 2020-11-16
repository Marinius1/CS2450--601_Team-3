import json

'''
Updates employee pay info and stores.
Named the function stupid because I hate it.
'''
class new:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)


    def stupid_function(self):
        x1 = "Model/0.json"
        x2 = "Model/1.json"
        x3 = "Model/2.json"
        x4 = "Model/3.json"
        x5 = "Model/4.json"
        x6 = "Model/5.json"
        x7 = "Model/6.json"
        x8 = "Model/7.json"
        x9 = "Model/8.json"
        x10 = "Model/9.json"

        with open(x9) as f:
            d9 = json.load(f)
            with open(x10, 'w') as f1:
                json.dump(d9, f1)

        with open(x8) as f:
            d8 = json.load(f)
            with open(x9, 'w') as f1:
                json.dump(d8, f1)

        with open(x7) as f:
            d7 = json.load(f)
            with open(x8, 'w') as f1:
                json.dump(d7, f1)

        with open(x6) as f:
            d6 = json.load(f)
            with open(x7, 'w') as f1:
                json.dump(d6, f1)

        with open(x5) as f:
            d5 = json.load(f)
            with open(x6, 'w') as f1:
                json.dump(d5, f1)

        with open(x4) as f:
            d4 = json.load(f)
            with open(x5, 'w') as f1:
                json.dump(d4, f1)

        with open(x3) as f:
            d3 = json.load(f)
            with open(x4, 'w') as f1:
                json.dump(d3, f1)

        with open(x2) as f:
            d2 = json.load(f)
            with open(x3, 'w') as f1:
                json.dump(d2, f1)

        with open(x1) as f:
            d1 = json.load(f)
            with open(x2, 'w') as f1:
                json.dump(d1, f1)

        with open(x1) as f:
            d1 = json.load(f)
            for i in self.data:
                if i["Pay type"] == "Hourly":
                    z = float(i["Pay amount"]) * float(i["Hours/sales"])
                    zz = float(i["Hours/sales"]) // 8 #Hourly accrue 1 hour per 8 hours worked.
                    zzz = zz // 3 #random amount time used

                elif i["Pay type"] == "Commission":
                    z = float(i["Pay amount"]) * float(i["Hours/sales"])
                    zz = z // 100 #Commission earn an 1 for every $100
                    zzz = zz // 3  # random amount time used

                elif i["Pay type"] == "Salary":
                    z = float(i["Pay amount"]) / 12
                    zz = 25
                    zzz = zz  // 3 # random amount time used

                d1.append({"Employee number": i["Employee number"], "First name": i["First name"],
                           "Last name": i["Last name"], "Total pay": str(round(z,2)), "PTO used": str(zzz), "PTO total":str(zz)})
            with open(x1, 'w') as f:
                json.dump(d1, f)

    def edit_PTO(self, employeeId, hours_used, hours_remain, file):
        with open(file) as f:
            data1 = json.load(f)
        for i in data1:
            if i["Employee number"] == employeeId:
                z = data1.index(i)
                data1.pop(z)
                data1.append({"Employee number": i["Employee number"], "Total pay": i["Total pay"],
                              "PTO total": hours_remain, "PTO used": hours_used})
                with open(file, 'w') as outfile:
                    json.dump(data1, outfile)

#n = new("employee_file.json")
#n.stupid_function()
#'''
#n.edit_PTO(Employee ID, Hours used, hours total, file to change)
#'''