import random


with open('employee_number.txt', 'w') as outfile:
    second = random.sample(range(100000, 999999), 899999)
    for _ in range(899999):
        first = random.randint(10, 99)
        employee_number = str(str(first) + "-" + str(second.pop(0)))
        outfile.write(employee_number)
        outfile.write("\n")

