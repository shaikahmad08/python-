#print only id in "one.csv"
import csv
fp=open('one.csv','r')
user_emp=list(csv.reader(fp))

#using for loop to print all id in one.csv

for user in user_emp:
    print(user[0])               #display only id
                       

#using while loop to print all id 

i=0
while i<=len(user_emp)-1:
    print(user_emp[i][0])                     #display only id
    i=i+1
    
#using sliceing 
    
for user in user_emp:
    print(user[0:4])