import csv
fp=open('one.csv','r')
empl=list(csv.reader(fp))

for emp in empl:
    for user in emp:
        print(user)                #display line by line
fp.close()



import csv 
fp=open('one.csv','r')
empl=list(csv.reader(fp))

for emp in empl:
    for data in emp:
        print(data,'\t',end='')      #display all at a time
    print()
fp.close()
