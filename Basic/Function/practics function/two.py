employees=[
    {"id":1,"first_name":"Constantine","gender":"Female"},
    {"id":2,"first_name":"Julio","gender":"Female"},
    {"id":3,"first_name":"Paxon","gender":"Male"},
    {"id":4,"first_name":"Brent","gender":"Male"},
    {"id":5,"first_name":"Vachel","gender":"Male"}
]
#print only male with lambda
emp=list(filter(lambda employees : employees['gender'] == 'Male', employees))
print(emp)

#print only male emp with lambda using filter


# for loop 
for employee in employees:
    #  print(employee['gender'])
    #  print(employee["gender"]=="Male")
     if(employee['gender']=='Male'):
        #print(employee)
        print(employee['first_name'])

#while loop
i=0
while i<=len(employees)-1:
    print(employees[i]['gender']=='Male')
    i=i+1
