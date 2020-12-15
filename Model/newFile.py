import json
import os

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
            os.remove(x10)
            with open(x10, 'w') as f3:
                json.dump(d9, f3)

        with open(x8) as f:
            d8 = json.load(f)
            os.remove(x9)
            with open(x9, 'w') as f3:
                json.dump(d8, f3)

        with open(x7) as f:
            d7 = json.load(f)
            os.remove(x8)
            with open(x8, 'w') as f3:
                json.dump(d7, f3)

        with open(x6) as f:
            d6 = json.load(f)
            os.remove(x7)
            with open(x7, 'w') as f3:
                json.dump(d6, f3)

        with open(x5) as f:
            d5 = json.load(f)
            os.remove(x6)
            with open(x6, 'w') as f3:
                json.dump(d5, f3)

        with open(x4) as f:
            d4 = json.load(f)
            os.remove(x5)
            with open(x5, 'w') as f3:
                json.dump(d4, f3)

        with open(x3) as f:
            d3 = json.load(f)
            os.remove(x4)
            with open(x4, 'w') as f3:
                json.dump(d3, f3)

        with open(x2) as f:
            d2 = json.load(f)
            os.remove(x3)
            with open(x3, 'w') as f3:
                json.dump(d2, f3)


        with open(x1) as f:
            d1 = json.load(f)
            os.remove(x2)
            with open(x2, 'w') as f3:
                json.dump(d1, f3)

        os.remove(x1)
        d = []
        for i in self.data:
            if i["Pay type"] == "Hourly":
                hrly = i["Hourly"]
                if hrly == "None":
                    hrly = 0
                hrsls = i['Hours/sales']
                if hrsls == "None":
                    hrsls = 0
                if hrsls == "":
                    hrsls = 0
                z = float(hrly) * float(hrsls)

            elif i["Pay type"] == "Commission":
                slry = i["Salary"]
                if slry == "None":
                    slry = 0
                hrsls = i['Hours/sales']
                if hrsls == "None":
                    hrsls = 0
                cmmsn = i["Commission"]
                if cmmsn == "None":
                    cmmsn = 0
                if cmmsn == "":
                    cmmsn = 0
                z = ((float(slry)/24) +  ((float(hrsls)) * (int(cmmsn)/100)))

            elif i["Pay type"] == "Salary":
                slry = i["Salary"]
                if slry == "None":
                    slry = 0
                z = float(slry) / 24

            d.append({"Employee number": i["Employee number"], "First name": i["First name"],
                           "Last name": i["Last name"], "Total pay": str(round(z,2))})
        with open(x1, 'w') as f:
            json.dump(d, f)

    def edit_PTO(self, employeeId, hours_used, hours_remain):
        for i in self.data:
            if i["Employee number"] == employeeId:
                i["PTO"] = hours_remain
                i["PTOused"] = hours_used

        with open("Model/employee_file.json", 'w') as outfile:
            json.dump(self.data, outfile)



#n = new("employee_file.json")
#n.edit_PTO("55-555555", '3', '3')
#n.stupid_function()
