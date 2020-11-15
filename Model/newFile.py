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
        x1 = "0.json"
        x2 = "1.json"
        x3 = "2.json"
        x4 = "3.json"
        x5 = "4.json"
        x6 = "5.json"
        x7 = "6.json"
        x8 = "7.json"
        x9 = "8.json"
        x10 = "9.json"

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
                elif i["Pay type"] == "Commission":
                    z = float(i["Pay amount"]) * float(i["Hours/sales"])
                elif i["Pay type"] == "Salary":
                    z = float(i["Pay amount"]) / 12
                d1.append({"Employee number": i["Employee number"], "Expected pay": str(z)})
            with open(x1, 'w') as f:
                json.dump(d1, f)

'''
n = new("employee_file.json")
n.stupid_function()
'''