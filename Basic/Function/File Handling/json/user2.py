import json
fp=open('user.json')
datas=json.load(fp)

#print only male user
for data in datas:
    if data['gender']=="Male":
        print(data['first_name'],data['last_name'],data['gender'])

#print only female user
for data in datas:
    if data['gender']=='Female':
        print(data['first_name'],data['last_name'],data['gender'])

#print without male and female
for data in datas:
    if data['gender']!='Male'and data['gender']!='Female':
        print(data['first_name'],data['last_name'],data['gender'])

