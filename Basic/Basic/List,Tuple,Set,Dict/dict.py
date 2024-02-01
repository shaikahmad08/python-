        #Dict--key,value pair
# d={}
# print(type(d))
# 
# d={
#  'id':101,
# 'name':'sk',
# 'place':'nlr'
# }
# print(d)

#using crud operation

                #create
d1={
    'id':102,
    'name':'shaik',
    'movie':'salaar',
    'loc':['nellore','bangalore']
   }
                #read
print(d1)
print(d1.get('id'))
print(d1.get('name'))
print(d1.get('loc'))
print(d1['loc'][1])

print(d1.keys())
print(d1.values())
print(d1.items())

for key in d1.keys():
    print(key)

for value in d1.values():
    print(value)
        
for key,value in d1.items():
    print(key,":",value)
    
                #update

d1['email']='shaik@gmail.com'  ##updating email in d1 
print(d1)

               #delete
d1.popitem()   #del romdom present in the dict list(key,value)
print(d1)

d1.pop("id")  #add element to pop
print(d1)

del d1['name']
print(d1)

del d1['loc']
print(d1)
