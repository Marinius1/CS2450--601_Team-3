import json
import random


class CreateTimecards:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)


    def randInputs(self):
        with open("TimeCards.csv",'w') as f:
            for i in self.data:
                f.write(str(i["Employee number"]))
                f.write(",")
                f.write(str(random.randint(2,12)))
                f.write(",")
                f.write(str(random.randint(2, 12)))
                f.write(",")
                f.write(str(random.randint(2, 12)))
                f.write(",")
                f.write(str(random.randint(2, 12)))
                f.write(",")
                f.write(str(random.randint(2, 12)))
                f.write('\n')


c = CreateTimecards("employee_file.json")
c.randInputs()
