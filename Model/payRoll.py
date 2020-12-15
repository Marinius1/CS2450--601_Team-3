import json

'''
After the current employee time cards get pushed to 0.json.
uses 0.json as the end of the pay period. 1.json-9.json are archives.
Creates CSV file with payment info for each employee.
'''
class payRoll:

    def __init__(self):
        with open("Model/employee_file.json") as f:
            self.data = json.load(f)

    def payroll(self, fyle):
        with open(fyle, 'w') as f1:
            for i in self.data:
                f1.write(i["Employee number"])
                f1.write(" ")
                f1.write(i["First name"])
                f1.write(" ")
                f1.write(i["Last name"])
                f1.write(" ")
                f1.write("Pay for this period:")
                k = i["Timecard"].strip('][').split(', ')
                r = [float(ele) for ele in k]
                hours = (sum(r))

                if i["Pay type"] == "Hourly":
                    f1.write(str(round(float(i["Hourly"])*hours,2)))
                elif i["Pay type"] == "Salary":
                    f1.write(str(round(float(i["Salary"])/2,2)))
                elif i["Pay type"] == "Commission":
                    f1.write(str(round((float(i["Commission"]) * (hours/100)) + float(i["Salary"])/24,2)))
                f1.write('\n')



'''
p = payRoll()
p.payroll("payroll.csv")
'''