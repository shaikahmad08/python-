import csv
fp=open('one.csv','r')
empl=list(csv.reader(fp)) #convert into list 
print(type(empl))
print(empl)

#using for loop
import csv
fp=open('one.csv','r')
empl=list(csv.reader(fp)) #convert into list 

for emp in empl:
    print(emp)

fp.close()


#using while loop
import csv
fp=open('one.csv','r')
empl=list(csv.reader(fp)) #convert into list 
 
i=0
while i<=len(empl)-1:
    print(empl[i])
    i=i+1
    
fp.close()
