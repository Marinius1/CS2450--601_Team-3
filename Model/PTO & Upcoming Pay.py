import json

class time_commissions:

    def __init__(self, filename):
        self.filename = filename
        with open(filename) as file:
            self.data = json.load(file)

    def hourly(self):
        with open('dataFile.json') as infile:
            data1 = json.load(infile)
        total_pay = []
        for i in self.data:
            if i["Pay type"] == "Hourly":
                print("hello")

                p = i["Employee number"]
                with open('timecards.csv','r') as f:
                    for item in f:
                        item.rstrip().split(',')
                        if item[0] == p:
                            for j in item:
                                #addin up pay not working
                                z = j * int(i["Pay amount"])
                                total_pay.append(z)
            data1.append({"Employee number":i["Employee number"], "Total pay": str(sum(total_pay))})
            with open('dataFile.json', 'w') as outfile:
                json.dump(data1, outfile)

t = time_commissions("data.json")
t.hourly()
