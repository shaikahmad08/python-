#number len in one.csv
import csv
fp=open('one.csv','r')
data=csv.reader(fp)

user_list=list(data)
print(len(user_list)-1)
fp.close()