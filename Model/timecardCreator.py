import json
import random


class CreateTimecards:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)


    def randInputs(self):
        with open("TimeCards.csv",'r') as f:
            for i in self.data:
                f.write(i["Employee number"])
                f.write()