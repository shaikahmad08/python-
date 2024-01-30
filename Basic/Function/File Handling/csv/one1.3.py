#print only male employee in user_data

import csv
fp=open('one.csv','r')
user_data=list(csv.reader(fp))

 # Assuming 'gender' is the four column 
gender_index=3

for user in user_data:
    if user[gender_index]=='Male':
        print(user)



i=0
while i<=len(user_data)-1:
    if user_data[i][gender_index]=='Female':
        print(user_data[i])
    i=i+1

