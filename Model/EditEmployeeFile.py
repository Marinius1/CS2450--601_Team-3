import json

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
                        j["PTO total"] = i["PTO total"]
                        j["PTO used"] = i["PTO used"]
                        j["Hours/sales"] = i["Hours/sales"]

        with open("Model/employee_file.json", 'w') as f:
            json.dump(data, f)


'''
e = editThis("51-4678119")
e.edit()
'''