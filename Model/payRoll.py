import json

'''
After the current employee time cards get pushed to 0.json.
uses 0.json as the end of the pay period. 1.json-9.json are archives.
Creates CSV file with payment info for each employee.
'''
class payRoll:

    def __init__(self, fyle):
        with open("Model/employee_file.json") as f:
            self.data = json.load(f)
            self.fyle = fyle

    def payroll(self):
        with open(self.fyle, 'w') as f1:
            for i in self.data:
                f1.write(i["Employee number"])
                f1.write(" ")
                f1.write(i["First name"])
                f1.write(" ")
                f1.write(i["Last name"])
                f1.write(" ")
                f1.write("Pay for this period:")
                if i["Pay type"] == "Hourly":
                    f1.write(str(round(float(i["Hourly"])*sum(float(i["Timecard"])),2)))
                elif i["Pay type"] == "Salary":
                    f1.write(str(round(float(i["Salary"])/2,2)))
                elif i["Pay type"] == "Commission":
                    f1.write(str(round(float((float(i["Commission"])*sum(float(i["Timecards"])/100) + float(i["Salary"])/24)))))
#                z = float(i["PTO total"]) - float(i["PTO used"])
#                f1.write(" ")
#                f1.write("Remaining PTO:")
#                f1.write(str(round(z, 2)))
                f1.write(',\n')



#p = payRoll()
#p.payroll("payroll.csv")
