#print all first name and last name.

import json
fp=open('user.json')
datas=json.load(fp)
print(datas) #it will show data prsent in json

for data in datas:
    print(data['first_name'],data['gender'])                   #it will print first_name in data
   #print(data['first_name'].upper())           #it will print all characters are in upper case
   #print(data['first_name'].lower())            #it will print all characters are in lower case
    


