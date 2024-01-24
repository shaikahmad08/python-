emp_details=[
    {"id":1,"first_name":"Constantine","gender":"Male"},
    {"id":2,"first_name":"Julio","gender":"Male"},
    {"id":3,"first_name":"Paxon","gender":"Male"},
    {"id":4,"first_name":"Brent","gender":"Male"},
    {"id":5,"first_name":"Vachel","gender":"Male"}
]
# using lambda
emps_details = lambda emp_details: (emp_details, emp_details)
result = emps_details(emp_details)
print(result)

#using lambda with a map
emps_details=list(map(lambda emp_details:emp_details['first_name'],emp_details))
print(emps_details)  

#using set with lambda in a map 
emps_details=set(map(lambda emp_details:emp_details['first_name'],emp_details))
print(emps_details)  


#using for loop
for emp_details in emp_details:
    print(emp_details['gender'])

#using while loop
i=0
while i<=len(emp_details)-1:
    print(emp_details[i])
    i=i+1

