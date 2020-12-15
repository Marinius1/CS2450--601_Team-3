import json

def archive_employee(empID):
    with open("Model/employee_file.json") as file:
        data = json.load(file)
        for i in data:
            if empID == i["Employee number"]:
                with open('deleted_employees.json') as infile:
                    data = json.load(infile)
                    data.append(i)
                with open('deleted_employees.json', 'w') as outfile:
                    json.dump(data, outfile)
'''
archive_employee("51-4678119")
'''



