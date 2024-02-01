import csv
fp=open('one.csv','r')
datas=list(csv.reader(fp))

gender_index=3

for data in datas:
        print(data[1:3])