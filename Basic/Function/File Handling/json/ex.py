import json
fp=open('user.json','r')
datas=json.load(fp)
#print(datas)
for data in datas:
    if data['gender'] in ['Male','Female']:
        print(data['last_name'],data['gender'])

