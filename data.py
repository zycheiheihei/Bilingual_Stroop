import csv
import json
import os

files = os.listdir('result')

header = ['subject','chinese_match','chinese_opposite','chinese_meaningless','english_match','english_opposite','english_meaningless']
rows = []

cnt = 0
for file in files:
    if '.json' not in file:
        continue
    row = [file.split('.')[0]]
    f = open('result/'+file,'r')
    data = json.load(f)

    for s in data.keys():
        for t in data[s].keys():
            print(s,t)
            row.append(data[s][t])

    rows.append(row)

with open('result/total.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    f_csv.writerows(rows)