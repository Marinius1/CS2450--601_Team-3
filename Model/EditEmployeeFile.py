import json

def archive_employee(empID):
    with open("Model/employee_file.json") as file:
        data = json.load(file)
        file.close()
        for i in data:
            if empID == i["Employee number"]:
                with open('Model/deleted_employees.json') as infile:
                    data = json.load(infile)
                    data.append(i)
                    infile.close()
                with open('Model/deleted_employees.json', 'w') as outfile:
                    json.dump(data, outfile)
                    outfile.close()


def edit_employee(empID, change, info):
    with open("Model/employee_file.json") as file:
        data = json.load(file)
        for i in data:
            if empID == i["Employee number"]:
                if change == "First name":
                    i["First name"] = info
                elif change == "Last name":
                    i["Last name"] = info

                elif change == "Pay type":
                    i["Pay type"] = info
                elif change == "Hourly":
                    i["Hourly"] = info
                elif change == "Commission":
                    i["Commission"] = info
                elif change == "Salary":
                    i["Salary"] = info

                elif change == "Address":
                    i["Address"] = info
                elif change == "State":
                    i["State"] = info
                elif change == "City":
                    i["City"] = info
                elif change == "Zip":
                    i["Zip"] = info

                elif change == "Birth day":
                    i["Birth day"] = info
                elif change == "Birth month":
                    i["Birth month"] = info
                elif change == "Birth year":
                    i["Birth year"] = info
                elif change == "Social security":
                    i["Social security"] = info

                elif change == "Phone":
                    i["Phone"] = info
                elif change == "Start day":
                    i["Start day"] = info
                elif change == "Start month":
                    i["Start month"] = info
                elif change == "Start year":
                    i["Start year"] = info

                elif change == "Hours/sales":
                    i["Hours/sales"] = info
                elif change == "Role":
                    i["Role"] = info
                elif change == "Position":
                    i["Position"] = info
                elif change == "Team":
                    i["Team"] = info

                elif change == "Timecard":
                    i["Timecard"] = info
                elif change == "PTO":
                    i["PTO"] = info
                elif change == "PTOused":
                    i["PTOused"] = info
                else:
                    raise Exception("Sorry, invalid inputs.")
        with open('Model/employee_file.json', 'w') as outfile:
            json.dump(data, outfile)


class editThis:

    def __init__(self, data):
        self.data = data

    def edit(self):
        with open("Model/employee_file.json") as file:
            data = json.load(file)
            for i in self.data:
                empID = str(i["Employee number"])
                for j in data:
                    if j["Employee number"] == empID:
                        j["PTO"] = i["PTO"]
                        j["PTOused"] = i["PTOused"]
                        j["Hours/sales"] = i["Hours/sales"]

        with open("Model/employee_file.json", 'w') as f:
            json.dump(data, f)
'''
edit_employee("51-4678119", "First name", "Isaac")
archive_employee("51-4678119")
'''



