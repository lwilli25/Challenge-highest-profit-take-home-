import csv
file = open (r'C:\Users\XXXXX\Documents\personal\python\data2.csv')
reader = csv.reader(file)
lines = len(list(reader))
print(lines-1)

import json
y=json.dumps(file)
print (y)

