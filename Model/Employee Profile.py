import json

with open('data.json') as file:
    data = json.load(file)
x = str(input("Enter name of employee:"))


def admin_view():
    for i in data:
        if i["First name"] == x:
            print(i["Employee number"],i["First name"], i["Pay amount"], i["Social security"])

def view():
    for i in data:
        if i["First name"] == x:
            print(i["Employee number"],i["First name"])


view()
admin_view()