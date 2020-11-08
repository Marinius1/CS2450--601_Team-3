
def import_employee_file():
    writefile = open('data.txt', 'a')
    file = str(input(("Enter file name here:")))
    with open(file, 'r') as f:
        for line in f:
            employeelist = []
            line = line.strip()
            employeelist.append(line)
            id = employeelist.pop(0)
            id = id.split(',')
            payType = id.pop(7)
            name = id.pop(0)


            if payType == '1':
                paytype = "salary"
            elif payType == '2':
                paytype = "Commission"
            elif payType == '3':
                paytype = "hourly"

            print("*Birth date should be in format mm/dd/yyyy*")
            x = str(input("Enter Birth Date:"))

            data = {"Employee number": id, "Name": name, "Birth date": x,"Pay type": paytype, "Pay amount": pay_amount()}

