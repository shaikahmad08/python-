                           #set-- indexing and slicing are not possible
s={}
print(type(s))

s={10}
print(type(s))
print(s)

s={10,20,30,30,40,50}
print(s)

s={10,20,30,30,40,50}
for s1 in s:
    print(s1)

s={10,20,30,30,"sk","true",(0,10.5)}
print(s)

s1={99,199,299,399,499}
s2={399,499,599,699,700}
print(s1 | s2)   #union
print(s1 & s2)   #intersection
print(s1 - s2)   #difference
print(s1 ^ s2)   #symmetric_difference

#using CRUD operation

#update operation
s={100,200,300,400,500}

s.add(99)
print(s)

s.update([299])
print(s)

s.copy()
print(s)

#delete operation
s={100,200,300,400,500}
s.pop()
print(s)

s.remove(500)
print(s)

s.discard(800)
print(s)

s.clear()
print(s)



