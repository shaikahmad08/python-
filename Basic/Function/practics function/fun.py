employees=[
    {"id":1,"first_name":"Constantine","gender":"Female"},
    {"id":2,"first_name":"Julio","gender":"Female"},
    {"id":3,"first_name":"Paxon","gender":"Male"},
    {"id":4,"first_name":"Brent","gender":"Male"},
    {"id":5,"first_name":"Vachel","gender":"Male"}
]
def func(emp):
     if(emp)['gender']=='Male':
        return True
     else:
        return False
x=filter(func,employees)
print(list(x))