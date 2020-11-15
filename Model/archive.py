import json

'''
IGNORE
'''

def archive(file):
    with open("prev_period.json") as arc:
        x = json.load(arc)
        with open(file, 'w') as y:
            json.dump(x, y)


archive("1.json")
